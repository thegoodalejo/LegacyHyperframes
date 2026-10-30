# SPEC · Clip del sitio: Equipos — «Falta uno en Parqueadero»

2026-10-30 · Contrato de construcción de la historia elegida en [STORY.md](STORY.md) (el dueño ya no revisa guiones: se eligió aquí). Cada
adjetivo es un número, los valores por defecto están prohibidos con nombre y los planos van cuadro por cuadro sobre la grilla real de la
pista. Se construye desde aquí, se revisa contra esto y se cambia aquí cuando la vista previa cambie la película. Hereda el sistema de
[Membresía](../clip-sitio-membresia/SPEC.md) (mismo reloj, mismas letras, misma ventana, mismas curvas, mismo látigo, misma firma), el
formato de [Eventos](../clip-sitio-eventos/SPEC.md) y las lecciones del [REVIEW de Membresía](../clip-sitio-membresia/REVIEW.md) (ya
aplicadas: niveles del kit, el látigo en una sola tira, entradas un cuadro antes del pulso, «Datos de ejemplo» a 31 px abajo a la izquierda,
encuadres recalculados con las cajas reales, el extractor que atrasa ~2 cuadros en tramos a menos de 1×).

```text
GOAL:    Un pastor que no conoce Kingdom termina pensando «el líder asignó, ella aceptó desde su celular y el líder lo vio sin preguntar:
         el domingo quedó cubierto» y toca «Prueba gratis 30 días».
OUTPUT:  HyperFrames · dos composiciones de la misma línea de tiempo: 1080×1350 (4:5, sitio y feed) y 1080×1920 (9:16, Reels e historias) · 30 fps.
TIME:    30,5 s = 915 cuadros: cuerpo 0–28,0 (cuadros 0–839) + firma 28,0–30,5 (840–914). 120 BPM = 15 cuadros por pulso (grilla real en §0).
LOOK:    noche del sitio (#060D1F) con el halo y la retícula de puntos del kit; tinta #EAF0FF; un solo acento, el dorado #E8B95A, en tres
         lugares y no más (la ceja «EQUIPOS», la palabra «cubierto» y el botón de la firma). Fraunces 560 / −0,02 em para las frases; Inter
         para la ceja y «Datos de ejemplo». El medio: la app REAL de Kingdom Demo grabada en celular, nítida (1170 px de ancho), dentro de
         una ventana con radio 28, anillo de 1 px y sombra 0 40 80 −24 al 65 %; nunca un teléfono dibujado.
OBJECTS: la ventana con una tira de dos mundos (el celular del líder Jorge, arriba; el de Gabriela, abajo); el punto de toque de la
         grabación; las cuatro frases; la ceja; la píldora «Datos de ejemplo»; la corona del cierre. Nada más existe en el cuadro.
MOTION:  curvas por papel (§1.6); a lo sumo un movimiento de cámara por compás (14 cuadros, power2.inOut), quieto después y nunca mientras la
         app escribe o se desplaza; cada corte y cada entrada en un pulso; cada cambio grande en un golpe (120 · 180 · 360 · 600 · 660 · 720 · 840).
SHOTS:   ocho planos (§2).
BANNED:  §1.8.
QA:      §4.
```

---

## 0. El reloj: la grilla real de la pista

La música es «Product Launch» (The_Mountain) del 14,05 al 42,05 s; t = 0 del clip ↔ 14,05 de la pista. Los pulsos vienen de
`_identidad/musica/product-launch-the-mountain.pulsos.json` restándoles 14,05 y redondeando a 30 fps (recalculado el 2026-10-30: idéntico a
Eventos): **todos caen en el múltiplo de 15 cuadros salvo el 9,455 s, que cae en el cuadro 284** (nada ocurre ahí). Cada pulso se calcula
desde su índice, nunca sumando 15 repetidamente.

| Compás | Cuadros | Pulsos (cuadro · fuerza) | Intensidad | Lo que le toca a este clip |
|---|---|---|---|---|
| 1 | 0–59 | 0 ·0,69 · 15 ·0,64 · 30 ·0,49 · 45 ·0,48 | 0,57 | El calendario de Seguridad con «4 de 5 · 1 por cubrir»; la frase 1, una landing por pulso; la cámara a la cobertura |
| 2 | 60–119 | 60 ·0,57 · 75 ·0,55 · 90 ·0,57 · 105 ·0,61 | 0,58 | **75:** toque en el domingo → el turno; 90 la cámara a Parqueadero; 105 el dedo se posa en «Asignar» |
| 3 | 120–179 | **120 ·0,93** (entra el bajo) · 135 ·0,62 · 150 ·0,59 · 165 ·0,51 | 0,66 | **120:** «Asignar» → iris → la lista sugerida. Frase 2. 150 la casilla de Gabriela; 165 la cámara al pie |
| 4 | 180–239 | **180 ·0,87** (pico) · 195 ·0,83 · 210 ·0,67 · 225 ·0,72 | **0,77** | **180:** «Asignar (1)» → «Sin avisar» y la barra «Avisar a 1 persona»; 195 la ceja; 210 la cámara a la barra |
| 5 | 240–299 | **240 ·0,92** · 255 ·0,77 · 270 ·0,58 · 284 ·0,52 | 0,70 | **240:** «Avisar a 1 persona» → «Avisados» |
| 6 | 300–359 | 300 ·0,77 · 315 ·0,74 · 330 ·0,60 · 345 ·0,58 | 0,68 | **300:** «OK» → «Por confirmar»; la cámara a Parqueadero |
| 7 | 360–419 | **360 ·0,76** · 375 ·0,64 · 390 ·0,50 · 405 ·0,46 | 0,59 | **360: látigo** al celular de Gabriela, «Tu próximo servicio»; frase 3. **375:** la tarjeta → iris → su servicio; 390 a «Llega a las…» |
| 8 | 420–479 | 420 ·0,75 · 435 ·0,61 · 450 ·0,49 · 465 ·0,49 | 0,59 | 420 la cámara abre; **450:** la app baja a «Instrucciones» |
| 9 | 480–539 | 480 ·0,67 · 495 ·0,67 · 510 ·0,54 · 525 ·0,50 | 0,59 | 480 acercamiento a los colores y el cronograma |
| 10 | 540–599 | 540 ·0,63 · 555 ·0,56 · 570 ·0,61 · 585 ·0,68 | 0,62 | **540:** la app vuelve arriba; 570 la cámara a «Aceptar»; 596 la marca |
| 11 | 600–659 | **600 ·0,93** (segunda subida) · 615 ·0,69 · 630 ·0,52 · 645 ·0,49 | 0,66 | **600:** «Aceptar» → «¡Gracias por servir! Tu líder ya lo sabe.» y «Confirmado». Frase 3 sale |
| 12 | 660–719 | **660 ·0,90** · 675 ·0,89 · 690 ·0,76 · 705 ·0,68 | **0,81** | **660: látigo de vuelta** → el turno del líder: Gabriela «Confirmado» (la prueba más fuerte); 690 la cámara retrocede: «5 de 5» |
| 13 | 720–779 | **720 ·0,96** · 735 ·0,77 · 750 ·0,59 · 765 ·0,60 | 0,73 | Frase 4; la ceja se va; la ventana se hace a un lado |
| 14 | 780–839 | 780 ·0,88 · 795 ·0,74 · 810 ·0,62 · 825 ·0,60 | 0,71 | Quieto; la subida; el dip |
| — | **840** ·1,00 | el golpe más fuerte de la pista | — | **La firma.** La música se va debajo de las campanas |

Las dos pruebas del clip caen en los dos golpes reales de la segunda subida: «Aceptar» en el 600 (0,93) y el látigo de vuelta con
«Confirmado» en el 660 (el compás más fuerte del cuerpo). El primer látigo, en el 360 (0,76), abre el respiro con el cambio de persona.

---

## 1. Los números del estilo

### 1.1 Paleta (tokens de `identidad/kit.css`; nada fuera de esta lista)

| Papel | Token | Valor | Dónde puede aparecer |
|---|---|---|---|
| Fondo | `--k-noche` | `#060D1F` | A sangre, todo el cuerpo |
| Halo | `.k-halo` | azul `rgba(53,118,218,.45)` arriba a la derecha + dorado `rgba(217,162,52,.22)` abajo a la izquierda | Fondo, bajo todo; se asienta 1,08 → 1 en 0, 180 y 720 |
| Puntos | `.k-puntos` | `rgba(169,190,235,.35)`, 2 px cada 42 px, desvanecidos a la izquierda | Fondo; **nunca se mueven** |
| Tinta | `--k-noche-tinta` | `#EAF0FF` | Las frases |
| Acento | `--k-noche-dorado` | `#E8B95A` | Solo: la ceja «EQUIPOS», la palabra *cubierto*, el botón de la firma |
| Anillo | `--k-noche-linea` | `rgba(234,240,255,.12)` | El borde de la ventana |
| Fondo de la app | `--k-app-fondo` | `#FAF9FD` | Detrás de la grabación y entre los dos mundos de la tira (nunca se ve más de un cuadro) |
| Azul de marca | `--k-azul` | `#3576DA` | **Solo en la firma** (la baldosa) |
| Placa | `.k-datos-ejemplo` | `rgba(6,13,31,.72)` | La píldora «Datos de ejemplo» |
| Dip | — | `rgba(6,13,31,.40)` | Los 3 cuadros antes de la firma, solo sobre la ventana |

