# SPEC · Clip del sitio: Academia — «La clase ya empezó»

2026-10-30 · Contrato de construcción de la historia elegida en [STORY.md](STORY.md). Mismo sistema que
[Membresía](../clip-sitio-membresia/SPEC.md) (y las lecciones de su [REVIEW.md](../clip-sitio-membresia/REVIEW.md)): cada adjetivo es un
número, los valores por defecto están prohibidos con nombre y los planos van cuadro por cuadro. Se construye desde aquí, se revisa contra esto
y se cambia aquí cuando la vista previa cambie la película. Lo que aquí dice «igual que Membresía» se copia de su `index.html` sin reabrirlo.

```text
GOAL:    Un pastor que no conoce Kingdom termina pensando «el profesor pone un código, cada quien marca desde su silla y al final
         sale el certificado» y toca «Prueba gratis 30 días».
OUTPUT:  HyperFrames · dos composiciones de la misma línea de tiempo: 1080×1350 (4:5, sitio y feed) y 1080×1920 (9:16) · 30 fps.
TIME:    30,5 s = 915 cuadros: cuerpo 0–28,0 (cuadros 0–839) + firma 28,0–30,5 (840–914). 120 BPM = 15 cuadros por pulso (grilla real, §0).
LOOK:    noche del sitio (#060D1F) con el halo y la retícula de puntos del kit; tinta #EAF0FF; un solo acento, el dorado #E8B95A, en tres
         lugares y no más (la ceja «ACADEMIA», la palabra «líderes» y el botón de la firma). Fraunces 560 / −0,02 em para las frases;
         Inter para la ceja y «Datos de ejemplo». El medio: la app REAL de Kingdom Demo grabada en celular (1170 px de ancho), dentro
         de la misma ventana de Membresía (radio 28, anillo de 1 px, sombra 0 40 80 −24 al 65 %); nunca un teléfono dibujado.
OBJECTS: la ventana (tres celulares: el del profesor, el de la alumna, el de quien coordina); el punto de toque; las cuatro frases; la
         ceja; la píldora «Datos de ejemplo»; la corona del cierre. Nada más existe en el cuadro.
MOTION:  curvas por papel (§1.6); un movimiento de cámara por compás (14 cuadros, power2.inOut), quieto después; cada corte y cada
         entrada en un pulso; cada cambio de mundo en un golpe (120 · 240 · 360 · 600 · 660 · 720 · 840).
SHOTS:   ocho planos (§2).
BANNED:  §1.8.
QA:      §4.
```

---

## 0. El reloj: la grilla real de la pista

«Product Launch» (The_Mountain) del 14,05 al 42,05 s; t = 0 del clip ↔ 14,05 de la pista. Los pulsos vienen de
`_identidad/musica/product-launch-the-mountain.pulsos.json` restándoles 14,05 y redondeando a 30 fps: **todos caen en el múltiplo de 15
salvo el 9,455 s (cuadro 284)**; no hay ningún evento ahí. Cada pulso se calcula desde su índice; nunca se suma 15 repetidamente.

| Compás | Cuadros | Pulsos (cuadro · fuerza) | Lo que le toca a este clip |
|---|---|---|---|
| 1 | 0–59 | 0 ·0,69 · 15 ·0,64 · 30 ·0,49 · 45 ·0,48 | El profesor: el código en pantalla; la frase 1 palabra por pulso |
| 2 | 60–119 | 60 ·0,58 · 75 ·0,55 · 90 ·0,57 · 105 ·0,61 | La cámara baja al contador «13 de 18 marcaron»; el temporizador real |
| 3 | 120–179 | **120 ·0,93** (bajo) · 135 ·0,62 · 150 ·0,59 · 165 ·0,51 | **Látigo a la alumna; un número por pulso: 120 · 135 · 150 · 165.** Frase 2 |
| 4 | 180–239 | **180 ·0,87** (pico) · 195 ·0,83 · 210 ·0,67 · 225 ·0,72 | **«¡Listo! Quedó tu asistencia»** en el pico; la ceja en el 195 |
| 5 | 240–299 | **240 ·0,92** · 255 ·0,77 · 270 ·0,58 · 284 ·0,52 | **Látigo de vuelta al profesor: «14 de 18 marcaron»**; 270 «Presente» → 15 |
| 6 | 300–359 | 300 ·0,77 · 315 ·0,75 · 330 ·0,60 · 345 ·0,59 | 300 «Presente» → 16; 330 acercamiento al contador |
| 7 | 360–419 | **360 ·0,76** · 375 ·0,64 · 390 ·0,50 · 405 ·0,46 | **Látigo a quien coordina: «Por aprobar»**; frase 3; 375 toque → la lista |
| 8 | 420–479 | 420 ·0,75 · 435 ·0,61 · 450 ·0,49 · 465 ·0,49 | La lista se desplaza; la cámara baja a la barra |
| 9 | 480–539 | 480 ·0,67 · 495 ·0,67 · 510 ·0,54 · 525 ·0,50 | 480 toque «Aprobar (9)»; el diálogo «¿Aprobar la graduación?» |
| 10 | 540–599 | 540 ·0,63 · 555 ·0,56 · 570 ·0,61 · 585 ·0,68 | El diálogo quieto; el dedo baja al botón |
| 11 | 600–659 | **600 ·0,93** (2.ª subida) · 615 ·0,69 · 630 ·0,52 · 645 ·0,49 | **Toque «Aprobar (9)»: «¡Listo! 9 graduados, con su certificado.»**; «Certificados (9)» |
| 12 | 660–719 | **660 ·0,90** · 675 ·0,89 · 690 ·0,76 · 705 ·0,68 | **Toque «Ver»: el certificado**; 675 acercamiento al nombre |
| 13 | 720–779 | **720 ·0,96** · 735 ·0,77 · 750 ·0,59 · 765 ·0,60 | Frase 4; la cámara al «Código de verificación»; la ventana se hace a un lado |
| 14 | 780–839 | 780 ·0,88 · 795 ·0,74 · 810 ·0,62 · 825 ·0,60 | Quieto; la subida; el dip |
| — | **840** ·1,00 | el golpe más fuerte de la pista | **La firma.** La música se va debajo de las campanas |

---

## 1. Los números del estilo

### 1.1 Paleta (tokens de `identidad/kit.css`; nada fuera de esta lista)

| Papel | Token | Valor | Dónde puede aparecer |
|---|---|---|---|
| Fondo | `--k-noche` | `#060D1F` | A sangre, todo el cuerpo |
| Halo | `.k-halo` | azul `rgba(53,118,218,.45)` arriba a la derecha + dorado `rgba(217,162,52,.22)` abajo a la izquierda | Fondo; se asienta 1,08 → 1 al entrar cada mundo (0 · 120 · 240 · 360 · 720) |
| Puntos | `.k-puntos` | `rgba(169,190,235,.35)`, 2 px cada 42 px | Fondo; **nunca se mueven** |
| Tinta | `--k-noche-tinta` | `#EAF0FF` | Las frases |
| Acento | `--k-noche-dorado` | `#E8B95A` | Solo: la ceja «ACADEMIA», la palabra *líderes*, el botón de la firma |
| Anillo | `--k-noche-linea` | `rgba(234,240,255,.12)` | El borde de la ventana |
| Fondo de la app | `--k-app-fondo` | `#FAF9FD` | Detrás de la grabación (no se ve) |
| Azul de marca | `--k-azul` | `#3576DA` | **Solo en la firma** |
| Placa | `.k-datos-ejemplo` | `rgba(6,13,31,.72)` | La píldora «Datos de ejemplo» |
| Dip | — | `rgba(6,13,31,.40)` | Los cuadros 837–839, solo sobre la ventana |

Los colores de la app (el morado `#015BBE`-primario del tema, el lila de las casillas, el verde del chequeo) viven dentro de la grabación
y no se tocan. **El tono de Academia en el sitio es terciario (verde azulado) y no se usa aquí:** la ceja es dorada como en toda la serie.

### 1.2 Tipografía

| Pieza | Clase (kit v1.1) | Familia · peso | 4:5 | 9:16 | Reglas |
|---|---|---|---|---|---|
| Frase | `.k-feed-frase` (`.k-titular` + `.k-vertical` en 9:16) | Fraunces 560; `<em>` itálica 500 dorada | **80 px** · 1,04 · −0,02 em | **104 px** | Máx. 2 líneas en 4:5 (3 en 9:16), saltos fijados a mano; izquierda; `text-wrap: balance` apagado; sin sombra |
| Ceja | `.k-feed-ceja` | Inter 700, MAYÚSCULAS | **30 px** · +0,10 em | **34 px** | Una palabra: «ACADEMIA» |
| Datos de ejemplo | `.k-datos-ejemplo.k-feed-datos` | Inter 600 | **31 px**, píldora de 56 px (como quedó en Membresía: 28 del kit no aguanta la ventana a 0,92) | igual | Abajo a la izquierda de la ventana, a 24 px (pedido del dueño) |
| Texto de la app | (grabación) | Inter de la app, 14 px CSS el cuerpo | ≥ **31,6 px** | ≥ **34,5 px** | Nunca por debajo de 28 px en ningún encuadre (§1.5) |

