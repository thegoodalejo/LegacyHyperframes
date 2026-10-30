# SPEC v2 · Clip del sitio: Membresía — «Valeria llegó el domingo»

2026-10-30 · **Versión 2: la ampliación** ([STORY.md](STORY.md) → §Ampliación). La v1 (Historia A tal cual, 30,5 s) se construyó y se publicó
el mismo día ([REVIEW.md](REVIEW.md)); el dueño pidió después unos 10 s más para mostrar que la persona nueva **tiene una ruta de
crecimiento y objetivos de conexión**, y ya no revisa guiones: la dirección creativa decide. Este documento sigue siendo el contrato de
construcción: cada adjetivo es un número, los valores por defecto están prohibidos con nombre y los planos van cuadro por cuadro. **Lo de 0
a 24,0 s (cuadros 0–719) queda como se construyó**; lo nuevo empieza en el toque «Listo» del 720.

```text
GOAL:    Un pastor que no conoce Kingdom termina pensando «llegó el domingo, el lunes alguien la llamó y ya tiene un camino» y toca «Prueba gratis 30 días».
OUTPUT:  HyperFrames · dos composiciones de la misma línea de tiempo: 1080×1350 (4:5, sitio y feed) y 1080×1920 (9:16, Reels e historias) · 30 fps.
TIME:    38,5 s = 1155 cuadros: cuerpo 0–36,0 (cuadros 0–1079) + firma 36,0–38,5 (1080–1154). 120 BPM = 15 cuadros por pulso (grilla real abajo).
         (v1: 30,5 s = 915 cuadros, firma en el 840.)
LOOK:    noche del sitio (#060D1F) con el halo y la retícula de puntos del kit; tinta #EAF0FF; un solo acento, el dorado #E8B95A, en tres
         lugares y no más (la ceja «MEMBRESÍA», la palabra «ninguna» y el botón de la firma). Fraunces 560 / −0,02 em para las frases;
         Inter para la ceja y «Datos de ejemplo». El medio: la app REAL de Kingdom Demo grabada en celular, nítida (1170 px de ancho),
         dentro de una ventana con radio 28, anillo de 1 px y sombra 0 40 80 −24 al 65 %; nunca un teléfono dibujado.
OBJECTS: la ventana (el celular de quien registra; tras el látigo, el de quien acompaña: Mi seguimiento y, desde el 780, la ficha de
         Valeria); el punto de toque de la grabación; las cinco frases; la ceja; la píldora «Datos de ejemplo»; la corona del cierre.
MOTION:  curvas por papel (§1.6); un movimiento de cámara por compás (14 cuadros, power2.inOut), quieto después; cada corte y cada
         entrada en un pulso; cada cambio de mundo en un golpe (120 · 180 · 600 · 660 · 720 · 780 · 840 · 960 · 1080).
SHOTS:   nueve planos (§2).
BANNED:  §1.8.
QA:      §4.
```

---

## 0. El reloj: la grilla real de la pista

La música es «Product Launch» (The_Mountain) del **14,05 al 50,05 s** (v1: hasta el 42,05). t = 0 del clip ↔ 14,05 de la pista. Los pulsos
vienen de `_identidad/musica/product-launch-the-mountain.pulsos.json` restándoles 14,05 y redondeando a 30 fps: **todos caen en el múltiplo
de 15 cuadros salvo el 9,455 s, que cae en el cuadro 284** (uno antes del 285 ideal; no hay ningún evento ahí). Los cuadros de abajo son los
que se usan; nunca se suma 15 repetidamente (deriva), cada pulso se calcula desde su índice.

| Compás | Cuadros | Pulsos (cuadro · fuerza) | Intensidad del compás | Lo que le toca al video |
|---|---|---|---|---|
| 1 | 0–59 | 0 ·0,69 · 15 ·0,64 · 30 ·0,49 · 45 ·0,48 | 0,57 | El gancho: la app ya trabajando, la frase 1 palabra por pulso |
| 2 | 60–119 | 60 ·0,58 · 75 ·0,55 · 90 ·0,57 · 105 ·0,61 | 0,58 | Cierra un campo por pulso; la pantalla baja a «Registrar» |
| 3 | 120–179 | **120 ·0,93** (entra el bajo) · 135 · 150 · 165 | 0,66 | El toque en «Registrar»: Kingdom entra. Frase 2 |
| 4 | 180–239 | **180 ·0,87** (pico) · 195 ·0,83 · 210 · 225 | **0,77** | El látigo al otro celular; la tarjeta de Valeria; la ceja |
| 5 | 240–299 | **240 ·0,92** · 255 ·0,77 · 270 · 284 | 0,70 | Acercamiento 1 (la llamada, el semáforo) |
| 6 | 300–359 | 300 ·0,77 · 315 ·0,75 · 330 · 345 | 0,68 | Acercamiento 2 («Después: …») y vuelta |
| 7 | 360–419 | 360 ·0,76 · 375 ·0,64 · 390 · 405 | 0,59 | Frase 3; toque «Marcar cumplido» |
| 8 | 420–479 | 420 ·0,75 · 435 ·0,61 · 450 · 465 | 0,59 | El reporte: «Contestó» |
| 9 | 480–539 | 480 ·0,67 · 495 ·0,67 · 510 · 525 | 0,59 | El comentario se escribe |
| 10 | 540–599 | 540 ·0,63 · 555 · 570 ·0,61 · 585 ·0,68 | 0,62 | El dedo baja al botón del diálogo |
| 11 | 600–659 | **600 ·0,93** (segunda subida) · 615 ·0,69 · 630 · 645 | 0,66 | Toque «Marcar cumplido» del diálogo: cumplido. Frase 3 sale |
| 12 | 660–719 | **660 ·0,90** · 675 ·0,89 · 690 ·0,76 · 705 ·0,68 | **0,81** | Acercamiento a «Ahora va en: …» (la prueba más fuerte del seguimiento) |
| 13 | 720–779 | **720 ·0,96** · 735 ·0,77 · 750 · 765 | 0,73 | Toque «Listo»; la tarjeta al día se lee |
| 14 | 780–839 | **780 ·0,88** · 795 ·0,74 · 810 · 825 | 0,71 | **Toque en el nombre → iris → la ficha de Valeria**; acercamiento a la fila «Avance» |
| **15** | **840–899** | **840 ·1,00 (el más fuerte de la pista)** · 855 ·0,68 · 870 ·0,51 · 885 ·0,52 | 0,68 | **Toque en «Avance»: la ruta se abre de golpe. Frase 4** |
| 16 | 900–959 | **900 ·0,84** · 915 ·0,82 · 930 ·0,75 · 945 ·0,66 | **0,77** | Acercamiento a «Objetivos de conexión» |
| 17 | 960–1019 | **960 ·0,98** · 975 ·0,74 · 990 ·0,60 · 1005 ·0,57 | 0,72 | Frase 5 (la del sitio); la ventana se hace a un lado; la ceja se va |
| 18 | 1020–1079 | 1020 ·0,79 · 1035 ·0,75 · 1050 ·0,70 · 1065 ·0,67 | 0,72 | Quieto; la subida; el dip |
| — | **1080** ·0,93 | **empieza el «Clímax brillante»** (50,05 de la pista) | — | **La firma.** La música se va debajo de las campanas mientras sube |

**Por qué este tramo y no otro.** El 42,05 (1,00) deja de ser la firma y pasa a ser **la revelación de la ruta**: la cosa más importante del
módulo sobre el golpe más fuerte. Para la firma, el siguiente golpe limpio del inicio del clímax es el **50,05 (0,93)**: cae en la grilla
(cuadro 1080 exacto), la música entra en su parte más brillante justo cuando la corona se levanta y se desvanece en 1 s bajo las campanas.
El **52,05** se descartó: es más débil (0,81) y en el mapa de pulsos la grilla se desordena justo después (52,54 ·0,95 · 52,98 · 53,42 ·
53,87: un redoble que caería debajo de las campanas). Resultado: **+8 s** (36 de cuerpo, 18 compases), dentro de los «~40 s» del pedido.
Los pulsos nuevos redondean limpios: 45,065 → 930,45 → 930; 47,035 → 989,55 → 990; 49,055 → 1050,15 → 1050.

Corrección al STORY (v1, se mantiene): la segunda subida empieza en **20,0 (cuadro 600, 0,93)** y el compás más fuerte del cuerpo
hasta el 24 es el 12 (22–24).

---

## 1. Los números del estilo

### 1.1 Paleta (tokens de `identidad/kit.css`; nada fuera de esta lista)

| Papel | Token | Valor | Dónde puede aparecer |
|---|---|---|---|
| Fondo | `--k-noche` | `#060D1F` | A sangre, todo el cuerpo |
| Halo | `.k-halo` | azul `rgba(53,118,218,.45)` arriba a la derecha + dorado `rgba(217,162,52,.22)` abajo a la izquierda | Fondo, bajo todo |
| Puntos | `.k-puntos` | `rgba(169,190,235,.35)`, 2 px cada 42 px, desvanecidos hacia la izquierda (35 %) | Fondo; **nunca se mueven** |
| Tinta | `--k-noche-tinta` | `#EAF0FF` | Las frases |
| Tinta 2 | `--k-noche-tinta-2` | `#A9B6D6` | (`.k-feed-texto`; **no se usa en este clip**) |
| Acento | `--k-noche-dorado` | `#E8B95A` | Solo: la ceja «MEMBRESÍA», la palabra *ninguna*, el botón de la firma |
| Anillo | `--k-noche-linea` | `rgba(234,240,255,.12)` | El borde de la ventana |
| Fondo de la app | `--k-app-fondo` | `#FAF9FD` | Detrás de la grabación (nunca se ve, salvo un cuadro de carga) |
| Azul de marca | `--k-azul` | `#3576DA` | **Solo en la firma** (la baldosa) |
| Placa | `.k-datos-ejemplo` | `rgba(6,13,31,.72)` | La píldora «Datos de ejemplo» |
| Dip | — | `rgba(6,13,31,.40)` | Los 3 cuadros antes de la firma, solo sobre la ventana |