Los colores de la app (el rojo de «1 por cubrir», el azul de la barra de cobertura y del chip «Confirmado», el verde agua de «Por confirmar»,
la barra oscura de «Avisar», el ámbar de la tarjeta «Tu próximo servicio», las muestras Negro · Azul oscuro · Gris) viven dentro de la
grabación y no se tocan. `--k-noche-tinta-2` no se usa.

### 1.2 Tipografía

| Pieza | Clase (kit v1.1) | Familia · peso | 4:5 | 9:16 | Interlineado · tracking | Reglas |
|---|---|---|---|---|---|---|
| Frase | `.k-feed-frase` (`.k-titular` + `.k-vertical` en 9:16) | Fraunces 560; `<em>` itálica 500 dorada | **80 px** | **104 px** | 1,04 · −0,02 em | Máx. **2 líneas** en 4:5 (3 en 9:16), saltos fijados a mano. Izquierda. Sin sombra |
| Ceja | `.k-feed-ceja` (`.k-ceja`) | Inter 700, MAYÚSCULAS | **30 px** | **34 px** | 1 · +0,10 em | Una palabra: «EQUIPOS» |
| Datos de ejemplo | `.k-datos-ejemplo .k-feed-datos` | Inter 600 | **31 px**, píldora de 56 px de alto | igual | 1 · 0 | Blanca sobre la placa; **abajo a la izquierda de la ventana**, a 24 px del borde visible |
| Texto de la app | (grabación) | Inter de la app: 14 px CSS el cuerpo, 24 px el `h1`, **11–12 px las marcas y los chips** | ≥ **28 px** lo que se lee | ≥ **28 px** | — | Las marcas de 11 px («✓ Habilidad», «0 en 60 días», «Sin app») y los chips de 11–12 px («1 por cubrir», «Por confirmar», «Confirmado», «5 de 5») **solo se leen desde M o más cerca** (§1.5); en G pasan, no se leen |

Saltos de línea fijados (4:5, ≈ 23 caracteres por línea a 80 px en 888 px):
«¿Quién cubre / el domingo?» · «Kingdom sugiere / a quién poner» · «Y sabe a qué / hora llegar» · «Que cada puesto de / servicio esté
*cubierto*». En 9:16 (≈ 19 por línea a 104 px) la frase 4 va en tres: «Que cada puesto / de servicio / esté *cubierto*»; las demás igual. Si
`check` mide la línea 2 de la frase 4 por encima de 888 px, el salto pasa a «Que cada puesto / de servicio esté *cubierto*» y se mide otra
vez; nunca se achica la letra.

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
| Látigo (la tira) | **1100 px** por mundo | **1000 px** por mundo |
| Ventana al final (desde el 724) | escala **0,92** desde el centro inferior + x **+48** | escala 0,92 desde el centro superior + x **+36** |
| Datos de ejemplo | abajo a la izquierda de la ventana, 24 px del borde visible | ídem |
| Firma | `cierre-clip` (kit v1.1) | `cierre-corto` (kit v1) |

Variables de `index.html` (como en Membresía): 4:5 `--f-k: 0.752137`, `--f-grab-alto: 1904.41px`, `--f-latigo: 1100px`; 9:16
`--f-k: 0.820513`, `--f-grab-alto: 2077.54px`, `--f-ventana-hvis: 850px`, `--f-latigo: 1000px`. La tira lleva dos `.mundo` apilados: **`#m1`
arriba (el celular de Jorge) y `#m2` abajo (el de Gabriela)**, cada uno con su envoltorio (`#m1in`, `#m2in`) para su aterrizaje y su propia
cámara (`#cam1`, `#cam2`). El 360 la tira **sube** un mundo (entra `#m2` desde abajo); el 660 **baja** un mundo (vuelve `#m1` desde arriba). Los
dos mundos son la misma grabación en tramos distintos.

### 1.5 La cámara dentro de la ventana: escalas y objetivos

Grabación a 3× (390×844 px CSS → **1170×2532 px**). **ppc** = píxeles del cuadro por píxel CSS del celular. Lo visible de la app en el
celular va del 56 (bajo la barra «Kingdom Demo») al 770 (sobre la barra inferior).

| Nivel | Qué se ve | 4:5: ppc (escala del video) · visibles en px CSS | 9:16: ppc (escala) · visibles | 14 px → · 11 px → |
|---|---|---|---|---|
| **G** general | todo el ancho del celular | **2,256** (0,752) · 390 × 439 | **2,462** (0,821) · 390 × 345 | 31,6 · 24,8 (no se lee) |
| **G⁺** | una tarjeta con sus márgenes | 2,436 (0,812) · 361 × 406 | 2,659 (0,886) · 361 × 320 | 34 · 26,8 (no se lee) |
| **F** final (con la ventana a 0,92) | el turno de la cabeza a Parqueadero | 2,572 (0,857) · 342 × 385; en pantalla ×0,92 → 2,366 | 2,708 (0,903) · 354 × 314; ×0,92 → 2,491 | 33 · 28,4 / 29,9 |
| **M** medio | una zona: la tarjeta, el diálogo, un grupo de puestos | **3,158** (1,053) · 279 × 313 | **3,446** (1,149) · 279 × 247 | 44 · **34,7** |
| **C** cerrado | una línea | **4,061** (1,354) · 217 × 244 | **4,431** (1,477) · 217 × 192 | 57 · 44,7 |

G = ×1,00 · G⁺ = ×1,08 · F = ×1,14 (×1,10 en 9:16) · M = ×1,40 · C = ×1,80 sobre el general. La cámara es `scale` + `x`/`y` sobre `#cam1` o
`#cam2`, sujeta a los bordes de la grabación (función `enc()` de Membresía); el `<video>` nunca se transforma ni se busca. El objetivo de cada
movimiento es una **caja de `pasos.json`** (px CSS del viewport 390×844). Las cajas de abajo son estimaciones medidas sobre las capturas
publicadas de la ayuda (`equipos/calendario-y-turnos/01-calendario`, `equipos/asignar-y-avisar/02-sugerencias`,
`mi-iglesia/responder-un-servicio/01-tarjeta` y `02-asignacion`, pasadas a 390 px) y sobre los estilos de las pantallas; **las reales salen de
la grabación** y se anotan en el REVIEW.

| Objetivo | Mundo | Nivel | Centro estimado (x, y CSS) | Lo que debe quedar dentro |
|---|---|---|---|---|
| `semana` | 1 | M | (195, 400) → 243–556 | «Dom, 1 de nov» y su fila entera: «9:00 a. m.», «Servicio General», la barra de cobertura, «4 de 5», **«1 por cubrir»**; arriba puede asomar el aviso «Tienes N asignaciones sin avisar» (real) |
| `por-cubrir` | 1 | C | (130, 430) → 308–552, x 21–238 | la fila del domingo de «9:00 a. m.» a «1 por cubrir» a 45 px; el centro de la fila (el toque del 75) dentro |
| `turno-cabeza` | 1 | M | (195, 230) → 73–386 | «Seguridad» (volver), «Domingo, 1 de noviembre», **«Servicio General»**, «9:00 a. m.», el chip **«4 de 5»**, «Copiar del turno anterior · Sumar puesto» |
| `parqueadero` | 1 | M | (195, 440) → 283–596 | **«Parqueadero · 1 de 2 · Asignar»**, «Rut Londoño Isaza · Confirmado», el puesto punteado «Vacante» (después Gabriela con su chip), el título «Entrada» |
| `sugerencias` | 1 | M | (195, 285) → 128–441 | **«Asignar · Parqueadero»**, «Asignar por un periodo», «Elige a una persona…», el buscador, la fila de **Gabriela** con «✓ Habilidad · 0 en 60 días» y la segunda fila con «Sin app» |
| `pie` | 1 | G | (195, 560) → 340–779 | antes del 180: las filas de abajo y **«Cancelar · Asignar (1)»**; después: los dos puestos de Parqueadero, Entrada y la barra oscura «Avisar a 1 persona» |
| `avisar` | 1 | M | (195, 606) → 449–762 | la fila de Gabriela con **«Sin avisar»** y la barra **«1 asignación sin avisar · Avisar a 1 persona»** |
| `avisados` | 1 | M | (215, 422) → 265–578, x 75–354 | el diálogo entero: **«Avisados»**, «Le llegó el aviso a 1 persona. Verás aquí cuando responda.», «OK» |
| `tarjeta` | 2 | G⁺ | (195, 272) → 69–475 | «Buenos días, Gabriela», «Iglesia Kingdom Demo 1» y la tarjeta **«Tu próximo servicio»** entera con «Aceptar · No puedo» |
| `servicio-cabeza` | 2 | M | (195, 250) → 93–406 | «Domingo, 1 de noviembre», **«Parqueadero»** (76 px), «Seguridad · Servicio General», «Llega a las 7:45 a. m.», «Empieza a las 9:00 a. m.», la dirección, «Por confirmar» |
| `llegada` | 2 | C | (150, 245) → 123–367, x 42–259 | **«Llega a las 7:45 a. m.»** (con su reloj) a 57 px, con «Parqueadero» arriba y «Empieza a las…» abajo |
| `servicio` | 2 | G | (195, 275) → 56–495 | toda la parte alta; después del 450: «Instrucciones», «Oficina de la entrada principal», «Uniforme del equipo · Chaleco reflectivo…», «Colores» |
| `paleta` | 2 | M | (195, 480) → 323–636 | después del 450: **Negro · Azul oscuro · Gris** y el cronograma (7:45 · 8:00 · 8:30) |
| `botones` | 2 | M | (195, 360) → 203–516 | «Llega a las…», la dirección, el chip, **«Aceptar · No puedo»** y «Quiénes más sirven ese día»; después del 600: «Confirmado», **«¡Gracias por servir! Tu líder ya lo sabe.»** y «Ya no puedo» |
| `cierre` | 1 | F | (195, 340) → 148–533 (9:16: 200–514) | «Servicio General», el chip **«5 de 5»**, Parqueadero «2 de 2» con Rut y **Gabriela «Confirmado»** (en pantalla ≥ 28 px con la ventana a 0,92) |

