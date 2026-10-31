# SPEC · Recorrido del módulo: Eventos — «Terminó la reunión, y el lunes el pastor lo ve»

2026-10-30 · Contrato de construcción de la historia de [STORY.md](STORY.md) (el dueño ya no revisa guiones). Cada adjetivo es un número,
los valores por defecto están prohibidos con nombre y los planos van cuadro por cuadro sobre la grilla real de la pista. Hereda del
[clip](../clip-sitio-eventos/SPEC.md) su sistema y **sus primeros 720 cuadros enteros** (ya construidos y verificados en su
[REVIEW](../clip-sitio-eventos/REVIEW.md)); este SPEC dice qué cambia en ellos al pasar a 16:9 y especifica todo lo demás.

```text
GOAL:    Un pastor que no conoce Kingdom termina pensando «el líder reporta en la casa, aun sin señal, y yo lo veo todo el lunes:
         quién está al día, qué reunión crece y dónde falta una» y toca «Prueba gratis 30 días».
OUTPUT:  HyperFrames 0.8.221 · 1920×1080 (16:9) · 30 fps. (9:16 queda fuera de este SPEC: §8.)
TIME:    97,0 s = 2910 cuadros: cuerpo 0–92,0 (0–2759) + cierre del Comercial 92,0–97,0 (2760–2909). 120 BPM = 15 cuadros por pulso.
LOOK:    la noche del sitio (#060D1F) con el halo y los puntos del kit; tinta #EAF0FF; un solo acento, el dorado #E8B95A, en tres lugares
         (la ceja «EVENTOS», la palabra «reunión» de la frase final y el botón del cierre). Fraunces 560 / −0,02 em para las frases, Inter
         para la ceja y «Datos de ejemplo». El medio: la app REAL de Kingdom Demo en dos ventanas del kit: `.k-ventana-16x9` (720×900, el
         celular de Jorge) y `.k-ventana-escritorio` (1440×760, el computador del pastor); radio 28 / 20, anillo de 1 px, sombra del kit.
OBJECTS: la ventana del celular (Jorge, cuenta 103); la ventana del computador (el pastor, cuenta 101); las marcas de toque; las nueve
         frases; la ceja; las dos píldoras «Datos de ejemplo»; la corona del cierre. Nada más existe en el cuadro.
MOTION:  curvas por papel (§1.6); un movimiento de cámara por compás, quieta después y nunca mientras la app escribe o se desplaza; cada
         toque y cada corte en un pulso; los cambios grandes en los golpes (120 · 180 · 600 · 660 · 840 · 900 · 960 · 1080 · 1320 · 1560 ·
         1800 · 2100 · 2580 · 2760).
SHOTS:   doce planos (§2): P1–P5 del clip, P6 sin señal, P7 el látigo y el tablero, P8 el mapa, P9 la lista, P10 la ficha, P11 la frase
         final, P12 el cierre.
BANNED:  §1.8.
QA:      §6.
```

---

## 0. La música: «Product Launch» alargada a 96 s, y su grilla

### 0.1 La edición (una repetición sin costura)

La pista dura 86,05 s y el recorrido necesita 96. Se repiten **12 compases (24,000 s)**: se toca del 14,05 al 44,05 y se vuelve al 20,05,
y de ahí sigue hasta el final. Por qué ahí (medido sobre el mp3 el 2026-10-30, no oído):

- La pista está construida en bloques de 24 s: el compás 42,05–44,05 (el golpe más fuerte) repite al 18,05–20,05 (la entrada del bajo) y el
  44,05–46,05 repite al 20,05–22,05. Buscando entre todos los saltos de 20 a 30 s en borde de compás (cromas + bandas por compás), este es
  el de menor distancia (0,34 el compás que sigue, 0,60 el que precede); y la **correlación de la onda** entre 43,6–46,4 y 19,6–22,4 es
  **0,81 con desfase 0** (±30 ms probados): es el mismo material, a la muestra.
- La energía en los 120 ms del empalme es igual en los dos lados (RMS 0,174 y 0,175).
- Efecto en el video: el golpe más fuerte de la pista (42,05) suena **dos veces**, en el 28,0 y en el 52,0, y la pista termina sola: su
  último golpe (82,05) cae en el **92,0**, donde empieza el cierre, y el acorde se apaga debajo de las campanas.

Dos `<audio>` del mismo archivo en dos pistas, con un cruce de 30 ms que termina 70 ms **antes** del golpe del empalme (el golpe entero sale
del lado B). Niveles en el carril de volumen (valores absolutos; 0,75 como la mezcla final del clip, REVIEW §5):

```html
<!-- Música A: pista 14,05 → 44,025 (clip 0 → 29,975). El cruce: 0,75 → 0 entre el 29,945 y el 29,975. -->
<audio id="musica-a" src="assets/musica/product-launch-the-mountain.mp3" data-start="0" data-media-start="14.05" data-duration="29.975"
  data-track-index="20"
  data-automation='{"version":1,"lanes":[{"target":"volume","points":[{"t":0,"v":0.75},{"t":29.945,"v":0.75},{"t":29.975,"v":0}]}]}'></audio>
<!-- Música B: pista 19,995 → 86,05 (clip 29,945 → 96,0). Entra 0 → 0,75 en 30 ms; el golpe del 20,045 cae en el 29,995 (cuadro 900).
     El acorde final (82,045) cae en el 92,0: 0,75 → 0,24 (−10 dB) en el 92,4, debajo de las campanas, y 0 en el 94,0. -->
<audio id="musica-b" src="assets/musica/product-launch-the-mountain.mp3" data-start="29.945" data-media-start="19.995" data-duration="66.055"
  data-track-index="21"
  data-automation='{"version":1,"lanes":[{"target":"volume","points":[{"t":0,"v":0},{"t":0.03,"v":0.75},{"t":62.055,"v":0.75},{"t":62.455,"v":0.24},{"t":64.055,"v":0}]}]}'></audio>
```

Relación de tiempos: clip = pista − 14,05 antes del 29,975; clip = pista + 9,95 después. Se comprueba con
`npx hyperframes audio <render> --json`: ningún golpe extra ni hueco entre el 29,8 y el 30,2, y el golpe del 30,0 a la altura de los del
28,0 y el 32,0 (±1,5 dB); con `ffmpeg -af ebur128` la sonoridad momentánea no salta más de 1 LU en el 29,9–30,1. Si salta: el cruce pasa a
60 ms (29,915–29,975 en A, `data-start` 29,915 y `data-media-start` 19,965 en B), nunca se mueve el punto.

### 0.2 La grilla real

`pulsos.json` del kit vale tal cual hasta el 52,0 de la pista. **Del 53,8 al 80,2 el detector se enganchó en los contratiempos** (pulsos en
x,295 / x,795): la medición propia (flujo por banda) muestra corcheas parejas en toda la pista, el bombo en los x,045 y los cambios de
sección exactamente en el 50,045, el 66,045 y el 82,045 (el primer pulso de cada compás es siempre el más fuerte: +3 a +6 dB en el clímax).
Así que **la grilla es 2,045 + 0,5·k en toda la pista** y en el clip todo pulso cae en un múltiplo de 15 cuadros (±0,15 cuadro). Cada pulso
se calcula desde su índice, nunca sumando 15. Lo único irregular es el redoble del 52,5–53,4 de la pista (clip 62,5–63,4, cuadros
1875–1902): ahí no cae nada.

| Compás | Clip (s) | Cuadros | La pista | Fuerza del primer pulso | Sección | Lo que le toca |
|---|---|---|---|---|---|---|
| 1–12 | 0–24 | 0–719 | 14,05–38,05 | (SPEC del clip §0) | entrada → bajo (120) → pico (180) → respiro → 2.ª subida (600, 660) | **La historia del clip, sin cambios de tiempo** |
| 13 | 24 | 720 | 38,05 | 0,96 | 2.ª subida | Frase 4; la cámara a los botones del «¡Listo!» |
| 14 | 26 | 780 | 40,05 | 0,88 | | **«Volver a la lista»** → la lista sin señal; 810 la casa |
| 15 | **28** | **840** | **42,05** | **1,00** | el golpe más fuerte | **«Igual que la última vez», sin señal** |
| 16 | **30** | **900** | 44,05 → **20,05** | 0,87 (la costura) | 1.ª subida (repetida) | **«Guardar asistencia»**: «1 sin enviar» |
| 17 | 32 | 960 | 22,05 | 0,92 | | **Vuelve la señal: se envía sola.** Frase 5 |
| 18 | 34 | 1020 | 24,05 | 0,77 | | Quieto; la frase 5 se lee |
| 19 | **36** | **1080** | 26,05 | 0,76 | **respiro** | **El látigo** al computador; el tablero cuenta |
| 20 | 38 | 1140 | 28,05 | 0,75 | | Frase 6 |
| 21 | 40 | 1200 | 30,05 | 0,67 | | La cámara a las cifras de la derecha |
| 22 | 42 | 1260 | 32,05 | 0,63 (sube al 33,55: 0,68) | | La cámara vuelve a «Mapa»; el dedo espera |
| 23 | **44** | **1320** | 34,05 | 0,93 | **2.ª subida (2.ª vez)** | **«Mapa»** |
| 24 | 46 | 1380 | 36,05 | 0,90 | | «Dónde viven» |
| 25 | 48 | 1440 | 38,05 | 0,96 | | Acercamiento al centro |
| 26 | 50 | 1500 | 40,05 | 0,88 | | La cámara abre a las capas |
| 27 | **52** | **1560** | **42,05** | **1,00** | el más fuerte (2.ª vez) | **«Zonas sin evento»**. Frase 7 |
| 28 | 54 | 1620 | 44,05 | 0,84 | | La cámara a una zona |
| 29 | 56 | 1680 | 46,05 | 0,98 | | Punch a la zona |
| 30 | 58 | 1740 | 48,05 | 0,79 | | La app sube a las pestañas |
| 31 | **60** | **1800** | 50,05 | 0,93 | **clímax** | **«Eventos»**: la lista. Frase 8 |
| 32 | 62 | 1860 | 52,05 | 0,81 (redoble 62,5–63,4) | | La cámara a las columnas de la derecha |
| 33 | 64 | 1920 | 54,05 | +3,9 dB | | Toque en «Tendencia»: se reordena |
| 34 | 66 | 1980 | 56,05 | +3,2 dB | | El buscador: «Jorge Gallego» |
| 35 | 68 | 2040 | 58,05 | +5,7 dB | | La app baja a sus reuniones |
| 36 | **70** | **2100** | 60,05 | +5,3 dB | | **La casa → iris → la ficha** |
| 37 | 72 | 2160 | 62,05 | +4,0 dB | | La app baja a «Asistencia» |
| 38 | 74 | 2220 | 64,05 | +3,0 dB | | «Última reunión: … 10 personas» |
| 39 | 76 | 2280 | 66,05 | +1,2 dB | **salida** | La tendencia y la meta |
| 40 | 78 | 2340 | 68,05 | −6,3 dB (débil) | | «Quiénes vinieron» |
| 41 | 80 | 2400 | 70,05 | −0,2 dB | | Punch a «Ximena Hoyos Vélez» |
| 42 | 82 | 2460 | 72,05 | −4,5 dB | | La cámara abre a la tarjeta |
| 43 | 84 | 2520 | 74,05 | +0,3 dB | | El encuadre del final |
| 44 | **86** | **2580** | 76,05 | +1,2 dB | | **Frase 9**; la ceja se va |
| 45 | 88 | 2640 | 78,05 | −0,3 dB | | La ventana a 0,96 |
| 46 | 90 | 2700 | 80,05 | −2,6 dB | | Quieto; la subida desde el 2716 |
| — | **92** | **2760** | **82,05** | el acorde final | | **El cierre del Comercial**; campanas en el 92,38 |