Saltos de línea fijados:
«La clase / ya empezó.» · «Sin listas / de papel.» · «Quien cumple, / se gradúa.» · «Forma a los *líderes* / que tu visión necesita».
En 9:16 (≈ 19 caracteres por línea a 104 px) la frase 4 va en tres: «Forma a los *líderes* / que tu visión / necesita».

### 1.3 Radios y sombras

Igual que Membresía: `.k-ventana` radio **28 px**, `0 0 0 1px var(--k-noche-linea)` + `0 40px 80px -24px rgba(0,0,0,.65)`, `overflow: hidden`;
la píldora 999 px sin sombra; frases y ceja sin sombra ni brillo; la firma con lo del kit.

### 1.4 Disposición por formato

| | 4:5 (1080×1350) | 9:16 (1080×1920) |
|---|---|---|
| Márgenes | 96 a los lados, 72 arriba | 60 a los lados; banda útil 168–1330 |
| Ceja | x 96 · y 72 (30 px) | x 60 · y 188 (34 px) |
| Frase | x 96 · y 124 · ancho 888 · 2 líneas de 83 px → termina en 290 | x 60 · y 236 · ancho 960 · hasta 3 líneas de 108 px → 560 |
| Ventana | x 100 · y 360 · **880 × 1050**, sangra 60 px por abajo (se ve 880×990) | x 60 · y 480 · **960 × 850**, completa |
| Ventana al final (desde el 724) | escala **0,92** desde el centro inferior + x **+48** | escala 0,92 desde el centro superior + x **+36** |
| Datos de ejemplo | dentro de la ventana, abajo a la izquierda, a 24 px (subida 60 px por el sangrado) | ídem |
| Firma | `cierre-clip` | `cierre-corto` |

Variables `--f-*` y `window.KD` de `clip-sitio-membresia/index.html`, tal cual (`--f-k: 0.752137`, `--f-grab-alto: 1904.41px`,
`--f-latigo: 1100px`; en 9:16 lo que dice su REVIEW §8).

### 1.5 La cámara dentro de la ventana: escalas

La grabación llega a 3× (390×844 px CSS → 1170×2532). **ppc** = píxeles del cuadro por píxel CSS del celular. Los mismos cuatro niveles de
Membresía (G = ×1,00 · G⁺ = ×1,08 · M = ×1,40 · C = ×1,80 sobre el general):

| Nivel | 4:5: ppc · visible (px CSS) | 9:16: ppc · visible | Texto de la app de 14 px → |
|---|---|---|---|
| **G** | 2,256 · 390 × 439 | 2,462 · 390 × 345 | 31,6 · 34,5 px |
| **G⁺** | 2,436 · 361 × 406 | 2,659 · 361 × 320 | 34 · 37 px |
| **M** | 3,158 · 279 × 313 | 3,446 · 279 × 247 | 44 · 48 px |
| **C** | 4,061 · 217 × 244 | 4,431 · 217 × 192 | 57 · 62 px |

El objetivo de cada movimiento es una **caja de `pasos.json`** (px CSS) centrada en lo visible de la ventana, con la cámara sujeta a los
bordes de la grabación (`enc()` de Membresía). La cámara es `scale` + `x`/`y` sobre `#cam`; el `<video>` nunca se transforma ni se busca.

Medidas tomadas de las capturas publicadas de la ayuda (px CSS, viewport 390×844; se confirman con las cajas reales al grabar):

- **La toma del profesor** (`toma.page.ts`): título de la clase ≈ 106 · «Marquen su asistencia con este código» 165 · los **cuatro números
  182–262** (≈ 80 px de alto cada uno: a G salen de 180 px) · barra 271 · «El código cambia en N s» 290 · QR 309–550 · **«N de 18 marcaron»
  593–635** (el número ≈ 42 px CSS → 95 px a G) · «Se cierra sola en 14:xx» 654 · «5 minutos más | Cerrar la toma» 677–724 · «Faltan (N)»
  753 · las filas con «Presente» desde ≈ 800 (fuera del primer viewport: el tramo 3 se graba con la página desplazada).
- **El cuadro de la alumna** (`asistencia.page.ts` + `codigo-cuadro`): «Marcar asistencia» 89 · «Fundamentos bíblicos» 153 · «Repaso
  general» 191 · fecha 230 · «Escribe los 4 números que muestra tu profesor» 271–296 · **las cuatro casillas 322–398** (≈ 60 px CSS: 190 px
  a M) · la ayuda 423–440. Después del envío: el chequeo 254–326 · **«¡Listo! Quedó tu asistencia» 351** · «Ir a Mis cursos» 430.
- **La lista de graduación y el certificado** a 390 px no tienen captura: sus cajas salen de la grabación («(real)» en §2).

### 1.6 Curvas y duraciones (cada tween lleva su curva por nombre)

| Papel | Curva | Cuadros | Detalle |
|---|---|---|---|
| `entrada-palabra` | `power4.out` | 4 | blur 6 → 0 + opacidad; **sin desplazamiento**; arranca un cuadro antes del pulso (REVIEW §4.7) para que el primer cuadro visible sea el pulso. Palabras a 2 cuadros, salvo la frase 1 (una por pulso) |
| `entrada-linea` | `power4.out` | 6 | la línea entera, blur 8 → 0 (frase 2 y ceja) |
| `salida-texto` | `power3.in` | 4–5 | blur 0 → 8 + opacidad; empieza 2–3 cuadros antes del pulso (blur swap) |
| `camara` | `power2.inOut` | **14** | un movimiento por compás; después, quieta; **nunca mientras la app se desplaza sola** |
| `punch` | `power2.inOut` | **9** | solo el del cuadro 675 |
| `latigo` | `power3.inOut` | **10** | **una sola tira** (REVIEW §4.10) con los tres mundos apilados a 1100 px (4:5) ∕ 1000 px (9:16) (§2.0): el látigo mueve la tira una ranura (arriba = al otro celular; abajo = de vuelta). El mundo que llega aterriza 1,04 → 1,00 (`power3.out`, 10 cuadros) |
| `iris` | `power2.out` | 5 | `clip-path: circle(0 → 1900px at X Y)` desde el centro del botón tocado (375 y 660); still del cuadro anterior debajo |
| `pop-numero` | `power3.out` | 4 | **no se anima nada de la app**: el número aparece en su casilla en la grabación; el «pop» es solo el sonido `aparicion` (§1.7). Igual el contador |
| `ventana-cambio` | `power2.inOut` | 15 | escala 1 → 0,92 + x, 724–738 |
| `halo` | `sine.out` | 90 | escala 1,08 → 1,00 al entrar cada mundo (0, 120, 240, 360, 720) |
| `dip` | escalón | 3 | capa `rgba(6,13,31,.40)` sobre la ventana, 837–839 |
| firma | las del kit | 75 | no se imita en el cuerpo |
| velocidad de la grabación | `data-playback-rate` por tramo | — | entre **0,35× y 3,5×**; las rampas entre acciones, nunca durante un toque ni mientras cae un número |

`data-motion-blur="on"` con `data-motion-blur-shutter="180"` en la raíz. Nunca `filter: blur()` sobre la grabación.

### 1.7 Sonido

| Capa | Fuente | Nivel | Regla |
|---|---|---|---|
| Música | `assets/musica/product-launch-the-mountain.mp3`, `data-media-start` 14,05, 29,0 s | 0,7 en el carril de volumen (−18 LUFS) | 0,7 hasta 28,0 → 0,224 en 28,4 → 0 en 29,0 (igual que Membresía) |
| Sonidos de acción | kit v1.1: `toque` (3 tomas rotadas a/b/c) · `aparicion` · `desliz` · `subida` · `confirmacion` | `data-volume="1"`; **1,4** en los cinco clave: toque 601 y 661, las dos `confirmacion` (181, 603) y el `desliz` del 120 | `data-start` = cuadro del sonido / 30 − acento (toque 0 · aparicion 0 · desliz 0,2 · subida 1,5 · confirmacion 0,1). El pico suena **un cuadro después** de su imagen |
| Sonido de marca | `identidad/audio/sonido-marca.wav` | 1 | En **28,38 s** (cuadro 851) |
| Mezcla | — | **−16 LUFS**, pico real ≤ **−1 dBTP** | `normalize-audio` sobre el render de entrega; medido con `hyperframes audio`, no oído |

