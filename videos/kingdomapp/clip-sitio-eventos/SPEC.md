# SPEC · Clip del sitio: Eventos — «Terminó la reunión»

2026-10-30 · Contrato de construcción de la historia elegida en [STORY.md](STORY.md) (el dueño ya no revisa guiones: se eligió aquí). Cada
adjetivo es un número, los valores por defecto están prohibidos con nombre y los planos van cuadro por cuadro sobre la grilla real de la
pista. Se construye desde aquí, se revisa contra esto y se cambia aquí cuando la vista previa cambie la película. Hereda el sistema de
[Membresía](../clip-sitio-membresia/SPEC.md) (mismo reloj, mismas letras, misma ventana, mismas curvas, misma firma) y las lecciones de su
[REVIEW](../clip-sitio-membresia/REVIEW.md) (ya aplicadas: niveles del kit, látigo en una tira, entradas un cuadro antes del pulso,
«Datos de ejemplo» a 31 px abajo a la izquierda).

```text
GOAL:    Un pastor que no conoce Kingdom termina pensando «terminó la reunión y antes de llegar a la casa ya estaba reportada, con su número»
         y toca «Prueba gratis 30 días».
OUTPUT:  HyperFrames · dos composiciones de la misma línea de tiempo: 1080×1350 (4:5, sitio y feed) y 1080×1920 (9:16, Reels e historias) · 30 fps.
TIME:    30,5 s = 915 cuadros: cuerpo 0–28,0 (cuadros 0–839) + firma 28,0–30,5 (840–914). 120 BPM = 15 cuadros por pulso (grilla real en §0).
LOOK:    noche del sitio (#060D1F) con el halo y la retícula de puntos del kit; tinta #EAF0FF; un solo acento, el dorado #E8B95A, en tres
         lugares y no más (la ceja «EVENTOS», la palabra «reunión» y el botón de la firma). Fraunces 560 / −0,02 em para las frases; Inter
         para la ceja y «Datos de ejemplo». El medio: la app REAL de Kingdom Demo grabada en celular, nítida (1170 px de ancho), dentro de
         una ventana con radio 28, anillo de 1 px y sombra 0 40 80 −24 al 65 %; nunca un teléfono dibujado.
OBJECTS: la ventana (el celular de Jorge, un solo mundo); el punto de toque de la grabación; las cuatro frases; la ceja; la píldora «Datos
         de ejemplo»; la corona del cierre. Nada más existe en el cuadro.
MOTION:  curvas por papel (§1.6); un movimiento de cámara por compás (14 cuadros, power2.inOut), quieto después y nunca mientras la app
         escribe o se desplaza; cada corte y cada entrada en un pulso; cada cambio grande en un golpe (120 · 180 · 600 · 660 · 720 · 840).
SHOTS:   siete planos (§2).
BANNED:  §1.8.
QA:      §4.
```

---

## 0. El reloj: la grilla real de la pista

La música es «Product Launch» (The_Mountain) del 14,05 al 42,05 s; t = 0 del clip ↔ 14,05 de la pista. Los pulsos vienen de
`_identidad/musica/product-launch-the-mountain.pulsos.json` (el mismo mapa que usó Membresía) restándoles 14,05 y redondeando a 30 fps:
**todos caen en el múltiplo de 15 cuadros salvo el 9,455 s, que cae en el cuadro 284** (nada ocurre ahí). Cada pulso se calcula desde su
índice, nunca sumando 15 repetidamente.

| Compás | Cuadros | Pulsos (cuadro · fuerza) | Intensidad | Lo que le toca a este clip |
|---|---|---|---|---|
| 1 | 0–59 | 0 ·0,69 · 15 ·0,64 · 30 ·0,49 · 45 ·0,48 | 0,57 | Servir con «Reuniones por reportar»; la frase 1, una landing por pulso; la cámara a la fila |
| 2 | 60–119 | 60 ·0,58 · 75 ·0,55 · 90 ·0,57 · 105 ·0,61 | 0,58 | **75:** toque «Reportar» → el reporte entra; 90 la cámara abre a la lista; 105 el dedo se posa |
| 3 | 120–179 | **120 ·0,93** (entra el bajo) · 135 · 150 · 165 | 0,66 | **120:** «Igual que la última vez»: la lista se marca sola. Frase 2. 150 la app baja al final de la lista |
| 4 | 180–239 | **180 ·0,87** (pico) · 195 ·0,83 · 210 · 225 | **0,77** | **180:** iris a la hoja «Persona nueva»; 195 la ceja «EVENTOS» |
| 5 | 240–299 | **240 ·0,92** · 255 ·0,77 · 270 · 284 | 0,70 | «Ximena» (240) y «Hoyos Vélez» (270) |
| 6 | 300–359 | 300 ·0,77 · 315 ·0,75 · 330 · 345 | 0,68 | El teléfono (315–341); «Mujer» (345); la cámara abre a la hoja entera |
| 7 | 360–419 | 360 ·0,76 · 375 ·0,64 · 390 · 405 | 0,59 | Frase 3; **375:** «Agregar»: la fila «Ximena Hoyos Vélez · Nueva» |
| 8 | 420–479 | 420 ·0,75 · 435 ·0,61 · 450 · 465 | 0,59 | 450: «+» visitantes → «Total: 6 personas» |
| 9 | 480–539 | 480 ·0,67 · 495 ·0,67 · 510 · 525 | 0,59 | 480: «+» → «Total: 7 personas»; 510 acercamiento al total |
| 10 | 540–599 | 540 ·0,63 · 555 · 570 ·0,61 · 585 ·0,68 | 0,62 | La cámara a los botones; el dedo llega a «Guardar asistencia» |
| 11 | 600–659 | **600 ·0,93** (segunda subida) · 615 ·0,69 · 630 · 645 | 0,66 | **600:** «Guardar asistencia»: la barra 15 → 66 %, el paso ② «Reporte». «Muy bien» (615), «El perdón» (630–651). Frase 3 sale |
| 12 | 660–719 | **660 ·0,90** · 675 ·0,89 · 690 ·0,76 · 705 ·0,68 | **0,81** | **660:** «Enviar reporte» → «¡Listo! … 7 personas.» (la prueba más fuerte); 690 el punch a la tarjeta |
| 13 | 720–779 | **720 ·0,96** · 735 ·0,77 · 750 · 765 | 0,73 | Frase 4; la ceja se va; la ventana se hace a un lado |
| 14 | 780–839 | 780 ·0,88 · 795 ·0,74 · 810 · 825 | 0,71 | Quieto; la subida; el dip |
| — | **840** ·1,00 | el golpe más fuerte de la pista | — | **La firma.** La música se va debajo de las campanas |

Las dos pruebas del clip caen en los dos golpes reales de la segunda subida: «Guardar asistencia» en el 600 (0,93) y «Enviar reporte» en el
660 (el compás más fuerte del cuerpo). La frase final, en el 720 (0,96).

---

## 1. Los números del estilo

### 1.1 Paleta (tokens de `identidad/kit.css`; nada fuera de esta lista)

| Papel | Token | Valor | Dónde puede aparecer |
|---|---|---|---|
| Fondo | `--k-noche` | `#060D1F` | A sangre, todo el cuerpo |
| Halo | `.k-halo` | azul `rgba(53,118,218,.45)` arriba a la derecha + dorado `rgba(217,162,52,.22)` abajo a la izquierda | Fondo, bajo todo; se asienta 1,08 → 1 en 0, 180 y 720 |
| Puntos | `.k-puntos` | `rgba(169,190,235,.35)`, 2 px cada 42 px, desvanecidos a la izquierda | Fondo; **nunca se mueven** |
| Tinta | `--k-noche-tinta` | `#EAF0FF` | Las frases |
| Acento | `--k-noche-dorado` | `#E8B95A` | Solo: la ceja «EVENTOS», la palabra *reunión*, el botón de la firma |
| Anillo | `--k-noche-linea` | `rgba(234,240,255,.12)` | El borde de la ventana |
| Fondo de la app | `--k-app-fondo` | `#FAF9FD` | Detrás de la grabación (nunca se ve) |
| Azul de marca | `--k-azul` | `#3576DA` | **Solo en la firma** (la baldosa) |
| Placa | `.k-datos-ejemplo` | `rgba(6,13,31,.72)` | La píldora «Datos de ejemplo» |
| Dip | — | `rgba(6,13,31,.40)` | Los 3 cuadros antes de la firma, solo sobre la ventana |

