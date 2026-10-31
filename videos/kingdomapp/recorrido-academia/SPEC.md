# SPEC · Recorrido de Academia — «La clase ya empezó… y lo que sigue» (16:9)

2026-10-30 · Contrato de construcción de la historia de [STORY.md](STORY.md). La parte 1 es el clip publicado
([clip-sitio-academia](../clip-sitio-academia/): su [SPEC](../clip-sitio-academia/SPEC.md), su [REVIEW](../clip-sitio-academia/REVIEW.md) y su
`index.html`), llevado a 16:9 sin reabrirlo; la parte 2 es nueva. Mismo método: cada adjetivo es un número, los valores por defecto están
prohibidos con nombre y los planos van cuadro por cuadro. Se construye desde aquí, se revisa contra esto y se cambia aquí cuando la vista
previa cambie la película. «Igual que el clip» quiere decir: copiado de `clip-sitio-academia/index.html` con los cambios de §2.1.

```text
GOAL:    Un pastor que no conoce Kingdom termina pensando «con esto armo los cursos, los exámenes se califican solos, veo quién se
         está quedando y el certificado vale afuera» y toca «Prueba gratis 30 días».
OUTPUT:  HyperFrames 0.8.221 · una composición 1920×1080 (16:9) · 30 fps. (La 9:16 queda para después; no se especifica aquí.)
TIME:    97,0 s = 2910 cuadros: cuerpo 0–92,0 (cuadros 0–2759) + cierre del Comercial 92,0–97,0 (2760–2909). 120 BPM = 15 cuadros
         por pulso en todo el video (la costura de la música conserva la grilla, §0).
LOOK:    la noche del sitio (#060D1F) con el halo y la retícula de puntos del kit; tinta #EAF0FF; un solo acento, el dorado #E8B95A, en
         tres lugares (la ceja «ACADEMIA», la palabra «líderes» y el botón del cierre). Fraunces 560 84 px / −0,02 em para las frases;
         Inter para la ceja y «Datos de ejemplo». El medio: la app REAL de Kingdom Demo, en dos ventanas del kit sobre la noche: el
         celular (`.k-ventana-16x9`, 720×900) y el escritorio (`.k-ventana-escritorio`, 1440×760); nunca un aparato dibujado.
OBJECTS: las dos ventanas; seis mundos de celular (profesor, alumna, quien coordina, la alumna en el examen, el profesor en la sábana,
         la página de verificación) y dos de escritorio (el asistente, el tablero); el punto de toque; las nueve frases; la ceja; la
         píldora «Datos de ejemplo»; el cierre del Comercial. Nada más existe en el cuadro.
MOTION:  curvas por papel (§1.6); un movimiento de cámara por compás (14 cuadros, power2.inOut), quieto después; cada corte y cada
         entrada en un pulso; cada cambio de mundo en un golpe (120 · 240 · 360 · 840 · 1320 · 1680 · 2040 · 2280 · 2760).
SHOTS:   catorce planos (§2).
BANNED:  §1.8.
QA:      §4.
```

---

## 0. La música: la edición y el reloj

### 0.1 La edición (una sola costura, medida)

«Product Launch» (The_Mountain, `_identidad/musica/product-launch-the-mountain.mp3`, 86,05 s, 120 BPM, compases de 2 s desde el 2,05;
`kit.json` → `musica.biblioteca.product-launch`) se alarga **repitiendo 24 s (12 compases): del 22,05 al 46,05 de la pista**, es decir, el
final de la primera subida, el respiro y la segunda subida con sus golpes del 36, el 38 y el 42,05. Se toca del 14,05 al 46,05 (lo mismo que
el clip y dos compases más), se salta al 22,05 y se sigue hasta el final natural de la pista.

**Por qué ahí** (análisis de los 41 compases por timbre, armonía y energía, 2026-10-30): el compás que sigue al salto (pista 22,05) es el
más parecido de toda la pista al que se esperaba oír (46,05; similitud 0,61, la mejor para ese compás), y el anterior al salto (44,05) se
parece al anterior al destino (20,05; 0,65). Los dos bordes son tiempos fuertes con ataque (46,045: 0,98; 22,045: 0,92), y el cruce de 30 ms
**termina 5 ms antes** del ataque: el golpe del 22,05 suena entero y tapa la unión. Medido sobre la prueba: la envolvente de 31,60 a 32,40 del
montaje coincide con la que se esperaba (pista 45,65–46,45) a ±0,4 dB; el salto de muestra en la mezcla (0,074) está dentro de lo que la
pista tiene en sus propios tiempos fuertes (0,061–0,078); después de la costura el montaje es la pista muestra a muestra (correlación
0,998). Se descartaron: repetir el clímax (50,05–58,05 suena dos veces seguidas en la pista; cuatro veces se nota), repetir la salida
(alarga lo tranquilo al final), dos o tres costuras de 8 s (más puntos donde se puede notar) y empezar en el 2,05 (obliga a poner algo antes
del gancho).

```bash
# en recorrido-academia/ (script "musica" del package.json): 31,99 s + 64,037 s − 0,03 s de cruce = 95,997 s
ffmpeg -hide_banner -y -i ../_identidad/musica/product-launch-the-mountain.mp3 -filter_complex \
  "[0:a]atrim=start=14.05:end=46.04,asetpts=PTS-STARTPTS[a];[0:a]atrim=start=22.01,asetpts=PTS-STARTPTS[b];[a][b]acrossfade=d=0.03:c1=tri:c2=tri[m]" \
  -map "[m]" -ar 44100 -c:a pcm_s16le assets/musica/product-launch-recorrido.wav
```

- **Comprobación al armarla:** `ffprobe` da **95,997 s** (±5 ms). El cruce de 30 ms ocupa 31,960–31,990 del video (pista 46,010–46,040
  con 22,010–22,040). Mapa exacto: **video = pista − 14,05** hasta el 31,99 y **video = pista + 9,95** desde el 31,99.
- **Licencia:** la de Pixabay permite modificar la pista (`_identidad/licencias.md`); la pista editada no se redistribuye sola. Tiene
  Content ID: en YouTube puede llegar un reclamo de monetización, que se disputa con la licencia.

### 0.2 El reloj del video

| Video | Pista | Tramo de la pista (`kit.json` → `mapa`) | Lo que le toca al video |
|---|---|---|---|
| 0–4 | 14,05–18,05 | entrada sin bajo | El gancho del clip |
| 4–12 | 18,05–26,05 | primera subida (bajo en 18,05, pico en 20) | Profesor ↔ alumna |
| 12–20 | 26,05–34,05 | respiro | La lista de graduación |
| 20–28 | 34,05–42,05 | segunda subida (golpes 36 · 38 · 42,05) | Aprobar → el certificado de Andrea |
| **28**–32 | 42,05–46,05 | el golpe más fuerte y su compás | Látigo al escritorio: el asistente |
| **32**–36 | 22,05–26,05 (repetido) | final de la primera subida | El asistente, pasos 2–3 |
| 36–44 | 26,05–34,05 (repetido) | respiro | El asistente, pasos 3–5 y «¡Publicado!» |
| **44**–60 | 34,05–50,05 (repetido hasta 46,05) | segunda subida otra vez (golpe más fuerte en el **52,0**) | El examen que se califica solo; la sábana |
| **60**–76 | 50,05–66,05 | clímax brillante (dos frases de 8 s) | La sábana filtrada; el tablero |
| **76**–92 | 66,05–82,05 | salida tranquila | La verificación; la frase del sitio |
| **92**–96 | 82,05–86,05 | el último acorde, que se apaga solo (−17 dB en 92,0 → −31 en 93,0 → −89 en 96,0) | El cierre del Comercial |

### 0.3 La grilla, pulso por pulso

**Cuadros 0–839:** la tabla de `clip-sitio-academia/SPEC.md` §0, sin cambios (todos los pulsos en múltiplos de 15 salvo el 284).

**Cuadros 840–2760** (cuadro · fuerza). Hasta el 1860, la fuerza es la de `product-launch-the-mountain.pulsos.json` en el instante de la
pista; **desde el 1800 la detección de esa grilla se va a las corcheas** (marca 52,535, 53,415, 54,305… de la pista, medio pulso
corrido): en el clímax y la salida las negras siguen en la grilla de 2,05 + 0,5·n (el análisis por compases lo confirma) y la fuerza que va
abajo en *cursiva* es el flujo espectral medido en ese instante (otra escala: 1,00 = el 99,5 % más fuerte de la pista). Nada del video cae en
una corchea.