Los veintiún eventos, por cuadro de imagen (el sonido, uno después): `desliz` 120 (látigo, 1,4) · `aparicion` 120 · 135 · 150 · 165 (los
cuatro números) · `confirmacion` 180 (¡Listo!, 1,4) · `aparicion` 195 (la ceja) · `desliz` 240 (látigo de vuelta) · `toque` a 270 ·
`aparicion` 273 (→ 15) · `toque` b 300 · `aparicion` 303 (→ 16) · `desliz` 360 (látigo) · `toque` c 375 (la lista) · `desliz` 420 (la lista
se desplaza, 0 dB) · `toque` a 480 («Aprobar (9)») · `toque` b 600 (confirmar, 1,4) · `confirmacion` 603 (1,4) · `toque` c 660 («Ver», 1,4) ·
`subida` 796–853 (golpe en el 840) · campanas 851. Sin tics de tecla. **Cuatro `aparicion` seguidas (120–165) son la figura rítmica del
clip:** si en la vista previa suenan a máquina, las del 135 y el 150 bajan a 0,7; nunca se quitan.

### 1.8 BANNED: los valores por defecto prohibidos, con nombre

Los veinte de Membresía (§1.8) valen enteros. Además, propios de este clip:

21. **Dibujar o resaltar los números del código** (un recuadro, un brillo, un contador animado encima de la app): los números, el contador y
    el chequeo son los de la grabación; lo único que se les agrega es un sonido.
22. **Un teclado dibujado** para la alumna. No hay teclado en la emulación y no se inventa: el número aparece en su casilla y basta.
23. **El látigo de vuelta igual al de ida.** De ida la tira sube; de vuelta baja. Si los dos van en la misma dirección, el espectador pierde
    cuál celular es cuál.
24. **Mover la cámara mientras la app se desplaza sola** (420–447 y 615–642): dos movimientos encimados se leen como temblor.
25. **Leer el diálogo entero.** «¿Aprobar la graduación?» se encuadra con su título y su botón; el cuerpo queda legible pero no se le da
    tiempo de lectura completa (no se estira el plano para eso).
26. **Un cuarto mundo.** El clip termina en el celular de quien coordina; no vuelve a la alumna para «Mis cursos → Terminados» aunque su
    certificado exista (sería un quinto látigo).

---

## 2. Los planos, cuadro por cuadro

### 2.0 Convenciones

- **G / G⁺ / M / C:** §1.5. «Sobre X» = la caja de X (`pasos.json`) centrada en la ventana. Cuando una caja no está en las capturas se marca
  «(real)»: sale de la grabación.
- **Pulso:** el cuadro de §0. Un evento «en el 120» aterriza en el cuadro 120; su sonido suena en el 121.
- **Grabación:** una sola corrida de la escena de §3; los tramos: **T1** `codigo` (profesor, 103), **T2** `alumna` (104), **T3** `contador`
  (profesor, 103), **T5** `por-aprobar`, **T6** `lista`/`aprobar`/`aprobado`/`certificados` y **T7** `certificado` (quien coordina, 101).
  `cerrar-toma` y `enviar` (103) se graban y no se usan.
- **La tira de mundos** (`#tira`): tres ranuras apiladas de 1100 px (4:5) ∕ 1000 px (9:16): **m1** el profesor, **m2** la alumna, **m3**
  quien coordina. Los látigos mueven la tira: 120 → m2 (sube 1100), 240 → m1 (baja 1100: el mismo mundo con T3 dentro; la grabación de m1
  cambia de T1 a T3 durante el látigo del 236–246, cuando m1 está fuera del cuadro), 360 → m3 (sube 2200 desde m1, o sea el látigo recorre
  dos ranuras en los mismos 10 cuadros: se ve igual de rápido porque el mundo 2 pasa borroso con el motion blur). Si en la vista previa el
  salto doble molesta, m3 se coloca en la ranura 2 durante el 236–246 (m2 ya no se usa) y el látigo del 360 es de una ranura.
- **Textos de la app:** los reales de `frontend-v2/public/i18n/es.json` (STORY §5). Lo que no se puede saber hasta grabar lleva «(real)».
- Las frases siempre en el mismo lugar (§1.4); una a la vez; la ceja encima de la frase.

### 2.1 Tabla maestra (todo lo que cambia, por cuadro)

