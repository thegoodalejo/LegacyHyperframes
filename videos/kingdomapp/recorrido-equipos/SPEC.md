# SPEC · Recorrido de Equipos — «Falta uno en Parqueadero… y el domingo, cubierto» (16:9)

2026-10-30 · Contrato de construcción de la historia de [STORY.md](STORY.md). La parte 1 es el clip publicado
([clip-sitio-equipos](../clip-sitio-equipos/): su [SPEC](../clip-sitio-equipos/SPEC.md), su [REVIEW](../clip-sitio-equipos/REVIEW.md) y su
`index.html`), llevado a 16:9 sin reabrirlo; la parte 2 es nueva. Mismo método que [Academia](../recorrido-academia/SPEC.md) y
[Eventos](../recorrido-eventos/SPEC.md): cada adjetivo es un número, los valores por defecto están prohibidos con nombre y los planos van
cuadro por cuadro. Se construye desde aquí, se revisa contra esto y se cambia aquí cuando la vista previa cambie la película. «Igual que el
clip» = copiado de `clip-sitio-equipos/index.html` con los cambios de §2.1. «Igual que Academia» = copiado de
`recorrido-academia/SPEC.md` (el sistema de dos escenarios es el mismo).

```text
GOAL:    Un pastor que no conoce Kingdom termina pensando «veo antes del domingo qué falta en cada departamento, cada equipo se organiza
         en su chat, y servir le cuenta a cada persona en su crecimiento» y toca «Prueba gratis 30 días».
OUTPUT:  HyperFrames 0.8.221 · una composición 1920×1080 (16:9) · 30 fps. (La 9:16 queda para después; no se especifica aquí.)
TIME:    97,0 s = 2910 cuadros: cuerpo 0–92,0 (0–2759) + cierre del Comercial 92,0–97,0 (2760–2909). 120 BPM = 15 cuadros por pulso
         en todo el video (la costura conserva la grilla, §0).
LOOK:    la noche del sitio (#060D1F) con el halo y la retícula de puntos del kit; tinta #EAF0FF; un solo acento, el dorado #E8B95A, en
         tres lugares (la ceja «EQUIPOS», la palabra «cubierto» y el botón del cierre). Fraunces 560 84 px / −0,02 em para las frases;
         Inter para la ceja y «Datos de ejemplo». El medio: la app REAL de Kingdom Demo en dos ventanas del kit sobre la noche: el celular
         (`.k-ventana-16x9`, 720×900) y el escritorio (`.k-ventana-escritorio`, 1440×760); nunca un aparato dibujado.
OBJECTS: las dos ventanas; en el celular, dos mundos en la tira vertical (m1 = Jorge, m2 = Gabriela) y en el escritorio uno (e1 = la
         cobertura del administrador); el punto de toque; las nueve frases; la ceja; la píldora «Datos de ejemplo»; el cierre del
         Comercial. Nada más existe en el cuadro.
MOTION:  curvas por papel (§1.6); un movimiento de cámara por compás (14 cuadros, power2.inOut), quieta después y nunca mientras la app
         se desplaza; cada toque y cada corte en un pulso; cada cambio de mundo en un golpe (120 · 180 · 360 · 660 · 720 · 840 · 1320 ·
         1800 · 1920 · 2160 · 2280 · 2520 · 2760).
SHOTS:   catorce planos (§2.3).
BANNED:  §1.8.
QA:      §4.
```

---

## 0. La música: la edición y el reloj

### 0.1 La edición (la misma de Academia)

La parte 1 de este recorrido dura lo mismo que la de Academia (840 cuadros) y el cierre cae en el mismo cuadro (2760). **La edición es,
muestra a muestra, la de `recorrido-academia/SPEC.md` §0.1**: «Product Launch» (`_identidad/musica/product-launch-the-mountain.mp3`,
86,05 s, 120 BPM, compases de 2 s desde el 2,05) se toca del 14,05 al 46,04, salta al 22,01 y sigue hasta el final natural de la pista;
los **12 compases repetidos** son el final de la primera subida, el respiro y la segunda subida. Las razones y las medidas (similitud de los
compases de los bordes, ataque del 22,045 entero después del cruce, envolvente a ±0,4 dB, correlación 0,998 después de la costura) están
allí y no se repiten.

```bash
# en recorrido-equipos/ (script "musica" del package.json): 31,99 s + 64,037 s − 0,03 s de cruce = 95,997 s
ffmpeg -hide_banner -y -i ../_identidad/musica/product-launch-the-mountain.mp3 -filter_complex \
  "[0:a]atrim=start=14.05:end=46.04,asetpts=PTS-STARTPTS[a];[0:a]atrim=start=22.01,asetpts=PTS-STARTPTS[b];[a][b]acrossfade=d=0.03:c1=tri:c2=tri[m]" \
  -map "[m]" -ar 44100 -c:a pcm_s16le assets/musica/product-launch-recorrido.wav
```

- **Comprobación al armarla:** `ffprobe` da **95,997 s** (±5 ms). Mapa: **video = pista − 14,05** hasta el 31,99 y **video = pista + 9,95**
  desde el 31,99. Si `recorrido-academia/assets/musica/product-launch-recorrido.wav` ya existe y su `sha256sum` es el del archivo que da
  este comando, se copia en vez de generarlo.
- **Licencia:** Pixabay permite modificar la pista (`_identidad/licencias.md`); la editada no se redistribuye sola. Tiene Content ID: en
  YouTube puede llegar un reclamo de monetización, que se disputa con la licencia.

### 0.2 El reloj del video

| Video | Pista | Tramo de la pista (`kit.json` → `mapa`) | Lo que le toca al video |
|---|---|---|---|
| 0–4 | 14,05–18,05 | entrada sin bajo | El gancho del clip: «4 de 5 · 1 por cubrir» |
| 4–12 | 18,05–26,05 | primera subida (bajo en 18,05, pico en 20) | Asignar → Avisar |
| 12–20 | 26,05–34,05 | respiro | El celular de Gabriela: su servicio y sus instrucciones |
| 20–28 | 34,05–42,05 | segunda subida (golpes 36 · 38 · 42,05) | «Aceptar» → el líder la ve «Confirmado» → «5 de 5» |
| **28**–32 | 42,05–46,05 | el golpe más fuerte y su compás | Látigo al escritorio: la cobertura |
| **32**–36 | 22,05–26,05 (repetido) | final de la primera subida | Gabriela en verde en Seguridad |
| 36–44 | 26,05–34,05 (repetido) | respiro | «Solo lo que falta» |
| **44**–60 | 34,05–50,05 (repetido hasta 46,05) | segunda subida otra vez (el golpe más fuerte en el **52,0**) | El chat de Alabanza: votar, «Asistiré», escribir |
| **60**–76 | 50,05–66,05 | clímax (dos frases de 8 s) | Servir → cerrar el turno → «1 persona cumplió su objetivo» |
| **76**–92 | 66,05–82,05 | salida tranquila | Gabriela: «Servir» cumplido; la frase del sitio |
| **92**–96 | 82,05–86,05 | el último acorde, que se apaga solo | El cierre del Comercial |

### 0.3 La grilla, pulso por pulso

**Cuadros 0–839:** la tabla de `clip-sitio-equipos/SPEC.md` §0, sin cambios (todo pulso en múltiplo de 15; el 285 real cae en el 284 y
ahí no hay nada).

**Cuadros 840–2760** (cuadro · fuerza), medidos el 2026-10-30 con `product-launch-the-mountain.pulsos.json` en el instante de la pista
que le toca a cada cuadro (§0.1). **La grilla del detector vale hasta el 52,535 de la pista (cuadro 1875).** Después marca el redoble
(52,975 · 53,415 · 53,865 = cuadros 1888–1915, donde **no cae nada**) y, del 54,305 al 80,175 de la pista (cuadros 1934–2700), **se engancha
en los contratiempos** (x,295 / x,795: medio pulso corrido). En ese tramo las negras siguen en 2,045 + 0,5·k (los cambios de sección en el
50,045, el 66,045 y el 82,045; Eventos §0.2 y Academia §0.3 lo midieron igual) y la fuerza que va en *cursiva* es el flujo espectral medido
por Academia en el mismo cuadro del mismo archivo (1,00 = el 99,5 % más fuerte de la pista). **Nada del video cae en un contratiempo.**

| Compás | Cuadros | Pulsos (cuadro · fuerza) | Lo que le toca |
|---|---|---|---|
| 15 | 840–899 | **840 ·1,00** · 855 ·0,68 · 870 ·0,51 · 885 ·0,52 | **Látigo al escritorio**: la cobertura |
| 16 | 900–959 | **900 ·0,84** · 915 ·0,82 · 930 ·0,75 · 945 ·0,66 | 900 la app baja a Seguridad |
| 17 | 960–1019 | **960 ·0,92** (costura) · 975 ·0,77 · 990 ·0,58 · 1005 ·0,52 | 960 la cámara a Gabriela (D⁺) |
| 18 | 1020–1079 | 1020 ·0,77 · 1035 ·0,74 · 1050 ·0,60 · 1065 ·0,58 | 1020 la cámara abre; 1035 la app sube; 1050 la cámara al interruptor |
| 19 | 1080–1139 | **1080 ·0,76** · 1095 ·0,64 · 1110 ·0,50 · 1125 ·0,46 | **1080 toque «Solo lo que falta»** |
| 20 | 1140–1199 | 1140 ·0,75 · 1155 ·0,61 · 1170 ·0,49 · 1185 ·0,49 | 1140 la cámara a Alabanza |
| 21 | 1200–1259 | 1200 ·0,67 · 1215 ·0,67 · 1230 ·0,54 · 1245 ·0,50 | 1200 la cámara a Audiovisual (si cabe) |
| 22 | 1260–1319 | 1260 ·0,63 · 1275 ·0,56 · 1290 ·0,61 · 1305 ·0,68 | Quieto |
| 23 | 1320–1379 | **1320 ·0,93** · 1335 ·0,69 · 1350 ·0,52 · 1365 ·0,49 | **Látigo de vuelta: el chat de Alabanza** |
| 24 | 1380–1439 | **1380 ·0,90** · 1395 ·0,89 · 1410 ·0,76 · 1425 ·0,68 | 1380 la cámara a la encuesta |
| 25 | 1440–1499 | **1440 ·0,96** · 1455 ·0,77 · 1470 ·0,59 · 1485 ·0,60 | **1440 toque «Way Maker»** |
| 26 | 1500–1559 | **1500 ·0,88** · 1515 ·0,74 · 1530 ·0,62 · 1545 ·0,60 | 1500 la app baja al ensayo |
| 27 | 1560–1619 | **1560 ·1,00** · 1575 ·0,68 · 1590 ·0,51 · 1605 ·0,52 | **1560 toque «Asistiré»** + punch |
| 28 | 1620–1679 | 1620 ·0,84 · 1635 ·0,82 · 1650 ·0,75 · 1665 ·0,66 | 1620 la cámara al pie del chat |
| 29 | 1680–1739 | **1680 ·0,98** · 1695 ·0,74 · 1710 ·0,60 · 1725 ·0,57 | 1680 toque en la caja; el mensaje se escribe |
| 30 | 1740–1799 | 1740 ·0,79 · 1755 ·0,75 · 1770 ·0,69 · 1785 ·0,67 | 1740 toque «Enviar»; 1770 la cámara a la barra de abajo |
| 31 | 1800–1859 | **1800 ·0,93** · 1815 ·0,84 · 1830 ·0,63 · 1845 ·0,49 | **1800 toque «Servir»** (empieza el clímax) |
| 32 | 1860–1919 | 1860 ·0,81 · **1875 ·0,95** · (redoble 1888–1915) | 1860 la cámara a la tarjeta; nada entre 1875 y 1915 |
| 33 | 1920–1979 | **1920 ·*1,00*** · 1935 ·*0,92* · 1950 ·*0,67* · 1965 ·*0,76* | **1920 toque en la fila → iris → «Cerrar el turno»** |
| 34 | 1980–2039 | 1980 ·*0,62* · 1995 ·*1,00* · 2010 ·*0,69* · 2025 ·*0,68* | 1980 la cámara a Gabriela «Sirvió» |
| 35 | 2040–2099 | **2040 ·*1,00*** · 2055 ·*1,00* · 2070 ·*0,83* · 2085 ·*0,83* | **2040 toque «No llegó»** |
| 36 | 2100–2159 | 2100 ·*0,71* · 2115 ·*0,87* · 2130 ·*0,73* · 2145 ·*0,71* | 2100 la cámara a la barra «Cerrar el turno» |
| 37 | 2160–2219 | **2160 ·*1,00*** · **2175 ·*1,00*** · 2190 ·*0,58* · 2205 ·*0,68* | **2160 toque «Cerrar el turno»; 2175 el aviso del objetivo** |
| 38 | 2220–2279 | 2220 ·*0,54* · 2235 ·*1,00* · 2250 ·*0,68* · 2265 ·*1,00* | Quieto |
| 39 | 2280–2339 | **2280 ·*0,77*** · 2295 ·*0,46* · 2310 ·*0,41* · 2325 ·*0,43* | **Látigo vertical: Gabriela**; 2310 la cámara a la barra de abajo |
| 40 | 2340–2399 | 2340 ·*0,46* · 2355 ·*0,50* · 2370 ·*0,46* · 2385 ·*0,47* | **2340 toque «Objetivos»**; 2370 el check terminado |
| 41 | 2400–2459 | **2400 ·*0,76*** · 2415 ·*0,51* · 2430 ·*0,44* · 2445 ·*0,40* | 2400 la cámara a «Servir» (C) |
| 42 | 2460–2519 | 2460 ·*0,46* · 2475 ·*0,57* · 2490 ·*0,39* · 2505 ·*0,42* | Quieto |
| 43 | 2520–2579 | **2520 ·*0,80*** · 2535 ·*0,51* · 2550 ·*0,45* · 2565 ·*0,43* | **La frase del sitio**; la ventana a un lado |
| 44–45 | 2580–2699 | 2580 ·*0,94* · … | Quieto |
| 46 | 2700–2759 | 2700 ·*0,34* · 2715 ·*0,67* · 2730 ·*0,41* · 2745 ·*0,98* | La subida (desde 2716); el dip 2757–2759 |
| — | **2760** | el último acorde (pista 82,05) | **El cierre del Comercial** |