### 1.6 Curvas y duraciones (cada tween lleva su curva por nombre)

| Papel | Curva | Cuadros | Detalle |
|---|---|---|---|
| `entrada-palabra` | `power4.out` | 4 | `filter: blur(6px) → 0` + opacidad; **sin desplazamiento**; arranca un cuadro antes del pulso (el primer cuadro visible es el pulso). Palabras a 2 cuadros, salvo la frase 1 (una landing por pulso) |
| `entrada-linea` | `power4.out` | 6 | la línea entera, blur 8 → 0 (frase 2 y ceja) |
| `salida-texto` | `power3.in` | 4–5 | blur 0 → 8 + opacidad, la línea entera, 2–3 cuadros antes del pulso («blur swap») |
| `camara` | `power2.inOut` | **14** | a lo sumo uno por compás; quieta después; **nunca mientras la app se desplaza** (450–459, 540–549) |
| `retroceso` | `power2.inOut` | **9** | solo el del 690 (M `parqueadero` → F `cierre`): el «punch» de la serie, hacia afuera |
| `aterrizaje-app` | `power3.out` | 10 | el match cut del 78: el turno entra a **1,03 → 1,00** en `#m1in`, origen en el centro de lo visible. Es la única vez |
| `iris` | `power2.out` | 5 | `clip-path: circle(0 at X Y) → circle(1900px at X Y)`, X Y = el centro del botón tocado (caja de `pasos.json`) en px de la grabación ajustada; debajo, un still del cuadro anterior. **Dos:** 120–125 desde «Asignar» (`#m1`) y 375–380 desde la tarjeta (`#m2`). La cámara del mundo salta al objetivo nuevo **dentro** del iris |
| `latigo` | `power3.inOut` | **10** | una sola tira (lección del REVIEW de Membresía: nunca dos curvas, nunca un cuadro con la ventana vacía): **356–366** la tira sube `--f-latigo` (el más rápido en el 361); **656–666** baja `--f-latigo` (el más rápido en el 661). El mundo que llega aterriza 1,04 → 1,00 en su envoltorio (360–370 y 660–670). El blur de render hace la estela; nada de `filter` |
| `dedo-espera` | `power2.out` | 4 | la marca de toque aparece y **se queda quieta** hasta el toque: 105 → 120 (una sola vez, la del bajo). Las demás aparecen 4 cuadros antes de su toque |
| `toque` | `power2.out` / `power2.in` | 4 · 2 · 6 | la marca aparece (opacidad 0 → 1, escala 0,6 → 1), se hunde a 0,86 en el cuadro y se va 6 después; la onda 36 → 58 px CSS en 0,45 s, `#015BBE` al 90 % |
| `ventana-cambio` | `power2.inOut` | 15 | escala 1 → 0,92 + x (§1.4), 724–738 |
| `halo` | `sine.out` | 90 | 1,08 → 1,00 en 0, 180 y 720; los puntos no se mueven |
| `dip` | escalón | 3 | 837–839 |
| firma | las del kit | 75 | `back.out(2.2)` de la corona; **no se imita en el cuerpo** |
| resortes | ninguno | — | nada rebota salvo la corona |
| velocidad de la grabación | `data-playback-rate` por tramo (o carril `rate`) | — | entre **0,35× y 3,5×**; las rampas van entre acciones, nunca durante un toque. Los cortes caen en los `huecos_de_pantalla` de `pasos.json` y en las esperas de la API |

`data-motion-blur="on"` con `data-motion-blur-shutter="180"` en la raíz. **Nunca `filter: blur()` sobre la grabación.**

### 1.7 Sonido

| Capa | Fuente | Nivel | Regla |
|---|---|---|---|
| Música | `assets/musica/product-launch-the-mountain.mp3`, `data-media-start` 14,05, dura 29 s | 0,7 en el carril de volumen (−18 LUFS, `kit.json`) | 0,7 hasta el 840 → 0,224 en el 852 → 0 en el 870 |
| Sonidos de acción (kit v1.1) | `toque` · `aparicion` · `desliz` · `subida` · `confirmacion` | el nivel del kit (`data-volume="1"`, 4–10 dB bajo la música); **1,4** solo en los tres toques clave (121 · 181 · 601), en los dos `desliz` de los látigos y en la `confirmacion` del 603 | `data-start` = cuadro / 30 − acento; el pico suena **un cuadro después** de su imagen. `toque` rota a (`toque.wav`), b (+3 %), c (−3 %), nunca la misma dos veces seguidas. Sin tics de tecla (no se escribe nada) |
| Sonido de marca | `identidad/audio/sonido-marca.wav` | tal cual | en **28,38 s** (cuadro 851) |
| Mezcla | — | −16 LUFS integrados, pico real ≤ −1 dBTP | `normalize-audio` sobre el render de entrega; se comprueba con `hyperframes audio --json`. Si el normalizador recorta, los 1,4 bajan a 1,2 |

Los 20 eventos, con su causa (cuadro del sonido = imagen + 1):

| Cuadro | Sonido | Causa |
|---|---|---|
| 76 | toque a | la fila del domingo |
| 121 | toque c (1,4) | «Asignar» (el bajo) |
| 151 | toque a | la casilla de Gabriela |
| 181 | toque b (1,4) | «Asignar (1)» (el pico) |
| 184 | aparicion | la barra «Avisar a 1 persona» sube |
| 196 | aparicion | la ceja «EQUIPOS» |
| 241 | toque c | «Avisar a 1 persona» |
| 243 | confirmacion (1,0) | «Avisados» |
| 301 | toque a | «OK» |
| 304 | aparicion | el chip pasa a «Por confirmar» |
| 349–361 | desliz (1,4) | el látigo de ida (acento en el 360) |
| 376 | toque b | la tarjeta «Tu próximo servicio» |
| 451–463 | desliz | la app baja a «Instrucciones» (acento en el 455) |
| 541–553 | desliz | la app vuelve arriba (acento en el 545) |
| 601 | toque c (1,4) | «Aceptar» (la segunda subida) |
| 603 | confirmacion (1,4) | «¡Gracias por servir! Tu líder ya lo sabe.» |
| 649–661 | desliz (1,4) | el látigo de vuelta (acento en el 660) |
| 663 | confirmacion (1,0) | «Confirmado» en el turno del líder |
| 796–853 | subida | su golpe (acento 1,5 s) en el 840 |
| 851 | campanas | la firma + 0,38 |

Ninguno sin causa visible; 0–6 s lleva cinco. Nada de whoosh en los movimientos de cámara, en el iris ni en el retroceso del 690.

### 1.8 BANNED: los valores por defecto prohibidos, con nombre

Los 20 de Membresía valen enteros (fundido de 0,5 s para todo; fade + deslizar hacia arriba; zoom lineal; «creeping scale»; fundido
cruzado entre mundos; teléfono dibujado; texto que se mueve mientras se lee o «respira»; logo en una esquina; brillo, neón, partículas,
orbes; degradados nuevos y tarjetas de vidrio; tres tarjetas en fila, KPI, «01 / 02», corner brackets, HUD; whoosh en cada corte y el mismo
`toque` sin rotar; reproducción fuera de 0,35×–3,5×; retocar un píxel de la app; texto de la app < 28 px; centrarlo todo; cifras sin «Datos
de ejemplo»; más de 3 s sin cambio visible; un pulso vacío entre el 0 y el 360; `from()`, `autoAlpha` sobre un `.clip`, `transform` de CSS
donde GSAP transforma, el `<video>` y su envoltorio con tiempo a la vez), los 26 de Eventos donde apliquen (21 la cámara y el desplazamiento a
la vez; 22 más de tres `confirmacion` o dos a menos de 1 s; 25 una marca donde no se tocó). Y los de este clip:

27. **Dibujar el aviso del celular** (la notificación «Te asignaron: …» del sistema) entre los dos mundos, o un globo, un sobre o una flecha
    que «viaja» de un celular al otro. La grabación no lo tiene y el látigo ya cuenta el viaje: nada inventado.
28. **Recrear o «ayudar» a la app:** la lista sugerida, los chips («Sin avisar», «Por confirmar», «Confirmado», «5 de 5»), la barra oscura o
    el «¡Gracias por servir!» como gráficos propios, o animar el cambio de un chip con un tween. Todo sale de la grabación.
29. **Leer las marcas de 11 px desde G.** «✓ Habilidad», «0 en 60 días», «Sin app» y los chips se leen solo en M o C (§1.5); el plano que
    los necesita está en M.
30. **Un tercer látigo, o un látigo en otra dirección.** Ida = la tira sube (el celular de ella llega desde abajo); vuelta = baja. Ningún
    otro cambio de pantalla usa el látigo (el diálogo y el servicio de ella entran por iris; el turno, por el match cut).
31. **Mostrar «Redes y solicitudes».** En el sitio es «Próximamente»: el chip «Abierto a redes» del puesto vacante y el del apoyo de red de
    Entrada no aparecen (la escena los apaga en la base local, §3), y la cámara no visita «Vacantes abiertas» ni «Solicitudes».