(Las «dB» son la sonoridad de los primeros 120 ms del compás contra la del compás del 42,05, medidas el 2026-10-30; sustituyen a la fuerza
del detector donde este se equivocó.)

---

## 1. Los números del estilo

### 1.1 Paleta

La del clip (SPEC del clip §1.1) sin cambios: `--k-noche`, `.k-halo` (se asienta 1,08 → 1 en el 0, 180, **1080, 1560 y 2580**), `.k-puntos`
(nunca se mueven), `--k-noche-tinta` en las frases, `--k-noche-dorado` solo en la ceja, *reunión* y el botón del cierre, `--k-noche-linea`
en los anillos, la placa de `.k-datos-ejemplo` y el dip al 40 %. Los colores de la app (ámbar de las filas, verde de «Reportada», el rojo
del semáforo, el azul de las capas del mapa, el amarillo de «Espera señal») viven en las grabaciones y no se tocan.

### 1.2 Tipografía (16:9)

| Pieza | Clase | Letra | Tamaño | Reglas |
|---|---|---|---|---|
| Frase, mundo celular | `.k-titular` | Fraunces 560, `<em>` itálica 500 dorada | **88 px**, interlínea 1,04, −0,02 em | Columna izquierda, máx. **2 líneas** de ≤ 6 palabras, saltos fijados (abajo). Izquierda. Sin sombra |
| Frase, mundo computador | `.k-titular` | igual | **84 px** | **Una línea** sobre la ventana (≤ 1440 px de ancho, ≤ 34 caracteres) |
| Ceja | `.k-ceja` | Inter 700, mayúsculas, dorado | **28 px**, +0,10 em | «EVENTOS» |
| Datos de ejemplo | `.k-datos-ejemplo` | Inter 600 | **28 px**, píldora de 52 px | Abajo a la izquierda **dentro** de cada ventana, a 24 px de sus bordes (pedido del dueño para la serie) |
| Texto de la app (celular) | grabación | — | **≥ 25 px** (el cuerpo de 14 px a 1,846 ppc = 25,8) | |
| Texto de la app (computador) | grabación | — | **≥ 25 px** lo que se lee (14 px a 1,80 ppc = 25,2); en el plano E-A del mapa, 20 px las capas y la leyenda (el mapa es la imagen) | |

**Por qué 25 y no 28 como el clip:** el 28 del clip sale de verlo en un celular a 390 px de ancho; el 16:9 se ve en la página del módulo
en un computador, en YouTube y en una pantalla de presentación. La ventana del celular del kit mide 720 de ancho: a ancho completo el
cuerpo de la app queda en 25,8 px y es la misma composición que el clip.

Saltos fijados (columna de 912 px, ≈ 21 caracteres por línea a 88 px):
«Terminó la reunión. / ¿Quién vino?» · «Los de siempre, / en un toque.» · «Y queda registrada / en la iglesia» · «¿Sin señal? / La asistencia
se guarda» · «Y se envía sola / al volver la señal». En una línea (computador): «El pastor lo ve todo» · «Y dónde falta una reunión» ·
«Cuál crece y cuál necesita apoyo» · «Cada *reunión* cuenta, y cuenta bien».

### 1.3 Radios y sombras

Las del kit: `.k-ventana` radio 28 (celular) y `.k-ventana-escritorio` radio 20, anillo `rgba(234,240,255,.16)`, sombra
`0 2px 6px rgba(0,0,0,.25), 0 40px 80px -24px rgba(0,0,0,.7)`; la píldora 999 px; frases y ceja sin sombra; el cierre, el del kit.

### 1.4 Disposición: los dos mundos

| | Mundo celular (0–1079) | Mundo computador (1080–2759) |
|---|---|---|
| Ventana | `.k-ventana-16x9` **720×900** en **x 1104 · y 90** (termina en 1824 · 990) | `.k-ventana-escritorio` **1440×760** en **x 240 · y 260** (termina en 1680 · 1020) |
| Grabación ajustada | 1170×2532 → **720×1558,15** (`--f-k: 0.615385`, `--f-grab-alto: 1558.15px`) | 1920×1080 → **1440×810** (`--f-k: 0.75`, `--f-grab-alto: 810px`; el plano lleno sangra 50 px abajo) |
| Ceja | x 96 · y 372 | x 240 · y 84 |
| Frase | x 96 · y 420 · ancho 912 · hasta 2 líneas → 603 | x 240 · y 124 · ancho 1440 · 1 línea → 212 |
| Datos de ejemplo | x 1128 · y 914 (dentro de la ventana) | x 264 · y 944 (dentro de la ventana) |
| Ventana al final | — | desde el 2640: escala **0,96** con origen en el centro inferior (1680×1020 → queda en 1411×730, de y 290 a 1020) |

Los dos mundos viven en una **tira** de 3840×1080 (`#tira`): el celular en x 0–1919 y el computador en x 1920–3839. El látigo es mover la
tira (§2, 1080). La ceja y las frases **no** van en la tira: cambian de lugar con un blur swap.

### 1.5 La cámara: escalas

**ppc** = píxeles del cuadro por píxel CSS de la app. La cámara es `scale` + `x`/`y` sobre `#cam-cel` y `#cam-esc` (origen 0 0, sujeta a
los bordes de la grabación con `enc()` del clip); el `<video>` nunca se transforma.

**Celular** (grabación a 3×, 390×844 CSS):

| Nivel | × sobre el plano | ppc | Se ven (CSS) | Cuerpo 14 px → |
|---|---|---|---|---|
| G16 | 1,00 | 1,846 | 390 × 487 | 25,8 px |
| G16⁺ | 1,08 | 1,994 | 361 × 451 | 27,9 px |
| M16 | 1,40 | 2,585 | 279 × 348 | 36,2 px |
| C16 | 1,80 | 3,323 | 217 × 271 | 46,5 px (1,11 px de la grabación por px: nítido) |

**Los cuadros 0–779 reusan la cámara del clip tal cual:** los mismos objetivos (cajas CSS de su `pasos.json`) y los mismos multiplicadores
sobre el plano (G ×1,00, `fila` ×1,15, `hojaAlta` ×1,40, `telefono` ×1,80, `botones` ×1,30, `tarjeta` ×1,13…, REVIEW del clip §2 y §4.6).
Como la ventana de 16:9 tiene la misma proporción de ancho que el plano del clip (390 CSS a ×1) y es un 11 % más alta (487 contra 439 CSS),
cada encuadre muestra lo mismo a lo ancho y un poco más arriba y abajo; `enc()` lo sujeta a la grabación. Nada se recalcula a mano: cambian
las variables de §1.4.

**Computador** (grabación a 1,5×, 1280×720 CSS):

| Nivel | × sobre el plano | ppc | Se ven (CSS) | Cuerpo 14 px → | Para |
|---|---|---|---|---|---|
| E-A abierto | 1,28 | 1,44 | 1000 × 528 | 20,2 px | **solo** el mapa y la cabecera de la ficha (el título en 40 px CSS → 58 px) |
| E-G | 1,60 | 1,80 | 800 × 422 | 25,2 px | las cifras, la lista, la tarjeta |
| E-M | 2,00 | 2,25 | 640 × 338 | 31,5 px | una línea o dos (el límite: 1,5 px de la grabación por px) |

Objetivos (las cajas reales salen de cada `pasos.json`; estas son las que se piden):