| Compás | Cuadros | Pulsos (cuadro · fuerza) | Lo que le toca |
|---|---|---|---|
| 15 | 840–899 | **840 ·1,00** · 855 ·0,68 · 870 ·0,51 · 885 ·0,52 | **Látigo al escritorio**; 870 toque «Nuevo curso»; 885 las opciones |
| 16 | 900–959 | **900 ·0,84** · 915 ·0,82 · 930 ·0,75 · 945 ·0,66 | 900 toque «En blanco» (iris); 915 «Paso 1 de 5»; el nombre se escribe |
| 17 | 960–1019 | **960 ·0,92** (costura) · 975 ·0,77 · 990 ·0,58 · 1005 ·0,52 | «Paso 2 de 5»: las materias se escriben |
| 18 | 1020–1079 | 1020 ·0,77 · 1035 ·0,74 · 1050 ·0,60 · 1065 ·0,58 | 1020 el paso 2 completo |
| 19 | 1080–1139 | 1080 ·0,76 · 1095 ·0,64 · 1110 ·0,50 · 1125 ·0,46 | «Paso 3 de 5» (respiro) |
| 20 | 1140–1199 | 1140 ·0,75 · 1155 ·0,61 · 1170 ·0,49 · 1185 ·0,49 | «Paso 4 de 5» |
| 21 | 1200–1259 | 1200 ·0,67 · 1215 ·0,67 · 1230 ·0,54 · 1245 ·0,50 | «Paso 5 de 5»; 1230 la cámara al pie |
| 22 | 1260–1319 | 1260 ·0,63 · 1275 ·0,56 · 1290 ·0,61 · 1305 ·0,68 | 1260 toque «Publicar»; 1275 «¡Publicado!» |
| 23 | 1320–1379 | **1320 ·0,93** · 1335 ·0,69 · 1350 ·0,52 · 1365 ·0,49 | **Látigo de vuelta: la alumna, «Pregunta 1 de 3»** |
| 24 | 1380–1439 | **1380 ·0,90** · **1395 ·0,89** · 1410 ·0,76 · 1425 ·0,68 | 1380 «Cuatro»; 1395 «Siguiente»; 1410 pregunta 2 |
| 25 | 1440–1499 | **1440 ·0,96** · 1455 ·0,77 · 1470 ·0,59 · 1485 ·0,60 | 1440 «Verdadero»; 1455 «Siguiente»; 1470 pregunta 3 |
| 26 | 1500–1559 | **1500 ·0,88** · 1515 ·0,74 · 1530 ·0,62 · 1545 ·0,60 | 1500 «Pablo»; 1515 «Revisar»; 1530 «Respondiste 3 de 3» con el reloj en «0:01»; 1545 «Calculando tu nota…» |
| 27 | 1560–1619 | **1560 ·1,00** · 1575 ·0,68 · 1590 ·0,51 · 1605 ·0,52 | **«Tu nota · 5 / 5»** |
| 28 | 1620–1679 | 1620 ·0,84 · 1635 ·0,82 · 1650 ·0,75 · 1665 ·0,66 | 1620 la lista «Correcta» |
| 29 | 1680–1739 | **1680 ·0,98** · 1695 ·0,74 · 1710 ·0,60 · 1725 ·0,57 | **Látigo abajo: el profesor, el 5 en la sábana** |
| 30 | 1740–1799 | 1740 ·0,79 · 1755 ·0,75 · 1770 ·0,69 · 1785 ·0,67 | 1740 la cámara a los filtros |
| 31 | 1800–1859 | **1800 ·*1,00*** · 1815 ·*0,98* · 1830 ·*0,77* · 1845 ·*0,81* | **1800 toque «En riesgo»** (empieza el clímax) |
| 32 | 1860–1919 | 1860 ·*0,71* · 1875 ·*0,97* · 1890 ·*0,71* · 1905 ·*0,69* | 1860 la tabla se corre hasta «Final» |
| 33 | 1920–1979 | **1920 ·*1,00*** · 1935 ·*0,92* · 1950 ·*0,67* · 1965 ·*0,76* | 1920 la cámara a la columna «Final» |
| 34 | 1980–2039 | 1980 ·*0,62* · 1995 ·*1,00* · 2010 ·*0,69* · 2025 ·*0,68* | Quieto |
| 35 | 2040–2099 | **2040 ·*1,00*** · 2055 ·*1,00* · 2070 ·*0,83* · 2085 ·*0,83* | **Látigo al escritorio: el tablero** |
| 36 | 2100–2159 | 2100 ·*0,71* · 2115 ·*0,87* · 2130 ·*0,73* · 2145 ·*0,71* | 2100 la app baja a «Alumnos en riesgo» |
| 37 | 2160–2219 | **2160 ·*1,00*** · **2175 ·*1,00*** · 2190 ·*0,58* · 2205 ·*0,68* | 2160 toque en la primera persona; 2175 la ficha |
| 38 | 2220–2279 | 2220 ·*0,54* · 2235 ·*1,00* · 2250 ·*0,68* · 2265 ·*1,00* | Quieto |
| 39 | 2280–2339 | **2280 ·*0,77*** · 2295 ·*0,46* · 2310 ·*0,41* · 2325 ·*0,43* | **Látigo de vuelta: `/verificar`**; 2310 el código se escribe |
| 40 | 2340–2399 | 2340 ·*0,46* · 2355 ·*0,50* · 2370 ·*0,46* · 2385 ·*0,47* | 2340 toque «Verificar» |
| 41 | 2400–2459 | **2400 ·*0,76*** · 2415 ·*0,51* · 2430 ·*0,44* · 2445 ·*0,40* | **«Certificado válido»** |
| 42 | 2460–2519 | 2460 ·*0,46* · 2475 ·*0,57* · 2490 ·*0,39* · 2505 ·*0,42* | 2460 la cámara a la tarjeta entera |
| 43 | 2520–2579 | **2520 ·*0,80*** · 2535 ·*0,51* · 2550 ·*0,45* · 2565 ·*0,43* | **La frase del sitio**; la ventana a un lado |
| 44 | 2580–2639 | 2580 ·*0,94* · 2595 ·*0,47* · 2610 ·*0,38* · 2625 ·*0,45* | Quieto |
| 45 | 2640–2699 | 2640 ·*0,78* · 2655 ·*0,48* · 2670 ·*0,40* · 2685 ·*0,42* | Quieto |
| 46 | 2700–2759 | 2700 ·*0,34* · 2715 ·*0,67* · 2730 ·*0,41* · 2745 ·*0,98* | La subida (desde 2716); el dip 2757–2759 |
| — | **2760** | el último acorde (pista 82,05) | **El cierre del Comercial** |

### 0.4 Nivel de la música

`<audio id="musica" src="assets/musica/product-launch-recorrido.wav" data-start="0" data-duration="96">`, **sin `data-volume`**: 0,7 en el
carril de volumen (−18 LUFS, como el clip) de principio a fin. **Sin fundido**: la pista termina sola debajo del cierre (§0.2). Si en la vista
previa las campanas del 92,38 quedan tapadas, el carril baja a 0,5 entre 92,0 y 92,3 (y se anota en el REVIEW); nada más se toca.

---

## 1. Los números del estilo

### 1.1 Paleta

La de `clip-sitio-academia/SPEC.md` §1.1, tal cual (fondo `#060D1F`, halo, puntos que nunca se mueven, tinta `#EAF0FF`, dorado `#E8B95A`
solo en la ceja, «líderes» y el botón del cierre; anillo `rgba(234,240,255,.12)`; placa de «Datos de ejemplo» `rgba(6,13,31,.72)`; el azul
de marca solo dentro del cierre). Cambia: el **dip** va en los cuadros **2757–2759** sobre las dos ventanas; el **halo** se asienta
1,08 → 1,00 (`sine.out`, 90 cuadros) en 0 · 120 · 240 · 360 · 840 · 1320 · 1680 · 2040 · 2280. Los colores de la app (el semáforo verde,
amarillo y rojo de la sábana, el azul del tema) viven dentro de la grabación y no se tocan ni se repiten fuera.

### 1.2 Tipografía (16:9)

| Pieza | Clase del kit | Familia · peso | Tamaño | Reglas |
|---|---|---|---|---|
| Frase | `.k-titular` con `font-size: 84px` | Fraunces 560; `<em>` itálica 500 dorada | **84 px** · interlínea 1,04 (87,4 px) · −0,02 em | Máx. 2 líneas en el escenario del celular, **1 línea** en el del escritorio; saltos fijados a mano; izquierda; `text-wrap: balance` apagado; sin sombra |
| Ceja | `.k-ceja` | Inter 700, MAYÚSCULAS, +0,10 em | **28 px** | Una palabra: «ACADEMIA» |
| Datos de ejemplo | `.k-datos-ejemplo` (la de 16:9) | Inter 600 | **22 px**, píldora de 40 px | En cada ventana, abajo a la izquierda, a 24 px |
| Texto de la app | (grabación) | la de la app | ≥ **28 px** en todo encuadre de lectura | §1.5 |

Saltos fijados: «La clase / ya empezó.» · «Sin listas / de papel.» · «Quien cumple, / se gradúa.» · «Un curso, en cinco pasos.» (una línea) ·
«Exámenes que / se califican solos.» · «Sabes quién / va en riesgo.» · «Toda tu escuela, de un vistazo.» (una línea) · «Y cualquiera / lo
verifica.» · «Forma a los *líderes* / que tu visión necesita». La más ancha es «que tu visión necesita» (≈ 890 px a 84 px): entra en la
columna de 936 px; si `check` marca desborde, la columna crece hacia la ventana (nunca se baja la letra de 84).

### 1.3 Radios y sombras

Los del kit: `.k-ventana` radio **28** (celular) y **20** (`.k-ventana-escritorio`), anillo y sombra de `kit.css`, `overflow: hidden`. Frases
y ceja sin sombra ni brillo.

### 1.4 Disposición: dos escenarios

| | Escenario del celular | Escenario del escritorio |
|---|---|---|
| Ventana | `#ventana-cel.k-ventana.k-ventana-16x9`: **x 1104 · y 90 · 720 × 900** | `#ventana-esc.k-ventana.k-ventana-escritorio`: **x 240 · y 260 · 1440 × 760** |
| Ceja | x 120 · y 412 | x 240 · y 92 |
| Frase | x 120 · y 460 · ancho 936 · hasta 2 líneas → termina en 635 | x 240 · y 132 · una línea → termina en 219 |
| Datos de ejemplo | dentro de la ventana, abajo a la izquierda, a 24 px | ídem |
| Final (desde el 2524) | la ventana a escala **0,92** con origen «100% 50%» y x **+24** (su borde izquierdo pasa de 1104 a 1186) | — |

- **Las dos ventanas viven en una sola tira horizontal** (`#escena`): la del celular en x 1104 y la del escritorio en x 240 + 1920 = **2160**.
  `#escena` en x 0 muestra el celular; en x **−1920**, el escritorio. Fuera de cuadro, cada una queda entera fuera (la del celular en
  −816…−96; la del escritorio en 2160…3600).
- **Las frases y la ceja no viajan con el látigo:** salen con blur antes y entran después, en el lugar de su escenario (§1.6). La ceja hace
  el mismo cambio de lugar en cada látigo horizontal y se queda quieta en el vertical.
- El 90 % seguro para títulos (96 px a los lados, 54 arriba y abajo) se cumple en los dos escenarios.

`window.KD` (la versión 16:9 de la del clip; las variables `--f-*` se derivan de aquí):

```js
window.KD = {
  fps: 30,
  cel: { x: 1104, y: 90, w: 720, h: 900, hVis: 900 },          // --f-k = 720/1170 = 0.615385; --f-grab-alto = 1558.15px
  esc: { x: 240, y: 260, w: 1440, h: 760, hVis: 760 },         // K = 1440/1920 = 0.75; alto de la grabación ajustada = 810
  grabCel: { w: 1170, h: 2532, cssW: 390 },                    // celular 390×844 a 3×
  grabEsc: { w: 1920, h: 1080, cssW: 1280 },                   // escritorio 1280×720 a 1,5× (modo video de capturar.mjs)
  latigoV: 1000,                                               // ranuras de la tira vertical del celular
  latigoH: 1920,                                               // la tira horizontal entre escenarios
  cambio: { escala: 0.92, x: 24, origen: '100% 50%' },         // la ventana del celular se hace a un lado (2524–2538)
};
```

### 1.5 La cámara: escalas de lectura

`enc(s, cx, cy)` del clip, una por ventana (con su `W`, `HV`, `PPC = W / cssW` y `VH`): pone el punto (cx, cy) en px CSS en el centro de lo
visible con la escala s, sin salirse de la grabación. **Una escala es de lectura si el texto de 14 px de la app queda en ≥ 28 px.**

**Celular (`#ventana-cel`, PPC 1,846):**

| Nivel | s | px del cuadro por px CSS | Visible (px CSS) | 14 px → |
|---|---|---|---|---|
| **G** | **1,085** | 2,003 | 359 × 449 | **28,0** |
| G⁺ | 1,15 | 2,123 | 340 × 424 | 29,7 |
| M | 1,40 | 2,585 | 279 × 348 | 36,2 |
| C | 1,80 | 3,323 | 217 × 271 | 46,5 |

G = 1,085 deja 1 px CSS de margen a los lados de las tarjetas de la app (x 16–374): es el plano general de todo el video. **Ningún encuadre
de lectura del celular baja de 1,085.** A 1,8, cada píxel de la grabación ocupa 1,1 px: nítida.