(Lo que el detector marca en esos cuadros, para quien lo compare: 1890 → 52,975 · 1905 → 53,415 · 1920 → 53,865 · 1935 → 54,305 · … · 2700 →
80,175; desde el 2715 vuelve a la grilla: 80,545 · 81,045 · 81,545 · 82,045.)

### 0.4 Nivel de la música

`<audio id="musica" src="assets/musica/product-launch-recorrido.wav" data-start="0" data-duration="96" data-track-index="20">`, **sin
`data-volume`**: **0,75** en el carril de volumen de principio a fin (el nivel del clip: −17,1 LUFS con sus sonidos, REVIEW del clip §5).
**Sin fundido**: la pista termina sola debajo del cierre. Si en la vista previa las campanas del 92,38 quedan tapadas, el carril baja a 0,5
entre 92,0 y 92,3 (y se anota en el REVIEW); nada más se toca.

---

## 1. Los números del estilo

### 1.1 Paleta

La de `clip-sitio-equipos/SPEC.md` §1.1, tal cual (fondo `#060D1F`, halo, puntos que nunca se mueven, tinta `#EAF0FF`, dorado `#E8B95A`
solo en la ceja, *cubierto* y el botón del cierre; anillo `rgba(234,240,255,.12)`; placa de «Datos de ejemplo» `rgba(6,13,31,.72)`; el azul
de marca solo dentro del cierre). Cambian: el **dip** va en **2757–2759** sobre las dos ventanas; el **halo** se asienta 1,08 → 1,00
(`sine.out`, 90 cuadros) en **0 · 180 · 720 · 840 · 1320 · 1800 · 2280**. Los colores de la app (el semáforo verde, ámbar y rojo de la
cobertura, el rojo de «No llegó», el azul del tema) viven en la grabación y no se tocan ni se repiten fuera.

### 1.2 Tipografía (16:9)

| Pieza | Clase del kit | Familia · peso | Tamaño | Reglas |
|---|---|---|---|---|
| Frase | `.k-titular` con `font-size: 84px` | Fraunces 560; `<em>` itálica 500 dorada | **84 px** · interlínea 1,04 (87,4 px) · −0,02 em | Máx. 2 líneas en el celular (la del sitio, **3**), **1 línea** en el escritorio; saltos fijados a mano; izquierda; `text-wrap: balance` apagado; sin sombra |
| Ceja | `.k-ceja` | Inter 700, MAYÚSCULAS, +0,10 em | **28 px** | Una palabra: «EQUIPOS» |
| Datos de ejemplo | `.k-datos-ejemplo` (la de 16:9) | Inter 600 | **22 px**, píldora de 40 px | En cada ventana, abajo a la izquierda, a 24 px |
| Texto de la app | (grabación) | la de la app | ≥ **28 px** en todo encuadre de lectura | §1.5 |

Saltos fijados: «¿Quién cubre / el domingo?» · «Kingdom sugiere / a quién poner» · «Y sabe a qué / hora llegar» · «Y el domingo, /
completo.» · «Lo que falta, antes del domingo.» (una línea) · «Cada equipo, / con su chat.» · «Servir cuenta.» (una línea) · «Y da un paso /
en su ruta.» · «Que cada puesto / de servicio / esté *cubierto*» (tres líneas, como la 9:16 del clip; la más ancha, «esté *cubierto*»,
≈ 560 px). La más ancha de todas es «Lo que falta, antes del domingo.» (32 caracteres, ≈ 1300 px) en el escritorio, que tiene 1440: cabe.
Si `check` marca desborde en alguna, la columna crece hacia la ventana; **nunca se baja la letra de 84**.

### 1.3 Radios y sombras

Los del kit: `.k-ventana` radio **28** (celular) y **20** (`.k-ventana-escritorio`), anillo y sombra de `kit.css`, `overflow: hidden`.
Frases y ceja sin sombra ni brillo.

### 1.4 Disposición: dos escenarios

Igual que Academia §1.4:

| | Escenario del celular | Escenario del escritorio |
|---|---|---|
| Ventana | `#ventana-cel.k-ventana.k-ventana-16x9`: **x 1104 · y 90 · 720 × 900** | `#ventana-esc.k-ventana.k-ventana-escritorio`: **x 240 · y 260 · 1440 × 760** |
| Ceja | x 120 · y 412 | x 240 · y 92 |
| Frase | x 120 · y 460 · ancho 936 · 2 líneas → termina en 635 (la del sitio, 3 → 722) | x 240 · y 132 · una línea → termina en 219 |
| Datos de ejemplo | dentro de la ventana, abajo a la izquierda, a 24 px | ídem |
| Final (desde el 2524) | la ventana a escala **0,92** con origen «100% 50%» y x **+24** | — |

- **Las dos ventanas viven en una tira horizontal** (`#escena`): el celular en x 1104 y el escritorio en x 240 + 1920 = **2160**. `#escena`
  en x 0 muestra el celular; en x **−1920**, el escritorio.
- **Las frases y la ceja no viajan con el látigo horizontal:** salen con blur antes y entran después, en el lugar de su escenario. En el
  látigo vertical (2280) la ceja se queda quieta.
- El 90 % seguro para títulos (96 px a los lados, 54 arriba y abajo) se cumple en los dos escenarios.

```js
window.KD = {
  fps: 30,
  cel: { x: 1104, y: 90, w: 720, h: 900, hVis: 900 },          // --f-k = 720/1170 = 0.615385; --f-grab-alto = 1558.15px
  esc: { x: 240, y: 260, w: 1440, h: 760, hVis: 760 },         // K = 1440/1920 = 0.75; alto de la grabación ajustada = 810
  grabCel: { w: 1170, h: 2532, cssW: 390, cssH: 844 },         // celular 390×844 a 3×
  grabEsc: { w: 1920, h: 1080, cssW: 1280 },                   // escritorio 1280×720 a 1,5× (modo video de capturar.mjs)
  latigoV: 1000,                                               // la tira vertical del celular (el clip usaba 1100 en 4:5)
  latigoH: 1920,                                               // la tira horizontal entre escenarios
  cambio: { escala: 0.92, x: 24, origen: '100% 50%' },         // la ventana del celular se hace a un lado (2524–2538)
};
```

### 1.5 La cámara: escalas de lectura

`enc(s, cx, cy)` del clip, una por ventana (con su `W`, `HV`, `PPC = W / cssW` y `VH`). **Una escala es de lectura si el texto de 14 px de
la app queda en ≥ 28 px.**

**Celular (`#ventana-cel`, PPC 1,846):** **G 1,085** (359 × 449 px CSS; 14 px → 28,0) · G⁺ 1,15 (340 × 424; 29,7) · M 1,40 (279 × 348;
36,2) · C 1,80 (217 × 271; 46,5). **Ningún encuadre de lectura del celular baja de 1,085.**

**Escritorio (`#ventana-esc`, PPC 1,125):** **D 1,80** (711 × 375 px CSS; 14 px → 28,4; el píxel de la grabación a 1,35) · D⁺ 2,00
(640 × 338; 31,5; 1,50, el tope del kit). El plano entero del escritorio (s = 1) **solo existe durante el látigo**; ningún encuadre pasa de
2,0.

### 1.6 Curvas y duraciones (cada tween con su curva por nombre)

| Papel | Curva | Cuadros | Detalle |
|---|---|---|---|
| `entrada-palabra` | `power4.out` | 4 | blur 6 → 0 + opacidad; sin desplazamiento; arranca un cuadro antes del pulso; palabras a 2 cuadros (la frase 1, una por pulso) |
| `entrada-linea` | `power4.out` | 6 | la línea entera, blur 8 → 0 (la frase 2 y cada entrada de la ceja) |
| `salida-texto` | `power3.in` | 4–5 | blur 0 → 8 + opacidad; empieza 3 cuadros antes del golpe del cambio de mundo |
| `camara` | `power2.inOut` | **14** | un movimiento por compás; después, quieta; nunca mientras la app se desplaza o escribe |
| `punch` | `power2.inOut` | **9** | **1560** («Asistiré») y **2175** (el aviso del objetivo) |
| `match-cut` | `power3.out` | 10 | el mundo que entra por un toque aterriza 1,03 → 1,00 desde el punto tocado: 75 (del clip), **1800** («Servir») y **2340** («Objetivos») |
| `latigo-v` | `power3.inOut` | **10** | la tira vertical, 1000 px: **sube = al otro celular** (356–366 y **2270–2280**), **baja = de vuelta** (656–666); el que llega aterriza 1,04 → 1,00 (`power3.out`, 10) |
| `latigo-h` | `power3.inOut` | **10** | `#escena` 1920 px: **a la izquierda = al escritorio** (830–840), **a la derecha = de vuelta** (1310–1320); aterriza 1,04 → 1,00 (`power3.out`, 10, desde su centro) |
| `iris` | `power2.out` | 5 | `clip-path: circle(0 → 1900px)` desde el centro del botón tocado, en px de la ventana: 120 y 375 (del clip) y **1920** (la fila del turno por cerrar) |
| `ventana-cambio` | `power2.inOut` | 15 | 2524–2538: escala 1 → 0,92, origen «100% 50%», x +24 |
| `halo` | `sine.out` | 90 | §1.1 |
| `dip` | escalón | 3 | `rgba(6,13,31,.40)` sobre las dos ventanas, 2757–2759 |
| marcas de toque | las del clip | — | aparece 4 cuadros antes, se hunde en el cuadro, se va con el corte si la pantalla cambia debajo (REVIEW del clip §4.7) |
| velocidad de la grabación | `data-playback-rate` | — | **1×** en todo; nada se acelera ni se frena |
| cierre | las del kit | 150 | no se imita en el cuerpo |