| Objetivo | Grabación | Nivel | Lo que debe quedar dentro |
|---|---|---|---|
| `listo-botones` | clip | M16 | «¡Listo!», la frase con el total y los botones «Volver a la lista · Reportar la siguiente» |
| `lista-sin-red` | sin señal | G16 | «Reportar», el chip **«Sin señal»**, las pestañas y las filas de la lista con la casa |
| `reporte-sin-red` | sin señal | G16 | el título, «Pendiente», los atajos, la nota «Sin señal: la asistencia se guarda…», los pasos y «0 marcadas · Igual que la última vez» |
| `lista-marcada` | sin señal | G16 | el mismo encuadre con las filas en ámbar y «N marcadas» |
| `en-cola` | sin señal | G16 | los chips **«Sin señal» · «1 sin enviar»**, el título, **«Espera señal»**, los atajos, «Guardado en este dispositivo…» y los pasos |
| `chips` | sin señal | M16 | «Reportar», los dos chips, el título y «Espera señal» |
| `kpis-izq` | tablero | E-G | las pestañas «Resumen · Mapa · Eventos», el período y «Eventos activos · Asistencia del período · Personas por reunión · Reuniones reportadas» |
| `kpis-der` | tablero | E-G | «Al día» (con su fondo rojo y «N retrasados…»), «Tendencia ↗ ↘», «Metas logradas» |
| `vistas` | tablero | E-G | igual que `kpis-izq` (la pestaña «Mapa» a la vista) |
| `mapa` | tablero | E-A | las capas «Eventos · Dónde viven · Zonas sin evento» y el mapa |
| `centro` | tablero | E-G | el centro de la ciudad con los círculos y las zonas más densas |
| `zona` | tablero | E-G | la zona sin evento más grande (se elige en la grabación), con círculos alrededor para que se entienda «sin reunión cerca» |
| `tabla` / `tabla-der` | tablero | E-G | el encabezado y ≥ 7 filas: «Evento · Reportes · Promedio · Tendencia» / «Tendencia · Nivel · Asistencia · Reuniones · Última» |
| `buscar` | tablero | E-M | «Buscar evento o responsable» con «Jorge Gallego» escrito |
| `filas-jorge` | tablero | E-G | sus filas (las dos casas y el discipulado), con su semáforo y su tendencia |
| `ficha-cabeza` | tablero | E-A | la portada, «Casa de Paz Laureles 1», sus chips y sus acciones |
| `asistencia` | tablero | E-G | la tarjeta «Asistencia» de «Estado del reporte» a la meta |
| `ultima` | tablero | E-M | «Última reunión: 28 de oct de 2026 · 10 personas (8 por nombre · 2 visitantes)» y el promedio |
| `tendencia-meta` | tablero | E-M | «Tendencia» y «Meta: 15 personas en las últimas 8 reuniones» con su barra |
| `quienes` | tablero | E-M | «Quiénes vinieron el 28 de oct de 2026» y los nombres |
| `ximena` | tablero | E-M ×1,12 (punch) | el nombre «Ximena Hoyos Vélez» con sus vecinos |
| `cierre` | tablero | E-G ×1,07 | la tarjeta de «Última reunión» a «Quiénes vinieron»; con la ventana a 0,96 el cuerpo queda en 25,9 px |

### 1.6 Curvas y duraciones

Las del clip (SPEC del clip §1.6) para todo lo que ya existe: `entrada-palabra` (`power4.out`, 4 cuadros, blur 6 → 0, sin desplazarse,
un cuadro antes del pulso; palabras a 2 cuadros), `entrada-linea`, `salida-texto` (blur swap), `camara` (`power2.inOut`, **14** cuadros),
`punch` (9), `aterrizaje-app` (`power3.out`, 10 cuadros, 1,03 → 1,00 en el envoltorio del mundo), `iris` (`power2.out`, 5), `dedo-espera`,
`toque`, `halo` (`sine.out`, 90), `dip` (3), resortes ninguno salvo la corona, velocidad de la grabación **0,35×–3,5×**, cortes en las
esperas de `pasos.json`. Nuevas:

| Papel | Curva | Cuadros | Detalle |
|---|---|---|---|
| `latigo` | `power3.inOut` | **9** (1080–1088) | `#tira` x 0 → −1920 con el desenfoque de movimiento del render (obturador 180); el computador llega desenfocado y se asienta solo. Una sola vez |
| `ceja-cambio` | blur swap | 4 + 4 | la ceja sale 1074–1077 (blur 0 → 8) y entra en su lugar nuevo 1095–1098 (8 → 0) |
| `ventana-final` | `power2.inOut` | 15 | 2640–2654: la ventana del computador 1 → 0,96, origen centro inferior |
| `scroll-app` | — | lo que dure en la grabación (≈ 300 ms suaves) | los desplazamientos de `ver` del computador se dejan ver (1740, 1950, 2040, 2160) con la cámara quieta; los saltos de un cuadro se compensan con `comp()` como en el clip |

`data-motion-blur="on"` y `data-motion-blur-shutter="180"` en la raíz. **Nunca `filter: blur()` sobre una grabación.**

### 1.7 Sonido

| Capa | Fuente | Nivel | Regla |
|---|---|---|---|
| Música | dos `<audio>` de `product-launch-the-mountain.mp3` (§0.1) | 0,75 (carril de volumen) | la costura en el 29,945–29,975; 0,24 en el 92,4; 0 en el 94,0 |
| Sonidos de acción (kit v1.1) | `toque` (a, b = +3 %, c = −3 %, rotados), `aparicion`, `desliz`, `subida`, `confirmacion` | `data-volume="1"`; `confirmacion` del 123, 663 y **961** a 1,4 | `data-start` = cuadro del sonido / 30 − acento; el sonido cae un cuadro después de su imagen. Sin tics de tecla |
| Sonido de marca | `identidad/audio/sonido-marca.wav` | tal cual | **92,38 s** (cierre + 0,38) |
| Mezcla | — | **−16 LUFS ±1** integrados, pico real ≤ −1 dBTP | medido en el render (`hyperframes audio --json` y `ffmpeg ebur128`); si el render baja el nivel solo, los toques clave bajan a 0,9, nunca la música |

Los sonidos de 0 a 719 son los 22 del clip hasta el 663 inclusive, con sus niveles finales (REVIEW del clip §5). Desde el 720 (la tabla
completa; la toma de `toque` sigue la rotación desde la b del 661):

| Cuadro | Sonido | `data-start` | Causa |
|---|---|---|---|
| 781 | toque a | 26.033 | «Volver a la lista» |
| 811 | toque b | 27.033 | la fila de la casa |
| 841 | toque c | 28.033 | «Igual que la última vez», sin señal (golpe 1,00) |
| 843 | aparicion | 28.100 | las filas se marcan, «N marcadas» |
| 871 | desliz | 28.833 (acento 0,2) | la app baja a «Guardar asistencia» |
| 901 | toque a | 30.033 | «Guardar asistencia» (la costura de la música) |
| 904 | aparicion | 30.133 | el chip «1 sin enviar» |
| 961 | **confirmacion (1,4)** | 31.933 (acento 0,1) | los chips se van: **se envió sola** |
| 1081 | desliz | 35.833 | el látigo |
| 1321 | toque b | 44.033 | «Mapa» |
| 1381 | toque c | 46.033 | «Dónde viven» |
| 1561 | toque a | 52.033 | «Zonas sin evento» (golpe 1,00) |
| 1564 | aparicion | 52.133 | aparecen las zonas |
| 1741 | desliz | 57.833 | la app sube a las pestañas |
| 1801 | toque b | 60.033 | «Eventos» |
| 1921 | toque c | 64.033 | «Tendencia» |
| 1981 | toque a | 66.033 | el buscador |
| 2101 | toque b | 70.033 | «Casa de Paz Laureles 1» |
| 2716–2773 | subida | 90.533 (acento 1,5) | su golpe en el 2760 |
| 2771 | campanas | 92.38 | el cierre + 0,38 |

Tres `confirmacion` en todo el video (123, 663 y 961), una por prueba; el cierre lleva las campanas. Sin sonido: las
cámaras, los punch, el iris del 2100 (ya suena su toque), la escritura de «Jorge Gallego», los desplazamientos del 1950, 2040 y 2160.

### 1.8 BANNED: los valores por defecto prohibidos, con nombre

Los 20 de Membresía y los 21–26 del clip valen enteros (SPEC del clip §1.8: fundidos de 0,5 s, fade + deslizar, zoom lineal, «creeping
scale», fundido cruzado entre mundos, teléfono dibujado, texto que se mueve o «respira», logo en una esquina, brillos y partículas,
degradados nuevos y vidrio, tres tarjetas en fila / KPI / «01 / 02» / HUD dibujados por nosotros, whoosh en cada corte, velocidad fuera de
0,35×–3,5×, retocar la app, cifras sin «Datos de ejemplo», más de 3,4 s sin cambio visible, cámara y desplazamiento de la app a la vez, una
`confirmacion` por toque, recrear pantallas de la app, látigo «para animar», marcas de toque donde la grabación no tocó, frases sobre lo
que se lee de la app). Y los de este recorrido:

27. **Un segundo látigo.** Hay un solo cambio de mundo (1080). Dentro de cada mundo, las pantallas cambian por el toque (match cut o iris).
28. **Un cursor o una flecha de mouse dibujados en el computador.** El computador también lleva la marca de toque de la serie (36 → 58 px
    CSS en 0,45 s, `#015BBE` al 90 %), donde `toques[]` dice que se hizo clic. Las grabaciones van con `toque: false`.
29. **Mostrar el texto de la app a menos de 25 px** en un plano que se lee (todo menos E-A del mapa y de la cabecera de la ficha).
30. **Mover el mapa, el tablero o la ficha con la cámara a más de E-M (2,25 ppc).** Más allá la grabación se ve pixelada.
31. **Usar la costura de la música como excusa de un corte.** En el 30,0 la imagen sigue con su toque; la costura no se ve ni se oye.
32. **Gráficos propios del tablero, del mapa o de la ficha** (una flecha que señala la zona, un círculo alrededor de «10 personas», una
    cifra repetida fuera de la ventana): todo sale de la grabación y la cámara es lo único que señala.
33. **Las tres cifras del clip («7 marcadas», «Total: 10», «10 personas») dichas en una frase.** Cambian con la semilla; las dice la app.

---

## 2. Los planos, cuadro por cuadro

### 2.0 Convenciones

- Niveles y objetivos: §1.5. «Pulso»: la grilla de §0.2. Un evento «en el 840» aterriza en el cuadro 840; su sonido, en el 841.
- Grabaciones: **clip** = `clip-sitio-eventos/assets/grabaciones/grabacion.mp4` (se reusa); **sin señal** =
  `clips/recorrido-eventos-sin-senal`; **tablero** = `clips/recorrido-eventos-tablero` (§4). «grab.» = cuadro de la grabación.