**Escritorio (`#ventana-esc`, PPC 1,125):**

| Nivel | s | px del cuadro por px CSS | Visible (px CSS) | 14 px → | Píxel de la grabación → |
|---|---|---|---|---|---|
| **D** | **1,80** | 2,025 | 711 × 375 | **28,4** | 1,35 px |
| D⁺ | 2,00 | 2,250 | 640 × 338 | 31,5 | 1,50 px (el tope del kit) |

El plano entero del escritorio (s = 1, la pantalla de 1280 px completa) deja el texto en 15,8 px: **solo existe durante el látigo** (el
mundo aterriza ya en D). Ningún encuadre de escritorio pasa de 2,0.

### 1.6 Curvas y duraciones (cada tween con su curva por nombre)

| Papel | Curva | Cuadros | Detalle |
|---|---|---|---|
| `entrada-palabra` | `power4.out` | 4 | blur 6 → 0 + opacidad; sin desplazamiento; arranca un cuadro antes del pulso; palabras a 2 cuadros (la frase 1, una por pulso) |
| `entrada-linea` | `power4.out` | 6 | la línea entera, blur 8 → 0 (la frase 2 y cada entrada de la ceja) |
| `salida-texto` | `power3.in` | 4–5 | blur 0 → 8 + opacidad; empieza 3 cuadros antes del golpe del cambio de mundo |
| `camara` | `power2.inOut` | **14** | un movimiento por compás; después, quieta; nunca mientras la app se desplaza sola |
| `punch` | `power2.inOut` | **9** | 675 (el nombre del certificado, del clip) y **1560** (la nota) |
| `latigo-v` | `power3.inOut` | **10** | la tira vertical del celular, 1000 px; arriba = al otro celular, abajo = de vuelta; el mundo que llega aterriza 1,04 → 1,00 (`power3.out`, 10) |
| `latigo-h` | `power3.inOut` | **10** | `#escena` 1920 px: **a la izquierda = al escritorio, a la derecha = de vuelta**; termina en el golpe (830–840, 1310–1320, 2030–2040, 2270–2280); la ventana que llega aterriza 1,04 → 1,00 (`power3.out`, 10 cuadros, desde su centro) |
| `iris` | `power2.out` | 5 | `clip-path: circle(0 → 1900px)` desde el centro del botón tocado: 375 y 660 (del clip) y **900** («En blanco» → el asistente) |
| `ventana-cambio` | `power2.inOut` | 15 | 2524–2538: escala 1 → 0,92, origen «100% 50%», x +24 |
| `halo` | `sine.out` | 90 | §1.1 |
| `dip` | escalón | 3 | `rgba(6,13,31,.40)` sobre las dos ventanas, 2757–2759 |
| marcas de toque | las del clip | — | aparece 4 cuadros antes, se hunde en el cuadro, se va 6 después; la onda de 450 ms (3 cuadros donde la pantalla cambia debajo del dedo) |
| velocidad de la grabación | `data-playback-rate` | — | **1×** en todo, salvo la escritura de las materias del asistente (960–1019) a **2×**; nada se frena |
| cierre | las del kit | 150 | no se imita en el cuerpo |

`data-motion-blur="on"` y `data-motion-blur-shutter="180"` en la raíz (los látigos se ven con el borrón real). Nunca `filter: blur()` sobre
una grabación.

### 1.7 Sonido

| Capa | Fuente | Nivel | Regla |
|---|---|---|---|
| Música | `assets/musica/product-launch-recorrido.wav` (§0.1) | 0,7 en el carril (−18 LUFS) | §0.4 |
| Sonidos de acción | kit v1.1 (`toque` en tres tomas a/b/c: `identidad/audio/toque.wav` y `assets/audio/toque-b.wav`, `toque-c.wav` del clip), `aparicion`, `desliz`, `subida`, `confirmacion` | `data-volume="1"`; **1,4** en los clave | `data-start = (cuadro de la imagen + 1) / 30 − acento` (toque 0 · aparicion 0 · desliz 0,2 · subida 1,5 · confirmacion 0,1) |
| Sonido de marca | `identidad/audio/sonido-marca.wav` | 1 | **92,38 s** (inicio del cierre + 0,38 de `kit.json`) |
| Mezcla de entrega | — | **−16 LUFS** integrada, pico real ≤ **−1 dBTP** | `npx hyperframes audio` sobre el render; si −16 pasa el pico, se bajan a 1,2 los sonidos de 1,4 antes que dejar la mezcla en −17,5 (el clip quedó en −17,6: se anota igual) |

**Los eventos de la parte 1 (0–839)** son los del clip (`clip-sitio-academia/index.html`, 20 sonidos), **sin** la `subida` del 26,53 ni
el sonido de marca del 28,38.

**Los eventos de la parte 2** (cuadro de la imagen → `data-start` en s):

| Imagen | Sonido | `data-start` | Nivel | Causa en pantalla |
|---|---|---|---|---|
| 840 | `desliz` | 27,833 | **1,4** | Látigo al escritorio |
| 870 | `toque` a | 29,033 | 1 | «Nuevo curso» |
| 900 | `toque` b | 30,033 | 1 | «En blanco» (iris) |
| 960 | `toque` c | 32,033 | 1 | «Siguiente» (fuera de cuadro: se oye, como el «Listo» de Membresía) → «Paso 2 de 5» |
| 1080 | `toque` a | 36,033 | 1 | «Siguiente» → paso 3 |
| 1140 | `toque` b | 38,033 | 1 | «Siguiente» → paso 4 |
| 1200 | `toque` c | 40,033 | 1 | «Siguiente» → paso 5 |
| 1260 | `toque` a | 42,033 | 1 | «Publicar» |
| 1275 | `confirmacion` | 42,433 | 1 | «¡Publicado!» |
| 1320 | `desliz` | 43,833 | 1 | Látigo de vuelta al celular |
| 1380 | `toque` b | 46,033 | 1 | «Cuatro» |
| 1395 | `toque` c | 46,533 | 1 | «Siguiente» |
| 1440 | `toque` a | 48,033 | 1 | «Verdadero» |
| 1455 | `toque` b | 48,533 | 1 | «Siguiente» |
| 1500 | `toque` c | 50,033 | 1 | «Pablo» |
| 1515 | `toque` a | 50,533 | 1 | «Revisar» |
| 1560 | `confirmacion` | 51,933 | **1,4** | «Tu nota · 5 / 5» |
| 1680 | `desliz` | 55,833 | 1 | Látigo hacia abajo, al profesor |
| 1800 | `toque` b | 60,033 | **1,4** | «En riesgo» |
| 1803 | `aparicion` | 60,133 | 1 | La tabla queda con los que están en riesgo |
| 1860 | `desliz` | 61,833 | 1 | La tabla se corre hasta «Final» (la app, con la cámara quieta) |
| 2040 | `desliz` | 67,833 | 1 | Látigo al escritorio |
| 2160 | `toque` c | 72,033 | 1 | La primera persona en riesgo |
| 2175 | `aparicion` | 72,533 | 1 | La ficha académica entra |
| 2280 | `desliz` | 75,833 | 1 | Látigo de vuelta al celular |
| 2340 | `toque` a | 78,033 | 1 | «Verificar» |
| 2400 | `confirmacion` | 79,933 | **1,4** | «Certificado válido» |
| 2716–2773 | `subida` | **90,533** | 1 | Hacia el cierre (golpe en el 2761) |
| 2771 | marca | 92,38 | 1 | Las campanas del cierre |

Sin tics de tecla (ni en el nombre del curso ni en el código del certificado). **Dos sonidos de acción nunca se enciman, salvo**
1800 + 1803 y 2160 + 2175 (toque y su resultado). La `subida` es la única del video.

### 1.8 BANNED: los valores por defecto prohibidos, con nombre

Valen enteros los de `clip-sitio-membresia/SPEC.md` §1.8 (1–20) y los de `clip-sitio-academia/SPEC.md` §1.8 (21–25). **El 26 («un cuarto
mundo») no aplica**: el recorrido existe para mostrar más mundos. Además:

27. **Un cursor de ratón** en el escritorio. La grabación va sin cursor (`toque: false`) y el toque se marca con la misma marca del celular.
28. **Leer cada paso del asistente.** Los pasos 2 a 5 pasan a uno por compás con la cámara quieta sobre la barra «Paso N de 5»: no se para
    a leer los campos ni se mueve la cámara en cada paso.
29. **Esconder el salto de tiempo del examen** con un fundido, un «más tarde» o un texto propio. El corte del 1530 muestra el reloj en
    «0:01» (venía en ≈ «0:4x») y el del 1545, «La evaluación cerró. Calculando tu nota…»: lo dice la app.
30. **Una transición que no sea de la serie.** Solo látigo (vertical entre celulares, horizontal entre escenarios), iris desde el toque
    (375, 660, 900) y dip + corte al cierre. Nunca un fundido entre mundos, nunca un zoom a través de un botón.
31. **El escritorio a menos de 1,8** en un encuadre de lectura, o a más de 2,0 en cualquiera.
32. **Dibujar el QR o el PDF del certificado.** Lo que se muestra es la página real `/verificar`; el QR lo menciona la propia app («o lee su
    QR con la cámara»).
33. **Cambiar la frase del sitio** («Forma a los líderes que tu visión necesita») o el lema y el llamado del cierre.
34. **Un fundido de música** en la costura o al final, o un segundo corte. La pista suena entera desde el 22,01 y termina sola.
35. **Las frases viajando con el látigo horizontal.** Salen con blur en su escenario y entran en el otro.
36. **Un número que no está en la grabación** (la nota, los inscritos, las cifras del tablero) dibujado o resaltado encima; y **una cifra
    sin «Datos de ejemplo»** a la vista.
37. **La ventana del escritorio con un marco de navegador** (barra de direcciones, pestañas) o la del celular con la barra de estado de un
    teléfono. Las ventanas son las del kit y nada más.

---

## 2. Los planos, cuadro por cuadro

### 2.0 Convenciones

- **Grabaciones:** **K** = la del clip (`assets/grabaciones/clase/grabacion.mp4`, 1170×2532, 95,07 s; sus cuadros como en el REVIEW del
  clip); **C** = la nueva de celular (`assets/grabaciones/celular/`, escena §3.2); **E** = la nueva de escritorio
  (`assets/grabaciones/escritorio/`, escena §3.3). «C·nota» = el tramo `nota` de C en su `pasos.json`; «+N» = N cuadros después de la acción
  de ese paso.
- **Niveles:** G, G⁺, M, C (celular) y D, D⁺ (escritorio), de §1.5. «Sobre X» = la caja de X (`pasos.json` → `caja`, px CSS) centrada en lo
  visible. **«(real)»** = la caja no se conoce hasta grabar: se toma de `pasos.json` o del cuadro y se anota en el REVIEW.