32. **Marcar la sugerencia «a mano»:** ningún subrayado, círculo o brillo sobre la fila de Gabriela; la fila elegida se llena sola en la app.

Después del primer render, cada valor por defecto que aun así aparezca se nombra aquí y se corrige.

---

## 2. Los planos, cuadro por cuadro

### 2.0 Convenciones

- **G / G⁺ / F / M / C** y los nombres de objetivo (`semana`, `parqueadero`, `botones`…): §1.5. «Sobre X» = la caja de X centrada en la
  ventana. **Mundo 1** = el celular de Jorge (cuenta 103); **mundo 2** = el de Gabriela (cuenta 105).
- **Pulso**: el cuadro de la grilla de §0. Un evento «en el 120» aterriza en el cuadro 120 (su sonido suena en el 121).
- **Grabación**: una sola, `clips/equipos-parqueadero`, con los tramos `calendario · turno · asignar · elegir · asignado · avisar ·
  por-confirmar · gabriela · servicio · instrucciones · arriba · aceptar · lider` (§3). Los cortes de video caen en pausas de la grabación o
  bajo un látigo.
- **Textos de la app**: son los reales, verificados en `frontend-v2/public/i18n/es.json` (`eq.*`) y en las pantallas: «Calendario», «{n} de
  {total}», «{n} por cubrir», «Asignar», «Vacante», «Confirmado», «Asignar · {funcion}», «Asignar por un periodo», «Elige a una persona. Queda
  sin avisar hasta que toques «Avisar».», «Buscar integrante», «✓ Habilidad», «{n} en 60 días», «Sin app», «Asignar ({n})», «Sin avisar», «1
  asignación sin avisar», «Avisar a 1 persona», «Avisados», «Le llegó el aviso a 1 persona. Verás aquí cuando responda.», «Por confirmar»,
  «Tu próximo servicio», «Llega a las {hora}», «Aceptar», «No puedo», «Empieza a las {hora}», «Quiénes más sirven ese día», «Instrucciones»,
  «Lugar de encuentro», «Vestimenta», «Colores», «Cronograma», «¡Gracias por servir! Tu líder ya lo sabe.», «Ya no puedo». Y de la semilla
  (`backend/cron/jobs/_demo_servicio.php`): «Seguridad», «Parqueadero», «Servicio General», «Oficina de la entrada principal», «Uniforme del
  equipo · Chaleco reflectivo y carné a la vista», «Negro · Azul oscuro · Gris», los tres pasos del cronograma, llegada 75 min antes del culto
  de las 9:00 (= 7:45 a. m.). Lo que cambia con el día y la semilla (la fecha, «Buenos días», los nombres de la lista, cuántas confirmadas)
  lleva «(real)».
- Las frases siempre en el mismo lugar (§1.4); una frase a la vez; la ceja encima de la frase.
- **Posiciones CSS** de la app: estimadas (§1.5); las reales, de `pasos.json`.

### 2.1 Tabla maestra (todo lo que cambia, por cuadro)

| Cuadro | Pulso | La app (grabación) | Cámara | Texto | Sonido | Transición |
|---|---|---|---|---|---|---|
| **0** | ● | Mundo 1 · tramo `calendario` · Seguridad → Calendario, desplazado al primer domingo: «Dom, 1 de nov (real)» · «9:00 a. m.» · **«Servicio General»** · la barra a 4/5 · **«4 de 5» (real)** · **«1 por cubrir»** en rojo; debajo, «Dom, 8 de nov». «Datos de ejemplo» abajo a la izquierda | M `semana` | **«¿Quién»** ya aterrizada (es la miniatura) | — | — |
| 15 · 30 · 45 | ● ● ● | quieta | quieta | **«cubre»** 15 · **«el»** 30 · **«domingo?»** 45. Frase 1 completa y muerta de quieta hasta el 117 | — | |
| 46–59 | | quieta | **Movimiento del compás 1**: M → **C `por-cubrir`** («4 de 5 · 1 por cubrir» a 45 px) | | — | |
| 71–81 | **75 ●** | **75: toque en la fila del domingo** → la app navega al turno; el corte cae en la espera | quieta en C | | `toque` a en el 76 | **Match cut sobre el toque:** en el 78 la pantalla ya es el turno, en M `turno-cabeza`, y entra 1,03 → 1,00 (`aterrizaje-app`, 78–88) |
| 78–89 | | **El turno (real):** «Seguridad» ← · «Domingo, 1 de noviembre» · **«Servicio General»** · «9:00 a. m.» · el chip **«4 de 5»** · «Copiar del turno anterior» · «Sumar puesto» | M `turno-cabeza` | | — | |
| **90–103** | ● | quieta | **Movimiento del compás 2**: M → **M `parqueadero`**: «Parqueadero · 1 de 2 · **Asignar**», «Rut Londoño Isaza (real) · Confirmado», el puesto punteado **«Vacante»** | | — | |
| **105** | ● | quieta | quieta | | — | **`dedo-espera`:** la marca aparece sobre «Asignar» (105–109) y se queda |
| 117–121 | | | | la frase 1 sale | | |
| **120** | **●●● bajo** | **toque en «Asignar»** → el diálogo **«Asignar · Parqueadero»** con la lista sugerida (real): arriba **«Gabriela Hinestroza Perea · ✓ Habilidad · 0 en 60 días»**, debajo «Gilberto Rojas Córdoba (real) · ✓ Habilidad · 4 en 60 días · Sin app»… | salta a **M `sugerencias`** dentro del iris | **«Kingdom sugiere / a quién poner»** entrada-linea 120–126 | **`toque` c (1,4) en el 121** | **Iris desde «Asignar»** 120–125 (still del 119 debajo) |
| 135 | ● | la lista quieta (las marcas se leen a 35 px) | quieta | frase 2 quieta | — | |
| **150** | ● | **toque en la casilla de Gabriela** → la fila se llena (secondary container) y el botón dice **«Asignar (1)»** | quieta | | `toque` a en el 151 | |
| **165–178** | ● | quieta | **Movimiento del compás 3**: M → **G `pie`** (las filas de abajo y «Cancelar · Asignar (1)») | | — | |
| 176 | | | | la frase 2 sale 177–181 | | la marca aparece sobre «Asignar (1)» |
| **180** | **●●● pico** | **toque en «Asignar (1)»** → el diálogo se cierra (≈ 150 ms) y en Parqueadero está **Gabriela Hinestroza Perea · «Sin avisar»** (chip punteado), «2 de 2»; sube la barra oscura **«1 asignación sin avisar · Avisar a 1 persona»** (≈ 183) | quieta en G `pie` | — | **`toque` b (1,4) en el 181**; `aparicion` en el 184 | halo 1,08 → 1 (180–270) |
| **195** | ● | quieta | quieta | **«EQUIPOS»** entrada-linea 195–201 | `aparicion` en el 196 | |
| **210–223** | ● | quieta | **Movimiento del compás 4**: G → **M `avisar`** (la fila de ella con «Sin avisar» y la barra) | | — | |
| 236 | | | | | | la marca aparece sobre «Avisar a 1 persona» |
| **240** | **●●** | **toque en «Avisar a 1 persona»** → el diálogo **«Avisados · Le llegó el aviso a 1 persona. Verás aquí cuando responda.» · OK** (entra en ≈ 150 ms) | **Movimiento del compás 5**: M → **M `avisados`**, 240–253 | | `toque` c en el 241; **`confirmacion` (1,0) en el 243** | |
| 296 | | | | | | la marca aparece sobre «OK» |
| **300** | ● | **toque en «OK»** → el diálogo se va y el turno se recarga: Gabriela **«Por confirmar»** (verde agua), la barra oscura ya no está | **Movimiento del compás 6**: M → **M `parqueadero`**, 300–313 | | `toque` a en el 301; `aparicion` en el 304 | |
| 315–355 | ● ● ● | quieta: «Rut · Confirmado», «Gabriela · Por confirmar» | quieta | | — | |
| **356–366** | **360 ●** | Mundo 2 · tramo `gabriela` · Mi iglesia: «Buenos días, Gabriela (real)» · «Iglesia Kingdom Demo 1» · la tarjeta **«Tu próximo servicio · Dom, 1 de nov · Servicio General · Parqueadero · Seguridad · Llega a las 7:45 a. m.» · Aceptar · No puedo** | `#cam2` en **G⁺ `tarjeta`** | **«Y sabe a qué / hora llegar»**: Y 360 · sabe 362 · a 364 · qué 366 · hora 368 · llegar 370 | **`desliz` (1,4) 349–361** | **Látigo de ida**: la tira sube 1100 px (356–366, el más rápido en el 361); `#m2in` aterriza 1,04 → 1,00 (360–370). Debajo, el cambio de cuenta de la grabación |
| **375** | ● | **toque en la tarjeta** → su servicio (real): «Domingo, 1 de noviembre» · **«Parqueadero»** · «Seguridad · Servicio General» · **«Llega a las 7:45 a. m.»** · «Empieza a las 9:00 a. m.» · la dirección (real) · **«Por confirmar»** · Aceptar · No puedo | salta a **M `servicio-cabeza`** dentro del iris | frase 3 quieta | `toque` b en el 376 | **Iris desde la tarjeta** 375–380 (still del 374 debajo) |
| **390–403** | ● | quieta | **Movimiento del compás 7**: M → **C `llegada`** («Llega a las 7:45 a. m.» a 57 px) | | — | |
| **420–433** | ● | quieta | **Movimiento del compás 8**: C → **G `servicio`** | | — | |
| **450–459** | ● | **la app baja a «Instrucciones»** (`ver #instrucciones`, 300 ms reales a 1×): pasan «Quiénes más sirven ese día» y sus filas (real) y entran **«Instrucciones» · «Oficina de la entrada principal» · «Uniforme del equipo · Chaleco reflectivo y carné a la vista» · «Colores»** | **quieta** (G) | | `desliz` (acento 455) | |
| **480–493** | ● | quieta | **Movimiento del compás 9**: G → **M `paleta`**: **Negro · Azul oscuro · Gris** y el cronograma «7:45 a. m. Llegada: recoge tu radio y tu chaleco» · «8:00 a. m. Reunión con el líder: los puestos del día» · «8:30 a. m. Cada uno en su puesto…» | | — | |
| **540–549** | ● | **la app vuelve arriba** (`ver #servicio-aceptar`, 300 ms): entran la cabecera y **«Aceptar · No puedo»** | **quieta** (M `paleta`) | | `desliz` (acento 545) | |
| **570–583** | ● | quieta | **Movimiento del compás 10**: M → **M `botones`** («Llega a las…», el chip «Por confirmar», «Aceptar · No puedo») | | — | |
| 596 | | | | la frase 3 sale 597–601 | | la marca aparece sobre «Aceptar» |
| **600** | **●●● 2.ª subida** | **toque en «Aceptar»** → **«¡Gracias por servir! Tu líder ya lo sabe.»** (✓, entra ≈ 602) entre la cabecera y los botones; el chip pasa a **«Confirmado»** (azul); en lugar de los botones queda «Ya no puedo» | quieta en M `botones` (la app cambia, la cámara no: es la primera prueba) | | **`toque` c (1,4) en el 601**; **`confirmacion` (1,4) en el 603** | |
| 615–655 | ● ● ● | quieta: el anuncio, «Confirmado» | quieta | | — | |
| **656–666** | **660 ●●● golpe** | Mundo 1 · tramo `lider` · el turno recién abierto (real): Parqueadero «2 de 2» · «Rut Londoño Isaza · Confirmado» · **«Gabriela Hinestroza Perea · Confirmado»** | `#cam1` en **M `parqueadero`** (el mismo encuadre en que se dejó en el 313) | | **`desliz` (1,4) 649–661**; **`confirmacion` (1,0) en el 663** | **Látigo de vuelta**: la tira baja 1100 px (656–666, el más rápido en el 661); `#m1in` aterriza 1,04 → 1,00 (660–670). Debajo, el cambio de cuenta |
| **690–698** | ● | quieta | **Retroceso** M → **F `cierre`** (9 cuadros): aparece arriba el chip **«5 de 5» (real)** y «Servicio General» | — | — | |
| **720** | **●●● golpe** | quieta (el turno real) | quieta en F `cierre` | **«Que cada puesto de / servicio esté *cubierto*»**: Que 720 · cada 722 · puesto 724 · de 726 · servicio 728 · esté 730 · *cubierto* 732. **La ceja sale 720–723** | — | **La ventana se hace a un lado**: escala 1 → 0,92 + x (§1.4), 724–738; halo 1,08 → 1 (720–810) |
| 735–836 | 735 … 825 | quieta | quieta | frase 4 quieta ≥ 3,5 s | **`subida`** 796–853 (golpe en el 840) | |
| **837–839** | | — | — | — | — | **Dip** al 40 %, 3 cuadros |
| **840** | **●●● el más fuerte** | — | — | — | la música 0,7 → 0,224 (852) → 0 (870) | **Corte a la firma**: 4:5 `cierre-clip`, 9:16 `cierre-corto`; `{"llamado":"prueba","fondo":"azul","idioma":"es"}` |
| 846 · 853 ↓ | | la K sube; las 7 barras de la corona desde 0,45 s (`back.out(2.2)`) | | «Kingdom» 0,75 s; **«Prueba gratis 30 días»** 0,95 s | **Campanas en el 851** | |
| **914** | | último cuadro: la corona completa y el botón | | | silencio de música desde el 870 | fin |