- Textos de la app verificados en `frontend-v2/public/i18n/es.json` (`ev3.*`, `ev6.*`, `ev2.*`) y en los componentes: «Sin señal», «{n} sin
  enviar», «Espera señal», «Guardado en este dispositivo: se enviará solo cuando vuelva la señal.», «Sin señal: la asistencia se guarda en
  este dispositivo y se envía sola al volver la conexión.», «Volver a la lista», «Igual que la última vez», «Guardar asistencia», «Tablero
  de eventos», «Resumen · Mapa · Eventos», «Eventos activos», «Asistencia del período», «Personas por reunión», «Reuniones reportadas»,
  «Al día», «Tendencia», «Metas logradas», «Nuevos por los eventos», «Dónde viven», «Zonas sin evento», «Zonas sin evento: {n}», «Buscar
  evento o responsable», «Asistencia», «Estado del reporte», «Última reunión», «Promedio de 3 meses», «Meta», «Quiénes vinieron el {fecha}».
  Lo que cambia con la semilla lleva «(real)».

### 2.1 Tabla maestra

| Cuadro | Pulso | La app | Cámara | Texto | Sonido | Transición |
|---|---|---|---|---|---|---|
| **0–719** | | **Todo como el clip** (REVIEW del clip §2 y §3): la grabación del clip, sus 30 tramos, sus stills, sus 14 marcas de toque, su cámara con `enc()` y `comp()`, el iris del 180 | la del clip, con las variables de §1.4 | frases 1–3 y la ceja en la columna izquierda (§1.4), mismos cuadros | los 22 del clip hasta el 663 | match cut del 78, iris del 180 |
| **720** | ●● golpe 0,96 | clip, grab. 1386 → 1445 a 1× (el «¡Listo!» quieto: «Casa de Paz Laureles 1, miércoles, 28 de octubre: 10 personas.» (real)) | 720–733: `tarjeta` → **M16 `listo-botones`** | **«¿Sin señal? / La asistencia se guarda»**: ¿Sin 720 · señal? 722 · La 724 · asistencia 726 · se 728 · guarda 730 | — | |
| 776 | | | quieta | | | la marca aparece sobre «Volver a la lista» (en el punto de `toques[]` de **sin señal**, tramo `volver`) |
| **780** | ● 0,88 | **toque en «Volver a la lista»** → la lista de Reportar **sin señal**: el chip **«Sin señal»** arriba, la fila de la casa con su reunión siguiente (real) | en el corte: **G16 `lista-sin-red`** | | `toque` a 781 | **Match cut sobre el toque**: del 781 es **sin señal** (desde su primer cuadro de la lista ya puesta), `aterrizaje-app` 781–791 |
| 806 · **810** | ● | la marca aparece (806); **toque en la fila de la casa** → el reporte de la vencida desde el dispositivo: «Casa de Paz Laureles 1 · miércoles, 21 de octubre» (real), **«Pendiente»**, la nota **«Sin señal: la asistencia se guarda en este dispositivo y se envía sola al volver la conexión.»**, «0 marcadas · Igual que la última vez» | en el corte: **G16 `reporte-sin-red`** | | `toque` b 811 | match cut, `aterrizaje-app` 813–823 |
| 836 · **840** | **●●● 1,00** | la marca (836); **toque en «Igual que la última vez»** → las filas se marcan a la vez, en ámbar, **«7 marcadas» (real)**, sin señal | quieta (`lista-marcada` = el mismo encuadre) | | `toque` c 841 · `aparicion` 843 | |
| **870** | ● | la app baja hasta «Guardar asistencia» (el `ver` de la grabación) | **quieta** | | `desliz` 871 | |
| 896 · **900** | **●●● la costura** | la marca (896); **toque en «Guardar asistencia»** (el ícono del reloj) → paso ②: los chips **«Sin señal» · «1 sin enviar»**, **«Espera señal»**, «Guardado en este dispositivo: se enviará solo cuando vuelva la señal.», la nota «El reporte necesita señal…», «Lo envío después» | 900–913 → **G16 `en-cola`** | | `toque` a 901 · `aparicion` 904 | si la app salta arriba al cambiar de paso, el corte cae en el salto (es su pantalla nueva) |
| **930** | ● | quieta | 930–943 → **M16 `chips`** | | — | |
| 956–960 | | | | la frase 4 sale (blur swap) | | |
| **960** | **●●● 0,92** | **vuelve la señal:** el chip «1 sin enviar» y el chip «Sin señal» **se van**; «Espera señal» cambia a su estado nuevo (real) y la nota «Guardado en este dispositivo…» se va. El corte cae en la espera: el primer cuadro sin chips es el 960 | quieta | **«Y se envía sola / al volver la señal»**: Y 960 · se 962 · envía 964 · sola 966 · al 968 · volver 970 · la 972 · señal 974 | **`confirmacion` (1,4) 961** | |
| **990** | ● | quieta | 990–1003 → **G16 `en-cola`** (el mismo encuadre, ya sin chips) | | — | |
| 1004–1071 | | quieta (sin señal: la grabación sigue a 1×) | quieta | frase 5 quieta | — | |
| 1072–1077 | | | | la frase 5 sale 1072–1076; la ceja sale 1074–1077 | | |
| **1080** | ●● respiro | **tablero**, tramo `tablero`: el «Tablero de eventos» de la cuenta 101 apenas cargado, **las cifras contando desde 0** (`app-cifra-animada`, 0,6 s: 1081–1099) | **E-G `kpis-izq`** desde el primer cuadro | — | `desliz` 1081 | **El látigo**: `#tira` 0 → −1920, 1080–1088 (`latigo`); halo 1,08 → 1 (1080–1170) |
| **1095** | ● | quieta | quieta | **«EVENTOS»** entra en su lugar del computador (1095–1098) | — | |
| **1140** | ● | quieta | quieta | **«El pastor lo ve todo»**: El 1140 · pastor 1142 · lo 1144 · ve 1146 · todo 1148 | — | |
| **1200** | ● | quieta | 1200–1213 → **E-G `kpis-der`**: «Al día **28 / 69** (real)» en su fondo rojo con «N retrasados · N sin reportar…», «Tendencia ↗ N ↘ N» (real), «Metas logradas» | | — | |
| **1260** | ● | quieta | 1260–1273 → **E-G `vistas`** | | — | |
| 1305 | | | | | | **`dedo-espera`**: la marca se posa sobre «Mapa» y espera |
| 1316–1320 | | | | la frase 6 sale | | |
| **1320** | **●●● 0,93** | **toque en «Mapa»** → el mapa de la ciudad con los eventos en círculos (agrupados) y la leyenda; las capas «Eventos · Dónde viven · Zonas sin evento» arriba. El corte salta la carga de las teselas y el desplazamiento del `ver` de la grabación | en el corte: **E-A `mapa`** | | `toque` b 1321 | match cut, `aterrizaje-app` 1322–1332 |
| 1376 · **1380** | ● | la marca; **toque en «Dónde viven»** → las zonas de ~1 km con gente de la iglesia, en azul que se aclara (el corte cae en la espera de la capa) | quieta | | `toque` c 1381 | |
| **1440** | ● | quieta | 1440–1453 → **E-G `centro`** | | — | |
| **1500** | ● | quieta | 1500–1513 → **E-A `mapa`** | | — | |
| 1556 · **1560** | **●●● 1,00** | la marca; **toque en «Zonas sin evento»** → aparecen las zonas con al menos 10 personas y ningún evento a menos de 2 km; la leyenda dice **«Zonas sin evento: N» (real)** | quieta | **«Y dónde falta una reunión»**: Y 1560 · dónde 1562 · falta 1564 · una 1566 · reunión 1568 | `toque` a 1561 · `aparicion` 1564 | halo 1,08 → 1 (1560–1650) |
| **1620** | ● | quieta | 1620–1633 → **E-G `zona`** | | — | |
| **1680** | ● 0,98 | quieta | **punch** 1680–1688 → `zona` ×1,12 (2,02 ppc) | | — | |
| **1740** | ● | la app **sube a las pestañas** (el `ver` suave de la grabación, ≈ 300 ms) | **quieta** durante el desplazamiento; 1755–1768 → **E-G `tabla`** (la caja de las pestañas) | | `desliz` 1741 | |
| 1796–1800 | | | | la frase 7 sale | | la marca aparece sobre «Eventos» (1796) |
| **1800** | **●●● clímax** | **toque en «Eventos»** → la lista: una fila por evento con su semáforo («Sin reportar», «Retrasado» en rojo arriba: el orden de la app es lo más urgente primero), su promedio, su tendencia (↗ +N % / ↘ −N %, real) y su meta | en el corte: **E-G `tabla`** | **«Cuál crece y cuál necesita apoyo»**: Cuál 1800 · crece 1802 · y 1804 · cuál 1806 · necesita 1808 · apoyo 1810 | `toque` b 1801 | match cut, `aterrizaje-app` 1802–1812 |
| **1860** | ● | quieta | 1860–1873 → **E-G `tabla-der`** | | — | |
| 1875–1902 | | (el redoble de la pista: nada cae aquí) | quieta | | | |
| 1916 · **1920** | ● | la marca; **toque en «Tendencia»** (el encabezado) → la lista se reordena por tendencia | quieta | | `toque` c 1921 | |
| **1950** | ● | la app sube al buscador (el `ver` de la grabación) | **quieta** | | — | |
| 1965–1978 | | quieta | → **E-M `buscar`** | | — | |
| 1976 · **1980** | ● | la marca; **toque en «Buscar evento o responsable»**; **1983–2010 se escribe «Jorge Gallego»** (13 teclas a 1×) | quieta | | `toque` a 1981 | |
| **2025** | ● | la lista se filtra (el corte cae en la espera de 500 ms del buscador y la carga): quedan las reuniones de Jorge (real) | quieta | | — | |
| **2040** | ● | la app baja a sus filas (el `ver` de la grabación) | **quieta** | | — | |
| 2055–2068 | | quieta | → **E-G `filas-jorge`** | | — | |
| 2070–2074 | | | | la frase 8 sale | | |
| 2096 · **2100** | **●●● 60,05** | la marca; **toque en «Casa de Paz Laureles 1»** → **su ficha**: la portada, el nombre, «Casa de paz», el estado del reporte (real), «Reportar» | 2100: **E-A `ficha-cabeza`** | | `toque` b 2101 | **Iris desde el toque**, 2100–2105 (still del 2099 debajo) |
| **2160** | ● | la app baja a la tarjeta «Asistencia» (el `ver` de la grabación) | **quieta**; 2175–2188 → **E-G `asistencia`** | | — | |
| **2220** | ● | quieta | 2220–2233 → **E-M `ultima`**: **«28 de oct de 2026 · 10 personas (8 por nombre · 2 visitantes)» (real)** | | — | |
| **2280** | ● salida | quieta | 2280–2293 → **E-M `tendencia-meta`** (real: la tendencia y la barra de la meta) | | — | |
| **2340** | ● | quieta | 2340–2353 → **E-M `quienes`**: «Quiénes vinieron el 28 de oct de 2026» y los nombres | | — | |
| **2400** | ● | quieta | **punch** 2400–2408 → `ximena` ×1,12: **«Ximena Hoyos Vélez»** | | — | |
| **2460** | ● | quieta | 2460–2473 → **E-G `asistencia`** | | — | |
| **2520** | ● | quieta | 2520–2533 → **E-G `cierre`** (×1,07) | | — | |
| **2580** | **●●** | quieta | quieta | **«Cada *reunión* cuenta, y cuenta bien»**: Cada 2580 · *reunión* 2582 · cuenta, 2584 · y 2586 · cuenta 2588 · bien 2590. **La ceja sale 2580–2583** | — | halo 1,08 → 1 (2580–2670) |
| **2640** | ● | quieta | quieta | frase 9 quieta | — | **`ventana-final`** 2640–2654: 1 → 0,96 |
| 2655–2756 | | quieta (la ficha real) | quieta | frase 9 quieta (3,4 s) | **`subida`** 2716–2773 | |
| 2757–2759 | | | | | | **dip** al 40 %, 3 cuadros |
| **2760** | **el acorde final** | — | — | — | música 0,75 → 0,24 (2772) → 0 (2820) | **corte al cierre**: `identidad/cierre-comercial.html`, `{"publico":"iglesia","llamado":"prueba","contacto":"sitio","fondo":"noche","idioma":"es"}` |
| 2771 | | la corona se levanta (0–1,0 s del cierre) | | «Kingdom», la ceja «La app para iglesias» y «Kingdom es para *toda la iglesia*» (1,1–2,3 s); el botón «Prueba gratis 30 días» y `kingdom-sitio.web.app` (2,3–2,9 s) | **campanas 92,38** | |
| **2909** | | último cuadro: el cierre completo | | | silencio de música desde el 2820 | fin |