- **Pulso:** el cuadro de §0.3; un evento «en el 1380» se ve en el 1380 y suena en el 1381.
- **Mundos y ranuras.** La tira vertical del celular (`#tira`, dentro de `#ventana-cel`) tiene **dos ranuras** de 1000 px, como quedó el
  clip: **m1** (y 0) y **m2** (y −1000). Cada mundo tiene su cámara y su contenido se cambia solo cuando la ranura está fuera de cuadro:

  | Ranura | 0–365 | 365–1600 | 1600–2050 | 2050–2760 |
  |---|---|---|---|---|
  | m1 | el profesor (K: T1 y T3), cámara `#cam1` | — | **el profesor en la sábana** (C·sabana…final), `#cam5` | **la verificación** (C·verificar…buscar), `#cam6` |
  | m2 | la alumna (K: T2, 100–245) y quien coordina (K: T5–T7, desde el 340), `#cam2` / `#cam3` | quien coordina hasta el 850; **la alumna en el examen** desde el 1300 (C·examen…nota), `#cam4` | — | — |

  La ventana del escritorio tiene dos mundos apilados en el mismo lugar (sin tira): **e1** el asistente (E·catalogo…publicar, `#camE1`,
  visible 830–1320) y **e2** el tablero (E·tablero…ficha, `#camE2`, visible 2030–2280).
- Las frases, siempre en el lugar de su escenario (§1.4); una a la vez; la ceja encima.

### 2.1 Parte 1 (0–839): el clip en 16:9

Se copia `clip-sitio-academia/index.html` y se cambia **solo** esto:

1. **Formato:** raíz 1920×1080, `data-duration="97"`. `#ventana` del clip → `#ventana-cel` con `.k-ventana-16x9` dentro de `#escena`;
   `window.KD` de §1.4 (`W` 720, `HV` 900, `K` 0,615385, `PPC` 1,846, `VH` 1558,15, látigo vertical **1000**). Las marcas de toque siguen
   en `calc(px * var(--f-k))` con el `--f-k` nuevo.
2. **Los mismos 22 tramos de video** (v01–v22), con sus mismos `data-start`, `data-duration` y `data-media-start`, desde
   `assets/grabaciones/clase/grabacion.mp4`. Mismos cortes, mismos iris (375 y 660), mismos látigos (110–120 arriba, 230–240 abajo,
   350–360 arriba) y mismos aterrizajes.
3. **Las mismas cámaras** con `s' = max(s, 1,085)`:

   | Encuadre del clip | s del clip | s en 16:9 | (cx, cy) |
   |---|---|---|---|
   | E1.codigo | 1 | **1,085** | 195 · 279,5 |
   | E1.contador | 1 | **1,085** | 195 · 624,5 |
   | E1.catorce | 1,08 | **1,085** | 195 · 383 |
   | E1.dieciseis | 1,4 | 1,4 | 147 · 428 (alineado a la izquierda, igual que el clip) |
   | E2.casillas · E2.listo | 1,2 | 1,2 | 195 · 355 · 195 · 330 |
   | E3.tarjeta | 1,08 | **1,085** | 195 · 265 |
   | E3.lista | 1,1 | 1,1 | 190 · 205 |
   | E3.barra | 1 | **1,085** | 195 · 624,5 |
   | E3.dialogo | 1,15 | 1,15 | 190 · 421 |
   | E3.aviso | 1,08 | **1,085** | con su `y` especial: `HV − s·(VH + 34·PPC)` (el aviso por encima de «Datos de ejemplo») |
   | E3.certs | 1,12 | 1,12 | 190 · 190 |
   | E3.cert | 1 | **1,085** | 195 · 372 |
   | E3.nombre (punch 675) | 1,35 | 1,35 | 195 · 405 |
   | E3.codigo (720) | 1,04 | **1,085** | 195 · 633 (ya no hay ventana a escala 0,92 en este punto) |

   El ancho visible es el mismo del clip a la misma s (390 / s px CSS) y el alto, 11 % mayor: todos los encuadres del clip caben.
4. **Las frases** van a la columna izquierda (§1.4): la 1 y la 2 igual que en el clip; **la 3 se queda hasta el 837** (sale 837–841, con
   el látigo horizontal); la 4 del clip (la del sitio) **no va aquí**: pasa al 2520. La ceja entra en el 195 como en el clip y se queda.
5. **Se quitan:** la ventana a un lado del 724–738, la `subida` del 26,53, el dip del 837–839, la firma del 840 y su sonido de marca.
6. **Del 720 al 839:** la cámara va a E3.codigo en el 720–733 («por haber terminado…» hasta «Copiar el enlace para verificarlo» con
   **«Código de verificación · 7YU79-NNB7A»** a la vista) y se queda. El código queda en pantalla 3,6 s: es el dato que vuelve en el 2310.

### 2.2 Parte 2 (840–2909): tabla maestra

| Cuadro | Pulso | La app (grabación) | Cámara | Texto | Sonido | Transición |
|---|---|---|---|---|---|---|
| 830–840 | | m2 (el certificado) sale a la izquierda con `#escena`; e1 llega desde la derecha: E·catalogo, «Cursos» con «Nuevo curso» | e1 llega en **D** sobre «Nuevo curso» y la cabecera del catálogo (real) | frase 3 sale 837–841; la ceja sale 837–840 | `desliz` acento 841 (1,4) | **Látigo horizontal a la izquierda**; e1 aterriza 1,04 → 1,00 (840–850); halo |
| **840** | ● 1,00 | E·catalogo quieto | D | ceja arriba (`entrada-linea`, 842–848); «Un · curso, · en · cinco · pasos.» 843 · 845 · 847 · 849 · 851 | | |
| 870 | ● | toque «Nuevo curso» (E·nuevo, la acción) | quieta | | `toque` a | marca de toque |
| 885 | ● | corte en la espera: las opciones para empezar, con «En blanco» (E·nuevo +15) | quieta | | | |
| **900** | ● 0,84 | toque «En blanco» (E·paso-1, la acción) | 900–913 → **D** sobre `#cu-avance` y `#cu-nombre` (real) | | `toque` b | **iris** desde «En blanco» (900–905): debajo, el cuadro de las opciones |
| 905–959 | | dentro del iris, corte en la carga: «Paso 1 de 5 · Datos, modalidad y visibilidad», la barra con 1 de 5; **915–955: «Matrimonios fuertes» se escribe a 1×** (E·nombre); 955–959 quieto | quieta desde el 913 | | — | |
| **960** | ● 0,92 | corte: el primer cuadro de «Paso 2 de 5 · Materias y clases» (E·paso-2 +4) | **quieta en el mismo encuadre** (`#cu-avance` y lo de arriba del paso) | | `toque` c (fuera de cuadro) | — (la costura de la música cae aquí) |
| 960–1019 | | E·paso-2 desde la primera tecla de «Comunicación» a **2×**: «Comunicación» → «Escuchar con amor» → «Hablar con verdad» | quieta | | | |
| 1020 | ● | corte: el paso 2 completo (E·paso-2, el último cuadro antes de «Siguiente»): «Comunicación» con sus dos clases y «Finanzas en casa» con «El presupuesto familiar» | quieta | | | |
| **1080** | ● 0,76 | corte: «Paso 3 de 5 · Actividades y pesos», ya repartido (E·paso-3, después del último «Repartir») | quieta | | `toque` a | |
| **1140** | ● 0,75 | corte: «Paso 4 de 5 · Criterios de aprobación» con la asistencia mínima marcada (E·paso-4, después de marcar) | quieta | | `toque` b | |
| **1200** | ● 0,67 | corte: «Paso 5 de 5 · Logro y prerrequisito» (E·paso-5) | quieta | | `toque` c | |
| 1230 | ● | quieto | 1230–1243 → **D** sobre el pie: «Guardar borrador» y **«Publicar»** (real) | | | |
| **1260** | ● | toque «Publicar» (E·publicar, la acción) | quieta | | `toque` a | marca |
| 1275 | ● | corte en la espera: el diálogo **«¡Publicado!» · «Ya puedes abrir un grupo: su horario, sus fechas y quién lo dicta.»** (E·publicar +N, real) | 1275–1288 → **D** sobre el diálogo | | `confirmacion` | |
| 1310–1320 | | e1 sale a la derecha; vuelve el celular con **m2 = la alumna** (C·examen) | m2 llega en **G** sobre la pregunta (real) | frase 4 y ceja salen 1317–1320 | `desliz` | **Látigo horizontal a la derecha**; aterriza 1320–1330; halo |
| **1320** | ● 0,93 | C·examen: «Quiz de los evangelios» · **«Pregunta 1 de 3»** · el reloj de su ventana (≈ «0:5x», real) · «¿Cuántos evangelios hay en el Nuevo Testamento?» · A Tres · B Cuatro · C Cinco | G | ceja a la izquierda (1322–1328); «Exámenes · que / se · califican · solos.» 1322 · 1324 · 1326 · 1328 · 1330 | | |
| **1380** | ● 0,90 | toque «B · Cuatro» (C·p1): la opción se marca y «Respuesta guardada» | quieta | | `toque` b | marca (3 cuadros: la pantalla cambia) |
| **1395** | ● 0,89 | toque «Siguiente» (C·p1-sig) | quieta | | `toque` c | marca |
| 1410 | ● | corte en la espera: **«Pregunta 2 de 3»** · «El evangelio de Lucas lo escribió un médico.» · Verdadero · Falso | quieta | | | |
| **1440** | ● 0,96 | toque «Verdadero» (C·p2) | quieta | | `toque` a | marca |
| 1455 | ● | toque «Siguiente» (C·p2-sig) | quieta | | `toque` b | marca |
| 1470 | ● | corte: **«Pregunta 3 de 3»** · «¿Quién escribió la mayoría de las cartas del Nuevo Testamento?» · Pedro · Juan · Pablo · Santiago | quieta | | | |
| **1500** | ● 0,88 | toque «C · Pablo» (C·p3) | quieta | | `toque` c | marca |
| 1515 | ● | toque «Revisar» (C·revisar) | quieta | | `toque` a | marca |
| 1530 | ● | corte **con el salto de tiempo a la vista**: la vista «todas» —**«Respondiste 3 de 3»** y **«No hay que entregar: lo que tengas marcado a las {hora} es tu respuesta. Hasta esa hora puedes cambiarlo.»**— tomada de los **últimos 15 cuadros antes del cierre** (C·cierre), con el reloj de arriba en **«0:01»** (el toque de «Revisar» del 1515 lo dejó en ≈ «0:4x»: el reloj dice que pasó el tiempo) | 1530–1543 → **M** sobre el reloj y ese texto (real; si no caben juntos, el reloj manda y el texto se lee en G⁺) | | | |
| 1545 | ● | corte: el cuadro siguiente al cierre, **«La evaluación cerró. Calculando tu nota…»** (C·cierre; la app quita el reloj al llegar a cero y pide la nota a los 2 s) | quieta | | | |
| **1560** | ● 1,00 | corte en la espera: **«Tu nota · 5 / 5 · Alcanzó la nota mínima (3)»** (C·nota) | **punch** 1560–1568 → **C** sobre `#ev-nota` | | `confirmacion` (1,4) | |
| 1620 | ● 0,84 | C·nota, el `ver` a la lista (la app se desplaza: se usa el cuadro de después) | 1620–1633 → **G** sobre la lista: «1 · Correcta · 1 de 1 puntos» y «B Cuatro · Tu respuesta · La correcta» (real) | | | |
| 1670–1680 | | la tira baja: m1 = **el profesor en la sábana**, ya desplazada a la fila de la alumna (C·su-nota, después del `ver`) | m1 llega en **M** sobre la fila de la alumna con su **5** en la columna «Quiz de los evangelios» (real) | frase 5 sale 1677–1681 (la ceja se queda) | `desliz` | **Látigo vertical hacia abajo** (de vuelta al profesor); aterriza 1680–1690 |
| **1680** | ● 0,98 | C·su-nota quieto | M | «Sabes · quién / va · en · riesgo.» 1682 · 1684 · 1686 · 1688 · 1690 | | |
| 1740 | ● 0,79 | quieto | 1740–1753 → **G** sobre los filtros: «Todos · 18», «Cumple · N», «En riesgo · N», «No cumple · N» y el comienzo de la tabla (real) | | | |
| **1800** | ● *1,00* | toque «En riesgo» (C·en-riesgo): la tabla queda con los que están en riesgo | quieta | | `toque` b (1,4) · `aparicion` 1804 | marca |
| 1860 | ● | la tabla se corre de lado hasta «Final» (C·final: el desplazamiento suave de la app, ≈ 27 cuadros) | **quieta** (BANNED 24 del clip) | | `desliz` | |
| **1920** | ● *1,00* | quieto: la columna «Final» con el ícono del semáforo (⚠) y la nota de cada uno | 1920–1933 → **M** sobre la columna «Final» y los nombres fijos (real) | | | |
| 1980–2029 | | quieto | quieta | | | |
| 2030–2040 | | el celular sale a la izquierda; e2 llega: E·tablero | e2 llega en **D** sobre las cifras (real) | frase 6 y ceja salen 2037–2040 | `desliz` | **Látigo horizontal a la izquierda**; aterriza 2040–2050; halo |
| **2040** | ● *1,00* | E·tablero: las cifras del día («Grupos en curso», «Personas», «Asistencia», «Nota promedio», «En riesgo»…) | D | ceja arriba (2042–2048); «Toda · tu · escuela, · de · un · vistazo.» 2043 · 2045 · 2047 · 2049 · 2051 · 2053 | | |
| 2100 | ● | E·riesgo: la app baja a «Alumnos en riesgo» (su desplazamiento suave) | quieta, encuadrada desde el 2040 para que la lista entre en ella al bajar (real) | | | |
| **2160** | ● *1,00* | toque en la primera persona de la lista (E·ficha, la acción) | quieta | | `toque` c | marca |
| 2163–2175 | | la ficha académica entra desde la derecha (la animación real del panel) | — | | `aparicion` 2176 | |
| 2175 | ● *1,00* | quieto: la ficha (nombre, su semáforo y lo que le falta: «Asistencia: N % de 75 %», real) | 2175–2188 → **D** sobre el panel | | | |
| 2270–2280 | | e2 sale a la derecha; vuelve el celular con **m1 = `/verificar`** (C·verificar) | m1 llega en **G** sobre la cabecera y el formulario (real) | frase 7 y ceja salen 2277–2280 | `desliz` | **Látigo horizontal a la derecha**; aterriza 2280–2290; halo |
| **2280** | ● | C·verificar: el logo de Kingdom, **«Verificar un certificado»** · «Comprueba que un certificado de una iglesia en Kingdom es auténtico.» · «Código del certificado» · «Verificar» · «Escribe los 10 caracteres del código que trae el certificado (o lee su QR con la cámara).» | G | ceja a la izquierda (2282–2288); «Y · cualquiera / lo · verifica.» 2282 · 2284 · 2286 · 2288 | | |
| 2310–2333 | ● | **«7YU79-NNB7A» se escribe** a 1× (C·codigo) | quieta | | — | |
| **2340** | ● | toque «Verificar» (C·buscar, la acción) → «Buscando…» | quieta | | `toque` a | marca |
| **2400** | ● *0,76* | corte en la espera: **«Certificado válido»** · Nombre **Andrea Perea López** · Curso **Fundamentos bíblicos** · Iglesia (la de la demo) · Fecha · Código **7YU79-NNB7A** (C·buscar +N) | 2400–2413 → **M** sobre el sello y el nombre | | `confirmacion` (1,4) | |
| 2460 | ● | quieto | 2460–2473 → **G** sobre la tarjeta entera (el sello y los cinco datos) | | | |
| **2520** | ● *0,80* | quieto | quieta | la ceja sale 2520–2523; «Forma · a · los · *líderes* / que · tu · visión · necesita» 2519 · 2521 · … · 2533 (dos cuadros entre palabras) | | |
| 2524–2538 | | | | | | **La ventana a un lado**: 0,92, origen «100% 50%», x +24 |
| 2539–2756 | | quieto (C·buscar, el final de su pausa) | quieta | la frase sostenida 7,9 s | `subida` desde 90,533 | |
| 2757–2759 | | | | | | **dip** sobre la ventana |
| **2760** | ● | — | — | — | marca en 92,38 | **corte al cierre del Comercial** (`#escena` oculta) |