### 2.2 Los ocho planos

#### P1 · «¿Quién cubre el domingo?» — cuadros 0–119 (compases 1–2) · pulsos 0, 15, 30, 45, 75, 90, 105

- **Grabación:** tramos `calendario` (el calendario ya desplazado al primer domingo, quieto 2,5 s; se usa a 1×) y `turno` (el toque y la
  carga del turno; el corte cae en la espera). Lo demás, a 1×.
- **Encuadre 4:5:** M `semana` (0–45), C `por-cubrir` (59–77), M `turno-cabeza` (78–89), M `parqueadero` (103–119). **9:16:** M muestra 247
  px CSS: `semana` se centra en la fila (sin el aviso de arriba); los demás igual.
- **Cámara:** quieta hasta el 45; 46–59 a C; el match cut del 78 cambia de encuadre (corte con causa); 90–103 a `parqueadero`. Nada más.
- **Texto:** frase 1 por pulsos (la primera landing ya puesta en el cuadro 0); sale 117–121.
- **Sonido:** toque 76.
- **Transición:** el match cut sobre el toque del 75 (`aterrizaje-app` 78–88); cierra con el iris del 120.
- **Válvula si el turno tarda en cargar** (más de 0,5 s en la grabación): el corte en la espera se alarga, nada cambia en el clip; si en el 78
  la pantalla nueva no está, el toque se adelanta al 60 y el compás 1 se queda sin movimiento (la fila se lee en M).

#### P2 · «Kingdom sugiere a quién poner» — cuadros 120–179 (compás 3) · pulsos 120 (bajo), 135, 150, 165

- **Grabación:** tramos `asignar` (el toque y el diálogo con la lista, 1,5 s quieto) y `elegir` (la casilla).
- **Encuadre:** M `sugerencias` (120–164): el título, la ayuda, el buscador y las dos primeras filas, las marcas a 35 px. G `pie` desde el 178.
  En 9:16 (247 px CSS en M) se centra en la ayuda y las dos filas; el título queda fuera (la frase 2 ya lo dice).
- **Cámara:** salta a M dentro del iris; 165–178 a G. Ninguna otra.
- **Texto:** frase 2 entra 120–126 (línea entera), sale 177–181.
- **Sonido:** toque 121 (1,4), toque 151.
- **Transición:** iris desde «Asignar» (120–125).
- **Si Gabriela no sale primera** (la `ref` `rivales` lo avisa, §3): la cámara se centra en su fila, donde esté; la frase no dice «la
  primera».

#### P3 · «Avisar» — cuadros 180–355 (compases 4–6) · pulsos 180 (pico), 195, 210, 240, 300

- **Grabación:** tramos `asignado` (el diálogo que se cierra, la barra; 1,5 s quieto), `avisar` (el toque y «Avisados», 1,5 s quieto) y
  `por-confirmar` (el «OK», la recarga, 1,5 s quieto). A 1× salvo las pausas, que se recortan; si asoma la K del cargador tras «Asignar (1)» o
  «Avisar», se corta en la espera.
- **Encuadre:** G `pie` (180–209), M `avisar` (223–239), M `avisados` (253–299), M `parqueadero` (313–355). En 9:16 `avisar` (313 px de
  alto) va en G⁺.
- **Cámara:** 210–223, 240–253 y 300–313, uno por compás.
- **Texto:** la ceja «EQUIPOS» 195–201; sin frase (los toques y los chips son el espectáculo).
- **Sonido:** toque 181 (1,4), aparicion 184 y 196, toque 241, confirmacion 243, toque 301, aparicion 304.
- **Transición:** ninguna dentro; cierra con el látigo del 360.

#### P4 · «Y sabe a qué hora llegar» — cuadros 356–599 (compases 7–10) · pulsos 360, 375, 390, 420, 450, 480, 540, 570, 585

- **Grabación:** tramos `gabriela` (Mi iglesia con la tarjeta quieta 1,5 s; antes, el cambio de cuenta, que queda bajo el látigo), `servicio`
  (el toque, la página, 1,5 s quieta), `instrucciones` (`ver`, 2 s quieto) y `arriba` (`ver`, 1,2 s quieto). A 1×.
- **Encuadre:** G⁺ `tarjeta` (360–374), M `servicio-cabeza` (375–389), C `llegada` (403–419), G `servicio` (433–479), M `paleta` (493–569),
  M `botones` (desde el 583). En 9:16: `tarjeta` en G (la tarjeta entera cabe en 345 px), `paleta` centrada en los colores y los dos primeros
  pasos.
- **Cámara:** 390–403, 420–433, 480–493 y 570–583; **muerta de quieta** mientras la app se desplaza (450–459, 540–549).
- **Texto:** frase 3 entra 360–370 (seis palabras a 2 cuadros); sale 597–601.
- **Sonido:** desliz 349–361 (1,4), toque 376, desliz 455 y 545.
- **Transición:** látigo de ida (356–366), iris desde la tarjeta (375–380).

#### P5 · «Aceptar» — cuadros 600–655 (compás 11) · pulso 600 (segunda subida)

- **Grabación:** tramo `aceptar` (el toque y el anuncio quietos 2 s). A 1×.
- **Encuadre:** M `botones`, el mismo del 583: antes del toque, «Por confirmar» y los botones; después, «Confirmado», el anuncio y «Ya no
  puedo». La app empuja los botones hacia abajo al poner el anuncio: todo sigue dentro de 203–516.
- **Cámara:** quieta todo el compás (la prueba la da la app, como el compás 8 de Eventos).
- **Texto:** ninguno (frase 3 ya salió).
- **Sonido:** toque 601 (1,4), confirmacion 603 (1,4).
- **Transición:** cierra con el látigo de vuelta del 660.