Los colores de la app (el ámbar de las filas marcadas, el verde de «Reportada», el azul `#015BBE` de los botones y de la barra de avance, el
rojo de «2 vencidas») viven dentro de la grabación y no se tocan. `--k-noche-tinta-2` no se usa.

### 1.2 Tipografía

| Pieza | Clase (kit v1.1) | Familia · peso | 4:5 | 9:16 | Interlineado · tracking | Reglas |
|---|---|---|---|---|---|---|
| Frase | `.k-feed-frase` (`.k-titular` + `.k-vertical` en 9:16) | Fraunces 560; `<em>` itálica 500 dorada | **80 px** | **104 px** | 1,04 · −0,02 em | Máx. **2 líneas** en 4:5 (3 en 9:16), saltos fijados a mano. Izquierda. Sin sombra |
| Ceja | `.k-feed-ceja` (`.k-ceja`) | Inter 700, MAYÚSCULAS | **30 px** | **34 px** | 1 · +0,10 em | Una palabra: «EVENTOS» |
| Datos de ejemplo | `.k-datos-ejemplo .k-feed-datos` | Inter 600 | **31 px**, píldora de 56 px de alto | igual | 1 · 0 | Blanca sobre la placa; **abajo a la izquierda de la ventana** (pedido del dueño, 2026-10-30), a 24 px del borde visible; 31 y no 28 para que con la ventana a 0,92 siga en ≥ 28 |
| Texto de la app | (grabación) | Inter de la app, 14 px CSS el cuerpo, 22 px los títulos | ≥ **31,6 px** | ≥ **34,5 px** | — | Nunca por debajo de 28 px en ningún encuadre (§1.5) |

Saltos de línea fijados (4:5, ≈ 23 caracteres por línea a 80 px en 888 px):
«Terminó la reunión. / ¿Quién vino?» · «Los de siempre, / en un toque.» · «Y queda registrada / en la iglesia» · «Cada *reunión* cuenta, /
y cuenta bien». En 9:16 (≈ 19 por línea a 104 px) la frase 4 va en tres: «Cada *reunión* / cuenta, / y cuenta bien»; las demás igual.

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

Variables de `index.html` (como en Membresía): 4:5 `--f-k: 0.752137`, `--f-grab-alto: 1904.41px`; 9:16 `--f-k: 0.820513`,
`--f-grab-alto: 2077.54px`, `--f-ventana-hvis: 850px`. Sin `--f-latigo` ni `#m2` (un solo mundo): la tira tiene un solo `.mundo` con su
envoltorio `#m1in` para el aterrizaje del 78.

### 1.5 La cámara dentro de la ventana: escalas

Grabación a 3× (390×844 px CSS → **1170×2532 px**). **ppc** = píxeles del cuadro por píxel CSS del celular.

| Nivel | Qué se ve | 4:5: ppc (escala del video) · visibles en px CSS | 9:16: ppc (escala) · visibles | Texto de la app 14 px → |
|---|---|---|---|---|
| **G** general | todo el ancho del celular | **2,256** (0,752) · 390 × 439 | **2,462** (0,821) · 390 × 345 | 31,6 px · 34,5 px |
| **G⁺** | una tarjeta con sus márgenes | 2,436 (0,812) · 361 × 406 | 2,659 (0,886) · 361 × 320 | 34 px · 37 px |
| **M** medio | una zona de la tarjeta, la hoja o el diálogo | **3,158** (1,053) · 279 × 313 | **3,446** (1,149) · 279 × 247 | 44 px · 48 px |
| **C** cerrado | una línea | **4,061** (1,354) · 217 × 244 | **4,431** (1,477) · 217 × 192 | 57 px · 62 px |

G = ×1,00 · G⁺ = ×1,08 · M = ×1,40 · C = ×1,80 sobre el general. La cámara es `scale` + `x`/`y` sobre `#cam` dentro de la ventana, sujeta a
los bordes de la grabación (función `enc()` de Membresía); el `<video>` nunca se transforma ni se busca. El objetivo de cada movimiento es
una **caja de `pasos.json`** (px CSS del viewport 390×844). Las cajas de abajo son estimaciones medidas sobre las capturas publicadas de la
ayuda (`eventos/reportar-una-reunion/01-tarjeta`, `02-asistencia`, `06-listo`); **las reales salen de la grabación** y se anotan en el REVIEW.

| Objetivo | Nivel | Centro estimado (x, y CSS) | Lo que debe quedar dentro |
|---|---|---|---|
| `servir` | G | (195, 219) → CSS 0–439 | barra «Kingdom Demo», «Servir en Iglesia Kingdom Demo 1», «Hola, Jorge Gallego Gil», la tarjeta «Reuniones por reportar» con sus dos primeras filas enteras |
| `fila` | M | (195, 290) → 133–446 | «Hola, Jorge…», la cabecera de la tarjeta y la fila «Casa de Paz Laureles 1 · Mié, 28 de oct · 2 vencidas · Reportar» a 44 px |
| `reporte-cabeza` (el mismo encuadre `fila`, pantalla nueva) | M | (195, 290) → 133–446 | el título del evento, «Pendiente», los atajos de fecha, ① ② ✓ con su barra y «0 marcadas · Igual que la última vez» |
| `lista` | G | (195, 624) → 405–844 (tope de abajo) | «N marcadas · Igual que la última vez», «Buscar a alguien más» y las cuatro casillas con «Vino 4 de 4» |
| `final-lista` | G | igual que `lista`; la app ya desplazada | las últimas casillas, «Persona nueva», «Visitantes», «Total: 4 personas», «No hubo reunión · Guardar asistencia» |
| `hoja-alta` | M | (195, 440) → 283–596 | «Persona nueva», Nombres, Apellidos, Indicativo + Teléfono, Mujer / Hombre |
| `hoja-baja` | M | (195, 600) → 443–756 | Teléfono, Mujer / Hombre, «Es un niño o una niña (sin teléfono)», Cancelar / Agregar |
| `hoja` | G⁺ | (195, 540) → 337–743 | la hoja entera, de Nombres a «Agregar» |
| `nueva-fila` | M | (195, 480) → 323–636 | la fila «Ximena Hoyos Vélez · Nueva», «Persona nueva», «Visitantes», «Total» |
| `total` | C | (110, 600) → 478–722 | la línea «Total: 7 personas» (y el contador de visitantes) |
| `botones` | M | (195, 640) → 483–796 | «Total: 7 personas» y los botones «No hubo reunión · Guardar asistencia» |
| `formulario` | G | (195, 450) → 230–669 | ① ② ✓ con la barra al 66 %, «Reporte de la casa de paz», «¿Cómo estuvo la reunión?», Muy bien / Bien / Difícil, «Tema de la palabra» |
| `listo` | G | (195, 449) → 229–668 | «Reportada», los atajos, los tres pasos hechos, la barra al 100 %, la tarjeta «¡Listo!» completa con sus dos botones |
| `listo-tarjeta` | M | (195, 500) → 343–656 | el ícono, «¡Listo!», «Casa de Paz Laureles 1, miércoles, 28 de octubre: 7 personas.» y «Volver a la lista» |
| `cierre` | G⁺ | (195, 418) → 215–621 | «Reportada», los pasos hechos, la barra, el ícono, «¡Listo!» y la frase con el total (con la ventana a 0,92: cuerpo ≥ 31 px) |

