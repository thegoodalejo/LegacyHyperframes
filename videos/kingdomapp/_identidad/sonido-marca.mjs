// Sonido de marca de Kingdom: propio, sin terceros ni licencias, y siempre idéntico (mismo código, misma huella en kit.json).
// Acompaña a «la corona se levanta». Cada receta es una frase corta; `acentos` dice dónde cae cada nota y el último acento es el que se
// alinea con la corona completa (0,9 s después de que empieza la firma; ver kit.json → piezas.*.sonido).
// Va a −20 LUFS; esa normalización la hace montar-kit.mjs con FFmpeg.
//   node sonido-marca.mjs <salida.wav> [receta]     escribe el WAV crudo (48 kHz, estéreo, 16 bits, pico a −3 dBFS)
// Se usa Math de V8 y operaciones en orden fijo: el resultado es el mismo en cualquier máquina con Node 22.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

export const SR = 48000;
export const hz = midi => 440 * Math.pow(2, (midi - 69) / 12);

/** Suma una nota (parciales [razón, amplitud, tau]) a L y R desde `inicio`. `trem` = [Hz, profundidad] para el vibrato de un vibráfono. */
export function mezclar(L, R, N, inicio, frecuencia, parciales, ataque, ganancia, paneo, trem) {
  // Paneo de igual potencia: −1 izquierda, 0 centro, 1 derecha.
  const a = (paneo + 1) * Math.PI / 4;
  const gl = Math.cos(a) * ganancia, gr = Math.sin(a) * ganancia;
  const i0 = Math.round(inicio * SR);
  for (let i = i0; i < N; i++) {
    const t = (i - i0) / SR;
    let env = t < ataque ? 0.5 - 0.5 * Math.cos(Math.PI * t / ataque) : 1;
    if (trem) env *= 1 - trem[1] * (0.5 - 0.5 * Math.cos(2 * Math.PI * trem[0] * t));
    let s = 0;
    for (const [razon, amp, tau] of parciales) s += amp * Math.exp(-t / tau) * Math.sin(2 * Math.PI * frecuencia * razon * t);
    s *= env;
    L[i] += s * gl;
    R[i] += s * gr;
  }
}

// Reverberación de Schroeder (4 peines con amortiguación + 2 pasatodo), un poco distinta por canal para dar amplitud.
export function reverb(x, N, separacion) {
  const k = SR / 44100;
  const peines = [1557, 1617, 1491, 1422].map(d => Math.round((d + separacion) * k));
  const pasatodo = [556, 225].map(d => Math.round((d + separacion) * k));
  const y = new Float64Array(N);
  for (const d of peines) {
    const buf = new Float64Array(d);
    let p = 0, filtro = 0;
    for (let i = 0; i < N; i++) {
      const sal = buf[p];
      filtro = sal * 0.72 + filtro * 0.28;
      buf[p] = x[i] + filtro * 0.8;
      y[i] += sal * 0.25;
      p = (p + 1) % d;
    }
  }
  for (const d of pasatodo) {
    const buf = new Float64Array(d);
    let p = 0;
    for (let i = 0; i < N; i++) {
      const b = buf[p];
      const sal = -y[i] + b;
      buf[p] = y[i] + b * 0.5;
      y[i] = sal;
      p = (p + 1) % d;
    }
  }
  return y;
}

// Timbres
const CAMPANA_SUAVE = [[1, 1, 1.1], [2, 0.22, 0.45], [3, 0.07, 0.22], [5.4, 0.025, 0.07]];
const SENO_LARGO = tau => [[1, 1, tau]];

