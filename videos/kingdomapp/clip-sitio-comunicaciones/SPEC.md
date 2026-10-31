# SPEC · Clip del sitio: Comunicaciones — «Alguien nuevo escribe»

2026-10-30 · Contrato de construcción de la historia elegida en [STORY.md](STORY.md); el dueño ya no revisa guiones, así que se eligió aquí.
Cada adjetivo es un número, los valores por defecto están prohibidos con nombre y los planos van cuadro por cuadro sobre la grilla real de
la pista. Se construye desde aquí, se revisa contra esto y se cambia aquí cuando la vista previa cambie la película.

Hereda de [Membresía](../clip-sitio-membresia/SPEC.md) y de [Eventos](../clip-sitio-eventos/SPEC.md) el reloj, las letras, la ventana, las
curvas y la firma. También trae las lecciones del [REVIEW de Membresía](../clip-sitio-membresia/REVIEW.md), ya aplicadas:
- los niveles de sonido del kit;
- las entradas un cuadro antes del pulso;
- «Datos de ejemplo» a 31 px, abajo a la izquierda;
- el toque fuera de encuadre se oye y no se dibuja.

```text
GOAL:    Un pastor que no conoce Kingdom termina pensando «si alguien nuevo le escribe a mi iglesia, mi equipo le contesta en un toque, y
         cuando mando un aviso sé quién lo leyó», y toca «Prueba gratis 30 días».
OUTPUT:  HyperFrames · dos composiciones de la misma línea de tiempo: 1080×1350 (4:5, sitio y feed) y 1080×1920 (9:16, Reels e historias) · 30 fps.
TIME:    30,5 s = 915 cuadros: cuerpo 0–28,0 (cuadros 0–839) + firma 28,0–30,5 (840–914). 120 BPM = 15 cuadros por pulso (grilla real en §0).
LOOK:    Noche del sitio (#060D1F) con el halo y la retícula de puntos del kit; tinta #EAF0FF.
         Un solo acento, el dorado #E8B95A, en tres lugares y no más: la ceja «COMUNICACIONES», la palabra «nadie» y el botón de la firma.
         Fraunces 560 / −0,02 em para las frases; Inter para la ceja y «Datos de ejemplo».
         El medio: la app REAL de Kingdom Demo grabada en celular, nítida (1170 px de ancho), dentro de una ventana con radio 28, anillo de
         1 px y sombra 0 40 80 −24 al 65 %. Nunca un teléfono dibujado, nunca la marca ni el verde de WhatsApp.
OBJECTS: la ventana (el celular de quien atiende, un solo mundo); el punto de toque de la grabación; las cuatro frases; la ceja; la píldora
         «Datos de ejemplo»; la corona del cierre. Nada más existe en el cuadro.
MOTION:  Curvas por papel (§1.6). Un movimiento de cámara por compás (14 cuadros, power2.inOut), quieta después, y nunca mientras la app
         escribe, crece o se desplaza. Cada corte y cada entrada caen en un pulso; cada cambio grande, en un golpe
         (120 · 180 · 600 · 660 · 720 · 840).
SHOTS:   siete planos (§2).
BANNED:  §1.8.
QA:      §4.
```

---

## 0. El reloj: la grilla real de la pista

**La pista:** «Product Launch» (The_Mountain) del 14,05 al 42,05 s; el t = 0 del clip es el 14,05 de la pista.

**Los pulsos:** salen de `_identidad/musica/product-launch-the-mountain.pulsos.json` (el mismo mapa de Membresía y Eventos), restándoles
14,05 y redondeando a 30 fps.
- Todos caen en un múltiplo de 15 cuadros, salvo el de 9,455 s, que cae en el cuadro 284. Ahí no pasa nada.
- Cada pulso se calcula desde su índice, nunca sumando 15 una y otra vez.

| Compás | Cuadros | Pulsos (cuadro · fuerza) | Intensidad | Lo que le toca a este clip |
|---|---|---|---|---|
| 1 | 0–59 | 0 ·0,69 · 15 ·0,64 · 30 ·0,49 · 45 ·0,48 | 0,57 | La cola de la bandeja; la frase 1, una landing por pulso; la cámara a la fila de Mariana |
| 2 | 60–119 | 60 ·0,58 · 75 ·0,55 · 90 ·0,57 · 105 ·0,61 | 0,58 | **75:** toque en Mariana: su conversación entra. 90: la cámara a la cabecera y su mensaje. 105: el dedo se posa en «Tomar» |
| 3 | 120–179 | **120 ·0,93** (entra el bajo) · 135 · 150 · 165 | 0,66 | **120:** «Tomar»: «Atendiendo» y la nota. Frase 2. 150: la cámara baja al compositor |
| 4 | 180–239 | **180 ·0,87** (pico) · 195 ·0,83 · 210 · 225 | **0,77** | **180:** «/»: suben las respuestas rápidas. 195: la ceja «COMUNICACIONES» |
| 5 | 240–299 | **240 ·0,92** · 255 ·0,77 · 270 · 284 | 0,70 | **240:** «/horarios»: el compositor se llena |
| 6 | 300–359 | 300 ·0,77 · 315 ·0,75 · 330 · 345 | 0,68 | **300:** enviar: la respuesta en el hilo. 315: la cámara a la pregunta y la respuesta |
| 7 | 360–419 | 360 ·0,76 · 375 ·0,64 · 390 · 405 | 0,59 | Frase 3. **375:** volver: «Cola 3». 390: la cámara arriba |
| 8 | 420–479 | 420 ·0,75 · 435 ·0,61 · 450 · 465 | 0,59 | **420:** «Campañas». 450: la cámara a las tarjetas |
| 9 | 480–539 | 480 ·0,67 · 495 ·0,67 · 510 · 525 | 0,59 | 480: la lista baja hasta la invitación |
| 10 | 540–599 | 540 ·0,63 · 555 · 570 ·0,61 · 585 ·0,68 | 0,62 | 540: la cámara a la tarjeta de la invitación; el dedo llega en el 596 |
| 11 | 600–659 | **600 ·0,93** (segunda subida) · 615 ·0,69 · 630 · 645 | 0,66 | **600:** la invitación → el reporte con sus números (la primera prueba). Frase 3 sale |
| 12 | 660–719 | **660 ·0,90** · 675 ·0,89 · 690 ·0,76 · 705 ·0,68 | **0,81** | **660:** «respondieron»; 675: los nombres con «Allí estaré» (la prueba más fuerte); 690: la cámara a los nombres |
| 13 | 720–779 | **720 ·0,96** · 735 ·0,77 · 750 · 765 | 0,73 | Frase 4; la ceja se va; la ventana se hace a un lado |
| 14 | 780–839 | 780 ·0,88 · 795 ·0,74 · 810 · 825 | 0,71 | Quieto; la subida; el dip |
| — | **840** ·1,00 | el golpe más fuerte de la pista | — | **La firma.** La música se va debajo de las campanas |

Las dos pruebas caen en los dos golpes reales de la segunda subida:
- **600 (0,93):** el reporte con «115 leídos»;
- **660–675 (0,90 · 0,89):** los nombres de quienes respondieron. Es el compás más fuerte del cuerpo.

El primer gesto de Kingdom, «Tomar», cae en el bajo (120) y la frase final en el 720 (0,96).

---

## 1. Los números del estilo

### 1.1 Paleta (tokens de `identidad/kit.css`; nada fuera de esta lista)

| Papel | Token | Valor | Dónde puede aparecer |
|---|---|---|---|
| Fondo | `--k-noche` | `#060D1F` | A sangre, todo el cuerpo |
| Halo | `.k-halo` | azul `rgba(53,118,218,.45)` arriba a la derecha + dorado `rgba(217,162,52,.22)` abajo a la izquierda | Fondo, bajo todo; se asienta 1,08 → 1 en 0, 180 y 720 |
| Puntos | `.k-puntos` | `rgba(169,190,235,.35)`, 2 px cada 42 px, desvanecidos a la izquierda | Fondo; **nunca se mueven** |
| Tinta | `--k-noche-tinta` | `#EAF0FF` | Las frases |
| Acento | `--k-noche-dorado` | `#E8B95A` | Solo: la ceja «COMUNICACIONES», la palabra *nadie*, el botón de la firma |
| Anillo | `--k-noche-linea` | `rgba(234,240,255,.12)` | El borde de la ventana |
| Fondo de la app | `--k-app-fondo` | `#FAF9FD` | Detrás de la grabación (nunca se ve) |
| Azul de marca | `--k-azul` | `#3576DA` | **Solo en la firma** (la baldosa) |
| Placa | `.k-datos-ejemplo` | `rgba(6,13,31,.72)` | La píldora «Datos de ejemplo» |
| Dip | — | `rgba(6,13,31,.40)` | Los 3 cuadros antes de la firma, solo sobre la ventana |