Los colores de la app (el verde del semáforo, el azul `#015BBE` de los botones, el borde azul del chip «Casa de paz · ¿cuál?») viven dentro
de la grabación y no se tocan.

### 1.2 Tipografía

| Pieza | Clase (kit v1.1) | Familia · peso | 4:5 | 9:16 | Interlineado · tracking | Reglas |
|---|---|---|---|---|---|---|
| Frase | `.k-feed-frase` (`.k-titular` en 9:16 con `.k-vertical`) | Fraunces 560; `<em>` itálica 500 dorada | **80 px** | **104 px** | 1,04 · −0,02 em | Máx. **2 líneas**, saltos fijados a mano (§2.0). Izquierda, `text-wrap: balance` apagado (los saltos son nuestros). Sin sombra |
| Ceja | `.k-feed-ceja` (`.k-ceja`) | Inter 700, MAYÚSCULAS | **30 px** | **34 px** | 1 · +0,10 em | Una palabra: «MEMBRESÍA» |
| Datos de ejemplo | `.k-datos-ejemplo` | Inter 600 | 31 px (REVIEW §4.12), píldora de 56 px de alto | igual | 1 · 0 | Blanca sobre la placa; dentro de la ventana, abajo a la izquierda, a 24 px |
| Texto de la app | (grabación) | Inter de la app, 14 px CSS el cuerpo, 22 px los títulos | ≥ **31,6 px** en el cuadro | ≥ **34,5 px** | — | Nunca por debajo de 28 px en ningún encuadre (§1.5) |

Saltos de línea fijados (iguales en los dos formatos):
«Valeria llegó / el domingo.» · «Registrada. / Aun sin señal.» · «Y ya tiene quién / la llame» · **«Y una ruta / para crecer»** (nueva) ·
«Que *ninguna* persona / se pierda».
Anchos estimados: 80 px ≈ 23 caracteres por línea en 888 px; 104 px ≈ 19 en 960 px. En 9:16 la frase 5 se parte «Que *ninguna* / persona se
pierda»; la frase 4 cabe igual en los dos formatos.

### 1.3 Radios y sombras

| Pieza | Radio | Sombra / borde |
|---|---|---|
| `.k-ventana` | **28 px** | `0 0 0 1px var(--k-noche-linea)` + `0 40px 80px -24px rgba(0,0,0,.65)`; `overflow: hidden`; fondo `--k-app-fondo` |
| «Datos de ejemplo» | 999 px | ninguna |
| Frases y ceja | — | **ninguna** (nada de text-shadow ni brillo) |
| Firma | la del kit (`cierre-corto` / `cierre-clip`) | la del kit |

### 1.4 Disposición por formato

| | 4:5 (1080×1350) | 9:16 (1080×1920) |
|---|---|---|
| Márgenes | 96 a los lados, 72 arriba | 60 a los lados; banda útil **168–1330** (lo de la plataforma); debajo de 1330 solo halo y puntos |
| Ceja | x 96 · y 72 (30 px → termina en 108) | x 60 · y 188 (34 px → 229) |
| Frase | x 96 · y 124 · ancho 888 · 2 líneas de 83 px → termina en 290 | x 60 · y 236 · ancho 960 · 2 líneas de 108 px → 452 |
| Ventana | x 100 · y 360 · **880 × 1050**: **sangra 60 px por abajo** (se ve 880×990; las esquinas de abajo nunca aparecen) | x 60 · y 480 · **960 × 850** (480→1330), completa |
| Ventana al final (**desde el cuadro 964**; v1: 724) | escala **0,92** desde el centro inferior (la parte de arriba baja de 360 a 444) + x **+48** | escala 0,92 desde el centro superior (termina en 1262 < 1330) + x **+36** |
| Datos de ejemplo | dentro de la ventana, abajo a la izquierda, a 24 px de los bordes | ídem |
| Firma | `cierre-clip` (kit v1.1, 1080×1350, 2,5 s) | `cierre-corto` (kit v1) |

La ventana ocupa el 81 % (4:5) y el 89 % (9:16) del ancho: la app es la protagonista; nunca un objeto chico en medio del vacío.

### 1.5 La cámara dentro de la ventana: escalas

La grabación llega a 3× (390×844 px CSS → **1170×2532 px**). Se mide en **ppc = píxeles del cuadro por píxel CSS del celular**. Tres niveles:

| Nivel | Qué se ve | 4:5: ppc (escala del video 3×) · ancho × alto visibles en px CSS | 9:16: ppc (escala) · visibles | Texto de la app 14 px → |
|---|---|---|---|---|
| **G** general | todo el ancho del celular | **2,256** (0,752) · 390 × 439 | **2,462** (0,821) · 390 × 345 | 31,6 px · 34,5 px |
| **G⁺** | el ancho de una tarjeta con sus márgenes | 2,436 (0,812) · 361 × 406 | 2,659 (0,886) · 361 × 320 | 34 px · 37 px |
| **M** medio | una zona de la tarjeta o del diálogo | **3,158** (1,053) · 279 × 313 | **3,446** (1,149) · 279 × 247 | 44 px · 48 px |
| **C** cerrado | una línea | **4,061** (1,354) · 217 × 244 | **4,431** (1,477) · 217 × 192 | 57 px · 62 px |

G = ×1,00 · G⁺ = ×1,08 · M = ×1,40 · C = ×1,80 sobre el general. En C la fuente de 3× se amplía 1,35–1,48×: aceptable en punch-ins de 1–2 s
(riesgo anotado en §5). Con la ventana a 0,92 (desde el cuadro 964) la cámara va en G⁺: el cuerpo de la app queda en 31,3 / 34 px (≥ 28).
El objetivo de cada movimiento es una **caja de `pasos.json`** (px CSS del viewport 390×844) centrada en la ventana, con la cámara
sujeta a los bordes del celular (nunca se ve fuera de la grabación). La cámara es un `scale` + `x`/`y` sobre un envoltorio dentro de la
ventana; el `<video>` nunca se transforma ni se busca.

**Los tres mundos y su desplazamiento (nuevo en v2).** Cada mundo es un envoltorio con la grabación ajustada al ancho de la ventana
(`--f-grab-alto` de alto) y su propio `top`, para que la cámara no tenga que saltar cuando cambia lo que hay debajo del lente:

| Mundo | Pantalla | Envoltorio | `top` | Con la cámara en (escala 1, x 0, y 0) se ve |
|---|---|---|---|---|
| 1 | «Nueva persona» (cuenta 103) | `#m1` | 0 | el tope de arriba del celular (CSS 0–439) |
| 2 | Mi seguimiento (103) | `#m2in` | `hVis − grabAlto` (= −914 px en 4:5) | el tope de abajo (CSS 405–844): la tarjeta de Valeria y la barra inferior |
| **3** | **La ficha de Valeria (103)** | **`#m3in`** | **0** | **el tope de arriba de la ficha (CSS 0–439): cabecera y la fila «Avance»** |

Así, en el 780 la cámara está quieta en el G del mundo 2 (0, 0) y el iris descubre el mundo 3 ya encuadrado en su cabecera **sin mover la
cámara** (como en los irises del 120 y del 375). El centro del iris 3 se da en coordenadas de `#m3in`: `(tx·K, ty·K + OFF2)`, donde `(tx, ty)`
es el toque en el nombre en px del video (`pasos-2.json → toques[]`), `K = 880/1170` y `OFF2 = −914` (el nombre se toca en la pantalla del
mundo 2, que está 914 px más arriba que el mundo 3 en la tira). `#m3in` va **encima** de `#m2in` (orden del DOM o `z-index`), y el iris lo
recorta 780–785; a partir del 786 `clip-path: none`.

### 1.6 Curvas y duraciones (cada tween lleva su curva por nombre)

| Papel | Curva | Cuadros | Detalle |
|---|---|---|---|
| `entrada-palabra` | `power4.out` | 4 | `filter: blur(6px) → 0` + opacidad 0 → 1; **sin desplazamiento**. Palabras a 2 cuadros (0,067 s), salvo la frase 1 (una por pulso). Arranca un cuadro antes del pulso para que el primer cuadro visible sea el pulso (REVIEW §4.7) |
| `entrada-linea` | `power4.out` | 6 | la línea entera, blur 8 → 0 + opacidad (frase 2 y ceja) |
| `salida-texto` | `power3.in` | 4–5 | blur 0 → 8 + opacidad 1 → 0, la línea entera. Empieza 2–3 cuadros antes del pulso para que la entrada caiga en el pulso («blur swap»: el fondo no corta) |
| `camara` | `power2.inOut` | **14** | un movimiento por compás; después, quieta |
| `punch` | `power2.inOut` | **9** | solo el del cuadro 660 |
| `latigo` | `power3.inOut` | 10 | una sola tira, 176–186 (REVIEW §4.10); el mundo 2 aterriza 1,04 → 1,00 (`power3.out`, 180–190) |
| `iris` | `power2.out` | 5 | `clip-path: circle(0 at X Y) → circle(1900px at X Y)`, X Y = el centro del botón (o del nombre) tocado, en coordenadas del envoltorio que se recorta. **Tres irises: 120 («Registrar»), 375 («Marcar cumplido»), 780 (el nombre de Valeria → su ficha)** |
| `ventana-cambio` | `power2.inOut` | 15 | escala 1 → 0,92 + x (§1.4), **964–978**: 4 cuadros después de la frase 5 (movimiento secundario) |
| `halo` | `sine.out` | 90 | escala 1,08 → 1,00 al entrar cada mundo o cada cierre: **cuadros 0, 180, 780 y 960**; los puntos no se mueven |
| `dip` | escalón | 3 | capa `rgba(6,13,31,.40)` sobre la ventana, **cuadros 1077–1079**, sin curva |
| firma | las del kit | 75 | `back.out(2.2)` de la corona y compañía; **no se imita en el cuerpo** |
| resortes | ninguno | — | nada rebota salvo la corona del kit |
| velocidad de la grabación | `data-playback-rate` por tramo (o carril `rate`) | — | entre **0,35× y 3,5×**; las rampas van entre acciones, nunca durante una letra o un toque. Un tramo quieto puede ir a 0,5× para cubrir más clip (P3, P8) |