### 2.3 Los planos de la parte 2

#### P9 · «Un curso, en cinco pasos» — 840–1319 (compases 15–22)
El látigo horizontal es la puerta al escritorio: lo que era un grupo pasa a ser la escuela. La cámara se fija en D sobre la barra «Paso N
de 5» desde el 913 y **no se mueve hasta el 1230**: lo que se mueve es la app (el nombre que se escribe, las materias a 2×) y la barra, que
gana un segmento en cada golpe (960, 1080, 1140, 1200). Los cortes caen en el primer cuadro de cada paso. 1230 lleva la cámara al pie para
que el toque de «Publicar» se vea; 1275, al diálogo «¡Publicado!». Lectura: el nombre del paso se lee en cada compás (≥ 1,5 s cada uno).

#### P10 · «Exámenes que se califican solos» — 1320–1679 (compases 23–28)
La alumna de la parte 1, ahora en su examen. **Tres respuestas en tres golpes** (1380 · 1440 · 1500), cada una con su «Siguiente» medio
pulso después; la cámara quieta en G (la pregunta, las opciones y el reloj caben). 1530: «No hay que entregar…» en M, con el reloj ya en
«0:01» —es la frase que explica el plano y el reloj dice que pasó el tiempo—. **1545: «La evaluación cerró. Calculando tu nota…»**;
**1560, en el golpe más fuerte de la parte 2: la nota**, con un
punch a C. 1620: la lista de las tres «Correcta».

#### P11 · «Sabes quién va en riesgo» — 1680–2029 (compases 29–34)
El látigo baja al profesor, como en la parte 1 (abajo = de vuelta al profesor). **El primer cuadro es la fila de la alumna con su 5 en la
columna del quiz**: el dato viajó. 1740: la cámara sube a los filtros; **1800, el primer golpe del clímax: «En riesgo»** y la tabla se queda
con los que están en riesgo. 1860: la app corre la tabla hasta «Final» con la cámara quieta; 1920: M sobre los íconos del semáforo.

#### P12 · «Toda tu escuela, de un vistazo» — 2040–2279 (compases 35–38)
Segundo viaje al escritorio, a la segunda frase del clímax. Las cifras del tablero en D (2040); la app baja a «Alumnos en riesgo» (2100) con
la cámara quieta; **2160: toque en la primera persona** y su ficha entra por la derecha (la animación de la app); 2175: D sobre la ficha, que
dice qué le falta. Del grupo a la escuela y de la escuela a una persona.

#### P13 · «Y cualquiera lo verifica» — 2280–2519 (compases 39–42)
De vuelta al celular, pero ya no es de nadie de la iglesia: la página pública, sin menú ni cuenta. El código que se vio en el certificado de
Andrea (720–839) **se escribe** (2310) y **«Certificado válido»** llega en el 2400 con su nombre y su curso. La salida de la música baja sola:
el plano es tranquilo a propósito.

#### P14 · La frase del sitio y el cierre — 2520–2909
«Forma a los *líderes* que tu visión necesita» palabra a palabra en el 2520; la ceja se va; la ventana se hace a un lado (2524–2538) y todo
queda quieto salvo el halo; la `subida` empieza en el 90,533 y su golpe cae con el cierre. Dip 2757–2759. **2760: `cierre-comercial`**:

```html
<div id="cierre-comercial" data-composition-id="cierre-comercial" data-composition-src="identidad/cierre-comercial.html"
  data-variable-values='{"publico":"iglesia","llamado":"prueba","contacto":"sitio","fondo":"noche","idioma":"es"}'
  data-start="92" data-duration="5" data-track-index="6" data-width="1920" data-height="1080"></div>
<audio id="marca-cierre" src="identidad/audio/sonido-marca.wav" data-start="92.38" data-duration="2.1" data-track-index="26" data-volume="1"></audio>
```

---

## 3. Las grabaciones

### 3.1 Lo que se reusa

- **La grabación del clip, entera y sin cambios:** `clip-sitio-academia/assets/grabaciones/grabacion.mp4` (1170×2532, 30 fps, 95,07 s) y su
  `pasos.json` → `recorrido-academia/assets/grabaciones/clase/`. Se usan los mismos 22 tramos (§2.1); nada de la parte 1 se vuelve a grabar.
- **Los sonidos del clip:** `clip-sitio-academia/assets/audio/toque-b.wav` y `toque-c.wav` → `recorrido-academia/assets/audio/`.
- **El kit:** `npm run kit` (monta `identidad/` con `cierre-comercial.html`, los sonidos de acción y el sonido de marca); `frame.md` =
  `identidad/frame-comercial.md`.

Dos escenas nuevas, una por dispositivo, sobre Kingdom Demo en español, con `capturar.mjs --modo video` y `toque: false`:

```bash
cd tools/ayuda
node capturar.mjs clips/recorrido-academia-celular --idioma es --modo video      # → salida/video/es/clips/recorrido-academia-celular/
node capturar.mjs clips/recorrido-academia-escritorio --idioma es --modo video   # → salida/video/es/clips/recorrido-academia-escritorio/
# cada una: grabacion.mp4 + pasos.json; se copian a recorrido-academia/assets/grabaciones/celular/ y …/escritorio/
```

Lo que la herramienta ya hace y las escenas usan (sin nada nuevo): `como` e `ir` del primer paso antes de grabar; `como` a mitad de la
escena (otra cuenta); `escribir` a 70 ms por tecla; `ver` con desplazamiento suave; `marcar`; `clicSiHay` (espera 3 s); `pausa` sin tope en
video; `sql` tras restaurar el volcado; `refs` con `{@nombre}` (se consultan una vez, en orden, justo antes de abrir Chrome, con el cliente
de MariaDB: una ref puede llevar dos sentencias, `UPDATE …; SELECT …`, y vale la primera columna de la primera fila).