### 1.6 Curvas y duraciones (cada tween lleva su curva por nombre)

| Papel | Curva | Cuadros | Detalle |
|---|---|---|---|
| `entrada-palabra` | `power4.out` | 4 | `filter: blur(6px) → 0` + opacidad; **sin desplazamiento**; arranca un cuadro antes del pulso (el primer cuadro visible es el pulso). Palabras a 2 cuadros, salvo la frase 1 (una landing por pulso) |
| `entrada-linea` | `power4.out` | 6 | la línea entera, blur 8 → 0 (frase 2 y ceja) |
| `salida-texto` | `power3.in` | 4–5 | blur 0 → 8 + opacidad, la línea entera, 2–3 cuadros antes del pulso («blur swap») |
| `camara` | `power2.inOut` | **14** | un movimiento por compás; quieta después; **nunca mientras la app escribe o se desplaza** |
| `punch` | `power2.inOut` | **9** | solo el del cuadro 690 |
| `aterrizaje-app` | `power3.out` | 10 | el match cut del 78: la pantalla nueva (el reporte) entra a escala **1,03 → 1,00** en `#m1in`, origen en el centro de lo visible de la ventana. Es la única vez: las demás pantallas cambian dentro de la app sin ayuda |
| `iris` | `power2.out` | 5 | `clip-path: circle(0 at X Y) → circle(1900px at X Y)`, X Y = el centro de «Persona nueva» (caja de `pasos.json`) en px de la grabación ajustada; debajo, un still del cuadro 179 |
| `dedo-espera` | `power2.out` | 4 | la marca de toque aparece y **se queda quieta** hasta el toque: 105 → 120 (una sola vez, la del bajo: el dedo se posa y espera). Las demás marcas aparecen 4 cuadros antes de su toque |
| `toque` | `power2.out` / `power2.in` | 4 · 2 · 6 | la marca aparece (opacidad 0 → 1, escala 0,6 → 1), se hunde a 0,86 en el cuadro y se va 6 después; la onda 36 → 58 px CSS en 0,45 s, `#015BBE` al 90 % |
| `ventana-cambio` | `power2.inOut` | 15 | escala 1 → 0,92 + x (§1.4), 724–738 |
| `halo` | `sine.out` | 90 | 1,08 → 1,00 en 0, 180 y 720; los puntos no se mueven |
| `dip` | escalón | 3 | 837–839 |
| firma | las del kit | 75 | `back.out(2.2)` de la corona; **no se imita en el cuerpo** |
| resortes | ninguno | — | nada rebota salvo la corona |
| velocidad de la grabación | `data-playback-rate` por tramo (o carril `rate`) | — | entre **0,35× y 3,5×**; las rampas van entre acciones, nunca durante una letra o un toque. Los cortes caen en los `huecos_de_pantalla` de `pasos.json` |

`data-motion-blur="on"` con `data-motion-blur-shutter="180"` en la raíz. **Nunca `filter: blur()` sobre la grabación.**

### 1.7 Sonido

| Capa | Fuente | Nivel | Regla |
|---|---|---|---|
| Música | `assets/musica/product-launch-the-mountain.mp3`, `data-media-start` 14,05, dura 29 s | 0,7 en el carril de volumen (−18 LUFS, `kit.json`) | 0,7 hasta el 840 → 0,224 en el 852 → 0 en el 870 |
| Sonidos de acción (kit v1.1) | `toque` · `aparicion` · `desliz` · `subida` · `confirmacion` | el nivel del kit (`data-volume="1"`, 4–10 dB bajo la música); **1,4** solo en los cuatro toques clave (121 · 181 · 601 · 661) y en las `confirmacion` del 123 y del 663 | `data-start` = cuadro / 30 − acento; el pico suena **un cuadro después** de su imagen. `toque` rota a (`toque.wav`), b (+3 %), c (−3 %), nunca la misma dos veces seguidas. Sin tics de tecla |
| Sonido de marca | `identidad/audio/sonido-marca.wav` | tal cual | en **28,38 s** (cuadro 851) |
| Mezcla | — | −16 LUFS integrados, pico real ≤ −1 dBTP | `normalize-audio` sobre el render de entrega; se comprueba con `hyperframes audio --json`. Si el normalizador recorta, los 1,4 bajan a 1,2 |

Los 24 eventos, con su causa (cuadro del sonido = imagen + 1):

| Cuadro | Sonido | Causa |
|---|---|---|
| 76 | toque a | «Reportar» |
| 121 | toque c (1,4) | «Igual que la última vez» |
| 123 | confirmacion (1,4) | las filas se marcan, «4 marcadas» |
| 155 | desliz | la app baja al final de la lista (acento en el 155) |
| 181 | toque b (1,4) | «Persona nueva» |
| 196 | aparicion | la ceja «EVENTOS» |
| 241 · 271 · 301 | toque a · b · c | Nombres · Apellidos · Teléfono |
| 346 | toque a | «Mujer» |
| 376 | toque b | «Agregar» |
| 379 | aparicion | la fila «Ximena Hoyos Vélez · Nueva» |
| 451 · 481 | toque c · toque a | «+» · «+» |
| 453 · 483 | aparicion · aparicion | «Total: 6 personas» · «Total: 7 personas» |
| 601 | toque b (1,4) | «Guardar asistencia» |
| 603 | confirmacion (1,0) | el paso ① hecho, la barra al 66 % |
| 616 · 631 | toque c · toque a | «Muy bien» · «Tema de la palabra» |
| 661 | toque b (1,4) | «Enviar reporte» |
| 663 | confirmacion (1,4) | «¡Listo!» |
| 796–853 | subida | su golpe (acento 1,5 s) en el 840 |
| 851 | campanas | la firma + 0,38 |

Ninguno sin causa visible; 0–6 s lleva seis. Nada de whoosh en los movimientos de cámara ni en el desplazamiento del 652.

### 1.8 BANNED: los valores por defecto prohibidos, con nombre

Los 20 de Membresía valen enteros (fundido de 0,5 s para todo; fade + deslizar hacia arriba; zoom lineal; «creeping scale»; fundido
cruzado entre mundos; teléfono dibujado; texto que se mueve mientras se lee o «respira»; logo en una esquina; brillo, neón, partículas,
orbes; degradados nuevos y tarjetas de vidrio; tres tarjetas en fila, KPI, «01 / 02», corner brackets, HUD; whoosh en cada corte y el mismo
`toque` sin rotar; reproducción fuera de 0,35×–3,5×; retocar un píxel de la app; texto de la app < 28 px; centrarlo todo; cifras sin «Datos
de ejemplo»; más de 3 s sin cambio visible; un pulso vacío entre el 0 y el 360; `from()`, `autoAlpha` sobre un `.clip`, `transform` de
CSS donde GSAP transforma, el `<video>` y su envoltorio con tiempo a la vez). Y los de este clip:

21. **La cámara y el desplazamiento de la app a la vez.** Cuando la app baja (150–165, 652–660), la cámara está muerta de quieta; cuando
    la cámara se mueve, la app no escribe ni se desplaza.
22. **Dos `confirmacion` a menos de 1 s, o una por cada toque.** Tres en todo el clip, una por prueba: 123, 603, 663. Los «+» llevan
    `aparicion`; los campos, solo `toque`.
23. **Recrear la hoja «Persona nueva», la barra de avance o el «¡Listo!»** como gráficos propios, o «ayudar» a la barra con un tween. Todo
    sale de la grabación; la barra crece sola (transición de 0,3 s de la app).
