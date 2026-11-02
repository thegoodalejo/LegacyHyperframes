// Video del Tipo Recurso de Kingdom (decisión 239; KingdomApp docs/videos/README.md → «Tipo 5. Recurso»), desde la carpeta del proyecto:
//   node ../_herramientas/recurso.mjs preparar --idioma es   kit, voz Kokoro, línea de tiempo en la rejilla de la música, cama musical en
//                                                            bucle con la voz encima, tiempos-<idioma>.json, VTT, SCRIPT.md e index.html
//   npx --yes hyperframes@0.8.221 check                      (0 errores) · snapshot --at <las mitades que imprime preparar>
//   node ../_herramientas/recurso.mjs render --idioma es     render con los temporales en F: (renders/recurso-<idioma>.mp4) y su tiempo
//   node ../_herramientas/recurso.mjs entregar --idioma es   entrega/<idioma>/: video-1080.mp4, video-720.mp4, poster.jpg/.webp, video.vtt,
//                                                            ficha.json; verifica −16 LUFS integrados y pico ≤ −1,5 dBTP
// El proyecto tiene su guion.mjs (formato en ../README.md → «Tipo Recurso (v1.2)») y sus composiciones (compositions/<id>.html), que son
// motion design sin la app (excepción a la regla 1 de las directivas, decidida por el dueño) o, en la variante «Para líderes» (kit v1.3,
// decisión 241), la app v2 recreada en HTML con las piezas .k-app-* y KRecurso.app. Todo lo demás se genera: el kit (montar-kit.mjs,
// sin editarlo), la voz (una frase por archivo, en caché por texto), la música («Product Launch» encadenada en compases hasta cubrir el
// video y terminando en su final natural con el cierre), el host y los tiempos que cada escena lee con identidad/recurso.js.
// Viene de tutorial-wiki.mjs (voz, normalización en dos pasadas, VTT, entrega).
import { spawn, spawnSync } from 'node:child_process';
import crypto from 'node:crypto';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { montarKit } from './montar-kit.mjs';

// Una sola versión del CLI para el Tipo Recurso (tiene `tts`, `check`, `snapshot` y `render`; se comprueba en cada preparar).
export const HF = '0.8.221';
const CPS = 30;
const PULSO = 0.5;
const COMPAS = 2;
const SR = 48000;
const PROYECTO = process.cwd();
const HERRAMIENTAS = path.dirname(fileURLToPath(import.meta.url));
const KIT = path.resolve(HERRAMIENTAS, '..', '_identidad');
const PYTHON = process.env.HYPERFRAMES_PYTHON ?? path.resolve(HERRAMIENTAS, '..', '..', '..', '.venv-tts', 'Scripts', 'python.exe');

const MAX_SUBTITULO = 84; // 2 líneas de ~42 caracteres (docs/videos/identidad.md → Texto en pantalla)
const MAX_LINEA = 42;
// Valores por defecto de las escenas con voz (segundos): antes de la primera frase, entre frases y después de la última.
const ENTRADA = 0.5, PAUSA = 0.3, COLA = 0.8;
// Mezcla: la música baja bajo la voz con rampas suaves y sube en las escenas sin voz (huecos de más de UNIR s entre frases).
const BAJAR = 0.45, SUBIR = 1.2, UNIR = 3.0, ANTES_VOZ = 0.12, TRAS_VOZ = 0.35;

const args = process.argv.slice(2);
const COMANDO = args[0];
const IDIOMA = args.includes('--idioma') ? args[args.indexOf('--idioma') + 1] : 'es';
if (!['preparar', 'render', 'entregar'].includes(COMANDO) || !['es', 'en', 'pt'].includes(IDIOMA)) {
  console.error('Uso: node ../_herramientas/recurso.mjs preparar|render|entregar --idioma es|en|pt   (desde la carpeta del proyecto)');
  process.exit(1);
}

const sha = b => crypto.createHash('sha256').update(b).digest('hex');
const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
const attrJson = o => JSON.stringify(o).replace(/&/g, '&amp;').replace(/'/g, '&#39;');
const r3 = n => Math.round(n * 1000) / 1000;
const arriba = (x, paso) => r3(Math.ceil(x / paso - 1e-6) * paso);
const enRejilla = (x, paso, desfase = 0) => Math.abs((x - desfase) / paso - Math.round((x - desfase) / paso)) < 1e-4;
const loc = (v, campo = '') => {
  if (v === undefined || v === null) return undefined;
  if (typeof v === 'string' || typeof v === 'number' || typeof v === 'boolean') return v;
  if (typeof v === 'object' && (IDIOMA in v || 'es' in v)) {
    if (!(IDIOMA in v)) throw new Error(`falta la versión «${IDIOMA}» de ${campo || JSON.stringify(v).slice(0, 60)}`);
    return v[IDIOMA];
  }
  return v;
};

function correr(cmd, argumentos, opciones = {}) {
  const r = spawnSync(cmd, argumentos, { encoding: 'utf8', maxBuffer: 1 << 28, ...opciones });
  if (r.status !== 0) throw new Error(`${cmd} ${argumentos.slice(0, 5).join(' ')}…: ${(r.stderr || r.error?.message || '').toString().slice(-700)}`);
  return r;
}
const ffmpeg = a => correr('ffmpeg', ['-hide_banner', '-loglevel', 'error', '-y', ...a]);
const duracion = archivo => Number(correr('ffprobe', ['-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', archivo]).stdout.trim());

/** Sonoridad integrada y pico verdadero (loudnorm en modo medida). */
function medir(archivo, extra = []) {
  const m = correr('ffmpeg', ['-hide_banner', ...extra, '-i', archivo, '-vn', '-af', 'loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json', '-f', 'null', '-']);
  const i0 = m.stderr.lastIndexOf('{');
  const j = JSON.parse(m.stderr.slice(i0, m.stderr.indexOf('}', i0) + 1));
  return { I: Number(j.input_i), TP: Number(j.input_tp), LRA: Number(j.input_lra), j };
}

/** Sonoridad a `lufs` con loudnorm en dos pasadas (lineal: no cambia la dinámica). */
function normalizar(entrada, salida, lufs, tp = -1.5, extra = []) {
  const { j } = medir(entrada);
  if (!Number.isFinite(Number(j.input_i))) throw new Error(`no pude medir la sonoridad de ${entrada}`);
  ffmpeg(['-i', entrada, '-vn', '-af', `loudnorm=I=${lufs}:TP=${tp}:LRA=11:measured_I=${j.input_i}:measured_TP=${j.input_tp}:` +
    `measured_LRA=${j.input_lra}:measured_thresh=${j.input_thresh}:offset=${j.target_offset}:linear=true`, '-ar', String(SR), ...extra, salida]);
}

/** PCM en float32 intercalado a 48 kHz. */
function decodificar(archivo, canales) {
  const r = spawnSync('ffmpeg', ['-hide_banner', '-loglevel', 'error', '-i', archivo, '-f', 'f32le', '-ac', String(canales), '-ar', String(SR), '-'],
    { maxBuffer: 1 << 30 });
  if (r.status !== 0) throw new Error(`no pude decodificar ${archivo}: ${r.stderr?.toString().slice(-300)}`);
  const b = r.stdout;
  return new Float32Array(b.buffer.slice(b.byteOffset, b.byteOffset + b.length));
}

/** WAV PCM de 16 bits (sin tramado: siempre el mismo archivo para la misma entrada). */
function escribirWav(ruta, pcm, canales) {
  const datos = Buffer.alloc(pcm.length * 2);
  for (let i = 0; i < pcm.length; i++) datos.writeInt16LE(Math.max(-32768, Math.min(32767, Math.round(pcm[i] * 32767))), i * 2);
  const h = Buffer.alloc(44);
  h.write('RIFF', 0); h.writeUInt32LE(36 + datos.length, 4); h.write('WAVE', 8); h.write('fmt ', 12);
  h.writeUInt32LE(16, 16); h.writeUInt16LE(1, 20); h.writeUInt16LE(canales, 22); h.writeUInt32LE(SR, 24);
  h.writeUInt32LE(SR * canales * 2, 28); h.writeUInt16LE(canales * 2, 32); h.writeUInt16LE(16, 34); h.write('data', 36); h.writeUInt32LE(datos.length, 40);
  fs.mkdirSync(path.dirname(ruta), { recursive: true });
  fs.writeFileSync(ruta, Buffer.concat([h, datos]));
}

// ─── El CLI fijado ──────────────────────────────────────────────────────────────────────────────────────────────────────────
function verificarCli() {
  const r = spawnSync('npx', ['--yes', `hyperframes@${HF}`, 'tts', '--help'], { encoding: 'utf8', shell: process.platform === 'win32', maxBuffer: 1 << 24 });
  const salida = `${r.stdout}${r.stderr}`;
  if (r.status !== 0 || !salida.includes(`hyperframes tts v${HF}`) || !/Kokoro/i.test(salida)) {
    throw new Error(`hyperframes@${HF} no responde con «tts» (Kokoro): ${salida.slice(-300)}`);
  }
}

// ─── Voz: una frase por archivo, en caché por (voz, velocidad, sonoridad, texto) — la misma clave de tutorial-wiki.mjs ───────────
const textoVoz = f => String(loc(f.voz, 'voz') ?? f[IDIOMA]).replace(/[«»"“”*]/g, '').replace(/\s+/g, ' ').trim();
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
      // El Python va con barras normales: con barras invertidas el CLI no lo encuentra y cae al del sistema (sin kokoro-onnx).
      { env: { ...process.env, HYPERFRAMES_PYTHON: PYTHON.split(path.sep).join('/') }, shell: process.platform === 'win32' });
    normalizar(crudo, wav, kit.voz.lufs);
    fs.rmSync(crudo);
    fs.rmSync(txt);
    console.log(`  voz nueva  ${path.basename(wav)}  ${texto.slice(0, 70)}`);
  }
  return { wav, archivo: `assets/voice/${IDIOMA}/${nombre}.wav`, duracion: duracion(wav) };
}