### 2.2 Los planos

#### P1–P5 · La historia del clip — cuadros 0–719

Sin cambios de tiempo ni de contenido: SPEC del clip §2.2 (P1–P5) y su REVIEW §2–§4 (los tramos reales de la grabación, las compensaciones
de los saltos del 525, 615 y 645, los stills `still-364.png` y `still-1027.png`, las marcas que se van con el corte). Lo único que cambia
es la disposición (§1.4): la ventana del celular a la derecha y la ceja y las frases en la columna izquierda. La ceja «EVENTOS» entra en el
195 en su lugar del celular (x 96 · y 372). La frase 3 sale en el 597–601 como en el clip; entre el 601 y el 720 no hay frase (las dos
pruebas las da la app).

#### P6 · «¿Sin señal?» — cuadros 720–1079 (compases 13–18)

- **Grabación:** clip grab. 1386–1445 (720–779); **sin señal**, tramos `volver` (desde la lista ya puesta), `casa`, `igual`, `abajo`,
  `guardar` y `senal` (781–1079), a 1× salvo los recortes en las esperas.
- **Por qué funciona la costura del 780:** la escena **sin señal** rehace el mismo reporte del clip (mismos pasos, misma semilla) para
  llegar al mismo «¡Listo!» con el botón «Volver a la lista» en el mismo lugar, así que la marca que dibuja el montaje (de `toques[]` de
  **sin señal**) cae sobre el botón del cuadro del clip. Del 781 en adelante todo es **sin señal**; ningún cuadro de su «¡Listo!» se usa.
- **Cámara:** 720–733 (M16 `listo-botones`), los cortes del 781 y del 813 (cambian de encuadre en el corte), 900–913, 930–943, 990–1003.
  Quieta en 840–899 (la app marca y baja) y en el 960 (los chips se van).
- **Texto:** frase 4 720–956; frase 5 960–1076. La ceja se queda hasta el 1077.
- **Válvula si la lista sin señal tarda** (el chip «Sin señal» aparece cuando la primera petición falla): el corte del 781 cae en el primer
  cuadro en que el chip ya está; nada cambia en el clip.
- **Válvula si la señal tarda en enviar** (`sinRed: false` → el envío → los chips se van): se corta la espera; el primer cuadro sin chips
  es el 960.

#### P7 · El látigo y «El pastor lo ve todo» — cuadros 1080–1319 (compases 19–22)

- **Grabación:** **tablero**, tramo `tablero`: desde el primer cuadro del tablero ya dibujado con las cifras en 0 (el cuadro siguiente al
  «Cargando…»). Las cifras cuentan 0,6 s (18 cuadros) y quedan quietas; la grabación sigue a 1× (es una pantalla quieta: se puede usar
  cualquier tramo de su espera).
- **El látigo:** `#tira` (los dos mundos lado a lado) se mueve −1920 px en 9 cuadros (`power3.inOut`); el desenfoque es el del render, horizontal.
  La frase 5 y la ceja ya salieron (1072–1077): el látigo cruza la noche limpia. El computador llega con la cámara ya en `kpis-izq`.
- **Cámara:** quieta hasta el 1199; 1200–1213 y 1260–1273.
- **Texto:** la ceja vuelve (1095), frase 6 1140–1320.
- **Sonido:** `desliz` (1081).

#### P8 · «Y dónde falta una reunión» — cuadros 1320–1799 (compases 23–30)

- **Grabación:** **tablero**, tramo `mapa`: el mapa ya con teselas (se corta la carga), las dos capas encendidas cada una en su toque y
  cada una ya dibujada en el cuadro siguiente al pulso (el corte cae en su espera).
- **Cámara:** el corte del 1322 (E-A), 1440–1453, 1500–1513, 1620–1633, el punch 1680–1688, 1755–1768. Quieta durante el desplazamiento
  del 1740.
- **Texto:** frase 7 1560–1800 (en el segundo golpe más fuerte).
- **El objetivo `zona`** se elige al construir sobre el cuadro 1600: la zona sin evento (relleno de `ev6-zonas`) con más celdas juntas y
  al menos dos círculos de eventos a la vista alrededor. Se anota en el REVIEW.
- **Plan B (si «Zonas sin evento: 0»):** la escena tiene el paso opcional de §4.3 (5 personas); la toma de 1560 usa ese tramo.

#### P9 · «Cuál crece y cuál necesita apoyo» — cuadros 1800–2099 (compases 31–35)

- **Grabación:** **tablero**, tramo `tabla`.
- **Cámara:** el corte del 1802, 1860–1873, 1965–1978, 2055–2068; quieta en los desplazamientos del 1950 y 2040 y mientras se escribe
  (1983–2010).
- **Texto:** frase 8 1800–2074.
- **Válvula si el clímax va atropellado** (cinco cosas en diez segundos): se quita el reordenamiento del 1920 y la cámara se queda en
  `tabla-der` hasta el 1950.

#### P10 · La ficha de la casa — cuadros 2100–2579 (compases 36–43)

- **Grabación:** **tablero**, tramo `ficha`: el clic, la ficha, el `ver` suave a «Asistencia» y 16 s quietos.
- **El iris** desde el enlace de la casa (2100–2105) sobre un still del cuadro 2099 (el de la lista filtrada), como el del clip.
- **Cámara:** un movimiento por compás: 2175 (tras el desplazamiento del 2160), 2220, 2280, 2340, el punch del 2400, 2460, 2520.
- **Texto:** ninguno: la ficha dice «10 personas» y «Ximena Hoyos Vélez» con sus propias letras. Es el pago de las frases 2 y 3 del clip.
- **Si la tarjeta muestra «Las personas de esta reunión solo las ve…»** (`ficha-asistentes-reservado`, el administrador no debería verlo):
  `quienes` y `ximena` se cambian por un punch a `ultima` en el 2340 y el 2400.

#### P11 · «Cada reunión cuenta, y cuenta bien» — cuadros 2580–2759 (compases 44–46)

- **Grabación:** **tablero**, la ficha quieta.
- **Cámara:** quieta (ya está en `cierre` desde el 2533). La ventana a 0,96 en 2640–2654; el cuerpo de la app sigue en ≥ 25 px.
- **Texto:** frase 9 2580–2759 (6 s; quieta 3,4 s después del último movimiento). La ceja sale 2580–2583.
- **Sonido:** `subida` 2716–2773. **Transición:** dip 2757–2759 y corte duro al 2760.

#### P12 · El cierre del Comercial — cuadros 2760–2909

`identidad/cierre-comercial.html` (5 s, 1920×1080) con `{"publico":"iglesia","llamado":"prueba","contacto":"sitio","fondo":"noche","idioma":"es"}`;
el sonido de marca lo pone el host en el **92,38**. La música es el acorde final de la pista, bajado a −10 dB en el 2772 y apagado en el
2820. El cierre es el cuadro final del video (2,9–5,0 s quieto).

---

## 3. Lo que se reusa del clip

| Qué | De dónde | Para |
|---|---|---|
| `grabacion.mp4` (1170×2532, 30 fps, 53,1 s) y `pasos.json` | `clip-sitio-eventos/assets/grabaciones/` | 0–779: **grab. 23–1445** con exactamente los tramos, velocidades y cortes del REVIEW del clip §2 (0–719), más grab. **1386–1445** a 1× (720–779) |
| `still-364.png`, `still-1027.png` | `clip-sitio-eventos/assets/stills/` | el iris del 180 y la barra del 602–609 |
| `toque-b.wav`, `toque-c.wav` | `clip-sitio-eventos/assets/audio/` | las tomas de `toque` |
| El montaje de 0–719 | `clip-sitio-eventos/index.html` | se copia: los 30 tramos de video, las 14 marcas, la cámara (`enc()`, `comp()`, los objetivos y multiplicadores) y los 22 sonidos hasta el 663; cambian `--f-*`, `window.KD` (ventana 720×900 en 1104·90) y la posición de la ceja, las frases y la píldora (§1.4) |
| `frase-1.html` … `frase-3.html`, `ceja.html`, `fondo.html` | `clip-sitio-eventos/compositions/` | se copian y se pasan a 1920×1080 con la columna de §1.4 (88 px; `.k-titular` en vez de `.k-feed-frase`) |