Desenfoque de movimiento: `data-motion-blur="on"` con `data-motion-blur-shutter="180"` en la raíz de las dos composiciones (látigo, cámara y
desplazamientos de la app). **Nunca `filter: blur()` sobre la grabación**; el blur de CSS es solo para el texto.

### 1.7 Sonido

| Capa | Fuente | Nivel | Regla |
|---|---|---|---|
| Música | `assets/musica/product-launch-the-mountain.mp3`, `data-media-start` 14,05, **dura 37,0 s (cuadros 0–1109)** | cama a **−18 LUFS** (kit.json: `volumen` 0,7, en el carril de volumen con valores absolutos, REVIEW §4.9) | Desvanece bajo la firma: carril **0,7 hasta el 1080 (36,0) → 0,224 (−10 dB) en el 1092 (36,4) → 0 en el 1110 (37,0)** (30 cuadros; la primera campana del 1091 ya se oye limpia) |
| Sonidos de acción (kit v1.1) | `toque` 75 ms · `aparicion` 220 ms · `desliz` 360 ms (acento 0,2) · `subida` 1,9 s (acento 1,5) · `confirmacion` 320 ms (acento 0,1) | el nivel del kit (`data-volume="1"`, 4–10 dB bajo la música); **1,4 (+3 dB) en los tres toques clave (121, 601 y 841), en las dos `confirmacion` (123, 603), en la `aparicion` del 843 y en el `desliz` del látigo** | El pico suena **un cuadro después** de su imagen (`data-start` = cuadro del sonido / 30 − acento). `toque` rota tres tomas (a = `toque.wav`, b = +3 %, c = −3 % de tono). **Sin tics de tecla** |
| Sonido de marca | `sonido-marca.mjs` (campanas, −20 LUFS, acentos 0 · 0,20 · 0,52) | tal cual | Lo pone el host en **36,38 s** (cuadro 1091: firma + 0,38) |
| Mezcla | — | **−16 LUFS** integrados, pico real ≤ **−1 dBTP** | `npx hyperframes normalize-audio` y se comprueba con `npx hyperframes audio <render> --json` (medido, no oído). El borrador v1 dio −17,7 LUFS / −1,4 dBTP: al normalizar hay que limitar o bajar los 1,4 a 1,2 (REVIEW §6.2) |

**Los sonidos, en orden:** toque 61 · toque 91 · aparicion 109 · desliz 109–120 · toque 121 (+) · confirmacion 123 (+) · toque 151 · aparicion
166 · desliz 174–185 (+, el látigo) · aparicion 196 · toque 376 · toque 451 · toque 496 · toque 601 (+) · confirmacion 603 (+) · toque 721 ·
**toque 781** (a, el nombre) · **toque 841 (+, b, «Avance»)** · **aparicion 843 (+, la tarjeta que se abre)** · subida 1036–1093 (golpe 1080) ·
campanas 1091. **Diecinueve sonidos de acción más la subida y las campanas: veintiún eventos en 38,5 s** (v1: dieciocho en 30,5), ninguno
sin causa visible. Ningún whoosh en los
movimientos de cámara; ningún sonido en el iris del 780 además del toque (como en el 375).

### 1.8 BANNED: los valores por defecto prohibidos, con nombre

1. **El fundido de 0,5 s con `power2.out` (o la curva sin nombrar de GSAP) para todo.** Cada tween lleva su curva de §1.6; nada entra solo por opacidad.
2. **Fade + deslizarse hacia arriba** como entrada de texto. Las palabras entran por blur, sin moverse.
3. **Zoom lineal** o `linear` en la cámara (`linear` solo valdría para rotación o progreso, y aquí no hay).
4. **El acercamiento lento y arrastrado** (1,0 → 1,08 en 8 s): el «creeping scale» que delata un video generado. Movimientos discretos de 14 cuadros en pulsos.
5. **Fundido cruzado entre mundos.** Solo las tres transiciones con causa: iris desde el toque, látigo vertical, dip + corte.
6. **Teléfono dibujado** alrededor de la grabación (también `.k-telefono`), bisel, barra de estado inventada, marco negro.
7. **Texto que se mueve mientras se lee; titulares que siguen derivando** después de aterrizar; «breathing» o pulsos en títulos o en la ventana.
8. **El logo en una esquina**, marca de agua, la corona antes del cuadro 1080.
9. **Brillo, neón, destellos, lens flare, partículas, orbes.** El halo del kit es un degradado fijo que se asienta una vez por mundo; nunca late.
10. **Degradados nuevos** (morados, azules, mesh), **tarjetas de vidrio**, fondos distintos de la noche.
11. **Tres tarjetas en fila, rejillas de KPI, título sobre captura oscurecida, etiquetas «01 / 02», corner brackets, HUD.**
12. **Whoosh en cada corte** o en los movimientos de cámara; el mismo `toque` sin rotar; dings, chimes o tonos ajenos al kit.
13. **Reproducción de la app por encima de 3,5× o por debajo de 0,35×** (parece un glitch o un error).
14. **Retocar un píxel de la app:** ni resaltados, ni flechas, ni cursor dibujado en posproducción, **ni animar la apertura de la tarjeta
    «Avance» ni hacer aparecer los chips de los objetivos uno a uno**: la app los muestra de golpe y así se dejan; la cámara es el único gesto.
    El punto de toque viene de las coordenadas reales de la grabación.
15. **Texto de la app por debajo de 28 px.** Ningún encuadre de §1.5 baja de 31 px.
16. **Centrarlo todo.** Las frases van a la izquierda, al margen; solo la ventana (el sujeto) va centrada.
17. **Cifras sin «Datos de ejemplo».** La píldora está desde el cuadro 0.
18. **Más de 3 s sin un cambio visible** en el cuerpo (`sweep_static`): el tramo más quieto (**975–1076**) lleva el asentamiento del halo
    (960–1050) y la subida (1036–1093).
19. **Un pulso vacío entre los cuadros 0 y 360.** O aterriza una palabra, o cierra un campo, o aparece algo real de la app.
20. **Un desplazamiento de página en la ficha** (780–1079): la ficha se graba quieta, abierta arriba; lo que recorre la tarjeta es la cámara.
    (Si la tarjeta no cabe, la válvula de §5, y el desplazamiento se esconde dentro de un movimiento de cámara, como el salto a «Registrar».)
21. Del contrato de HyperFrames: `from()` en escenas (siempre `fromTo`), `autoAlpha`/`display` sobre un `.clip`, `transform` de CSS en un
    elemento que GSAP transforma, el `<video>` con tiempo y su envoltorio con tiempo a la vez.

Después del primer render, cada valor por defecto que aun así aparezca se nombra aquí y se corrige.

---

## 2. Los planos, cuadro por cuadro

### 2.0 Convenciones

- **G / G⁺ / M / C**: los niveles de §1.5. «Sobre X» = la caja de X (`pasos.json` o `pasos-2.json`) centrada en la ventana.
- **Pulso**: el cuadro de la grilla de §0. Un evento «en el 120» aterriza en el cuadro 120 (su sonido suena en el 121).
- **Grabaciones** (§3): **G1** = `grabacion.mp4` + `pasos.json` del 2026-10-30 (T1 alta y T3 seguimiento, cuenta 103; T2 asignar, cuenta 101,
  no sale en cámara), que sirve a los cuadros **0–785**; **G2** = `grabacion-2.mp4` + `pasos-2.json` (la misma escena con el tramo **T5** al
  final), que sirve **desde el 780** (la ficha). «grab.» = cuadro de G1; «grab2.» = cuadro de G2.
- **Textos de la app**: son los reales, verificados en `frontend-v2/public/i18n/es.json`, en la plantilla de Membresía
  (`backend/_datos/personas_catalogos.php`) y en `ficha-avance.component.ts`. Lo que no se puede saber hasta grabar lleva «(real)».
- Las frases siempre en el mismo lugar (§1.4); una frase a la vez; la ceja encima de la frase.
- **Correcciones ya absorbidas de la construcción** (REVIEW): el flujo «Llegó a un culto» va `Llamada de bienvenida → Mensaje de bienvenida
  (automático) → Se conecta con una casa de paz → …`; el formulario de la llamada trae «Petición de oración» y **«Observaciones»** (no
  «Comentario (opcional)»); el botón del diálogo que cumple el paso dice **«Marcar cumplido»** (`#btn-enviar-reporte`); el toque en «Listo»
  (720) queda fuera del encuadre C y **se oye, no se dibuja**.

### 2.1 Tabla maestra (todo lo que cambia, por cuadro)