`data-motion-blur="on"` y `data-motion-blur-shutter="180"` en la raíz. Nunca `filter: blur()` sobre una grabación.

### 1.7 Sonido

| Capa | Fuente | Nivel | Regla |
|---|---|---|---|
| Música | `assets/musica/product-launch-recorrido.wav` (§0.1) | 0,75 en el carril | §0.4 |
| Sonidos de acción | kit v1.1 (`toque` en tres tomas a/b/c: `identidad/audio/toque.wav` y `assets/audio/toque-b.wav`, `toque-c.wav` del clip), `aparicion`, `desliz`, `subida`, `confirmacion` | `data-volume="1"`; **1,4** solo en los `desliz` de los látigos y en las dos `confirmacion` clave (los toques clave a 1,0: con 1,4 el pico pasaba de −1 dBTP, REVIEW del clip §4.9) | `data-start = (cuadro de la imagen + 1) / 30 − acento` (toque 0 · aparicion 0 · desliz 0,2 · subida 1,5 · confirmacion 0,1) |
| Sonido de marca | `identidad/audio/sonido-marca.wav` | 1 | **92,38 s** |
| Mezcla de entrega | — | **−16 LUFS** integrada (±1), pico real ≤ **−1 dBTP** | `npx hyperframes audio` sobre el render; si −16 pasa el pico, se queda en lo que dé con −1 dBTP y se anota (el clip quedó en −17,1) |

**Los eventos de la parte 1 (0–839)** son los del clip (`clip-sitio-equipos/index.html`, REVIEW §3): los 8 `toque` (76 · 121 · 151 · 181 ·
241 · 301 · 376 · 601), las 3 `aparicion` (184 · 196 · 304), las 3 `confirmacion` (243 · 603 a 1,4 · 662), los 4 `desliz` (360 y 660 a
1,4; 451 y 541) — 18 en total —, **sin** la `subida` del 796–853 ni las campanas del 851.

**Los eventos de la parte 2** (cuadro de la imagen → `data-start` en s):

| Imagen | Sonido | `data-start` | Nivel | Causa en pantalla |
|---|---|---|---|---|
| 840 | `desliz` | 27,833 | **1,4** | Látigo al escritorio |
| 900 | `desliz` | 29,833 | 1 | La app baja a Seguridad |
| 1035 | `desliz` | 34,333 | 1 | La app vuelve arriba |
| 1080 | `toque` a | 36,033 | 1 | «Solo lo que falta» |
| 1083 | `aparicion` | 36,133 | 1 | Quedan solo los que les falta |
| 1320 | `desliz` | 43,833 | **1,4** | Látigo de vuelta al celular |
| 1440 | `toque` b | 48,033 | 1 | «Way Maker» |
| 1500 | `desliz` | 49,833 | 1 | La app baja al ensayo |
| 1560 | `toque` c | 52,033 | 1 | «Asistiré» |
| 1563 | `aparicion` | 52,133 | 1 | «N van» sube uno (real: el cuadro en que cambia; se ajusta a ±2) |
| 1680 | `toque` a | 56,033 | 1 | La caja del mensaje |
| 1740 | `toque` b | 58,033 | 1 | «Enviar» |
| 1743 | `aparicion` | 58,133 | 1 | Su mensaje en el chat (real) |
| 1800 | `toque` c | 60,033 | 1 | «Servir» (corte sobre el toque) |
| 1920 | `toque` a | 64,033 | 1 | La fila del turno (iris) |
| 2040 | `toque` b | 68,033 | 1 | «No llegó» |
| 2160 | `toque` c | 72,033 | 1 | «Cerrar el turno» |
| 2175 | `confirmacion` | 72,433 | **1,4** | «1 persona cumplió su objetivo de servir en la ruta.» |
| 2280 | `desliz` | 75,833 | **1,4** | Látigo vertical al celular de Gabriela |
| 2340 | `toque` a | 78,033 | 1 | «Objetivos» (corte sobre el toque) |
| 2369 | `confirmacion` | 78,900 | **1,4** | El check de «Servir» termina de dibujarse (real: el cuadro en que el trazo se cierra; §2.2) |
| 2716–2773 | `subida` | **90,533** | 1 | Hacia el cierre (golpe en el 2761) |
| 2771 | marca | 92,38 | 1 | Las campanas del cierre |

Sin tics de tecla (el mensaje del chat se escribe en silencio). **Dos sonidos de acción nunca se enciman, salvo** 1080 + 1083, 1560 + 1563
y 1740 + 1743 (toque y su resultado). La `subida` es la única del video.

### 1.8 BANNED: los valores por defecto prohibidos, con nombre

Valen enteros los de `clip-sitio-membresia/SPEC.md` §1.8 (1–20), los de `clip-sitio-equipos/SPEC.md` §1.8 (incluida la 31: nada de «Abierto
a redes», «Apoyo de red» ni «Vacantes abiertas» en cuadro) y los de `recorrido-academia/SPEC.md` §1.8 del 27 al 37 que apliquen (sin cursor,
látigo solo entre escenarios o personas, escritorio entre 1,8 y 2,0, nada de marco de navegador, ninguna cifra dibujada encima, la frase del
sitio y el cierre sin tocar, ninguna frase viajando con el látigo horizontal). Además:

38. **Las pestañas de la cobertura en cuadro con «Por red» abierta**, o cualquier encuadre que lea «Por red» como protagonista. Los
    encuadres de la cobertura empiezan debajo de las pestañas (§2.2); «Por red» y «Por semana» no se tocan.
39. **Un látigo entre el chat y el cierre del turno.** Es la misma persona: se pasa con el toque en «Servir» y el corte sobre el toque.
40. **La fecha del turno cerrado como dato legible** (la fila de la tarjeta y la línea de arriba del título). El turno que se cierra es el
    domingo pasado de la base (STORY §6): se encuadra sin ella o, si no se puede, a menos de 28 px y menos de 1 s.
41. **Un número que cambie fuera de la app** (los votos, «N van», «5 sirvieron», «13 de 19») o un resaltado dibujado sobre Gabriela. Lo que
    la señala es la cámara.
42. **La ventana del escritorio con barra del navegador o con el cursor**, o el teclado del celular dibujado. La escritura del mensaje se ve
    en la caja de la app, nada más.
43. **El aviso del objetivo cerrado por un toque en cámara.** El «Entendido» se toca fuera de cámara (la escena lo hace después del tramo).
44. **Un fundido, un zoom a través de un botón o una cortinilla** para pasar de la cobertura al chat o del líder a Gabriela.

---

## 2. Los planos, cuadro por cuadro

### 2.0 Convenciones

- **Grabaciones:** **K** = la del clip (`assets/grabaciones/parqueadero/grabacion.mp4`, 1170×2532, 30 fps, 65,23 s; sus cuadros como en el
  REVIEW del clip); **C** = la nueva de celular (`assets/grabaciones/celular/`, escena §3.2); **E** = la nueva de escritorio
  (`assets/grabaciones/escritorio/`, escena §3.3). «C·voto» = el tramo `voto` de C en su `pasos.json`; «+N» = N cuadros después de la
  acción de ese paso.
- **Niveles:** G, G⁺, M, C (celular) y D, D⁺ (escritorio), de §1.5. «Sobre X» = la caja de X (`pasos.json` → `caja`, px CSS) centrada en lo
  visible. **«(real)»** = la caja no se conoce hasta grabar: se toma de `pasos.json` o del cuadro y se anota en el REVIEW.
- **Pulso:** el cuadro de §0.3; un evento «en el 1440» se ve en el 1440 y suena en el 1441.
- **Mundos.** La tira vertical (`#tira`, dentro de `#ventana-cel`) tiene dos ranuras de 1000 px, como el clip: **m1** (y 0) y **m2**
  (y +1000). Cada mundo tiene su cámara y, como en el clip, una segunda cámara dentro de su iris. El contenido de una ranura se cambia solo
  cuando está fuera de cuadro:

  | Ranura | 0–356 | 356–666 | 666–830 | 1320–2280 | 2280–2760 |
  |---|---|---|---|---|---|
  | m1 (Jorge, 103) | K: el calendario y el turno (`#cam1`, `#iris1 > #cam1b`) | (fuera) | K: el turno, «5 de 5» | **C: el chat de Alabanza → Servir → «Cerrar el turno»** (`#cam3`, `#iris3 > #cam3b`) | (fuera) |
  | m2 (Gabriela, 105) | (fuera) | K: Mi iglesia y su servicio (`#cam2`, `#iris2 > #cam2b`) | (fuera) | (fuera) | **C: Mi iglesia → «Mis objetivos»** (`#cam4`) |

  La ventana del escritorio tiene un mundo, **e1** (E: la cobertura, `#camE1`), visible 830–1320. Entre el 840 y el 1310 la ventana del
  celular está fuera de cuadro (en `#escena`) y m1 cambia de K a C.
- Las frases, siempre en el lugar de su escenario (§1.4); una a la vez; la ceja encima.

### 2.1 Parte 1 (0–839): el clip en 16:9

Se copia `clip-sitio-equipos/index.html` y se cambia **solo** esto:

1. **Formato:** raíz 1920×1080, `data-duration="97"`. `#ventana` del clip → `#ventana-cel` con `.k-ventana-16x9` dentro de `#escena`;
   `window.KD` de §1.4 (`W` 720, `HV` 900, `K` 0,615385, `PPC` 1,846, `VH` 1558,15, látigo vertical **1000** en vez de 1100). Las marcas
   de toque y los dos iris siguen en px de la ventana con el `--f-k` nuevo (`enVentana()` del clip).
2. **Los mismos 24 tramos de video y los dos stills** (`still-362.png` bajo el iris del 120 y `still-1132.png` bajo el del 375), con sus
   mismos `data-start`, `data-duration` y `data-media-start`, desde `assets/grabaciones/parqueadero/grabacion.mp4`. Mismos cortes, mismo
   match cut (75–88), mismos iris (120 y 375), mismos látigos (356–366 sube, 656–666 baja) y mismos aterrizajes.