Todo lo demás es nuevo: `frase-4.html` … `frase-9.html`, el látigo, la ventana del computador y su cámara, y las grabaciones de §4.
El proyecto se arma como el clip: `BRIEF.md` (con `tipo: comercial`), `hyperframes.json`, `package.json` con `"kit"` y `"musica"`, y
`frame.md` copiado de `identidad/frame-comercial.md` antes del flujo de HyperFrames (`README.md` del directorio).

---

## 4. Las grabaciones nuevas

### 4.1 Cómo se graban

```bash
cd F:/Proyectos/KingdomApp/tools/ayuda
node capturar.mjs clips/recorrido-eventos-sin-senal --idioma es --modo video   # celular 390×844 a 3× → 1170×2532
node capturar.mjs clips/recorrido-eventos-tablero   --idioma es --modo video   # computador 1280×720 a 1,5× → 1920×1080
# → salida/video/es/clips/<escena>/grabacion.mp4 + pasos.json (inicio/fin, tramo, accion, toques[], teclas[], caja, caja_video)
```

- Las dos sobre **la misma carga de Kingdom Demo que la grabación del clip** (la reunión pendiente del miércoles **2026-10-28**): la `ref`
  `mismaSemilla` lo exige y la escena se niega si no.
- **Con internet** (las teselas del mapa son de OpenFreeMap) y con la API local; `toque: false` (el montaje dibuja la marca).
- Selectores verificados el 2026-10-30 en `frontend-v2/src/app/pages/eventos/` (`reporte.component.ts`, `reportar.page.ts`,
  `cola-indicador.component.ts`, `reporte-asistencia.component.ts`, `reporte-persona-nueva.component.ts`, `tablero.page.ts`,
  `tablero-mapa.component.ts`, `tablero-tabla.component.ts`, `tablero-filtros.component.ts`, `evento.page.ts`) y en las escenas de la
  ayuda que ya los usan (`eventos/reportar-una-reunion.mjs` para el camino sin señal y `#ev-cola-pendientes`, `eventos/tablero-y-mapa.mjs`,
  `eventos/ver-eventos.mjs`, `clips/eventos-casa-de-paz.mjs`).
- `ver` con `bloque: 'nearest'` solo toma la caja (no desplaza si el elemento ya se ve): así se anotan objetivos sin mover la pantalla.

### 4.2 `tools/ayuda/escenas/clips/recorrido-eventos-sin-senal.mjs`

```js
// Grabación para el RECORRIDO del sitio «Eventos» (LegacyHyperframes/videos/kingdomapp/recorrido-eventos/SPEC.md §4.2), cuadros 780–1079.
// NO es una escena de un artículo de la ayuda: no se publica ni entra en la frescura. Una escena de CELULAR (390×844 a 3x = 1170×2532, 30 cps)
// grabada SIN el círculo del toque (`toque: false`): el montaje dibuja el suyo sobre toques[] y las cajas de pasos.json.
//   node capturar.mjs clips/recorrido-eventos-sin-senal --idioma es --modo video
// Tramos: previo (rehace el reporte del clip, no se usa salvo para que «Volver a la lista» quede donde estaba en el clip) · volver · casa ·
// igual · abajo · guardar · senal. Todo con la cuenta 103 (el servidor Jorge Gallego Gil), responsable de la primera casa de paz de la semilla.
// Datos ficticios de Kingdom Demo: «Ximena Hoyos Vélez» y el teléfono 5550198765 no existen en la demo.
const CASA = `(SELECT r.id_evento FROM ev_responsables r JOIN kd_usuario_sedes us ON us.id_persona = r.id_persona AND us.id_sede = r.id_sede
               WHERE us.id_usuario = 103 ORDER BY r.id_evento LIMIT 1)`;
// Las reuniones esperadas de esa casa que siguen pendientes, de la más reciente a la más vieja (la semilla deja tres).
const PENDIENTE = n => `SELECT fecha FROM ev_reuniones WHERE id_evento = ${CASA} AND estado = 'pendiente' AND esperada = 1 ORDER BY fecha DESC LIMIT 1 OFFSET ${n}`;

export default {
  articulo: 'clips/recorrido-eventos-sin-senal',
  movil: true,
  toque: false,
  pantallas: [
    'frontend-v2/src/app/pages/eventos/reportar.page.ts',
    'frontend-v2/src/app/pages/eventos/reportar-lista.component.ts',
    'frontend-v2/src/app/pages/eventos/eventos-cabecera.component.ts',
    'frontend-v2/src/app/pages/eventos/cola-indicador.component.ts',
    'frontend-v2/src/app/pages/eventos/reporte.component.ts',
    'frontend-v2/src/app/pages/eventos/reporte-asistencia.component.ts',
    'frontend-v2/src/app/pages/eventos/reporte-persona-nueva.component.ts',
    'frontend-v2/src/app/pages/membresia/formulario-responder.component.ts',
  ],
  refs: {
    casa: `SELECT ${CASA}`,
    pendiente: PENDIENTE(0),
    // La misma carga de Kingdom Demo que la grabación del clip (su «¡Listo!» dice «miércoles, 28 de octubre»): si no, se niega.
    mismaSemilla: `SELECT IF((${PENDIENTE(0)}) = '2026-10-28', 1, NULL)`,
    // La reunión que se reporta sin señal: la siguiente pendiente (la que la lista abre después de reportar la del 28).
    vencida: PENDIENTE(1),
    // «Igual que la última vez» marca a la gente de la última reunión con asistencia: ≥ 3, como en el clip (allí marcó 7).
    ultima: `SELECT IF(COUNT(*) >= 3, COUNT(*), NULL) FROM ev_asistencias a
              WHERE a.id_reunion = (SELECT id FROM ev_reuniones WHERE id_evento = ${CASA} AND estado IN ('reportada', 'parcial') AND nombres > 0
                                    ORDER BY fecha DESC LIMIT 1)`,
  },
  // Sin señal, el navegador anota cada petición que no pudo salir (la app la guarda en el dispositivo a propósito).
  consolaEsperada: ['ERR_INTERNET_DISCONNECTED'],
  pasos: [
    // 1-14. previo: el mismo reporte del clip, con señal, hasta el «¡Listo!» en el mismo lugar de la pantalla (no se usa en el video).
    { tramo: 'previo', como: 103, ir: '/servir/eventos/reportar?evento={@casa}&fecha={@pendiente}',
      espera: '#reporte[data-evento="{@casa}"] #asis-lista li.fila', pausa: 1500 },
    { clic: '#btn-igual-ultima', espera: '#asis-lista li.fila.si', pausa: 600 },
    { clic: '#btn-persona-nueva', espera: '#nueva-nombres', pausa: 600 },
    { escribir: { en: '#nueva-nombres', texto: 'Ximena' }, pausa: 200 },
    { escribir: { en: '#nueva-apellidos', texto: 'Hoyos Vélez' }, pausa: 200 },
    { escribir: { en: '#nueva-telefono', texto: '5550198765' }, pausa: 200 },
    { clic: '#nueva-genero-F', pausa: 300 },
    { clic: '#btn-agregar-nueva', oculto: 'mat-dialog-container' },
    { espera: '#asis-lista li.fila[data-nueva]', pausa: 300 },
    { clic: '#btn-visitantes-mas', pausa: 300 },
    { clic: '#btn-visitantes-mas', pausa: 300 },
    { clic: '#btn-guardar-asistencia', espera: '#reporte-formulario' },
    { marcar: '[data-pregunta="como"] mat-radio-button[data-opcion="muy_bien"]', pausa: 300 },
    { escribir: { en: '[data-pregunta="tema"] input, [data-pregunta="tema"] textarea', texto: 'El perdón' }, pausa: 300 },
    { clic: '#btn-enviar-reporte', espera: '#reporte-listo' },
    // 15. El «¡Listo!» centrado como en el clip (su grab. 1386–1445 sale del mismo `ver`).
    { ver: '#reporte-listo', pausa: 2500 },
    { ver: '#btn-volver', bloque: 'nearest', pausa: 300 },   // solo la caja de «Volver a la lista» (la marca del 776–780)
    // 16. Se va la señal (no se ve: el navegador queda sin red).
    { sinRed: true, pausa: 600 },
    // 17. «Volver a la lista» (el toque del 780): la lista desde el dispositivo, con el chip «Sin señal» arriba.
    { tramo: 'volver', clic: '#btn-volver', espera: 'app-ev-reportar-lista button.fila[data-evento="{@casa}"]' },
    { espera: '#ev-chip-sin-red', pausa: 1500 },
    // 18. La casa (el toque del 810): su reunión siguiente, abierta desde el dispositivo, con la nota «Sin señal: …».
    { tramo: 'casa', clic: 'app-ev-reportar-lista button.fila[data-evento="{@casa}"]',
      espera: '#reporte[data-fecha="{@vencida}"] #reporte-sin-red', pausa: 1500 },
    // 19. «Igual que la última vez» sin señal (el toque del 840, el golpe más fuerte): las filas se marcan a la vez.
    { tramo: 'igual', clic: '#btn-igual-ultima', espera: '#asis-lista li.fila.si', pausa: 1500 },
    // 20. La app baja a «Guardar asistencia» (el desliz del 870).
    { tramo: 'abajo', ver: '#btn-guardar-asistencia', pausa: 1200 },
    // 21. «Guardar asistencia» (el toque del 900): queda en el dispositivo: «Espera señal», «1 sin enviar», la nota de la cola.
    { tramo: 'guardar', clic: '#btn-guardar-asistencia', espera: '#reporte-en-cola', pausa: 2500 },
    { ver: '#ev-cola-pendientes', bloque: 'nearest', pausa: 300 },   // solo la caja de los chips (objetivo `chips` del 930)
    // 22. Vuelve la señal (el 960): la cola se envía sola y los chips se van. Quieto 3,5 s para el final del plano.
    { tramo: 'senal', sinRed: false, oculto: '#ev-cola-pendientes', pausa: 3500 },
  ],
};
```