Los colores de la app viven dentro de la grabación y no se tocan:
- la burbuja que sale (primary-container) y la que entra (blanca);
- la píldora «En la cola» (tertiary-container) y «Atendiendo» (secondary-container);
- los globos de no leídos;
- las fichas «Leído»;
- el bloque rojo «Por qué no les llegó».

`--k-noche-tinta-2` no se usa.

### 1.2 Tipografía

| Pieza | Clase (kit v1.1) | Familia · peso | 4:5 | 9:16 | Interlineado · tracking | Reglas |
|---|---|---|---|---|---|---|
| Frase | `.k-feed-frase` (`.k-titular` + `.k-vertical` en 9:16) | Fraunces 560; `<em>` itálica 500 dorada | **80 px** | **104 px** | 1,04 · −0,02 em | Máx. **2 líneas** en 4:5 (3 en 9:16), saltos fijados a mano. Izquierda. Sin sombra |
| Ceja | `.k-feed-ceja` (`.k-ceja`) | Inter 700, MAYÚSCULAS | **30 px** | **34 px** | 1 · +0,10 em | Una palabra: «COMUNICACIONES» (≈ 330 px a 30 px) |
| Datos de ejemplo | `.k-datos-ejemplo .k-feed-datos` | Inter 600 | **31 px**, píldora de 56 px de alto | igual | 1 · 0 | Blanca sobre la placa; **abajo a la izquierda de la ventana**, a 24 px del borde visible |
| Texto de la app | (grabación) | Inter de la app: cuerpo 14 px CSS, secundario 12 px, títulos 16–22 px | ≥ **28 px** lo que se lee | ≥ **28 px** | — | Ver §1.5: cada encuadre declara qué se lee y a cuántos px |

Saltos de línea fijados (4:5, ≈ 23 caracteres por línea a 80 px en 888 px):
- «Alguien nuevo escribe. / ¿Quién contesta?»
- «Todo tu equipo, / un solo número.»
- «Y sabes quién / leyó el aviso»
- «Habla con tu iglesia, / sin perder a *nadie*»

En 9:16 (≈ 19 por línea a 104 px) la frase 1 y la frase 4 van en tres líneas; las demás quedan igual:
- «Alguien nuevo / escribe. / ¿Quién contesta?»
- «Habla con / tu iglesia, / sin perder a *nadie*»

### 1.3 Radios y sombras

| Pieza | Radio | Sombra / borde |
|---|---|---|
| `.k-ventana` | **28 px** | `0 0 0 1px var(--k-noche-linea)` + `0 40px 80px -24px rgba(0,0,0,.65)`; `overflow: hidden`; fondo `--k-app-fondo` |
| «Datos de ejemplo» | 999 px | ninguna |
| Frases y ceja | — | **ninguna** |
| Firma | la del kit (`cierre-clip` / `cierre-corto`) | la del kit |

### 1.4 Disposición por formato

| | 4:5 (1080×1350) | 9:16 (1080×1920) |
|---|---|---|
| Márgenes | 96 a los lados, 72 arriba | 60 a los lados; banda útil **168–1330**; debajo de 1330 solo halo y puntos |
| Ceja | x 96 · y 72 (30 px → termina en 108) | x 60 · y 188 (34 px → 229) |
| Frase | x 96 · y 124 · ancho 888 · 2 líneas de 83 px → 290 | x 60 · y 236 · ancho 960 · hasta 3 líneas de 108 px → 560 |
| Ventana | x 100 · y 360 · **880 × 1050**: sangra 60 px por abajo (se ve 880×990) | x 60 · y 480 · **960 × 850**, completa |
| Ventana al final (desde el 724) | escala **0,92** desde el centro inferior + x **+48** | escala 0,92 desde el centro superior + x **+36** |
| Datos de ejemplo | abajo a la izquierda de la ventana, 24 px del borde visible | ídem |
| Firma | `cierre-clip` (kit v1.1) | `cierre-corto` (kit v1) |

Variables de `index.html` (como en Membresía y Eventos):
- **4:5:** `--f-k: 0.752137`, `--f-grab-alto: 1904.41px`.
- **9:16:** `--f-k: 0.820513`, `--f-grab-alto: 2077.54px`, `--f-ventana-hvis: 850px`.

Sin `--f-latigo` ni `#m2`, porque es un solo mundo. La tira lleva un solo `.mundo` con su envoltorio `#m1in` para el aterrizaje del 78.

### 1.5 La cámara dentro de la ventana: escalas

La grabación va a 3× (390×844 px CSS → **1170×2532 px**). **ppc** = píxeles del cuadro por píxel CSS del celular.

| Nivel | Qué se ve | 4:5: ppc (escala del video) · visibles en px CSS | 9:16: ppc (escala) · visibles | 14 px → | 12 px → |
|---|---|---|---|---|---|
| **G** general | todo el ancho del celular | **2,256** (0,752) · 390 × 439 | **2,462** (0,821) · 390 × 345 | 31,6 · 34,5 | 27,1 · 29,5 |
| **G⁺** | una tarjeta o una lista con sus márgenes | 2,436 (0,812) · 361 × 406 | 2,659 (0,886) · 361 × 320 | 34 · 37 | 29,2 · 31,9 |
| **M⁻** | el cierre (solo con la ventana a 0,92) | 2,594 (0,865) · 339 × 381 | 2,831 (0,944) · 339 × 300 | 36,3 · 39,6 (×0,92: 33,4 · 36,5) | 31,1 · 34 (×0,92: **28,6** · 31,3) |
| **M** medio | una conversación, la lista de respuestas o los nombres | **3,158** (1,053) · 279 × 313 | **3,446** (1,149) · 279 × 247 | 44 · 48 | 37,9 · 41,4 |
| **C** cerrado | una línea | 4,061 (1,354) · 217 × 244 | 4,431 (1,477) · 217 × 192 | 57 · 62 | 48,7 · 53 |

G = ×1,00 · G⁺ = ×1,08 · M⁻ = ×1,15 · M = ×1,40 · C = ×1,80 sobre el general. C no se usa en este clip: las burbujas y las tarjetas miden
más de 217 px de ancho y quedarían cortadas.

**La regla de los 28 px**, más precisa que en Eventos porque esta app usa mucho texto secundario de 12 px:
- **lo que el plano dice que se lee** queda en ≥ 28 px;
- el texto secundario que nadie necesita leer (la hora de una fila, «•••• 8588 · fecha», los porcentajes de los KPI a G) puede quedar en
  24–27 px.

**Cómo se mueve la cámara:**
- Es `scale` + `x`/`y` sobre `#cam` dentro de la ventana, sujeta a los bordes de la grabación (la función `enc()` de Membresía).
- El `<video>` nunca se transforma ni se busca.
- El objetivo de cada movimiento es una **caja de `pasos.json`** (px CSS del viewport 390×844).

**De dónde salen las cajas de abajo:**
- Son estimaciones medidas sobre el CSS de las pantallas (`bandeja.page.ts`, `bandeja-hilo.component.ts`, `campanas.page.ts`,
  `campana-reporte.component.ts`) y sobre las capturas de escritorio de la ayuda (`comunicaciones/bandeja/01-cola`, `02-tomar`,
  `campanas/06-reporte`).
- La barra de la app ocupa 0–56 y la barra inferior del celular 764–844.
- **Las cajas reales salen de la grabación** y se anotan en el REVIEW.

