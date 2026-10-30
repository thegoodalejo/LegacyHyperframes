// Sonidos de acción de Kingdom (kit v1.1): propios, generados por código con el mismo motor de sonido-marca.mjs y siempre idénticos
// (mismo código, misma huella en kit.json → sonidosAccion.*.sha256). Acompañan las acciones visibles de un video sin voz (el clip del
// sitio, el Comercial, el Corto) y van por debajo de la música: acompañan, no distraen.
//   toque         un toque suave en pantalla (75 ms)
//   aparicion     un elemento o una tarjeta que aparece (220 ms)
//   desliz        un barrido de aire para un corte rápido o una transición (360 ms)
//   subida        1,5 s que suben y terminan en un golpe (el golpe cae a 1,5 s; dura 1,9 s con la cola)
//   confirmacion  un «listo» de dos notas suaves, Si5 → Mi6 (320 ms)
// Las notas son de Mi mayor, como las campanas de la marca. El ruido sale de un generador con semilla fija: nada es aleatorio.
// El WAV crudo sale con el pico a −3 dBFS (lo que firma la huella); montar-kit.mjs le aplica la `ganancia` de kit.json, que fija su nivel
// respecto de la música (kit.json → sonidosAccion.mezcla).
//   node sonidos-accion.mjs <carpeta> [nombre…]     escribe <nombre>.wav crudos (48 kHz, estéreo, 16 bits)
// Se usa Math de V8 y operaciones en orden fijo: el resultado es el mismo en cualquier máquina con Node 22.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { SR, hz, mezclar, reverb } from './sonido-marca.mjs';

/** Generador de números con semilla (mulberry32): el «ruido» es siempre el mismo. Devuelve valores en [−1, 1). */
function ruido(semilla) {
  let a = semilla >>> 0;
  return () => {
    a = (a + 0x6d2b79f5) >>> 0;
    let t = a;
    t = Math.imul(t ^ (t >>> 15), t | 1);
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
    return ((t ^ (t >>> 14)) >>> 0) / 2147483648 - 1;
  };
}

/** Filtro de estado variable (Chamberlin con dos pasadas): pasa banda o pasa bajos con frecuencia y Q por muestra. */
function filtro() {
  let bajo = 0, banda = 0;
  return (x, f, q, tipo) => {
    const k = 2 * Math.sin(Math.PI * Math.min(f, SR / 4) / (2 * SR)); // dos pasadas = el doble de muestras
    for (let p = 0; p < 2; p++) {
      bajo += k * banda;
      const alto = x - bajo - banda / q;
      banda += k * alto;
    }
    return tipo === 'bajo' ? bajo : banda;
  };
}

/** Envolvente con subida en coseno de `ataque` s y caída exponencial `tau` s. */
const env = (t, ataque, tau) => (t < ataque ? 0.5 - 0.5 * Math.cos(Math.PI * t / ataque) : 1) * Math.exp(-Math.max(0, t - ataque) / tau);

/** Paneo de igual potencia (−1 izquierda, 1 derecha). */
const paneo = p => [Math.cos((p + 1) * Math.PI / 4), Math.sin((p + 1) * Math.PI / 4)];

/** Tono con deslizamiento de frecuencia (fase acumulada): de f0 a f1 en `glide` s, exponencial. */
function tono(L, R, N, inicio, f0, f1, glide, parciales, ataque, ganancia, pan) {
  const [gl, gr] = paneo(pan);
  const i0 = Math.round(inicio * SR);
  const fases = parciales.map(() => 0);
  for (let i = i0; i < N; i++) {
    const t = (i - i0) / SR;
    const f = t < glide ? f0 * Math.pow(f1 / f0, t / glide) : f1;
    let s = 0;
    for (let j = 0; j < parciales.length; j++) {
      const [razon, amp, tau] = parciales[j];
      fases[j] += 2 * Math.PI * f * razon / SR;
      s += amp * Math.exp(-t / tau) * Math.sin(fases[j]);
    }
    const a = t < ataque ? 0.5 - 0.5 * Math.cos(Math.PI * t / ataque) : 1;
    L[i] += s * a * ganancia * gl;
    R[i] += s * a * ganancia * gr;
  }
}