### 3.2 La escena de celular: `tools/ayuda/escenas/clips/recorrido-academia-celular.mjs`

```js
// Grabación para el RECORRIDO de Academia (LegacyHyperframes/videos/kingdomapp/recorrido-academia/SPEC.md §3.2): la parte 2 en CELULAR.
// NO es una escena de un artículo de la ayuda: no se publica ni entra en la frescura. Una sola escena de CELULAR (390×844 a 3x =
// 1170×2532, 30 cps) grabada SIN el círculo del toque (`toque: false`): el montaje dibuja el suyo sobre las cajas y los toques de pasos.json.
//   node capturar.mjs clips/recorrido-academia-celular --idioma es --modo video
//   → salida/video/es/clips/recorrido-academia-celular/grabacion.mp4 + pasos.json
// Tres tramos, en este orden (el primero depende del reloj):
//   1. examen (104, la alumna de «Fundamentos bíblicos»): presenta el «Quiz de los evangelios» en SU PROPIA ventana, que cierra 75 s después
//      de la última referencia; responde las tres bien, «Revisar», y espera el cierre: la app la califica sola y muestra «Tu nota».
//   2. sabana (103, el profesor del grupo): la sábana de notas con la nota recién llegada, el filtro «En riesgo» y la columna «Final».
//   3. verificar (la página pública /verificar: sin menú ni cuenta a la vista): escribe el código del certificado de la parte 1 y llega
//      «Certificado válido».
// Estado previo por SQL: (a) el intento de la alumna en el quiz se borra (con sus respuestas y su nota) y se crea uno nuevo, sin responder,
// con las tres preguntas en el orden del banco y sin barajar; (b) el primer certificado de Kingdom Demo pasa a ser el de la parte 1 del video
// (el código, el nombre, el curso y la fecha que se ven en la grabación del clip: clip-sitio-academia/REVIEW.md §2).
const GRUPO = `(SELECT g.id FROM ac_grupos g JOIN ac_cursos c ON c.id = g.id_curso
                JOIN ac_inscripciones i ON i.id_grupo = g.id JOIN kd_usuario_sedes us ON us.id_persona = i.id_persona AND us.id_usuario = 104
                WHERE c.con_notas = 1 AND g.estado = 'en_curso' ORDER BY g.id LIMIT 1)`;
const ALUMNA = `(SELECT id_persona FROM kd_usuario_sedes WHERE id_usuario = 104 AND estado = 'activo' LIMIT 1)`;
// El «Quiz de los evangelios» de la copia del grupo: la primera evaluación por orden (la segunda es el «Examen final»).
const QUIZ = `(SELECT a.id FROM ac_actividades a WHERE a.id_grupo = ${GRUPO} AND a.tipo = 'evaluacion' ORDER BY a.orden, a.id LIMIT 1)`;
const PREGUNTA = n => `(SELECT ep.id_pregunta FROM ac_evaluacion_preguntas ep WHERE ep.id_actividad = ${QUIZ}
                        ORDER BY ep.orden, ep.id_pregunta LIMIT 1 OFFSET ${n})`;
// El índice ORIGINAL de la opción correcta (el de data-opcion: las opciones se muestran en su orden porque el quiz queda sin barajar).
const CORRECTA = n => `SELECT JSON_VALUE(p.correctas, '$[0]') FROM ac_preguntas p WHERE p.id = ${PREGUNTA(n)}`;
// Lo que se ve en el certificado de la parte 1 (la grabación del clip, cuadro 2516): se copia tal cual.
const CERT = { codigo: '7YU79NNB7A', legible: '7YU79-NNB7A', persona: 'Andrea Perea López', curso: 'Fundamentos bíblicos', fecha: '2026-10-30' };

export default {
  articulo: 'clips/recorrido-academia-celular',
  movil: true,
  toque: false,
  pantallas: [
    'frontend-v2/src/app/pages/academia/evaluacion.page.ts',
    'frontend-v2/src/app/pages/academia/presentar-pregunta.component.ts',
    'frontend-v2/src/app/pages/academia/resultado-evaluacion.component.ts',
    'frontend-v2/src/app/pages/academia/grupo.page.ts',
    'frontend-v2/src/app/pages/academia/notas/notas-grupo.component.ts',
    'frontend-v2/src/app/pages/verificar/verificar.page.ts',
  ],
  sql: [
    // (a) La alumna presenta el quiz AHORA. Fuera su intento de la semilla (sus respuestas se van en cascada) y su nota; el quiz sin barajar
    // (preguntas y opciones en el orden del banco: las respuestas de abajo van por el índice original); un intento nuevo, sin responder,
    // con SU PROPIA ventana (acEvalVentanaDe), abierta desde hace un minuto. La hora de cierre la fija la última referencia (`cierre`).
    `DELETE FROM ac_intentos WHERE id_actividad = ${QUIZ} AND id_persona = ${ALUMNA}`,
    `DELETE FROM ac_notas WHERE id_actividad = ${QUIZ} AND id_persona = ${ALUMNA}`,
    `UPDATE ac_evaluaciones SET aleatorio = 0 WHERE id_actividad = ${QUIZ}`,
    `INSERT INTO ac_intentos (id_actividad, id_persona, numero, abre_at, cierra_at, preguntas)
     SELECT ep.id_actividad, ${ALUMNA}, 1, UTC_TIMESTAMP() - INTERVAL 1 MINUTE, UTC_TIMESTAMP() + INTERVAL 30 MINUTE,
            CONCAT('[', GROUP_CONCAT(ep.id_pregunta ORDER BY ep.orden, ep.id_pregunta), ']')
       FROM ac_evaluacion_preguntas ep WHERE ep.id_actividad = ${QUIZ} GROUP BY ep.id_actividad`,
    // (b) El certificado de Andrea (parte 1) existe y se puede verificar: el primero de Kingdom Demo (de un grupo ya cerrado) toma su código,
    // su nombre, su curso y su fecha. La iglesia queda la suya (la misma de la parte 1). Datos ficticios.
    `UPDATE ac_certificados SET codigo = '${CERT.codigo}', nombre_persona = '${CERT.persona}', nombre_curso = '${CERT.curso}',
            fecha = '${CERT.fecha}', anulado_at = NULL
      WHERE id = (SELECT id FROM (SELECT c.id FROM ac_certificados c JOIN kd_sedes s ON s.id = c.id_sede
                                   WHERE s.codigo = 'KDEMO' ORDER BY c.id LIMIT 1) x)`,
  ],
  refs: {
    grupo: `SELECT ${GRUPO}`,
    alumna: `SELECT ${ALUMNA}`,
    quiz: `SELECT ${QUIZ}`,
    p1: `SELECT ${PREGUNTA(0)}`,
    p2: `SELECT ${PREGUNTA(1)}`,
    p3: `SELECT ${PREGUNTA(2)}`,
    c1: CORRECTA(0),
    c2: CORRECTA(1),
    c3: CORRECTA(2),
    cert: `SELECT COUNT(*) FROM ac_certificados WHERE codigo = '${CERT.codigo}' HAVING COUNT(*) = 1`,   // sin fila: la escena no arranca
    // ÚLTIMA (las refs corren en orden, justo antes de abrir Chrome): la ventana de la alumna cierra 75 s después de esta consulta. La
    // grabación empieza ≈ 10–20 s después; responder lleva ≈ 12 s; el resto se espera en el tramo `cierre` y se recorta en el montaje.
    cierre: `UPDATE ac_intentos SET abre_at = UTC_TIMESTAMP() - INTERVAL 1 MINUTE, cierra_at = UTC_TIMESTAMP() + INTERVAL 75 SECOND
              WHERE id_actividad = ${QUIZ} AND id_persona = ${ALUMNA} AND numero = 1;
             SELECT IF(ROW_COUNT() = 1, 1, NULL)`,
  },
  pasos: [
    // ── 1. La alumna (104) presenta el quiz (P10). La entrada se hace antes de grabar: el video abre en «Pregunta 1 de 3».
    { tramo: 'examen', como: 104, ir: '/servir/academia/evaluacion/{@quiz}', espera: '.pregunta[data-pregunta="{@p1}"]' },
    { clicSiHay: '#ev-aviso-5 .cerrar-aviso', pausa: 2500 },                                   // fuera de cámara: el aviso de los 5 minutos
    { tramo: 'p1', clic: '.pregunta[data-pregunta="{@p1}"] [data-opcion="{@c1}"]', pausa: 1000 },        // «Cuatro» (1380)
    { tramo: 'p1-sig', clic: '#ev-siguiente', espera: '.pregunta[data-pregunta="{@p2}"]', pausa: 1200 },  // 1395 → 1410
    { tramo: 'p2', clic: '.pregunta[data-pregunta="{@p2}"] [data-opcion="{@c2}"]', pausa: 1000 },        // «Verdadero» (1440)
    { tramo: 'p2-sig', clic: '#ev-siguiente', espera: '.pregunta[data-pregunta="{@p3}"]', pausa: 1200 },  // 1455 → 1470
    { tramo: 'p3', clic: '.pregunta[data-pregunta="{@p3}"] [data-opcion="{@c3}"]', pausa: 1000 },        // «Pablo» (1500)
    { tramo: 'revisar', clic: '#ev-siguiente', espera: '#ev-todas', pausa: 2000 },                       // «Respondiste 3 de 3 · No hay que entregar…» (1530)
    // El cierre: el reloj baja hasta «0:01» en la vista «Respondiste 3 de 3», «La evaluación cerró. Calculando tu nota…» y la nota (la app
    // la pide sola a los 2 s). Se espera de sobra: lo que sobra se recorta (1530, 1545 y 1560 salen de aquí).
    { tramo: 'cierre', pausa: 70000 },
    { tramo: 'nota', espera: '#ev-nota-valor', pausa: 2500 },                                           // «Tu nota · 5 / 5» (1560)
    { ver: 'app-ac-resultado-evaluacion ol.lista', bloque: 'start', pausa: 2500 },                       // las tres «Correcta» (1620)

    // ── 2. El profesor (103): la sábana del grupo (P11).
    { tramo: 'sabana', como: 103, ir: '/servir/academia/grupo/{@grupo}', espera: '#tab-grupo-notas' },
    { clic: '#tab-grupo-notas', espera: '#no-sabana', pausa: 600 },
    { tramo: 'su-nota', ver: '#no-sabana tr[data-persona="{@alumna}"] td[data-actividad="{@quiz}"]', pausa: 2800 },   // el 5 de la alumna (1680)
    { tramo: 'en-riesgo', clic: '#no-f-en_riesgo', pausa: 2200 },                                        // el filtro (1800)
    { tramo: 'final', ver: '#no-sabana tbody tr:first-child td.col-final', pausa: 5500 },                // la columna «Final» (1860–2029)

    // ── 3. Cualquiera verifica el certificado (P13): la página pública, sin menú.
    { tramo: 'verificar', ir: '/verificar', espera: '#ver-codigo', pausa: 1800 },
    { tramo: 'codigo', escribir: { en: '#ver-codigo', texto: CERT.legible }, pausa: 600 },               // 2310–2333
    { tramo: 'buscar', clic: '#ver-buscar', espera: '#ver-resultado[data-estado="valido"]', pausa: 13000 },   // 2340 → 2400 → hasta el 2759
  ],
};
```