/** Palabras con su tiempo estimado dentro de la frase: los grupos que separa la puntuación caen en los silencios más largos de la voz y,
 *  dentro de cada grupo, cada palabra dura según sus sílabas. Error típico ±0,15 s: sirve para que el texto aparezca con la voz. */
function palabrasEstimadas(wav, texto) {
  const pcm = decodificar(wav, 1);
  const N = 480; // 10 ms
  const db = [];
  for (let i = 0; i + N <= pcm.length; i += N) {
    let s = 0;
    for (let j = i; j < i + N; j++) s += pcm[j] * pcm[j];
    db.push(10 * Math.log10(s / N + 1e-12));
  }
  const tope = Math.max(...db);
  const habla = db.map(x => x > tope - 32);
  const a = habla.indexOf(true), b = habla.lastIndexOf(true) + 1;
  const silencios = [];
  for (let i = a, ini = -1; i < b; i++) {
    if (!habla[i] && ini < 0) ini = i;
    if (habla[i] && ini >= 0) {
      if (i - ini >= 12) silencios.push({ ini: ini / 100, fin: i / 100, largo: (i - ini) / 100 });
      ini = -1;
    }
  }
  // *así* en el texto de la frase marca palabras clave (clave: true): la composición puede iluminarlas; la voz y el VTT no llevan asteriscos.
  const crudas = String(texto).split(/\s+/).filter(w => w.replace(/\*/g, ''));
  const claves = [];
  let enClave = false;
  for (const w of crudas) {
    if (w.startsWith('*')) enClave = true;
    claves.push(enClave);
    if (w.length > 1 && /\*[.,;:!?…»"”)]*$/.test(w)) enClave = false;
  }
  const palabras = crudas.map(w => w.replace(/\*/g, ''));
  const grupos = [[]];
  palabras.forEach((w, i) => {
    grupos.at(-1).push(w);
    if (/[,;:.?!…]["»”)]*$/.test(w) && i < palabras.length - 1) grupos.push([]);
  });
  let tramos;
  if (grupos.length > 1 && silencios.length >= grupos.length - 1) {
    const cortes = [...silencios].sort((x, y) => y.largo - x.largo).slice(0, grupos.length - 1).sort((x, y) => x.ini - y.ini);
    tramos = grupos.map((g, k) => ({ g, ini: k === 0 ? a / 100 : cortes[k - 1].fin, fin: k === grupos.length - 1 ? b / 100 : cortes[k].ini }));
  } else tramos = [{ g: palabras, ini: a / 100, fin: b / 100 }];
  const silabas = w => Math.max(1, (w.toLowerCase().match(/[aeiouáéíóúüy]+/g) || []).length) + 0.35;
  const out = [];
  for (const t of tramos) {
    const total = t.g.reduce((s, w) => s + silabas(w), 0);
    let c = t.ini;
    for (const w of t.g) {
      const d = ((t.fin - t.ini) * silabas(w)) / total;
      out.push({ texto: w, inicio: r3(c), fin: r3(c + d), ...(claves[out.length] ? { clave: true } : {}) });
      c += d;
    }
  }
  return out;
}

/** Parte un subtítulo largo en dos, por la coma o el espacio más cercano a la mitad. */
function partir(texto, max = MAX_SUBTITULO) {
  if (texto.length <= max) return [texto];
  const mitad = texto.length / 2;
  let mejor = -1, puntaje = Infinity;
  for (const m of texto.matchAll(/, | (?:y|e|o|u|ni|and|or|but|pero|que|e|ou|mas) | /g)) {
    const coma = m[0].startsWith(',');
    const corte = coma ? m.index + 1 : m.index;
    const p = Math.abs(corte - mitad) + (coma ? 0 : m[0].length > 1 ? 6 : 12);
    if (p < puntaje) { puntaje = p; mejor = corte; }
  }
  if (mejor <= 0) return [texto];
  return [texto.slice(0, mejor).trim(), texto.slice(mejor).trim()].flatMap(x => partir(x, max));
}
const enLineas = t => (t.length <= MAX_LINEA ? t : partir(t, MAX_LINEA).length === 2 ? partir(t, MAX_LINEA).join('\n') : t);

const vttHora = s => {
  const ms = Math.round(s * 1000);
  const h = Math.floor(ms / 3600000), m = Math.floor(ms / 60000) % 60, seg = Math.floor(ms / 1000) % 60;
  return `${String(h).padStart(2, '0')}:${String(m).padStart(2, '0')}:${String(seg).padStart(2, '0')}.${String(ms % 1000).padStart(3, '0')}`;
};

function idComposicion(src) {
  const archivo = path.join(PROYECTO, `${src}.html`);
  if (!fs.existsSync(archivo)) throw new Error(`falta ${src}.html`);
  const html = fs.readFileSync(archivo, 'utf8');
  const m = html.slice(Math.max(0, html.indexOf('<template'))).match(/data-composition-id="([^"]+)"/);
  if (!m) throw new Error(`${src}.html no tiene data-composition-id dentro de su <template>`);
  return { id: m[1], declaraTiempos: /"id"\s*:\s*"tiempos"/.test(html) };
}

// ─── Música: el plan de «Product Launch» en tiempo del video ─────────────────────────────────────────────────────────────────
/** Encadena entrada → bucle → salida en compases (cada segmento empieza en un segundo par del video, así los compases de la pista caen
 *  siempre en segundos pares) y deja el último golpe de la pista en la firma del cierre. El cierre empieza en C = S + (cierreEn − salida),
 *  donde S (par) es donde arranca la salida; C cae en un pulso (en un compás si la firma está a un número par de segundos del inicio).
 *  Devuelve C (≥ fin del cuerpo) y los segmentos { v (video), p0, p1 (pista) }. */
function planMusica(plan, pista, cierre, finCuerpo) {
  const mapa = pista.mapa;
  const fase = mapa.primerCompas % COMPAS; // 0,05: los compases de la pista
  const corte = plan.corte ?? COMPAS;
  const entrada = plan.entrada, bucle = plan.bucle, salida = plan.salida;
  const enCompas = x => enRejilla(x, COMPAS, fase);
  for (const x of [entrada[0], entrada[1], salida, ...bucle.flat()]) {
    if (!enCompas(x)) throw new Error(`musica: ${x} no es cabeza de compás de la pista (${fase} + 2k)`);
  }
  for (const [b0, b1] of bucle) if (!enRejilla(b1 - b0, corte)) throw new Error(`musica: el tramo del bucle ${b0}–${b1} no es múltiplo del corte (${corte} s)`);
  if (!enRejilla(corte, COMPAS)) throw new Error('musica.corte debe ser múltiplo de 2 s (un compás)');
  const cierreEn = r3(mapa.ultimoGolpe - cierre.firma); // segundo de la pista donde empieza el cierre
  const salidaAntes = r3(cierreEn - salida);
  if (salidaAntes < 0) throw new Error(`musica.salida (${salida}) debe ser anterior a ${cierreEn}`);
  const largoEntrada = r3(entrada[1] - entrada[0]);
  for (let S = arriba(finCuerpo - salidaAntes, COMPAS); ; S = r3(S + COMPAS)) {
    const C = r3(S + salidaAntes);
    const segs = [];
    if (S < 0) {
      // Video muy corto: solo la salida, desde el compás que deja el último golpe en la firma.
      segs.push({ v: 0, p0: r3(salida - S), p1: mapa.fin });
      return { C, segs, cierreEn };
    }
    if (S <= largoEntrada) {
      if (!enRejilla(S, corte) && S !== largoEntrada) continue;
      if (S > 0) segs.push({ v: 0, p0: entrada[0], p1: r3(entrada[0] + S) });
    } else {
      const F = r3(S - largoEntrada);
      if (!enRejilla(F, corte)) continue;
      segs.push({ v: 0, p0: entrada[0], p1: entrada[1] });
      let v = largoEntrada, falta = F, k = 0;
      while (falta > 1e-6) {
        const [b0, b1] = bucle[k++ % bucle.length];
        const d = Math.min(r3(b1 - b0), falta);
        segs.push({ v, p0: b0, p1: r3(b0 + d) });
        v = r3(v + d);
        falta = r3(falta - d);
      }
    }
    segs.push({ v: S, p0: salida, p1: mapa.fin });
    return { C, segs, cierreEn };
  }
}

/** Lleva instantes de la pista a tiempo del video a través de los segmentos. */
const aVideo = (segs, tiempos) => segs.flatMap(s => tiempos.filter(t => t >= s.p0 - 1e-6 && t < s.p1 - 1e-6).map(t => r3(s.v + t - s.p0)));

/** Cama musical: segmentos con cruces de potencia constante de `cruce` s que terminan 10 ms antes de cada cabeza de compás, la envolvente
 *  de la voz (en dB) y el volumen de la biblioteca. Determinista. */
function camaMusical(pistaPcm, segs, largo, cruce, envolvente, volumen) {
  const n = Math.ceil(largo * SR);
  const out = new Float32Array(n * 2);
  const total = pistaPcm.length / 2;
  segs.forEach((s, i) => {
    const primero = i === 0, ultimo = i === segs.length - 1;
    const pre = primero ? 0 : cruce + 0.01;
    const finPista = ultimo ? s.p1 : s.p1 - 0.01;
    const desde = Math.round((s.p0 - pre) * SR), hasta = Math.min(total, Math.round(finPista * SR));
    const destino = Math.round((s.v - pre) * SR);
    const nIn = Math.round(cruce * SR), nOut = Math.round(cruce * SR);
    for (let k = desde; k < hasta; k++) {
      const d = destino + (k - desde);
      if (d < 0 || d >= n) continue;
      let g = 1;
      const deInicio = k - desde, alFin = hasta - 1 - k;
      if (!primero && deInicio < nIn) g *= Math.sin((Math.PI / 2) * (deInicio / nIn));
      if (primero && deInicio < 480) g *= deInicio / 480;
      if (!ultimo && alFin < nOut) g *= Math.sin((Math.PI / 2) * (alFin / nOut));
      if (ultimo && alFin < 2400) g *= alFin / 2400;
      out[d * 2] += pistaPcm[k * 2] * g;
      out[d * 2 + 1] += pistaPcm[k * 2 + 1] * g;
    }
  });
  for (let i = 0; i < n; i++) {
    const g = volumen * Math.pow(10, envolvente(i / SR) / 20);
    out[i * 2] *= g;
    out[i * 2 + 1] *= g;
  }
  return out;
}

/** Envolvente en dB de la música: 0 sin voz, −bajo bajo la voz; rampas coseno (baja antes de la frase, sube despacio después). */
function hacerEnvolvente(regiones, bajo) {
  const cos = x => 0.5 - 0.5 * Math.cos(Math.PI * Math.max(0, Math.min(1, x)));
  return t => {
    let g = 0;
    for (const r of regiones) {
      if (t < r.a - BAJAR || t > r.b + SUBIR) continue;
      const f = t < r.a ? cos((t - (r.a - BAJAR)) / BAJAR) : t > r.b ? 1 - cos((t - r.b) / SUBIR) : 1;
      g = Math.min(g, -bajo * f);
    }
    return g;
  };
}

const PARA = ['pastores', 'lideres', 'administradores', 'servidores'];
// v1.3 (decisión 241): la sección de Recursos donde se publica y, en «Para líderes», el departamento. Listas cerradas: es el contrato con el
// publicador de KingdomApp (tools/recursos/publicar.mjs); un valor nuevo se agrega aquí y allá a la vez.
const SECCIONES = ['pastores', 'lideres'];
const DEPARTAMENTOS = ['afirmacion', 'academia'];
/** «para» (a quién va), «seccion» y «departamento» (listas cerradas) y «mensaje» (el texto de WhatsApp, con {enlace}) del guion, validados;
 *  todos son opcionales. */
function extrasFicha(guion) {
  let para = guion.para;
  if (para !== undefined) {
    if (!Array.isArray(para) || !para.length || para.some(x => !PARA.includes(x))) throw new Error(`para: lista con valores de ${PARA.join(', ')}`);
    para = [...new Set(para)];
  }
  const seccion = guion.seccion;
  if (seccion !== undefined && !SECCIONES.includes(seccion)) throw new Error(`seccion: uno de ${SECCIONES.join(', ')}`);
  const departamento = guion.departamento;
  if (departamento !== undefined && !DEPARTAMENTOS.includes(departamento)) throw new Error(`departamento: uno de ${DEPARTAMENTOS.join(', ')}`);
  const mensaje = loc(guion.mensaje, 'mensaje');
  if (mensaje !== undefined && (typeof mensaje !== 'string' || !mensaje.includes('{enlace}'))) throw new Error('mensaje: el texto de WhatsApp debe llevar {enlace} donde va el enlace');
  return { para, seccion, departamento, mensaje };
}

// ─── preparar ───────────────────────────────────────────────────────────────────────────────────────────────────────────────
async function cargarGuion() {
  const ruta = path.join(PROYECTO, 'guion.mjs');
  if (!fs.existsSync(ruta)) throw new Error('falta guion.mjs en la carpeta del proyecto');
  return (await import(`${pathToFileURL(ruta).href}?v=${Date.now()}`)).default;
}

async function preparar() {
  const guion = await cargarGuion();
  for (const c of ['slug', 'titulo', 'descripcion', 'escenas']) if (!guion[c]) throw new Error(`guion.mjs no tiene «${c}»`);
  if (!/^[a-z0-9-]+$/.test(guion.slug)) throw new Error('slug: solo minúsculas, números y guiones');
  const titulo = loc(guion.titulo, 'titulo'), descripcion = loc(guion.descripcion, 'descripcion');
  if (titulo.replace(/\*/g, '').length > 48) console.warn(`  aviso: el título tiene ${titulo.replace(/\*/g, '').length} caracteres (máx. ~48 en la intro)`);
  if (descripcion.length > 200) console.warn(`  aviso: la descripción tiene ${descripcion.length} caracteres (la vista previa de WhatsApp corta cerca de 160)`);
  const llamado = guion.llamado ?? 'acompanamiento', contacto = guion.contacto ?? 'whatsapp';
  if (!['acompanamiento', 'compartir', 'ninguno'].includes(llamado)) throw new Error('llamado: acompanamiento | compartir | ninguno');
  if (!['whatsapp', 'sitio', 'ninguno'].includes(contacto)) throw new Error('contacto: whatsapp | sitio | ninguno');

  extrasFicha(guion);
  verificarCli();
  const kit = await montarKit(PROYECTO);
  const introPieza = kit.piezas['intro-recurso'];
  const siguiente = loc(guion.siguiente, 'siguiente') ?? '';
  const cierreBase = kit.piezas['cierre-recurso'];
  const cierre = siguiente ? cierreBase : { ...cierreBase, ...cierreBase.variantes.sinSiguiente };
  const pistaId = guion.musica?.pista ?? 'product-launch';
  const pista = kit.musica.biblioteca[pistaId];
  if (!pista?.mapa?.recurso) throw new Error(`la pista «${pistaId}» no tiene plan del Tipo Recurso en kit.json`);
  const plan = { ...pista.mapa.recurso, ...(guion.musica ?? {}) };
  const bajoLaVoz = plan.bajoLaVoz ?? 20;
  if (bajoLaVoz < 18 || bajoLaVoz > 24) console.warn(`  aviso: musica.bajoLaVoz = ${bajoLaVoz} dB (el kit pide 18–24)`);

  // Música en el proyecto (fuera de git).
  const mp3 = path.join(PROYECTO, 'assets', 'musica', path.basename(pista.archivo));
  fs.mkdirSync(path.dirname(mp3), { recursive: true });
  if (!fs.existsSync(mp3)) fs.copyFileSync(path.join(KIT, pista.archivo), mp3);

  // 1. Escenas y voz.
  const escenas = [];
  let t = introPieza.duracion;
  const ids = new Set();
  for (const e of guion.escenas) {
    if (!e.id || !/^[a-z0-9-]+$/.test(e.id)) throw new Error(`escena sin id válido (minúsculas, números y guiones): ${JSON.stringify(e).slice(0, 80)}`);
    if (ids.has(e.id)) throw new Error(`escena repetida: ${e.id}`);
    ids.add(e.id);
    const src = e.capitulo ? 'identidad/capitulo-recurso' : (e.composicion ?? `compositions/${e.id}`).replace(/\.html$/, '');
    const comp = idComposicion(src);
    if (!comp.declaraTiempos) console.warn(`  aviso: ${src}.html no declara la variable «tiempos» (la escena no podrá leer sus tiempos)`);
    const variables = {};
    for (const [k, v] of Object.entries(e.capitulo ?? {})) variables[k] = loc(v, `${e.id}.capitulo.${k}`);
    for (const [k, v] of Object.entries(e.variables ?? {})) variables[k] = loc(v, `${e.id}.variables.${k}`);
    if (e.capitulo) variables.idioma = IDIOMA;
    const conVoz = (e.frases ?? []).length > 0;
    const alinear = e.alinear ?? (conVoz ? 'pulso' : 'compas');
    const inicio = arriba(t, alinear === 'compas' ? COMPAS : PULSO);
    if (escenas.length) escenas.at(-1).duracion = r3(inicio - escenas.at(-1).inicio);
    let dur;
    const frases = [];
    if (conVoz) {
      let cursor = e.entrada ?? ENTRADA;
      e.frases.forEach((f, j) => {
        if (typeof f[IDIOMA] !== 'string') throw new Error(`${e.id}: la frase ${j + 1} no tiene texto en «${IDIOMA}»`);
        const a = voz(f, kit);
        let desde = Math.max(cursor, f.desde ?? 0);
        if (f.alPulso) desde = arriba(desde, PULSO);
        desde = r3(desde);
        frases.push({
          id: `voz-${e.id}-${j + 1}`, clave: f.clave ?? null, texto: f[IDIOMA].replace(/\*/g, ''), textoPantalla: f[IDIOMA],
          wav: a.wav, archivo: a.archivo, duracion: r3(a.duracion), inicio: desde, fin: r3(desde + a.duracion),
          palabras: palabrasEstimadas(a.wav, f[IDIOMA]).map(p => ({ ...p, inicio: r3(desde + p.inicio), fin: r3(desde + p.fin) })),
        });
        cursor = desde + a.duracion + (f.pausa ?? PAUSA);
      });
      dur = arriba(Math.max(e.minimo ?? 0, frases.at(-1).fin + (e.cola ?? COLA)), PULSO);
    } else {
      dur = arriba(e.duracion ?? 4, PULSO);
    }
    if (!conVoz && dur > 8) console.warn(`  aviso: ${e.id} dura ${dur} s sin voz (frame-recurso.md: nada quieto más de ~6 s)`);
    escenas.push({ id: e.id, src, compId: comp.id, inicio, duracion: dur, frases, variables, estirable: !!e.estirable, alinear, conVoz, sonidos: e.sonidos ?? [] });
    t = r3(inicio + dur);
  }
  const finCuerpo = t;

  // 2. Música: el cierre en un compás par, con el último golpe en la firma; la holgura va a las escenas estirables (en compases) y a la última.
  const { C, segs, cierreEn } = planMusica(plan, pista, cierre, finCuerpo);
  let holgura = r3(C - finCuerpo);
  const estirables = escenas.filter(e => e.estirable);
  for (let k = 0; holgura >= COMPAS - 1e-6 && estirables.length; k++) {
    estirables[k % estirables.length].duracion = r3(estirables[k % estirables.length].duracion + COMPAS);
    holgura = r3(holgura - COMPAS);
  }
  escenas.at(-1).duracion = r3(escenas.at(-1).duracion + holgura);
  let c = introPieza.duracion;
  for (const e of escenas) {
    e.inicio = arriba(c, e.alinear === 'compas' ? COMPAS : PULSO);
    c = r3(e.inicio + e.duracion);
  }
  if (Math.abs(c - C) > 1e-3) throw new Error(`interno: el cuerpo termina en ${c} y el cierre empieza en ${C}`);
  const cierreInicio = C;
  const total = r3(C + cierre.duracion);
  const largoMusica = r3(C + (pista.mapa.fin - cierreEn));

  // 3. Mezcla: voz a −16 LUFS (cada frase ya normalizada) y la música a su volumen de biblioteca, bajando bajo la voz.
  const frasesAbs = escenas.flatMap(e => e.frases.map(f => ({ ...f, a: r3(e.inicio + f.inicio), b: r3(e.inicio + f.fin) })));

  // Sonidos de acción del kit (pocos y exactos, cada uno con su causa en pantalla): en el host, con el acento un cuadro después del momento.
  //   sonidos: [{ sonido: 'aparicion', en: 2.5 }]  ·  { sonido: 'confirmacion', frase: 'clave' | 1, palabra: 3, desfase: -0.25, alPulso: true }
  const sonidos = [];
  for (const e of escenas) {
    for (const [k, x] of e.sonidos.entries()) {
      const d = kit.sonidosAccion?.sonidos?.[x.sonido];
      if (!d) throw new Error(`${e.id}: el sonido «${x.sonido}» no está en el kit (${Object.keys(kit.sonidosAccion.sonidos).join(', ')})`);
      let rel = x.en;
      if (x.frase !== undefined) {
        const fr = typeof x.frase === 'number' ? e.frases[x.frase] : e.frases.find(y => y.clave === x.frase);
        if (!fr) throw new Error(`${e.id}: el sonido ${k + 1} apunta a una frase que no existe (${x.frase})`);
        rel = x.palabra !== undefined ? fr.palabras[Math.min(x.palabra, fr.palabras.length - 1)].inicio : fr.inicio;
      }
      if (typeof rel !== 'number') throw new Error(`${e.id}: el sonido ${k + 1} necesita «en» (segundos en la escena) o «frase»`);
      rel = rel + (x.desfase ?? 0); // primero el desfase y luego el pulso: igual que T.pulso(t + desfase) en la escena
      if (x.alPulso) rel = arriba(rel, PULSO);
      sonidos.push({ id: `snd-${e.id}-${k + 1}`, nombre: x.sonido, inicio: r3(Math.max(0, e.inicio + rel + 1 / CPS - d.acento)), duracion: d.duracion });
    }
  }
  const regiones = [];
  for (const f of frasesAbs) {
    const a = f.a - ANTES_VOZ, b = f.b + TRAS_VOZ;
    if (regiones.length && a - regiones.at(-1).b < UNIR) regiones.at(-1).b = b;
    else regiones.push({ a, b });
  }
  // Bajo la voz: la música queda `bajoLaVoz` dB por debajo de la voz (voz −16, música sin voz −18 → baja 18 dB con 20).
  const bajo = bajoLaVoz - (kit.voz.lufs - kit.musica.lufs); // = bajoLaVoz − (−16 − (−18)) = bajoLaVoz − 2
  const envolvente = hacerEnvolvente(regiones, bajo);
  const pistaPcm = decodificar(mp3, 2);
  const cama = camaMusical(pistaPcm, segs, largoMusica, plan.cruce ?? 0.03, envolvente, pista.volumen);
  const vozPcm = new Float32Array(Math.ceil(total * SR));
  const cacheVoz = new Map();
  for (const f of frasesAbs) {
    if (!cacheVoz.has(f.wav)) cacheVoz.set(f.wav, decodificar(f.wav, 1));
    const p = cacheVoz.get(f.wav), d = Math.round(f.a * SR);
    for (let i = 0; i < p.length && d + i < vozPcm.length; i++) vozPcm[d + i] += p[i];
  }
  const dirMezcla = path.join(PROYECTO, 'assets', 'mezcla', IDIOMA);
  fs.rmSync(dirMezcla, { recursive: true, force: true });
  escribirWav(path.join(dirMezcla, 'musica.wav'), cama, 2);
  escribirWav(path.join(dirMezcla, 'voz.wav'), vozPcm, 1);

  // Comprobación de la mezcla: sonoridad de la música y de la voz en los mismos tramos con voz, y de la música sin voz.
  const tramo = (pcm, canales, rangos) => {
    const partes = rangos.flatMap(([a, b]) => [pcm.subarray(Math.round(a * SR) * canales, Math.round(b * SR) * canales)]);
    const largo = partes.reduce((s, p) => s + p.length, 0), out = new Float32Array(largo);
    let o = 0;
    for (const p of partes) { out.set(p, o); o += p.length; }
    return out;
  };
  const tmp = path.join(dirMezcla, 'tmp');
  const conVoz = frasesAbs.map(f => [f.a, f.b]);
  escribirWav(path.join(tmp, 'm-voz.wav'), tramo(cama, 2, conVoz), 2);
  escribirWav(path.join(tmp, 'v-voz.wav'), tramo(vozPcm, 1, conVoz), 1);
  const sinVozRangos = escenas.filter(e => !e.conVoz).map(e => [e.inicio + 0.6, e.inicio + e.duracion - 0.3]).filter(([a, b]) => b - a > 1);
  const mVoz = medir(path.join(tmp, 'm-voz.wav')).I, vVoz = medir(path.join(tmp, 'v-voz.wav')).I;
  let mSin = null;
  if (sinVozRangos.length) {
    escribirWav(path.join(tmp, 'm-sin.wav'), tramo(cama, 2, sinVozRangos), 2);
    mSin = medir(path.join(tmp, 'm-sin.wav')).I;
  }
  fs.rmSync(tmp, { recursive: true, force: true });

  // 4. Tiempos en el video: compases, golpes y secciones de la música; escenas y frases.
  const golpes = aVideo(segs, pista.mapa.golpes);
  const pulsosJson = JSON.parse(fs.readFileSync(path.join(KIT, pista.pulsos), 'utf8')).beats;
  const fuertesUmbral = [...pulsosJson.map(b => b.strength)].sort((x, y) => x - y)[Math.floor(pulsosJson.length * 0.9)];
  const fuertes = aVideo(segs, pulsosJson.filter(b => b.strength >= fuertesUmbral).map(b => r3(Math.round((b.time - pista.mapa.primerCompas % COMPAS) / PULSO) * PULSO + pista.mapa.primerCompas % COMPAS)));
  const secciones = segs.flatMap(s => pista.mapa.tramos.filter(x => x.hasta > s.p0 && x.desde < s.p1)
    .map(x => ({ desde: r3(s.v + Math.max(x.desde, s.p0) - s.p0), hasta: r3(s.v + Math.min(x.hasta, s.p1) - s.p0), que: x.que })));
  const picos = [...new Set([...golpes, ...fuertes])].sort((x, y) => x - y);
  const tiemposEscena = e => {
    const rel = picos.filter(g => g >= e.inicio && g < e.inicio + e.duracion).map(g => r3(g - e.inicio));
    return {
      duracion: e.duracion, inicioAbs: e.inicio, idioma: IDIOMA, compas0: r3((COMPAS - (e.inicio % COMPAS)) % COMPAS), golpes: rel,
      frases: e.frases.map(f => ({ id: f.id, clave: f.clave, texto: f.texto, inicio: f.inicio, fin: f.fin, palabras: f.palabras })),
    };
  };

  // 5. Subtítulos (VTT, no quemados): uno por frase, partido en cues de 2 líneas de ~42 caracteres.
  const subtitulos = [];
  for (const e of escenas) {
    e.frases.forEach((f, j) => {
      const inicio = e.inicio + f.inicio;
      const fin = j + 1 < e.frases.length ? e.inicio + e.frases[j + 1].inicio - 0.05 : e.inicio + Math.min(e.duracion, f.fin + 0.6);
      const partes = partir(f.texto);
      const largo = partes.reduce((s, p) => s + p.length, 0);
      let cc = inicio;
      for (const p of partes) {
        const d = (fin - inicio) * (p.length / largo);
        subtitulos.push({ inicio: r3(cc), fin: r3(cc + d), texto: enLineas(p) });
        cc += d;
      }
    });
  }
  fs.mkdirSync(path.join(PROYECTO, 'renders'), { recursive: true });
  const vtt = ['WEBVTT', '', ...subtitulos.flatMap((s, i) => [String(i + 1), `${vttHora(s.inicio)} --> ${vttHora(s.fin)}`, s.texto, ''])].join('\n');
  fs.writeFileSync(path.join(PROYECTO, 'renders', `recurso-${IDIOMA}.vtt`), vtt);

  // 6. index.html (generado por idioma; no va a git).
  const h = [];
  h.push(`<!doctype html>
<html lang="${IDIOMA}">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1920, height=1080" />
    <title>${esc(titulo.replace(/\*/g, ''))} — Recursos de Kingdom (${IDIOMA})</title>
    <!-- GENERADO por _herramientas/recurso.mjs desde guion.mjs (kit ${kit.version}, hyperframes@${HF}): no editar a mano. -->
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
    <script src="identidad/recurso.js"></script>
    <link rel="stylesheet" href="identidad/fuentes/fuentes.css" />
    <link rel="stylesheet" href="identidad/kit.css" />
    <style>
      html, body { margin: 0; width: 1920px; height: 1080px; overflow: hidden; background: #060d1f; }
      #root { position: relative; width: 1920px; height: 1080px; overflow: hidden; background: #060d1f; font-family: 'Inter', sans-serif; }
      #root > [data-composition-src] { position: absolute; inset: 0; }
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="root" data-start="0" data-width="1920" data-height="1080" data-duration="${total}">
      <div id="fondo-recurso" data-composition-id="fondo-recurso" data-composition-src="identidad/${kit.piezas['fondo-recurso'].archivo}" data-track-kind="graphics"
        data-variable-values='${attrJson({ duracion: r3(cierreInicio - introPieza.duracion) })}'
        data-start="${introPieza.duracion}" data-duration="${r3(cierreInicio - introPieza.duracion)}" data-track-index="0" data-width="1920" data-height="1080"></div>
      <div id="intro-recurso" data-composition-id="intro-recurso" data-composition-src="identidad/${introPieza.archivo}" data-track-kind="graphics"
        data-variable-values='${attrJson({ titulo, ceja: loc(guion.ceja, 'ceja') ?? '', idioma: IDIOMA })}'
        data-start="0" data-duration="${introPieza.duracion}" data-track-index="1" data-width="1920" data-height="1080"></div>`);
  for (const e of escenas) {
    h.push(`      <div id="escena-${e.id}" data-composition-id="${e.compId}" data-composition-src="${e.src}.html" data-track-kind="graphics"
        data-variable-values='${attrJson({ ...e.variables, tiempos: JSON.stringify(tiemposEscena(e)) })}'
        data-start="${e.inicio}" data-duration="${e.duracion}" data-track-index="2" data-width="1920" data-height="1080"></div>`);
  }
  h.push(`      <div id="cierre-recurso" data-composition-id="cierre-recurso" data-composition-src="identidad/${cierreBase.archivo}" data-track-kind="graphics"
        data-variable-values='${attrJson({ siguiente, llamado, contacto, idioma: IDIOMA })}'
        data-start="${cierreInicio}" data-duration="${cierre.duracion}" data-track-index="1" data-width="1920" data-height="1080"></div>
      <audio id="musica" src="assets/mezcla/${IDIOMA}/musica.wav" data-start="0" data-duration="${largoMusica}" data-track-index="10" data-volume="1"></audio>
      <audio id="voz" src="assets/mezcla/${IDIOMA}/voz.wav" data-start="0" data-duration="${total}" data-track-index="11" data-volume="1"></audio>
      <audio id="marca-intro" src="identidad/audio/sonido-marca.wav" data-start="${r3(introPieza.sonido)}" data-duration="${kit.sonido.duracion}" data-track-index="12" data-volume="1"></audio>
      <audio id="marca-cierre" src="identidad/audio/sonido-marca.wav" data-start="${r3(cierreInicio + cierre.sonido)}" data-duration="${kit.sonido.duracion}" data-track-index="13" data-volume="1"></audio>
${sonidos.map(x => `      <audio id="${x.id}" src="identidad/audio/${x.nombre}.wav" data-start="${x.inicio}" data-duration="${x.duracion}" data-track-index="14" data-volume="1"></audio>\n`).join('')}    </div>
    <script>
      // El host solo monta escenas y audio; el fondo (fondo-recurso) y cada escena animan lo suyo.
      const tl = gsap.timeline({ paused: true });
      tl.set({}, {}, ${total});
      window.__timelines['root'] = tl;
    </script>
  </body>
</html>
`);
  fs.writeFileSync(path.join(PROYECTO, 'index.html'), h.join('\n'));

  const tiempos = {
    version: 1, generado: `recurso.mjs (kit ${kit.version}, hyperframes@${HF})`, slug: guion.slug, idioma: IDIOMA, titulo, descripcion, total, cps: CPS,
    intro: { inicio: 0, duracion: introPieza.duracion, sonido: introPieza.sonido },
    cierre: { inicio: cierreInicio, duracion: cierre.duracion, firma: r3(cierreInicio + cierre.firma), sonido: r3(cierreInicio + cierre.sonido), siguiente, llamado, contacto },
    musica: {
      pista: pistaId, archivo: `assets/mezcla/${IDIOMA}/musica.wav`, largo: largoMusica, pulso: PULSO, compas: COMPAS, primerPulso: 0,
      nota: 'Pulsos en múltiplos de 0,5 s del video y compases en los segundos pares; golpes = los del mapa de la pista; fuertes = los pulsos más intensos (10 %)',
      segmentos: segs.map(s => ({ video: [s.v, r3(s.v + s.p1 - s.p0)], pista: [s.p0, s.p1] })), secciones, golpes, fuertes,
      mezcla: { vozLufs: kit.voz.lufs, sinVozLufs: kit.musica.lufs, bajoLaVoz, bajaDb: r3(bajo), medido: { musicaBajoLaVoz: r3(mVoz), vozEnEsosTramos: r3(vVoz), diferencia: r3(vVoz - mVoz), musicaSinVoz: mSin === null ? null : r3(mSin) } },
    },
    escenas: escenas.map(e => ({
      id: e.id, composicion: `${e.src}.html`, compId: e.compId, inicio: e.inicio, duracion: e.duracion, fin: r3(e.inicio + e.duracion), conVoz: e.conVoz,
      ...tiemposEscena(e), frases: e.frases.map(f => ({ id: f.id, clave: f.clave, texto: f.texto, inicio: f.inicio, fin: f.fin, inicioAbs: r3(e.inicio + f.inicio), finAbs: r3(e.inicio + f.fin), palabras: f.palabras })),
    })),
    subtitulos,
  };
  fs.writeFileSync(path.join(PROYECTO, `tiempos-${IDIOMA}.json`), JSON.stringify(tiempos, null, 1));
  escribirScript(guion);

  const cuerpoDur = r3(cierreInicio - introPieza.duracion);
  const mmss = s => `${Math.floor(s / 60)}:${String(Math.round(s % 60)).padStart(2, '0')}`;
  console.log(`✓ ${guion.slug} (${IDIOMA}): ${escenas.length} escenas, ${frasesAbs.length} frases, ${subtitulos.length} subtítulos; intro ${introPieza.duracion} s + cuerpo ${cuerpoDur} s + cierre ${cierre.duracion} s = ${total} s (${mmss(total)})`);
  for (const e of escenas) {
    const voz = e.frases.length ? `voz ${e.frases[0].inicio}–${e.frases.at(-1).fin}` : 'sin voz';
    console.log(`  ${e.id.padEnd(22)} ${String(e.inicio).padStart(7)} s  dura ${String(e.duracion).padStart(5)} s  (${voz})`);
  }
  console.log(`  música: ${segs.map(s => `${s.p0}–${s.p1}@${s.v}`).join(' → ')}; holgura ${r3(C - finCuerpo)} s; cierre en ${cierreInicio} s (pista ${cierreEn})`);
  console.log(`  mezcla: música bajo la voz ${mVoz.toFixed(1)} LUFS, voz ${vVoz.toFixed(1)} LUFS → ${(vVoz - mVoz).toFixed(1)} dB por debajo` +
    (mSin === null ? '' : `; música sin voz ${mSin.toFixed(1)} LUFS`));
  const mitades = [introPieza.duracion / 2, ...escenas.map(e => e.inicio + e.duracion / 2), cierreInicio + cierre.duracion - 0.5].map(x => r3(x));
  console.log(`  mitades para el snapshot: npx --yes hyperframes@${HF} snapshot --at ${mitades.join(',')} --no-end`);
  if (total < 300 || total > 420) console.warn(`  aviso: el video dura ${mmss(total)} (el Tipo Recurso pide 5–7 min)`);
}

function escribirScript(guion) {
  const l = ['# SCRIPT — narración bloqueada', '', '<!-- GENERADO desde guion.mjs por _herramientas/recurso.mjs: se edita guion.mjs. -->', '',
    `Slug: \`${guion.slug}\` · Llamado: ${guion.llamado ?? 'acompanamiento'} · Contacto: ${guion.contacto ?? 'whatsapp'}`, ''];
  const nombres = { es: 'Español', en: 'English', pt: 'Português' };
  for (const idioma of ['es', 'en', 'pt']) {
    const tit = typeof guion.titulo === 'string' ? (idioma === 'es' ? guion.titulo : null) : guion.titulo?.[idioma];
    if (!tit) continue;
    l.push(`## ${nombres[idioma]} — «${tit}»`, '', `> ${typeof guion.descripcion === 'string' ? guion.descripcion : guion.descripcion?.[idioma] ?? ''}`, '');
    guion.escenas.forEach((e, i) => {
      const cap = e.capitulo ? ` — capítulo ${e.capitulo.numero ?? ''} «${typeof e.capitulo.titulo === 'string' ? e.capitulo.titulo : e.capitulo.titulo?.[idioma] ?? ''}»` : '';
      l.push(`### ${i + 1}. ${e.id}${cap}`, '');
      if (!(e.frases ?? []).length) l.push(`_(sin voz, ${e.duracion ?? 4} s)_`);
      for (const f of e.frases ?? []) l.push(`- ${f[idioma] ?? '_(falta)_'}${f.voz?.[idioma] ? ` _(se pronuncia: ${f.voz[idioma]})_` : ''}`);
      l.push('');
    });
  }
  fs.writeFileSync(path.join(PROYECTO, 'SCRIPT.md'), l.join('\n'));
}

// ─── render ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────
async function render() {
  const tiempos = JSON.parse(fs.readFileSync(path.join(PROYECTO, `tiempos-${IDIOMA}.json`), 'utf8'));
  const idx = fs.readFileSync(path.join(PROYECTO, 'index.html'), 'utf8');
  if (!idx.includes(`<html lang="${IDIOMA}">`)) throw new Error(`index.html es de otro idioma: corre «preparar --idioma ${IDIOMA}» antes`);
  // Temporales en el disco del proyecto (F:): el render guarda cuadros y C: está casi lleno.
  const tmp = path.join(PROYECTO, 'renders', 'tmp');
  fs.mkdirSync(path.join(tmp, 'cuadros'), { recursive: true });
  const salida = `renders/recurso-${IDIOMA}.mp4`;
  const argumentos = ['--yes', `hyperframes@${HF}`, 'render', '--quality', 'high', '--output', salida, '--frames-cache-dir', path.join(tmp, 'cuadros'), '--quiet'];
  console.log(`render de ${tiempos.total} s con hyperframes@${HF} (temporales en ${path.relative(PROYECTO, tmp)})…`);
  const t0 = process.hrtime.bigint();
  const cola = [];
  const codigo = await new Promise(res => {
    const p = spawn('npx', argumentos, { shell: process.platform === 'win32', env: { ...process.env, TEMP: tmp, TMP: tmp }, stdio: ['ignore', 'pipe', 'pipe'] });
    const guardar = d => { cola.push(d.toString()); while (cola.join('').length > 8000) cola.shift(); };
    p.stdout.on('data', guardar);
    p.stderr.on('data', guardar);
    p.on('close', res);
  });
  const segundos = Number(process.hrtime.bigint() - t0) / 1e9;
  if (codigo !== 0) throw new Error(`el render falló (código ${codigo}):\n${cola.join('').slice(-2500)}`);
  const d = duracion(path.join(PROYECTO, salida));
  const medida = { idioma: IDIOMA, video: r3(d), segundosRender: r3(segundos), porSegundoDeVideo: r3(segundos / d), hyperframes: HF, fecha: new Date().toISOString().slice(0, 10) };
  fs.writeFileSync(path.join(PROYECTO, 'renders', `render-${IDIOMA}.json`), JSON.stringify(medida, null, 1));
  fs.rmSync(tmp, { recursive: true, force: true });
  console.log(`✓ ${salida}: ${d.toFixed(1)} s de video en ${(segundos / 60).toFixed(1)} min (${medida.porSegundoDeVideo} s de render por segundo de video)`);
}

// ─── entregar ───────────────────────────────────────────────────────────────────────────────────────────────────────────────
async function entregar() {
  const guion = await cargarGuion();
  const kit = JSON.parse(fs.readFileSync(path.join(KIT, 'kit.json'), 'utf8'));
  const mp4 = path.join(PROYECTO, 'renders', `recurso-${IDIOMA}.mp4`);
  const vtt = path.join(PROYECTO, 'renders', `recurso-${IDIOMA}.vtt`);
  for (const f of [mp4, vtt]) if (!fs.existsSync(f)) throw new Error(`falta ${path.relative(PROYECTO, f)} (preparar y render primero)`);
  const tiempos = JSON.parse(fs.readFileSync(path.join(PROYECTO, `tiempos-${IDIOMA}.json`), 'utf8'));
  const d = duracion(mp4);
  if (Math.abs(d - tiempos.total) > 0.2) throw new Error(`el render dura ${d.toFixed(2)} s y la composición ${tiempos.total} s: vuelve a renderizar`);
  const destino = path.join(PROYECTO, 'entrega', IDIOMA);
  fs.rmSync(destino, { recursive: true, force: true });
  fs.mkdirSync(destino, { recursive: true });

  // Audio: el del render (mezcla con su propio objetivo) a −16 LUFS en dos pasadas lineales, con 1 dB de margen de pico para el AAC.
  // Video: CRF con techo de bitrate (1080: 1,4 Mb/s + 128 kb/s ≈ 69 MB en 6 min como máximo; 720: 650 + 96 kb/s ≈ 34 MB).
  const lufs = kit.voz.lufs;
  // v1.3: el AAC rebasa el pico del WAV (a 96 kb/s, hasta ~1,4 dB con la mezcla de «Afirmando la cosecha»). El video se codifica UNA vez
  // sin audio y el audio se prepara con un margen de pico que baja de a 1 dB (limitador suave antes de normalizar) hasta que el archivo
  // ya codificado cumpla; cada margen se calcula una sola vez y sirve para los dos videos.
  const audios = new Map();
  const audioCon = (margen) => {
    if (audios.has(margen)) return audios.get(margen);
    const audio = path.join(destino, `audio${margen}.wav`);
    normalizar(mp4, audio, lufs, margen);
    const m = medir(audio);
    if (m.TP > margen || Math.abs(m.I - lufs) > 0.3) {
      // El modo lineal no alcanzó (picos): limitador suave y otra pasada.
      const lim = path.join(destino, 'audio-lim.wav');
      ffmpeg(['-i', audio, '-af', `alimiter=limit=${r3(Math.pow(10, (margen - 0.6) / 20))}:attack=5:release=60:level=disabled`, '-ar', String(SR), lim]);
      normalizar(lim, audio, lufs, margen);
      fs.rmSync(lim);
    }
    audios.set(margen, audio);
    return audio;
  };
  const x264 = ['-c:v', 'libx264', '-preset', 'slow', '-tune', 'animation', '-profile:v', 'high', '-pix_fmt', 'yuv420p', '-g', String(CPS * 2)];
  const video1080 = path.join(destino, 'video-1080.mp4'), video720 = path.join(destino, 'video-720.mp4');
  const solo1080 = path.join(destino, 'solo-1080.mp4'), solo720 = path.join(destino, 'solo-720.mp4');
  ffmpeg(['-i', mp4, '-map', '0:v:0', '-an', ...x264, '-crf', '20', '-maxrate', '1400k', '-bufsize', '2800k', solo1080]);
  ffmpeg(['-i', mp4, '-map', '0:v:0', '-an', '-vf', 'scale=1280:720:flags=lanczos', ...x264, '-crf', '22', '-maxrate', '650k', '-bufsize', '1300k', solo720]);
  const margenes = {};
  for (const [solo, kbps, salida] of [[solo1080, '128k', video1080], [solo720, '96k', video720]]) {
    for (const margen of [-2.5, -3.5, -4.5]) {
      ffmpeg(['-i', solo, '-i', audioCon(margen), '-map', '0:v:0', '-map', '1:a:0', '-c:v', 'copy', '-c:a', 'aac', '-b:a', kbps, '-ar', String(SR),
        '-movflags', '+faststart', salida]);
      margenes[path.basename(salida)] = margen;
      const v = medir(salida);
      if (v.TP <= -1.6 && Math.abs(v.I - lufs) <= 0.4) break;
    }
  }
  for (const f of [solo1080, solo720, ...audios.values()]) fs.rmSync(f, { force: true });
  fs.copyFileSync(vtt, path.join(destino, 'video.vtt'));

  // Póster para la vista previa de WhatsApp (1200×630, menos de 300 KB): el título del episodio al final de la intro, o el segundo del guion.
  const enPoster = Number(guion.poster?.en ?? tiempos.intro.duracion - 0.8);
  const poster = path.join(destino, 'poster.jpg');
  for (const q of [3, 4, 5, 7, 9]) {
    ffmpeg(['-ss', String(enPoster), '-i', mp4, '-frames:v', '1', '-vf', 'scale=1200:675:flags=lanczos,crop=1200:630', '-q:v', String(q), poster]);
    if (fs.statSync(poster).size < 300000) break;
  }
  ffmpeg(['-ss', String(enPoster), '-i', mp4, '-frames:v', '1', '-vf', 'scale=1200:675:flags=lanczos,crop=1200:630', '-c:v', 'libwebp', '-quality', '82', path.join(destino, 'poster.webp')]);

  // Verificación: sonoridad y pico de los dos videos tal como se entregan.
  const verif = {};
  for (const f of [video1080, video720]) {
    const v = medir(f);
    verif[path.basename(f)] = { lufs: r3(v.I), picoDbtp: r3(v.TP) };
    if (Math.abs(v.I - lufs) > 0.5 || v.TP > -1.5) throw new Error(`${path.basename(f)}: ${v.I} LUFS y pico ${v.TP} dBTP (debe ser ${lufs} ±0,5 y ≤ −1,5)`);
  }
  // ficha.json con la forma exacta que espera el publicador de la app (Plataforma → Recursos): slug, idioma, titulo, descripcion, duracion,
  // ancho y alto (los del video de 1080), archivos { nombre: { bytes, sha256 } } y, si el guion los trae, para y mensaje. Las medidas
  // técnicas (sonoridad, pico, versiones) van aparte, a renders/entrega-<idioma>.json, para no mezclarlas con lo que se publica.
  const archivos = {};
  for (const nombre of ['video-1080.mp4', 'video-720.mp4', 'poster.jpg', 'poster.webp', 'video.vtt']) {
    const b = fs.readFileSync(path.join(destino, nombre));
    archivos[nombre] = { bytes: b.length, sha256: sha(b) };
  }
  const [ancho, alto] = correr('ffprobe', ['-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=width,height', '-of', 'csv=p=0', video1080]).stdout.trim().split(',').map(Number);
  if (ancho !== 1920 || alto !== 1080) throw new Error(`video-1080.mp4 mide ${ancho}×${alto} (debe ser 1920×1080)`);
  if (archivos['poster.jpg'].bytes >= 300000) throw new Error(`poster.jpg pesa ${archivos['poster.jpg'].bytes} bytes (WhatsApp pide menos de 300 KB)`);
  const { para, seccion, departamento, mensaje } = extrasFicha(guion);
  const ficha = {
    slug: guion.slug, idioma: IDIOMA, titulo: tiempos.titulo.replace(/\*/g, ''), descripcion: tiempos.descripcion, duracion: r3(duracion(video1080)),
    ancho, alto, archivos, ...(para ? { para } : {}), ...(seccion ? { seccion } : {}), ...(departamento ? { departamento } : {}),
    ...(mensaje ? { mensaje } : {}),
  };
  fs.writeFileSync(path.join(PROYECTO, 'renders', `entrega-${IDIOMA}.json`), JSON.stringify({
    kit: kit.version, hyperframes: HF, fecha: new Date().toISOString().slice(0, 10), audio: verif, margenPicoAntesDelAac: margenes,
    video720: { bytes: archivos['video-720.mp4'].bytes }, poster: { en: enPoster, ancho: 1200, alto: 630 },
  }, null, 1));
  fs.writeFileSync(path.join(destino, 'ficha.json'), JSON.stringify(ficha, null, 2) + '\n');
  const mb = n => (n / 1048576).toFixed(1);
  console.log(`✓ entrega/${IDIOMA}/ (${d.toFixed(1)} s): video-1080 ${mb(archivos['video-1080.mp4'].bytes)} MB (${verif['video-1080.mp4'].lufs} LUFS, ${verif['video-1080.mp4'].picoDbtp} dBTP) · ` +
    `video-720 ${mb(archivos['video-720.mp4'].bytes)} MB · póster ${Math.round(archivos['poster.jpg'].bytes / 1024)} KB · VTT · ficha.json` +
    `${para ? ` (para: ${para.join(', ')})` : ''}${seccion ? ` (sección: ${seccion}${departamento ? ` · ${departamento}` : ''})` : ''}`);
  console.log('  Publicarlo en Recursos (Plataforma) lo hace el líder; el dueño lo revisa ya publicado.');
}

const comandos = { preparar, render, entregar };
comandos[COMANDO]().catch(e => { console.error(`✗ ${e.message}`); process.exit(1); });