#### P6 · «Tu líder ya lo sabe» — cuadros 656–719 (compás 12) · pulsos 660 (golpe), 690

- **Grabación:** tramo `lider` (el cambio de cuenta bajo el látigo, el turno recién abierto y **6,5 s quieto** a 1× para 660–839).
- **Encuadre:** M `parqueadero` (660–689): el mismo encuadre en que el mundo 1 se quedó en el 313, ahora con «Confirmado» donde decía «Por
  confirmar»; F `cierre` desde el 699: «Servicio General», **«5 de 5»** y los dos puestos de Parqueadero confirmados.
- **Cámara:** el retroceso del 690 (9 cuadros). Nada más.
- **Texto:** ninguno.
- **Sonido:** desliz 649–661 (1,4), confirmacion 663.
- **Transición:** látigo de vuelta (656–666).

#### P7 · «Que cada puesto de servicio esté cubierto» — cuadros 720–839 (compases 13–14) · pulsos 720 (golpe), 735 … 825

- **Grabación:** el resto del tramo `lider` (quieto a 1×).
- **Encuadre:** F `cierre` con la ventana a 0,92 y corrida (§1.4): los chips a ≥ 28 px. En 9:16 la ventana se encoge desde arriba y termina
  en 1262.
- **Cámara:** quieta (ya está en F desde el 699). El halo se asienta 720–810.
- **Texto:** frase 4 entra 720–732 (*cubierto* en itálica dorada); la ceja sale 720–723; la frase se sostiene 3,5 s.
- **Sonido:** subida 796–853.
- **Transición:** dip 837–839 y corte duro al 840.

#### P8 · «La firma» — cuadros 840–914

- 4:5: `identidad/cierre-clip.html`; 9:16: `identidad/cierre-corto.html`. Variables `{"llamado":"prueba","fondo":"azul","idioma":"es"}`.
- Campanas en 28,38 (cuadro 851). La música: 0,7 → 0,224 (852) → 0 (870).
- El único gesto de marca del clip.

---

## 3. La grabación: la escena `tools/ayuda/escenas/clips/equipos-parqueadero.mjs`

Una sola escena de **celular** (`movil: true`, 390×844 a 3× → **1170×2532**, 30 cps) sin el círculo del toque (`toque: false`), con
`capturar.mjs --modo video` sobre Kingdom Demo en español:

```bash
cd F:/Proyectos/KingdomApp/tools/ayuda
node capturar.mjs clips/equipos-parqueadero --idioma es --modo video
# → salida/video/es/clips/equipos-parqueadero/grabacion.mp4 + pasos.json (inicio/fin, tramo, accion, toques[], caja, caja_video)
```

**Cuentas:** 103 = el servidor **Jorge Gallego Gil**, líder de Seguridad (`_demo_servicio.php`: «La cuenta de prueba de servidor … queda
líder de Seguridad»); 105 = el miembro **Gabriela Hinestroza Perea** (la de la escena de la ayuda `mi-iglesia/responder-un-servicio`). La
escena cambia de cuenta dos veces con `como` (103 → 105 → 103); cada cambio graba unos segundos de carga que quedan debajo de un látigo.

**Lo que la semilla garantiza** (verificado en `_demo_servicio.php` y, el 2026-10-30, en la base local de capturas `ayuda_capturas_db`):
Seguridad tiene la plantilla «Culto del domingo» (Parqueadero ×2, Entrada ×2, Rondas ×1) sobre «Servicio General» de las 9:00; **el segundo
puesto de Parqueadero del próximo domingo queda vacante** (línea 374); las instrucciones de Seguridad (fijas y del domingo: lugar, vestimenta,
paleta de 3 colores, 3 pasos, llegada 75 min antes) están copiadas al turno. En la base local el turno de 2026-11-01 es Parqueadero: Rut
Londoño Isaza (confirmada) y VACANTE; Entrada: David Sepúlveda Hernández y Sara Restrepo Mejía (confirmadas; Sara como apoyo de red); Rondas:
Juan José García Quintero (confirmada) → **«4 de 5»**; ningún otro integrante de Seguridad con la habilidad Parqueadero tiene 0 servicios en 60
días. **Lo que la semilla no trae:** a Gabriela en Seguridad (está en Evangelismo). El gancho `sql` la pone antes de grabar (es la base local
de capturas, que `capturar.mjs` restaura del volcado en cada corrida) y apaga «Abierto a redes» y el apoyo de red de ese turno (regla 31).
Las cuatro sentencias se probaron el 2026-10-30 en una transacción con `ROLLBACK`: la vacante es el puesto 161, quedan 4 confirmadas y la
habilidad queda puesta.

**Datos ficticios:** todo es Kingdom Demo; no se escribe nada en la app (sin teclado).

**Selectores** (verificados en `frontend-v2/src/app/pages/equipos/`: `calendario.component.ts` (`a.turno[data-clave]`), `turno.page.ts`
(`[data-asignar]`, `section.grupo[data-funcion]`, `li.puesto[data-estado]`, `#turno-cobertura`, `#turno-avisar`), `asignar.component.ts`
(`#asignar-lista mat-checkbox[data-persona]`, `#asignar-confirmar`), `proximo-tarjeta.component.ts` (`#tarjeta-proximo-servicio`,
`#proximo-abrir`), `instrucciones-vista.component.ts` (`#instrucciones`, `#ins-paleta`, `#ins-pasos`); en `pages/mi/servicio.page.ts`
(`#servicio-aceptar`, `#servicio-anuncio`, `#servicio-estado`) y en `components/app-dialog.component.ts` (`#btn-ok`)).