3. **Las mismas cámaras** con `s' = max(s, 1,085)`:

   | Encuadre del clip | s del clip | s en 16:9 | (cx, cy) |
   |---|---|---|---|
   | semana (M) | 1,4 | 1,4 | 155,5 · 490 |
   | porCubrir (C) | 1,8 | 1,8 | 125 · 450 |
   | turnoCabeza | 1,15 | 1,15 | 176 · 245 |
   | parqueadero1 | 1,08 | **1,085** | 195 · 440 |
   | sugerencias | 1,15 | 1,15 | 195 · 270 |
   | pie | 1 | **1,085** | 195 · 565 |
   | avisar | 1,25 | 1,25 | 172 · 604 |
   | avisados | 1,08 | **1,085** | 195 · 422 |
   | parqueadero2 (M) | 1,4 | 1,4 | 155,5 · 440 |
   | cierre | 1,2 | 1,2 | 176 · 362 |
   | tarjeta | 1 | **1,085** | 195 · 275 |
   | servicioCabeza (M) | 1,4 | 1,4 | 160 · 261,5 |
   | llegada (C) | 1,8 | 1,8 | 130 · 225 |
   | servicio | 1 | **1,085** | 195 · 275 |
   | paleta | 1,04 | **1,085** | 195 · 468 |
   | botones | 1,08 | **1,085** | 195 · 372 |

   El ancho visible es el del clip a la misma s (390 / s px CSS) y el alto, **11 % mayor** (487,5 / s contra 438,8 / s): todos los
   encuadres del clip caben. Se revisan en la vista previa los tres que el clip ajustó al borde: **paleta** (a ×1,085 «Colores» y las horas
   del cronograma quedan a 1 px del borde: si tocan, cx pasa a 194 y se acepta un roce de 1 px; nunca se baja de 1,085), **tarjeta** y
   **turnoCabeza** (el aterrizaje 1,04 / 1,03 no puede cortar «Buenas tardes» ni «Domingo»).
4. **Las frases** van a la columna izquierda (§1.4): la 1, la 2 y la 3 en sus cuadros del clip (0 · 15 · 30 · 45; 120–126; 360–370), con los
   saltos de §1.2. **La 4 del clip (la del sitio) no va aquí**: pasa al 2520. En su lugar, en el 720, **«Y · el · domingo, / completo.»**
   720 · 722 · 724 · 726, quieta hasta el 837 (sale 837–841 con el látigo horizontal). La ceja entra en el 195 como en el clip y **se queda**
   (en el clip salía en el 720).
5. **Se quitan:** la ventana a un lado del 724–738, la `subida` del 796–853, el dip del 837–839, la firma del 840 (`cierre-clip`) y sus
   campanas.
6. **Del 720 al 839:** el tramo del clip (K 1660–1843) sigue igual en el encuadre `cierre` (×1,2): «9:00 a. m.», **«5 de 5»**, los botones,
   Parqueadero con Rut y Gabriela «Confirmado». Con la ventana a escala 1 (ya no baja a 0,92) el chip «5 de 5» queda en ≈ 29 px (en el clip,
   27). Se revisa que «Datos de ejemplo» no tape a Gabriela (REVIEW del clip §4.6): la píldora queda 24 px más abajo que en 4:5 en px CSS
   (el alto visible es mayor); si la tapa, `cierre` pasa a cy 352.

### 2.2 Parte 2 (840–2909): tabla maestra

| Cuadro | Pulso | La app (grabación) | Cámara | Texto | Sonido | Transición |
|---|---|---|---|---|---|---|
| 830–840 | | m1 (el turno) sale a la izquierda con `#escena`; e1 llega desde la derecha: E·cobertura, la página ya cargada | e1 llega en **D** sobre la barra de la reunión: el selector «Reunión · Dom, 1 de nov · Servicio General · 9:00 a. m.», «Solo lo que falta» y, debajo, **«13 de 19 confirmados (68 %)»** y la cabecera del primer equipo; las pestañas, fuera, arriba (real) | frase 4 sale 837–841; la ceja sale 837–840 | `desliz` (1,4) | **Látigo horizontal a la izquierda**; e1 aterriza 1,04 → 1,00 (840–850); halo |
| **840** | ● 1,00 | E·cobertura quieto | D | ceja arriba (`entrada-linea`, 842–848); «Lo · que · falta, · antes · del · domingo.» 843 · 845 · 847 · 849 · 851 · 853 | | |
| **900** | ● 0,84 | E·seguridad: la app baja a la tarjeta de **Seguridad** (su desplazamiento; si es un salto, se ve en el 900): «Seguridad · 5/5 · 100 %», la barra verde llena; Parqueadero: Rut Londoño Isaza · Confirmado, **Gabriela Hinestroza Perea · Confirmado**; Entrada; Rondas | **quieta** | | `desliz` | |
| **960** | ● 0,92 (costura) | quieto | 960–973 → **D⁺** sobre Parqueadero: los dos puntos verdes y **«Gabriela Hinestroza Perea · Confirmado»** a 31,5 px (real) | | — | — (la costura de la música cae aquí; la imagen no corta) |
| 1020 | ● | quieto | 1020–1033 → **D** sobre el centro de lo visible | | | |
| 1035 | ● | E·arriba: la app vuelve arriba (el selector y el interruptor) | quieta | | `desliz` | |
| 1050 | ● | quieto | 1050–1063 → **D** sobre «Solo lo que falta» y el total (real) | | | |
| **1080** | ● 0,76 | toque «Solo lo que falta» (E·falta, la acción): el interruptor se enciende; corte en la espera (la recarga): en el **1083**, la lista solo con lo que falta: **Seguridad, Evangelismo y Medios ya no están**; quedan **Alabanza** (2/7, los puestos «Vacante» en rojo y «Por confirmar» en ámbar) y **Audiovisual** (3/4, uno por confirmar). El total sigue en «13 de 19» | quieta | | `toque` a · `aparicion` 1083 | marca de toque |
| 1140 | ● | quieto | 1140–1153 → **D** sobre la tarjeta de Alabanza: su cifra roja «2/7 · 29 %» y sus funciones con los puntos rojos y ámbar (real) | | | |
| 1200 | ● | quieto | 1200–1213 → **D** un poco más abajo, para que entre la cabecera de Audiovisual «3/4 · 75 %» (real: si no cabe con Alabanza, la cámara se queda) | | | |
| 1260–1309 | | quieto | quieta | | | |
| 1310–1320 | | e1 sale a la derecha; vuelve el celular con **m1 = Jorge en el chat de Alabanza** (C·chat, ya en la encuesta) | m1 llega en **G** arriba: «Alabanza», **el anuncio anclado** «📌 … ¡Hola, equipo! Ensayamos todos los jueves a las 7 p. m.…» y el hilo con la encuesta (real) | frase 5 y ceja salen 1317–1320 | `desliz` (1,4) | **Látigo horizontal a la derecha**; aterriza 1320–1330; halo |
| **1320** | ● 0,93 | C·chat quieto | G | ceja a la izquierda (1322–1328); «Cada · equipo, / con · su · chat.» 1322 · 1324 · 1326 · 1328 · 1330 | | |
| 1380 | ● 0,90 | quieto | 1380–1393 → **M** sobre la encuesta: «Encuesta · **¿Con qué canción abrimos el domingo? 🎶** · Elige una · Grande y fuerte · Way Maker · Cuán grande es Él» con sus cuentas y «N votos» (real) | | | |
| **1440** | ● 0,96 | toque «Way Maker» (C·voto): su círculo se marca, la cuenta sube uno y la barra crece | quieta | | `toque` b | marca |
| **1500** | ● 0,88 | C·ensayo: la app baja a la tarjeta **«Reunión · Ensayo de Alabanza · jue, {fecha} · 7:00 p. m. – 9:00 p. m. · Cada semana hasta … · Salón principal · Repasamos la lista del domingo…»** con «Asistiré · No asistiré» y «N van · 1 no va · N sin responder» | **quieta** (la tarjeta queda en el centro de lo visible: la cámara M está centrada en el centro del hilo, real) | | `desliz` | |
| **1560** | ● 1,00 | toque «Asistiré» (C·asistire): el botón se llena; en el **1563**, «N van» sube uno (real) | **punch** 1560–1568 → **C** sobre los dos botones y la cuenta (real) | | `toque` c · `aparicion` 1563 | marca |
| 1620 | ● 0,84 | quieto | 1620–1633 → **G⁺** sobre el final del hilo y la caja de escribir (real) | | | |
| **1680** | ● 0,98 | toque en la caja (C·mensaje); **1683–1738: «¡Cuenten conmigo el jueves!» se escribe** a 1× | quieta | | `toque` a | marca |
| **1740** | ● 0,79 | toque «Enviar» (C·enviar): la caja se vacía; en el **1743**, su mensaje aparece al final del hilo (a la derecha; el reloj y luego el visto) | quieta | | `toque` b · `aparicion` 1743 | marca |
| 1770 | ● | quieto | 1770–1783 → **G** abajo: el final del hilo, la caja y **la barra de abajo de la app con «Servir»** (real) | frase 6 sale 1797–1801 | | |
| **1800** | ● 0,93 | toque «Servir» de la barra de abajo (C·servir, la acción); corte en la espera: **el inicio de Servir de Jorge** con la tarjeta **«Cerrar el turno · 1 · 1 turno de tus equipos espera que marques quién sirvió.»** y su fila «Seguridad · Servicio General» | corte a **G** sobre la tarjeta (real); el mundo aterriza 1,03 → 1,00 (1800–1810) desde el punto tocado | «Servir · cuenta.» 1802 · 1804 (una línea) | `toque` c | **corte sobre el toque** (el de la serie: el 75 del clip); halo |
| 1860 | ● 0,81 | quieto | 1860–1873 → **M** sobre la tarjeta: el título, el «1», el texto y la fila **sin la fecha** (que queda a la derecha, fuera; real) | | | |
| 1875–1915 | | quieto | quieta | | | (el redoble de la pista: nada cae aquí) |
| **1920** | ● *1,00* | toque en la fila (C·cerrar, la acción) → corte en la espera: **«Cerrar el turno»**: «Seguridad · Servicio General», el chip «Por cerrar» y «Se cierra hasta el …», **«5 sirvieron · 0 no llegaron»** y la lista, cada uno con «✓ Sirvió» marcado | dentro del iris, **G⁺** desde el título «Cerrar el turno» hacia abajo (la línea de la fecha, encima del título, fuera; real) | | `toque` a | **iris** desde la fila (1920–1925): debajo, el cuadro de la tarjeta |
| 1980 | ● | quieto | 1980–1993 → **M** sobre **la fila de Gabriela** («Gabriela Hinestroza Perea · Parqueadero · ✓ Sirvió · No llegó») y la siguiente (real) | | | |
| **2040** | ● *1,00* | toque «No llegó» en la fila siguiente (C·no-llego): la fila se pone roja y su «No llegó» se llena | quieta | | `toque` b | marca |
| 2100 | ● | quieto (la barra oscura de abajo, fija: «Los confirmados vienen marcados «Sirvió»: marca a quien no llegó.» · **«Cerrar el turno»**) | 2100–2113 → **G⁺** abajo: la fila de Gabriela, la roja y la barra (real) | | | |
| **2160** | ● *1,00* | toque «Cerrar el turno» (C·cerrar-turno, la acción) | quieta | | `toque` c | marca |
| **2175** | ● *1,00* | corte en la espera: el aviso **«✓ El turno quedó cerrado · 1 persona cumplió su objetivo de servir en la ruta. · Entendido»** (C·cerrar-turno +N); detrás, el resumen «4 sirvieron · 1 no llegaron» | **punch** 2175–2183 → **M** sobre el aviso entero (real) | | `confirmacion` (1,4) | |
| 2184–2269 | | quieto | quieta | | | |
| 2270–2280 | | la tira sube: entra **m2 = Gabriela** (C·gabriela): «Buenas tardes, Gabriela · Iglesia Kingdom Demo 1» y sus tarjetas (real) | m2 llega en **G** arriba (real) | frase 7 sale 2277–2281 (la ceja se queda) | `desliz` (1,4) | **Látigo vertical hacia arriba** (al otro celular, como el 356 del clip); aterriza 2280–2290; halo |
| **2280** | ● *0,77* | C·gabriela quieto | G | «Y · da · un · paso / en · su · ruta.» 2282 · 2284 · 2286 · 2288 · 2290 · 2292 · 2294 | | |
| 2310 | ● | quieto | 2310–2323 → **G** abajo: sus tarjetas y **la barra de abajo con «Objetivos»** (real) | | | |
| **2340** | ● | toque «Objetivos» (C·objetivos, la acción); corte en la espera: **«Mis objetivos»** («En curso» y **«Para conectarte»**); la lista de conexión sube (`k-subir`) desde el **2349** y en «Servir» el círculo crece 2349–2359 y **el check se dibuja 2359–2369**; al lado, «Cumplido el {hoy}» (real: el `data-media-start` se elige para que el trazo se cierre en el 2369) | corte a **G** arriba de «Mis objetivos» (el título y las dos secciones, real); aterriza 1,03 → 1,00 (2340–2350) | | `toque` a · `confirmacion` 2369 (1,4) | **corte sobre el toque** |
| **2400** | ● *0,76* | quieto | 2400–2413 → **C** sobre «Servir» con su check y «Cumplido el …» (≥ 46 px; real) | | | |
| 2460–2519 | | quieto | quieta | | | |
| **2520** | ● *0,80* | quieto | quieta | frase 8 sale 2515–2519; la ceja sale 2520–2523; «Que · cada · puesto / de · servicio / esté · *cubierto*» 2519 · 2521 · … · 2533 (dos cuadros entre palabras) | | |
| 2524–2538 | | | | | | **La ventana a un lado**: 0,92, origen «100% 50%», x +24 |
| 2539–2756 | | quieto (C·objetivos, el final de su pausa) | quieta | la frase sostenida 7,9 s | `subida` desde 90,533 | |
| 2757–2759 | | | | | | **dip** sobre la ventana |
| **2760** | ● | — | — | — | marca en 92,38 | **corte al cierre del Comercial** (`#escena` oculta) |