**Comprobaciones obligatorias al grabar** (si una falla, se vuelve a grabar):
1. En `pasos.json`, el tramo `revisar` termina **antes** de que empiece el cierre: entre la acción de `revisar` y el primer cuadro con
   «Calculando tu nota…» hay al menos 3 s, y el cuadro anterior a ese muestra la vista «Respondiste 3 de 3» con el reloj en «0:01». Si la alumna no alcanzó a responder antes del cierre (la máquina tardó más de 60 s en abrir
   Chrome), se sube el `INTERVAL 75 SECOND` a 120 y la `pausa` del cierre a 110000.
2. «Tu nota» dice **5 / 5** (las tres correctas). Si dice otra cosa, el índice de alguna opción no es el del banco: se revisan `c1`–`c3`.
3. En la sábana, la celda de la alumna en la columna del quiz dice **5** en el cuadro del `ver` de `su-nota`.
4. La verificación muestra **Andrea Perea López · Fundamentos bíblicos · 7YU79-NNB7A** y la **fecha que se ve en el certificado de la
   parte 1** (cuadro 2516 de la grabación del clip). Si la fecha del clip es otra, se cambia `CERT.fecha` y se graba otra vez.

### 3.3 La escena de escritorio: `tools/ayuda/escenas/clips/recorrido-academia-escritorio.mjs`

```js
// Grabación para el RECORRIDO de Academia (LegacyHyperframes/videos/kingdomapp/recorrido-academia/SPEC.md §3.3): la parte 2 en ESCRITORIO.
// NO es una escena de un artículo de la ayuda. En video el escritorio es 1280×720 a 1,5x (1920×1080 reales, 30 cps), sin cursor ni círculo
// (`toque: false`): el montaje dibuja su marca de toque sobre las cajas de pasos.json.
//   node capturar.mjs clips/recorrido-academia-escritorio --idioma es --modo video
//   → salida/video/es/clips/recorrido-academia-escritorio/grabacion.mp4 + pasos.json
// Una cuenta: 101, el administrador, que coordina Academia.
//   1. curso (P9): el asistente de 5 pasos crea «Matrimonios fuertes» y lo publica (los pasos de escenas/academia/crear-un-curso.mjs,
//      con pausas largas en cada resultado, que el montaje recorta).
//   2. tablero (P12): el tablero de Academia, «Alumnos en riesgo» y la ficha académica de la primera persona.
// Sin estado previo: todo sale de Kingdom Demo; el curso lo crea la escena.
export default {
  articulo: 'clips/recorrido-academia-escritorio',
  toque: false,
  pantallas: [
    'frontend-v2/src/app/pages/academia/cursos.page.ts',
    'frontend-v2/src/app/pages/academia/curso.page.ts',
    'frontend-v2/src/app/pages/academia/curso-empezar.component.ts',
    'frontend-v2/src/app/pages/academia/curso-datos.component.ts',
    'frontend-v2/src/app/pages/academia/curso-estructura.component.ts',
    'frontend-v2/src/app/pages/academia/curso-pesos.component.ts',
    'frontend-v2/src/app/pages/academia/curso-criterios.component.ts',
    'frontend-v2/src/app/pages/academia/curso-logro.component.ts',
    'frontend-v2/src/app/pages/academia/tablero.page.ts',
    'frontend-v2/src/app/pages/academia/seguimiento/tablero-riesgo.component.ts',
    'frontend-v2/src/app/pages/academia/seguimiento/ficha-academica.component.ts',
  ],
  pasos: [
    // ── 1. El asistente (P9). La entrada se hace antes de grabar: el video abre en el catálogo de cursos.
    { tramo: 'catalogo', como: 101, ir: '/servir/academia', espera: '#btn-nuevo-curso', pausa: 1800 },   // 830–869
    { tramo: 'nuevo', clic: '#btn-nuevo-curso', espera: '#btn-empezar-blanco', pausa: 1000 },             // 870 → 885
    { tramo: 'paso-1', clic: '#btn-empezar-blanco', espera: '#cu-nombre', pausa: 800 },                   // 900 → 905
    { tramo: 'nombre', escribir: { en: '#cu-nombre', texto: 'Matrimonios fuertes' }, pausa: 800 },       // 915–955
    { escribir: { en: '#cu-descripcion', texto: 'Para parejas: comunicación, finanzas y fe en casa.' } },
    { clic: '#cu-categoria' },
    { clic: 'mat-option >> nth=1', oculto: '.cdk-overlay-pane mat-option' },
    { clic: '#cu-modalidades [data-modalidad="presencial"]' },
    { clic: '#cu-visibilidades [data-visibilidad="abierto_aprobacion"]', pausa: 800 },
    { tramo: 'paso-2', clic: '#btn-cu-siguiente', espera: '#cu-nueva-materia', pausa: 800 },            // 960
    { escribir: { en: '#cu-nueva-materia', texto: 'Comunicación' } },
    { tecla: 'Enter' },
    { escribir: { en: '[data-nueva-clase="0"]', texto: 'Escuchar con amor' } },
    { tecla: 'Enter' },
    { escribir: { en: '[data-nueva-clase="0"]', texto: 'Hablar con verdad' } },
    { tecla: 'Enter' },
    { escribir: { en: '#cu-nueva-materia', texto: 'Finanzas en casa' } },
    { tecla: 'Enter' },
    { escribir: { en: '[data-nueva-clase="1"]', texto: 'El presupuesto familiar' } },
    { tecla: 'Enter', pausa: 2500 },                                                                    // 1020–1079: el paso 2 completo
    { tramo: 'paso-3', clic: '#btn-cu-siguiente', espera: '#cu-con-notas', pausa: 600 },
    { marcar: '#cu-con-notas' },
    { clic: '[data-agregar-actividad="0"]' },
    { clic: '.cdk-overlay-pane [data-tipo="nota"]', oculto: '.cdk-overlay-pane [data-tipo]' },
    { clic: '[data-agregar-actividad="1"]' },
    { clic: '.cdk-overlay-pane [data-tipo="evaluacion"]', oculto: '.cdk-overlay-pane [data-tipo]' },
    { clic: '#btn-repartir-materias' },
    { clic: '[data-repartir-materia="0"]' },
    { clic: '[data-repartir-materia="1"]', pausa: 2500 },                                               // 1080–1139
    { tramo: 'paso-4', clic: '#btn-cu-siguiente', espera: '#cu-cr-asistencia', pausa: 600 },
    { marcar: '#cu-cr-asistencia', pausa: 2500 },                                                       // 1140–1199
    { tramo: 'paso-5', clic: '#btn-cu-siguiente', espera: '#cu-logro', pausa: 2500 },                   // 1200–1259
    { tramo: 'publicar', clic: '#btn-cu-publicar', espera: 'mat-dialog-container', pausa: 3000 },       // 1260 → 1275–1319
    { clic: 'mat-dialog-actions button:not(#btn-confirm)', oculto: 'mat-dialog-container' },          // fuera de cámara: «Más tarde»

    // ── 2. El tablero (P12).
    { tramo: 'tablero', ir: '/servir/academia/tablero', espera: '#tab-cifras', pausa: 3000 },           // 2030–2099
    { tramo: 'riesgo', ver: '#tab-riesgo', bloque: 'start', pausa: 2500 },                              // 2100–2159
    { tramo: 'ficha', clic: '#tab-riesgo-lista button >> nth=0', espera: '.panel-ficha', pausa: 4000 },   // 2160 → 2175–2279
  ],
};
```

**Comprobaciones al grabar:** el diálogo «¡Publicado!» aparece (si la app pide algo que falta, el `#cu-faltas` lo dice y la escena se
detiene en la espera); el tablero muestra «Datos de hace N min» con un N de hoy (si el resumen de la demo es viejo, se toca «Actualizar»
antes de grabar: `{ clic: '#tab-actualizar' }` como primer paso del tramo `tablero`); la ficha entra por la derecha y no tapa el nombre en
la lista (si lo tapa, el encuadre del 2175 se centra en el panel y basta).

### 3.4 Selectores, verificados el 2026-10-30 en `frontend-v2/src/app/pages/`

- **Examen** (`academia/evaluacion.page.ts`): `#ev-cual` («Pregunta N de M»), `#ev-reloj`, `#ev-aviso-5` y su `.cerrar-aviso`,
  `#ev-siguiente` (en la última pregunta dice «Revisar» y abre la vista `#ev-todas`), `#ev-guardado`, `#ev-cerrando`; la ruta
  `/servir/academia/evaluacion/:id` (la usa `escenas/academia/mis-cursos.mjs`). **Pregunta** (`academia/presentar-pregunta.component.ts`):
  `.pregunta[data-pregunta]` y cada opción `button.opcion[data-opcion]` con el **índice original** de la opción. **Resultado**
  (`academia/resultado-evaluacion.component.ts`): `#ev-nota`, `#ev-nota-valor`, `#ev-aprobada`, `ol.lista`.
- **Sábana** (`academia/notas/notas-grupo.component.ts`): `#no-sabana`, `#no-f-cumple`, `#no-f-en_riesgo`, `#no-f-no_cumple`,
  `tbody tr[data-persona]`, `td[data-actividad]`, `td.col-final`; la pestaña `#tab-grupo-notas` (`academia/grupo.page.ts`, `'tab-grupo-' + s.id`;
  la usa `escenas/academia/notas-entregas-y-evaluaciones.mjs`).
- **Verificación** (`verificar/verificar.page.ts`, ruta pública `verificar` en `app.routes.ts`): `#ver-codigo` (acepta el código con guion,
  `maxlength` 13), `#ver-buscar`, `#ver-resultado[data-estado="valido"]`.
- **Asistente** (`academia/curso.page.ts` y sus componentes; todos los usa `escenas/academia/crear-un-curso.mjs`): `#btn-nuevo-curso`,
  `#btn-empezar-blanco`, `#cu-nombre`, `#cu-descripcion`, `#cu-categoria`, `#cu-modalidades [data-modalidad]`,
  `#cu-visibilidades [data-visibilidad]`, `#btn-cu-siguiente`, `#cu-nueva-materia`, `[data-nueva-clase]`, `#cu-con-notas`,
  `[data-agregar-actividad]`, `.cdk-overlay-pane [data-tipo]`, `#btn-repartir-materias`, `[data-repartir-materia]`, `#cu-cr-asistencia`,
  `#cu-logro`, `#btn-cu-publicar`, `#cu-avance` (la barra «Paso N de 5» con sus cinco segmentos). El diálogo de «¡Publicado!» es el de
  `components/app-dialog.component.ts`: `#btn-confirm` («Abrir un grupo») y el otro botón de `mat-dialog-actions` («Más tarde»).