| Cuadro | Pulso | La app (grabación) | Cámara | Texto | Sonido | Transición |
|---|---|---|---|---|---|---|
| **0** | ● | G1 · «Nueva persona»: el teléfono `5557654321` ya puesto (fuera de cámara), el campo «Nombres» con la **«V»** recién escrita, «Datos de ejemplo» en su esquina | G sobre la parte alta del formulario (título «Nueva persona», Nombres, Apellidos, Teléfono) | **«Valeria»** ya aterrizada (es la miniatura) | — | — |
| 5 · 10 · 15 · 20 · 25 · 30 | 15 ● | «a·l·e·r·i·a», una letra cada 5 cuadros (0,47×); «Valeria» completo en el 30 | quieta | **«llegó»** en el 15 (entrada-palabra) | — | |
| 30 · 45 | 30 ● 45 ● | el punto de toque viaja a «Apellidos» | 46–59: G → G sobre Apellidos y el selector (CSS 200–639; REVIEW §4.1) | **«el»** en el 30, **«domingo.»** en el 45. Frase 1 completa y muerta de quieta hasta el 117 | — | |
| **60** | ● | toque en «Apellidos»; «Cardona Ríos» a 1,36× | quieta | — | `toque` a en el 61 | |
| **90** | ● | toque en «Cómo llegó» → se abre el selector: grupo **«Eventos»** y **«Otras formas de llegar»** | quieta | — | `toque` b en el 91 | |
| **105** | ● | toque en **«Servicio General»** → la app elige el único evento y muestra el chip (ícono `church` · Servicio General) en el 108 | quieta | — | `aparicion` en el 109 | |
| 108–119 | | la pantalla salta hasta «Registrar» (grab. 460→461, en el 114) | **Movimiento del compás 2**: G → G sobre el diálogo y «Registrar» (CSS 311–750), 108–119 | la frase 1 sale 117–121 | `desliz` 109–120 | |
| **120** | **●●● bajo** | **toque en «Registrar»** | quieta (ya centrada) | **«Registrada. / Aun sin señal.»** entrada-linea 120–126 | **`toque` c (+) en el 121**; `confirmacion` (+) en el 123 | **Iris desde el toque** 120–125: debajo, un still del cuadro 119; encima, la grabación recortada por el círculo que crece desde el centro de «Registrar» |
| 122–149 | 135 ● | el diálogo real: **«Guardada en este dispositivo»** · «Valeria Cardona Ríos queda guardada aquí y se envía sola cuando haya señal.» · botón **«Entendido»** | quieta sobre el diálogo (G) | frase 2 quieta | — | |
| **150** | ● | toque en «Entendido» → el diálogo se cierra; el formulario queda limpio | **Movimiento del compás 3**: G centrado → G sobre la cabecera (arriba), 150–163 | | `toque` a en el 151 | |
| **165** | ● | en la cabecera aparece el botón real **«1 sin enviar»** (`#btn-pendientes`, ícono `schedule_send`) | quieta | | `aparicion` en el 166 | |
| 172–178 | | vuelve la señal, el alta se envía sola y **«1 sin enviar» desaparece** (178) | quieta | la frase 2 sale 177–181 | — | |
| **176–186** | **180 ●●● pico** | la tira sube 1100 px: el mundo 1 se va y el mundo 2 llega (una sola curva, el cuadro más rápido en el 181); el mundo 2 aterriza 1,04 → 1,00 (180–190). La ventana no se mueve: cambia lo que hay dentro | G1 T3 llega en **G** (el tope de abajo): encabezado «Mi seguimiento», pestaña **«Acompañados»**, el buscador con «Valeria», y la **tarjeta de Valeria Cardona Ríos**: paso **«Llamada de bienvenida»** (ícono `call`) · chip **«A tiempo»** (verde) · **«Desde hoy · vence en 3 días»** · **«Después: Mensaje de bienvenida»** · botones llamar, **«Marcar cumplido»**, «Dejar de acompañar» | — | **`desliz` (+) 174–185** (el látigo) | **Látigo vertical**; halo a 1,08 → 1 (180–270) |
| **195** | ● | quieta (la tarjeta) | quieta | **«MEMBRESÍA»** entrada-linea 195–201 | `aparicion` en el 196 | |
| **240** | ●● | quieta | **Movimiento del compás 5**: G → **M** sobre la mitad alta de la tarjeta (nombre, «Llamada de bienvenida», «A tiempo», «Desde hoy · vence en 3 días»), 240–253 | — | — | |
| **300** | ● | quieta | **Movimiento del compás 6**: M → **C** sobre la línea **«Después: Mensaje de bienvenida»**, 300–313 | — | — | |
| **345** | ● | quieta | vuelta C → **G** sobre la tarjeta (el botón «Marcar cumplido» a la vista), 345–359 | — | — | |
| **360** | ● | quieta | quieta | **«Y ya tiene quién / la llame»**: Y 360 · ya 362 · tiene 364 · quién 366 · la 368 · llame 370 (completa en el 374) | — | |
| **375** | ● | **toque en «Marcar cumplido»** | quieta | frase 3 quieta | `toque` b en el 376 | **Iris desde el toque** 375–380 (still del 374 debajo) |
| 377–389 | | el diálogo real **«Reporte del paso»** · «**Valeria Cardona Ríos** · Llamada de bienvenida» · pregunta **«¿Cómo fue?»** con **Contestó / No contestó / Lo visité** · «Petición de oración» · **«Observaciones»** · botones **«Solo registrar el intento»** y **«Marcar cumplido»** | quieta | | — | |
| **390** | ● | quieta | **Movimiento del compás 7**: G → **M** sobre «¿Cómo fue?» y sus tres opciones, 390–403 | | — | |
| **450** | ● | el punto de toque **marca «Contestó»** (el radio se llena en el 456) | quieta | | `toque` c en el 451 | |
| **480** | ● | quieta | **Movimiento del compás 9**: M sobre la pregunta → **M** sobre «Observaciones», 480–493 | | — | |
| **495** | ● | toque en el campo | quieta | | `toque` a en el 496 | |
| 501–566 | 510 · 525 · 540 · 555 | se escribe **«Muy contenta, viene el domingo»** con las teclas reales (1,14×) | **quieta** (ningún movimiento mientras se escribe) | frase 3 quieta | — (sin tics) | |
| **570** | ● | el punto de toque baja hacia los botones | **Movimiento del compás 10**: M del campo → **M (×1,3)** sobre los botones del diálogo, 570–583 | | — | |
| 585 | ● | el punto llega al botón «Marcar cumplido» del diálogo | quieta | | — | |
| **600** | **●●● 2.ª subida** | **toque en «Marcar cumplido» del diálogo** (`#btn-enviar-reporte`) → el resultado (603): ícono `task_alt` · **««Llamada de bienvenida» cumplido»** · **«Ahora va en: Mensaje de bienvenida»** · botones «Elegir otro paso» y **«Listo»** | **Movimiento del compás 11**: M de los botones → **M (×1,35)** sobre el bloque del resultado, 600–613 | la frase 3 sale 597–601 | **`toque` b (+) en el 601**; **`confirmacion` (+) en el 603** | |
| **660** | **●●● golpe** | quieta | **Punch** M → **×1,5** sobre la línea **«Ahora va en: Mensaje de bienvenida»** (247 px CSS: a 1,5 cabe; «Listo» queda fuera), 660–668, 9 cuadros | — | — | |
| 690 | ● | el punto de toque va a «Listo» (fuera del encuadre) | quieta | | — | |
| **720** | **●●● golpe (0,96)** | **toque en «Listo»** (grab. 2932; se oye, no se dibuja) → el diálogo se cierra (729) → **la tarjeta ya dice «Mensaje de bienvenida» (ícono `chat`) · «A tiempo» · «Desde hoy · vence mañana» · «Después: Se conecta con una casa de paz»** (desde el 738) | **Movimiento del compás 13**: ×1,5 → **G** sobre la tarjeta (el tope de abajo del mundo 2: `E2.tarjeta`; v1 iba a G⁺ porque la ventana se encogía aquí; ya no), 720–733 | **ninguna frase** (v1 ponía aquí la frase final); la ceja sigue | `toque` c en el 721 | — |
| 735–779 | 735 · 750 · 765 | quieta: la tarjeta al día se lee 1,5 s (G1 v25 sigue hasta el 785) | quieta | — | — | |
| **780** | **●●● golpe (0,88)** | **toque en el nombre «Valeria Cardona Ríos»** de la tarjeta (`a.nombre`, el enlace a su ficha; G2, tramo `ficha`) | **quieta** en (0, 0): el mundo 3 llega debajo del lente con `top: 0` (§1.5) | — | `toque` a en el 781 | **Iris desde el toque** 780–785: debajo, la tarjeta (G1 v25, quieta, hasta el 785); encima, `#m3in` recortado por el círculo que crece desde el centro del nombre |
| 783–809 | 795 ● | **la ficha de Valeria** (G2, la carga se corta como las esperas de los diálogos: el primer cuadro útil en el 783): foto con sus iniciales, **«Valeria Cardona Ríos»**, el chip del semáforo de actividad («Verde · hoy», real), **«Llegó el 30 de oct. · Culto o evento · Servicio General»** (la fecha es la del día de la grabación), «Registrada por Jorge Gallego Gil el …» (real), **«Llamar» · «WhatsApp» · «Editar»** · ⋮; debajo, la primera tarjeta, plegada: **«Avance»** con su resumen **«Mensaje de bienvenida · ● A tiempo»**; luego Datos, Etiquetas, Cuidado…, plegadas | G sobre la cabecera (CSS 0–439) | — | — | |
| **810** | ● | quieta | **Movimiento del compás 14**: G → **M** sobre la fila **«Avance · Mensaje de bienvenida · ● A tiempo»** (caja de `button[data-seccion="avance"]`, `pasos-2.json`), 810–823 | — | — | |
| **840** | **●●● el más fuerte (1,00)** | **toque en «Avance»** → la tarjeta **se abre de golpe** (la app no la anima; el dedo se suelta ≈ 6 cuadros después de apoyarse y la apertura real se corta para que aparezca en el **842**): **«Flujo: Llegó a un culto»** · el paso **«Mensaje de bienvenida»** (ícono `chat`) con **«● A tiempo · Desde hoy · vence mañana»** · **«Después: Se conecta con una casa de paz»** · botón **«Marcar cumplido»** · título **«Objetivos de conexión»** con sus chips: **«Casa de paz · ¿cuál?»** (botón con borde azul, ícono `travel_explore`: la demo liga el objetivo a Eventos) · **«Servir»** (`volunteer_activism`) · **«Clases de la visión»** (`school`) · título **«Historial de pasos»**: «Empezó «Mensaje de bienvenida»» · «Cumplió «Llamada de bienvenida»» · «Empezó «Llamada de bienvenida»», cada uno con «hoy, HH:MM · Jorge Gallego Gil» (reales) | **Movimiento del compás 15**: M de la fila → **M** sobre el bloque del paso (caja de `#avance-paso` con «Flujo:» arriba y «Después:» abajo), 840–853 | **«Y una ruta / para crecer»**: Y 840 · una 842 · ruta 844 · para 846 · crecer 848 (completa en el 852) | **`toque` b (+) en el 841**; **`aparicion` (+) en el 843** (la tarjeta que se abre) | la espera real entre el dedo y la apertura se corta (G2: del cuadro del toque al primer cuadro con `#avance-objetivos` visible) |
| 855–899 | 855 · 870 · 885 | quieta | quieta | frase 4 quieta (3,5 s hasta el 957) | — | |
| **900** | ●● (0,84) | quieta | **Movimiento del compás 16**: M del paso → **G⁺** centrado en **«Objetivos de conexión»** y sus chips (caja de `#avance-objetivos` más el `h4` de arriba: cy = caja.y − 14). G⁺ porque los chips ocupan el ancho de la tarjeta (358 px CSS) y en M (279) se cortarían; **si `caja.w ≤ 279` (los chips caben en tres filas) va a M**, 900–913 | frase 4 quieta | — | |
| 915–959 | 915 · 930 · 945 | quieta | quieta | la frase 4 sale 957–961 | — | |
| **960** | **●●● golpe (0,98)** | quieta | **Movimiento del compás 17**: G⁺ de los objetivos → **G⁺** sobre la tarjeta «Avance» entera (de la fila «Avance» al final de los chips; el historial entra si cabe; caja de `#ficha-avance`), 960–973 | **«Que *ninguna* persona / se pierda»**: Que 960 · *ninguna* 962 · persona 964 · se 966 · pierda 968 (completa en el 972). **La ceja sale 960–963** | — | **La ventana se hace a un lado**: escala 1 → 0,92 + x (§1.4), 964–978; halo a 1,08 → 1 (960–1050) |
| 975–1076 | 975 · 990 … 1065 | quieta (la ficha real) | quieta | frase 5 quieta ≥ 3,5 s | **`subida`** de −14 dB en el 1036 a +4 dB en su golpe del 1080 | |
| **1077–1079** | | — | — | — | — | **Dip**: la ventana al 40 % de oscuridad, 3 cuadros |
| **1080** | **●●● empieza el clímax (0,93)** | — | — | — | la música cae de 0,7 a 0,224 (1080–1092) y a 0 (1110) | **Corte a la firma**: 9:16 `cierre-corto`, 4:5 `cierre-clip`; variables `llamado: prueba`, `fondo: azul`, `idioma: es` |
| 1086 · 1093 ↓ | | la K sube (0,20 s de la firma); las 7 barras de la corona desde el 0,45 (cada 0,05 s, `back.out(2.2)`) | | «Kingdom» 0,75 s; botón **«Prueba gratis 30 días»** 0,95 s | **Campanas en el 1091** (36,38 s); acentos 1091 · 1097 · 1107 | |
| **1154** | | último cuadro: la corona completa y el botón | | | silencio de música desde el 1110 | fin |