### 2.3 Los planos

#### P1–P7 · El clip — 0–719
Los siete primeros planos del clip (REVIEW del clip §2), en 16:9 y con los cambios de §2.1.

#### P8 · «Y el domingo, completo» — 720–839 (compases 13–14)
El turno del líder quieto en `cierre` con «5 de 5»; la frase contesta la pregunta del cuadro 0. La ventana no se mueve: en el 840 viene el
látigo.

#### P9 · «Lo que falta, antes del domingo» — 840–1319 (compases 15–22)
El látigo horizontal es la puerta a toda la iglesia: lo que era un turno pasa a ser cada departamento. Primero el total; en el 900 la app
baja a Seguridad y **Gabriela está ahí, en verde** (el dato viaja del celular del líder al computador del administrador); en la costura (960)
la cámara se acerca a su nombre. En el 1080, **«Solo lo que falta»**: Seguridad desaparece porque está completo y quedan los que aún tienen
puntos rojos y ámbar. El respiro de la música deja leer lo que falta sin que nada más se mueva. Alabanza queda a la vista: es el equipo al
que entramos en el plano siguiente.

#### P10 · «Cada equipo, con su chat» — 1320–1799 (compases 23–30)
De vuelta al celular de Jorge, ahora como cantante de Alabanza. El anuncio anclado se lee en el aterrizaje; la encuesta en el 1380; **su
voto en el 1440**; la app baja al ensayo del jueves en el 1500 y **«Asistiré» cae en el golpe más fuerte de la parte 2 (1560)** con un punch
a los botones y la cuenta. Del 1680 al 1740 escribe y envía su mensaje (lo que todo grupo hace, al final y breve). En el 1770 la cámara baja
a la barra de la app, donde está «Servir».

#### P11 · «Servir cuenta» — 1800–2279 (compases 31–38)
El clímax. **1800: toque en «Servir»** y el inicio de Servir entra sobre el toque (el corte de la serie, como el 75 del clip): la tarjeta
«Cerrar el turno» espera. **1920: toque en la fila** y el iris abre la lista de quién sirvió, con los confirmados ya marcados; en el 1980 la
cámara encuentra a Gabriela. **2040: «No llegó»** en el que faltó (el líder marca, la app no lo hace sola). **2160: «Cerrar el turno»**, y
**2175: «1 persona cumplió su objetivo de servir en la ruta.»** con un punch. Cuatro toques en cuatro golpes fuertes y el resultado en el
quinto.

#### P12 · «Y da un paso en su ruta» — 2280–2519 (compases 39–42)
El látigo vertical sube al celular de Gabriela, como en el 12,0 del clip: «Buenas tardes, Gabriela» dice de quién es. En el 2340 toca
«Objetivos» y **el check de «Servir» se dibuja** (2359–2369) con la `confirmacion`; en el 2400 la cámara se acerca. La salida de la música
baja sola: el plano es tranquilo a propósito.

#### P13 · La frase del sitio — 2520–2759
«Que cada puesto de servicio esté *cubierto*» palabra a palabra en el 2520, en tres líneas; la ceja se va; la ventana se hace a un lado
(2524–2538) y todo queda quieto salvo el halo; la `subida` empieza en el 90,533 y su golpe cae con el cierre. Dip 2757–2759.

#### P14 · El cierre — 2760–2909

```html
<div id="cierre-comercial" data-composition-id="cierre-comercial" data-composition-src="identidad/cierre-comercial.html"
  data-variable-values='{"publico":"iglesia","llamado":"prueba","contacto":"sitio","fondo":"noche","idioma":"es"}'
  data-start="92" data-duration="5" data-track-index="6" data-width="1920" data-height="1080"></div>
<audio id="marca-cierre" src="identidad/audio/sonido-marca.wav" data-start="92.38" data-duration="2.1" data-track-index="26" data-volume="1"></audio>
```

---

## 3. Las grabaciones

### 3.1 Lo que se reusa

- **La grabación del clip, entera y sin cambios:** `clip-sitio-equipos/assets/grabaciones/grabacion.mp4` (1170×2532, 30 fps, 65,23 s) y su
  `pasos.json` → `recorrido-equipos/assets/grabaciones/parqueadero/`. Se usan los mismos 24 tramos y los dos stills
  (`clip-sitio-equipos/assets/stills/still-362.png` y `still-1132.png` → `recorrido-equipos/assets/stills/`). Nada de la parte 1 se vuelve a
  grabar.
- **Los sonidos del clip:** `clip-sitio-equipos/assets/audio/toque-b.wav` y `toque-c.wav` → `recorrido-equipos/assets/audio/`.
- **La música:** la de Academia (§0.1).
- **El kit:** `npm run kit` (monta `identidad/` con `cierre-comercial.html`, los sonidos de acción y el sonido de marca); `frame.md` =
  `identidad/frame-comercial.md`.
- **Las piezas de las escenas:** `tools/ayuda/lib/escenas-equipos.mjs` (`SEGURIDAD`, `ALABANZA`, `ficha`, `funcion`, `servir`, `mi`), las
  mismas del clip.

Dos escenas nuevas, una por dispositivo, sobre Kingdom Demo en español, con `capturar.mjs --modo video` y `toque: false`:

```bash
cd F:/Proyectos/KingdomApp/tools/ayuda
node capturar.mjs clips/recorrido-equipos-celular --idioma es --modo video      # → salida/video/es/clips/recorrido-equipos-celular/
node capturar.mjs clips/recorrido-equipos-escritorio --idioma es --modo video   # → salida/video/es/clips/recorrido-equipos-escritorio/
# cada una: grabacion.mp4 + pasos.json; se copian a recorrido-equipos/assets/grabaciones/celular/ y …/escritorio/
```

Lo que la herramienta ya hace y las escenas usan (sin nada nuevo): `como` e `ir` del primer paso antes de grabar; `como` a mitad de la
escena; `clic`, `marcar`, `escribir` (70 ms por tecla), `ver` (con `bloque`), `espera`, `oculto`, `pausa`; `sql` tras restaurar el volcado;
`refs` con `{@nombre}` (se consultan una vez, en orden, justo antes de abrir Chrome; sin fila, la escena no arranca). Cada escena restaura
la base de capturas desde el volcado: el `sql` de una no ve el de la otra.

**Todo el SQL de §3.2 y §3.3 se probó el 2026-10-30 en la base local de capturas** (`ayuda_capturas_db`, el volcado en inglés de la misma
semilla), en una transacción con `ROLLBACK`: Gabriela queda confirmada en la vacante del próximo domingo (1 fila), en el segundo
Parqueadero del domingo pasado (1 fila), y el voto y la respuesta de Jorge se borran (1 y 1); las referencias dan `falta` = Julián Villa
Jaramillo (Entrada), `way` = 2, `ensayo_vigente` = 1 (el jueves sembrado es el 5 de nov), `servir` = el objetivo 17, `pendiente` = 1,
`no_domingo` = 1 y `t0_primero` = 1.

### 3.2 La escena de celular: `tools/ayuda/escenas/clips/recorrido-equipos-celular.mjs`

