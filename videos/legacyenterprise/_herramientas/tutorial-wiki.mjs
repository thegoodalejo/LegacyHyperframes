// Tutorial narrado del Tipo Wiki de LegacyEnterprise (LegacyEnterprise docs/videos/ y docs/ayuda/videos.md), desde la carpeta del proyecto:
//   node ../_herramientas/tutorial-wiki.mjs preparar --idioma es|en   monta el kit, voz, escenas, index.html, subtítulos (VTT) y SCRIPT.md
//   npx --yes hyperframes@0.8.62 check · snapshot · render --quality high --output renders/tutorial-<idioma>.mp4
//   node ../_herramientas/tutorial-wiki.mjs entregar --idioma es|en   póster + copia a LegacyEnterprise/tools/ayuda/salida/tutorial/…
// El proyecto solo tiene su guion.mjs (y BRIEF.md, STORYBOARD.md). Todo lo demás se genera: la grabación REAL de la app (tools/ayuda, modo
// video), la voz Kokoro fijada (una frase por archivo, en caché por texto), la intro y el cierre del kit (_identidad, montado en identidad/
// sin editarlo). La duración de cada escena la manda lo que dura su tramo de la grabación o su voz, lo que sea mayor (se congela el último
// cuadro mientras la voz termina).
import { spawnSync } from 'node:child_process';
import crypto from 'node:crypto';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const HF = '0.8.62';
const CPS = 30;
const PROYECTO = process.cwd();
const HERRAMIENTAS = path.dirname(fileURLToPath(import.meta.url));
const KIT = path.resolve(HERRAMIENTAS, '..', '_identidad');
const LE = path.resolve(process.env.LEGACYENTERPRISE_REPO ?? path.join(HERRAMIENTAS, '..', '..', '..', '..', 'LegacyEnterprise'));
const PYTHON = process.env.HYPERFRAMES_PYTHON ?? path.resolve(HERRAMIENTAS, '..', '..', '..', '.venv-tts', 'Scripts', 'python.exe');

// Escenario: la grabación (1920×1080) a 0,8 dentro del cuadro; arriba la llamada, abajo los subtítulos, sin tapar la app.
const PANTALLA = { x: 192, y: 72, w: 1536, h: 864 };
const MAX_SUBTITULO = 84;           // 2 líneas de ~42 caracteres (identidad.md → Texto en pantalla)
const INICIO_VOZ = 0.35, ENTRE_FRASES = 0.35, COLA = 0.8;

const args = process.argv.slice(2);
const COMANDO = args[0];
const IDIOMA = args[args.indexOf('--idioma') + 1];
if (!['preparar', 'entregar'].includes(COMANDO) || !['es', 'en'].includes(IDIOMA)) {
  console.error('Uso: node ../_herramientas/tutorial-wiki.mjs preparar|entregar --idioma es|en   (desde la carpeta del proyecto)');
  process.exit(1);
}