| Cuadro | Pulso | La app (grabación) | Cámara | Texto | Sonido | Transición |
|---|---|---|---|---|---|---|
| **0** | ● | T1 · la toma de asistencia del profesor: «Fundamentos bíblicos · Fundamentos · miércoles 7 p. m.» / «Repaso general», **«Marquen su asistencia con este código»**, los **cuatro números** (los mismos que escribirá la alumna), la barra y «El código cambia en N s», el QR. «Datos de ejemplo» en su esquina | **G** sobre CSS 60–499: el título, los números, la barra, la mitad alta del QR (es la miniatura) | **«La»** ya aterrizada | — | — |
| 15 · 30 · 45 | ● ● ● | el temporizador real tictaquea (cada 30 cuadros, en la fase que caiga); la barra del código se acorta | quieta | **«clase»** 15 · **«ya»** 30 · **«empezó.»** 45; completa y quieta hasta el 117 | — | |
| **60** | ● | quieta (la app sigue viva) | **Movimiento del compás 2**: G → **G** sobre CSS 405–844: la mitad baja del QR, **«13 de 18 marcaron»**, «Se cierra sola en 14:xx», «5 minutos más | Cerrar la toma», «Faltan (5)», 60–73 | — | — | |
| 75 · 90 · 105 | ● ● ● | los segundos del temporizador bajan (real) | quieta | — | — | |
| 110–120 | | T1 sale hacia arriba; T2 llega desde abajo: el cuadro de la alumna con **«Escribe los 4 números que muestra tu profesor»** y las cuatro casillas vacías (los 3–4 cuadros anteriores a la primera tecla) | T2 llega en **M** sobre las casillas (CSS 271–440: la pregunta, las casillas, la ayuda) | la frase 1 sale 117–121 | **`desliz` (1,4) acento en el 120** | **Látigo arriba** 110–120, aterriza 1,04 → 1,00 (120–130); halo a 1,08 → 1 (120–210) |
| **120** | **●●● bajo** | **el primer número entra en su casilla** (tecla real: `teclas[0]` del tramo `digito-1`) | quieta | **«Sin listas / de papel.»** entrada-linea 120–126 | **`aparicion` (1,0) en el 121** | |
| **135** | ● | el segundo número (`digito-2`); entre teclas la grabación va a 1,5–2× para que cada una caiga en su pulso | quieta | frase 2 quieta | `aparicion` en el 136 | |
| **150** | ● | el tercero | quieta | | `aparicion` en el 151 | |
| **165** | ● | el cuarto: la app lo envía sola («Enviando…» puede verse un instante, real) | quieta | | `aparicion` en el 166 | |
| **180** | **●●● pico** | **«¡Listo! Quedó tu asistencia»** con el círculo de chequeo y debajo «Fundamentos bíblicos · Repaso general» (real) (la espera del envío se recorta para que el resultado entre en el 180, como «Guardada» en Membresía) | **Movimiento del compás 4**: M casillas → **M** sobre el chequeo y la línea «¡Listo! Quedó tu asistencia» (CSS 254–360), 180–193 | | **`confirmacion` (1,4) en el 181** | |
| **195** | ● | quieta (aparece «Ir a Mis cursos» debajo, real) | quieta | **«ACADEMIA»** entrada-linea 195–201 | `aparicion` en el 196 | |
| 210 · 225 | ● ● | quieta | quieta | | — | (los dos pulsos de reposo del clip: el resultado se lee) |
| 230–240 | | T2 sale hacia abajo; T3 llega desde arriba: la toma del profesor otra vez, **desplazada** para que se vean juntos el contador y las primeras filas de «Faltan» | T3 llega en **G⁺** sobre «**14 de 18 marcaron**» · «Se cierra sola en 13:xx» · los botones · «Faltan (4)» · las dos primeras filas con **«Presente»** (real) | frase 2 quieta | **`desliz` (1,0) acento en el 240** | **Látigo abajo** 230–240; halo 240–330 |
| **270** | ● | **toque en «Presente»** de la primera fila → la fila se va y el contador pasa a **«15 de 18»** (273, real) | quieta | | `toque` a en el 271; `aparicion` en el 274 | |
| **300** | ● | **toque en «Presente»** de la siguiente → **«16 de 18»** | quieta | | `toque` b en el 301; `aparicion` en el 304 | |
| **330** | ● | quieta | **Movimiento del compás 6**: G⁺ → **M** sobre «16 de 18 marcaron» y «Se cierra sola en …» (la prueba: el profesor lo ve al instante), 330–343 | | — | |
| 350–360 | | T3 sale hacia arriba; T5 llega desde abajo: la pantalla principal de Academia de quien coordina con la tarjeta **«Por aprobar» 1** y su lista: «Fundamentos bíblicos · Fundamentos · miércoles 7 p. m. · 9 para graduar · enviada por Jorge Gallego Gil el …» (real) | T5 llega en **G⁺** sobre la tarjeta «Por aprobar» (real) | la frase 2 sale 357–361 | **`desliz` (1,0) acento en el 360** | **Látigo arriba** 350–360; halo 360–450 |
| **360** | **●** | quieta | quieta | **«Quien cumple, / se gradúa.»**: Quien 360 · cumple, 362 · se 364 · gradúa. 366 | — | |
| **375** | ● | **toque en la lista de «Por aprobar»** | quieta | frase 3 quieta | `toque` c en el 376 | **Iris desde el toque** 375–380 (still del 374 debajo) |
| 380–389 | | la sección «Graduar» del grupo: **«Se gradúan 9 · 9 no se gradúan»** y las personas: «Andrea Perea López · Nota 3,88 · Asistencia 83,3 % (5 de 6) · Cumple los criterios · Se gradúa · Excluir»… (nombres y cifras reales del día) | **G** (la lista desde arriba) | | — | |
| **390** | ● | quieta | **Movimiento del compás 7**: G → **M** sobre el encabezado «Se gradúan 9 · 9 no se gradúan» y la primera persona, 390–403 | | — | |
| **420**–447 | ● | **la lista se desplaza sola** (el `ver` suave de 900 ms hasta la cuarta persona): pasan dos o tres filas, alguna «No cumple: asistencia del 66,7 % (pide 75 %)» (real) | **quieta** (BANNED 24) | | `desliz` (1,0) acento en el 421 | |
| **465** | ● | quieta | **Movimiento del compás 8**: M → **G⁺** sobre las últimas filas visibles y la barra fija **«Devolver al profesor | Aprobar (9)»** (real) | | — | |
| **480** | ● | **toque en «Aprobar (9)»** → el diálogo **«¿Aprobar la graduación?»** · «Se gradúan 9 y 9 no. Cada graduado recibe su logro, su certificado y el aviso. No se puede deshacer (un certificado sí se puede anular).» · Cancelar · **Aprobar (9)** (entra 483–488, real) | quieta hasta el 495 | | `toque` a en el 481 | |
| **495** | ● | quieta | **Movimiento del compás 9**: G⁺ → **M** sobre el diálogo (título, cuerpo, botones) (real), 495–508 | | — | |
| 510–597 | 510 … 585 | el diálogo quieto 3 s; el punto de toque baja al botón hacia el 585 | quieta | frase 3 quieta; **sale 597–601** | — | |
| **600** | **●●● 2.ª subida** | **toque en «Aprobar (9)»** del diálogo → se cierra; abajo el aviso real **«¡Listo! 9 graduados, con su certificado.»** (5 s) | **Movimiento del compás 11**: M diálogo → **G⁺** sobre el final de la lista y el aviso (real), 600–613 | — | **`toque` b (1,4) en el 601; `confirmacion` (1,4) en el 603** | |
| 615–642 | ● | **la app se desplaza sola** hasta **«Certificados (9)»** · «Descargar todos (para imprimir)» · cada persona con «Ver» y «Descargar» (real) | **quieta** | | `desliz` (1,0) acento en el 616 | |
| **645** | ● | quieta | **Movimiento**: G⁺ → **M** sobre «Certificados (9)», «Descargar todos (para imprimir)» y la primera fila con «Ver» (real), 645–658 | | — | |
| **660** | **●●● golpe** | **toque en «Ver»** | quieta | | **`toque` c (1,4) en el 661** | **Iris desde el toque** 660–665 (still del 659 debajo) |
| 665–674 | | T7: **el certificado**: «IGLESIA KINGDOM DEMO 1» · «CERTIFICADO» · «Iglesia Kingdom Demo 1 otorga el presente certificado a» · ***Nombre Apellido*** · «por haber terminado satisfactoriamente el curso Fundamentos bíblicos.» · la fecha (real) | **G** sobre la tarjeta del certificado (de «IGLESIA…» a la fecha; real) | | — | |
| **675** | **●●** | quieta | **Punch** G → **M** sobre «otorga el presente certificado a · *Nombre* · por haber terminado … Fundamentos bíblicos.», 675–683, 9 cuadros | | — | |
| 690 · 705 | ● ● | quieta | quieta | | — | |
| **720** | **●●● golpe** | quieta | **Movimiento del compás 13**: M → **G** sobre el bloque de abajo: «por haber terminado…», la fecha, **«Descargar certificado»**, **«Código de verificación»**, el código (p. ej. **UBBBE-C3BR8**), «Copiar el enlace para verificarlo» (real; si no cabe en G, M desde «Descargar certificado» hasta «Copiar el enlace para verificarlo»), 720–733 | **«Forma a los *líderes* / que tu visión necesita»**: Forma 720 · a 722 · los 724 · *líderes* 726 · que 728 · tu 730 · visión 732 · necesita 734 (completa en el 738). **La ceja sale 720–723** | — | **La ventana se hace a un lado** 724–738; halo 720–810 |
| 738–836 | 750 … 825 | quieta (la página del certificado) | quieta | frase 4 quieta ≥ 3,4 s | **`subida`** 796–853 (golpe en el 840) | |
| **837–839** | | — | — | — | — | **Dip** 40 %, 3 cuadros |
| **840** | **●●● el más fuerte** | — | — | — | música 0,7 → 0,224 (852) → 0 (870) | **Corte a la firma**: `cierre-clip` (4:5) / `cierre-corto` (9:16), `{"llamado":"prueba","fondo":"azul","idioma":"es"}` |
| 846 · 853 ↓ | | la K sube; las 7 barras de la corona desde el 0,45 | | «Kingdom» 0,75 s; **«Prueba gratis 30 días»** 0,95 s | **Campanas en el 851** | |
| **914** | | último cuadro: la corona completa y el botón | | | | fin |

### 2.2 Los ocho planos

#### P1 · «El código en pantalla» — cuadros 0–109 (compases 1–2) · pulsos 0 … 105

- **Grabación:** T1 desde su primer cuadro (la página ya cargada: la entrada se hace antes de grabar) a **1×** durante 3,7 s: el temporizador
  y la barra del código deben verse correr a su velocidad real. Sin cortes.
- **Encuadre 4:5:** G sobre CSS 60–499 (0–59); G sobre 405–844 (desde el 73). **9:16:** G muestra 345 px CSS: 0–59 sobre 120–465 (los
  números, la barra, el QR); 73+ sobre 500–844 (el contador, el temporizador, los botones, «Faltan»).
- **Cámara:** un solo movimiento (60–73). Nada más: el reloj de la app es el movimiento.
- **Texto:** frase 1 por pulsos (la primera palabra ya puesta en el cuadro 0); sale 117–121.
- **Sonido:** ninguno hasta el látigo (la música sola: la entrada sin bajo).
- **Transición:** látigo arriba 110–120.
- **Válvula:** si el primer viewport muestra menos de lo medido (una cabecera más alta en la grabación), el encuadre del 0 baja hasta que
  los cuatro números queden a ≥ 120 px del borde superior de la ventana; la frase 1 no toca la ventana.

#### P2 · «Cuatro números, un pulso cada uno» — cuadros 110–179 (compás 3) · pulsos 120 (bajo), 135, 150, 165

- **Grabación:** T2 desde 4 cuadros antes de la primera tecla (`tramo digito-1 → teclas[0]`) hasta el cuadro anterior a «¡Listo!». Entre
  teclas la escena deja ≈ 0,8–1,0 s (toque en el campo + tecla + pausa 400 ms): se reproduce a **1,6–2,0×** para que cada tecla caiga en su
  pulso; **el cuadro de cada tecla va a 1×** (dos cuadros antes y dos después).
- **Encuadre:** M sobre las casillas (CSS 271–440). Igual en 9:16 (M muestra 247 px CSS: cabe).
- **Cámara:** quieta todo el plano.
- **Texto:** frase 2 entra 120–126 (línea entera).
- **Sonido:** desliz 120 (1,4), aparicion 121 · 136 · 151 · 166.
- **Transición:** llega con el látigo; cierra con el resultado del 180 (sin transición: el «¡Listo!» reemplaza las casillas en la misma
  tarjeta).