```js
// Grabación para el RECORRIDO de Equipos (LegacyHyperframes/videos/kingdomapp/recorrido-equipos/SPEC.md §3.2): la parte 2 en CELULAR.
// NO es una escena de un artículo de la ayuda: no se publica ni entra en la frescura. Una sola escena de CELULAR (390×844 a 3x =
// 1170×2532, 30 cps) grabada SIN el círculo del toque (`toque: false`): el montaje dibuja el suyo sobre las cajas y los toques de pasos.json.
//   node capturar.mjs clips/recorrido-equipos-celular --idioma es --modo video
//   → salida/video/es/clips/recorrido-equipos-celular/grabacion.mp4 + pasos.json
// Tres tramos, en este orden:
//   1. chat (103, Jorge, integrante de Alabanza): el chat de Alabanza con su anuncio anclado; vota «Way Maker» en la encuesta, dice
//      «Asistiré» al ensayo del jueves y escribe un mensaje.
//   2. cerrar (103, ahora líder de Seguridad, sin cambiar de cuenta): «Servir» en la barra de abajo → la tarjeta «Cerrar el turno» → el
//      turno del domingo pasado con Gabriela «Sirvió» → «No llegó» en el de Entrada → «Cerrar el turno» → «1 persona cumplió su objetivo
//      de servir en la ruta».
//   3. gabriela (105): Mi iglesia → «Objetivos» → «Servir» cumplido, con el check que se dibuja.
// Estado previo por SQL (solo en la base local de capturas, que capturar.mjs restaura del volcado en cada corrida): Gabriela entra a
// Seguridad con la habilidad Parqueadero (como en el clip) y queda confirmada en el segundo puesto de Parqueadero del último turno de
// Seguridad por cerrar (la semilla deja «por cerrar» el último domingo); ese turno queda sin marcas; sin apoyo de red en cuadro; el voto y la
// respuesta al ensayo de Jorge se borran para que los haga en cámara. Gabriela ya trae un servicio «sirvió» (Evangelismo) y va en una ruta
// en curso: con este cierre llega a los «2 servicios en 60 días» del objetivo «Servir» de la demo. Datos ficticios.
import { ALABANZA, SEGURIDAD, ficha, funcion, mi, servir } from '../../lib/escenas-equipos.mjs';

const KDEMO = "(SELECT id FROM kd_sedes WHERE codigo = 'KDEMO')";
const SEG = `(${SEGURIDAD})`;
const ALAB = `(${ALABANZA})`;
const PARQ = `(${funcion('Seguridad', 'Security', 'Parqueadero', 'Parking')})`;
const ENTRADA = `(${funcion('Seguridad', 'Security', 'Entrada', 'Entrance')})`;
const GABRIELA = `(${ficha(105)})`;
const JORGE = `(${ficha(103)})`;
// El turno por cerrar: el último de Seguridad entre hace 6 días y ayer (no se graba un domingo: ref `no_domingo`). Envuelto en una tabla
// derivada para poder usarlo en un UPDATE de la misma tabla.
const TC = `(SELECT id FROM (SELECT t.id FROM eq_turnos t WHERE t.id_equipo = ${SEG}
  AND t.fecha BETWEEN CURDATE() - INTERVAL 6 DAY AND CURDATE() - INTERVAL 1 DAY AND t.estado IN ('programado', 'cerrado')
  ORDER BY t.fecha DESC LIMIT 1) tc)`;
const ENCUESTA = `(SELECT e.id FROM eq_encuestas e WHERE e.id_equipo = ${ALAB} AND e.anonima = 0 ORDER BY e.id LIMIT 1)`;
const ENSAYO = `(SELECT id FROM ev_eventos WHERE id_sede = ${KDEMO} AND id_equipo = ${ALAB} ORDER BY id LIMIT 1)`;
const SERVIR_OBJ = `(SELECT id FROM mem_objetivos WHERE id_sede = ${KDEMO} AND nombre IN ('Servir', 'Serve') AND servicio_ref IS NOT NULL LIMIT 1)`;

const ENC = '#chat-hilo [data-encuesta="{@enc}"]';
const REU = '#chat-hilo [data-reunion="{@ensayo}"]';
const FILA_TC = '#tarjeta-por-cerrar [data-cerrar="{@tc}"]';
const FILA_GAB = '#cerrar-personas li.persona[data-persona="{@gabriela}"]';
const FILA_FALTA = '#cerrar-personas li.persona[data-persona="{@falta}"]';
const SERVIR_OK = '#objetivos-conexion li[data-objetivo="{@servir}"][data-estado="cumplido"]';

export default {
  articulo: 'clips/recorrido-equipos-celular',
  movil: true,
  toque: false,
  pantallas: [
    mi('chat.page.ts'), mi('chat-encuesta.component.ts'), mi('chat-reunion.component.ts'), mi('chat-mensaje.component.ts'),
    'frontend-v2/src/app/pages/servir/servir-inicio.page.ts', servir('por-cerrar-tarjeta.component.ts'), servir('cerrar.page.ts'),
    mi('mi-inicio.page.ts'), mi('objetivos.page.ts'), mi('objetivos-conexion.component.ts'),
    'frontend-v2/src/app/layout/shell/navegacion.ts',
  ],
  sql: [
    // Gabriela, integrante de Seguridad desde hace 90 días, con la habilidad Parqueadero (lo mismo que el clip).
    `INSERT IGNORE INTO eq_integrantes (id_sede, id_equipo, id_persona, rol, estado, desde, por, decidido_por, decidido_at, created_at)
     SELECT ${KDEMO}, ${SEG}, ${GABRIELA}, 'integrante', 'activo', CURDATE() - INTERVAL 90 DAY, 103, 103, NOW() - INTERVAL 90 DAY, NOW() - INTERVAL 90 DAY`,
    `INSERT IGNORE INTO eq_habilidades (id_integrante, id_funcion)
     SELECT i.id, ${PARQ} FROM eq_integrantes i WHERE i.id_equipo = ${SEG} AND i.id_persona = ${GABRIELA}`,
    // El turno por cerrar, sin cerrar y sin marcas (si el volcado lo trae cerrado).
    `UPDATE eq_turnos SET estado = 'programado', cerrado_por = NULL, cerrado_at = NULL WHERE id = ${TC}`,
    `UPDATE eq_asignaciones SET sirvio = NULL, sirvio_por = NULL, sirvio_at = NULL WHERE id_turno = ${TC}`,
    // Sin «Redes y solicitudes» en cuadro (en el sitio es Próximamente): ningún apoyo de red de esta semana ni de la que viene.
    `UPDATE eq_asignaciones SET origen = 'equipo', id_red = NULL WHERE id_sede = ${KDEMO} AND origen = 'red' AND fecha >= CURDATE() - INTERVAL 7 DAY`,
    // Gabriela en el segundo puesto de Parqueadero de ese turno, confirmada (toma el lugar del último confirmado de Parqueadero).
    `UPDATE eq_asignaciones a JOIN (SELECT a2.id FROM eq_asignaciones a2 JOIN eq_puestos pu ON pu.id = a2.id_puesto
        WHERE a2.id_turno = ${TC} AND pu.id_funcion = ${PARQ} AND a2.estado = 'confirmada' ORDER BY pu.orden DESC, a2.id DESC LIMIT 1) x ON x.id = a.id
     SET a.id_persona = ${GABRIELA}, a.origen = 'equipo', a.id_red = NULL`,
    // Jorge vota y responde en cámara: fuera su voto de la semilla y su respuesta al ensayo.
    `DELETE FROM eq_encuesta_votos WHERE id_persona = ${JORGE} AND id_encuesta IN (SELECT id FROM eq_encuestas WHERE id_equipo = ${ALAB})`,
    `DELETE FROM eq_reunion_respuestas WHERE id_persona = ${JORGE} AND id_evento IN (SELECT id FROM ev_eventos WHERE id_equipo = ${ALAB})`,
  ],
  refs: {
    seg: SEGURIDAD,
    alab: ALABANZA,
    gabriela: ficha(105),
    // Sin fila (NULL), la escena no arranca:
    no_domingo: `SELECT IF(DAYOFWEEK(CURDATE()) = 1, NULL, 1)`,                       // un domingo, el turno de hoy sería el del clip y el que se cierra
    tc: `SELECT t.uuid FROM eq_turnos t WHERE t.id = ${TC}`,
    en_tc: `SELECT a.id FROM eq_asignaciones a WHERE a.id_turno = ${TC} AND a.id_persona = ${GABRIELA} AND a.estado = 'confirmada'`,
    falta: `SELECT a.id_persona FROM eq_asignaciones a JOIN eq_puestos pu ON pu.id = a.id_puesto
            WHERE a.id_turno = ${TC} AND pu.id_funcion = ${ENTRADA} AND a.estado = 'confirmada' ORDER BY pu.orden, a.id LIMIT 1`,
    enc: `SELECT ${ENCUESTA}`,
    way: `SELECT o.id FROM eq_encuesta_opciones o WHERE o.id_encuesta = ${ENCUESTA} AND o.texto = 'Way Maker'`,
    ensayo: `SELECT ${ENSAYO}`,
    // El jueves sembrado no pasó (si pasó, la tarjeta ya no trae «Asistiré» de nadie: se vuelve a sembrar el volcado).
    ensayo_vigente: `SELECT IF(MIN(fecha) >= CURDATE(), 1, NULL) FROM eq_reunion_respuestas WHERE id_evento = ${ENSAYO}`,
    servir: `SELECT ${SERVIR_OBJ}`,
    // Gabriela va en una ruta en curso, no tiene «Servir» y lleva exactamente 1 servicio «sirvió» en 60 días: el cierre la lleva a 2.
    pendiente: `SELECT IF(COUNT(DISTINCT a.id_turno) = 1, 1, NULL) FROM eq_asignaciones a
                  JOIN mem_persona_ruta r ON r.id_persona = a.id_persona AND r.estado = 'en_curso'
                 WHERE a.id_persona = ${GABRIELA} AND a.sirvio = 'si' AND a.fecha >= CURDATE() - INTERVAL 59 DAY
                   AND NOT EXISTS (SELECT 1 FROM mem_persona_objetivos po WHERE po.id_persona = a.id_persona AND po.id_objetivo = ${SERVIR_OBJ})`,
  },
  pasos: [
    // ── 1. El chat de Alabanza (P10). La entrada se hace antes de grabar; la app deja la encuesta en el centro (lo que se ve en el 1320).
    { tramo: 'chat', como: 103, ir: '/mi/equipos/{@alab}', espera: ENC },
    { ver: ENC, bloque: 'center', pausa: 300 },
    { ver: '#chat-anclado', bloque: 'nearest', pausa: 3500 },                 // caja del anuncio anclado (el 1320) y la espera del 1380
    { ver: ENC, bloque: 'nearest', pausa: 200 },                              // caja de la encuesta (objetivo del 1380)
    { tramo: 'voto', clic: `${ENC} [data-opcion="{@way}"]`, pausa: 1800 },     // «Way Maker» (1440)
    { tramo: 'ensayo', ver: REU, bloque: 'center', pausa: 1800 },             // la app baja al ensayo (1500)
    { tramo: 'asistire', clic: `${REU} [data-asistire="{@ensayo}"]`, pausa: 3600 },   // «Asistiré» (1560) → «N van» (1563)
    { ver: '#chat-texto', bloque: 'nearest', pausa: 200 },                    // caja de la caja de escribir (objetivo del 1620)
    { tramo: 'mensaje', clic: '#chat-texto', pausa: 100 },                    // el toque del 1680
    { escribir: { en: '#chat-texto', texto: '¡Cuenten conmigo el jueves!' }, pausa: 300 },   // 1683–1738
    { tramo: 'enviar', clic: '#chat-enviar', pausa: 2000 },                   // 1740 → su mensaje (1743)
    { ver: '#nav-ir-servir', bloque: 'nearest', pausa: 200 },                 // caja de «Servir» en la barra de abajo (objetivo del 1770)

    // ── 2. Servir cuenta (P11). Jorge sigue en su cuenta: «Servir» está en su barra de Mi iglesia (navegacion.ts → navMi).
    { tramo: 'servir', clic: '#nav-ir-servir', espera: FILA_TC, pausa: 300 },             // 1800
    { ver: '#tarjeta-por-cerrar', bloque: 'nearest', pausa: 3800 },                       // caja de la tarjeta (1860) y el redoble
    { tramo: 'cerrar', clic: FILA_TC, espera: `${FILA_GAB}[data-marca="si"]`, pausa: 300 }, // 1920 → la lista
    { ver: FILA_GAB, bloque: 'nearest', pausa: 3500 },                                    // caja de la fila de Gabriela (1980)
    { tramo: 'no-llego', clic: `${FILA_FALTA} [data-marcar="no"]`, pausa: 2000 },         // 2040
    { ver: '#cerrar-enviar', bloque: 'nearest', pausa: 1800 },                            // caja de la barra (2100)
    { tramo: 'cerrar-turno', clic: '#cerrar-enviar', espera: 'mat-dialog-container #btn-ok', pausa: 4000 },   // 2160 → el aviso (2175)
    { clic: 'mat-dialog-container #btn-ok', oculto: 'mat-dialog-container' },             // fuera de cámara: «Entendido»

    // ── 3. Gabriela (P12). El cambio de cuenta queda debajo del látigo del 2270–2280.
    { tramo: 'gabriela', como: 105, ir: '/mi', espera: '#nav-objetivos', pausa: 2000 },   // «Buenas tardes, Gabriela» (2280)
    { ver: '#nav-objetivos', bloque: 'nearest', pausa: 200 },                             // caja de «Objetivos» (objetivo del 2310)
    { tramo: 'objetivos', clic: '#nav-objetivos', espera: SERVIR_OK, pausa: 15000 },      // 2340 → el check (2359–2369) → hasta el 2759
  ],
};
```

**Comprobaciones obligatorias al grabar** (si una falla, se vuelve a grabar):
1. La encuesta sube **una** cuenta en «Way Maker» con el toque (en la base de prueba, de 7 a 8) y «Asistiré» queda lleno con «N van»
   uno más (de 9 a 10). Si la cuenta tarda (la respuesta va por la cola del chat), el cuadro del 1563 se toma del primero en que cambia.
