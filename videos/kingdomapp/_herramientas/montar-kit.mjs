// Monta el kit de identidad de Kingdom (../_identidad) en <proyecto>/identidad/, desde la carpeta del proyecto:
//   node ../_herramientas/montar-kit.mjs
// Copia exacta del kit (se rehace en cada corrida y nunca se edita en el proyecto), comprueba que el favicon siga siendo el de la app
// (KingdomApp/frontend-v2/public/favicon.svg), deja el sonido de marca en identidad/audio/sonido-marca.wav a la sonoridad del kit y, desde
// la v1.1, los sonidos de acción en identidad/audio/<nombre>.wav con su nivel de mezcla (kit.json → sonidosAccion).
// Lo usan los tres tipos (Wiki, Comercial y Corto); la herramienta de tutoriales de la wiki lo llamará al preparar cada idioma.
import { spawnSync } from 'node:child_process';
import crypto from 'node:crypto';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const PROYECTO = process.cwd();
const HERRAMIENTAS = path.dirname(fileURLToPath(import.meta.url));
const KIT = path.resolve(HERRAMIENTAS, '..', '_identidad');
const KINGDOM = path.resolve(process.env.KINGDOMAPP_REPO ?? path.join(HERRAMIENTAS, '..', '..', '..', '..', 'KingdomApp'));

const sha = b => crypto.createHash('sha256').update(b).digest('hex');

function correr(cmd, argumentos) {
  const r = spawnSync(cmd, argumentos, { encoding: 'utf8', maxBuffer: 1 << 26 });
  if (r.status !== 0) throw new Error(`${cmd} ${argumentos.slice(0, 4).join(' ')}…: ${(r.stderr || r.error?.message || '').slice(-600)}`);
  return r;
}

/** Sonoridad a `lufs` con loudnorm en dos pasadas (lineal: no cambia la dinámica). */
function normalizar(entrada, salida, lufs) {
  const m = correr('ffmpeg', ['-hide_banner', '-i', entrada, '-af', `loudnorm=I=${lufs}:TP=-1.5:LRA=11:print_format=json`, '-f', 'null', '-']);
  const desde = m.stderr.lastIndexOf('{');
  const j = JSON.parse(m.stderr.slice(desde, m.stderr.indexOf('}', desde) + 1));
  if (!Number.isFinite(Number(j.input_i))) throw new Error(`no pude medir la sonoridad de ${entrada}`);
  correr('ffmpeg', ['-hide_banner', '-loglevel', 'error', '-y', '-i', entrada, '-af',
    `loudnorm=I=${lufs}:TP=-1.5:LRA=11:measured_I=${j.input_i}:measured_TP=${j.input_tp}:measured_LRA=${j.input_lra}:` +
    `measured_thresh=${j.input_thresh}:offset=${j.target_offset}:linear=true`, '-ar', '48000', salida]);
}