| Objetivo | Nivel | Centro estimado (x, y CSS) | Lo que debe quedar dentro (y lo que se lee) |
|---|---|---|---|
| `cola` | G | (195, 345) → 125–564 | Las pestañas del módulo, **«Cola 4 · Mis chats 2 · Todas 8»**, «Buscar por nombre o número» y las filas de Juan, Carolina y **Mariana** (nombre, «Hola, buenas noches. ¿A qué hor…», su globo, «Sin ficha») y la parte de arriba de Camilo. Se leen los nombres y los mensajes (31,6 px) |
| `fila` | G⁺ | (195, 400) → 197–603 | Las filas de Carolina, **Mariana entera** y Camilo a 34 px. **Y, en la pantalla siguiente, la burbuja del mensaje de Mariana** (≈ 206–330): este encuadre recibe el match cut del 78 |
| `hilo-cabeza` | M | (195, 216) → 60–373 | ← «Mariana Ospina», «Sin ficha · +575550123987 · Línea principal» (38 px), **«En la cola»**, **«Tomar»** y sus tres íconos, «Hoy» y **la burbuja entera a 44 px**; debajo, el lugar donde aparece la nota |
| `compositor` | M | (195, 600) → 443–756 | El hueco donde suben las respuestas (≈ 470–690), el compositor «Escribe un mensaje» con enviar y «Puedes escribir libre durante … h … min» |
| `respuesta` | M | (195, 330) → 173–486 | La burbuja de Mariana, la nota «… tomó la conversación» y **la respuesta** («Andrés Felipe Restrepo Gómez», el horario, la hora y su palomita). Al volver (375), en este mismo encuadre: **«Cola 3 · Mis chats 3»** (34,7 px) y las filas que quedan |
| `arriba` | G | (195, 219) → 0–439 | La barra, «Bandeja», **las pestañas** (Bandeja · el ícono de Campañas · Automatizaciones · Más), las vistas y las dos primeras filas; después del toque del 420, en el mismo encuadre: «Campañas», «Nueva campaña», las pestañas y los filtros |
| `campanas` | G⁺ | (195, 380) → 177–583 | Los filtros y las primeras tarjetas: «Bienvenida a los nuevos de octubre · Borrador», «Noche de oración del viernes · Fuera de horario» con su barra y sus números |
| `tarjeta` | G⁺ | sobre la caja de la tarjeta de la invitación después de bajar (≈ 512–682) | **«Invitación: culto de jóvenes del domingo» · «Completada»**, la línea de detalle, la barra y «137 enviados · 100 % entregados · 84 % leídos · 23 respondieron · 39 clics · 2 fallidos» (29 px) |
| `kpis` | G | (195, 545) → 325–764 | La barra al 100 % y las cuatro primeras filas de números: **139 Total · 137 enviados 99 % · 137 entregados 100 % · 115 leídos 84 % · 23 respondieron 17 % · 39 clics 28 % · 2 fallidos 1 % · 0 omitidos**. Las cifras a 50 px y los nombres a 31,6 px |
| `nombres` | M | (195, 380) → 223–536, tras bajar | «Destinatarios (23)» y las cinco primeras filas: el nombre (50 px), la ficha **«Leído»** y «•••• 8588 · fecha · **↩ Allí estaré** · abrió el enlace» (38 px) |
| `cierre` | M⁻ | (195, 420) → 229–611 | «Destinatarios (23)» y seis filas con su «Leído» y su «Allí estaré»; con la ventana a 0,92, el texto de 12 px queda en 28,6 px |

### 1.6 Curvas y duraciones (cada tween lleva su curva por nombre)

| Papel | Curva | Cuadros | Detalle |
|---|---|---|---|
| `entrada-palabra` | `power4.out` | 4 | `filter: blur(6px) → 0` + opacidad; **sin desplazamiento**; arranca un cuadro antes del pulso (el primer cuadro visible es el pulso). Palabras a 2 cuadros, salvo la frase 1 (una landing por pulso) |
| `entrada-linea` | `power4.out` | 6 | La línea entera, blur 8 → 0 (frase 2 y ceja) |
| `salida-texto` | `power3.in` | 4–5 | Blur 0 → 8 + opacidad, la línea entera, 2–3 cuadros antes del pulso («blur swap») |
| `camara` | `power2.inOut` | **14** | Un movimiento por compás; quieta después; **nunca mientras la app escribe, crece o se desplaza** |
| `aterrizaje-app` | `power3.out` | 10 | El match cut del 78: la conversación de Mariana entra a escala **1,03 → 1,00** en `#m1in`, con el origen en el centro de lo visible de la ventana. **Es la única vez**: las demás pantallas (la lista en el 375, las campañas en el 420, el reporte en el 603) cambian dentro de la app sin ayuda |
| `dedo-espera` | `power2.out` | 4 | La marca de toque aparece y **se queda quieta** hasta el toque, solo 105 → 120 (sobre «Tomar», esperando el bajo). Las demás marcas aparecen 4 cuadros antes de su toque |
| `toque` | `power2.out` / `power2.in` | 4 · 2 · 6 | La marca aparece (opacidad 0 → 1, escala 0,6 → 1), se hunde a 0,86 en el cuadro del toque y se va 6 cuadros después. La onda va de 36 a 58 px CSS en 0,45 s, en `#015BBE` al 90 % |
| `ventana-cambio` | `power2.inOut` | 15 | Escala 1 → 0,92 + x (§1.4), 724–738 |
| `halo` | `sine.out` | 90 | 1,08 → 1,00 en 0, 180 y 720; los puntos no se mueven |
| `dip` | escalón | 3 | 837–839 |
| firma | las del kit | 75 | `back.out(2.2)` de la corona; **no se imita en el cuerpo** |
| resortes | ninguno | — | Nada rebota salvo la corona |
| velocidad de la grabación | `data-playback-rate` por tramo (o carril `rate`) | — | Entre **0,35× y 3,5×**; las rampas van entre acciones, nunca durante una tecla o un toque. Los cortes caen en los `huecos_de_pantalla` de `pasos.json` |

`data-motion-blur="on"` con `data-motion-blur-shutter="180"` en la raíz. **Nunca `filter: blur()` sobre la grabación.** No hay iris en este clip.

### 1.7 Sonido

| Capa | Fuente | Nivel | Regla |
|---|---|---|---|
| Música | `assets/musica/product-launch-the-mountain.mp3`, `data-media-start` 14,05, dura 29 s | 0,7 en el carril de volumen (−18 LUFS, `kit.json`) | 0,7 hasta el 840 → 0,224 en el 852 → 0 en el 870 |
| Sonidos de acción (kit v1.1) | `toque` · `aparicion` · `desliz` · `subida` · `confirmacion` | El nivel del kit (`data-volume="1"`, 4–10 dB bajo la música); **1,4** solo en los cinco toques clave (121 · 181 · 301 · 601 · 661) y en las `confirmacion` del 303 y del 688 | `data-start` = cuadro / 30 − acento; el pico suena **un cuadro después** de su imagen. `toque` rota entre a (`toque.wav`), b (+3 %) y c (−3 %), nunca la misma dos veces seguidas. Sin tics de tecla |
| Sonido de marca | `identidad/audio/sonido-marca.wav` | tal cual | En **28,38 s** (cuadro 851) |
| Mezcla | — | −16 LUFS integrados, pico real ≤ −1 dBTP | `normalize-audio` sobre el render de entrega; se comprueba con `hyperframes audio --json`. Si el normalizador recorta, los 1,4 bajan a 1,2 |

Los 20 eventos, con su causa (el cuadro del sonido es el de la imagen + 1):

| Cuadro | Sonido | Causa |
|---|---|---|
| 76 | toque a | La fila de Mariana |
| 121 | toque c (1,4) | «Tomar» |
| 123 | aparicion | «Atendiendo» y la nota «… tomó la conversación» |
| 181 | toque b (1,4) | El compositor y «/» (las respuestas suben con el mismo toque: no llevan sonido propio) |
| 196 | aparicion | La ceja «COMUNICACIONES» |
| 241 | toque a | «/horarios» |
| 243 | aparicion | El compositor se llena con el horario |
| 301 | toque c (1,4) | Enviar |
| 303 | confirmacion (1,4) | La respuesta queda en el hilo |
| 376 | toque b | Volver (la flecha queda fuera del encuadre: se oye y no se dibuja) |
| 421 | toque a | La pestaña «Campañas» |
| 485 | desliz | La lista baja hasta la invitación (acento en el 485) |
| 601 | toque b (1,4) | La invitación |
| 603 | confirmacion (1,0) | El reporte con sus números |
| 661 | toque c (1,4) | «respondieron» |
| 672 | desliz | La app baja a los nombres (acento en el 672) |
| 688 | confirmacion (1,4) | Los nombres con «Leído» y «Allí estaré», ya quietos |
| 796–853 | subida | Su golpe (acento de 1,5 s) en el 840 |
| 851 | campanas | La firma + 0,38 |

Ningún sonido va sin causa visible, y entre 0 y 6 s hay cinco. Nada de whoosh en los movimientos de cámara ni en el cambio de pantalla de
los toques. Las tres `confirmacion` son una por prueba: 303, 603 y 688.

### 1.8 BANNED: los valores por defecto prohibidos, con nombre

**Los 20 de Membresía, enteros:**
- fundido de 0,5 s para todo; fade + deslizar hacia arriba; zoom lineal; «creeping scale»; fundido cruzado entre mundos;
- teléfono dibujado;
- texto que se mueve mientras se lee o «respira»;
- logo en una esquina;
- brillo, neón, partículas, orbes; degradados nuevos y tarjetas de vidrio;
- tres tarjetas en fila, KPI, «01 / 02», corner brackets, HUD;
- whoosh en cada corte y el mismo `toque` sin rotar;
- reproducción fuera de 0,35×–3,5×;
- retocar un píxel de la app;
- texto que se lee < 28 px;
- centrarlo todo;
- cifras sin «Datos de ejemplo»;
- más de 3 s sin cambio visible;
- un pulso vacío entre el 0 y el 330 (la excepción del 330–359 está abajo, en el 29);
- `from()`, `autoAlpha` sobre un `.clip`, `transform` de CSS donde GSAP transforma, el `<video>` y su envoltorio con tiempo a la vez.

**Los de Eventos que valen aquí:** la cámara y el desplazamiento de la app a la vez; dos `confirmacion` a menos de 1 s; un látigo «para
animar»; dibujar una marca de toque donde la grabación no tocó.