Notas: el camino sin señal (`sinRed`, `#ev-chip-sin-red`, `#reporte-en-cola`, `#ev-cola-pendientes`, la fila de la lista) es el que ya
graba la escena de la ayuda `eventos/reportar-una-reunion.mjs`; «Reportar la siguiente» **no** sirve aquí porque abre otro evento (la
siguiente fila de la lista), no la reunión vencida de la misma casa. Tiempo ≈ 45 s de grabación para 10 s de video.

### 4.3 `tools/ayuda/escenas/clips/recorrido-eventos-tablero.mjs`

```js
// Grabación para el RECORRIDO del sitio «Eventos» (LegacyHyperframes/videos/kingdomapp/recorrido-eventos/SPEC.md §4.3), cuadros 1080–2759.
// NO es una escena de un artículo de la ayuda: no se publica ni entra en la frescura. Una escena de COMPUTADOR (1280×720 a 1,5x = 1920×1080,
// 30 cps) grabada SIN la flecha ni la onda del clic (`toque: false`): el montaje dibuja su marca sobre toques[] y las cajas de pasos.json.
//   node capturar.mjs clips/recorrido-eventos-tablero --idioma es --modo video
// Tramos: previo (Jorge, 103, rehace el reporte del clip para que la ficha diga «10 personas» y nombre a Ximena; no se usa en el video) ·
// tablero · mapa · tabla · ficha (el pastor, 101: Andrés Felipe Restrepo Gómez, administrador de Kingdom Demo).
// Datos ficticios de Kingdom Demo: «Ximena Hoyos Vélez» y el teléfono 5550198765 no existen en la demo.
const CASA = `(SELECT r.id_evento FROM ev_responsables r JOIN kd_usuario_sedes us ON us.id_persona = r.id_persona AND us.id_sede = r.id_sede
               WHERE us.id_usuario = 103 ORDER BY r.id_evento LIMIT 1)`;
const PENDIENTE = n => `SELECT fecha FROM ev_reuniones WHERE id_evento = ${CASA} AND estado = 'pendiente' AND esperada = 1 ORDER BY fecha DESC LIMIT 1 OFFSET ${n}`;

export default {
  articulo: 'clips/recorrido-eventos-tablero',
  toque: false,
  pantallas: [
    'frontend-v2/src/app/pages/eventos/reportar.page.ts',
    'frontend-v2/src/app/pages/eventos/reporte.component.ts',
    'frontend-v2/src/app/pages/eventos/reporte-asistencia.component.ts',
    'frontend-v2/src/app/pages/eventos/reporte-persona-nueva.component.ts',
    'frontend-v2/src/app/pages/eventos/tablero.page.ts',
    'frontend-v2/src/app/pages/eventos/tablero-filtros.component.ts',
    'frontend-v2/src/app/pages/eventos/tablero-resumen.component.ts',
    'frontend-v2/src/app/pages/eventos/tablero-mapa.component.ts',
    'frontend-v2/src/app/pages/eventos/tablero-tabla.component.ts',
    'frontend-v2/src/app/pages/eventos/evento.page.ts',
  ],
  refs: {
    casa: `SELECT ${CASA}`,
    pendiente: PENDIENTE(0),
    mismaSemilla: `SELECT IF((${PENDIENTE(0)}) = '2026-10-28', 1, NULL)`,
    ultima: `SELECT IF(COUNT(*) >= 3, COUNT(*), NULL) FROM ev_asistencias a
              WHERE a.id_reunion = (SELECT id FROM ev_reuniones WHERE id_evento = ${CASA} AND estado IN ('reportada', 'parcial') AND nombres > 0
                                    ORDER BY fecha DESC LIMIT 1)`,
  },
  pasos: [
    // 1-14. previo: Jorge reporta la reunión del 28 igual que en el clip (7 + Ximena + 2 visitantes = 10 personas). No se usa en el video.
    { tramo: 'previo', como: 103, ir: '/servir/eventos/reportar?evento={@casa}&fecha={@pendiente}',
      espera: '#reporte[data-evento="{@casa}"] #asis-lista li.fila', pausa: 600 },
    { clic: '#btn-igual-ultima', espera: '#asis-lista li.fila.si', pausa: 300 },
    { clic: '#btn-persona-nueva', espera: '#nueva-nombres', pausa: 300 },
    { escribir: { en: '#nueva-nombres', texto: 'Ximena' }, pausa: 200 },
    { escribir: { en: '#nueva-apellidos', texto: 'Hoyos Vélez' }, pausa: 200 },
    { escribir: { en: '#nueva-telefono', texto: '5550198765' }, pausa: 200 },
    { clic: '#nueva-genero-F', pausa: 300 },
    { clic: '#btn-agregar-nueva', oculto: 'mat-dialog-container' },
    { espera: '#asis-lista li.fila[data-nueva]', pausa: 300 },
    { clic: '#btn-visitantes-mas', pausa: 300 },
    { clic: '#btn-visitantes-mas', pausa: 300 },
    { clic: '#btn-guardar-asistencia', espera: '#reporte-formulario' },
    { marcar: '[data-pregunta="como"] mat-radio-button[data-opcion="muy_bien"]', pausa: 300 },
    { escribir: { en: '[data-pregunta="tema"] input, [data-pregunta="tema"] textarea', texto: 'El perdón' }, pausa: 300 },
    { clic: '#btn-enviar-reporte', espera: '#reporte-listo', pausa: 600 },
    // 15. El lunes: el pastor (101) abre el tablero (el látigo del 1080). Las cifras cuentan 0,6 s desde 0 y quedan quietas.
    { tramo: 'tablero', como: 101, ir: '/servir/eventos/tablero', espera: '#tablero-kpis [data-kpi="al_dia"]', pausa: 3500 },
    { ver: '#tablero-kpis', bloque: 'nearest', pausa: 200 },                  // caja de las cifras (kpis-izq / kpis-der)
    { ver: '#tablero-kpis [data-kpi="al_dia"]', bloque: 'nearest', pausa: 200 },
    { ver: '#vista-mapa', bloque: 'nearest', pausa: 1200 },                   // caja de «Mapa» (la marca que espera desde el 1305)
    // 16-18. «Mapa» (el 1320), «Dónde viven» (el 1380) y «Zonas sin evento» (el 1560, el golpe más fuerte).
    { tramo: 'mapa', clic: '#vista-mapa', espera: '#mapa-leyenda', pausa: 3000 },   // las teselas de OpenFreeMap tienen tiempo de llegar
    { ver: 'mat-chip-listbox.capas', bloque: 'start', pausa: 2000 },
    { clic: '#capa-personas', espera: '#mapa-leyenda .escala', pausa: 3000 },
    { clic: '#capa-zonas', espera: '#mapa-leyenda .zona-muestra', pausa: 4000 },
    // Plan B (solo si la leyenda dice «Zonas sin evento: 0»): quitar el comentario de la línea siguiente y grabar otra vez.
    // { elegir: { en: '#zonas-minimo', opcion: '5 personas' }, pausa: 3000 },
    // 19-22. «Eventos» (el 1800): la lista; «Tendencia» (el 1920); el buscador con «Jorge Gallego» (el 1980); sus filas (el 2040).
    { ver: '#vista-eventos', pausa: 1500 },                                  // la app sube a las pestañas (el 1740), desplazamiento suave
    { tramo: 'tabla', clic: '#vista-eventos', espera: '#tablero-tabla tbody tr', pausa: 2000 },
    { ver: '#tablero-tabla thead', bloque: 'nearest', pausa: 200 },          // caja del encabezado (tabla / tabla-der)
    { clic: '#orden-tendencia', pausa: 2000 },
    { ver: '#tablero-buscar', pausa: 1500 },                                 // la app sube al buscador (el 1950)
    { escribir: { en: '#tablero-buscar', texto: 'Jorge Gallego' }, pausa: 3000 },   // 500 ms del buscador + la carga
    { ver: '#tablero-tabla tr[data-evento="{@casa}"]', pausa: 1500 },        // la app baja a sus filas (el 2040)
    // 23-24. La casa (el 2100, iris) → su ficha; la app baja a «Asistencia» (el 2160) y queda quieta 16 s (2175–2759).
    { tramo: 'ficha', clic: '#tablero-tabla tr[data-evento="{@casa}"] td.evento a', espera: '#ficha-asistencia', pausa: 2000 },
    { ver: '#ficha-asistencia', bloque: 'start', pausa: 16000 },
    // Solo las cajas de los objetivos de la cámara (no desplazan: ya se ven).
    { ver: '#ficha-ultima', bloque: 'nearest', pausa: 200 },
    { ver: '#ficha-meta', bloque: 'nearest', pausa: 200 },
    { ver: '#ficha-asistentes, #ficha-asistentes-reservado', bloque: 'nearest', pausa: 200 },
  ],
};
```

Notas:

- El paso 15 entra con `como: 101` a mitad de la grabación (la herramienta lo permite en cualquier paso); el cambio de cuenta, el
  «Cargando…» y la primera pintura del tablero se cortan: el video arranca en el primer cuadro con las cifras en 0.
- `#ficha-meta` existe porque la categoría Casa de Paz tiene meta (15 personas en 8 reuniones, `_demo_eventos.php`). Si la ficha mostrara
  `#ficha-asistentes-reservado`, el último paso no falla (lleva los dos selectores) y entra la válvula de P10.
- Tiempo ≈ 2 min 10 s de grabación (40 s de `previo`) para 56 s de video. Las cifras del tablero, del mapa y de la lista son reales de la
  demo y cambian con la carga; ninguna frase depende de ellas.

### 4.4 Lo que la semilla garantiza y lo que no

- **Garantiza** (`backend/cron/jobs/_demo_eventos.php`): la cuenta 103 es responsable de la primera casa de paz, que tiene sus tres últimas
  reuniones sin reportar (línea 178: la más reciente se reporta en `previo`, la siguiente sin señal); la categoría Casa de Paz pide
  formulario, cuenta visitantes y tiene meta y niveles; el tablero lo ve el administrador (101); las personas de la demo tienen ubicación
  (la capa «Dónde viven» necesita ≥ 5 por celda).