```js
// Grabación para el clip del sitio público «Falta uno en Parqueadero» (LegacyHyperframes/videos/kingdomapp/clip-sitio-equipos/SPEC.md §3).
// NO es una escena de un artículo de la ayuda: no se publica ni entra en la frescura. Una sola escena de CELULAR (390×844 a 3x = 1170×2532,
// 30 cps) grabada SIN el círculo del toque (`toque: false`): el montaje dibuja el suyo sobre toques[] y las cajas de pasos.json.
//   node capturar.mjs clips/equipos-parqueadero --idioma es --modo video
//   → salida/video/es/clips/equipos-parqueadero/grabacion.mp4 + pasos.json
// Tres caras en una grabación: el líder de Seguridad (103, Jorge Gallego Gil) asigna a Gabriela en Parqueadero y la avisa; ella (105,
// Gabriela Hinestroza Perea) abre su servicio, ve sus instrucciones y acepta; el líder (103) la ve confirmada. Los dos cambios de cuenta
// quedan debajo de los látigos del clip.
// Tramos: calendario · turno · asignar · elegir · asignado · avisar · por-confirmar · gabriela · servicio · instrucciones · arriba · aceptar ·
// lider. Los `ver` con `bloque: 'nearest'` no desplazan: solo dejan la caja del objetivo de la cámara en pasos.json.
// Antes de grabar (gancho `sql`, solo en la base local de capturas): Gabriela entra a Seguridad con la habilidad Parqueadero (la semilla la
// tiene en Evangelismo), y el turno del domingo queda sin «Abierto a redes» ni apoyo de red (en el sitio «Redes y solicitudes» es Próximamente).
import { SEGURIDAD, ficha, funcion, mi, servir, turnoDomingo } from '../../lib/escenas-equipos.mjs';

const KDEMO = "(SELECT id FROM kd_sedes WHERE codigo = 'KDEMO')";
const SEG = `(${SEGURIDAD})`;
const PARQ = `(${funcion('Seguridad', 'Security', 'Parqueadero', 'Parking')})`;
const GABRIELA = `(${ficha(105)})`;
// El turno de Seguridad del próximo domingo (su id) y su puesto de Parqueadero sin persona (lo deja vacante _demo_servicio.php).
const T0 = `(SELECT t.id FROM eq_turnos t WHERE t.id_equipo = ${SEG} AND t.fecha >= CURDATE() ORDER BY t.fecha LIMIT 1)`;
const VACANTE = `(SELECT pu.id FROM eq_puestos pu WHERE pu.id_turno = ${T0} AND pu.id_funcion = ${PARQ}
  AND NOT EXISTS (SELECT 1 FROM eq_asignaciones a WHERE a.id_puesto = pu.id AND a.estado NOT IN ('no_puede', 'liberada', 'cancelada'))
  ORDER BY pu.orden LIMIT 1)`;
const FILA_DOMINGO = 'a.turno[data-clave="{@t0}"]';
const GRUPO = 'section.grupo[data-funcion="{@parq}"]';

export default {
  articulo: 'clips/equipos-parqueadero',
  movil: true,
  toque: false,
  pantallas: [
    servir('equipo.page.ts'), servir('calendario.component.ts'), servir('turno.page.ts'), servir('asignar.component.ts'),
    mi('mi-inicio.page.ts'), servir('proximo-tarjeta.component.ts'), mi('servicio.page.ts'), servir('instrucciones-vista.component.ts'),
  ],
  sql: [
    // Gabriela, integrante de Seguridad desde hace 90 días, con la habilidad Parqueadero (0 servicios: sale primera en la lista sugerida).
    `INSERT IGNORE INTO eq_integrantes (id_sede, id_equipo, id_persona, rol, estado, desde, por, decidido_por, decidido_at, created_at)
     SELECT ${KDEMO}, ${SEG}, ${GABRIELA}, 'integrante', 'activo', CURDATE() - INTERVAL 90 DAY, 103, 103, NOW() - INTERVAL 90 DAY, NOW() - INTERVAL 90 DAY`,
    `INSERT IGNORE INTO eq_habilidades (id_integrante, id_funcion)
     SELECT i.id, ${PARQ} FROM eq_integrantes i WHERE i.id_equipo = ${SEG} AND i.id_persona = ${GABRIELA}`,
    // Sin «Redes y solicitudes» en cuadro: el puesto vacante sin «Abierto a redes» y el apoyo de red de Entrada como del equipo.
    `UPDATE eq_puestos SET abierto_redes = 0 WHERE id_turno = ${T0} AND id_funcion = ${PARQ}`,
    `UPDATE eq_asignaciones SET origen = 'equipo', id_red = NULL WHERE id_turno = ${T0} AND origen = 'red'`,
  ],
  refs: {
    seg: SEGURIDAD,
    t0: turnoDomingo('Seguridad', 'Security', 0),
    parq: funcion('Seguridad', 'Security', 'Parqueadero', 'Parking'),
    gabriela: ficha(105),
    // Sin la vacante de Parqueadero no hay historia: la consulta da NULL y capturar.mjs se niega.
    vacante: `SELECT ${VACANTE}`,
    // El gancho sql dejó a Gabriela en Seguridad con la habilidad (si no, NULL y se niega).
    habil: `SELECT h.id_integrante FROM eq_habilidades h JOIN eq_integrantes i ON i.id = h.id_integrante
            WHERE i.id_equipo = ${SEG} AND i.id_persona = ${GABRIELA} AND h.id_funcion = ${PARQ}`,
    // Informativas (siempre dan un valor; se leen en el registro): 4 confirmadas → el final dice «5 de 5»; 0 rivales → Gabriela sale primera.
    confirmadas: `SELECT COUNT(*) FROM eq_asignaciones WHERE id_turno = ${T0} AND estado = 'confirmada'`,
    rivales: `SELECT COUNT(*) FROM eq_integrantes i JOIN eq_habilidades h ON h.id_integrante = i.id AND h.id_funcion = ${PARQ}
              WHERE i.id_equipo = ${SEG} AND i.estado = 'activo' AND i.id_persona <> ${GABRIELA}
              AND NOT EXISTS (SELECT 1 FROM eq_asignaciones a WHERE a.id_persona = i.id_persona AND a.sirvio = 'si' AND a.fecha >= CURDATE() - INTERVAL 60 DAY)`,
  },
  pasos: [
    // 1-2. El calendario de Seguridad con el primer domingo al centro: «4 de 5 · 1 por cubrir» (cuadro 0 del clip).
    { tramo: 'calendario', como: 103, ir: '/servir/equipos/{@seg}?tab=calendario', espera: FILA_DOMINGO },
    { ver: FILA_DOMINGO, pausa: 2500 },
    // 3. El domingo (el toque del 75): el turno, arriba; Parqueadero con su vacante y «Asignar» caben sin desplazar.
    { tramo: 'turno', clic: FILA_DOMINGO, espera: '[data-asignar="{@parq}"]' },
    { ver: '#turno-cobertura', bloque: 'nearest', pausa: 200 },        // caja de «4 de 5» (objetivo del 78)
    { ver: GRUPO, bloque: 'nearest', pausa: 1500 },                    // caja de Parqueadero (objetivo del 90)
    // 4-5. «Asignar» (el toque del 120, el bajo): la lista sugerida, Gabriela arriba; su casilla (el toque del 150).
    { tramo: 'asignar', clic: '[data-asignar="{@parq}"]', espera: '#asignar-lista mat-checkbox[data-persona="{@gabriela}"]', pausa: 1500 },
    { tramo: 'elegir', marcar: '#asignar-lista mat-checkbox[data-persona="{@gabriela}"]', pausa: 1000 },
    // 6. «Asignar (1)» (el toque del 180, el pico): «Sin avisar» y la barra «Avisar a 1 persona».
    { tramo: 'asignado', clic: '#asignar-confirmar', oculto: 'mat-dialog-container', espera: '#turno-avisar', pausa: 1500 },
    { ver: `${GRUPO} li.puesto[data-estado="borrador"]`, bloque: 'nearest', pausa: 200 },   // caja de su fila (objetivo del 210)
    // 7. «Avisar a 1 persona» (el toque del 240): «Avisados».
    { tramo: 'avisar', clic: '#turno-avisar', espera: '#btn-ok', pausa: 1500 },
    // 8. «OK» (el toque del 300): el turno se recarga y ella queda «Por confirmar».
    { tramo: 'por-confirmar', clic: '#btn-ok', oculto: 'mat-dialog-container',
      espera: `${GRUPO} li.puesto[data-estado="por_confirmar"]`, pausa: 1500 },
    // 9. Gabriela (el látigo del 360, FUERA DE CÁMARA el cambio de cuenta): Mi iglesia con «Tu próximo servicio».
    { tramo: 'gabriela', como: 105, ir: '/mi', espera: '#tarjeta-proximo-servicio[data-estado="por_confirmar"] #proximo-aceptar' },
    { ver: '#tarjeta-proximo-servicio', bloque: 'nearest', pausa: 1500 },
    // 10. La tarjeta (el toque del 375): su servicio, con la hora de llegada.
    { tramo: 'servicio', clic: '#proximo-abrir', espera: '#servicio-aceptar' },
    { espera: '#ins-pasos', pausa: 1500 },                             // las instrucciones llegan con el detalle
    // 11-12. La app baja a las instrucciones (el desliz del 450) y vuelve a los botones (el del 540).
    { tramo: 'instrucciones', ver: '#instrucciones', pausa: 2000 },
    { ver: '#ins-paleta', bloque: 'nearest', pausa: 200 },             // caja de los colores (objetivo del 480)
    { tramo: 'arriba', ver: '#servicio-aceptar', pausa: 1200 },
    // 13. «Aceptar» (el toque del 600, la segunda subida): «¡Gracias por servir! Tu líder ya lo sabe.» y «Confirmado».
    { tramo: 'aceptar', clic: '#servicio-aceptar', espera: '#servicio-anuncio', pausa: 2000 },
    { ver: '#servicio-anuncio', bloque: 'nearest', pausa: 200 },
    // 14. El líder otra vez (el látigo del 660, FUERA DE CÁMARA el cambio de cuenta): Gabriela «Confirmado» y «5 de 5». Quieto 6,5 s.
    { tramo: 'lider', como: 103, ir: '/servir/equipos/{@seg}/turno/{@t0}',
      espera: `${GRUPO} li.puesto[data-estado="confirmada"]:has-text("Gabriela")`, pausa: 300 },
    { ver: `${GRUPO} li.puesto[data-estado="confirmada"]:has-text("Gabriela")`, bloque: 'nearest', pausa: 200 },
    { ver: '#turno-cobertura', bloque: 'nearest', pausa: 6500 },       // caja de «5 de 5» (objetivo del 690) y el final quieto
  ],
};
```

Notas sobre la escena:

- `ver` desplaza suave (300 ms) con `block: 'center'` salvo que el paso diga `bloque`; con `bloque: 'nearest'` no se mueve nada si el
  elemento ya está a la vista: así se toman las cajas sin cambiar el encuadre de la grabación. En el celular la barra de la app es fija:
  nunca `bloque: 'start'`.
- La herramienta espera 900 ms tras cada acción y lo que diga `pausa`; `marcar` toca la etiqueta de la casilla; `como` entra con la cuenta y
  `ir` navega (unos segundos de carga, que se cortan bajo los látigos). Todo lo que sobra se corta; nada se puede alargar: por eso las pausas
  de 1,5 s sobre lo que se mira y los 6,5 s finales.
- **Tiempos:** ≈ 3,4 + 2,8 + 1,1 + 2,4 + 2,4 + 1,9 + 2,4 + 1,1 + 2,4 + 2,4 + 4 (cuenta) + 2,4 + 2,4 + 2,9 + 1,1 + 2,1 + 2,9 + 1,1 + 4 (cuenta)
  + 1,2 + 1,1 + 7,4 ≈ **56 s de grabación** para 28 s de clip. No hace falta `consolaEsperada` (no hay tramo sin señal).
- **Si `vacante` da NULL** (la semilla cambió y el domingo ya no tiene la vacante): no se graba; se revisa `_demo_servicio.php` (línea 374).
  **Si `confirmadas` < 4**: se graba igual; el final dirá «N + 1 de 5» y el retroceso del 690 sigue (la frase 4 no depende del número).
  **Si `rivales` > 0**: se graba igual; la cámara del 120 se centra en la fila de Gabriela, donde esté.
- **Para los stills del iris:** los cuadros 119 (mundo 1) y 374 (mundo 2) se exportan (`ffmpeg -ss <t> -frames:v 1`) desde la grabación al
  tiempo de origen correspondiente y van como `<img>` en `assets/stills/`.
- **No se graba un domingo:** el «próximo domingo» de la semilla sería hoy y el calendario lo marcaría como «hoy».
- **Idiomas (en, pt después):** la misma escena con `--idioma en` graba la interfaz en inglés (las `refs` ya aceptan «Security» y «Parking»);
  las frases se traducen y los saltos se vuelven a fijar; la firma lleva `idioma`.

---

## 4. Lo que se revisa en la vista previa