/** Ruido filtrado: `forma(t)` → [frecuencia, q, amplitud, paneo] en cada instante. Cada canal con su propio ruido (más aire). */
function aire(L, R, N, inicio, fin, semilla, tipo, forma) {
  const nl = ruido(semilla), nr = ruido(semilla + 7919);
  const fl = filtro(), fr = filtro();
  const i0 = Math.round(inicio * SR), i1 = Math.min(N, Math.round(fin * SR));
  for (let i = i0; i < i1; i++) {
    const t = (i - i0) / SR;
    const [f, q, amp, pan] = forma(t);
    const [gl, gr] = paneo(pan);
    L[i] += fl(nl(), f, q, tipo) * amp * gl;
    R[i] += fr(nr(), f, q, tipo) * amp * gr;
  }
}

const CAMPANITA = tau => [[1, 1, tau], [2, 0.16, tau * 0.4], [3, 0.05, tau * 0.25]];

export const SONIDOS = {
  // Un toque suave: un «tic» de vidrio (Mi6 sobre Mi5) con un soplo de ruido de 3 ms. Sin chasquido duro: el ataque es de 1,5 ms.
  toque: {
    descripcion: 'Toque suave en pantalla: un «tic» corto de vidrio (Mi6 sobre Mi5) con un soplo brevísimo',
    duracion: 0.075, cola: 0.02, humedo: 0,
    componer(L, R, N) {
      mezclar(L, R, N, 0, hz(88), [[1, 1, 0.012]], 0.0015, 0.55, 0.05);
      mezclar(L, R, N, 0, hz(76), [[1, 1, 0.018]], 0.0015, 0.4, -0.05);
      aire(L, R, N, 0, 0.02, 11, 'banda', t => [3200, 1.1, 0.5 * env(t, 0.0005, 0.004), 0]);
    },
  },
  // Algo que aparece: una gota que sube de Mi5 a Si5 en 35 ms y un brillo en Mi6.
  aparicion: {
    descripcion: 'Aparece un elemento: una gota redonda que sube de Mi5 a Si5, con un brillo en Mi6',
    duracion: 0.22, cola: 0.07, humedo: 0.12,
    componer(L, R, N) {
      tono(L, R, N, 0, hz(76), hz(83), 0.035, [[1, 1, 0.06], [2, 0.12, 0.03]], 0.004, 0.6, 0);
      tono(L, R, N, 0.03, hz(88), hz(88), 0, [[1, 1, 0.045]], 0.003, 0.18, 0.2);
    },
  },
  // Barrido de aire: ruido por un filtro de banda que sube de 500 a 5000 Hz, crece hasta el 55 % y cae; viaja de izquierda a derecha.
  desliz: {
    descripcion: 'Barrido de aire: ruido filtrado que sube de 500 a 5000 Hz y cruza de izquierda a derecha',
    duracion: 0.36, cola: 0.04, humedo: 0,
    componer(L, R, N) {
      const d = 0.36, tp = 0.2;
      aire(L, R, N, 0, d, 23, 'banda', t => {
        const u = t / d;
        const a = t < tp ? Math.pow(Math.sin(Math.PI / 2 * t / tp), 2) : Math.pow(Math.cos(Math.PI / 2 * (t - tp) / (d - tp)), 2);
        return [500 * Math.pow(10, u), 1.4, a, -0.6 + 1.2 * u];
      });
    },
  },
  // Subida de 1,5 s que termina en un golpe: aire que sube de 300 a 6000 Hz y un tono que sube una octava (Mi3 → Mi4); en 1,5 s se
  // corta y cae el golpe (un bombo corto que baja de 150 a 55 Hz, Mi3 con sus armónicos para que se oiga en un celular y las campanas Mi5 + Si5 suaves).
  subida: {
    descripcion: 'Subida de 1,5 s (aire y un tono que sube una octava, Mi3 → Mi4) que termina en un golpe con campanas Mi5 + Si5',
    duracion: 1.9, cola: 0.25, humedo: 0.2,
    componer(L, R, N) {
      const g = 1.5;
      aire(L, R, N, 0, g, 37, 'banda', t => {
        const u = t / g;
        const corte = t > g - 0.006 ? (g - t) / 0.006 : 1;
        return [300 * Math.pow(20, u), 1.5 + 2.5 * u, Math.pow(u, 2.5) * corte * 0.5, 0];
      });
      // Tono que sube: fase acumulada, amplitud creciente y corte limpio en el golpe.
      const [gl, gr] = paneo(0);
      let fase = 0, fase5 = 0;
      for (let i = 0; i < Math.round(g * SR); i++) {
        const t = i / SR, u = t / g;
        const f = hz(52) * Math.pow(2, u);
        fase += 2 * Math.PI * f / SR;
        fase5 += 2 * Math.PI * f * 1.5 / SR;
        const corte = t > g - 0.006 ? (g - t) / 0.006 : 1;
        const s = (Math.sin(fase) + 0.35 * Math.sin(fase5)) * Math.pow(u, 2) * 0.16 * corte;
        L[i] += s * gl;
        R[i] += s * gr;
      }
      // El golpe.
      tono(L, R, N, g, 150, 55, 0.05, [[1, 1, 0.09]], 0.002, 0.55, 0);
      mezclar(L, R, N, g, hz(52), [[1, 1, 0.16], [2, 0.4, 0.08], [3, 0.15, 0.05]], 0.002, 0.4, 0);
      aire(L, R, N, g, g + 0.12, 41, 'bajo', t => [2500, 0.8, 0.45 * env(t, 0.001, 0.03), 0]);
      mezclar(L, R, N, g, hz(76), CAMPANITA(0.35), 0.003, 0.3, -0.2);
      mezclar(L, R, N, g, hz(83), CAMPANITA(0.35), 0.003, 0.22, 0.2);
    },
  },
  // «Listo»: dos notas suaves que resuelven en la tónica, Si5 → Mi6, a 0,1 s.
  confirmacion: {
    descripcion: '«Listo»: dos notas suaves que resuelven en la tónica, Si5 → Mi6',
    duracion: 0.32, cola: 0.08, humedo: 0.15,
    componer(L, R, N) {
      mezclar(L, R, N, 0, hz(83), CAMPANITA(0.12), 0.003, 0.35, -0.15);
      mezclar(L, R, N, 0.1, hz(88), CAMPANITA(0.14), 0.003, 0.4, 0.15);
    },
  },
};