**Los de este clip:**

21. **Créditos, saldos, precios o el cupo en pantalla** (decisión 215). La grabación nunca pasa por «Uso», «Calcular», «Encender una
    automatización», «Plataforma → Comunicaciones» ni por el costo aproximado en Meta. Si una pantalla del recorrido los trajera, la cámara
    no va ahí y se corta antes.
22. **La marca de WhatsApp**: su logo, su ícono, su verde (`#25D366`), su fondo de chat con dibujos o una burbuja «estilo WhatsApp» hecha a
    mano. Lo que se ve es la bandeja de Kingdom tal como es; la palabra «WhatsApp» no aparece en ninguna frase.
23. **Un número de WhatsApp real** o uno que no sea de la semilla. Los de la demo son ficticios (`+57 555 …`). Nada se escribe a mano en
    un número.
24. **Palomitas azules, «leído» o «entregado» en la respuesta a Mariana.** Meta simulado no manda esos estados: queda con una palomita
    (enviado) y así se muestra. No se dibuja, no se colorea ni se «completa».
25. **Recrear o «ayudar» a la app con gráficos propios:** las burbujas, la lista de respuestas, los KPI o los nombres; un contador
    animado («count-up») sobre 115 o 139; un subrayado sobre «Allí estaré». Todo sale de la grabación, y las cifras llegan quietas, como
    las pinta la app.
26. **Un látigo, un iris o un fundido para pasar de la bandeja a las campañas.** Es el mismo celular: la app cambia de pantalla por sus
    toques (volver, «Campañas», la invitación). El iris queda para cuando se abre una hoja, y aquí no se abre ninguna.
27. **Dibujar el toque del 375** (volver): la flecha está fuera del encuadre `respuesta`. Se oye y no se dibuja, como el «Listo» de
    Membresía.
28. **Copiar la animación de la app.** Las tarjetas de «Campañas» suben escalonadas (`k-subir`) porque así es la app. Ninguna pieza del
    montaje (frase, ceja, píldora) sube así.
29. **Más de 1,5 s de quietud entre el 0 y el 360, salvo una.** La excepción es el 330–359: la respuesta enviada se lee. Es el cierre del
    primer acto, y ahí solo cae el final del movimiento de cámara del 315.

Después del primer render, cada valor por defecto que aun así aparezca se nombra aquí y se corrige.

---

## 2. Los planos, cuadro por cuadro

### 2.0 Convenciones

- **G / G⁺ / M⁻ / M** y los nombres de objetivo (`cola`, `fila`, `hilo-cabeza`…) son los de §1.5. «Sobre X» = la caja de X centrada en la
  ventana.
- **Pulso** es el cuadro de la grilla de §0. Un evento «en el 120» aterriza en el cuadro 120 y su sonido suena en el 121.
- **Grabación:** una sola, `clips/comunicaciones-alguien-nuevo` (cuenta 101), con los tramos `cola · abrir · tomar · barra · horarios ·
  enviar · volver · campanas · bajar · reporte · respondieron` (§3). Los cortes de video caen en las pausas de la grabación.
- **Textos de la app:** son los reales, verificados en `frontend-v2/public/i18n/es.json` (`comb.*`, `comc.*`, `com.*`), en las plantillas
  de los componentes y en la semilla (`tools/ayuda/semillas/comunicaciones.php`):
  - de la bandeja: «Bandeja», «Cola», «Mis chats», «Todas», «Buscar por nombre o número», «Sin ficha», «Hoy», «En la cola», «Tomar»,
    «Atendiendo», «{u} tomó la conversación», «Escribe un mensaje», «Puedes escribir libre durante {h} h {m} min»;
  - las respuestas rápidas: «/horarios · Horarios de los cultos · Nos reunimos los domingos a las 8:00 a. m. y a las 10:30 a. m., y los
    miércoles a las 7:00 p. m.»;
  - de las campañas: «Campañas», «Nueva campaña», «Completada», «Total», «enviados», «entregados», «leídos», «respondieron», «clics»,
    «fallidos», «Botones que tocaron», «Por qué no les llegó», «Destinatarios», «Leído», «Allí estaré».

  Lo que cambia con la semilla lleva «(real)»: los nombres, las horas, las fechas, el número de Mariana, las cifras de la campaña y el
  nombre de la cuenta («Andrés Felipe Restrepo Gómez»).
- Las frases van siempre en el mismo lugar (§1.4) y una a la vez; la ceja va encima de la frase.
- **Posiciones CSS** de la app: estimadas (§1.5); las reales salen de `pasos.json`.

### 2.1 Tabla maestra (todo lo que cambia, por cuadro)