const sha = b => crypto.createHash('sha256').update(b).digest('hex');
const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
const attrJson = o => JSON.stringify(o).replace(/&/g, '&amp;').replace(/'/g, '&#39;');
const r3 = n => Math.round(n * 1000) / 1000;
const aCuadros = s => Math.ceil(s * CPS - 1e-6) / CPS;

function correr(cmd, argumentos, opciones = {}) {
  const r = spawnSync(cmd, argumentos, { encoding: 'utf8', maxBuffer: 1 << 26, ...opciones });
  if (r.status !== 0) throw new Error(`${cmd} ${argumentos.slice(0, 4).join(' ')}…: ${(r.stderr || r.error?.message || '').slice(-600)}`);
  return r;
}
const ffmpeg = a => correr('ffmpeg', ['-hide_banner', '-loglevel', 'error', '-y', ...a]);
function duracion(archivo) {
  const r = correr('ffprobe', ['-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', archivo]);
  return Number(r.stdout.trim());
}

/** Sonoridad a `lufs` con loudnorm en dos pasadas (lineal: no cambia la dinámica de la voz). */
function normalizar(entrada, salida, lufs) {
  const m = correr('ffmpeg', ['-hide_banner', '-i', entrada, '-af', `loudnorm=I=${lufs}:TP=-1.5:LRA=11:print_format=json`, '-f', 'null', '-']);
  const desde = m.stderr.lastIndexOf('{');
  const j = JSON.parse(m.stderr.slice(desde, m.stderr.indexOf('}', desde) + 1));
  if (!Number.isFinite(Number(j.input_i))) throw new Error(`no pude medir la sonoridad de ${entrada}`);
  ffmpeg(['-i', entrada, '-af', `loudnorm=I=${lufs}:TP=-1.5:LRA=11:measured_I=${j.input_i}:measured_TP=${j.input_tp}:` +
    `measured_LRA=${j.input_lra}:measured_thresh=${j.input_thresh}:offset=${j.target_offset}:linear=true`, '-ar', '48000', salida]);
}

// ─── 1. Kit de identidad montado en identidad/ (copia exacta; se rehace en cada corrida, nunca se edita aquí) ──────────────
async function montarKit() {
  const kit = JSON.parse(fs.readFileSync(path.join(KIT, 'kit.json'), 'utf8'));
  const favicon = fs.readFileSync(path.join(KIT, 'favicon.svg'));
  if (sha(favicon) !== kit.favicon_sha256) throw new Error('_identidad/favicon.svg no coincide con la huella del kit');
  const oficial = path.join(LE, 'frontend', 'public', 'favicon.svg');
  if (fs.existsSync(oficial) && sha(fs.readFileSync(oficial)) !== kit.favicon_sha256) {
    throw new Error('el favicon de la app cambió: el kit de identidad debe actualizarse (decisión del dueño, identidad.md)');
  }
  const destino = path.join(PROYECTO, 'identidad');
  const audio = path.join(destino, 'audio');
  const sonidoWav = path.join(audio, 'sonido-marca.wav');
  const conservar = fs.existsSync(sonidoWav) ? fs.readFileSync(sonidoWav) : null;
  fs.rmSync(destino, { recursive: true, force: true });
  for (const f of ['intro-wiki.html', 'cierre-wiki.html', 'kit.json', 'favicon.svg', 'logo.svg']) fs.cpSync(path.join(KIT, f), path.join(destino, f));
  for (const d of ['fuentes', 'iconos']) fs.cpSync(path.join(KIT, d), path.join(destino, d), { recursive: true });
  fs.mkdirSync(audio, { recursive: true });
  if (conservar) fs.writeFileSync(sonidoWav, conservar);
  else {
    // El sonido de marca vive en el bucket (no en git): se baja, se comprueba su huella y se deja a la sonoridad del kit.
    const r = await fetch(`${kit.bucket_publico}/${kit.sonido.clave}`);
    if (!r.ok) throw new Error(`sonido de marca: ${r.status}`);
    const ogg = Buffer.from(await r.arrayBuffer());
    if (sha(ogg) !== kit.sonido.sha256) throw new Error('el sonido de marca del bucket no coincide con su huella');
    const tmp = path.join(audio, 'sonido-marca.ogg');
    fs.writeFileSync(tmp, ogg);
    normalizar(tmp, sonidoWav, kit.sonido.lufs);
    fs.rmSync(tmp);
  }
  return kit;
}

// ─── 2. Grabación real de la app (LegacyEnterprise/tools/ayuda, modo video) ────────────────────────────────────────────────
function traerGrabacion(articulo) {
  const origen = path.join(LE, 'tools', 'ayuda', 'salida', 'video', IDIOMA, articulo);
  const archivos = ['grabacion.mp4', 'pasos.json'].map(f => path.join(origen, f));
  for (const f of archivos) {
    if (!fs.existsSync(f)) throw new Error(`falta ${f}: corre en LegacyEnterprise/tools/ayuda: node capturar.mjs ${articulo} --idioma ${IDIOMA} --modo video`);
  }
  const dir = path.join(PROYECTO, 'assets', 'captura', IDIOMA);
  fs.mkdirSync(dir, { recursive: true });
  fs.copyFileSync(archivos[0], path.join(dir, 'grabacion.mp4'));
  const pasos = JSON.parse(fs.readFileSync(archivos[1], 'utf8'));
  fs.writeFileSync(path.join(dir, 'pasos.json'), JSON.stringify(pasos, null, 1));
  return { grabacion: path.join(dir, 'grabacion.mp4'), pasos };
}

// ─── 3. Voz: una frase por archivo, en caché por (voz, velocidad, texto) ──────────────────────────────────────────────────
const textoVoz = f => (f.voz?.[IDIOMA] ?? f[IDIOMA]).replace(/[«»"“”]/g, '').replace(/\s+/g, ' ').trim();
function voz(frase, kit) {
  const { voz: v, velocidad } = kit.voz[IDIOMA];
  const texto = textoVoz(frase);
  const dir = path.join(PROYECTO, 'assets', 'voice', IDIOMA);
  fs.mkdirSync(dir, { recursive: true });
  const nombre = sha(`${v}|${velocidad}|${kit.voz.lufs}|${texto}`).slice(0, 12);
  const wav = path.join(dir, `${nombre}.wav`);
  if (!fs.existsSync(wav)) {
    const txt = path.join(dir, `${nombre}.txt`), crudo = path.join(dir, `${nombre}-crudo.wav`);
    fs.writeFileSync(txt, texto);
    correr('npx', ['--yes', `hyperframes@${HF}`, 'tts', txt, '-v', v, '-s', String(velocidad), '-o', crudo],
      { env: { ...process.env, HYPERFRAMES_PYTHON: PYTHON }, shell: process.platform === 'win32' });
    normalizar(crudo, wav, kit.voz.lufs);
    fs.rmSync(crudo);
    fs.rmSync(txt);
    console.log(`  voz nueva  ${path.basename(wav)}  ${texto.slice(0, 70)}`);
  }
  return { archivo: `assets/voice/${IDIOMA}/${nombre}.wav`, duracion: duracion(wav) };
}

/** Parte un subtítulo largo en dos, por la coma o el espacio más cercano a la mitad. */
function partir(texto) {
  if (texto.length <= MAX_SUBTITULO) return [texto];
  const mitad = texto.length / 2;
  // Puntaje = distancia a la mitad; cortar en una coma no suma, antes de «y/o/and…» suma 6, en cualquier otro espacio suma 12.
  let mejor = -1, puntaje = Infinity;
  for (const m of texto.matchAll(/, | (?:y|e|o|and|or|but|pero) | /g)) {
    const coma = m[0].startsWith(',');
    const corte = coma ? m.index + 1 : m.index;
    const p = Math.abs(corte - mitad) + (coma ? 0 : m[0].length > 1 ? 6 : 12);
    if (p < puntaje) { puntaje = p; mejor = corte; }
  }
  return [texto.slice(0, mejor).trim(), texto.slice(mejor).trim()].flatMap(partir);
}

const vttHora = s => {
  const ms = Math.round(s * 1000);
  const h = Math.floor(ms / 3600000), m = Math.floor(ms / 60000) % 60, seg = Math.floor(ms / 1000) % 60;
  return `${String(h).padStart(2, '0')}:${String(m).padStart(2, '0')}:${String(seg).padStart(2, '0')}.${String(ms % 1000).padStart(3, '0')}`;
};

// ─── preparar ──────────────────────────────────────────────────────────────────────────────────────────────────────────────
async function preparar() {
  const guion = (await import(pathToFileURL(path.join(PROYECTO, 'guion.mjs')).href)).default;
  const kit = await montarKit();
  const { grabacion, pasos } = traerGrabacion(guion.articulo);
  const P = pasos.pasos;
  const inicioTramo = t => { const p = P.find(x => x.tramo === t); if (!p) throw new Error(`pasos.json no tiene el tramo «${t}»`); return p; };

  const intro = kit.intro.duracion;
  const conSiguiente = !!guion.siguiente?.[IDIOMA];
  const cierre = conSiguiente ? kit.cierre : { ...kit.cierre, ...kit.cierre.sinSiguiente };
  let t = intro;
  const escenas = [];
  for (const [i, e] of guion.escenas.entries()) {
    const ini = inicioTramo(e.tramo);
    const sig = guion.escenas[i + 1] ? inicioTramo(guion.escenas[i + 1].tramo).inicio : P.at(-1).fin;
    const tramo = (sig - ini.inicio) / 1000;
    let cursor = INICIO_VOZ;
    const frases = e.frases.map((f, j) => {
      const a = voz(f, kit);
      const ancla = f.desde !== undefined ? (P[f.desde].inicio - ini.inicio) / 1000 : 0;
      const desde = Math.max(cursor, ancla);
      cursor = desde + a.duracion + ENTRE_FRASES;
      return { ...a, id: `voz-${String(i + 1).padStart(2, '0')}-${j + 1}`, texto: f[IDIOMA], desde };
    });
    const dur = aCuadros(Math.max(tramo, cursor - ENTRE_FRASES + COLA));
    escenas.push({ n: i + 1, tramo: e.tramo, desdeGrabacion: ini.inicio / 1000, tramoDur: tramo, dur, inicio: t, frases, llamada: e.llamada?.[IDIOMA] });
    t = r3(t + dur);
  }
  const total = r3(t + cierre.duracion);

  // Escenas: el tramo de la grabación y, si la voz dura más, el último cuadro congelado.
  const dirEsc = path.join(PROYECTO, 'assets', 'captura', IDIOMA);
  for (const e of escenas) {
    const segmento = Math.min(e.tramoDur, e.dur);
    const congelar = r3(e.dur - segmento);
    // -ss y -t antes de -i: limitan lo que se LEE (como opciones de salida, -t cortaría también el cuadro congelado).
    ffmpeg(['-ss', e.desdeGrabacion.toFixed(3), '-t', segmento.toFixed(3), '-i', grabacion,
      '-vf', `fps=${CPS}${congelar > 0 ? `,tpad=stop_mode=clone:stop_duration=${congelar}` : ''}`,
      '-c:v', 'libx264', '-preset', 'slow', '-crf', '16', '-pix_fmt', 'yuv420p', '-an', '-movflags', '+faststart',
      path.join(dirEsc, `escena-${String(e.n).padStart(2, '0')}.mp4`)]);
  }

  // Subtítulos: uno por frase (partido si pasa de 2 líneas), del inicio de su voz al inicio de la siguiente.
  const subtitulos = [];
  for (const e of escenas) {
    e.frases.forEach((f, j) => {
      const inicio = e.inicio + f.desde;
      const fin = j + 1 < e.frases.length ? e.inicio + e.frases[j + 1].desde - 0.05 : e.inicio + Math.min(e.dur, f.desde + f.duracion + 0.6);
      const partes = partir(f.texto);
      const largo = partes.reduce((s, p) => s + p.length, 0);
      let c = inicio;
      for (const p of partes) {
        const d = (fin - inicio) * (p.length / largo);
        subtitulos.push({ inicio: r3(c), fin: r3(c + d), texto: p });
        c += d;
      }
    });
  }

  // index.html (se genera por idioma; no va a git)
  const cierreInicio = r3(total - cierre.duracion);
  const h = [];
  h.push(`<!doctype html>
<html lang="${IDIOMA}">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1920, height=1080" />
    <title>${esc(guion.titulo[IDIOMA])} — Ayuda de LegacyEnterprise (${IDIOMA})</title>
    <!-- GENERADO por _herramientas/tutorial-wiki.mjs desde guion.mjs: no editar a mano. -->
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
    <link rel="stylesheet" href="identidad/fuentes/inter.css" />
    <style>
      html, body { margin: 0; width: 1920px; height: 1080px; overflow: hidden; background: #fbf8fd; }
      #root { position: relative; width: 1920px; height: 1080px; overflow: hidden; background: #fbf8fd; font-family: 'Inter', sans-serif; }
      #root > div[data-composition-src] { position: absolute; inset: 0; }
      #escenario { position: absolute; inset: 0; background: #eceaf1; }
      .pantalla { position: absolute; left: ${PANTALLA.x}px; top: ${PANTALLA.y}px; width: ${PANTALLA.w}px; height: ${PANTALLA.h}px;
        border-radius: 16px; box-shadow: 0 0 0 1px #c7c5d0, 0 10px 32px rgba(27, 27, 31, 0.12); background: #fbf8fd; }
      .llamada { position: absolute; left: ${PANTALLA.x}px; top: 14px; height: 46px; }
      .llamada span { display: flex; align-items: center; height: 46px; padding: 0 22px; border-radius: 999px; background: #4555b7;
        color: #ffffff; font-size: 30px; font-weight: 600; line-height: 1; }
      .subtitulo { position: absolute; left: 96px; right: 96px; bottom: 14px; display: flex; justify-content: center; }
      .subtitulo span { max-width: 1728px; padding: 10px 26px; border-radius: 12px; background: rgba(27, 27, 31, 0.8); color: #ffffff;
        font-size: 40px; font-weight: 500; line-height: 1.3; text-align: center; }
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="root" data-start="0" data-width="1920" data-height="1080" data-duration="${total}">
      <div id="intro-wiki" data-composition-id="intro-wiki" data-composition-src="identidad/intro-wiki.html"
        data-variable-values='${attrJson({ titulo: guion.titulo[IDIOMA], modulo: guion.modulo, idioma: IDIOMA })}'
        data-start="0" data-duration="${intro}" data-track-index="1" data-width="1920" data-height="1080"></div>
      <div id="escenario" class="clip" data-start="${intro}" data-duration="${r3(cierreInicio - intro)}" data-track-index="0"></div>`);
  for (const e of escenas) {
    const nn = String(e.n).padStart(2, '0');
    h.push(`      <video id="escena-${nn}" class="clip pantalla" src="assets/captura/${IDIOMA}/escena-${nn}.mp4" data-start="${e.inicio}" ` +
      `data-duration="${e.dur}" data-track-index="2" muted playsinline></video>`);
    if (e.llamada) {
      h.push(`      <div id="llamada-${nn}" class="clip llamada" data-start="${e.inicio}" data-duration="${e.dur}" data-track-index="3"><span id="llamada-${nn}-texto">${esc(e.llamada)}</span></div>`);
    }
  }
  subtitulos.forEach((s, i) => h.push(`      <div id="subtitulo-${String(i + 1).padStart(2, '0')}" class="clip subtitulo" data-start="${s.inicio}" ` +
    `data-duration="${r3(s.fin - s.inicio)}" data-track-index="4"><span>${esc(s.texto)}</span></div>`));
  for (const e of escenas) {
    for (const f of e.frases) {
      h.push(`      <audio id="${f.id}" src="${f.archivo}" data-start="${r3(e.inicio + f.desde)}" data-duration="${r3(f.duracion)}" ` +
        'data-track-index="10" data-volume="1"></audio>');
    }
  }
  h.push(`      <audio id="marca-intro" src="identidad/audio/sonido-marca.wav" data-start="${kit.intro.sonido}" data-duration="${kit.sonido.duracion}" data-track-index="11" data-volume="1"></audio>
      <audio id="marca-cierre" src="identidad/audio/sonido-marca.wav" data-start="${r3(cierreInicio + cierre.sonido)}" data-duration="${kit.sonido.duracion}" data-track-index="11" data-volume="1"></audio>
      <div id="cierre-wiki" data-composition-id="cierre-wiki" data-composition-src="identidad/cierre-wiki.html"
        data-variable-values='${attrJson({ siguiente: guion.siguiente?.[IDIOMA] ?? '', modulo: guion.modulo, idioma: IDIOMA })}'
        data-start="${cierreInicio}" data-duration="${cierre.duracion}" data-track-index="1" data-width="1920" data-height="1080"></div>
    </div>
    <script>
      const tl = gsap.timeline({ paused: true });
${escenas.filter(e => e.llamada).map(e => `      tl.fromTo('#llamada-${String(e.n).padStart(2, '0')}-texto', { y: -10, opacity: 0 }, { y: 0, opacity: 1, duration: 0.3, ease: 'power2.out' }, ${r3(e.inicio + 0.15)});`).join('\n')}
      tl.set({}, {}, ${total});
      window.__timelines['root'] = tl;
    </script>
  </body>
</html>
`);
  fs.writeFileSync(path.join(PROYECTO, 'index.html'), h.join('\n'));

  fs.mkdirSync(path.join(PROYECTO, 'renders'), { recursive: true });
  const vtt = ['WEBVTT', '', ...subtitulos.flatMap((s, i) => [String(i + 1), `${vttHora(s.inicio)} --> ${vttHora(s.fin)}`, s.texto, ''])].join('\n');
  fs.writeFileSync(path.join(PROYECTO, 'renders', `tutorial-${IDIOMA}.vtt`), vtt);
  fs.writeFileSync(path.join(PROYECTO, `tiempos-${IDIOMA}.json`), JSON.stringify({ total, intro, cierre: { inicio: cierreInicio, ...cierre },
    escenas: escenas.map(({ frases, ...e }) => ({ ...e, frases: frases.map(f => ({ id: f.id, desde: r3(f.desde), duracion: r3(f.duracion), texto: f.texto })) })) }, null, 1));
  escribirScript(guion);

  const cuerpo = r3(cierreInicio - intro);
  console.log(`✓ ${guion.articulo} (${IDIOMA}): ${escenas.length} escenas, ${subtitulos.length} subtítulos, cuerpo ${cuerpo} s + intro ${intro} s + cierre ${cierre.duracion} s = ${total} s`);
  for (const e of escenas) {
    const voz = e.frases.at(-1).desde + e.frases.at(-1).duracion;
    console.log(`  ${String(e.n).padStart(2, '0')} ${e.tramo.padEnd(10)} ${e.inicio.toFixed(2).padStart(6)} s  dura ${e.dur.toFixed(2)} s (tramo ${e.tramoDur.toFixed(2)}, voz ${voz.toFixed(2)})`);
  }
  if (cuerpo < 60 || cuerpo > 240) console.warn(`  aviso: el cuerpo dura ${cuerpo} s (la wiki pide 1–4 min de contenido para un tutorial)`);
}

function escribirScript(guion) {
  const l = ['# SCRIPT — narración bloqueada', '', `<!-- GENERADO desde guion.mjs por _herramientas/tutorial-wiki.mjs: se edita guion.mjs. -->`, '',
    `Artículo: \`${guion.articulo}\` · Módulo: ${guion.modulo}`, ''];
  for (const idioma of ['es', 'en']) {
    l.push(`## ${idioma === 'es' ? 'Español' : 'English'} — «${guion.titulo[idioma]}»`, '');
    guion.escenas.forEach((e, i) => {
      l.push(`### ${i + 1}. ${e.tramo}${e.llamada ? ` — llamada «${e.llamada[idioma]}»` : ''}`, '');
      for (const f of e.frases) l.push(`- ${f[idioma]}${f.desde !== undefined ? ` _(desde el paso ${f.desde})_` : ''}`);
      l.push('');
    });
  }
  fs.writeFileSync(path.join(PROYECTO, 'SCRIPT.md'), l.join('\n'));
}

// ─── entregar ──────────────────────────────────────────────────────────────────────────────────────────────────────────────
async function entregar() {
  const guion = (await import(pathToFileURL(path.join(PROYECTO, 'guion.mjs')).href)).default;
  const mp4 = path.join(PROYECTO, 'renders', `tutorial-${IDIOMA}.mp4`);
  const vtt = path.join(PROYECTO, 'renders', `tutorial-${IDIOMA}.vtt`);
  for (const f of [mp4, vtt]) if (!fs.existsSync(f)) throw new Error(`falta ${path.relative(PROYECTO, f)} (preparar y render primero)`);
  const tiempos = JSON.parse(fs.readFileSync(path.join(PROYECTO, `tiempos-${IDIOMA}.json`), 'utf8'));
  const d = duracion(mp4);
  if (Math.abs(d - tiempos.total) > 0.2) throw new Error(`el render dura ${d.toFixed(2)} s y la composición ${tiempos.total} s: vuelve a renderizar`);
  const destino = path.join(LE, 'tools', 'ayuda', 'salida', 'tutorial', IDIOMA, guion.articulo);
  fs.mkdirSync(destino, { recursive: true });
  // Sonoridad final a la del kit (el render mezcla con su propio objetivo): video copiado tal cual, audio en dos pasadas lineales.
  const kit = JSON.parse(fs.readFileSync(path.join(KIT, 'kit.json'), 'utf8'));
  const m = correr('ffmpeg', ['-hide_banner', '-i', mp4, '-af', `loudnorm=I=${kit.voz.lufs}:TP=-1.5:LRA=11:print_format=json`, '-vn', '-f', 'null', '-']);
  const i0 = m.stderr.lastIndexOf('{');
  const j = JSON.parse(m.stderr.slice(i0, m.stderr.indexOf('}', i0) + 1));
  ffmpeg(['-i', mp4, '-map', '0', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '160k', '-af', `loudnorm=I=${kit.voz.lufs}:TP=-1.5:LRA=11:` +
    `measured_I=${j.input_i}:measured_TP=${j.input_tp}:measured_LRA=${j.input_lra}:measured_thresh=${j.input_thresh}:offset=${j.target_offset}:linear=true`,
  '-ar', '48000', '-movflags', '+faststart', path.join(destino, 'tutorial.mp4')]);
  fs.copyFileSync(vtt, path.join(destino, 'tutorial.vtt'));
  // Póster: el final de la intro (marca, módulo y título), lo que la persona ve antes de darle play.
  ffmpeg(['-ss', String(tiempos.intro - 0.25), '-i', path.join(destino, 'tutorial.mp4'), '-frames:v', '1', '-c:v', 'libwebp', '-quality', '85', path.join(destino, 'tutorial-poster.webp')]);
  console.log(`✓ tutorial ${IDIOMA} (${d.toFixed(1)} s) en ${path.relative(LE, destino)}: publícalo con node publicar.mjs ${guion.articulo}`);
}

(COMANDO === 'preparar' ? preparar() : entregar()).catch(e => { console.error(`✗ ${e.message}`); process.exit(1); });