// El dueño eligió «campanas» el 2026-10-30 entre tres opciones (llegada, calma y campanas), después de descartar la v1 de siete notas
// rápidas («corona»). Las descartadas están descritas en KingdomApp docs/videos/identidad.md → «Sonido».
export const RECETAS = {
  // Campanas suaves «din, din… don» (Sol#5, Si5 y Mi5: Mi mayor), la última más larga y con brillo. La cola se desvanece en el último
  // medio segundo para que quepa en el cierre del tutorial sin «Sigue con» (2,5 s) y en el del Corto (2,5 s).
  campanas: {
    descripcion: 'Campanas suaves «din, din… don» (Mi mayor), la última más larga',
    duracion: 2.1, cola: 0.5, humedo: 0.28, acentos: [0, 0.2, 0.52],
    componer(m) {
      m(0, hz(80), CAMPANA_SUAVE, 0.003, 0.4, -0.25);
      m(0.2, hz(83), CAMPANA_SUAVE, 0.003, 0.4, 0.25);
      m(0.52, hz(76) - 0.6, CAMPANA_SUAVE, 0.003, 0.3, -0.1);
      m(0.52, hz(76) + 0.6, CAMPANA_SUAVE, 0.003, 0.3, 0.1);
      m(0.52, hz(64), SENO_LARGO(1), 0.12, 0.07, 0);
      m(0.52, hz(71), SENO_LARGO(1), 0.12, 0.05, 0);
    },
  },
};

/** La receta por defecto al correr este archivo a mano; montar-kit.mjs usa la de kit.json → sonido.receta. */
export const ELEGIDA = 'campanas';

export function generarSonidoMarca(nombre = ELEGIDA) {
  const receta = RECETAS[nombre];
  if (!receta) throw new Error(`no existe la receta de sonido «${nombre}»`);
  const N = Math.round(SR * receta.duracion);
  const L = new Float64Array(N), R = new Float64Array(N);
  receta.componer((inicio, f, parciales, ataque, ganancia, paneo, trem) => mezclar(L, R, N, inicio, f, parciales, ataque, ganancia, paneo, trem));

  const wl = reverb(L, N, 0), wr = reverb(R, N, 23);
  const salidaL = new Float64Array(N), salidaR = new Float64Array(N);
  const finDesde = N - Math.round((receta.cola ?? 0.3) * SR);
  let pico = 0;
  for (let i = 0; i < N; i++) {
    const fin = i < finDesde ? 1 : 0.5 + 0.5 * Math.cos(Math.PI * (i - finDesde) / (N - finDesde));
    salidaL[i] = (L[i] + wl[i] * receta.humedo) * fin;
    salidaR[i] = (R[i] + wr[i] * receta.humedo) * fin;
    pico = Math.max(pico, Math.abs(salidaL[i]), Math.abs(salidaR[i]));
  }
  const g = Math.pow(10, -3 / 20) / pico;

  // WAV PCM de 16 bits, estéreo intercalado.
  const datos = Buffer.alloc(N * 4);
  for (let i = 0; i < N; i++) {
    datos.writeInt16LE(Math.max(-32768, Math.min(32767, Math.round(salidaL[i] * g * 32767))), i * 4);
    datos.writeInt16LE(Math.max(-32768, Math.min(32767, Math.round(salidaR[i] * g * 32767))), i * 4 + 2);
  }
  const cab = Buffer.alloc(44);
  cab.write('RIFF', 0);
  cab.writeUInt32LE(36 + datos.length, 4);
  cab.write('WAVE', 8);
  cab.write('fmt ', 12);
  cab.writeUInt32LE(16, 16);
  cab.writeUInt16LE(1, 20);
  cab.writeUInt16LE(2, 22);
  cab.writeUInt32LE(SR, 24);
  cab.writeUInt32LE(SR * 4, 28);
  cab.writeUInt16LE(4, 32);
  cab.writeUInt16LE(16, 34);
  cab.write('data', 36);
  cab.writeUInt32LE(datos.length, 40);
  return Buffer.concat([cab, datos]);
}

const esPrincipal = process.argv[1] && path.resolve(process.argv[1]).toLowerCase() === fileURLToPath(import.meta.url).toLowerCase();
if (esPrincipal) {
  const [salida, nombre] = process.argv.slice(2);
  if (!salida) {
    console.error(`Uso: node sonido-marca.mjs <salida.wav> [${Object.keys(RECETAS).join('|')}]`);
    process.exit(1);
  }
  fs.writeFileSync(salida, generarSonidoMarca(nombre));
  console.log(salida);
}