### 2.2 Los nueve planos

#### P1 · «La puerta» — cuadros 0–119 (compases 1–2) · pulsos 0, 15, 30, 45, 60, 75, 90, 105 · **construido, no se toca**

- **Grabación:** G1 T1 desde el cuadro de la tecla «V» en «Nombres» hasta el salto a «Registrar» (tramos v01–v08 de `index.html`).
- **Encuadre 4:5:** G, 439 px CSS de alto: el título «Nueva persona», Nombres, Apellidos, Teléfono; 46–59 baja a Apellidos y el selector. **9:16:** G, 345 px CSS.
- **Cámara:** 46–59 y 108–119. Nada más.
- **Texto:** frase 1 por pulsos (la primera palabra ya puesta en el cuadro 0); sale 117–121.
- **Sonido:** toque 61, toque 91, aparicion 109, desliz 109–120.
- **Transición:** ninguna dentro; cierra con el toque del 120.

#### P2 · «Guardada aun sin señal» — cuadros 120–179 (compás 3) · pulsos 120 (bajo), 135, 150, 165 · **construido, no se toca**

- **Grabación:** G1 T1 desde el toque en «Registrar» hasta que desaparece «1 sin enviar» (v09–v13; still del 119 bajo el iris).
- **Encuadre:** G centrado en el diálogo (120–149); G sobre la cabecera (desde el 163).
- **Texto:** frase 2 entra 120–126, sale 177–181.
- **Sonido:** toque 121 (+), confirmacion 123 (+), toque 151, aparicion 166.
- **Transición:** iris desde «Registrar» (120–125) al entrar; látigo (176–186) al salir.

#### P3 · «Mi seguimiento: la tarjeta» — cuadros 180–359 (compases 4–6) · pulsos 180 (pico), 195, 240, 300, 345 · **construido, no se toca**

- **Grabación:** G1 T3, la tarjeta de Valeria quieta (v14, grab. 2207–2402 a 1×).
- **Cámara:** llega con el látigo (1,04 → 1,00); 240–253 a M; 300–313 a C («Después: …»); 345–359 vuelve a G.
- **Texto:** la ceja «MEMBRESÍA» 195–201; sin frase.
- **Sonido:** desliz 174–185 (látigo), aparicion 196 (ceja).

#### P4 · «El reporte» — cuadros 360–599 (compases 7–10) · pulsos 360, 375, 390, 450, 480, 495, 570, 585 · **construido, no se toca**

- **Grabación:** G1 T3 desde el toque en «Marcar cumplido» hasta el cuadro anterior al toque en el botón del diálogo (v15–v22; still del 374 bajo el iris).
- **Cámara:** tres movimientos de 14 cuadros, uno por compás (7, 9 y 10); el compás 8 es solo la app marcando «Contestó».
- **Texto:** frase 3 entra 360–374; sale 597–601.
- **Sonido:** toque 376, toque 451, toque 496.
- **Transición:** iris desde «Marcar cumplido» (375–380).

#### P5 · «Cumplido y el siguiente paso» — cuadros 600–719 (compases 11–12) · pulsos 600 (subida), 660 (golpe), 690 · **construido, no se toca**

- **Grabación:** G1 T3 desde el toque en «Marcar cumplido» del diálogo hasta el cuadro anterior al toque en «Listo» (v23–v24).
- **Cámara:** 600–613 a ×1,35 sobre el resultado; 660–668 punch a ×1,5 sobre «Ahora va en: Mensaje de bienvenida».
- **Texto:** ninguno (la prueba la da la app).
- **Sonido:** toque 601 (+), confirmacion 603 (+).

#### P6 · «La tarjeta al día y la ficha» — cuadros 720–839 (compases 13–14) · pulsos 720 (golpe), 735, 750, 765, 780 (golpe), 795, 810, 825 · **nuevo desde el 733**

- **Grabación:** 720–785: G1 T3 desde el toque en «Listo» (v25, grab. 2932→, a 1×): el diálogo se cierra (729), la tarjeta al día desde el 738;
  **v25 se recorta al 785** (v1 llegaba al 840). **Desde el 780: G2, tramo `ficha`**: el cuadro del toque en el nombre (`pasos-2.json →
  pasos[tramo=ficha].toques[0].cuadro`) cae en el 780; la carga de la ficha (el cambio de ruta, su cargador) **se corta**: el primer cuadro con
  la cabecera completa y la fila «Avance» con su resumen cae en el **783**. De ahí a 809 la ficha quieta a 1×.
- **Encuadre 4:5:** 720–733 la cámara vuelve a **G** sobre la tarjeta (`E2.tarjeta`, el tope de abajo: CSS 405–844, texto 31,6 px). En el 780
  **no se mueve**: el mundo 3 (`#m3in`, `top: 0`) muestra bajo el mismo lente la cabecera de la ficha (CSS 0–439: foto, nombre, chips,
  «Llegó el…», los botones y la fila «Avance» plegada). 810–823 a **M** sobre la fila «Avance» (caja de `button[data-seccion="avance"]`): la
  fila al centro, con los botones de la cabecera asomando arriba y Datos / Etiquetas plegadas abajo. **9:16:** G muestra 345 px CSS: la
  cabecera entera puede dejar la fila «Avance» en el borde; la cámara de la ficha va centrada 40–60 px CSS más abajo (`cy ≈ 220`, la barra
  superior de la app queda cortada) para que la fila entre; en M, lo mismo que en 4:5.
- **Cámara:** 720–733 (compás 13) y 810–823 (compás 14). Quieta en el iris.
- **Texto:** ninguno (la ceja sigue). La ventana **no** se encoge aquí (v1 lo hacía en el 724).
- **Sonido:** toque 721 (c), toque 781 (a).
- **Transición:** iris desde el nombre (780–785), el tercero del clip: la tarjeta (G1) debajo, la ficha (G2) encima. Es la costura entre las dos
  grabaciones y el iris la esconde: al 785 ya no queda nada de G1 en pantalla. El centro del círculo: `(tx·K, ty·K + OFF2)` en `#m3in` (§1.5).
- **Marcas de toque:** `tq-780`/`on-780` en las marcas del **mundo 2** (coordenadas de `pasos-2.json`, el toque ocurre sobre la tarjeta);
  la fila «Avance» (840) en las marcas del **mundo 3**.

#### P7 · «Avance: la ruta y los objetivos» — cuadros 840–959 (compases 15–16) · pulsos 840 (el más fuerte), 855, 870, 885, 900 (golpe), 915, 930, 945 · **nuevo**

- **Grabación:** G2, tramo `avance`: el cuadro del toque en la fila «Avance» (`toques[0].cuadro`) cae en el **840**; los ≈ 6 cuadros reales
  entre apoyar y soltar el dedo (la app abre al soltar) **se cortan** para que el primer cuadro con la tarjeta abierta caiga en el **842**.
  Después la ficha abierta, quieta, a 1× (o 0,5× si hace falta cubrir hasta el 1079: nada se mueve en la app).