2. «Cerrar el turno» abre con **Gabriela marcada «Sirvió»** y la fila de `falta` **no** es la de ella.
3. **El aviso dice «1 persona cumplió su objetivo de servir en la ruta.»** Si no sale (el cierre devolvió `objetivos: 0`), la ref
   `pendiente` dio 1 pero la ruta no lo marcó: se revisa que Equipos esté «empezado» en la demo (`eq_config.desde`) y que el objetivo siga
   ligado (`mem_objetivos.servicio_ref`); no se fabrica el aviso.
4. En «Mis objetivos», «Servir» sale **cumplido con el check dibujándose** después del toque. Si la animación no se ve (el equipo de
   grabación con «menos movimiento»), el check aparece entero: el `confirmacion` va en el cuadro en que aparece y se anota.
5. Ningún cuadro usado muestra «Red …», «Abierto a redes» ni «Vacantes abiertas».

### 3.3 La escena de escritorio: `tools/ayuda/escenas/clips/recorrido-equipos-escritorio.mjs`

```js
// Grabación para el RECORRIDO de Equipos (LegacyHyperframes/videos/kingdomapp/recorrido-equipos/SPEC.md §3.3): la parte 2 en ESCRITORIO.
// NO es una escena de un artículo de la ayuda. En video el escritorio es 1280×720 a 1,5x (1920×1080 reales, 30 cps), sin cursor ni círculo
// (`toque: false`): el montaje dibuja su marca de toque sobre las cajas de pasos.json.
//   node capturar.mjs clips/recorrido-equipos-escritorio --idioma es --modo video
//   → salida/video/es/clips/recorrido-equipos-escritorio/grabacion.mp4 + pasos.json
// Una cuenta: 101, el administrador (servicio.reportes sobre la sede). La cobertura de la iglesia del próximo domingo (P9): el total,
// Seguridad completo con Gabriela confirmada, y «Solo lo que falta».
// Estado previo por SQL (solo en la base local de capturas): lo que dejó la parte 1 del video. Gabriela entra a Seguridad con la habilidad
// Parqueadero y queda CONFIRMADA en el puesto vacante de Parqueadero del próximo domingo (en el clip lo aceptó); sin apoyo de red en
// cuadro. Datos ficticios.
import { ALABANZA, SEGURIDAD, ficha, funcion, servir } from '../../lib/escenas-equipos.mjs';

const KDEMO = "(SELECT id FROM kd_sedes WHERE codigo = 'KDEMO')";
const SEG = `(${SEGURIDAD})`;
const PARQ = `(${funcion('Seguridad', 'Security', 'Parqueadero', 'Parking')})`;
const GABRIELA = `(${ficha(105)})`;
// El turno de Seguridad del próximo domingo (el del clip).
const T0 = `(SELECT t.id FROM eq_turnos t WHERE t.id_equipo = ${SEG} AND t.fecha >= CURDATE() ORDER BY t.fecha LIMIT 1)`;
const SEC_SEG = '#cobertura-reunion section.equipo[data-equipo="{@seg}"]';
const SEC_ALAB = '#cobertura-reunion section.equipo[data-equipo="{@alab}"]';

export default {
  articulo: 'clips/recorrido-equipos-escritorio',
  toque: false,
  pantallas: [servir('cobertura.page.ts')],
  sql: [
    `INSERT IGNORE INTO eq_integrantes (id_sede, id_equipo, id_persona, rol, estado, desde, por, decidido_por, decidido_at, created_at)
     SELECT ${KDEMO}, ${SEG}, ${GABRIELA}, 'integrante', 'activo', CURDATE() - INTERVAL 90 DAY, 103, 103, NOW() - INTERVAL 90 DAY, NOW() - INTERVAL 90 DAY`,
    `INSERT IGNORE INTO eq_habilidades (id_integrante, id_funcion)
     SELECT i.id, ${PARQ} FROM eq_integrantes i WHERE i.id_equipo = ${SEG} AND i.id_persona = ${GABRIELA}`,
    `UPDATE eq_asignaciones SET origen = 'equipo', id_red = NULL WHERE id_sede = ${KDEMO} AND origen = 'red' AND fecha >= CURDATE()`,
    `UPDATE eq_puestos SET abierto_redes = 0 WHERE id_turno IN (SELECT t.id FROM eq_turnos t WHERE t.id_sede = ${KDEMO} AND t.fecha >= CURDATE())`,
    // Lo que dejó el clip: Gabriela confirmada en el puesto de Parqueadero que estaba vacante (la semilla lo deja vacante).
    `INSERT INTO eq_asignaciones (uuid, id_sede, id_equipo, id_turno, id_puesto, fecha, id_persona, estado, respondida_at, respondida_por,
                                  respondida_como, origen, asignada_por, avisada_at, created_at)
     SELECT UUID(), t.id_sede, t.id_equipo, t.id, pu.id, t.fecha, ${GABRIELA}, 'confirmada', NOW() - INTERVAL 1 HOUR, 105, 'persona', 'equipo',
            103, NOW() - INTERVAL 2 HOUR, NOW() - INTERVAL 2 HOUR
       FROM eq_turnos t JOIN eq_puestos pu ON pu.id_turno = t.id AND pu.id_funcion = ${PARQ}
      WHERE t.id = ${T0} AND NOT EXISTS (SELECT 1 FROM eq_asignaciones a WHERE a.puesto_vigente = pu.id)
      ORDER BY pu.orden LIMIT 1`,
  ],
  refs: {
    seg: SEGURIDAD,
    alab: ALABANZA,
    gabriela: ficha(105),
    // Sin fila, no arranca: Gabriela quedó confirmada en el turno del domingo, y ese domingo es la primera reunión de la cobertura.
    en_t0: `SELECT a.id FROM eq_asignaciones a WHERE a.id_turno = ${T0} AND a.id_persona = ${GABRIELA} AND a.estado = 'confirmada'`,
    t0_primero: `SELECT IF(MIN(t.fecha) = (SELECT t2.fecha FROM eq_turnos t2 WHERE t2.id = ${T0}), 1, NULL) FROM eq_turnos t
                  WHERE t.id_sede = ${KDEMO} AND t.fecha >= CURDATE() AND t.id_evento IS NOT NULL AND t.estado <> 'cancelado'`,
    // Informativa: Seguridad completo (en la base de prueba, 5 de 5).
    seg_confirmados: `SELECT COUNT(*) FROM eq_asignaciones WHERE id_turno = ${T0} AND estado = 'confirmada'`,
  },
  pasos: [
    // La entrada se hace antes de grabar: el video abre en la cobertura del próximo domingo («Por reunión», la pestaña por defecto).
    { tramo: 'cobertura', como: 101, ir: '/servir/equipos/cobertura', espera: SEC_SEG, pausa: 300 },
    { ver: '#cobertura-total', bloque: 'center', pausa: 2200 },                         // 830–899: el total y la barra
    { tramo: 'seguridad', ver: SEC_SEG, bloque: 'center', pausa: 300 },                 // 900: la app baja a Seguridad
    { ver: `${SEC_SEG} li.puesto:has-text("Gabriela")`, bloque: 'nearest', pausa: 3800 },   // caja de Gabriela (objetivo del 960)
    { tramo: 'arriba', ver: '#cobertura-total', bloque: 'center', pausa: 1500 },        // 1035: la app vuelve arriba
    { ver: '#cobertura-falta', bloque: 'nearest', pausa: 200 },                         // caja del interruptor (objetivo del 1050)
    { tramo: 'falta', clic: '#cobertura-falta button', oculto: SEC_SEG, pausa: 300 },   // 1080 → solo lo que falta (1083)
    { ver: SEC_ALAB, bloque: 'nearest', pausa: 8500 },                                  // caja de Alabanza (1140) y el resto del plano
  ],
};
```

**Comprobaciones al grabar:** el selector dice el **domingo del clip** («Dom, 1 de nov · Servicio General · 9:00 a. m.») si se graba antes
del 1 de noviembre; después de esa fecha dice el domingo siguiente (ninguna frase depende de la fecha; la de K y la de E no se comparan en
pantalla). Seguridad dice **«5/5 · 100 %»** con Gabriela «Confirmado»; con «Solo lo que falta», Seguridad no está y sí Alabanza; ningún
puesto dice «Red …». Si el interruptor no responde al `clic` en su `button` (la estructura de `mat-slide-toggle`), se usa
`#cobertura-falta label` y se anota.

### 3.4 Selectores, verificados el 2026-10-30 en `frontend-v2/src/app/pages/` (y `layout/shell/`)

- **Chat** (`mi/chat.page.ts`, ruta `/mi/equipos/:id`; los usan `escenas/mi-iglesia/el-chat-de-mi-equipo.mjs` y
  `escenas/equipos/encuestas-y-reuniones-del-equipo.mjs`): `#chat-anclado`, `#chat-hilo`, `#chat-texto`, `#chat-enviar`. **Encuesta**
  (`mi/chat-encuesta.component.ts`): `[data-encuesta]` (id de `eq_encuestas`), cada opción `button.opcion[data-opcion]` (id de
  `eq_encuesta_opciones`), `[data-votos]`. **Reunión** (`mi/chat-reunion.component.ts`): `[data-reunion]` (id del evento), `[data-asistire]`,
  `[data-no-asistire]`, `.conteo[data-van]`.
- **Barra de abajo** (`layout/shell/navegacion.ts` → `navMi`): en Mi iglesia, `#nav-objetivos` (si la iglesia tiene «Mis objetivos») y
  `#nav-ir-servir` (para quien también tiene Servir). La hoja de la grabación del clip muestra la barra de Gabriela: Inicio · Comunidades ·
  Cursos · **Objetivos**.
- **Servir** (`servir/servir-inicio.page.ts` con `equipos/por-cerrar-tarjeta.component.ts`): `#tarjeta-por-cerrar`, `#por-cerrar-n`, cada
  fila `a.fila[data-cerrar="{uuid del turno}"]` (la usa `escenas/equipos/cerrar-el-turno.mjs`).
- **Cerrar el turno** (`equipos/cerrar.page.ts`, `/servir/equipos/:id/turno/:clave/cerrar`): `#cerrar-titulo`, `#cerrar-momento`,
  `#cerrar-resumen`, `#cerrar-personas li.persona[data-persona][data-marca]`, `[data-marcar="si"|"no"]`, `#cerrar-barra` (fija abajo),
  `#cerrar-enviar`; el aviso es `dialog.success` (`components/app-dialog.component.ts`: `mat-dialog-container`, `#btn-ok`) con
  `eq4.cerrado_ok` y `eq4.objetivos_cumplidos_one`, solo si el cierre devuelve `objetivos > 0`.
- **Mis objetivos** (`mi/objetivos.page.ts` con `mi/objetivos-conexion.component.ts`, `/mi/objetivos`): `#objetivos-conexion`,
  `li[data-objetivo][data-estado="cumplido"]` con `svg.check` (el círculo `k-escala` 320 ms y el trazo `po6-trazo` 320 ms después) y
  «Cumplido el {fecha}» (`po6.o_cumplido_el`).
- **Cobertura** (`equipos/cobertura.page.ts`, `/servir/equipos/cobertura`; la usa `escenas/equipos/reportes.mjs`): `#cobertura-reunion`,
  `#cobertura-elegir`, `#cobertura-falta` (`mat-slide-toggle`), `#cobertura-total`, `section.equipo[data-equipo]` con `.cifra[data-color]` y
  `li.puesto[data-semaforo="verde"|"ambar"|"rojo"]`. Con «Solo lo que falta», un equipo completo no sale (`eqRepCoberturaReunion`).