| Cuadro | Pulso | La app (grabación) | Cámara | Texto | Sonido | Transición |
|---|---|---|---|---|---|---|
| **0** | ● | Tramo `cola` · **Bandeja**, vista **«Cola 4»**: las filas de Juan Rivera González (real), Carolina Mejía Arango (real), **Mariana Ospina · «Hola, buenas noches. ¿A qué hor…» · su globo «1» · «Sin ficha»** y Camilo Ríos (real), cada una con su hora y sus no leídos. «Datos de ejemplo» abajo a la izquierda | G `cola` | **«Alguien»** ya aterrizada (es la miniatura) | — | — |
| 15 · 30 · 45 | ● ● ● | quieta | quieta | **«nuevo escribe.»** 15 · **«¿Quién»** 30 · **«contesta?»** 45. La frase 1 completa y quieta hasta el 117 | — | |
| 46–59 | | quieta | **Movimiento del compás 1:** G → **G⁺ `fila`** (Mariana entera, al centro) | | — | |
| 71–81 | **75 ●** | **75: toque en la fila de Mariana.** La app navega a `?c=` y abre su conversación; el corte cae en la espera | quieta | | `toque` a en el 76 | **Match cut sobre el toque:** en el 78 la pantalla ya es la conversación y entra 1,03 → 1,00 (`aterrizaje-app`, 78–88) |
| 78–89 | | **La conversación (real):** «Hoy» y la burbuja **«Hola, buenas noches. ¿A qué hora es el culto del domingo? Es mi primera vez y quiero ir con mi esposo.»** con su hora | G⁺ (`fila`, el mismo encuadre) | | — | |
| **90–103** | ● | quieta | **Movimiento del compás 2:** G⁺ → **M `hilo-cabeza`**: ← «Mariana Ospina», «Sin ficha · +575550123987 · Línea principal», **«En la cola»**, **«Tomar»**, la burbuja a 44 px | | — | |
| **105** | ● | quieta | quieta | | — | **`dedo-espera`:** la marca aparece sobre «Tomar» (105–109) y se queda |
| 117–121 | | | | La frase 1 sale | | |
| **120** | **●●● bajo** | **Toque en «Tomar»** (pasa por `loading.wrap`: si asoma la K, se corta en la espera) | quieta | **«Todo tu equipo, / un solo número.»** `entrada-linea` 120–126 | **`toque` c (1,4) en el 121** | |
| 122 | | **La conversación cambia (real):** la píldora pasa a **«Atendiendo»**, «Tomar» se va (quedan transferir, cerrar y el panel) y bajo la burbuja aparece la nota **«Andrés Felipe Restrepo Gómez tomó la conversación · hh:mm»** | quieta | La frase 2, quieta | `aparicion` en el 123 | |
| **150–163** | ● | quieta | **Movimiento del compás 3:** M `hilo-cabeza` → **M `compositor`** (el hueco vacío y el compositor) | | — | |
| 176 | | | | La frase 2 sale, 177–181 | | La marca aparece sobre el compositor |
| **180** | **●●● pico** | **Toque en el compositor y «/»** (la tecla en el ≈ 182) → **suben las respuestas rápidas (real):** «/bienvenida · Bienvenida», **«/horarios · Horarios de los cultos»**, «/oracion · Petición de oración», «/gracias · Gracias», cada una con su texto en gris; el compositor dice «/» | quieta (ya está en M `compositor`: la lista sube dentro del encuadre) | — | **`toque` b (1,4) en el 181** | Halo 1,08 → 1 (180–270) |
| **195** | ● | Las respuestas, quietas | quieta | **«COMUNICACIONES»** `entrada-linea` 195–201 | `aparicion` en el 196 | |
| 236 | | | | | | La marca aparece sobre «/horarios» |
| **240** | **●●** | **Toque en «/horarios»** → la lista se va y el compositor crece (field-sizing) con **«Nos reunimos los domingos a las 8:00 a. m. y a las 10:30 a. m., y los miércoles a las 7:00 p. m.»** (50 px) | quieta | | `toque` a en el 241 · `aparicion` en el 243 | |
| 270 · 284 | ● ● | quieta: el texto se lee | quieta | | — | |
| 296 | | | | | | La marca aparece sobre enviar |
| **300** | ● | **Toque en enviar** → el compositor se vacía y en el hilo aparece **la respuesta** (a la derecha, «Andrés Felipe Restrepo Gómez», el horario, la hora y **una palomita**: enviado) | quieta | | **`toque` c (1,4) en el 301** · **`confirmacion` (1,4) en el 303** | |
| **315–328** | ● | quieta | **Movimiento del compás 6:** M `compositor` → **M `respuesta`** (la pregunta, la nota y la respuesta) | | — | |
| 330–359 | ● ● | quieta: se lee la respuesta (la excepción del BANNED 29) | quieta | | — | |
| **360** | ● | quieta | quieta | **«Y sabes quién / leyó el aviso»:** Y 360 · sabes 362 · quién 364 · leyó 366 · el 368 · aviso 370 | — | |
| **375** | ● | **Toque en volver** (la flecha, fuera del encuadre) → **la lista (real):** **«Cola 3 · Mis chats 3 · Todas 8»**, Juan, Carolina, Camilo. Mariana ya no espera | quieta (M `respuesta`: los contadores y las filas entran en él) | La frase 3, quieta | `toque` b en el 376 (sin marca) | Corte en la espera (la app cambia de pantalla) |
| **390–403** | ● | quieta | **Movimiento del compás 7:** M → **G `arriba`** (la barra, «Bandeja», las pestañas con el ícono de Campañas) | | — | |
| 416 | | | | | | La marca aparece sobre el ícono de Campañas |
| **420** | ● | **Toque en «Campañas»** → **las campañas (real):** «Campañas», «Nueva campaña», la pestaña ya con texto, los filtros «Todas · En curso · Programadas · …» y las tarjetas que suben escalonadas (la animación de la app) | quieta (G `arriba`) | | `toque` a en el 421 | Corte en la espera |
| **450–463** | ● | quieta | **Movimiento del compás 8:** G → **G⁺ `campanas`**: «Bienvenida a los nuevos de octubre · Borrador», «Noche de oración del viernes · Fuera de horario» | | — | |
| **480–495** | ● ● | **La lista baja hasta la invitación** (`ver`, desplazamiento suave a 1×): pasan «Recordatorio: Congreso de Jóvenes · Programada» y «Boletas del Congreso de Jóvenes · Programada» (real); llega **«Invitación: culto de jóvenes del domingo · Completada»** | **quieta** | | `desliz` (acento 485) | |
| **540–553** | ● | quieta | **Movimiento del compás 10:** G⁺ `campanas` → **G⁺ `tarjeta`** (la invitación, con su barra llena y sus números) | | — | |
| 596 | | | | La frase 3 sale, 597–601 | | La marca aparece sobre el nombre de la invitación |
| **600** | **●●● 2.ª subida** | **Toque en la invitación** → **su reporte (real):** el título, «← Campañas», «Exportar», **«Completada»** · «invitacion_culto · Línea principal · salió el … · terminó el …», la barra al 100 % y los números: **139 Total · 137 enviados 99 % · 137 entregados 100 % · 115 leídos 84 % · 23 respondieron 17 % · 39 clics 28 % · 2 fallidos 1 % · 0 omitidos** | **Movimiento del compás 11:** G⁺ → **G `kpis`**, 600–613 (el reporte aparece en el 603, ya con la cámara en camino) | | **`toque` b (1,4) en el 601** · `confirmacion` (1,0) en el 603 | Corte en la espera |
| 615–655 | ● ● ● | Los números, quietos | quieta | | — | |
| 656 | | | | | | La marca aparece sobre «respondieron» |
| **660** | **●●● golpe** | **Toque en «respondieron»** → la tarjeta queda marcada (contorno azul) y la lista de abajo se filtra; el título pasa a «Destinatarios (23)» (fuera del encuadre) | quieta | | **`toque` c (1,4) en el 661** | |
| **≈ 668–686** | **675 ●** | **La app baja hasta los nombres** (`ver`, suave): pasan «Botones que tocaron · ↩ Allí estaré · 23» y «Por qué no les llegó» (real); llegan «Destinatarios (23)» y las filas **«Emmanuel Zuluaga Rojas · Leído · •••• 8588 · fecha · ↩ Allí estaré · abrió el enlace», «Liliana Lopera Rojas · Leído · … · ↩ Allí estaré», «Amparo Úsuga Quiroz»…** (real) | **quieta** | | `desliz` (acento 672) · **`confirmacion` (1,4) en el 688** | |
| **690–703** | ● | quieta | **Movimiento del compás 12:** G → **M `nombres`** (los nombres a 50 px; «Leído» y «Allí estaré» a 38 px) | | — | |
| **720** | **●●● golpe** | quieta (la lista real) | **Movimiento del compás 13:** M → **M⁻ `cierre`** (seis filas), 720–733 | **«Habla con tu iglesia, / sin perder a *nadie*»:** Habla 720 · con 722 · tu 724 · iglesia, 726 · sin 728 · perder 730 · a 732 · *nadie* 734. **La ceja sale 720–723** | — | **La ventana se hace a un lado:** escala 1 → 0,92 + x (§1.4), 724–738; halo 1,08 → 1 (720–810) |
| 735–836 | 735 … 825 | quieta | quieta | La frase 4, quieta 3,5 s (más de 0,5 s + 0,3 s × 8 palabras = 2,9 s) | **`subida`** 796–853 (golpe en el 840) | |
| **837–839** | | — | — | — | — | **Dip** al 40 %, 3 cuadros |
| **840** | **●●● el más fuerte** | — | — | — | La música 0,7 → 0,224 (852) → 0 (870) | **Corte a la firma:** 4:5 `cierre-clip`, 9:16 `cierre-corto`; `{"llamado":"prueba","fondo":"azul","idioma":"es"}` |
| 846 · 853 ↓ | | La K sube; las 7 barras de la corona desde 0,45 s (`back.out(2.2)`) | | «Kingdom» en 0,75 s; **«Prueba gratis 30 días»** en 0,95 s | **Campanas en el 851** | |
| **914** | | Último cuadro: la corona completa y el botón | | | Sin música desde el 870 | Fin |

### 2.2 Los siete planos

#### P1 · «Alguien nuevo escribe» — cuadros 0–119 (compases 1–2) · pulsos 0, 15, 30, 45, 60, 75, 90, 105

- **Grabación:**
  - tramo `cola`: la bandeja quieta 3 s, usada a 1×;
  - tramo `abrir`: el toque y la carga de la conversación; el corte cae en la espera entre el toque y la pantalla nueva.
- **Encuadre 4:5:**
  - G `cola` hasta el 45;
  - G⁺ `fila` desde el 59; ahí cae el match cut, y la burbuja de Mariana tiene que quedar dentro;
  - M `hilo-cabeza` desde el 103.
- **Encuadre 9:16:**
  - G muestra 345 px CSS: `cola` se centra en las vistas y las tres primeras filas (≈ 177–522; Mariana entra entera);
  - M muestra 247 px: `hilo-cabeza` se centra en la fila de «Tomar» y la burbuja (≈ 100–347).
- **Cámara:** quieta hasta el 45; 46–59 a G⁺; el match cut del 78 en el mismo encuadre; 90–103 a M. Nada más.
- **Texto:** la frase 1 por pulsos (la primera landing ya puesta en el cuadro 0); sale 117–121.
- **Sonido:** toque en el 76.
- **Transición:** el match cut sobre el toque del 75 (`aterrizaje-app` 78–88); el plano cierra con el toque del 120.
- **Válvula:** si en la caja real la burbuja de Mariana no cabe con su fila en un mismo G⁺, el encuadre del 59 se queda en G `cola` (la
  fila ya se lee a 31,6 px) y el match cut aterriza en G. El 90 hace el único acercamiento.

#### P2 · «Todo tu equipo, un solo número» — cuadros 120–179 (compás 3) · pulsos 120 (bajo), 135, 150, 165

- **Grabación:** tramo `tomar`: el toque, la respuesta del servidor y la conversación releída, con 2 s quietos. Si asoma la K del cargador,
  se corta.
- **Encuadre:** M `hilo-cabeza` (la píldora, «Tomar» y la nota caben); M `compositor` desde el 163. En 9:16, la nota puede quedar
  justo debajo del borde de M: lo que se lee en el 122 es la píldora «Atendiendo».
- **Cámara:** quieta en el toque; 150–163 a M `compositor`.
- **Texto:** la frase 2 entra 120–126 (la línea entera) y sale 177–181.
- **Sonido:** toque en el 121 (1,4) y aparicion en el 123.
- **Transición:** ninguna; cierra con el toque del 180.

#### P3 · «/horarios» — cuadros 180–359 (compases 4–6) · pulsos 180 (pico), 195, 240, 300, 315

- **Grabación:**
  - tramo `barra`: el toque en el compositor, «/» y la lista quieta 2 s;
  - tramo `horarios`: el toque y el compositor lleno, quieto 2 s;
  - tramo `enviar`: el toque y la respuesta en el hilo, quieta 3 s.

  Todo a 1×; las pausas sobrantes se recortan para que cada toque caiga en su pulso.