- **Lo que se mira:** que los números que entran sean **los mismos** que mostró el profesor en P1 (§5, el minuto).

#### P3 · «¡Listo! Quedó tu asistencia» — cuadros 180–229 (compás 4) · pulsos 180 (pico), 195, 210, 225

- **Grabación:** T2 desde el primer cuadro con «¡Listo!» (la espera del envío, 6–12 cuadros reales, se recorta: corte en la pausa).
- **Encuadre:** M sobre el chequeo y la frase de la app (CSS 254–360).
- **Cámara:** 180–193 (el movimiento del compás); quieta después.
- **Texto:** la ceja «ACADEMIA» 195–201; frase 2 quieta.
- **Sonido:** confirmacion 181 (1,4), aparicion 196.
- **Transición:** látigo abajo 230–240 al salir.

#### P4 · «El profesor lo ve» — cuadros 230–349 (compases 5–6) · pulsos 240, 255, 270, 284, 300, 315, 330, 345

- **Grabación:** T3 desde la página desplazada (después del `ver` a la segunda fila de «Faltan») hasta el final de su pausa: ≈ 6 s reales
  para 3,7 s de clip; las esperas entre toques se recortan en pausas (`huecos_de_pantalla`), los toques van a 1×.
- **Encuadre 4:5:** G⁺ con el contador arriba y dos filas de «Faltan» abajo (real; estimado CSS 142–548 de la página desplazada). **9:16:**
  G⁺ muestra 320 px CSS: el contador + los botones + la primera fila; si la segunda no entra, el toque del 300 se encuadra con un movimiento
  de 14 cuadros en el 285–298 (compás 5 ya usó el suyo en el látigo: es la excepción anotada).
- **Cámara:** llega con el látigo; 330–343 a M sobre el contador.
- **Texto:** ninguno nuevo (frase 2 sostenida).
- **Sonido:** desliz 240, toque 271 + aparicion 274, toque 301 + aparicion 304.
- **Transición:** látigo abajo al entrar; látigo arriba al salir (350–360).
- **Si el contador no sube en cámara** (la app lo refresca cada 5 s en vez de al toque): el toque del 270 se queda y el pop se mueve al cuadro
  real en que cambia el número (anotado en el REVIEW); los pulsos de los toques no cambian.

#### P5 · «Por aprobar» — cuadros 350–389 (compás 7) · pulsos 360, 375

- **Grabación:** T5: la pantalla principal de Academia de quien coordina con la tarjeta «Por aprobar» (1,2 s de pausa) y el toque en la
  lista.
- **Encuadre:** G⁺ sobre la tarjeta (real; en 9:16 igual).
- **Cámara:** llega con el látigo; quieta.
- **Texto:** frase 3 entra 360–366 (cuatro palabras a 2 cuadros).
- **Sonido:** desliz 360, toque 376.
- **Transición:** látigo arriba al entrar; iris desde el toque (375–380) al salir.

#### P6 · «Quien cumple, se gradúa» — cuadros 380–599 (compases 7–10) · pulsos 390, 420, 465, 480, 495

- **Grabación:** T6 desde la lista (tramo `lista`) hasta el cuadro anterior al toque de confirmar. **El respiro: nada por encima de 1,2×**
  salvo las pausas de la herramienta; el desplazamiento de la lista (900 ms reales) va a 1×.
- **Encuadre:** G al abrir; M sobre el encabezado y la primera persona (403); G⁺ sobre las últimas filas y la barra (478); M sobre el diálogo
  (508). En 9:16 los mismos objetivos.
- **Cámara:** tres movimientos de 14 cuadros (390, 465, 495), nunca mientras la lista se desplaza (420–447).
- **Texto:** frase 3 quieta; sale 597–601.
- **Sonido:** desliz 421 (0 dB), toque 481.
- **Transición:** iris al entrar; ninguna al salir.
- **Válvula:** si la lista a 390 px trae las filas más altas y a G⁺ no entran dos filas y la barra, el 465 va a **G** (la barra con una fila
  basta: el toque es lo que importa).

#### P7 · «Nueve graduados, con su certificado» — cuadros 600–659 (compás 11) · pulsos 600 (subida), 615, 630, 645

- **Grabación:** T6 desde el toque de confirmar (`aprobado`) hasta el cuadro anterior al toque en «Ver» (`certificados`): el aviso de abajo
  aparece ≈ 3 cuadros después del toque (la espera del servidor se recorta a esos 3, como el resultado de Membresía); el desplazamiento a
  «Certificados (9)» va a 1×.
- **Encuadre:** G⁺ sobre el final de la lista y el aviso (613); M sobre «Certificados (9)» y la primera fila (658).
- **Cámara:** 600–613 y 645–658; quieta mientras la app se desplaza (615–642).
- **Texto:** ninguno (la frase 3 ya salió; la app habla: «¡Listo! 9 graduados, con su certificado.»).
- **Sonido:** toque 601 (1,4), confirmacion 603 (1,4), desliz 616.
- **Transición:** iris desde «Ver» (660–665) al salir.

#### P8 · «El certificado» — cuadros 660–839 (compases 12–14) · pulsos 660 (golpe), 675, 690, 705, 720 (golpe), 735 … 825

- **Grabación:** T7 desde la página del certificado cargada hasta el final (4,5 s de pausa grabada con el bloque del código a la vista; se
  sostiene a 1×). Entre el 665 y el 720 la página está en su posición inicial (la tarjeta arriba); el `ver` a «Copiar el enlace» ocurre en la
  grabación **antes** del cuadro que se usa desde el 720: ese desplazamiento de la app no se muestra (corte en la pausa), lo hace la cámara.
- **Encuadre:** G sobre la tarjeta (665); M sobre «otorga… · Nombre · por haber terminado… Fundamentos bíblicos» (683); desde el 733, G sobre
  «Descargar certificado» · «Código de verificación» · el código · «Copiar el enlace para verificarlo», con la ventana a 0,92 (el cuerpo de la
  app queda en 29 px: justo sobre el piso; si la vista previa lo muestra blando, el encuadre sube a G⁺ y deja fuera «Copiar el enlace»).
- **Cámara:** el punch del 675 (9 cuadros) y el movimiento del 720–733; después muerta de quieta.
- **Texto:** frase 4 entra 720–738 (*líderes* en itálica dorada: el único dorado del cuerpo junto a la ceja); la ceja sale 720–723; la
  frase se sostiene ≥ 3,4 s.
- **Sonido:** toque 661 (1,4); subida 796–853.
- **Transición:** iris al entrar; dip 837–839 y corte duro al 840.

#### La firma — cuadros 840–914

4:5 `identidad/cierre-clip.html`; 9:16 `identidad/cierre-corto.html`; variables `{"llamado":"prueba","fondo":"azul","idioma":"es"}`;
campanas en 28,38 (cuadro 851); la música 0,7 → 0,224 (852) → 0 (870). Es el único gesto de marca del clip.

---

## 3. La grabación: la escena `tools/ayuda/escenas/clips/academia-clase.mjs`

Una sola escena de **celular** (`movil: true`, `toque: false`: 390×844 a 3× → 1170×2532, 30 cps), con `capturar.mjs --modo video` sobre
Kingdom Demo en español:

```bash
cd tools/ayuda
node capturar.mjs clips/academia-clase --idioma es --modo video
# → salida/video/es/clips/academia-clase/grabacion.mp4 + pasos.json (inicio y fin de cada paso, su tramo, la caja, los toques y las teclas)
```

**Cuentas:** 103 = el servidor (Jorge Gallego Gil), profesor de todos los grupos de la demo; 104 = el alumno de captura, inscrito en
«Fundamentos bíblicos»; 101 = el administrador, que coordina Academia. Datos ficticios de Kingdom Demo; ningún texto del clip depende de un
nombre ni de una cifra.

**Estado previo por SQL** (`sql:` corre tras restaurar el volcado, antes de las `refs`): la clase extra de **hoy** («Repaso general», empezada
hace 10 minutos) del grupo en curso de «Fundamentos bíblicos» y la **toma abierta** con una semilla conocida (copiado de
`escenas/academia/marcar-mi-asistencia.mjs`, que ya se usa para las capturas de la ayuda), más **13 asistencias ya marcadas** en esa clase
(todos menos la alumna y cuatro más), para que la clase vaya por la mitad: el contador arranca en «13 de 18 marcaron» y «Faltan (5)».