- **Encuadre 4:5:** en el 840 la cámara está en M sobre la fila (279×313 CSS): al abrirse, la mitad baja del encuadre se llena de golpe con
  «Flujo: Llegó a un culto», el paso y «Después: …» (la fila de Datos se va hacia abajo). 840–853: M baja ≈ 120 px CSS para centrar el bloque
  del paso (caja de `#avance-paso`), con «Flujo:» arriba y «Después: Se conecta con una casa de paz» y «Marcar cumplido» abajo; texto 44 px.
  900–913: a **G⁺** centrado en «Objetivos de conexión» (el `h4`) y sus chips (`#avance-objetivos`): 361 px CSS de ancho, los chips
  completos, texto 34 px; si los chips caben en 279 px (tres filas), **M**. **9:16:** los mismos objetivos; M 279×247, G⁺ 361×320.
- **Cámara:** 840–853 (compás 15) y 900–913 (compás 16). Quieta el resto.
- **Texto:** frase 4 **«Y una ruta / para crecer»** entra 840–852 (cinco palabras a 2 cuadros), quieta 3,5 s, sale 957–961.
- **Sonido:** toque 841 (b, +), aparicion 843 (+).
- **Transición:** ninguna; la frase 5 cae sobre la misma imagen.
- **Qué debe leerse de un vistazo en el 853:** «Mensaje de bienvenida», «A tiempo», «Después: Se conecta con una casa de paz». **En el 913:**
  «Objetivos de conexión», «Casa de paz · ¿cuál?», «Servir», «Clases de la visión». Es la prueba más fuerte del clip: Kingdom sabe hacia dónde va Valeria.

#### P8 · «Que ninguna persona se pierda» — cuadros 960–1079 (compases 17–18) · pulsos 960 (golpe), 975, 990, 1005, 1020, 1035, 1050, 1065 · **nuevo (era P6 en 720–839)**

- **Grabación:** G2, la ficha abierta, quieta (el final del tramo `avance` y el `pausa: 5000`), a 1× o 0,5×.
- **Encuadre:** 960–973 a **G⁺** sobre la tarjeta «Avance» entera (caja de `#ficha-avance`; si mide más de 406 px CSS, centrada entre la fila
  «Avance» y el final de los chips: el historial entra lo que entre), con la ventana a 0,92 y corrida (§1.4): texto 31,3 px. En 4:5 la ventana
  baja (la parte de arriba a 444) y deja aire bajo la frase; en 9:16 se encoge desde arriba y termina en 1262.
- **Cámara:** 960–973 (compás 17); después muerta de quieta. El halo se asienta 960–1050.
- **Texto:** frase 5 entra 960–972 (*ninguna* en itálica dorada: el único dorado del cuerpo junto a la ceja); la ceja sale 960–963; la frase se
  sostiene 3,5 s.
- **Sonido:** subida 1036–1093 (golpe en el 1080).
- **Transición:** dip 1077–1079 y corte duro al 1080.

#### P9 · «La firma» — cuadros 1080–1154 · **construido; corre 240 cuadros**

- 9:16: `identidad/cierre-corto.html`; 4:5: `identidad/cierre-clip.html` (kit v1.1, misma línea de tiempo: baldosa 0–0,45 s, K 0,20, corona
  desde 0,45 cada 0,05 s, «Kingdom» 0,75, botón 0,95). Variables `{"llamado":"prueba","fondo":"azul","idioma":"es"}`.
- Campanas en 36,38 (cuadro 1091). La música: 0,7 → 0,224 (1080–1092) → 0 (1110).
- Es el único gesto de marca del clip. Nada del cuerpo imita la corona.

### 2.3 Lo que cambia en `index.html` respecto de la v1 (para quien construye)

| Pieza | v1 | v2 |
|---|---|---|
| `#root` `data-duration` | 30,5 | **38,5** |
| `#fondo` `data-duration` | 28 | **36** |
| `#ceja` | 6,466667 + 17,666667 (194–724) | 6,466667 + **25,633333** (194–963); sale 960–963 |
| `#frase-4` | «Que ninguna persona se pierda», 23,966667 + 4,033333 | **nueva** `compositions/frase-4.html` **«Y una ruta / para crecer»**: `data-start` **27,966667** (839), `data-duration` **4,066667** (hasta el 961); entra 840–852, sale 957–961 |
| `#frase-5` | — | **la de v1 renombrada** `compositions/frase-5.html` («Que *ninguna* persona / se pierda», `data-beat="ninguna" data-hold`): `data-start` **31,966667** (959), `data-duration` **4,033333** (hasta el 1080) |
| `#cierre-clip` | 28 + 2,5 | **36** + 2,5 |
| `v25` | 23,333333 + 4,666667 (700–840) | 23,333333 + **2,833333** (700–785) |
| `#m3in` + `v26`–`v28` | — | **nuevo** dentro de `#m2` (después de `#m2in`, encima): `top: 0`; `#iris3` con los tramos de G2: `v26` 780–842 (el toque en el nombre, corte de la carga, la ficha quieta; se parte en dos `<video>` si el corte lo pide), `v27` 840–842 (el toque en «Avance»), `v28` 842–1080 (la tarjeta abierta, quieta; rate 1 o 0,5); sus `.marcas` con `tq-840`/`on-840` |
| Marcas del mundo 2 | tq 375 · 450 · 495 · 600 | + **`tq-780`/`on-780`** (el nombre; coordenadas de `pasos-2.json`) |
| Cámara | hasta `E2.final` en el 720 | 720 → `E2.tarjeta`; **`E3`** (off = 0): `cabecera` (implícito: la cámara no se mueve en el 780), `fila` 810, `paso` 840, `objetivos` 900, `avance` 960 (cajas de `pasos-2.json`) |
| `irisDesde` | 120, 375 | + **780** (`#iris3`, centro `(tx·K, ty·K + OFF2)`) |
| Toques dibujados | [60, 90, 105, 120, 150, 375, 450, 495, 600] | + **780, 840** |
| Ventana a 0,92 | F(724) | **F(964)** |
| Dip · corte | 837 · 840 | **1077 · 1080**; `tl.set({}, {}, 38.5)` |
| Música | duration 29; carril 28 / 28,4 / 29 | **duration 37; carril 0,7@36,0 → 0,224@36,4 → 0@37,0** |
| Sonidos | 18 | + `snd-toque-780` (toque.wav, `data-start` 26,033333: suena en el 781) · `snd-toque-840` (toque-b, 28,033333: el 841, `data-volume` 1,4) · `snd-aparicion-843` (28,1: el 843, un cuadro después de la tarjeta abierta del 842, 1,4); `snd-subida` **34,533333** (golpe en el 1080); `marca-clip` **36,38** |
| Halo (`fondo.html`) | 0, 180, 720 | **0, 180, 780, 960** |
| Stills | 466, 2401 | sin still nuevo: bajo el iris del 780 sigue `v25` (la tarjeta quieta) |

Para 9:16, lo mismo que decía la v1 (REVIEW §8) más `#m3in` con `top: 0` y `--f-latigo` sin cambios.

---

## 3. Las grabaciones: la escena `tools/ayuda/escenas/clips/membresia-valeria.mjs`

Una sola escena de **celular** (`movil: true`, `toque: false`: viewport 390×844 a 3× → cuadros de **1170×2532 px**, 30 cps), con `capturar.mjs
--modo video` sobre Kingdom Demo en español (`node capturar.mjs clips/membresia-valeria --idioma es --modo video`). Sale
`salida/video/es/clips/membresia-valeria/grabacion.mp4` + `pasos.json`. Datos ficticios; «Valeria Cardona Ríos» y su teléfono `5557654321`
no existen en la demo. **Cuentas:** 101 = el administrador (Andrés Felipe Restrepo Gómez), que coordina; 103 = el servidor (Jorge Gallego Gil),
acompañante. `refs`: `jorge`, `catCulto`, `evCulto` (ya en la escena).

### 3.1 Dos grabaciones, una escena

La grabación del 2026-10-30 (**G1**: `assets/grabaciones/grabacion.mp4` + `pasos.json`, 113,2 s) sirve a los cuadros 0–785 tal como se
montaron: **no se vuelve a cortar**. La ampliación necesita la ficha de Valeria con su tarjeta «Avance» abierta, que G1 no tiene (su tramo
`ficha` llegaba por el menú ⋮ y dejaba la tarjeta plegada). Se agrega el tramo **T5** al final de la misma escena y se **vuelve a grabar
entera** (la herramienta restaura el volcado y repite el alta, la asignación y la llamada en ≈ 110 s; todo lo crea la app, nada por SQL):

- la salida se copia como **`assets/grabaciones/grabacion-2.mp4`** y **`pasos-2.json`** (G2); G1 se queda donde está;
- el montaje usa G2 **solo desde el cuadro 780** (el toque en el nombre): la costura entre G1 y G2 cae debajo del iris. La tarjeta de Valeria
  es idéntica en las dos (mismo volcado, mismos textos, «Desde hoy · vence mañana»): si la lista quedó un par de píxeles distinta no importa,
  porque G1 sigue en pantalla hasta el 785 y G2 solo aparece dentro del círculo;
- el toque del 780 se dibuja con la caja de `a.nombre` de **`pasos-2.json`** (tramo `ficha`), proyectada sobre la tarjeta de G1: el nombre
  está en el mismo sitio en las dos (la tarjeta va al tope con `bloque: 'start'` en ambas).

**Opción B** (si se prefiere una sola grabación): montar todo con G2, re-mapeando los 25 tramos de `index.html` con los cuadros nuevos de
`pasos-2.json` por el mismo método de REVIEW §2 (cada corte en una pausa, cada toque en su pulso). Es más trabajo y no mejora nada que se vea.

### 3.2 Los pasos nuevos (T5): para copiar al final de `pasos: [...]`