- **Encuadre:** M `compositor` (163–314), M `respuesta` (desde el 328). En 9:16, `compositor` se centra en la lista y el compositor
  (≈ 500–747): si la lista pasa de 247 px, se ven las tres primeras respuestas y «/horarios» queda dentro.
- **Cámara:** quieta mientras la lista sube (180), mientras el compositor crece (240) y mientras la respuesta aparece (300); 315–328 a M
  `respuesta`.
- **Texto:** la ceja entra 195–201; sin frase (la respuesta es el espectáculo).
- **Sonido:** toque en el 181 (1,4), aparicion en el 196, toque en el 241, aparicion en el 243, toque en el 301 (1,4) y confirmacion en
  el 303 (1,4).
- **Transición:** ninguna (todo cambia dentro de la app).
- **Si el orden de las respuestas es otro** (la búsqueda flexible con la consulta vacía las deja como vienen del servidor): da igual. La
  marca del 236 nace donde `pasos.json` dice que se tocó «/horarios».

#### P4 · «Y sabes quién leyó el aviso» — cuadros 360–599 (compases 7–10) · pulsos 360, 375, 390, 420, 450, 480, 540, 585

- **Grabación:**
  - tramo `volver`: el toque y la lista con «Cola 3», quieta 2 s;
  - tramo `campanas`: el toque y la lista de campañas, quieta 2 s;
  - tramo `bajar`: el desplazamiento suave hasta la invitación y 3,6 s quietos.

  Todo a 1×; el desplazamiento puede ir entre 0,8× y 1,5× para durar 480–495.
- **Encuadre:** M `respuesta` (el 375 entra en él), G `arriba` (403–449), G⁺ `campanas` (463–539), G⁺ `tarjeta` (desde el 553). En
  9:16, los mismos objetivos.
- **Cámara:** 390–403, 450–463 y 540–553, una vez por compás salvo el 9, que es la app bajando (la cámara muerta de quieta).
- **Texto:** la frase 3 entra 360–370, palabra a palabra, y sale 597–601.
- **Sonido:** toque en el 376 (sin marca), toque en el 421 y desliz en el 485.
- **Transición:** ninguna del montaje; dos cambios de pantalla de la app (375 y 420), cortados en sus esperas.

#### P5 · «115 leídos, 23 respondieron» — cuadros 600–719 (compases 11–12) · pulsos 600 (subida), 660 (golpe), 675, 690

- **Grabación:**
  - tramo `reporte`: el toque, la carga y los números quietos 2,4 s;
  - tramo `respondieron`: el toque, la lista filtrada, el desplazamiento suave a los nombres y 6 s quietos.

  A 1×; los cortes van en las esperas del servidor (si asoma la K del cargador en el filtro, se corta: §5).
- **Encuadre:** G `kpis` (613–689), M `nombres` (desde el 703). En 9:16, `kpis` muestra 345 px CSS: se centra en las filas 2 y 3
  (entregados · leídos · respondieron · clics); el Total queda arriba, fuera.
- **Cámara:** 600–613, quieta en el 660 y mientras la app baja (668–686), y 690–703.
- **Texto:** ninguno: las dos pruebas las da la app.
- **Sonido:** toque en el 601 (1,4), confirmacion en el 603, toque en el 661 (1,4), desliz en el 672 y confirmacion en el 688 (1,4).
- **Transición:** ninguna; cierra con la frase 4 del 720.
- **Válvula si 660–690 va atropellado:** el desplazamiento se adelanta y dura 662–680 a 1,5× (dentro del límite). Si aún no alcanza, el
  movimiento de cámara del 690 se queda en G y el 720 va directo a M⁻ `cierre`.

#### P6 · «Habla con tu iglesia, sin perder a nadie» — cuadros 720–839 (compases 13–14) · pulsos 720 (golpe), 735 … 825

- **Grabación:** el final del tramo `respondieron` (≥ 4 s quietos a 1×).
- **Encuadre:** M⁻ `cierre`, con la ventana a 0,92 y corrida (§1.4): «Destinatarios (23)» y seis filas con su nombre, su «Leído» y su
  «↩ Allí estaré»; el texto de 12 px queda en 28,6 px. En 9:16 la ventana se encoge desde arriba y termina en 1262.
- **Cámara:** 720–733 a M⁻; después, muerta de quieta. El halo se asienta 720–810.
- **Texto:** la frase 4 entra 720–734 (*nadie* en itálica dorada); la ceja sale 720–723; la frase se sostiene 3,5 s.
- **Sonido:** subida 796–853.
- **Transición:** dip 837–839 y corte duro al 840.

#### P7 · «La firma» — cuadros 840–914

- 4:5: `identidad/cierre-clip.html`; 9:16: `identidad/cierre-corto.html`. Variables `{"llamado":"prueba","fondo":"azul","idioma":"es"}`.
- Campanas en 28,38 (cuadro 851). La música: 0,7 → 0,224 (852) → 0 (870).
- El único gesto de marca del clip.

---

## 3. La grabación: la escena `tools/ayuda/escenas/clips/comunicaciones-alguien-nuevo.mjs`

Es una sola escena de **celular**: `movil: true`, 390×844 a 3× → **1170×2532**, 30 cps, sin el círculo del toque (`toque: false`). Se graba
con `capturar.mjs --modo video` sobre Kingdom Demo en español.

**La API de las capturas** tiene que estar encendida con Meta simulado, tal como pide
[docs/ayuda/capturas.md](../../../../KingdomApp/docs/ayuda/capturas.md) → «Entorno»:
- `COM_GRAPH_FAKE=1`;
- `COM_DESPERTAR_WORKER=0`;
- `COM_GRAPH_FAKE_PLANTILLAS=F:/dev/kingdom-local/ayuda_capturas_fake_plantillas.json`.

Sin ellas, la bandeja no envía.

```bash
cd F:/Proyectos/KingdomApp/tools/ayuda
node capturar.mjs clips/comunicaciones-alguien-nuevo --idioma es --modo video
# → salida/video/es/clips/comunicaciones-alguien-nuevo/grabacion.mp4 + pasos.json (inicio/fin, tramo, accion, toques[], teclas[], caja_video)
```

**Cuenta:** 101, el administrador **Andrés Felipe Restrepo Gómez**. Es la única cuenta de Kingdom Demo con Comunicaciones
(`_demo_capturas.php` no le da el módulo a ninguna otra) y la que atiende la bandeja en la semilla (`$YO = 101`).

**Datos ficticios**, todos de `tools/ayuda/semillas/comunicaciones.php`:
- **Mariana Ospina:** `wa_id 575550123987`, sin ficha. Escribió por el webhook simulado y quedó en la cola.
- **La respuesta rápida «/horarios»** del equipo.
- **La campaña** «Invitación: culto de jóvenes del domingo», que salió a la red Timoteo y tiene sus estados de Meta simulados.

En la escena no se escribe nada a mano salvo la tecla «/».

**Sin `COMO_IGLESIA`** (el `sql` que usan las escenas de la ayuda de Comunicaciones): el clip no muestra cupo, créditos ni precios
(decisión 215). Con la sede en demo, nada se cobra y nada de lo que se ve cambia.

**Lo que la semilla garantiza**, verificado el 2026-10-30 en el informe de la semilla de hoy
(`F:/dev/kingdom-local/ayuda_capturas_logs/comunicaciones_es.json`) y con consultas a `ayuda_capturas_db`:
- **La línea:** «Línea principal», conectada.
- **La cola:** 4 conversaciones. La de Mariana (296) tiene un solo mensaje entrante y ninguno saliente, y sigue en `cola`.
- **La respuesta rápida:** `horarios` es del equipo (`id_usuario NULL`) y está activa.
- **La campaña completada** (la 1, «Completada»): 139 destinatarios, de los cuales 115 leídos, 22 entregados sin leer y 2 fallidos; 23
  con `respondio_at`; el primero que respondió es Emmanuel Zuluaga Rojas.

**Lo que no garantiza:** que la ventana de 24 h de Mariana siga abierta. El mensaje tiene la hora de la semilla. `capturar.mjs` vuelve a
sembrar si el volcado no es de hoy, y la `ref` `mariana` exige menos de 20 horas.

**Selectores**, verificados en `frontend-v2/src/app/pages/comunicaciones/`:
- **`bandeja.page.ts`:** `#bandeja-lista .item[data-id]`.
- **`bandeja-hilo.component.ts`:**
  - `#btn-tomar`, `#hilo-estado[data-estado]`, `#compositor`;
  - `#respuestas-sugeridas button.sug[data-atajo]`, `#btn-enviar`, `#btn-hilo-volver`;
  - `.hilo .msg.sale`.