**El minuto del código** (lo único delicado): el código vale el minuto actual y el anterior, y el profesor (0–4 s) y la alumna (4–6 s) deben
mostrar **los mismos cuatro números**. Las `refs` se consultan una sola vez antes de grabar, así que la primera referencia **duerme hasta el
segundo 1 del minuto siguiente** (`SELECT SLEEP(61 - SECOND(UTC_TIMESTAMP()))`, que devuelve `0`: la herramienta lo acepta como valor) y las
cuatro siguientes calculan los dígitos de ese minuto recién empezado; la toma del profesor y la tecla de la alumna caen en los primeros
≈ 45 s de la grabación, dentro del mismo minuto. **Comprobación obligatoria al grabar:** los cuatro números del cuadro de T1 (a los 0,5 s
de la grabación) son los que entran en las casillas de T2; si no (la corrida empezó tarde o la máquina estaba lenta), se vuelve a grabar.

**Lo que la herramienta ya hace y la escena usa:** `como` e `ir` del primer paso antes de grabar; `escribir` con 70 ms por tecla y las
teclas reales en `pasos.json`; `ver` con desplazamiento suave y la caja; `clicSiHay` (espera 3 s y sigue si no está); `pausa` sin tope en
video; `refs` con `{@nombre}`; `sql`. No necesita nada nuevo.

```js
// Grabación para el clip del sitio público «La clase ya empezó» (LegacyHyperframes/videos/kingdomapp/clip-sitio-academia/SPEC.md §3).
// NO es una escena de un artículo de la ayuda: no se publica ni entra en la frescura. Una sola escena de CELULAR (390×844 a 3x = 1170×2532,
// 30 cps) grabada SIN el círculo del toque (`toque: false`): el montaje dibuja el suyo sobre las cajas y los toques de pasos.json.
//   node capturar.mjs clips/academia-clase --idioma es --modo video
//   → salida/video/es/clips/academia-clase/grabacion.mp4 + pasos.json
// Tres cuentas de Kingdom Demo: 103 (el profesor del grupo), 104 (la alumna inscrita en «Fundamentos bíblicos») y 101 (coordina Academia).
// Tramos: codigo (103) · alumna y digito-1..4 (104) · contador, presente-1 y presente-2 (103) · cerrar-toma y enviar (103, FUERA DE CÁMARA) ·
// por-aprobar · lista · aprobar · aprobado · certificados · certificado (101).
// Estado previo por SQL (el de escenas/academia/marcar-mi-asistencia.mjs, más la clase ya avanzada): una clase extra de HOY del grupo en
// curso de «Fundamentos bíblicos», empezada hace 10 minutos; la toma abierta por el profesor con una semilla conocida; y 13 de los 18
// inscritos ya marcaron (la clase va por la mitad: el contador arranca en «13 de 18 marcaron»). La alumna (104) y cuatro más no han marcado.
const SEMILLA = 'a1c0de5a1c0de5a1c0de5a1c0de5a1c0';
const K_IN = '57075506525303570755065253035707550652530357075506525303570755063636363636363636363636363636363636363636363636363636363636363636';
const K_OUT = '3d6d3f6c3839693d6d3f6c3839693d6d3f6c3839693d6d3f6c3839693d6d3f6c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c5c';
// El código del minuto actual con la regla del backend (acCodigo: HMAC-SHA256('ac:' . minuto, semilla) → los 4 primeros bytes módulo 10 000),
// con las llaves interna y externa del HMAC ya armadas para esa semilla.
const CODIGO = `LPAD(CONV(LEFT(SHA2(CONCAT(UNHEX('${K_OUT}'), UNHEX(SHA2(CONCAT(UNHEX('${K_IN}'), 'ac:', FLOOR(UNIX_TIMESTAMP() / 60)), 256))), 256), 8), 16, 10) % 10000, 4, '0')`;
// El grupo en curso del curso con notas («Fundamentos bíblicos»), donde está inscrita la cuenta 104.
const GRUPO = `(SELECT g.id FROM ac_grupos g JOIN ac_cursos c ON c.id = g.id_curso
                JOIN ac_inscripciones i ON i.id_grupo = g.id JOIN kd_usuario_sedes us ON us.id_persona = i.id_persona AND us.id_usuario = 104
                WHERE c.con_notas = 1 AND g.estado = 'en_curso' ORDER BY g.id LIMIT 1)`;
const ALUMNA = `(SELECT id_persona FROM kd_usuario_sedes WHERE id_usuario = 104 AND estado = 'activo' LIMIT 1)`;
const CLASE = `(SELECT id FROM ac_clases WHERE id_grupo = ${GRUPO} AND extra = 1 ORDER BY id DESC LIMIT 1)`;
const IDIOMA = `(SELECT idioma FROM kd_sedes WHERE codigo = 'KDEMO')`;

export default {
  articulo: 'clips/academia-clase',
  movil: true,
  toque: false,
  pantallas: [
    'frontend-v2/src/app/pages/academia/asistencia/toma.page.ts',
    'frontend-v2/src/app/pages/academia/asistencia.page.ts',
    'frontend-v2/src/app/pages/academia/asistencia/codigo-cuadro.component.ts',
    'frontend-v2/src/app/pages/academia/asistencia/codigo-dialog.component.ts',
    'frontend-v2/src/app/pages/academia/grupo.page.ts',
    'frontend-v2/src/app/pages/academia/graduar/proponer.component.ts',
    'frontend-v2/src/app/pages/academia/cursos.page.ts',
    'frontend-v2/src/app/pages/academia/graduar/por-aprobar.component.ts',
    'frontend-v2/src/app/pages/academia/graduar/revisar-lista.component.ts',
    'frontend-v2/src/app/pages/academia/graduar/persona-fila.component.ts',
    'frontend-v2/src/app/pages/academia/graduar/certificados-grupo.component.ts',
    'frontend-v2/src/app/pages/academia/graduar/certificado.page.ts',
  ],
  sql: [
    // La clase de hoy (una clase extra del grupo, en la hora de la iglesia: Bogotá, UTC−5) y la toma que abrió el profesor.
    `INSERT INTO ac_clases (uuid, id_curso, id_grupo, id_materia, titulo, orden, fecha, duracion_min, estado, extra, propia)
     SELECT UUID(), c.id_curso, c.id_grupo, c.id_materia, IF(${IDIOMA} = 'en', 'General review', 'Repaso general'), c.orden + 1,
            DATE_FORMAT(UTC_TIMESTAMP() - INTERVAL 5 HOUR - INTERVAL 10 MINUTE, '%Y-%m-%d %H:%i:00'), 90, 'programada', 1, 1
     FROM ac_clases c WHERE c.id_grupo = ${GRUPO} ORDER BY c.fecha DESC LIMIT 1`,
    `INSERT INTO ac_tomas (id_sede, id_grupo, id_clase, semilla, desde, hasta, abierta_por)
     SELECT g.id_sede, g.id, c.id, '${SEMILLA}', UTC_TIMESTAMP(), UTC_TIMESTAMP() + INTERVAL 15 MINUTE, 103
     FROM ac_clases c JOIN ac_grupos g ON g.id = c.id_grupo WHERE c.id_grupo = ${GRUPO} AND c.extra = 1`,
    // La clase va por la mitad: 13 inscritos ya marcaron con el código (la toma cuenta las asistencias «presente» de la clase, sin importar la
    // vía). Quedan sin marcar la alumna (104) y cuatro más: dos para los «Presente» del profesor en cámara.
    `INSERT IGNORE INTO ac_asistencias (id_sede, id_grupo, id_clase, id_persona, estado, via, registrado_por, created_at)
     SELECT g.id_sede, g.id, ${CLASE}, i.id_persona, 'presente', 'codigo', 103, UTC_TIMESTAMP() - INTERVAL 4 MINUTE
       FROM ac_inscripciones i JOIN ac_grupos g ON g.id = i.id_grupo
      WHERE i.id_grupo = ${GRUPO} AND i.estado = 'inscrito' AND i.id_persona <> ${ALUMNA}
      ORDER BY i.id_persona LIMIT 13`,
  ],
  refs: {
    // PRIMERO: dormir hasta el segundo 1 del minuto siguiente. Las refs se consultan una sola vez, antes de grabar; así los cuatro dígitos
    // valen el minuto entero (y el siguiente), y el profesor (0–4 s) y la alumna (4–6 s) muestran los mismos números. SLEEP devuelve 0.
    minuto: `SELECT SLEEP(61 - SECOND(UTC_TIMESTAMP()))`,
    grupo: `SELECT ${GRUPO}`,
    clase: `SELECT ${CLASE}`,
    toma: `SELECT id FROM ac_tomas WHERE id_clase = ${CLASE} ORDER BY id DESC LIMIT 1`,
    d1: `SELECT SUBSTRING(${CODIGO}, 1, 1)`,
    d2: `SELECT SUBSTRING(${CODIGO}, 2, 1)`,
    d3: `SELECT SUBSTRING(${CODIGO}, 3, 1)`,
    d4: `SELECT SUBSTRING(${CODIGO}, 4, 1)`,
    // El nombre de la alumna, por si su certificado existe al final (si no, se abre el primero).
    alumna: `SELECT nombre_completo FROM mem_personas WHERE id = ${ALUMNA}`,
  },
  pasos: [
    // ── 1. El profesor (103): el código en pantalla, la clase ya empezada (P1). La entrada se hace antes de grabar: el video abre aquí.
    { tramo: 'codigo', como: 103, ir: '/servir/academia/toma/{@clase}?toma={@toma}', espera: '#ac-toma-codigo', pausa: 4500 },
    { ver: '#ac-toma-contador', bloque: 'nearest', pausa: 300 },                 // solo la caja de «13 de 18 marcaron» (objetivo del 60)

    // ── 2. La alumna (104): el cuadro del código de esa clase, la pantalla que abre el aviso «Tu profesor está tomando asistencia» (P2 y P3).
    { tramo: 'alumna', como: 104, ir: '/servir/academia/asistencia/{@clase}', espera: '#ac-codigo-entrada' },
    { clicSiHay: '#ac-cuadro-x', pausa: 300 },                                   // fuera de cámara: si el cuadro automático se abre encima, se cierra
    { ver: '#ac-cuadro .cajas', bloque: 'center', pausa: 800 },                  // la caja de las cuatro casillas (objetivo del 120)
    { tramo: 'digito-1', escribir: { en: '#ac-codigo-entrada', texto: '{@d1}' }, pausa: 400 },   // el 120 (el bajo)
    { tramo: 'digito-2', escribir: { en: '#ac-codigo-entrada', texto: '{@d2}' }, pausa: 400 },   // el 135
    { tramo: 'digito-3', escribir: { en: '#ac-codigo-entrada', texto: '{@d3}' }, pausa: 400 },   // el 150
    { tramo: 'digito-4', escribir: { en: '#ac-codigo-entrada', texto: '{@d4}' }, espera: '#ac-cuadro-listo', pausa: 2500 },   // el 165 → «¡Listo!» en el 180

    // ── 3. El profesor otra vez (103): la toma con la alumna ya contada («14 de 18 marcaron») y dos «Presente» a quienes no tienen celular (P4).
    { tramo: 'contador', como: 103, ir: '/servir/academia/toma/{@clase}?toma={@toma}', espera: '#ac-toma-faltan [data-marcar]' },
    { ver: '#ac-toma-faltan [data-marcar] >> nth=1', bloque: 'center', pausa: 1500 },   // el contador y las primeras filas de «Faltan» juntos
    { tramo: 'presente-1', clic: '#ac-toma-faltan [data-marcar] >> nth=0', pausa: 600 },       // el 270 → «15 de 18»
    { tramo: 'presente-2', clic: '#ac-toma-faltan [data-marcar] >> nth=0', pausa: 1200 },      // el 300 → «16 de 18»
    { ver: '#ac-toma-contador', bloque: 'nearest', pausa: 1500 },                // la caja de «16 de 18 marcaron» (objetivo del 330)
    // Fuera de cámara: se cierra la toma antes de cerrar el grupo.
    { tramo: 'cerrar-toma', clic: '#ac-toma-cerrar', espera: '#btn-confirm' },
    { clic: '#btn-confirm', espera: '#ac-toma-cerrada' },

    // ── 4. Fuera de cámara (103): el profesor envía la lista de graduación. El grupo se cierra y quien coordina la recibe en «Por aprobar».
    { tramo: 'enviar', ir: '/servir/academia/grupo/{@grupo}?seccion=graduar', espera: '#ac-grad-enviar' },
    { clic: '#ac-grad-enviar', espera: '#btn-confirm' },
    { clic: '#btn-confirm', oculto: 'mat-dialog-container' },

    // ── 5. Quien coordina (101): la tarjeta «Por aprobar» en la pantalla principal de Academia (P5).
    { tramo: 'por-aprobar', como: 101, ir: '/servir/academia', espera: '#ac-por-aprobar a[data-por-aprobar]:has-text("Fundamentos")' },
    { ver: '#ac-por-aprobar', bloque: 'start', pausa: 1200 },
    // ── 6. La lista: cada persona con su nota, su asistencia y si cumple; se recorre y se aprueba (P6 y P7).
    { tramo: 'lista', clic: '#ac-por-aprobar a[data-por-aprobar]:has-text("Fundamentos")', espera: '[data-aprobar]' },   // el 375 (iris)
    { ver: '[data-lista]', bloque: 'start', pausa: 1200 },                       // «Se gradúan 9 · 9 no se gradúan» y la primera persona
    { ver: '[data-lista] [data-excluir] >> nth=3', bloque: 'center', pausa: 900 },   // la lista se desplaza sola (el 420–447)
    { tramo: 'aprobar', clic: '[data-aprobar]', espera: '#btn-confirm', pausa: 3500 },   // el 480: «¿Aprobar la graduación?», quieto 3,5 s
    { tramo: 'aprobado', clic: '#btn-confirm', oculto: 'mat-dialog-container' },         // el 600: «¡Listo! 9 graduados, con su certificado.»
    { espera: '#ac-grad-certificados [data-certificado]', pausa: 800 },
    { tramo: 'certificados', ver: '#ac-grad-certificados', bloque: 'start', pausa: 1500 },   // «Certificados (9)» · «Descargar todos (para imprimir)»
    // ── 7. Un certificado (P8): el de la alumna si se graduó; si no, el primero (clicSiHay espera 3 s y sigue; esa espera se recorta).
    { tramo: 'certificado', clicSiHay: '#ac-grad-certificados li:has-text("{@alumna}") [data-ver-certificado]' },   // el 660 (iris)
    { clicSiHay: '#ac-grad-certificados [data-ver-certificado] >> nth=0' },
    { espera: '#cert-vista', pausa: 2000 },
    { ver: '#cert-persona', bloque: 'center', pausa: 600 },                      // la caja del nombre (objetivo del 675)
    { ver: '#cert-copiar', bloque: 'end', pausa: 4500 },                         // el bloque del código a la vista (objetivo del 720); quieto 4,5 s
  ],
};
```