export async function montarKit(proyecto = PROYECTO) {
  if (path.resolve(proyecto) === path.resolve(KIT, '..') || path.resolve(proyecto) === KIT) {
    throw new Error('corre montar-kit desde la carpeta de un proyecto de video, no desde videos/kingdomapp');
  }
  const kit = JSON.parse(fs.readFileSync(path.join(KIT, 'kit.json'), 'utf8'));
  const favicon = fs.readFileSync(path.join(KIT, 'favicon.svg'));
  if (sha(favicon) !== kit.favicon.sha256) throw new Error('_identidad/favicon.svg no coincide con la huella del kit');
  const oficial = path.join(KINGDOM, 'frontend-v2', 'public', 'favicon.svg');
  if (fs.existsSync(oficial) && sha(fs.readFileSync(oficial)) !== kit.favicon.sha256) {
    throw new Error('el favicon de la app cambió: el kit de identidad debe actualizarse (decisión del dueño, docs/videos/identidad.md)');
  }

  const destino = path.join(proyecto, 'identidad');
  const audio = path.join(destino, 'audio');
  const sonidoWav = path.join(audio, 'sonido-marca.wav');
  const marcaVersion = path.join(audio, 'version.txt');
  const conservar = fs.existsSync(sonidoWav) && fs.existsSync(marcaVersion) &&
    fs.readFileSync(marcaVersion, 'utf8').trim() === kit.sonido.sha256 ? fs.readFileSync(sonidoWav) : null;
  fs.rmSync(destino, { recursive: true, force: true });
  for (const f of kit.archivos) fs.cpSync(path.join(KIT, f), path.join(destino, f));
  for (const d of ['fuentes', 'iconos']) fs.cpSync(path.join(KIT, d), path.join(destino, d), { recursive: true });
  fs.mkdirSync(audio, { recursive: true });

  if (conservar) fs.writeFileSync(sonidoWav, conservar);
  else {
    // El sonido de marca no vive en git ni en un bucket: lo genera el código del kit, siempre igual.
    const { generarSonidoMarca } = await import(pathToFileURL(path.join(KIT, 'sonido-marca.mjs')).href);
    const crudo = generarSonidoMarca(kit.sonido.receta);
    if (sha(crudo) !== kit.sonido.sha256) {
      console.warn(`  ⚠ el sonido de marca generado (${sha(crudo).slice(0, 8)}…) no coincide con kit.json (${kit.sonido.sha256.slice(0, 8)}…). ` +
        'Si cambió sonido-marca.mjs, eso es cambiar el kit (sube la versión); si no, revisa la versión de Node.');
    }
    const tmp = path.join(audio, 'sonido-marca-crudo.wav');
    fs.writeFileSync(tmp, crudo);
    normalizar(tmp, sonidoWav, kit.sonido.lufs);
    fs.rmSync(tmp);
    fs.writeFileSync(marcaVersion, kit.sonido.sha256 + '\n');
  }

  // Sonidos de acción (v1.1): se generan en cada montaje (milisegundos de cálculo, sin FFmpeg). La huella se comprueba sobre el crudo
  // (pico a −3 dBFS) y el archivo montado lleva el pico en `nivel` dBFS, el que lo deja por debajo de la música a −18 LUFS.
  const accion = kit.sonidosAccion;
  if (accion) {
    const { generarSonidoAccion } = await import(pathToFileURL(path.join(KIT, accion.archivo)).href);
    for (const [nombre, d] of Object.entries(accion.sonidos)) {
      const crudo = generarSonidoAccion(nombre);
      if (sha(crudo) !== d.sha256) {
        console.warn(`  ⚠ el sonido de acción «${nombre}» generado (${sha(crudo).slice(0, 8)}…) no coincide con kit.json (${d.sha256.slice(0, 8)}…). ` +
          'Si cambió sonidos-accion.mjs, eso es cambiar el kit (sube la versión); si no, revisa la versión de Node.');
      }
      fs.writeFileSync(path.join(audio, `${nombre}.wav`), generarSonidoAccion(nombre, d.nivel));
    }
  }

  console.log(`Kit de identidad de Kingdom ${kit.version} montado en identidad/.`);
  console.log('Sonido de marca (identidad/audio/sonido-marca.wav) en el host, en estos segundos desde el inicio de cada pieza:');
  for (const [pieza, d] of Object.entries(kit.piezas)) {
    const variantes = d.variantes ? '  ' + Object.entries(d.variantes).map(([k, x]) => `${k}: ${x.duracion} s, sonido ${x.sonido} s`).join(' · ') : '';
    console.log(`  ${pieza.padEnd(17)} ${d.ancho}×${d.alto}  ${d.duracion} s  sonido ${d.sonido} s${variantes}`);
  }
  if (accion) {
    console.log(`Sonidos de acción (identidad/audio/<nombre>.wav, data-volume="1" con la música a ${accion.mezcla.musica} LUFS; ` +
      'data-start = momento visible + 0,033 − acento):');
    for (const [nombre, d] of Object.entries(accion.sonidos)) {
      console.log(`  ${nombre.padEnd(13)} ${String(d.duracion).padEnd(5)} s  acento ${String(d.acento).padEnd(4)} s  pico ${d.nivel} dBFS`);
    }
  }
  const pistas = Object.entries(kit.musica?.biblioteca ?? {});
  if (pistas.length) {
    console.log(`Música (se copia de ../_identidad/musica/ a assets/musica/; data-volume para ${kit.musica.lufs} LUFS sin voz):`);
    for (const [id, p] of pistas) console.log(`  ${id.padEnd(17)} volumen ${p.volumen}  ${p.uso ?? 'sin uso por ahora'}`);
  }
  return kit;
}

if (process.argv[1] && path.resolve(process.argv[1]).toLowerCase() === fileURLToPath(import.meta.url).toLowerCase()) {
  montarKit().catch(e => {
    console.error(`montar-kit: ${e.message}`);
    process.exit(1);
  });
}