- **Tablero** (`academia/tablero.page.ts` y `academia/seguimiento/`): `#tab-cifras`, `li[data-cifra]`, `#tab-riesgo`, `#tab-riesgo-lista`,
  `#tab-actualizar`; la ficha abre con la clase `.panel-ficha` (`ficha-academica.service.ts`); los usa `escenas/academia/tablero.mjs`.
- **SQL:** `ac_intentos` (`abre_at`, `cierra_at`, `preguntas` JSON; `ac_respuestas` en cascada), `ac_notas` (única por actividad y
  persona), `ac_evaluaciones.aleatorio`, `ac_evaluacion_preguntas` (`id_actividad`, `id_pregunta`, `orden`), `ac_preguntas.correctas`
  (JSON), `ac_certificados` (`codigo` CHAR(10) único, `nombre_persona`, `nombre_curso`, `nombre_iglesia`, `fecha`, `anulado_at`): migración
  `042_ac_academia.sql`. La verificación lee esas columnas tal cual (`acVerificar`, `backend/_datos/academia_graduaciones.php`).

### 3.5 El proyecto

`recorrido-academia/` con `BRIEF.md` (`tipo: comercial`, `subtipo: clip-del-sitio`, `recorrido: academia`, `aspect: 16:9`), `frame.md`
(= `identidad/frame-comercial.md`), `hyperframes.json` y `package.json` copiados del clip con dos scripts: `"kit"` y
`"musica"` (el `ffmpeg` de §0.1). `assets/grabaciones/{clase,celular,escritorio}/`, `assets/audio/` (toque-b y toque-c),
`assets/musica/product-launch-recorrido.wav`. Composiciones: `fondo`, `frase-1` … `frase-9`, `ceja` (con sus dos lugares); en la raíz,
`#escena` con las dos ventanas, los tramos de video, las cámaras, los iris, las marcas, el cambio de ventana, el dip, la música y los
sonidos. Si `check` avisa `composition_file_too_large`, se deja (como el clip) o cada mundo pasa a una subcomposición del tamaño de su
ventana; la línea de tiempo no cambia.

**Entregables:** `renders/recorrido-academia-16x9.mp4` (1920×1080, 30 fps, 2910 cuadros, H.264 + AAC 48 kHz, −16 LUFS) para YouTube y
presentaciones, y para la página `/academia` una versión **1280×720** (H.264 y WebM) con su póster (el cuadro 0) en AVIF y WebP. El tope de
1,5 MB del README es por clip de 30 s: el recorrido va en el sitio con `preload="none"` y el póster (lo decide la entrega del sitio).

---

## 4. Lo que se revisa en la vista previa

Cuadros a mirar: `npx hyperframes snapshot --at 0,1.5,4.0,6.0,8.0,12.5,16.0,20.1,22.8,24.5,27.9,28.0,28.4,29.0,30.5,31.9,32.0,34.0,36.0,38.0,40.0,42.0,42.6,43.9,44.0,44.5,46.0,46.6,48.0,50.0,51.0,51.5,52.0,52.4,54.5,55.9,56.0,56.5,58.5,60.0,60.2,62.9,64.5,67.9,68.0,68.5,70.0,72.0,72.6,73.5,75.9,76.0,76.5,77.8,78.0,80.0,80.5,82.5,84.0,84.5,90.0,91.9,92.0,92.4,96.9`,
y `snapshot --range` de 16 cuadros sobre cada látigo: 3.6–4.1, 7.6–8.1, 11.6–12.1, **27.6–28.1, 43.6–44.1, 55.6–56.1, 67.6–68.1, 75.6–76.1**.

1. **Parte 1 (0–27,9):** lo mismo que el §4 del clip (puntos 1–9), con la ventana del celular a la derecha y las frases a la izquierda; el
   texto de la app ≥ 28 px en todos los encuadres (el general a 1,085); la frase 3 quieta del 12,2 al 27,9; en el **24,5** el bloque
   «Código de verificación · 7YU79-NNB7A · Copiar el enlace para verificarlo» legible y la ventana a escala 1.
2. **Los látigos horizontales** (28,0 · 44,0 · 68,0 · 76,0): ningún cuadro con las dos ventanas vacías ni con una ventana a medio camino
   quieta; a la izquierda al escritorio, a la derecha de vuelta; la frase anterior ya no está en el golpe y la nueva empieza en el +2;
   la ceja cambia de lugar con blur, nunca se desliza.
3. **El asistente (28–44):** la barra «Paso N de 5» cambia de 1 a 5 en 31,9 → 32,0 → 36,0 → 38,0 → 40,0 y la cámara no se mueve entre el
   30,5 y el 41,0; «Matrimonios fuertes» se lee entero en el 31,9; el toque de «Publicar» en el 42,0 y «¡Publicado!» en el 42,6; texto
   ≥ 28 px (D = 1,8).
4. **El examen (44–56):** «Pregunta 1 de 3» y el reloj en el 44,5; cada opción marcada en el cuadro de su golpe (46,0 · 48,0 · 50,0);
   en el 51,0 «No hay que entregar…» legible **con el reloj en «0:01»**; en el 51,5 «La evaluación cerró. Calculando tu nota…»; **«Tu nota ·
   5 / 5» en el 52,0** con el punch terminado en el 52,3; «Correcta» tres veces en el 54,5.
5. **La sábana (56–68):** en el 56,5 la fila de la alumna con su **5** en la columna del quiz; los filtros legibles en el 58,5; en el 60,2 la
   tabla filtrada; la cámara quieta mientras la tabla se corre (62,0–62,9); en el 64,5 los íconos del semáforo y las notas a ≥ 36 px.
6. **El tablero (68–76):** las cifras con «Datos de ejemplo» a la vista; el toque del 72,0; la ficha entera en el 73,5.
7. **La verificación (76–92):** el código se escribe entre el 77,0 y el 77,8; «Certificado válido» con **Andrea Perea López · Fundamentos
   bíblicos · 7YU79-NNB7A** en el 80,0, legible (≥ 36 px el nombre en el 80,5); la frase del sitio entera en el 84,5 con *líderes* dorada y
   la ventana a 0,92; nada se mueve del 85,0 al 91,8 salvo el halo; dip 91,9; **92,0 el primer cuadro del cierre** sin noche vacía.
8. **La música (oída, no solo medida):** la costura del **32,0** no se oye (se escucha 28–36 con audífonos dos veces; si se oye, se prueba
   el corte a 20 ms y a 50 ms del golpe antes de tocar el lugar); el último acorde se apaga debajo del cierre sin cortarse; las campanas se
   oyen en el 92,38. `npx hyperframes beats assets/musica/product-launch-recorrido.wav`: la grilla de 0,5 s sigue sin un pulso doble ni uno
   perdido entre el 31,0 y el 33,0.
9. **Sonido (medido):** cada `toque` y cada `aparicion` un cuadro después de su imagen; los golpes de `hyperframes audio` sobre el render
   en los toques de §1.7; **−16 LUFS** integrada (±1), pico real ≤ −1 dBTP; ningún par de sonidos encimado salvo 1800 + 1803 y 2160 + 2175.
10. **Textos:** ninguna palabra que no esté en la app, en las nueve frases o en el cierre; las frases en sus líneas fijadas; «Datos de
    ejemplo» en cada ventana con cifras; `npx hyperframes check` en 0 errores.
11. **La historia sin sonido** (así se ve en el sitio hasta que se toca el botón): código en pantalla → la alumna lo escribe → el profesor lo
    ve → la lista de quién cumple → aprobado, con certificado → el código del certificado → un curso en cinco pasos → la alumna responde
    y el reloj cierra → su nota → su 5 en la sábana → quién va en riesgo → el tablero y la ficha de una persona → alguien escribe el código
    → «Certificado válido» → Kingdom.

---

## 5. Riesgos y lo que se decide al grabar

- **El cierre del examen depende del reloj.** La ventana propia cierra 75 s después de la última referencia; la grabación arranca unos
  10–20 s después y la alumna responde en ≈ 12 s. Si la máquina va lenta y el cierre llega antes del «Revisar», `pasos.json` lo muestra
  (comprobación 1 de §3.2): se sube el margen y se graba otra vez. Si el cliente de MariaDB de la herramienta no acepta dos sentencias en
  una ref (debería: es `mysql -e`), la ref `cierre` pasa al final de `sql:` con `INTERVAL 90 SECOND` y la `pausa` del cierre a 90000.
- **El aviso de los 5 minutos** aparece apenas abre el examen (la ventana es corta); la escena lo cierra fuera de cámara. Si se vuelve a
  abrir, la pantalla sigue siendo la real: se encuadra sin él o se anota.
- **El certificado de la parte 2 es una fila de la demo reescrita** para que coincida con el de la grabación del clip. Es ficticio como todo
  lo demás; la fecha se compara con el cuadro del clip (comprobación 4). Si algún día se vuelve a grabar la parte 1, el `CERT` de la escena
  se actualiza con lo que diga la nueva.
- **La alumna puede no salir en el filtro «En riesgo»** (su semáforo depende de su asistencia en la demo): no importa, el 5 se ve antes
  del filtro (1680) y el filtro muestra a quienes sí están en riesgo.
- **El escritorio se lee solo de cerca** (D = 1,8 deja ver 711 × 375 px CSS): cada encuadre (la barra de pasos, el pie, el diálogo, las
  cifras, la lista, la ficha) se elige con la grabación y se anota en el REVIEW. Si el pie del asistente queda fuera de la pantalla de
  720 px, el toque de «Publicar» se marca donde está en el cuadro real y la cámara del 1230 va ahí.
- **La escritura de las materias a 2×** es el único tramo acelerado; si a 2× se ve agitado, se corta en la pausa entre la primera materia y
  la segunda y todo va a 1×.
- **La costura de la música** está medida (§0.1), pero nadie la ha oído: es la primera cosa que se escucha en la vista previa (§4.8).
- **Densidad:** la parte 2 tiene un toque por pulso en 46–51 (seis toques en 5 s). Si en la vista previa va atropellado, la válvula es quitar
  el sonido de los dos «Siguiente» (1395 y 1455): la marca se queda y el toque de la respuesta lleva el ritmo.
- **El README pide 60–75 s para el recorrido**; este dura 97 por decisión del dueño (~100 s). Se anota en `KingdomApp/docs/videos/README.md`
  al publicar.
- **Idiomas (en, pt después):** las dos escenas con `--idioma en` graban la interfaz en inglés (el quiz y la sábana salen del banco en
  inglés de la demo); el `CERT` sigue lo que diga el clip en inglés cuando exista. Las frases se traducen y los saltos se vuelven a fijar; el
  cierre lleva `idioma`.