24. **Un látigo «para animar».** Este clip tiene un solo mundo; un látigo sin cambio de persona es un whoosh con otro nombre.
25. **Dibujar una marca de toque donde la grabación no tocó**, o una marca que viaja «hasta» el botón. La marca nace donde `pasos.json`
    dice (`toques[]`); solo la del 105 espera quieta sobre su botón.
26. **La ceja o una frase sobre la hoja «Persona nueva» tapándole el título.** Las frases viven arriba del cuadro (§1.4); la ventana
    empieza en y = 360 y nada se superpone.

Después del primer render, cada valor por defecto que aun así aparezca se nombra aquí y se corrige.

---

## 2. Los planos, cuadro por cuadro

### 2.0 Convenciones

- **G / G⁺ / M / C** y los nombres de objetivo (`fila`, `lista`, `hoja-alta`…): §1.5. «Sobre X» = la caja de X centrada en la ventana.
- **Pulso**: el cuadro de la grilla de §0. Un evento «en el 120» aterriza en el cuadro 120 (su sonido suena en el 121).
- **Grabación**: una sola, `clips/eventos-casa-de-paz` (cuenta 103), con los tramos `inicio · reportar · igual · abajo · nueva · agregar ·
  visitantes · guardar · listo` (§3). Los cortes de video caen en pausas de la grabación.
- **Textos de la app**: son los reales, verificados en `frontend-v2/public/i18n/es.json` (`ev3.*`, `ev.*`) y en la semilla
  (`backend/cron/jobs/_demo_eventos.php`): «Reuniones por reportar», «Reportar», «{n} vencidas», «Pendiente», «Hoy», «Ayer», «Asistencia ·
  Reporte · Listo», «{n} marcadas», «Igual que la última vez», «Buscar a alguien más», «Vino {n} de 4», «Persona nueva», «Nombres»,
  «Apellidos», «Indicativo», «Teléfono», «Mujer», «Hombre», «Es un niño o una niña (sin teléfono)», «Agregar», «Nueva», «Visitantes»,
  «Quienes vinieron y no se registran», «Total: {n} personas», «No hubo reunión», «Guardar asistencia», «Reporte de la casa de paz», «La
  reunión», «¿Cómo estuvo la reunión?», «Muy bien · Bien · Difícil», «Tema de la palabra», «Peticiones de oración», «Enviar reporte»,
  «¡Listo!», «{evento}, {fecha}: {n} personas.», «Volver a la lista», «Reportar la siguiente», «Reportada». Lo que cambia con la semilla (el
  nombre de la casa, la fecha, los nombres de las personas, cuántas marca «Igual que la última vez») lleva «(real)».
- Las frases siempre en el mismo lugar (§1.4); una frase a la vez; la ceja encima de la frase.
- **Posiciones CSS** de la app: estimadas sobre las capturas de la ayuda; las reales, de `pasos.json`.

### 2.1 Tabla maestra (todo lo que cambia, por cuadro)

| Cuadro | Pulso | La app (grabación) | Cámara | Texto | Sonido | Transición |
|---|---|---|---|---|---|---|
| **0** | ● | Tramo `inicio` · Servir: barra «Kingdom Demo», «Servir en Iglesia Kingdom Demo 1», «Hola, Jorge Gallego Gil», la tarjeta **«Reuniones por reportar»** con su número en rojo y las filas: **«Casa de Paz Laureles 1 (real) · Mié, 28 de oct (real) · 2 vencidas (real)» · «Reportar»**, y dos más. «Datos de ejemplo» abajo a la izquierda | G `servir` | **«Terminó»** ya aterrizada (es la miniatura) | — | — |
| 15 · 30 · 45 | ● ● ● | quieta | quieta | **«la reunión.»** 15 · **«¿Quién»** 30 · **«vino?»** 45. Frase 1 completa y muerta de quieta hasta el 117 | — | |
| 46–59 | | quieta | **Movimiento del compás 1**: G → **M `fila`** (la fila de la casa con «2 vencidas» en rojo a 44 px) | | — | |
| 71–81 | **75 ●** | **75: toque en «Reportar»** (el botón de la fila). La app navega a `/servir/eventos/reportar?evento=&fecha=`; el corte cae en la espera | quieta en M | | `toque` a en el 76 | **Match cut sobre el toque:** en el 78 la pantalla ya es el reporte y entra 1,03 → 1,00 (`aterrizaje-app`, 78–88) |
| 78–89 | | **El reporte (real):** «Casa de Paz Laureles 1 · Casa de paz · miércoles, 28 de octubre», la píldora **«Pendiente»**, los atajos «Hoy · Ayer · **Mié, 28 de oct ●** · …», los pasos **① Asistencia · ② Reporte · ✓ Listo** con la barra al 15 %, **«0 marcadas» · «Igual que la última vez»** | M (`reporte-cabeza`, el mismo encuadre) | | — | |
| **90–103** | ● | quieta | **Movimiento del compás 2**: M → **G `lista`** (tope de abajo): «0 marcadas · Igual que la última vez», «Buscar a alguien más» y las cuatro casillas con **«Vino 4 de 4» (real)** | | — | |
| **105** | ● | quieta | quieta | | — | **`dedo-espera`:** la marca de toque aparece sobre «Igual que la última vez» (105–109) y se queda |
| 117–121 | | | | la frase 1 sale | | |
| **120** | **●●● bajo** | **toque en «Igual que la última vez»** | quieta | **«Los de siempre, / en un toque.»** entrada-linea 120–126 | **`toque` c (1,4) en el 121** | |
| 122 | | **las filas se marcan a la vez (real):** las casillas llenas, las filas en ámbar, **«4 marcadas» (real)**; la onda de Material termina en el 135 | quieta | frase 2 quieta | **`confirmacion` (1,4) en el 123** | |
| **150–165** | ● ● | **la app baja hasta el final de la lista** (`ver #btn-persona-nueva`, 300 ms reales a 0,6×): pasan las casillas y entran **«Persona nueva»**, **«Visitantes [− 0 +]»**, **«Total: 4 personas»** y «No hubo reunión · Guardar asistencia» | **quieta** (G) | | `desliz` (acento 155) | |
| 176 | | | | la frase 2 sale 177–181 | | la marca aparece sobre «Persona nueva» |
| **180** | **●●● pico** | **toque en «Persona nueva»** → la hoja real sube desde abajo (`hoja-abajo`, ≈ 200 ms): **«Persona nueva»** · Nombres · Apellidos · Indicativo «57» + Teléfono · Mujer / Hombre · «Es un niño o una niña (sin teléfono)» · Cancelar / **Agregar** | **Movimiento del compás 4**: G → **M `hoja-alta`**, 180–193 | — | **`toque` b (1,4) en el 181** | **Iris desde el toque** 180–185 (still del 179 debajo); halo 1,08 → 1 (180–270) |
| **195** | ● | la hoja quieta | quieta | **«EVENTOS»** entrada-linea 195–201 | `aparicion` en el 196 | |
| **240** | ●● | toque en «Nombres»; **242–257 se escribe «Ximena»** (7 teclas a 1×) | quieta | | `toque` a en el 241 | |
| **270** | ● | toque en «Apellidos»; **272–295 «Hoyos Vélez»** (11 teclas a 1×) | quieta | | `toque` b en el 271 | |
| **300** | ● | toque en «Teléfono» | **Movimiento del compás 6**: M → **M `hoja-baja`**, 300–313 (el dedo toca, todavía no escribe) | | `toque` c en el 301 | |
| 315–341 | ● ● | **se escribe `5550198765`** (10 teclas a 0,8×) | **quieta** | | — | |
| **345** | ● | **toque en «Mujer»** → el botón se llena | vuelta M → **G⁺ `hoja`** (de Nombres a «Agregar»), 345–359 | | `toque` a en el 346 | |
| **360** | ● | la hoja completa, quieta | quieta | **«Y queda registrada / en la iglesia»**: Y 360 · queda 362 · registrada 364 · en 366 · la 368 · iglesia 370 | — | |
| **375** | ● | **toque en «Agregar»** → la hoja se cierra (≈ 150 ms) y detrás está la lista: la fila **«Ximena Hoyos Vélez» con el chip «Nueva»**, marcada, encima de «Persona nueva»; **«Total: 5 personas»** | quieta | frase 3 quieta | `toque` b en el 376; **`aparicion` en el 379** (la fila) | |
| **390–403** | ● | quieta | **Movimiento del compás 7**: G⁺ → **M `nueva-fila`** (la fila nueva, «Persona nueva», «Visitantes», «Total») | | — | |
| **450** | ● | **toque en «+»** → Visitantes **1**, **«Total: 6 personas»** | quieta | | `toque` c 451 · `aparicion` 453 | |
| **480** | ● | **toque en «+»** → **2**, **«Total: 7 personas»** | quieta | | `toque` a 481 · `aparicion` 483 | |
| **510–523** | ● | quieta | **Movimiento del compás 9**: M → **C `total`** («Total: 7 personas» a 57 px) | | — | |
| **540–553** | ● | quieta | **Movimiento del compás 10**: C → **M `botones`** («Total» y «No hubo reunión · Guardar asistencia») | | — | |
| 585 · 596 | ● | el dedo llega a «Guardar asistencia» | quieta | la frase 3 sale 597–601 | — | la marca aparece en el 596 |
| **600** | **●●● 2.ª subida** | **toque en «Guardar asistencia»** → la app guarda (cola → servidor) y pasa al paso ②: **① hecho, la barra 15 → 66 %** (transición real de 0,3 s, 603–612), **«Reporte de la casa de paz» · «La reunión» · «¿Cómo estuvo la reunión?» · Muy bien / Bien / Difícil · «Tema de la palabra» · «Peticiones de oración»**; la escena centra la pregunta | **Movimiento del compás 11**: M → **G `formulario`**, 600–613 | | **`toque` b (1,4) en el 601**; `confirmacion` (1,0) en el 603 | |
| **615** | ● | **toque en «Muy bien»** → el radio se llena | quieta | | `toque` c 616 | |
| **630** | ● | toque en «Tema de la palabra»; **632–651 se escribe «El perdón»** (9 teclas a 1×) | quieta | | `toque` a 631 | |
| 652–660 | | la app baja hasta «Enviar reporte» (`ver`, 300 ms); la marca aparece en el 656 | quieta | | — | |
| **660** | **●●● golpe** | **toque en «Enviar reporte»** → **«¡Listo!»** (`task_alt`) · **«Casa de Paz Laureles 1, miércoles, 28 de octubre: 7 personas.» (real)** · «Volver a la lista» · «Reportar la siguiente»; arriba **«Reportada»** (verde), los tres pasos hechos y **la barra 66 → 100 %** (663–672) | **Movimiento del compás 12**: G → **G `listo`** (de «Reportada» a los botones), 660–673 | — | **`toque` b (1,4) en el 661**; **`confirmacion` (1,4) en el 663** | |
| **690** | ● | quieta | **Punch** G → **M `listo-tarjeta`**, 690–698 (9 cuadros): el ícono, «¡Listo!», la frase con **«7 personas»** a 44 px | — | — | |
| **720** | **●●● golpe** | quieta (el «¡Listo!» real) | **Movimiento del compás 13**: M → **G⁺ `cierre`** («Reportada», los pasos hechos, la barra, «¡Listo!», la frase con el total), 720–733 | **«Cada *reunión* cuenta, / y cuenta bien»**: Cada 720 · *reunión* 722 · cuenta, 724 · y 726 · cuenta 728 · bien 730. **La ceja sale 720–723** | — | **La ventana se hace a un lado**: escala 1 → 0,92 + x (§1.4), 724–738; halo 1,08 → 1 (720–810) |
| 735–836 | 735 … 825 | quieta | quieta | frase 4 quieta ≥ 3,6 s | **`subida`** 796–853 (golpe en el 840) | |
| **837–839** | | — | — | — | — | **Dip** al 40 %, 3 cuadros |
| **840** | **●●● el más fuerte** | — | — | — | la música 0,7 → 0,224 (852) → 0 (870) | **Corte a la firma**: 4:5 `cierre-clip`, 9:16 `cierre-corto`; `{"llamado":"prueba","fondo":"azul","idioma":"es"}` |
| 846 · 853 ↓ | | la K sube; las 7 barras de la corona desde 0,45 s (`back.out(2.2)`) | | «Kingdom» 0,75 s; **«Prueba gratis 30 días»** 0,95 s | **Campanas en el 851** | |
| **914** | | último cuadro: la corona completa y el botón | | | silencio de música desde el 870 | fin |