Reemplazan a los dos últimos pasos de la escena del 2026-10-30 (el tramo `ficha` opcional: el toque en el botón ⋮ de la tarjeta,
`button[mat-icon-button]`, y en `a[mat-menu-item]:has-text("Ver ficha")`), que se borran. Van justo después de `{ ver: TARJETA, bloque: 'start', pausa: 4000 }`.
Selectores verificados en `ruta-persona-item.component.ts` (`a.nombre`, el `routerLink` a la ficha), `ficha-seccion.component.ts`
(`button[data-plegable][data-seccion="avance"]`, solo en pantallas de menos de 600 px), `ficha-avance.component.ts` (`#ficha-avance`,
`#avance-paso`, `#avance-objetivos`, `ul.historial`) y `persona.page.ts` (`#ficha-nombre`). Las acciones (`clic`, `espera`, `ver`, `bloque`,
`pausa`) son las de `capturar.mjs`; `ver` hace `scrollIntoView({ block })`, así que con `bloque: 'nearest'` **no mueve la página** si el
elemento ya está a la vista: sirve solo para anotar su caja.

```js
    // 31–37. T5 · La ficha de Valeria con su tarjeta «Avance» abierta (SPEC v2 §2, P6–P8). Sustituye al tramo `ficha` del 2026-10-30
    // (⋮ → «Ver ficha»): ahora un solo toque, en el nombre de la tarjeta (el enlace a la ficha). La página NO se desplaza: la ficha abre arriba
    // y la tarjeta «Avance» abierta cabe debajo de la cabecera (si no cabe, SPEC §5). Los `ver` con bloque 'nearest' no mueven nada visible:
    // anotan la caja del elemento para la cámara del montaje.
    { tramo: 'ficha', clic: `${TARJETA} a.nombre`, espera: 'button[data-plegable][data-seccion="avance"]', pausa: 1500 },   // el toque del 780 → la ficha, «Avance» plegada
    { tramo: 'avance', clic: 'button[data-plegable][data-seccion="avance"]', espera: '#avance-objetivos', pausa: 1500 },   // el toque del 840 → la tarjeta se abre de golpe
    { ver: '#avance-paso', bloque: 'nearest', pausa: 200 },                 // caja del bloque del paso (objetivo de la cámara del 840)
    { ver: '#avance-objetivos', bloque: 'nearest', pausa: 200 },            // caja de los chips de «Objetivos de conexión» (objetivo del 900)
    { pausa: 5000 },                                                        // la ficha abierta, quieta: cubre 842–1079 (7,9 s; a 0,5× sobra)
    { ver: '#ficha-avance', bloque: 'nearest', pausa: 200 },                // caja de la tarjeta entera (objetivo del 960); si no cabe entera, desplaza: por eso va después de la pausa
    { ver: '#ficha-avance ul.historial', bloque: 'nearest', pausa: 200 },   // caja del historial, por si entra en el plano del 960
```

Y en `pantallas` se agregan `'frontend-v2/src/app/pages/membresia/persona.page.ts'`, `'frontend-v2/src/app/pages/membresia/ficha-seccion.component.ts'`
y `'frontend-v2/src/app/pages/membresia/ficha-avance.component.ts'`. El comentario de cabecera de la escena cambia «ficha (opcional…)» por
«ficha · avance (T5, la ampliación)». `consolaEsperada` sigue igual.

### 3.3 La escena completa, paso por paso (la del 2026-10-30 + T5)

| # | Tramo | Paso | Qué se ve / ritmo | En el clip |
|---|---|---|---|---|
| 1 | `alta` | `{ como: 103, ir: '/servir/membresia/nueva', espera: '#campo-nombres' }` | el formulario vacío (antes de grabar) | — |
| 2 | | `{ escribir: { en: '#campo-telefono', texto: '5557654321' }, pausa: 300 }` | **fuera de cámara** | — |
| 3 | | `{ clicSiHay: '#genero-F', pausa: 300 }` | **fuera de cámara** | — |
| 4 | `nombres` | `{ escribir: { en: '#campo-nombres', texto: 'Valeria' }, pausa: 300 }` | **cuadro 0 del clip = la «V»** | 0–30 |
| 5 | | `{ escribir: { en: '#campo-apellidos', texto: 'Cardona Ríos' }, pausa: 300 }` | | 60–85 |
| 6 | `forma` | `{ elegir: { en: '#campo-forma', opcion: 'Servicio General' } }` | el selector; la categoría | 90–105 |
| 7 | | `{ espera: '.nivel2 .elegido[data-evento="{@evCulto}"]' }` | el chip elegido (la demo tiene un solo evento en la categoría) | 105–108 |
| 8 | `sin-senal` | `{ sinRed: true, despachar: 'online', espera: '#chip-sin-red' }` | «Sin conexión: ves la última copia» (no se ve en el montaje: REVIEW §4.2) | — |
| 9 | | `{ ver: '#btn-guardar-persona' }` | la página salta a «Registrar» | 114 |
| 10 | `registrar` | `{ clic: '#btn-guardar-persona', espera: 'mat-dialog-container', captura: 'guardada' }` | **el toque del 120**; «Guardada en este dispositivo» | 120–149 |
| 11 | | `{ clic: 'mat-dialog-container button >> nth=-1', oculto: 'mat-dialog-container' }` | «Entendido» | 150 |
| 12 | `sin-enviar` | `{ ver: '#titulo-membresia', bloque: 'start' }`, `{ espera: '#btn-pendientes', pausa: 1200 }` | «1 sin enviar» | 165 |
| 13 | `con-senal` | `{ sinRed: false }`, `{ oculto: '#btn-pendientes', pausa: 1200 }` | el contador se va | 178 |
| 14–18 | `asignar` | `como: 101` → Personas → buscar «Valeria Cardona» → su ficha → «Cuidado» → «Asignar» → «Jorge Gallego» → guardar (como está en la escena) | **fuera de cámara** (todo el tramo) | — |
| 19 | `seguimiento` | `{ como: 103, ir: '/servir/membresia/seguimiento', espera: '#lista-seguimiento app-ruta-persona-item' }` | Mi seguimiento | — |
| 20 | | `{ escribir: { en: '#buscar-seguimiento', texto: 'Valeria' }, espera: TARJETA }` | **fuera de cámara** | — |
| 21 | `tarjeta` | `{ ver: TARJETA, bloque: 'start', pausa: 3500 }` | **el mundo 2 (180)** | 180–374 |
| 22 | | `ver` del `p.detalle:has-text("Después")` de la tarjeta, `pausa: 200` | caja de «Después: …» | (300) |
| 23 | `reporte` | `clic` en el `button.cumplido` de la tarjeta, `espera: '#dialogo-reporte .pregunta'`, `pausa: 1500` | **el toque del 375** | 375–389 |
| 24 | | `{ marcar: '#dialogo-reporte .pregunta >> nth=0 >> mat-radio-button >> nth=0', pausa: 1200 }` | «Contestó» | 450 |
| 25 | | `{ escribir: { en: '#dialogo-reporte textarea >> nth=1', texto: 'Muy contenta, viene el domingo' }, pausa: 1200 }` | «Observaciones» | 495–566 |
| 26 | `resultado` | `{ ver: '#btn-enviar-reporte', pausa: 400 }` | caja del botón | (570) |
| 27 | | `{ clic: '#btn-enviar-reporte', espera: '#resultado-reporte', captura: 'cumplido', pausa: 3000 }` | **el toque del 600** | 600–690 |
| 28 | | `{ ver: '#siguiente-propuesto', pausa: 200 }` | caja de «Ahora va en: …» | (660) |
| 29 | `tarjeta-final` | `{ clic: '#btn-aceptar-siguiente', oculto: '#dialogo-reporte' }` | **el toque del 720** | 720–737 |
| 30 | | `{ ver: TARJETA, bloque: 'start', pausa: 4000 }` | la tarjeta al día, quieta | 738–785 (G1) |
| **31** | **`ficha`** | `clic` en el `a.nombre` de la tarjeta (`TARJETA + ' a.nombre'`), `espera: 'button[data-plegable][data-seccion="avance"]'`, `pausa: 1500` | **el toque del 780** (G2); la ficha con «Avance · Mensaje de bienvenida · ● A tiempo» plegada | 780–839 |
| **32** | **`avance`** | `{ clic: 'button[data-plegable][data-seccion="avance"]', espera: '#avance-objetivos', pausa: 1500 }` | **el toque del 840**: la tarjeta se abre | 840–1079 |
| **33** | | `{ ver: '#avance-paso', bloque: 'nearest', pausa: 200 }` | caja del paso | (840) |
| **34** | | `{ ver: '#avance-objetivos', bloque: 'nearest', pausa: 200 }` | caja de los chips | (900) |
| **35** | | `{ pausa: 5000 }` | quieto | 842–1079 |
| **36** | | `{ ver: '#ficha-avance', bloque: 'nearest', pausa: 200 }` | caja de la tarjeta entera | (960) |
| **37** | | `{ ver: '#ficha-avance ul.historial', bloque: 'nearest', pausa: 200 }` | caja del historial | (960) |

Totales (medidos en `pasos.json` de G1 y estimados para T5): T1 ≈ 29 s, T2 ≈ 37 s (no sale), T3 ≈ 40 s, **T5 ≈ 14 s** → ≈ 120 s de
grabación, de los que ≈ 83 s sirven, para 36 s de clip.
`pantallas`: las nueve de la escena + `persona.page.ts`, `ficha-seccion.component.ts`, `ficha-avance.component.ts`.

**Lo que `pasos-2.json` tiene que traer para el montaje** (y cómo se usa):
- paso 31: `toques[0]` (el dedo en el nombre, px del video) → el centro del iris 3 y la marca `tq-780`; `caja` = `a.nombre`;
- paso 31 → el primer cuadro con la ficha cargada: se busca a ojo en los cuadros siguientes al `suelta_cuadro` (como se hizo con los diálogos);
  es el `data-media-start` de `v26`;
- paso 32: `toques[0].cuadro` → el 840; `caja` (la fila «Avance») → la cámara del 810 y la marca `tq-840`; el primer cuadro con la tarjeta
  abierta (después de `suelta_cuadro`) → el 842;