- **SQL:** `eq_integrantes`, `eq_habilidades`, `eq_turnos` (`estado`, `cerrado_por`, `cerrado_at`), `eq_puestos` (`abierto_redes`),
  `eq_asignaciones` (`puesto_vigente` generada y única, `sirvio`, `origen`, `id_red`), `eq_encuestas` / `eq_encuesta_opciones` /
  `eq_encuesta_votos`, `eq_reunion_respuestas` (`id_evento`, `fecha`, `id_persona`), `mem_persona_ruta`, `mem_objetivos`
  (`servicio_ref`), `mem_persona_objetivos`: migraciones 090–097.

### 3.5 El proyecto

`recorrido-equipos/` con `BRIEF.md` (`tipo: comercial`, `subtipo: clip-del-sitio`, `recorrido: equipos`, `aspect: 16:9`), `frame.md`
(= `identidad/frame-comercial.md`), `hyperframes.json` y `package.json` copiados del clip con dos scripts: `"kit"` y `"musica"` (§0.1).
`assets/grabaciones/{parqueadero,celular,escritorio}/`, `assets/stills/` (los dos del clip), `assets/audio/` (toque-b y toque-c),
`assets/musica/product-launch-recorrido.wav`. Composiciones: `fondo`, `frase-1` … `frase-9`, `ceja` (con sus dos lugares); en la raíz,
`#escena` con las dos ventanas, la tira vertical, los tramos de video, las cámaras, los iris, las marcas, el cambio de ventana, el dip, la
música y los sonidos. Si `check` avisa `composition_file_too_large`, se deja (como el clip) o cada mundo pasa a una subcomposición del
tamaño de su ventana; la línea de tiempo no cambia.

**Entregables:** `renders/recorrido-equipos-16x9.mp4` (1920×1080, 30 fps, 2910 cuadros, H.264 + AAC 48 kHz, −16 LUFS) para YouTube y
presentaciones, y para la página `/equipos` una versión **1280×720** (H.264 y WebM) con su póster (el cuadro 0) en AVIF y WebP, con
`preload="none"` (lo decide la entrega del sitio, como Academia).

---

## 4. Lo que se revisa en la vista previa

Cuadros a mirar (a mitad de cuadro: `(n + 0,3) / 30`, REVIEW del clip §6): `npx hyperframes snapshot --at
0.01,1.51,2.61,4.11,5.11,6.11,8.11,10.11,12.11,12.61,13.51,15.11,16.51,20.11,22.11,23.51,24.51,27.91,28.01,28.41,30.51,32.51,34.51,36.21,37.01,39.01,41.01,43.91,44.01,44.51,46.51,48.11,50.21,52.11,52.41,54.51,56.51,57.91,58.21,59.51,60.11,60.51,62.51,64.21,66.51,68.11,70.51,72.11,72.61,73.51,75.91,76.01,76.51,77.51,78.21,79.01,80.51,82.51,84.01,84.51,90.01,91.91,92.01,92.41,96.91`,
y `snapshot --range` de 16 cuadros sobre cada transición: 2.4–2.9 (match cut), 3.9–4.3 (iris), 11.8–12.3 (látigo), 12.4–12.8 (iris),
21.8–22.3 (látigo), **27.6–28.1, 43.6–44.1** (látigos horizontales), **59.9–60.4** (corte sobre «Servir»), **63.9–64.3** (iris),
**75.6–76.1** (látigo vertical), **77.9–78.4** (corte sobre «Objetivos»), 91.8–92.1 (dip y cierre).

1. **Parte 1 (0–27,9):** lo mismo que el §4 del clip, con la ventana del celular a la derecha y las frases a la izquierda; el texto de la
   app ≥ 28 px en todos los encuadres (el general a 1,085); «paleta», «tarjeta» y «turnoCabeza» sin cortes en los bordes; en el 24,5,
   «Y el domingo, completo.» entera con «5 de 5» legible y Gabriela «Confirmado» fuera de la píldora; la ventana a escala 1 hasta el 28,0.
2. **Los látigos horizontales** (28,0 y 44,0): ningún cuadro con las dos ventanas vacías ni con una a medio camino quieta; a la izquierda
   al escritorio, a la derecha de vuelta; la frase anterior ya no está en el golpe y la nueva empieza en el +2; la ceja cambia de lugar con
   blur, nunca se desliza.
3. **La cobertura (28–44):** las pestañas fuera de cuadro en todo el plano; «13 de 19 confirmados (68 %)» legible en el 28,4; en el 30,5
   Seguridad «5/5 · 100 %» y **Gabriela «Confirmado»** a ≥ 28 px (31,5 en D⁺ desde el 32,5); la cámara quieta mientras la app se mueve
   (30,0 y 34,5); en el 36,2 Seguridad ya no está y Alabanza sí, con sus puntos rojos y ámbar; texto ≥ 28 px (D = 1,8); «Datos de ejemplo»
   a la vista con cada cifra.
4. **El chat (44–60):** el anuncio anclado legible en el 44,5; la encuesta en M en el 46,5; en el 48,1 «Way Maker» marcada y su cuenta
   +1; en el 50,2 la tarjeta del ensayo centrada en lo que ve la cámara; **«Asistiré» lleno en el 52,1 y el punch terminado en el 52,4**,
   con «N van» +1 a ≥ 36 px; «¡Cuenten conmigo el jueves!» entero en la caja en el 57,9 y en el hilo en el 58,2; «Servir» a la vista en la
   barra de abajo en el 59,5.
5. **Servir cuenta (60–76):** en el 60,1 el inicio de Servir ya está (el corte sobre el toque, sin el cargador ni la pantalla anterior);
   en el 62,5 la tarjeta legible **sin la fecha**; nada se mueve entre el 62,5 y el 63,9 (el redoble); el iris del 64,0 nace en la fila;
   en el 66,5 la fila de Gabriela con «Sirvió» marcado a ≥ 36 px; en el 68,1 la otra fila en rojo; en el 70,5 la barra «Cerrar el turno»;
   **en el 72,6 el aviso «1 persona cumplió su objetivo de servir en la ruta.» entero y legible**.
6. **Gabriela (76–92):** en el 76,5 «Buenas tardes, Gabriela» (o «días») legible; «Objetivos» a la vista en el 77,5; en el 78,2 «Mis
   objetivos» sin esqueleto; **el check de «Servir» termina de dibujarse en el 78,9 ± 1 cuadro** y suena la `confirmacion`; en el 80,5
   «Servir» y «Cumplido el …» a ≥ 46 px; la frase del sitio entera en el 84,5 en tres líneas con *cubierto* dorada y la ventana a 0,92;
   nada se mueve del 85,0 al 91,8 salvo el halo; dip 91,9; **92,0 el primer cuadro del cierre** sin noche vacía.
7. **La música (oída, no solo medida):** la costura del **32,0** no se oye (28–36 con audífonos dos veces; si se oye, se prueba el cruce a
   20 ms y a 50 ms del golpe antes de tocar el lugar); el último acorde se apaga debajo del cierre sin cortarse; las campanas se oyen en el
   92,38. `npx hyperframes beats assets/musica/product-launch-recorrido.wav`: la grilla de 0,5 s sin un pulso doble ni uno perdido entre el
   31,0 y el 33,0.
8. **Sonido (medido):** cada `toque` y cada `aparicion` un cuadro después de su imagen; los golpes de `hyperframes audio` sobre el render
   en los cuadros de §1.7; **−16 LUFS** integrada (±1), pico real ≤ −1 dBTP; ningún par encimado salvo 1080 + 1083, 1560 + 1563 y
   1740 + 1743.
9. **Textos:** ninguna palabra que no esté en la app, en las nueve frases o en el cierre; nada de «Red …», «Abierto a redes», «Vacantes
   abiertas» ni «Por red» legible; `npx hyperframes check` en 0 errores.
10. **La historia sin sonido** (así se ve en el sitio hasta que se toca el botón): el domingo con uno por cubrir → Kingdom sugiere a
    Gabriela → la avisa → ella ve a qué hora llegar y acepta → «5 de 5» → toda la iglesia: Gabriela en verde y solo lo que falta → el chat
    del equipo: vota, «Asistiré», escribe → cerrar el turno: Gabriela «Sirvió» → «1 persona cumplió su objetivo» → el celular de Gabriela:
    «Servir» cumplido → Kingdom.

---

## 5. Riesgos y lo que se decide al grabar

- **El turno que se cierra es el domingo pasado de la base**, no el 1 de noviembre del clip (la base no trae un domingo del clip ya
  servido). Su fecha está en la fila de la tarjeta («Dom, 25 de oct» en la base de prueba) y encima del título de «Cerrar el turno»: los
  encuadres de 1860 y 1920 la dejan fuera (BANNED 40). Si la fila es tan angosta que la fecha entra en M, la cámara del 1860 va a C sobre el
  nombre «Seguridad · Servicio General» y se anota.
- **No se graba un domingo** (la ref `no_domingo` lo impide): el turno de hoy sería el del clip y el que se cierra a la vez, y Gabriela
  quedaría dos veces.
- **La cobertura y el clip hablan del mismo domingo solo si se graba antes del 2026-11-01.** Después, E muestra el domingo siguiente y C
  cierra el del 1 de noviembre; ninguna frase depende de la fecha, y si el domingo siguiente de la base no tiene la vacante en Parqueadero
  (la semilla la deja solo en el próximo), `en_t0` da NULL y la escena se niega: se vuelve a sembrar el volcado (`semilla.mjs`) para que
  «el próximo domingo» vuelva a ser el de la semilla.
- **El ensayo sembrado vence el jueves** que la semilla eligió (el 5 de nov en la base de prueba): `ensayo_vigente` se niega después y se
  vuelve a sembrar.
- **El objetivo depende de la semilla:** Gabriela debe ir en una ruta en curso, sin «Servir» y con 1 servicio en 60 días (`pendiente`).
  Si otra persona del turno también cumple al cerrar, el aviso dice «2 personas…»: la frase no depende del número, se graba igual y se
  anota.
- **«Asistiré» y el voto van por la cola del chat** (funcionan sin señal y se envían): con la API local llegan en < 1 s; el cuadro del
  cambio (1563) se toma del real. Si aparece el reloj de «enviando», se corta en la espera.
- **La animación del check** (640 ms) es la parte más fina del final: el `data-media-start` del tramo `objetivos` se ajusta para que el
  trazo se cierre en el 2369; si el inicio de «Mis objetivos» trae primero el esqueleto, se corta en la espera (el esqueleto no se ve).
- **El escritorio se lee solo de cerca** (D = 1,8 deja ver 711 × 375 px CSS): cada encuadre de la cobertura se elige con la grabación y se
  anota. Las tarjetas de los equipos son una columna de hasta 1024 px; Alabanza con sus siete puestos puede no caber entera en D: se
  encuadra su cabecera y los puntos rojos.
- **La costura de la música** es la de Academia, medida y no oída: es lo primero que se escucha en la vista previa (§4.7).
- **Densidad:** el chat tiene cinco acciones en 8 s (anclado, voto, ensayo, «Asistiré», mensaje). Si en la vista previa va atropellado, la
  válvula es quitar el mensaje (1680–1743): la cámara baja a la barra en el 1680 y el plano queda con el voto y el «Asistiré».
- **El README pide 60–75 s para el recorrido**; este dura 97 por decisión del dueño (~100 s, la serie). Se anota en
  `KingdomApp/docs/videos/README.md` al publicar.
- **Idiomas (en, pt después):** las dos escenas con `--idioma en` graban la interfaz en inglés (los equipos y las funciones salen en inglés;
  la encuesta y el ensayo de la demo siguen en español en el volcado en inglés: se revisa antes de grabar en inglés). Las frases se
  traducen y los saltos se vuelven a fijar; el cierre lleva `idioma`.