- **`comunicaciones-cabecera.component.ts`:** `#tab-com-campanas`.
- **`campanas.page.ts`:** `#camp-lista li.tarjeta[data-id]` y `#camp-abrir-{id}`.
- **`campana-reporte.component.ts`:** `#camp-reporte .kpi[data-k="respondieron"]`, `.cab-lista h3` y `#camp-destinatarios li`.

```js
// Grabación para el clip del sitio público «Alguien nuevo escribe» (LegacyHyperframes/videos/kingdomapp/clip-sitio-comunicaciones/SPEC.md §3).
// NO es una escena de un artículo de la ayuda: no se publica ni entra en la frescura. Una sola escena de CELULAR (390×844 a 3x = 1170×2532,
// 30 cps) grabada SIN el círculo del toque (`toque: false`): el montaje dibuja el suyo sobre toques[] y las cajas de pasos.json.
//   node capturar.mjs clips/comunicaciones-alguien-nuevo --idioma es --modo video
//   → salida/video/es/clips/comunicaciones-alguien-nuevo/grabacion.mp4 + pasos.json
// Tramos: cola · abrir · tomar · barra · horarios · enviar · volver · campanas · bajar · reporte · respondieron. Todo con la cuenta 101 (el
// administrador, la única de Kingdom Demo con Comunicaciones) y con la API de las capturas con Meta SIMULADO (COM_GRAPH_FAKE=1,
// COM_DESPERTAR_WORKER=0, COM_GRAPH_FAKE_PLANTILLAS: docs/ayuda/capturas.md → «Entorno»).
// Datos ficticios de semillas/comunicaciones.php: Mariana Ospina (575550123987, sin ficha) en la cola; la respuesta rápida «/horarios» del
// equipo; la campaña completada «Invitación: culto de jóvenes del domingo» con sus entregados, leídos y «Allí estaré». Sin COMO_IGLESIA: el
// clip no muestra cupo, créditos ni precios (decisión 215).
import { CONV, REF } from '../../lib/escenas-comunicaciones.mjs';

const MARIANA = '#bandeja-lista .item[data-id="{@mariana}"]';
const HORARIOS = '#respuestas-sugeridas button.sug[data-atajo="horarios"]';
// La respuesta enviada: el horario dice «8:00» en los dos idiomas (es «8:00 a. m.», en «8:00 a.m.»); Mariana no lo escribió.
const RESPUESTA = '.hilo .msg.sale:has-text("8:00")';
const TARJETA = '#camp-lista li.tarjeta[data-id="{@completada}"]';
const RESPONDIERON = '#camp-reporte .kpi[data-k="respondieron"]';

export default {
  articulo: 'clips/comunicaciones-alguien-nuevo',
  movil: true,
  toque: false,
  pantallas: [
    'frontend-v2/src/app/pages/comunicaciones/bandeja.page.ts',
    'frontend-v2/src/app/pages/comunicaciones/bandeja-hilo.component.ts',
    'frontend-v2/src/app/pages/comunicaciones/comunicaciones-cabecera.component.ts',
    'frontend-v2/src/app/pages/comunicaciones/campanas.page.ts',
    'frontend-v2/src/app/pages/comunicaciones/campana.page.ts',
    'frontend-v2/src/app/pages/comunicaciones/campana-reporte.component.ts',
  ],
  refs: {
    // Mariana, en la cola y con la ventana de 24 h abierta durante toda la grabación (escribió hace menos de 20 h). Si no, la escena se niega:
    // el volcado no es de hoy (capturar.mjs lo vuelve a sembrar) o alguien la tomó.
    mariana: `${CONV.sinFicha} AND estado = 'cola' AND ultimo_entrante_at > NOW() - INTERVAL 20 HOUR`,
    // La respuesta rápida del equipo que llena el compositor (cuadro 240 del clip).
    horarios: "SELECT id FROM com_respuestas_rapidas WHERE atajo = 'horarios' AND activo = 1 AND id_usuario IS NULL LIMIT 1",
    completada: REF.campanaCompletada,
    // El reporte se filtra por «respondieron» (cuadro 660): al menos cinco nombres con «Allí estaré», o la escena se niega (plan B, abajo).
    respondieron: `SELECT IF(COUNT(*) >= 5, COUNT(*), NULL) FROM com_campana_destinatarios
                    WHERE id_campana = (${REF.campanaCompletada}) AND respondio_at IS NOT NULL`,
  },
  pasos: [
    // 1. La cola de la bandeja, quieta (cuadro 0 del clip). La vista inicial es «Cola» porque tiene conversaciones.
    { tramo: 'cola', como: 101, ir: '/servir/comunicaciones/bandeja', espera: MARIANA, pausa: 3000 },
    // 2. La fila de Mariana (el toque del 75): su mensaje, «En la cola» y «Tomar».
    { tramo: 'abrir', clic: MARIANA, espera: '#btn-tomar', pausa: 1800 },
    // 3. «Tomar» (el toque del 120, el bajo): «Atendiendo» y la nota «… tomó la conversación».
    { tramo: 'tomar', clic: '#btn-tomar', espera: '#hilo-estado[data-estado="atencion"]', pausa: 2400 },
    // 4. «/» en el compositor (el toque del 180, el pico): suben las respuestas rápidas.
    { tramo: 'barra', escribir: { en: '#compositor', texto: '/' }, espera: HORARIOS, pausa: 2400 },
    // 5. «/horarios» (el toque del 240): la lista se va y el compositor se llena con el horario.
    { tramo: 'horarios', clic: HORARIOS, oculto: '#respuestas-sugeridas', pausa: 2400 },
    // 6. Enviar (el toque del 300): la respuesta queda en el hilo con su palomita (enviado; Meta simulado no manda «leído»).
    { tramo: 'enviar', clic: '#btn-enviar', espera: RESPUESTA, pausa: 2500 },
    { ver: RESPUESTA, pausa: 300 },                                    // solo para la caja de la respuesta (objetivo del 315)
    // 7. Volver (el toque del 375, fuera de encuadre): la lista con «Cola 3».
    { tramo: 'volver', clic: '#btn-hilo-volver', espera: '#bandeja-lista .item', pausa: 1800 },
    // 8. «Campañas» (el toque del 420): la lista de campañas, la más nueva primero.
    { tramo: 'campanas', clic: '#tab-com-campanas', espera: TARJETA, pausa: 2400 },
    // 9. La lista baja hasta la invitación, que es la más vieja (el desliz del 480).
    { tramo: 'bajar', ver: TARJETA, pausa: 3600 },
    // 10. La invitación (el toque del 600, la segunda subida): su reporte con los números.
    { tramo: 'reporte', clic: '#camp-abrir-{@completada}', espera: RESPONDIERON, pausa: 2400 },
    // 11. «respondieron» (el toque del 660, el golpe): la lista se filtra (el título dice «({@respondieron})»); la app baja a los nombres.
    { tramo: 'respondieron', clic: RESPONDIERON, espera: '#camp-reporte .cab-lista h3:has-text("({@respondieron})")', pausa: 400 },
    { ver: '#camp-destinatarios li >> nth=2', pausa: 6000 },          // los nombres quietos para el final (672–839)
  ],
};
```

**Notas sobre la escena:**

- **`ver`:** desplaza suave, con `block: 'center'`. En el celular la barra de la app es fija, así que no se usa `bloque: 'start'`
  (taparía el elemento).
  - El `ver` sobre la respuesta no mueve nada (el hilo es corto); está para que `pasos.json` traiga su caja.
  - El `ver` sobre la tercera fila de destinatarios deja arriba «Destinatarios (23)» y las primeras filas.
  - Las cajas de la cámara (§1.5) se toman de `caja` / `caja_video` del paso que las nombra.
- **Pausas:** la `pausa` de cada paso **reemplaza** los 900 ms que la herramienta espera por defecto tras cada acción. Cada una se midió
  contra lo que el clip necesita entre dos toques, más 0,4–0,5 s de margen. Todo lo que sobra se corta en el montaje; nada se puede
  alargar.
- **`escribir`:** toca el campo (es un toque real, con su caja) y escribe a 70 ms por tecla; aquí es una sola tecla, «/».
- **Tiempos:** ≈ 3 + 2,2 + 2,8 + 2,9 + 2,8 + 3 + 1,2 + 2,3 + 3,2 + 4,5 + 3,2 + 1 + 6,9 ≈ **39 s de grabación** para 28 s de clip. No hace
  falta `consolaEsperada`.
- **Plan B de «respondieron»** (la `ref` da NULL porque respondieron menos de cinco):
  - se toca «leídos» (`.kpi[data-k="leidos"]`) en lugar de «respondieron»;
  - la `espera` pasa a «Destinatarios (N)» con el número de leídos (una `ref` igual sobre `estado = 'leido'`);
  - las filas muestran «Leído» y algunas «Allí estaré»;
  - la frase 3 no cambia.
- **Si la ventana de Mariana está cerrada** (la `ref` `mariana` da NULL): no hay plan B en el guion. Se vuelve a sembrar el volcado del
  día (`capturar.mjs` lo hace solo si no es de hoy). Responder con una plantilla cambiaría la historia.