/** WAV PCM de 16 bits, estéreo, con el pico en `picoDb` dBFS (por omisión −3: el crudo que firma la huella de kit.json). */
export function generarSonidoAccion(nombre, picoDb = -3) {
  const s = SONIDOS[nombre];
  if (!s) throw new Error(`no existe el sonido de acción «${nombre}»`);
  const N = Math.round(SR * s.duracion);
  const L = new Float64Array(N), R = new Float64Array(N);
  s.componer(L, R, N);
  const wl = s.humedo ? reverb(L, N, 0) : null, wr = s.humedo ? reverb(R, N, 23) : null;
  const sl = new Float64Array(N), sr = new Float64Array(N);
  const finDesde = N - Math.round(s.cola * SR);
  let pico = 0;
  for (let i = 0; i < N; i++) {
    const fin = i < finDesde ? 1 : 0.5 + 0.5 * Math.cos(Math.PI * (i - finDesde) / (N - finDesde));
    sl[i] = (L[i] + (wl ? wl[i] * s.humedo : 0)) * fin;
    sr[i] = (R[i] + (wr ? wr[i] * s.humedo : 0)) * fin;
    pico = Math.max(pico, Math.abs(sl[i]), Math.abs(sr[i]));
  }
  // Primero al crudo (−3 dBFS) y redondeado a 16 bits; la ganancia de la mezcla se aplica sobre ese crudo, así el nivel final depende
  // solo de la huella y de kit.json.
  const g = Math.pow(10, -3 / 20) / pico, extra = Math.pow(10, (picoDb + 3) / 20);
  const datos = Buffer.alloc(N * 4);
  const q = v => Math.max(-32768, Math.min(32767, Math.round(v)));
  for (let i = 0; i < N; i++) {
    datos.writeInt16LE(q(q(sl[i] * g * 32767) * extra), i * 4);
    datos.writeInt16LE(q(q(sr[i] * g * 32767) * extra), i * 4 + 2);
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
  const [carpeta, ...nombres] = process.argv.slice(2);
  if (!carpeta) {
    console.error(`Uso: node sonidos-accion.mjs <carpeta> [${Object.keys(SONIDOS).join(' ')}]`);
    process.exit(1);
  }
  fs.mkdirSync(carpeta, { recursive: true });
  for (const n of nombres.length ? nombres : Object.keys(SONIDOS)) {
    fs.writeFileSync(path.join(carpeta, `${n}.wav`), generarSonidoAccion(n));
    console.log(path.join(carpeta, `${n}.wav`));
  }
}