### 2.2 Los siete planos

#### P1 · «Terminó la reunión» — cuadros 0–119 (compases 1–2) · pulsos 0, 15, 30, 45, 60, 75, 90, 105

- **Grabación:** tramos `inicio` (Servir quieto 1,5 s; se usa a 1×) y `reportar` (el toque y la carga del reporte; el corte cae en la espera
  entre el toque y la pantalla nueva). Lo demás, a 1×.
- **Encuadre 4:5:** G `servir` (CSS 0–439); M `fila` desde el 59. **9:16:** G muestra 345 px CSS: arranca 40 px más abajo (56–401: sin la
  barra de la app) para que la tarjeta entre entera; M igual.
- **Cámara:** quieta hasta el 45; 46–59 a M `fila`; el match cut del 78 en el mismo encuadre; 90–103 a G `lista`. Nada más.
- **Texto:** frase 1 por pulsos (la primera landing ya puesta en el cuadro 0); sale 117–121.
- **Sonido:** toque 76.
- **Transición:** el match cut sobre el toque del 75 (`aterrizaje-app` 78–88); cierra con el toque del 120.
- **Válvula si el reporte tarda en cargar** (más de 0,5 s en la grabación): el corte en la espera se alarga, nada cambia en el clip; si la
  pantalla nueva no está lista en el 78, el toque se adelanta al 60 y el compás 1 se queda sin movimiento de cámara (la fila ya se lee a G).

#### P2 · «Los de siempre, en un toque» — cuadros 120–179 (compás 3) · pulsos 120 (bajo), 135, 150, 165

- **Grabación:** tramos `igual` (el toque y las filas que se marcan; 1,5 s quietas) y `abajo` (el desplazamiento a 0,6× para que dure un
  pulso: 150–165).
- **Encuadre:** G `lista`, el tope de abajo de la grabación: las cuatro casillas se marcan **dentro del cuadro**. Igual en 9:16 (ahí caben
  tres casillas: la cuarta queda fuera, y en el 150 el desplazamiento la trae).
- **Cámara:** muerta de quieta todo el compás (la app se desplaza en 150–165: regla 21).
- **Texto:** frase 2 entra 120–126 (línea entera), sale 177–181.
- **Sonido:** toque 121 (1,4), confirmacion 123 (1,4), desliz 155.
- **Transición:** ninguna dentro; cierra con el iris del 180.
- **Plan B** (si «Igual que la última vez» marca menos de tres, §3): tres toques en casillas en 120 · 135 · 150 (`toque` c · a · b), sin
  `confirmacion`, el desplazamiento en 165–178 y la frase 2 pasa a **«Marca quién vino.»** (3 palabras, línea entera).

#### P3 · «Persona nueva» — cuadros 180–359 (compases 4–6) · pulsos 180 (pico), 195, 240, 270, 300, 345

- **Grabación:** tramo `nueva`: el toque, la hoja que sube, los tres campos escritos a 70 ms por tecla (se usan a 1×, el teléfono a 0,8×) y
  «Mujer». Las pausas de 400 ms entre campos se recortan para que cada toque caiga en su pulso.