- pasos 33, 34, 36, 37: sus `caja` → las cámaras del 840, 900 y 960 (`E3.paso`, `E3.objetivos`, `E3.avance`; el historial, si entra).

**Plan B para el tramo `asignar`:** como en la v1 (gancho `sql` solo si Coordinar o la ficha del administrador fallan a 390 px; no hizo falta el
2026-10-30).

---

## 4. Lo que se revisa en la vista previa

Cuadros a mirar: `npx hyperframes snapshot --at 0,1.5,3.6,4.0,4.2,5.5,6.0,6.2,8.5,10.5,12.5,13.3,15.1,18,20.0,20.1,22.3,24.0,24.6,25.5,26.0,26.1,26.2,27.0,27.5,28.0,28.07,28.4,29.5,30.0,30.5,32.0,32.4,32.6,35.9,36.0,36.4,38.4`
en las dos composiciones, `snapshot --range 5.8,6.3 --frames 16` para el látigo, **`--range 25.9,26.3 --frames 12`** para el iris de la ficha y
**`--range 27.9,28.5 --frames 18`** para la apertura de «Avance».

1. **Cuadro 0 (la miniatura):** la ventana con «Nueva persona» y la «V» escrita, «Valeria» en Fraunces ya puesta, «Datos de ejemplo» en su
   esquina. Nunca negro, nunca la marca. En 9:16, nada por encima de 168 ni por debajo de 1330 salvo halo y puntos.
2. **Cuadro 45:** las cuatro palabras aterrizadas y muertas de quietas; «Valeria» completo en el campo.
3. **Cuadro 120:** el toque en «Registrar» exactamente con el bajo; el círculo del iris nace del botón; la frase 2 entera en el 126.
   **165:** «1 sin enviar» a la vista; **178:** ya no está.
4. **176–186:** el látigo: ningún cuadro muestra la ventana vacía; la ceja cae en el 195 y no antes.
5. **Cuadro 253:** M sobre la tarjeta ≥ 44 px. **313:** C sobre «Después: Mensaje de bienvenida».
6. **360–374:** la frase 3 palabra a palabra sobre la tarjeta quieta; **380:** «Reporte del paso» abierto desde el toque.
7. **451:** «Contestó» marcado; **501–566:** la escritura se lee a ≥ 44 px y **la cámara no se mueve** mientras se escribe.
8. **600–613:** el toque con la segunda subida; `task_alt` y «“Llamada de bienvenida” cumplido»; la frase 3 ya no está.
9. **668:** «Ahora va en: Mensaje de bienvenida» a ≈ 51 px.
10. **720–738:** «Listo» en el golpe (se oye); el diálogo se va; la cámara en **G** sobre la tarjeta en el 733; **la tarjeta ya dice «Mensaje de
    bienvenida» en el 738**; **ninguna frase en pantalla**, la ceja sigue, la ventana a escala 1 (no se encogió).
11. **779 → 780 → 785:** la cámara **no se mueve**; el círculo nace en el nombre «Valeria Cardona Ríos»; dentro, la cabecera de la ficha;
    fuera, la tarjeta de G1 sin saltos. **783:** la ficha completa (foto, nombre, «Llegó el … · Culto o evento», los botones) y la fila
    **«Avance · Mensaje de bienvenida · ● A tiempo»** plegada; ningún cuadro de carga ni de página en blanco. **823:** M sobre la fila, ≥ 44 px.
12. **840 → 842:** el toque en «Avance» en el cuadro del golpe más fuerte; **en el 842 la tarjeta ya está abierta** (nada a medias); **853:** M
    sobre «Flujo: Llegó a un culto» · «Mensaje de bienvenida» · «● A tiempo · Desde hoy · vence mañana» · «Después: Se conecta con una casa de
    paz», ≥ 44 px; la frase 4 completa en el 852 («Y una ruta / para crecer»).
13. **913:** «Objetivos de conexión» con los tres chips enteros («Casa de paz · ¿cuál?», «Servir», «Clases de la visión»), ≥ 34 px, ninguno
    cortado por los bordes. Es la prueba más fuerte del clip: debe leerse de un vistazo.
14. **960–978:** la frase 5 aterrizada en el 972 con *ninguna* dorada; la ceja fuera; la ventana ya a 0,92 y corrida en el 978; la tarjeta
    «Avance» entera (o de la fila a los chips) en G⁺ ≥ 31 px.
15. **978–1076:** nada se mueve salvo el halo que se asienta; la frase 5 quieta ≥ 3,5 s. **1077–1079:** el dip al 40 %. **1080:** el primer
    cuadro de la firma (la baldosa creciendo), sin un cuadro de noche vacía entre medias.
16. **Sonido (medido, no oído):** cada `toque` un cuadro después de su imagen (61 · 91 · 121 · 151 · 376 · 451 · 496 · 601 · 721 · **781 · 841**);
    la `aparicion` del 843; las campanas en el 1091; la música a −10 dB en el 1092 y a 0 en el 1110; −16 LUFS, pico ≤ −1 dBTP; ningún tramo
    con dos sonidos de acción encimados salvo 601 + 603 y 841 + 843.
17. **Textos:** ninguna palabra que no esté en la app o en las cinco frases; ningún texto de la app < 28 px; las frases en 2 líneas en los dos
    formatos; `npx hyperframes check` en 0 errores (contraste AA incluido); las cifras siempre con «Datos de ejemplo».
18. **La historia sin sonido:** se entiende con la pantalla en silencio: llegó → registrada sin señal → alguien la llama → el siguiente paso →
    **su ficha → su ruta y sus objetivos** → ninguna se pierde → Kingdom.

---

## 5. Riesgos y lo que se decide al grabar

- **La tarjeta «Avance» abierta mide ≈ 480–520 px CSS** (fila, flujo, paso, «Después:», «Marcar cumplido», objetivos en dos filas, historial de
  tres) y empieza bajo una cabecera de ≈ 300–340 px: cabe en el viewport de 844 con poco margen; **el historial puede quedar cortado por
  abajo**. No pasa nada: la cámara del 960 encuadra de la fila a los chips. **Válvula** si ni los chips entran: un `{ ver: '#avance-objetivos',
  bloque: 'center' }` justo antes del `pausa: 5000` (un desplazamiento real, de una vez), y el montaje lo esconde dentro del movimiento del
  compás 16 (900–913), como hizo con el salto a «Registrar» (REVIEW §4.3). Nunca un desplazamiento a la vista con la cámara quieta.
- **El ancho de los chips** decide M o G⁺ en el 900: se mira `caja.w` de `#avance-objetivos` en `pasos-2.json` (≤ 279 → M, 44 px; si no, G⁺,
  34 px). Lo más probable es G⁺: «Casa de paz · ¿cuál?» (≈ 215 px) y «Servir» comparten fila.
- **«Casa de paz · ¿cuál?»** es un botón con borde porque la demo liga ese objetivo a la categoría «Casa de Paz» de Eventos (2 asistencias en
  30 días; `_demo_ruta_eventos.php`) y Jorge puede asignarle una casa. Es real y se deja: dice que falta elegirle casa. Si en el volcado de
  las capturas el vínculo no estuviera, saldría como chip simple con el ícono `cottage`; la cámara no cambia.
- **Los objetivos son los activos de la sede** (`personas_ruta_motor.php`: todos, no solo los del flujo), ninguno cumplido para Valeria. El
  orden y los nombres se confirman en la grabación: la plantilla trae Casa de paz · Servir · Clases de la visión.
- **La costura G1 → G2 (780):** la esconde el iris. Si la tarjeta de G2 no coincidiera con la de G1 (otro orden en la lista, otra hora), igual
  no se ve: G2 solo aparece dentro del círculo y ya es la ficha. Lo único que viaja de G2 a G1 es la posición del nombre para la marca del toque.
- **La fecha** de la ficha («Llegó el 30 de oct.», «Registrada por … el …») es la del día en que se graba; ninguna frase depende de ella.
- **La carga de la ficha** (cambio de ruta, cargador de la app): se corta como las esperas de los diálogos; si G2 muestra un esqueleto o un cuadro
  claro, no entra en el clip (el primer cuadro útil es el 783).
- **La apertura de «Avance»** ocurre al soltar el dedo (≈ 180 ms después de apoyarlo): el cuadro del toque (apoyar) va al 840 y la apertura se
  adelanta al 842 cortando la espera (como en el 120 y el 600). Si la app tardara más de un cuadro en pintar la tarjeta abierta, se toma el
  primer cuadro completo.
- **El 9:16** ve 345 px CSS en G: la cabecera de la ficha puede dejar la fila «Avance» fuera del encuadre del 783; la cámara de la ficha va
  40–60 px CSS más abajo (la barra superior de la app se corta). Se decide con las cajas.
- **La firma en el 50,05:** el clímax de la pista empieza ahí y la música sube mientras se desvanece (1 s); se mide en la mezcla que las campanas
  del 1091 queden limpias (REVIEW §6.2 midió −19,5 LUFS momentáneos en la firma de v1 con la música ya a −10 dB). Si la subida del clímax tapa
  la primera campana, el carril baja a −10 dB en el 1088 en vez del 1092.
- **+8 s, no 10:** la grilla manda; 38,5 s está dentro de los «~40». La alternativa de 40,5 s (firma en el 52,05) cae en un golpe más débil
  y sobre un redoble.
- **Lo heredado de la v1 sigue abierto:** la ampliación en C (1,35–1,48× de la fuente de 3×), el tramo 105–120 apretado, «Listo» fuera del
  encuadre del 660 (REVIEW §7), y la normalización a −16 LUFS que pide limitar.
- **Idiomas (en, pt después):** la misma escena con `--idioma en` graba la interfaz en inglés (incluida la ficha); las cinco frases se traducen
  y los saltos de línea se vuelven a fijar; la firma lleva `idioma`.