Cuadros a mirar: `npx hyperframes snapshot --at 0,1.5,2.0,2.5,2.6,3.0,3.5,4.0,4.1,4.5,5.0,5.5,6.0,6.1,6.5,7.5,8.0,8.1,8.5,10.0,10.2,11.8,11.9,12.0,12.3,12.5,13.4,14.5,15.0,15.4,16.5,18.0,18.4,19.5,20.0,20.1,21.0,21.9,22.0,22.3,23.3,24.0,24.5,27.9,28.0,28.4,30.4`
en las dos composiciones, y `snapshot --range 2.4,3.0 --frames 18` para el match cut del turno, `--range 3.9,4.3 --frames 12` y
`--range 12.4,12.8 --frames 12` para los dos iris, `--range 11.8,12.3 --frames 16` y `--range 21.8,22.3 --frames 16` para los dos látigos.

1. **Cuadro 0 (la miniatura):** el domingo con «4 de 5» y «1 por cubrir» en rojo a ≥ 34 px, «¿Quién» en Fraunces ya puesta, «Datos de
   ejemplo» abajo a la izquierda. Nunca negro, nunca la marca. En 9:16, nada por encima de 168 ni por debajo de 1330 salvo halo y puntos.
2. **Cuadro 45:** las cuatro landings de la frase 1 quietas. **59:** C sobre «4 de 5 · 1 por cubrir».
3. **75–88:** el toque en la fila y el turno que entra 1,03 → 1,00 sin un cuadro de página en blanco ni del esqueleto (si la app muestra el
   esqueleto, se corta). **103:** M sobre Parqueadero con «Vacante» y «Asignar»; **sin «Abierto a redes»**. **105–119:** la marca quieta.
4. **120–126:** el toque exactamente con el bajo; el iris nace de «Asignar»; la lista con Gabriela arriba y «✓ Habilidad · 0 en 60 días» a ≥
   34 px; la frase 2 entera en el 126. **150:** su fila llena; «Asignar (1)».
5. **180–184:** «Asignar (1)» con el pico; «Sin avisar» y la barra oscura; ninguna K del cargador. **195:** la ceja y no antes.
6. **240–253:** «Avisados» entero y legible; **300–313:** «Por confirmar» en su fila.
7. **356–366:** el látigo de ida en una sola tira, sin un cuadro con la ventana vacía ni la pantalla de carga de la cuenta; Mi iglesia de
   Gabriela aterriza 1,04 → 1,00; la frase 3 palabra a palabra.
8. **375–380:** el iris desde la tarjeta; **403:** «Llega a las 7:45 a. m.» a ≥ 57 px.
9. **450–459 y 540–549:** la app se desplaza y **la cámara no se mueve**. **493:** los tres colores y el cronograma a ≥ 44 px.
10. **600–603:** «Aceptar» con la segunda subida; «¡Gracias por servir! Tu líder ya lo sabe.» y «Confirmado» en el mismo encuadre.
11. **656–670:** el látigo de vuelta; el turno del líder en el mismo encuadre del 313 con «Confirmado» donde decía «Por confirmar»; **699:**
    F con «5 de 5» arriba y los dos puestos confirmados.
12. **720–738:** la frase 4 aterrizada en el 732 con *cubierto* dorada; la ceja fuera; la ventana a 0,92 y corrida; los chips a ≥ 28 px.
    **738–836:** nada se mueve salvo el halo; **837–839** el dip; **840** el primer cuadro de la firma sin noche vacía entre medias.
13. **Sonido (medido, no oído):** cada `toque` un cuadro después de su imagen; las tres `confirmacion` en 243, 603 y 663; los dos `desliz`
    de los látigos con su acento en 360 y 660; las campanas en el 851; la música a −10 dB en el 852 y a 0 en el 870; −16 LUFS, pico ≤ −1
    dBTP; ningún tramo con dos sonidos de acción encimados salvo 181 + 184, 241 + 243, 301 + 304, 601 + 603 y 661 + 663.
14. **Textos:** ninguna palabra que no esté en la app o en las cuatro frases; ningún texto que se lea < 28 px; las frases en 2 líneas (3 en
    9:16 la cuarta); `npx hyperframes check` en 0 errores (contraste AA incluido); «Datos de ejemplo» desde el cuadro 0.
15. **La historia sin sonido:** se entiende con la pantalla en silencio (así se verá en el sitio): falta uno el domingo → Kingdom sugiere a
    quién → se le avisa → ella ve a qué hora llegar → acepta → el líder la ve confirmada, 5 de 5 → cada puesto cubierto → Kingdom.

---

## 5. Riesgos y lo que se decide al grabar

- **El domingo de la semilla.** La vacante de Parqueadero es forzada (línea 374); las otras cuatro salen del reparto con azar sembrado (la
  base local da 4 confirmadas). Las `refs` lo dicen antes de grabar: sin vacante, no se graba; con menos confirmadas, el final dice «N de 5».
- **Gabriela por SQL.** Es la única escritura fuera de la app y solo en la base local de capturas (que se restaura del volcado en cada
  corrida). La alternativa por la app (el administrador 101 la agrega en Integrantes y le marca Parqueadero, como la escena de la ayuda
  `responder-un-servicio`) suma ~15 s de grabación fuera de cámara y un tercer cambio de cuenta; queda como plan B si el gancho falla.
- **El cargador de la app** (`loading.wrap`, la K animada a los 150 ms) en «Asignar (1)» y «Avisar»: con la API local no debería asomar; si
  asoma, se corta en la espera (los cortes del 180 y del 240 ya caen ahí).
- **Las cajas reales** del calendario (dónde queda el domingo tras el `ver`), del diálogo «Asignar» en el celular (si va a pantalla completa,
  `sugerencias` y `pie` se recalculan) y de la cabecera del turno (si «Copiar del turno anterior» y «Sumar puesto» van en una o dos filas)
  son estimaciones; los objetivos reales salen de `pasos.json` y el REVIEW los anota. La regla que no cambia: la cámara sujeta a la
  grabación, a lo sumo un movimiento por compás, nunca a la vez que la app se desplaza.
- **«Buenos días» y la fecha** cambian con la hora y el día de la grabación; ninguna frase depende de ellos.
- **Densidad de 120–180:** el iris, la frase 2, la casilla, la cámara al pie y el toque del pico en dos segundos. Si en la vista previa va
  atropellado, la casilla se adelanta al 135 y el movimiento al pie se quita: el 180 se toca con la cámara en M (el botón «Asignar (1)» queda
  fuera de cuadro y el toque se oye, como el «Listo» de Membresía).
- **Dos cambios de cuenta en una grabación:** si `como` deja ver la pantalla de entrada o un esqueleto, los látigos lo tapan (356–366,
  656–666): se elige el primer cuadro con la pantalla completa para el aterrizaje.
- **Dos cosas del kit v1.1 que este clip usa tal cual** (ya construidas para Membresía): `cierre-clip` y `.k-ventana` / `.k-feed-*`, el
  látigo en una sola tira y el modo video de celular con `toque: false` y `pasos.json` con `toques[]`. No hace falta nada nuevo de herramienta
  (el gancho `sql` y los `ver` con `bloque` ya existen).

---

## 6. Lo que cambió al construir (2026-10-30)

La grabación real y la vista previa cambiaron estos puntos; el detalle, con cada cuadro de la grabación, está en [REVIEW.md](REVIEW.md) §2–§4.

- **Toques reales** (cuadro de la grabación → cuadro del clip): fila del domingo 156 → 75 · «Asignar» 362 → 120 · casilla 463 → 150 ·
  «Asignar (1)» 524 → 180 · «Avisar a 1 persona» 689 → 240 · «Entendido» 805 → 300 · tarjeta 1132 → 375 · «Aceptar» 1469 → 600. Todos los
  tramos a 1×; los cambios de cuenta (910–1045 y 1609–1700) quedan bajo los látigos.
- **Textos reales:** el diálogo del aviso dice «Entendido» (no «OK»); Gabriela ve «Buenas tardes»; el calendario trae arriba «Tienes 6
  asignaciones sin avisar…» (queda fuera de cuadro).
- **La app salta en un cuadro** (no desplaza 300 ms): «baja a las instrucciones» en el 450 y «vuelve arriba» en el 540, con la cámara quieta.
- **Cortes nuevos en las esperas:** la K del cargador después de «Avisar», y después de «Aceptar» los botones apagados y el aviso «Tu
  respuesta quedó guardada: sale al volver la señal» que la app muestra un instante.
- **Imagen y sonido corridos un cuadro:** la barra «Avisar a 1 persona» en el 183 (`aparicion` 184), «Avisados» en el 242
  (`confirmacion` 243), «Por confirmar» en el 303 (`aparicion` 304), «¡Gracias por servir!» en el 602 (`confirmacion` 603) y «Confirmado»
  del líder en el 661 (`confirmacion` 662, no 663).
- **Encuadres:** el texto de la app ocupa de x 16 a x 374, así que varios M del §1.5 pasan a ×1,04–×1,25 (`turnoCabeza` ×1,15,
  `parqueadero1` G⁺, `sugerencias` ×1,15, `avisar` ×1,25, `avisados` G⁺, `tarjeta` G, `paleta` ×1,04, `botones` G⁺); `semana` (la miniatura)
  y `parqueadero2` sí son M. El `cierre` es ×1,2 desde «9:00 a. m.» para que «Datos de ejemplo» no tape el «Confirmado» de Gabriela:
  «Servicio General» queda fuera del plano final.
- **El iris nace donde se tocó en la pantalla:** cada mundo lleva dos cámaras (la de antes y la de dentro del iris) y el recorte va en px
  de la ventana.
- **Mezcla:** los tres toques clave a 1,0 (no 1,4) y la música a 0,75, como Eventos: −17,1 LUFS y −2,7 dBTP sin normalizar.