- **Encuadre:** M `hoja-alta` (180–299), M `hoja-baja` (313–344), G⁺ `hoja` (desde el 359). En 9:16, M muestra 247 px CSS: `hoja-alta` se
  centra en Nombres + Apellidos y `hoja-baja` en Teléfono + Mujer / Hombre + Agregar.
- **Cámara:** tres movimientos (180–193, 300–313, 345–359), uno por compás; **ninguno mientras se escribe** (242–257, 272–295, 315–341).
- **Texto:** la ceja «EVENTOS» 195–201; sin frase (la hoja y la escritura son el espectáculo).
- **Sonido:** toque 181 (1,4), aparicion 196, toque 241, 271, 301, 346.
- **Transición:** iris desde «Persona nueva» (180–185).
- **Si la hoja busca duplicados y aparece «¿Ya está registrada?»** (no debería: «Ximena» no está en el banco de nombres de la demo, §5): se
  deja ver (es real) y la cámara no la persigue; si tapa «Agregar», la escena cambia el nombre, no el guion.

#### P4 · «Y queda registrada» — cuadros 360–599 (compases 7–10) · pulsos 360, 375, 390, 450, 480, 510, 540, 585

- **Grabación:** tramos `agregar` (el toque, la hoja que se cierra, la fila nueva quieta 1,5 s) y `visitantes` (dos toques en «+» con 600 ms
  entre ellos y 1,2 s después; `ver` sobre el total y sobre «Guardar asistencia» para las cajas). A 1× salvo las pausas, que se recortan.
- **Encuadre:** G⁺ `hoja` hasta que se cierra; M `nueva-fila` (403–509); C `total` (523–539); M `botones` (desde el 553). En 9:16 los
  mismos objetivos.
- **Cámara:** 390–403, 510–523 y 540–553 (compases 7, 9 y 10); el compás 8 es solo la app contando.
- **Texto:** frase 3 entra 360–370 (seis palabras a 2 cuadros); sale 597–601.
- **Sonido:** toque 376, aparicion 379, toque 451 + aparicion 453, toque 481 + aparicion 483.
- **Transición:** ninguna (la hoja se cierra sola, dentro de la app).

#### P5 · «Guardar asistencia, enviar reporte» — cuadros 600–719 (compases 11–12) · pulsos 600 (subida), 615, 630, 660 (golpe), 690

- **Grabación:** tramos `guardar` (el toque, el paso ②, la pregunta, el tema) y `listo` (el toque y el «¡Listo!» quieto 4 s). A 1×; los
  cortes en las esperas del servidor (si asoma la K del cargador, se corta: §5).
- **Encuadre:** G `formulario` (613–689): los pasos con la barra, el título del formulario, la pregunta, los radios y el tema caben en 439
  px CSS; G `listo` (673–689); M `listo-tarjeta` (desde el 698). En 9:16, `formulario` muestra 345 px CSS: se centra en la barra, la
  pregunta y los radios; el tema entra al escribirse porque la app desplaza.
- **Cámara:** 600–613, 660–673 y el punch 690–698. Quieta mientras se escribe «El perdón» (632–651) y mientras la app baja (652–660).
- **Texto:** ninguno (las dos pruebas las da la app).
- **Sonido:** toque 601 (1,4), confirmacion 603, toque 616, 631, toque 661 (1,4), confirmacion 663 (1,4).
- **Transición:** ninguna; cierra con la frase 4 del 720.
- **Válvula si 630–660 va atropellado:** no se escribe el tema (es opcional en el formulario): 615 «Muy bien», 630 el dedo baja, 660
  «Enviar reporte». El clip no pierde nada: el tema no se lee a esa velocidad.

#### P6 · «Cada reunión cuenta, y cuenta bien» — cuadros 720–839 (compases 13–14) · pulsos 720 (golpe), 735 … 825

- **Grabación:** el final del tramo `listo` (4 s quietos a 1×).
- **Encuadre:** G⁺ `cierre` con la ventana a 0,92 y corrida (§1.4): «Reportada», los tres pasos hechos, la barra al 100 %, el ícono,
  «¡Listo!» y la frase con el total; el cuerpo de la app a ≥ 31 px. En 9:16 la ventana se encoge desde arriba y termina en 1262.
- **Cámara:** 720–733 a G⁺; después muerta de quieta. El halo se asienta 720–810.
- **Texto:** frase 4 entra 720–730 (*reunión* en itálica dorada); la ceja sale 720–723; la frase se sostiene 3,6 s.
- **Sonido:** subida 796–853.
- **Transición:** dip 837–839 y corte duro al 840.

#### P7 · «La firma» — cuadros 840–914

- 4:5: `identidad/cierre-clip.html`; 9:16: `identidad/cierre-corto.html`. Variables `{"llamado":"prueba","fondo":"azul","idioma":"es"}`.
- Campanas en 28,38 (cuadro 851). La música: 0,7 → 0,224 (852) → 0 (870).
- El único gesto de marca del clip.

---

## 3. La grabación: la escena `tools/ayuda/escenas/clips/eventos-casa-de-paz.mjs`

Una sola escena de **celular** (`movil: true`, 390×844 a 3× → **1170×2532**, 30 cps) sin el círculo del toque (`toque: false`), con
`capturar.mjs --modo video` sobre Kingdom Demo en español:

```bash
cd F:/Proyectos/KingdomApp/tools/ayuda
node capturar.mjs clips/eventos-casa-de-paz --idioma es --modo video
# → salida/video/es/clips/eventos-casa-de-paz/grabacion.mp4 + pasos.json (inicio/fin, tramo, accion, toques[], teclas[], caja_video)
```

**Cuenta:** 103 = el servidor **Jorge Gallego Gil**, responsable de la primera casa de paz de la semilla (`_demo_eventos.php` → «La cuenta de
prueba de servidor, responsable de dos casas y de un discipulado»). **Datos ficticios:** «Ximena Hoyos Vélez» y el teléfono `5550198765` no
existen en la demo («Ximena» no está en `DEMO_NOMBRES_F`, así que la hoja no propone «¿Ya está registrada?»).

**Lo que la semilla garantiza** (verificado en `backend/cron/jobs/_demo_eventos.php` y en las escenas de la ayuda `eventos/reportar-una-reunion.mjs`
y `eventos/ver-eventos.mjs`): la casa de la cuenta 103 tiene sus últimas tres reuniones sin reportar (línea 178: por eso la tarjeta dice
«2 vencidas» y abre la pendiente más reciente); la categoría Casa de Paz es asistencia por nombre, con visitantes, plazo de 2 días, sin
aprobación, y pide el formulario **«Reporte de la casa de paz»** con «¿Cómo estuvo la reunión?» (obligatoria: Muy bien / Bien / Difícil),
«Tema de la palabra» (corta, opcional) y «Peticiones de oración» (larga, opcional). Lo que no garantiza: a cuántas personas marca «Igual que
la última vez» (`igualQueLaUltima` → `ultima_personas`, la última reunión con asistencia de la casa, que viene de la copia de v1). La `ref`
`ultima` lo exige (≥ 3) o la escena se niega antes de grabar.

**Selectores** (verificados en `frontend-v2/src/app/pages/servir/servir-inicio.page.ts` y `pages/eventos/`: `por-reportar-tarjeta`,
`reporte`, `reporte-asistencia`, `reporte-persona-nueva`, y en `pages/membresia/formulario-responder.component.ts` para `[data-pregunta]`).