- **El idioma inglés (después):** la misma escena con `--idioma en` graba la interfaz en inglés.
  - «Sin ficha» → «No profile», «Allí estaré» → «I'll be there».
  - El atajo sigue siendo `horarios` y el selector de la respuesta («8:00») vale igual.
  - Las frases se traducen y los saltos se vuelven a fijar; la firma lleva `idioma`.

---

## 4. Lo que se revisa en la vista previa

**Cuadros a mirar** en las dos composiciones:

```
npx hyperframes snapshot --at 0,1.5,2.0,2.5,2.6,3.0,3.5,4.0,4.1,5.5,6.0,6.1,6.5,8.0,8.1,9.5,10.0,10.1,11.0,12.0,12.5,13.5,14.0,15.5,16.5,18.5,19.9,20.0,20.2,21.0,22.0,22.6,23.4,24.0,24.5,27.9,28.0,28.4,30.4
```

Además, tres tramos cuadro a cuadro:
- el match cut de la conversación: `snapshot --range 2.4,3.0 --frames 18`;
- la lista de respuestas: `--range 5.9,6.3 --frames 12`;
- el filtro y la bajada a los nombres: `--range 21.9,23.0 --frames 33`.

1. **Cuadro 0 (la miniatura):**
   - la bandeja con «Cola 4» y la fila de Mariana con «Sin ficha» y su globo;
   - «Alguien» en Fraunces, ya puesta;
   - «Datos de ejemplo» abajo a la izquierda.

   Nunca negro, nunca la marca. En 9:16, nada por encima de 168 ni por debajo de 1330, salvo el halo y los puntos.
2. **Cuadro 45:** las cuatro landings de la frase 1, quietas. **Cuadro 59:** G⁺ con la fila de Mariana entera.
3. **75–88:** el toque en la fila y la conversación que entra 1,03 → 1,00, sin un cuadro de pantalla en blanco ni de «Cargando…» (si la
   app lo muestra, se corta).
   - **103:** M con la burbuja entera a 44 px, «En la cola» y «Tomar».
   - **105–119:** la marca quieta sobre «Tomar».
4. **120–126:**
   - el toque exactamente con el bajo;
   - en el 122, «Atendiendo» y la nota «… tomó la conversación»;
   - la frase 2 entera en el 126.

   Ningún cuadro con la K del cargador.
5. **150–163:** la cámara baja al compositor con la app quieta.
6. **180–195:** la lista de respuestas sube dentro del encuadre con el toque, sin cortes. La ceja cae en el 195 y no antes, y no tapa nada
   de la ventana.
7. **240–243:** la lista se va y el compositor crece con el horario completo, a ≥ 44 px. La cámara no se mueve.
8. **300–303:** la respuesta aparece en el hilo con «Andrés Felipe Restrepo Gómez» (real) y **una palomita gris**, nunca azul.
   - **328:** M con la pregunta, la nota y la respuesta.
   - **330–359:** quieto (la única quietud permitida).
9. **360–370:** la frase 3 palabra a palabra. **375:** la lista con **«Cola 3»** legible (≥ 28 px) en el mismo encuadre, sin marca de
   toque dibujada.
10. **420:** las campañas en G, con la pestaña «Campañas» ya con su texto.
    - **480–495:** la lista baja y la cámara no se mueve.
    - **553:** G⁺ sobre «Invitación: culto de jóvenes del domingo · Completada», con sus números a ≥ 28 px.
11. **600–613:** el toque con la segunda subida y el reporte que aparece en el 603. En el 613, G con «115 leídos» y «23 respondieron» a
    50 px.
12. **660–690:**
    - el toque en «respondieron» en el golpe, con el contorno visible;
    - la app baja (la cámara quieta) a «Destinatarios (23)»;
    - **703:** M con «Emmanuel Zuluaga Rojas · Leído · ↩ Allí estaré» (real): los nombres a ≥ 44 px, «Allí estaré» a ≥ 28 px.

    Ningún cuadro de la lista sin filtrar (139) después del 668.
13. **720–738:**
    - la frase 4 aterrizada en el 734, con *nadie* dorada;
    - la ceja fuera;
    - la ventana a 0,92 y corrida;
    - M⁻ con seis filas y el texto de 12 px a ≥ 28 px.

    **738–836:** nada se mueve salvo el halo. **837–839:** el dip. **840:** el primer cuadro de la firma, sin noche vacía entre medias.
14. **Sonido (medido, no oído):**
    - cada `toque` un cuadro después de su imagen;
    - las tres `confirmacion` en el 303, el 603 y el 688;
    - las campanas en el 851;
    - la música a −10 dB en el 852 y a 0 en el 870;
    - −16 LUFS y pico ≤ −1 dBTP;
    - ningún tramo con dos sonidos de acción encimados, salvo 121 + 123, 241 + 243, 301 + 303, 601 + 603 y 672 + 688.
15. **Textos:**
    - ninguna palabra que no esté en la app o en las cuatro frases;
    - ningún texto que el plano dice que se lee por debajo de 28 px;
    - las frases en 2 líneas (3 en 9:16 la primera y la cuarta);
    - `npx hyperframes check` en 0 errores (contraste AA incluido);
    - «Datos de ejemplo» desde el cuadro 0.
16. **Lo que nunca aparece:** créditos, saldo, cupo, precios, el costo en Meta, el logo o el verde de WhatsApp, un número que no sea `+57
    555…`.
17. **La historia sin sonido** se entiende con la pantalla en silencio, como se verá en el sitio: alguien nuevo escribe → lo toma el
    equipo → «/horarios» → la respuesta sale → la invitación del domingo → 115 la leyeron → los nombres que dijeron «Allí estaré» → habla
    con tu iglesia, sin perder a nadie → Kingdom.

---

## 5. Riesgos y lo que se decide al grabar

- **La ventana de 24 horas de Mariana.** Es el único dato que depende de la hora. La `ref` `mariana` exige menos de 20 horas desde su
  mensaje. Si falla, se vuelve a sembrar el volcado del día: no hay plan B que no cambie la historia.
- **El cargador de la app** (`loading.wrap`, la K animada a los 150 ms) puede asomarse en dos momentos:
  - en «Tomar»;
  - en el filtro del reporte (los destinatarios se piden de nuevo).

  Con la API local no debería asomar. Si asoma, se corta en la espera: los cortes del 120 y del 660 ya caen ahí.
- **Dónde quedan las cosas en el celular.** Las cajas de §1.5 son estimaciones; los objetivos reales salen de `pasos.json` y el REVIEW
  los anota. Lo incierto:
  - la cabecera del hilo que se parte en dos renglones;
  - el alto de la lista de respuestas (hasta 13 rem, con desplazamiento propio);
  - dónde queda la tarjeta de la invitación después de bajar (es la última de la página y el desplazamiento se detiene en el fondo);
  - el alto de los KPI.

  La regla que no cambia: la cámara sujeta a la grabación, un movimiento por compás, nunca a la vez que la app.
- **El encuadre del match cut (59–78):** tiene que contener la fila de Mariana antes y su burbuja después. La válvula de P1 lo resuelve
  con G si no caben en G⁺.
- **«Cola 3»:** la lista se vuelve a pedir al volver (`cerrarHilo` → `cargarLista`). Si la grabación muestra un instante con «Cola 4», el
  corte cae después.
- **El toque de volver (375) no se dibuja:** la flecha queda fuera del encuadre `respuesta`, y llevar la cámara a la cabecera en ese
  compás sacaría la respuesta del cuadro. Es el mismo trato que el «Listo» de Membresía (REVIEW §4.5).
- **El contorno de «respondieron» es fino** (2 px CSS = 4,5 px en el video). Si en la vista previa no se lee como un toque, la marca, el
  sonido y la lista que cambia en el 668 lo explican. No se dibuja ningún resaltado propio (BANNED 25).
- **Los textos y las cifras reales** cambian con la semilla y ninguna frase depende de ellos:
  - las horas, las fechas, los nombres de la cola y de los destinatarios;
  - «Andrés Felipe Restrepo Gómez»;
  - 139 · 137 · 115 · 23 · 39 · 2.

  La semilla es la misma cada día (el mismo azar), así que deberían repetirse.
- **Densidad de 0–6 s:** cinco sonidos, tres toques y dos movimientos de cámara (como en Eventos). Si en la vista previa va atropellado,
  el movimiento 46–59 se quita (la válvula de P1).
- **Densidad de 600–703:** dos toques, una carga, un desplazamiento y un movimiento de cámara en 3,4 s. La válvula de P5 está lista.
- **Nada nuevo de herramienta ni de kit:** `cierre-clip`, `.k-ventana`, `.k-feed-*`, el modo video de celular con `toque: false` y
  `pasos.json` con `toques[]` ya existen. Lo único nuevo es el archivo de la escena, que se copia tal cual de §3.