- **No garantiza:** cuántas marca «Igual que la última vez» (la `ref` `ultima` exige ≥ 3; en la carga del clip fueron 7), cuántas zonas
  sin evento hay con 10 personas y 2 km (plan B: 5 personas), el orden de la lista y el nombre exacto de las otras reuniones de Jorge.

---

## 5. Montaje de las grabaciones nuevas

- **sin señal:** del primer cuadro de la lista ya puesta (tramo `volver`, después del toque) en adelante. Cada acción en su pulso: el
  toque de `casa` en el 810, el de `igual` en el 840, el `ver` de `abajo` en el 870, el toque de `guardar` en el 900, el primer cuadro sin
  `#ev-cola-pendientes` en el 960. Los cortes caen en las esperas (`huecos_de_pantalla`); las ondas de Material entre el toque y su efecto
  se recortan como en el clip (REVIEW §4.3). Velocidad 1× salvo donde un tramo no llegue a su pulso (0,35×–3,5×).
- **tablero:** el primer cuadro del tablero pintado con las cifras en 0 cae en el 1081; el mapa con teselas en el 1322; cada capa ya
  dibujada en el cuadro siguiente a su toque; la lista en el 1802; el desplazamiento del 1740, 1950, 2040 y 2160 a 1× (≈ 9 cuadros); la
  escritura de «Jorge Gallego» 1983–2010 a 1×; la lista filtrada en el 2025; la ficha bajo el iris en el 2101; 2175–2759 sale de los 16 s
  quietos del final (a 1×: 19,5 s de video piden 16 s de grabación más 3,5 s; **se alargan con un still** del último cuadro quieto desde
  el 2655, nunca con una velocidad menor que 0,35×).
- Los saltos de un cuadro que provoquen los `ver` de las cajas (`bloque: 'nearest'` no debería provocar ninguno) se compensan con `comp()`.
- La marca de toque del computador mide lo mismo en CSS de la app que la del celular (36 → 58 px), así que en el cuadro sale más chica
  (52 → 84 px a 1,44 ppc): es la misma marca de la serie, no un cursor.

---

## 6. Lo que se revisa en la vista previa

Cuadros: `npx hyperframes@0.8.221 snapshot --at 0,4.1,6.2,12.6,20.1,22.1,23.9,24.5,26.1,27.1,28.1,29.1,30.1,31.0,32.1,34.0,35.9,36.0,36.3,37.0,38.5,40.5,42.5,44.1,46.1,48.5,52.1,54.5,56.3,58.5,60.1,62.5,64.1,66.5,67.5,68.5,70.1,71.0,72.6,74.5,76.5,78.5,80.3,82.5,84.5,86.4,88.6,90.0,91.9,92.0,92.5,94.0,96.9`
y `snapshot --range 25.9,26.4 --frames 15` (la costura del 780), `--range 35.9,36.4 --frames 15` (el látigo), `--range 69.9,70.3 --frames 12`
(el iris de la ficha), `--range 29.8,30.3 --frames 15` (la costura de la música: la imagen no cambia por ella).

1. **0–24:** idéntico al clip (las 15 comprobaciones de su SPEC §4, en 16:9): mismos cuadros de cada toque, mismas frases, la píldora dentro
   de la ventana, el texto de la app ≥ 25 px.
2. **720–780:** la frase 4 aterriza en el 730 en dos líneas; la cámara en «Volver a la lista»; en el 780 la marca **está sobre el botón**
   (si cae a más de 6 px CSS del centro del botón del clip, la escena `previo` no reprodujo el «¡Listo!» del clip: se regraba).
3. **781–823:** la lista con el chip «Sin señal» ya puesto; el reporte de la vencida con «Pendiente» y la nota «Sin señal: …» legible
   (≥ 25 px).
4. **840–842:** las filas en ámbar con «N marcadas» exactamente con el golpe más fuerte. **870:** la app baja y la cámara no se mueve.
5. **900–904:** «Guardar asistencia» en la costura; «Espera señal» y «1 sin enviar» en el 903–904. **960:** el primer cuadro sin chips; la
   frase 5 entera en el 974.
6. **1080–1089:** el látigo es horizontal, de 9 cuadros, sin ningún cuadro de noche vacía; el computador llega con las cifras contando;
   **1099**: las cifras quietas en su valor.
7. **1140–1320:** la frase 6 en una línea; «Al día» con su rojo legible en el 1213; la marca espera sobre «Mapa» desde el 1305.
8. **1320–1800:** el mapa con teselas desde el 1322 (nunca gris); «Dónde viven» en el 1382; **las zonas en el 1562** con la leyenda «Zonas
   sin evento: N» con N > 0; la frase 7 en el 1568; el punch del 1688 sin pixelado (≤ 2,25 ppc).
9. **1800–2100:** la lista en el 1802 con rojos arriba; la frase 8 en una línea en el 1810; la reordenación en el 1922; «Jorge Gallego» se
   lee mientras se escribe; sus filas en el 2068 con su semáforo.
10. **2100–2580:** el iris nace del nombre de la casa; **«10 personas» a ≥ 31 px en el 2233**; la barra de la meta en el 2293; **«Ximena
    Hoyos Vélez» en el 2408**, entera y a ≥ 35 px.
11. **2580–2759:** la frase 9 con *reunión* dorada en el 2590; la ceja fuera; la ventana a 0,96 en el 2654 con el cuerpo ≥ 25 px; nada se
    mueve 2655–2756 salvo el halo; dip 2757–2759.
12. **2760–2909:** el cierre del Comercial desde el primer cuadro, sin noche vacía; el botón «Prueba gratis 30 días» y
    `kingdom-sitio.web.app`; el 2909 es el cierre completo.
13. **Sonido (medido, no oído):** los 22 sonidos del clip en sus cuadros; los 20 nuevos de §1.7 un cuadro después de su imagen; **la
    costura del 30,0** sin golpe extra ni hueco (§0.1); las campanas en el 92,38; −16 LUFS ±1, pico real ≤ −1 dBTP; la música a −10 dB en
    el 2772 y en 0 en el 2820.
14. **Textos:** ninguna palabra que no esté en la app, en las nueve frases o en el cierre; frases del celular en ≤ 2 líneas, del computador
    en 1; `npx hyperframes check` en 0 errores (contraste AA); «Datos de ejemplo» en las dos ventanas desde su primer cuadro.
15. **La historia sin sonido** (así se ve en el sitio): terminó la reunión → los de siempre → persona nueva → ¡Listo! → sin señal se
    guarda → se envía sola → el pastor ve todo → dónde falta una reunión → cuál crece y cuál necesita apoyo → la casa de Jorge con sus 10
    personas y Ximena → cada reunión cuenta → Kingdom, prueba gratis.

---

## 7. Riesgos y lo que se decide al grabar

- **La semilla de otro día.** Las tres grabaciones tienen que ser de la misma carga (la reunión del 28 de octubre). La `ref` `mismaSemilla`
  lo exige; si Kingdom Demo se recargó otro día, la decisión es **regrabar también `clips/eventos-casa-de-paz`** el mismo día que las dos
  nuevas, quitar la condición de fecha (o ponerle la nueva) y recalcular los cuadros de la grabación del clip en el montaje de 0–719 (los
  tiempos del video no cambian). Nunca un recorrido con una fecha en el «¡Listo!» y otra en la ficha.
- **Zonas sin evento vacías** con 10 personas y 2 km: plan B de §4.3 (5 personas). Si con 5 tampoco hay, el golpe del 1560 queda para
  «Dónde viven» y la frase 7 pasa a **«Y dónde vive tu gente»** (5 palabras, una línea); «Dónde viven» se mueve al 1380 como estaba.
- **El mapa sin teselas** (sin internet al grabar, o OpenFreeMap lento): la escena espera 3 s; si el fondo sale gris, se graba otra vez. No
  se dibuja un mapa.
- **«Igual que la última vez» marca otro número** que en el clip: si es distinto de 7, la ficha no dirá «10 personas» sino otro número; da
  igual para las frases, pero el «¡Listo!» del clip dice 10: la `ref` `ultima` se aprieta a `= 7` si se quiere la cifra exacta (se decide al
  grabar; con la misma carga es 7).
- **El clic en «Volver a la lista» no cae donde el clip** (la escena `previo` no dejó la pantalla igual): revisión 2 de §6; se ajusta la
  pausa del `ver` hasta que coincida.
- **El cargador de la app** (la K a los 150 ms) en «Guardar asistencia», la carga del tablero, el filtro y la ficha: se corta en la espera.
- **Densidad del clímax** (1800–2100): válvula de P9 (sin reordenar).
- **La costura de la música:** se mide (§0.1). Si `hyperframes audio` ve un golpe doble en el 30,0, el cruce se alarga a 60 ms.
- **El largo:** 97 s contra los 60–75 s que dice hoy `KingdomApp/docs/videos/README.md` para el recorrido (§8).

## 8. Lo que queda fuera y lo que hay que actualizar

- **9:16:** no se especifica aquí (lo decidido es 16:9). Cuando se haga: el mundo celular pasa tal cual a `.k-ventana-9x16`; el computador
  pide recortes nuevos (la ventana de 960×850 no muestra una fila de cifras a ≥ 25 px) y probablemente otra estructura para el tablero.
- **El largo del recorrido** en `KingdomApp/docs/videos/README.md` («de 60 a 75 s») y en la tabla de tipos (decisión 216/218): pasar a
  «de 60 a 100 s», como dice el pedido del 2026-10-30. Lo actualiza quien entregue el video, en la misma entrega.
- **Las dos escenas** van a `tools/ayuda/escenas/clips/` (no son de la ayuda: no se publican ni entran en la frescura).
- **El sitio:** el recorrido va en la página `/eventos` (`sitio/src/data/modulos.ts` no tiene todavía un campo para el recorrido; el clip
  usa `video`). Se agrega cuando el video exista; no es parte de este SPEC.