**Selectores, verificados el 2026-10-30** en `frontend-v2/src/app/pages/academia/`: `#ac-toma-codigo`, `#ac-toma-qr`, `#ac-toma-contador`,
`#ac-toma-restante`, `#ac-toma-extender`, `#ac-toma-cerrar`, `#ac-toma-cerrada`, `#ac-toma-faltan [data-marcar]` (`asistencia/toma.page.ts`);
`#ac-codigo-entrada`, `#ac-cuadro`, `#ac-cuadro .cajas`, `#ac-cuadro-listo` (`asistencia/codigo-cuadro.component.ts`); `#ac-cuadro-x`
(`asistencia/codigo-dialog.component.ts`); `#ac-ir-mis-cursos` (`asistencia.page.ts`, no se usa); `#ac-grad-enviar` (`graduar/proponer.component.ts`);
`?seccion=graduar` (`grupo.page.ts` lee `seccion` del query); `#ac-por-aprobar a[data-por-aprobar]` (`graduar/por-aprobar.component.ts`:
curso, grupo y «{n} para graduar · enviada por {quien} el {fecha}»); `[data-lista]`, `[data-aprobar]`, `[data-devolver]`
(`graduar/revisar-lista.component.ts`); `[data-excluir]` (`graduar/persona-fila.component.ts`); `#ac-grad-certificados`, `#ac-certs-todos`,
`[data-certificado]`, `[data-ver-certificado]` (`graduar/certificados-grupo.component.ts`); `#cert-vista`, `#cert-persona`, `#cert-descargar`,
`#cert-codigo`, `#cert-copiar`, `#cert-verificar` (`graduar/certificado.page.ts`); `#btn-confirm` es el botón del diálogo de confirmación de la
app (lo usan las escenas de la ayuda de Academia). Las columnas de `ac_clases`, `ac_tomas` y `ac_asistencias` son las que usan
`marcar-mi-asistencia.mjs` y `_demo_academia.php` (`demoAcAsistenciasInsertar`). El contador del profesor cuenta las filas `presente` de la
clase sin importar la vía (`acTomaEstado`, `backend/_datos/academia_asistencia.php`), así que las 13 insertadas por SQL suben el contador.