```js
// Grabación para el clip del sitio público «Terminó la reunión» (LegacyHyperframes/videos/kingdomapp/clip-sitio-eventos/SPEC.md §3).
// NO es una escena de un artículo de la ayuda: no se publica ni entra en la frescura. Una sola escena de CELULAR (390×844 a 3x = 1170×2532,
// 30 cps) grabada SIN el círculo del toque (`toque: false`): el montaje dibuja el suyo sobre toques[] y las cajas de pasos.json.
//   node capturar.mjs clips/eventos-casa-de-paz --idioma es --modo video
//   → salida/video/es/clips/eventos-casa-de-paz/grabacion.mp4 + pasos.json
// Tramos: inicio (Servir) · reportar · igual · abajo · nueva · agregar · visitantes · guardar · listo. Todo con la cuenta 103 (el servidor
// Jorge Gallego Gil), responsable de la primera casa de paz de la semilla.
// Datos ficticios de Kingdom Demo: «Ximena Hoyos Vélez» y el teléfono 5550198765 no existen en la demo («Ximena» no está en DEMO_NOMBRES_F).
const CASA = `(SELECT r.id_evento FROM ev_responsables r JOIN kd_usuario_sedes us ON us.id_persona = r.id_persona AND us.id_sede = r.id_sede
               WHERE us.id_usuario = 103 ORDER BY r.id_evento LIMIT 1)`;
const FILA_TARJETA = '#tarjeta-por-reportar a.fila[data-evento="{@casa}"]';

export default {
  articulo: 'clips/eventos-casa-de-paz',
  movil: true,
  toque: false,
  pantallas: [
    'frontend-v2/src/app/pages/servir/servir-inicio.page.ts',
    'frontend-v2/src/app/pages/eventos/por-reportar-tarjeta.component.ts',
    'frontend-v2/src/app/pages/eventos/reportar.page.ts',
    'frontend-v2/src/app/pages/eventos/eventos-cabecera.component.ts',
    'frontend-v2/src/app/pages/eventos/reporte.component.ts',
    'frontend-v2/src/app/pages/eventos/reporte-asistencia.component.ts',
    'frontend-v2/src/app/pages/eventos/reporte-persona-nueva.component.ts',
    'frontend-v2/src/app/pages/membresia/formulario-responder.component.ts',
  ],
  refs: {
    casa: `SELECT ${CASA}`,
    // La reunión pendiente más reciente de la casa (la que abre la tarjeta): si no hay, la escena no sirve.
    pendiente: `SELECT fecha FROM ev_reuniones WHERE id_evento = ${CASA} AND estado = 'pendiente' AND esperada = 1 ORDER BY fecha DESC LIMIT 1`,
    // «Igual que la última vez» (cuadro 120 del clip) tiene que marcar al menos a tres personas: las de la última reunión con asistencia.
    // Si son menos, la consulta da NULL y capturar.mjs se niega: entra el plan B del SPEC (tres casillas a mano).
    ultima: `SELECT IF(COUNT(*) >= 3, COUNT(*), NULL) FROM ev_asistencias a
              WHERE a.id_reunion = (SELECT id FROM ev_reuniones WHERE id_evento = ${CASA} AND estado IN ('reportada', 'parcial') AND nombres > 0
                                    ORDER BY fecha DESC LIMIT 1)`,
  },
  pasos: [
    // 1-2. Servir: la tarjeta «Reuniones por reportar» quieta (cuadro 0 del clip).
    { tramo: 'inicio', como: 103, ir: '/servir', espera: FILA_TARJETA },
    { pausa: 1500 },
    // 3. «Reportar» en la fila de la casa (el toque del 75): abre el reporte de la pendiente más reciente, con sus casillas.
    { tramo: 'reportar', clic: `${FILA_TARJETA} .boton`, espera: '#reporte[data-evento="{@casa}"] #asis-lista li.fila', pausa: 1500 },
    // 4. «Igual que la última vez» (el toque del 120, el bajo): las filas se marcan a la vez.
    { tramo: 'igual', clic: '#btn-igual-ultima', espera: '#asis-lista li.fila.si', pausa: 1500 },
    // 5. La app baja al final de la lista: «Persona nueva», «Visitantes», «Total» y los botones (el desliz del 150).
    { tramo: 'abajo', ver: '#btn-persona-nueva', pausa: 1200 },
    // 6-10. «Persona nueva» (el toque del 180, el pico): la hoja sube; nombres, apellidos, teléfono y «Mujer».
    { tramo: 'nueva', clic: '#btn-persona-nueva', espera: '#nueva-nombres', pausa: 1200 },
    { escribir: { en: '#nueva-nombres', texto: 'Ximena' }, pausa: 400 },
    { escribir: { en: '#nueva-apellidos', texto: 'Hoyos Vélez' }, pausa: 400 },
    { escribir: { en: '#nueva-telefono', texto: '5550198765' }, pausa: 400 },
    { clic: '#nueva-genero-F', pausa: 600 },
    // 11-12. «Agregar» (el toque del 375): la hoja se cierra y la fila «Ximena Hoyos Vélez · Nueva» queda marcada.
    { tramo: 'agregar', clic: '#btn-agregar-nueva', oculto: 'mat-dialog-container' },
    { espera: '#asis-lista li.fila[data-nueva]', pausa: 1500 },
    // 13-16. Dos visitantes (los toques del 450 y del 480); las cajas del total y de «Guardar asistencia».
    { tramo: 'visitantes', clic: '#btn-visitantes-mas', pausa: 600 },
    { clic: '#btn-visitantes-mas', pausa: 1200 },
    { ver: '#asis-total', pausa: 300 },                 // solo para la caja de «Total: 7 personas» (objetivo del 510)
    { ver: '#btn-guardar-asistencia', pausa: 400 },     // el dedo baja a los botones (objetivo del 540)
    // 17-21. «Guardar asistencia» (el toque del 600, la segunda subida): la barra salta y entra el paso ② «Reporte de la casa de paz».
    { tramo: 'guardar', clic: '#btn-guardar-asistencia', espera: '#reporte-formulario' },
    { ver: '[data-pregunta="como"]', pausa: 1200 },     // la pregunta al centro: la barra y el formulario caben en G
    { marcar: '[data-pregunta="como"] mat-radio-button[data-opcion="muy_bien"]', pausa: 600 },
    { escribir: { en: '[data-pregunta="tema"] input, [data-pregunta="tema"] textarea', texto: 'El perdón' }, pausa: 400 },
    { ver: '#btn-enviar-reporte', pausa: 400 },
    // 22-24. «Enviar reporte» (el toque del 660, el golpe): «¡Listo!» con el total; «Reportada» arriba. Quieto 4 s para el final.
    { tramo: 'listo', clic: '#btn-enviar-reporte', espera: '#reporte-listo' },
    { ver: '#reporte-listo', pausa: 4000 },
    { ver: '#reporte-listo p >> nth=0', pausa: 300 },   // solo para la caja de la frase con el total (objetivo del 690)
  ],
};
```

Notas sobre la escena:

- `ver` desplaza suave (300 ms) con `block: 'center'` salvo que el paso diga `bloque`; en el celular la barra de la app es fija, así que no
  se usa `bloque: 'start'` (taparía el elemento). Las cajas de la cámara (§1.5) se toman de `caja`/`caja_video` del paso que las nombra.
- La herramienta espera 900 ms tras cada acción y lo que diga `pausa`; `escribir` toca el campo (es un toque real, con su marca) y escribe a
  70 ms por tecla; `marcar` toca el radio. Todo lo que sobra se corta en el montaje; nada se puede alargar: por eso las pausas largas sobre
  lo que se mira (1,5 s) y los 4 s finales.
- **Tiempos:** ≈ 1,5 + 3 + 3 + 2 + 2,5 + 1,5 + 1,8 + 1,8 + 1,6 + 2 + 2,5 + 1,7 + 1,7 + 1,2 + 1,3 + 2,5 + 2 + 1,5 + 1,7 + 1,3 + 2,5 + 5 + 1,2 ≈
  **47 s de grabación** para 28 s de clip. No hace falta `consolaEsperada` (no hay tramo sin señal).