**Totales estimados:** T1 ≈ 5 s · T2 ≈ 9 s · T3 ≈ 8 s · fuera de cámara ≈ 10 s · T5 ≈ 3 s · T6 ≈ 14 s · T7 ≈ 11 s → ≈ 60 s de grabación para 28 s
de clip. Los stills de los dos iris (cuadros 374 y 659) se exportan con `ffmpeg -ss <t> -frames:v 1` y van como `<img>` en `assets/stills/`.

**Plan B si «Por aprobar» o la lista no se usan bien a 390 px:** los tramos 5–7 se graban en escritorio (una segunda escena,
`clips/academia-clase-escritorio.mjs`, sin `movil`, con `alto: 1000`, los mismos pasos desde `por-aprobar`) y en el montaje el mundo 3 es un
**recorte de escritorio** dentro de la misma ventana de 880 px (la grabación de 1920 px a 0,75–1,1× con la cámara dentro: la lista y el
certificado caben en columna; el texto de 14 px queda en 21–31 px, así que la cámara va a ≥ 1,33× sobre ese recorte). La ventana no cambia
de tamaño ni de sitio: cambia lo que hay dentro, como en los otros látigos.

---

## 4. Lo que se revisa en la vista previa

Cuadros a mirar: `npx hyperframes snapshot --at 0,1.5,2.4,3.6,4.0,4.5,5.5,6.0,6.5,8.0,9.0,10.1,11.4,12.0,12.5,13.4,14.5,16.0,17.0,19.5,20.0,20.1,21.9,22.0,22.8,24.0,24.5,27.9,28.0,28.4,30.4`
en las dos composiciones, y `snapshot --range 3.6,4.1 --frames 16`, `--range 7.6,8.1 --frames 16` y `--range 11.6,12.1 --frames 16` para los
tres látigos.

1. **Cuadro 0 (la miniatura):** la ventana con los cuatro números grandes del profesor y la mitad del QR; «La» en Fraunces ya puesta;
   «Datos de ejemplo» en su esquina. Nunca negro, nunca la marca. En 9:16, nada fuera de 168–1330 salvo halo y puntos.
2. **Cuadro 45:** las cuatro palabras quietas; **73:** «13 de 18 marcaron» en el centro de la ventana con el temporizador debajo; entre el 0 y
   el 110 el temporizador cambia al menos tres veces (la app está viva).
3. **110–120:** el látigo sube sin ningún cuadro con la ventana vacía; **120:** el primer número en su casilla exactamente con el bajo y la
   frase 2 entera en el 126; **135 · 150 · 165:** un número por pulso; **los cuatro números son los del cuadro 0.**
4. **180:** «¡Listo! Quedó tu asistencia» con el chequeo, en el pico; la ceja en el 195 y no antes.
5. **230–240:** el látigo **baja**; **240:** «14 de 18 marcaron» legible (el número ≥ 90 px) con dos «Presente» a la vista; **273 y 303:** el
   contador en 15 y 16 (o el cuadro real anotado); **343:** M sobre «16 de 18 marcaron».
6. **350–360:** el látigo sube; la frase 2 ya no está en el 361; la frase 3 completa en el 366; **375:** el toque en la lista y el iris.
7. **403:** «Se gradúan 9 · 9 no se gradúan» y una persona con «Cumple los criterios» a ≥ 44 px; **420–447:** la lista se desplaza sola y la
   cámara no se mueve; **478:** la barra «Devolver al profesor | Aprobar (9)» a la vista; **480:** el toque; **508:** el diálogo «¿Aprobar la
   graduación?» con su título a ≥ 44 px y el botón «Aprobar (9)».
8. **600–603:** el toque de confirmar con la segunda subida, el diálogo que se va y el aviso «¡Listo! 9 graduados, con su certificado.»;
   **658:** «Certificados (9)» y «Descargar todos (para imprimir)» con un «Ver» a la vista; la frase 3 ya no está.
9. **660–665:** el iris desde «Ver»; **683:** el nombre del certificado a ≥ 44 px con «por haber terminado satisfactoriamente el curso
   Fundamentos bíblicos.»; **738:** la frase 4 con *líderes* dorada, la ceja fuera, la ventana a 0,92 y corrida, y el bloque «Código de
   verificación · XXXXX-XXXXX · Copiar el enlace para verificarlo» legible (≥ 29 px el cuerpo, ≥ 40 px el código).
10. **738–836:** nada se mueve salvo el halo; **837–839:** el dip; **840:** el primer cuadro de la firma sin noche vacía.
11. **Sonido (medido):** cada `toque` y cada `aparicion` un cuadro después de su imagen; las cuatro `aparicion` en 121 · 136 · 151 · 166; las
    campanas en el 851; la música a −10 dB en el 852 y a 0 en el 870; −16 LUFS, pico ≤ −1 dBTP; ningún tramo con dos sonidos de acción
    encimados salvo 601 + 603.
12. **Textos:** ninguna palabra que no esté en la app o en las cuatro frases; ningún texto de la app < 28 px; las frases en 2 líneas (3 la
    última en 9:16); `npx hyperframes check` en 0 errores; «Datos de ejemplo» desde el cuadro 0.
13. **La historia sin sonido** (así arranca en el sitio): código en pantalla → la alumna lo escribe → listo → el profesor lo ve → la lista de
    quién cumple → aprobado, con certificado → el certificado y su código → Kingdom.

---

## 5. Riesgos y lo que se decide al grabar

- **El minuto del código.** La escena duerme hasta el segundo 1 del minuto y graba T1 y T2 en los primeros ≈ 45 s; si una corrida sale con
  números distintos en T1 y T2 (se ve en el primer snapshot), se repite. Si `SLEEP` de hasta 61 s molesta al cliente de MariaDB de la
  herramienta (no debería: `sql()` llama al cliente sin tope), la alternativa es lanzar la escena a mano en el segundo 1 y quitar la ref.
- **El cuadro automático de la alumna.** Al entrar con la cuenta 104 el cuadro del código puede abrirse solo encima de la página; la escena lo
  cierra fuera de cámara (`#ac-cuadro-x`). Si se abriera después (entre dígitos), la grabación lo muestra: se vuelve a grabar con el paso de
  cierre repetido antes de `digito-1`.
- **«Por aprobar», la lista y el certificado a 390 px** no tienen captura de celular. Sus componentes traen reglas para pantallas angostas
  (la barra de aprobar sube sobre la navegación por debajo de 840 px) y toda pantalla de v2 se prueba a 360 px, pero las cajas y los encuadres
  del mundo 3 se fijan con la grabación («(real)» en §2). Plan B en §3 (escritorio recortado).
- **La clase extra cambia los porcentajes.** Con una clase más, quien tenía 5 de 6 (83 %) pasa a 5 de 7 (71 %) si no marcó hoy; las 13
  asistencias insertadas cubren a los de siempre, pero «Se gradúan 9» puede ser 8 o 10. Las frases no dependen del número.
- **Que el grupo se cierre con la toma de hoy.** La escena cierra la toma antes de «Enviar para aprobar»; si el cierre del grupo rechazara la
  clase extra «programada» (no lo hace en el código leído: solo avisa «clases sin dictar»), se quita la clase extra del SQL y la toma se abre
  sobre la última clase dictada (el título del cuadro de la alumna cambia; nada más).
- **El contador del profesor se refresca cada 5 s** (`acTomaEstado`) además del toque: el salto a «15» y «16» puede verse 1–4 cuadros después
  del toque. El pop se mueve al cuadro real y se anota en el REVIEW; el pulso del toque no cambia.
- **El certificado de la alumna** solo existe si cumple los criterios (en la demo tiene 50 % de asistencia): lo normal es que el final
  muestre el certificado de otra persona del grupo. Si el dueño prefiere que sea el de la alumna, una línea de SQL en la escena la pone
  «presente» en las clases dictadas (`UPDATE ac_asistencias SET estado = 'presente' WHERE id_grupo = … AND id_persona = …`); se decide con la
  vista previa, no antes.
- **Densidad de 0–8 s:** tres látigos y nueve sonidos en doce segundos. Si en la vista previa va atropellado, la válvula es el látigo del
  240: en vez de volver al profesor, la alumna toca «Ir a Mis cursos» (`#ac-ir-mis-cursos`, real) y la cámara va a su tarjeta «Viniste a N de M
  clases» (el tramo se graba igual agregando ese paso tras `digito-4`); se pierde el contador, se gana calma. Decidirlo viendo.
- **Idiomas (en, pt después):** la misma escena con `--idioma en` graba la interfaz en inglés (la clase extra se llama «General review»); las
  frases se traducen y los saltos se vuelven a fijar; la firma lleva `idioma`.