- **Plan B** (la `ref` `ultima` da NULL, es decir, la última reunión con asistencia de esa casa tiene menos de tres personas): se quita la
  `ref` y el paso 4 pasa a tres `marcar` sobre `#asis-lista li.fila >> nth=0|1|2 >> mat-checkbox` con `pausa: 400` entre ellos; en el clip
  caen en 120 · 135 · 150 (P2) y la frase 2 pasa a «Marca quién vino.». La alternativa de sembrar asistencias con el gancho `sql` de la
  escena (`INSERT` en `ev_asistencias` con `id_reunion, id_persona, id_sede, id_evento, fecha, modo = 'migrada'`) es posible, pero toca las
  métricas de la casa (`evMetricasRecalcular`) y no vale la pena por una frase.
- **Para el still del iris:** el cuadro 179 de la ventana se exporta (`ffmpeg -ss <t> -frames:v 1`) desde la grabación al tiempo de origen
  correspondiente y va como `<img>` en `assets/stills/`.

---

## 4. Lo que se revisa en la vista previa

Cuadros a mirar: `npx hyperframes snapshot --at 0,1.5,2.0,2.5,2.6,3.0,3.5,4.0,4.1,5.0,5.5,6.0,6.2,6.5,8.0,9.0,10.5,11.5,12.0,12.5,12.6,15.0,16.0,17.4,19.5,20.0,20.4,21.0,22.0,22.1,22.4,23.3,24.0,24.5,27.9,28.0,28.4,30.4`
en las dos composiciones, y `snapshot --range 2.4,3.0 --frames 18` para el match cut del reporte y `--range 5.9,6.3 --frames 12` para el iris.

1. **Cuadro 0 (la miniatura):** Servir con la tarjeta «Reuniones por reportar» y la fila de la casa con «2 vencidas» en rojo, «Terminó» en
   Fraunces ya puesta, «Datos de ejemplo» abajo a la izquierda. Nunca negro, nunca la marca. En 9:16, nada por encima de 168 ni por debajo
   de 1330 salvo halo y puntos.
2. **Cuadro 45:** las cuatro landings de la frase 1 quietas. **59:** M sobre la fila, «2 vencidas» legible a 44 px.
3. **75–88:** el toque en «Reportar» y el reporte que entra 1,03 → 1,00 sin un cuadro de página en blanco (si la app muestra «Cargando…», se
   corta). **103:** G sobre la lista con las cuatro casillas y «Igual que la última vez». **105–119:** la marca quieta sobre el botón.
4. **120–126:** el toque exactamente con el bajo; en el 122 las filas en ámbar y «N marcadas»; la frase 2 entera en el 126.
5. **150–165:** la app baja y la cámara no se mueve; en el 165 se ven «Persona nueva», «Visitantes» y «Total: 4 personas».
6. **180–193:** el iris nace del botón «Persona nueva»; la hoja real entra; la ceja cae en el 195 y no antes.
7. **242–257, 272–295, 315–341:** la escritura se lee a ≥ 44 px y **la cámara no se mueve** mientras se escribe. **345:** «Mujer» lleno.
8. **360–370:** la frase 3 palabra a palabra sobre la hoja quieta; **376–380:** la hoja se cierra y aparece «Ximena Hoyos Vélez · Nueva»
   marcada; «Total: 5 personas».
9. **451 · 481:** los dos «+»; «Total: 6» y «Total: 7 personas»; **523:** C sobre el total a ≥ 57 px.
10. **600–613:** «Guardar asistencia» con la segunda subida; la barra crece 15 → 66 % y el paso ① queda hecho; el formulario con su pregunta.
    **616:** «Muy bien» marcado. **632–651:** «El perdón» con la cámara quieta.
11. **660–673:** «Enviar reporte» en el golpe; «¡Listo!» con la frase y el total; «Reportada» arriba; la barra al 100 %. **698:** M sobre la
    tarjeta del «¡Listo!» con «7 personas» a 44 px: debe leerse de un vistazo.
12. **720–738:** la frase 4 aterrizada en el 730 con *reunión* dorada; la ceja fuera; la ventana a 0,92 y corrida; G⁺ con «Reportada», los
    pasos hechos y el «¡Listo!». **738–836:** nada se mueve salvo el halo; **837–839** el dip; **840** el primer cuadro de la firma sin noche
    vacía entre medias.
13. **Sonido (medido, no oído):** cada `toque` un cuadro después de su imagen; las tres `confirmacion` en 123, 603 y 663; las campanas en el
    851; la música a −10 dB en el 852 y a 0 en el 870; −16 LUFS, pico ≤ −1 dBTP; ningún tramo con dos sonidos de acción encimados salvo
    121 + 123, 601 + 603 y 661 + 663.
14. **Textos:** ninguna palabra que no esté en la app o en las cuatro frases; ningún texto de la app < 28 px; las frases en 2 líneas (3 en
    9:16 la cuarta); `npx hyperframes check` en 0 errores (contraste AA incluido); «Datos de ejemplo» desde el cuadro 0.
15. **La historia sin sonido:** se entiende con la pantalla en silencio (así se verá en el sitio): reuniones por reportar → la lista en un
    toque → persona nueva → siete personas → ¡Listo! → cada reunión cuenta → Kingdom.

---

## 5. Riesgos y lo que se decide al grabar

- **Cuántas marca «Igual que la última vez».** Es el único dato que la semilla no fija. La `ref` `ultima` exige ≥ 3; si falla, el plan B
  (§3, P2) marca tres casillas a mano y cambia la frase 2. Se decide al restaurar el volcado, antes de grabar.
- **El cargador de la app** (`loading.wrap`, la K animada a los 150 ms) en «Guardar asistencia» y «Enviar reporte»: con la API local no
  debería asomar; si asoma, se corta en la espera (los cortes del 600 y del 660 ya caen ahí).
- **«¿Ya está registrada?»** en la hoja mientras se escribe el nombre: «Ximena» no está en el banco de nombres de la demo; si la búsqueda
  flexible igual trae a alguien, se cambia el nombre en la escena (p. ej. «Maritza»), nunca el guion.
- **Dónde queda la lista después de cada desplazamiento** (150, 652) y dónde aparece la fila «Nueva» (al final de la lista, antes de «Persona
  nueva», según `filasAsistencia`): las cajas de §1.5 son estimaciones; los objetivos reales salen de `pasos.json` y el REVIEW los anota. La
  regla que no cambia: la cámara sujeta a la grabación, un movimiento por compás, nunca a la vez que la app.
- **El texto del «¡Listo!»** («{evento}, {fecha}: {n} personas.») y el nombre de la casa cambian con la semilla; ninguna frase depende de
  ellos. El número será 7 si el botón marcó 4 (4 + 1 nueva + 2 visitantes); si marcó 3, será 6. Da igual.
- **Densidad de 600–660:** cuatro acciones y una escritura en dos segundos. La válvula de P5 (sin el tema) está lista.
- **Densidad de 0–6 s:** seis sonidos, cuatro toques y dos movimientos de cámara. Si en la vista previa va atropellado, el movimiento 46–59 se
  quita (la fila se lee a G) y el toque del 75 se adelanta al 60.
- **Dos cosas del kit v1.1 que este clip usa tal cual** (ya construidas para Membresía): `cierre-clip` y `.k-ventana` / `.k-feed-*`; y el
  modo video de celular con `toque: false` y `pasos.json` con `toques[]`, también ya hecho. No hace falta nada nuevo de herramienta.
- **Idiomas (en, pt después):** la misma escena con `--idioma en` graba la interfaz en inglés (los textos de la escena van en español porque
  son datos que escribe la persona; «El perdón» pasa a `{ es: 'El perdón', en: 'Forgiveness' }` como en la escena de la ayuda); las frases se
  traducen y los saltos se vuelven a fijar; la firma lleva `idioma`.
