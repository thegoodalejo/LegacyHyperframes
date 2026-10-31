# SPEC · Clip del sitio: Mi iglesia — «Se enteró toda la iglesia»

2026-10-30 · Contrato de construcción de la historia elegida en [STORY.md](STORY.md) (el dueño ya no revisa guiones: se eligió aquí). Cada
adjetivo es un número, los valores por defecto están prohibidos con nombre y los planos van cuadro por cuadro sobre la grilla real de la
pista. Se construye desde aquí, se revisa contra esto y se cambia aquí cuando la vista previa cambie la película. Hereda el sistema de
[Membresía](../clip-sitio-membresia/SPEC.md) y de [Eventos](../clip-sitio-eventos/SPEC.md) (mismo reloj, mismas letras, misma ventana, mismas
curvas, misma firma) y las lecciones del [REVIEW de Membresía](../clip-sitio-membresia/REVIEW.md) (ya aplicadas: niveles del kit, entradas un
cuadro antes del pulso, el `<video>` nunca transformado, «Datos de ejemplo» a 31 px abajo a la izquierda, cortes dentro de las pausas de la
grabación, la espera de la app recortada en vez de mostrada).

```text
GOAL:    Un pastor que no conoce Kingdom termina pensando «lo anunciaron, ella lo vio en su celular, se inscribió con su esposo y ya tiene la
         boleta en el bolsillo» y toca «Prueba gratis 30 días».
OUTPUT:  HyperFrames · dos composiciones de la misma línea de tiempo: 1080×1350 (4:5, sitio y feed) y 1080×1920 (9:16, Reels e historias) · 30 fps.
TIME:    30,5 s = 915 cuadros: cuerpo 0–28,0 (cuadros 0–839) + firma 28,0–30,5 (840–914). 120 BPM = 15 cuadros por pulso (grilla real en §0).
LOOK:    noche del sitio (#060D1F) con el halo y la retícula de puntos del kit; tinta #EAF0FF; un solo acento, el dorado #E8B95A, en tres
         lugares y no más (la ceja «MI IGLESIA», la palabra «bolsillo» y el botón de la firma). Fraunces 560 / −0,02 em para las frases;
         Inter para la ceja y «Datos de ejemplo». El medio: la app REAL de Kingdom Demo grabada en celular, nítida (1170 px de ancho), dentro
         de una ventana con radio 28, anillo de 1 px y sombra 0 40 80 −24 al 65 %; nunca un teléfono dibujado.
OBJECTS: la ventana (el celular de la miembro, un solo mundo); la novedad con la tarjeta del evento; el evento; la boleta con su QR; el punto
         de toque de la grabación; las cuatro frases; la ceja; la píldora «Datos de ejemplo»; la corona del cierre. Nada más existe en el cuadro.
MOTION:  curvas por papel (§1.6); un movimiento de cámara por compás (14 cuadros, power2.inOut), quieto después y nunca mientras la app se
         desplaza; cada corte y cada entrada en un pulso; cada cambio grande en un golpe (120 · 180 · 600 · 660 · 720 · 840).
SHOTS:   siete planos (§2).
BANNED:  §1.8.
QA:      §4.
```

---

## 0. El reloj: la grilla real de la pista

La música es «Product Launch» (The_Mountain) del 14,05 al 42,05 s; t = 0 del clip ↔ 14,05 de la pista. Los pulsos vienen de
`_identidad/musica/product-launch-the-mountain.pulsos.json` (el mismo mapa de Membresía y Eventos) restándoles 14,05 y redondeando a 30 fps:
**todos caen en el múltiplo de 15 cuadros salvo el 9,455 s, que cae en el cuadro 284** (nada ocurre ahí). Cada pulso se calcula desde su
índice, nunca sumando 15 repetidamente.

| Compás | Cuadros | Pulsos (cuadro · fuerza) | Intensidad | Lo que le toca a este clip |
|---|---|---|---|---|
| 1 | 0–59 | 0 ·0,69 · 15 ·0,64 · 30 ·0,49 · 45 ·0,48 | 0,57 | Mi iglesia arriba (el saludo); la frase 1, una landing por pulso |
| 2 | 60–119 | 60 ·0,58 · 75 ·0,55 · 90 ·0,57 · 105 ·0,61 | 0,58 | **60:** la app baja a la novedad (llega en el 75); 90 la cámara a la tarjeta y las reacciones; **105:** la flecha abre las reacciones |
| 3 | 120–179 | **120 ·0,93** (entra el bajo) · 135 · 150 · 165 | 0,66 | **120:** «Amén». Frase 2. 150 la cámara a la tarjeta del evento; 165 el dedo se posa en «Inscribirme» |
| 4 | 180–239 | **180 ·0,87** (pico) · 195 ·0,83 · 210 · 225 | **0,77** | **180:** iris al evento; 195 la ceja «MI IGLESIA» |
| 5 | 240–299 | **240 ·0,92** · 255 ·0,77 · 270 · 284 | 0,70 | 240 la cámara a las fechas y la descripción |
| 6 | 300–359 | 300 ·0,77 · 315 ·0,75 · 330 · 345 | 0,68 | 300 la app baja a «Inscripción»; 330 la cámara al mensaje y a «Inscribirme» |
| 7 | 360–419 | 360 ·0,76 · 375 ·0,64 · 390 · 405 | 0,59 | Frase 3; **375:** «Inscribirme» → «¿A quiénes inscribes?»; 390 la cámara a la lista |
| 8 | 420–479 | 420 ·0,75 · 435 ·0,61 · 450 · 465 | 0,59 | 420 el esposo; 450 «Seguir» → «1 de 2: Tú»; 465 la cámara al formulario |
| 9 | 480–539 | 480 ·0,67 · 495 ·0,67 · 510 · 525 | 0,59 | 480 «M» · 495 «Sí» · 510 «Seguir» → «2 de 2» |
| 10 | 540–599 | 540 ·0,63 · 555 · 570 ·0,61 · 585 ·0,68 | 0,62 | 540 «L» · 555 «No»; 570 la cámara a «Inscribir» |
| 11 | 600–659 | **600 ·0,93** (segunda subida) · 615 ·0,69 · 630 · 645 | 0,66 | **600:** «Inscribir» → el sello, el confeti, «¡Quedaste inscrito!». Frase 3 sale |
| 12 | 660–719 | **660 ·0,90** · 675 ·0,89 · 690 ·0,76 · 705 ·0,68 | **0,81** | **660:** «Ver boleta» → la boleta con su QR (la prueba más fuerte); 690 el punch al QR |
| 13 | 720–779 | **720 ·0,96** · 735 ·0,77 · 750 · 765 | 0,73 | **720:** el QR → la boleta a pantalla completa. Frase 4; la ceja se va; la ventana se hace a un lado |
| 14 | 780–839 | 780 ·0,88 · 795 ·0,74 · 810 · 825 | 0,71 | Quieto; la subida; el dip |
| — | **840** ·1,00 | el golpe más fuerte de la pista | — | **La firma.** La música se va debajo de las campanas |

Las dos pruebas caen en los dos golpes reales de la segunda subida: «Inscribir» en el 600 (0,93) y «Ver boleta» en el 660 (el compás más
fuerte del cuerpo). La boleta en grande y la frase final, en el 720 (0,96).

---

## 1. Los números del estilo

### 1.1 Paleta (tokens de `identidad/kit.css`; nada fuera de esta lista)

| Papel | Token | Valor | Dónde puede aparecer |
|---|---|---|---|
| Fondo | `--k-noche` | `#060D1F` | A sangre, todo el cuerpo |
| Halo | `.k-halo` | azul `rgba(53,118,218,.45)` arriba a la derecha + dorado `rgba(217,162,52,.22)` abajo a la izquierda | Fondo, bajo todo; se asienta 1,08 → 1 en 0, 180 y 720 |
| Puntos | `.k-puntos` | `rgba(169,190,235,.35)`, 2 px cada 42 px, desvanecidos a la izquierda | Fondo; **nunca se mueven** |
| Tinta | `--k-noche-tinta` | `#EAF0FF` | Las frases |
| Acento | `--k-noche-dorado` | `#E8B95A` | Solo: la ceja «MI IGLESIA», la palabra *bolsillo*, el botón de la firma |
| Anillo | `--k-noche-linea` | `rgba(234,240,255,.12)` | El borde de la ventana |
| Fondo de la app | `--k-app-fondo` | `#FAF9FD` | Detrás de la grabación (nunca se ve) |
| Azul de marca | `--k-azul` | `#3576DA` | **Solo en la firma** (la baldosa) |
| Placa | `.k-datos-ejemplo` | `rgba(6,13,31,.72)` | La píldora «Datos de ejemplo» |
| Dip | — | `rgba(6,13,31,.40)` | Los 3 cuadros antes de la firma, solo sobre la ventana |

Los colores de la app (el morado de «Amén» puesto y de los botones, el verde de la portada del Encuentro, el confeti, el blanco y negro de
la boleta en grande) viven dentro de la grabación y no se tocan. `--k-noche-tinta-2` no se usa.

### 1.2 Tipografía

| Pieza | Clase (kit v1.1) | Familia · peso | 4:5 | 9:16 | Interlineado · tracking | Reglas |
|---|---|---|---|---|---|---|
| Frase | `.k-feed-frase` (`.k-titular` + `.k-vertical` en 9:16) | Fraunces 560; `<em>` itálica 500 dorada | **80 px** | **104 px** | 1,04 · −0,02 em | Máx. **2 líneas** en 4:5 (3 en 9:16), saltos fijados a mano. Izquierda. Sin sombra |
| Ceja | `.k-feed-ceja` (`.k-ceja`) | Inter 700, MAYÚSCULAS | **30 px** | **34 px** | 1 · +0,10 em | Dos palabras: «MI IGLESIA» |
| Datos de ejemplo | `.k-datos-ejemplo .k-feed-datos` | Inter 600 | **31 px**, píldora de 56 px de alto | igual | 1 · 0 | Blanca sobre la placa; **abajo a la izquierda de la ventana**, a 24 px del borde visible; con la ventana a 0,92 queda en ≥ 28 |
| Texto de la app | (grabación) | Inter de la app, 14 px CSS el cuerpo, 22–24 px los títulos | ≥ **31,6 px** | ≥ **34,5 px** | — | Nunca por debajo de 28 px en ningún encuadre (§1.5) |

Saltos de línea fijados:

| Frase | 4:5 (80 px, 888 px de ancho) | 9:16 (104 px, 960 px de ancho) |
|---|---|---|
| 1 | «¿Se enteró / toda la iglesia?» | igual |
| 2 | «Llega a cada celular.» (una línea) | «Llega a cada / celular.» |
| 3 | «Y se inscribe / con su familia» | igual |
| 4 | «Tu iglesia, en el *bolsillo* / de cada miembro» | «Tu iglesia, / en el *bolsillo* / de cada miembro» |

**La primera línea de la frase 4 es la más larga de la serie** (26 caracteres; estimada en ≈ 780–820 px a 80 px con el tracking). Se mide en el
primer snapshot: si pasa de 888 px, la frase 4 en 4:5 va en tres líneas como en 9:16 («Tu iglesia, / en el *bolsillo* / de cada
miembro») y **sube al lugar de la ceja** (y = 72, libre desde el 723): tres líneas de 83 px → termina en 321, por encima de la ventana ya
encogida (su borde de arriba baja a 444, §1.4). No se achica la letra.

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
| Frase 4 | igual que las demás (o y = 72 en tres líneas, §1.2) | **y = 188** (el lugar de la ceja, libre desde el 723) · 3 líneas → 512 |
| Ventana | x 100 · y 360 · **880 × 1050**: sangra 60 px por abajo (se ve 880×990) | x 60 · y 480 · **960 × 850**, completa |
| Ventana al final (desde el 720) | escala **0,92** desde el centro inferior + x **+48** (su borde de arriba baja de 360 a 444) | escala **0,92** desde el **centro inferior** + x **+36** (de 480 a 548: deja 36 px bajo la frase 4) |
| Datos de ejemplo | abajo a la izquierda de la ventana, 24 px del borde visible | ídem |
| Firma | `cierre-clip` (kit v1.1) | `cierre-corto` (kit v1) |

Variables de `index.html` (como en Eventos): 4:5 `--f-k: 0.752137`, `--f-grab-alto: 1904.41px`; 9:16 `--f-k: 0.820513`,
`--f-grab-alto: 2077.54px`, `--f-ventana-hvis: 850px`. Sin `--f-latigo` ni `#m2` (un solo mundo): la tira tiene un solo `.mundo` con su
envoltorio `#m1in` para el aterrizaje del 663. **En 9:16 el cambio de la ventana arranca en el 720, no en el 724** (la tercera línea de la
frase 4 aterriza en el 734 y la ventana tiene que estar ya abajo): 720–734.

### 1.5 La cámara dentro de la ventana: escalas

Grabación a 3× (390×844 px CSS → **1170×2532 px**). **ppc** = píxeles del cuadro por píxel CSS del celular.

| Nivel | Qué se ve | 4:5: ppc (escala del video) · visibles en px CSS | 9:16: ppc (escala) · visibles | Texto de la app 14 px → |
|---|---|---|---|---|
| **G** general | todo el ancho del celular | **2,256** (0,752) · 390 × 439 | **2,462** (0,821) · 390 × 345 | 31,6 px · 34,5 px |
| **G⁺** | una tarjeta con sus márgenes | 2,436 (0,812) · 361 × 406 | 2,659 (0,886) · 361 × 320 | 34 px · 37 px |
| **M** medio | una zona de la tarjeta, la lista o el formulario | **3,158** (1,053) · 279 × 313 | **3,446** (1,149) · 279 × 247 | 44 px · 48 px |
| **C** cerrado | una línea | **4,061** (1,354) · 217 × 244 | **4,431** (1,477) · 217 × 192 | 57 px · 62 px |

G = ×1,00 · G⁺ = ×1,08 · M = ×1,40 · C = ×1,80 sobre el general. La cámara es `scale` + `x`/`y` sobre `#cam` dentro de la ventana, sujeta a
los bordes de la grabación (función `enc()` de Membresía); el `<video>` nunca se transforma ni se busca. El objetivo de cada movimiento es
una **caja de `pasos.json`** (px CSS del viewport 390×844). Las de abajo son estimaciones medidas sobre las capturas publicadas de la ayuda
(`mi-iglesia/inicio-de-mi-iglesia/01-inicio` y `02-novedades`, `mi-iglesia/inscribirme-a-un-evento/01-evento` y `02-boletas`, todas de la
cuenta 105); **las reales salen de la grabación** y se anotan en el REVIEW.

| Objetivo | Nivel | Centro estimado (x, y CSS) → visibles en 4:5 | Lo que debe quedar dentro |
|---|---|---|---|
| `inicio` | G | (195, 219) → 0–439, tope de arriba | la barra «Kingdom Demo» con su logo, «Buenos días, Gabriela» (real), «Iglesia Kingdom Demo 1», «Mis servicios», «Mis Equipos» y la parte de arriba de la destacada |
| (el mismo encuadre, la app ya abajo) | G | 0–439 | la novedad centrada por la app (≈ 172–672): «Novedades», su cabecera «Iglesia Kingdom Demo 1 · hace 3 minutos», «Inscripciones abiertas», el texto y la parte de arriba de la tarjeta |
| `reacciones` | M | (195, 560) → 403–716 | el cuerpo de la tarjeta del evento (la fecha, «Congreso de Jóvenes», «Inscribirme») y la barra «Reaccionar ˄ 👍🙌🙏 N»; el selector abre **hacia arriba** dentro de este encuadre |
| `tarjeta` | M | (195, 520) → 363–676 | la portada (abajo), la fecha, «Congreso de Jóvenes», **«Inscribirme»** a 44 px y la barra con «🙌 Amén» puesto |
| `evento` | G | (195, 300) → 80–519 | «← Mi iglesia», la portada, «Encuentro», **«Congreso de Jóvenes»** y el comienzo de las fechas |
| `datos` | M | (195, 520) → 363–676 | «Congreso de Jóvenes», «Del martes, 24 de noviembre al miércoles, 25 de noviembre · 8:00 a. m.» (real), «Día 1 · Día 2», la descripción |
| `inscripcion` | M | (195, 422) → 266–579 (la app ya bajó: la sección centrada) | «Inscripción», el mensaje «Llega 30 minutos antes con tu boleta en el celular (también funciona sin señal).» y **«Inscribirme»** |
| `quienes` | M | (195, 520) → 363–676 | «¿A quiénes inscribes? (hasta 4)», «Yo» ☑, el esposo (real) ☐ (y otro familiar, si lo hay), «Cancelar · Seguir» |
| `form` | G | (195, 422) → 202–641 (la app centró el formulario) | «1 de 2: Tú», «Talla de camiseta *» S · M · L · XL, «¿Es tu primera vez en el congreso?» Sí · No, «Atrás · Seguir» |
| `botones-form` | M | (195, 560) → 403–716 | «¿Es tu primera vez…?» Sí · No (No marcado) y «Atrás · **Inscribir**» |
| `resultado` | G | (195, 422) → 202–641 | el sello, «¡Quedaste inscrito!», «Tu boleta ya está en Mis boletas: también se ve sin señal.», las dos filas «Inscrito», «Ver boleta · Listo» |
| `boleta` | G | (195, 375) → 155–594 | «Congreso de Jóvenes», sus días, el lugar, «Tu boleta», el QR y «Código ······» |
| `qr` | M | (195, 440) → 283–596 | el QR y «Código ······» a 44 px |
| `grande` | G | (195, 378) → 158–597 | la boleta a pantalla completa: el QR (343 px CSS), el nombre y el código |

### 1.6 Curvas y duraciones (cada tween lleva su curva por nombre)

| Papel | Curva | Cuadros | Detalle |
|---|---|---|---|
| `entrada-palabra` | `power4.out` | 4 | `filter: blur(6px) → 0` + opacidad; **sin desplazamiento**; arranca un cuadro antes del pulso (el primer cuadro visible es el pulso). Palabras a 2 cuadros, salvo la frase 1 (una landing por pulso) |
| `entrada-linea` | `power4.out` | 6 | la línea entera, blur 8 → 0 (frase 2 y ceja) |
| `salida-texto` | `power3.in` | 4–5 | blur 0 → 8 + opacidad, la línea entera, 2–3 cuadros antes del pulso («blur swap») |
| `camara` | `power2.inOut` | **14** | un movimiento por compás; quieta después; **nunca mientras la app se desplaza** |
| `punch` | `power2.inOut` | **9** | solo el del cuadro 690 |
| `aterrizaje-app` | `power3.out` | 10 | el corte sobre el toque del 660: «Mis boletas» entra a escala **1,03 → 1,00** en `#m1in` (663–673), origen en el centro de lo visible de la ventana. Es la única vez |
| `iris` | `power2.out` | 5 | `clip-path: circle(0 at X Y) → circle(1900px at X Y)`, X Y = el centro de «Inscribirme» de la tarjeta (caja de `pasos.json`) en px de la grabación ajustada; debajo, un still del cuadro 179 |
| `dedo-espera` | `power2.out` | 4 | la marca de toque aparece y **se queda quieta** hasta el toque: 165 → 180 (una sola vez, la del pico). Las demás marcas aparecen 4 cuadros antes de su toque |
| `toque` | `power2.out` / `power2.in` | 4 · 2 · 6 | la marca aparece (opacidad 0 → 1, escala 0,6 → 1), se hunde a 0,86 en el cuadro y se va 6 después; la onda 36 → 58 px CSS en 0,45 s, `#015BBE` al 90 % |
| `ventana-cambio` | `power2.inOut` | 15 | escala 1 → 0,92 + x (§1.4): 4:5 724–738; 9:16 720–734 |
| `halo` | `sine.out` | 90 | 1,08 → 1,00 en 0, 180 y 720; los puntos no se mueven |
| `dip` | escalón | 3 | 837–839 |
| firma | las del kit | 75 | `back.out(2.2)` de la corona; **no se imita en el cuerpo** |
| resortes | ninguno del montaje | — | los resortes que se ven (el selector de reacciones, «Amén», el sello) son de la app; el montaje no rebota nada salvo la corona |
| velocidad de la grabación | `data-playback-rate` por tramo (o carril `rate`) | — | entre **0,35× y 3,5×**; las rampas van entre acciones, nunca durante un toque, el confeti o una animación de la app. Los cortes caen en los `huecos_de_pantalla` de `pasos.json` |

`data-motion-blur="on"` con `data-motion-blur-shutter="180"` en la raíz. **Nunca `filter: blur()` sobre la grabación.**

### 1.7 Sonido

| Capa | Fuente | Nivel | Regla |
|---|---|---|---|
| Música | `assets/musica/product-launch-the-mountain.mp3`, `data-media-start` 14,05, dura 29 s | 0,7 en el carril de volumen (−18 LUFS, `kit.json`) | 0,7 hasta el 840 → 0,224 en el 852 → 0 en el 870 |
| Sonidos de acción (kit v1.1) | `toque` 75 ms · `aparicion` 220 ms · `desliz` 360 ms (acento 0,2) · `subida` 1,9 s (acento 1,5) · `confirmacion` 320 ms (acento 0,1) | el nivel del kit (`data-volume="1"`, 4–10 dB bajo la música); **1,4** solo en los cuatro toques clave (121 · 181 · 601 · 661), en la `aparicion` del 123 y en la `confirmacion` del 603 | `data-start` = cuadro / 30 − acento; el pico suena **un cuadro después** de su imagen. `toque` rota a (`toque.wav`), b (+3 %), c (−3 %), nunca la misma dos veces seguidas. Sin tics |
| Sonido de marca | `identidad/audio/sonido-marca.wav` | tal cual | en **28,38 s** (cuadro 851) |
| Mezcla | — | −16 LUFS integrados, pico real ≤ −1 dBTP | `normalize-audio` sobre el render de entrega; se comprueba con `hyperframes audio --json`. Si el normalizador recorta, los 1,4 bajan a 1,2 |

Los 24 eventos, con su causa (cuadro del sonido = imagen + 1):

| Cuadro | Sonido | Causa |
|---|---|---|
| 63 | desliz (acento) | la app baja a la novedad (60–75) |
| 106 · 108 | toque a · aparicion | la flecha de las reacciones · el selector se abre |
| 121 · 123 | toque c (1,4) · aparicion (1,4) | «Amén» · «🙌 Amén» salta y el total sube en uno |
| 181 | toque b (1,4) | «Inscribirme» en la tarjeta (el iris) |
| 196 | aparicion | la ceja «MI IGLESIA» |
| 303 | desliz (acento) | la app baja a «Inscripción» (300–315) |
| 376 | toque a | «Inscribirme» |
| 421 · 451 | toque b · toque c | el esposo · «Seguir» |
| 481 · 496 · 511 | toque a · b · c | «M» · «Sí» · «Seguir» |
| 541 · 556 | toque a · b | «L» · «No» |
| 601 · 603 | toque c (1,4) · confirmacion (1,4) | «Inscribir» · el sello y «¡Quedaste inscrito!» |
| 661 · 663 | toque a (1,4) · confirmacion (1,0) | «Ver boleta» · la boleta con su QR |
| 721 · 723 | toque b · aparicion | el QR · la boleta a pantalla completa |
| 796–853 | subida | su golpe (acento 1,5 s) en el 840 |
| 851 | campanas | la firma + 0,38 |

Ninguno sin causa visible; 0–6 s lleva cinco y el sexto en el 181. Nada de whoosh en los movimientos de cámara, en el iris ni en el corte del
660. El confeti no lleva sonido propio (su sonido es la `confirmacion` del 603).

### 1.8 BANNED: los valores por defecto prohibidos, con nombre

Los 20 de Membresía valen enteros (fundido de 0,5 s para todo; fade + deslizar hacia arriba; zoom lineal; «creeping scale»; fundido
cruzado entre mundos; teléfono dibujado; texto que se mueve mientras se lee o «respira»; logo en una esquina; brillo, neón, partículas,
orbes; degradados nuevos y tarjetas de vidrio; tres tarjetas en fila, KPI, «01 / 02», corner brackets, HUD; whoosh en cada corte y el mismo
`toque` sin rotar; reproducción fuera de 0,35×–3,5×; retocar un píxel de la app; texto de la app < 28 px; centrarlo todo; cifras sin «Datos
de ejemplo»; más de 3 s sin cambio visible; un pulso vacío entre 0 y 6 s; `from()`, `autoAlpha` sobre un `.clip`, `transform` de CSS donde
GSAP transforma, el `<video>` y su envoltorio con tiempo a la vez). El «pulso vacío» se cuenta como en lo construido de Membresía (REVIEW
§3): entre 0 y 6 s cada pulso tiene un suceso; entre 6 y 12 s manda un cambio por compás (la cámara o la app) y ningún tramo quieto pasa de
1,6 s. Y los de este clip:

21. **La cámara y el desplazamiento de la app a la vez.** Cuando la app baja (60–75, 300–315, 452–464), la cámara está muerta de quieta;
    cuando la cámara se mueve, la app no se desplaza.
22. **Más de dos `confirmacion`, o una por cada toque.** Dos en todo el clip, una por prueba: 603 y 663. «Amén», la ceja y la boleta en
    grande llevan `aparicion`; los radios y las casillas, solo `toque`.
23. **Recrear o «ayudar» lo que hace la app:** el selector de reacciones, el salto de «Amén», el sello, el confeti, la boleta o el QR. Ni un QR
    propio, ni un brillo sobre el QR, ni confeti agregado si la app no lo dibujó en la grabación, ni un contador de reacciones animado aparte.
24. **Un látigo «para animar».** Este clip tiene un solo mundo (el celular de la miembro).
25. **Dibujar una marca de toque donde la grabación no tocó**, o una marca que viaja «hasta» el botón. La marca nace donde `pasos.json` dice
    (`toques[]`); solo la del 165 espera quieta sobre su botón.
26. **Una notificación dibujada** (un banner del sistema, un «push» de la iglesia, la campana con un número inventado). «Llega a cada
    celular» lo dice la frase; la imagen es la novedad real en el feed.
27. **La entrada a la app** (Google, WhatsApp o la pantalla de inicio de sesión) en cualquier cuadro.
28. **El blanco de la boleta a sangre.** La boleta a pantalla completa vive dentro de la ventana; nunca se agranda la ventana, ni se funde el
    cuadro a blanco, ni el dip del 837 es blanco (es noche al 40 %).
29. **La ceja o una frase sobre el título de la app** («Congreso de Jóvenes», «¡Quedaste inscrito!»). Las frases viven arriba del cuadro
    (§1.4); la ventana empieza en y = 360 y nada se superpone, tampoco durante el cambio de la ventana del 720.

Después del primer render, cada valor por defecto que aun así aparezca se nombra aquí y se corrige.

---

## 2. Los planos, cuadro por cuadro

### 2.0 Convenciones

- **G / G⁺ / M / C** y los nombres de objetivo (`inicio`, `reacciones`, `form`…): §1.5. «Sobre X» = la caja de X centrada en la ventana.
- **Pulso**: el cuadro de la grilla de §0. Un evento «en el 120» aterriza en el cuadro 120 (su sonido suena en el 121).
- **Grabación**: una sola, `clips/mi-iglesia-boleta` (cuenta 105), con los tramos `inicio · bajar · reaccion · evento · inscripcion · familia ·
  formulario · inscrito · boleta · grande` (§3). Los cortes de video caen en pausas de la grabación.
- **Textos de la app**: son los reales, verificados en `frontend-v2/public/i18n/es.json` (`po1.*`, `mi.*`, `bloques.*`, `evi.*`, `evb.*`), en
  `backend/_datos/portal.php` (el catálogo de reacciones) y en la semilla (`_demo_portal_3_publicaciones.php`, `_demo_eventos_inscripcion.php`):
  «Buenos días, {nombre}», «Novedades», «Próximos eventos», «Inscripciones abiertas», «Separa la fecha y asegura tu cupo: los cupos son
  limitados.», «Inscribirme», «Reaccionar», «Me gusta · Me edifica · Me sorprende · Amén» (👍 🙏 😮 🙌), «Mi iglesia», «Encuentro»,
  «Congreso de Jóvenes», «Día {n}», «Dos días para encontrarnos, adorar y crecer juntos. Trae tu Biblia y tu boleta.», «Inscripción»,
  «Llega 30 minutos antes con tu boleta en el celular (también funciona sin señal).», «¿A quiénes inscribes? (hasta {n})», «Yo»,
  «Cancelar», «Seguir», «{n} de {total}: {nombre}», «Tú», «Talla de camiseta», «S · M · L · XL», «¿Es tu primera vez en el congreso?»,
  «Sí · No», «Atrás», «Inscribir», «¡Quedaste inscrito!», «Tu boleta ya está en Mis boletas: también se ve sin señal.», «Inscrito», «Ver
  boleta», «Listo», «Mis boletas», «Tu boleta», «Código», «Descargar la boleta», «Cerrar». Lo que cambia con la semilla o con la hora (el
  saludo, el nombre de la miembro y de su esposo, las fechas del congreso, el lugar, los conteos de reacciones, el código) lleva «(real)».
- Las frases siempre en el mismo lugar (§1.4); una frase a la vez; la ceja encima de la frase.
- **Posiciones CSS** de la app: estimadas sobre las capturas de la ayuda; las reales, de `pasos.json`.

### 2.1 Tabla maestra (todo lo que cambia, por cuadro)

| Cuadro | Pulso | La app (grabación) | Cámara | Texto | Sonido | Transición |
|---|---|---|---|---|---|---|
| **0** | ● | Tramo `inicio` · Mi iglesia arriba: la barra **«Kingdom Demo»** con su logo, la campana, «?» y el avatar; **«Buenos días, Gabriela» (real)**, «Iglesia Kingdom Demo 1», «Mis servicios», «Mis Equipos 3» (real), la destacada «¡Bienvenidos a nuestra iglesia en la app!» asomando. «Datos de ejemplo» abajo a la izquierda | G `inicio` | **«¿Se»** ya aterrizada (es la miniatura) | — | — |
| 15 · 30 · 45 | ● ● ● | quieta | quieta | **«enteró»** 15 · **«toda la»** 30 · **«iglesia?»** 45. Frase 1 completa y muerta de quieta hasta el 117 | — | |
| **60–75** | ● ● | Tramo `bajar`: **la app baja sola** (desplazamiento suave real, a la velocidad que lo haga caber en 15 cuadros): pasan la destacada, el calendario del mes con sus puntos, los próximos eventos y «Novedades»; se detiene con la novedad centrada: **«Iglesia Kingdom Demo 1 · hace 3 minutos» · «Inscripciones abiertas» · «Separa la fecha y asegura tu cupo: los cupos son limitados.»** y la tarjeta del evento | **quieta** (G, el mismo encuadre) | | `desliz` (acento 63) | |
| **90–103** | ● | quieta | **Movimiento del compás 2**: G → **M `reacciones`** (el cuerpo de la tarjeta: la fecha (real), **«Congreso de Jóvenes»**, **«Inscribirme»**, y la barra «Reaccionar ˄ 👍🙌🙏 N (real)») | | — | |
| **105** | ● | tramo `reaccion`: **toque en la flecha «˄»** → el selector sube con «👍 Me gusta · 🙏 Me edifica · 😮 Me sorprende · 🙌 Amén», escalonado con su resorte (≈ 200 ms reales) | quieta | | `toque` a 106 · `aparicion` 108 | la marca aparece en el 101 |
| 116 · 117–121 | | | | la frase 1 sale | | la marca aparece sobre «Amén» en el 116 |
| **120** | **●●● bajo** | **toque en «🙌 Amén»** → el selector se cierra, el botón queda **«🙌 Amén»** en su color (morado claro) y su 🙌 salta, y **el total sube en uno (real)** | quieta | **«Llega a cada celular.»** entrada-linea 120–126 | **`toque` c (1,4) en el 121 · `aparicion` (1,4) en el 123** | |
| 135 | ● | el 🙌 termina su salto (la app lo anima 0,4 → 1,35 → 1 con su resorte, 121–≈138; se usa a 1×, sin rampa) | quieta | frase 2 quieta | — | |
| **150–163** | ● | quieta | **Movimiento del compás 3**: M `reacciones` → **M `tarjeta`** (sube ≈ 40 px CSS: «Inscribirme» al centro, «🙌 Amén» abajo) | | — | |
| **165** | ● | quieta | quieta | | — | **`dedo-espera`:** la marca aparece sobre «Inscribirme» (165–169) y se queda |
| 177–181 | | | | la frase 2 sale | | |
| **180** | **●●● pico** | tramo `evento`: **toque en «Inscribirme»** → la app abre el evento (el corte cae en la espera): **«← Mi iglesia»**, la portada (verde, real), «Encuentro», **«Congreso de Jóvenes»**, y la entrada propia de la app (la cabecera escala, los datos suben, 180–200) | la pantalla nueva llega en **G `evento`** (sin movimiento: el iris la descubre ya encuadrada) | — | **`toque` b (1,4) en el 181** | **Iris desde el toque** 180–185 (still del 179 debajo); halo 1,08 → 1 (180–270) |
| **195** | ● | quieta | quieta | **«MI IGLESIA»** entrada-linea 195–201 | `aparicion` 196 | |
| **240–253** | ●● | quieta | **Movimiento del compás 5**: G → **M `datos`** (las fechas (real), «Día 1 · Día 2», la descripción a 44 px) | | — | |
| **300–315** | ● ● | tramo `inscripcion`: **la app baja a «Inscripción»** (suave, real): entran **«Inscripción»**, el mensaje **«Llega 30 minutos antes con tu boleta en el celular (también funciona sin señal).»** y **«Inscribirme»** | **quieta** (M) | | `desliz` (acento 303) | |
| **330–343** | ● | quieta | **Movimiento del compás 6**: M → **M `inscripcion`** (el mensaje y el botón) | | — | |
| **360** | ● | quieta | quieta | **«Y se inscribe / con su familia»**: Y 360 · se 362 · inscribe 364 · con 366 · su 368 · familia 370 | — | la marca aparece sobre «Inscribirme» en el 371 |
| **375** | ● | tramo `familia`: **toque en «Inscribirme»** → entra (se desliza, real) **«¿A quiénes inscribes? (hasta 4)»** con **«Yo» ☑** y **{su esposo} (real) ☐** · «Cancelar · Seguir» | quieta | frase 3 quieta | `toque` a 376 | |
| **390–403** | ● | quieta | **Movimiento del compás 7**: M → **M `quienes`** | | — | |
| **420** | ● | **toque en la casilla del esposo** → ☑ | quieta | | `toque` b 421 | la marca en el 416 |
| **450** | ● | **toque en «Seguir»** → entra **«1 de 2: Tú»**: «Talla de camiseta *» S · M · L · XL y «¿Es tu primera vez en el congreso?» Sí · No; 452–464 la app centra el formulario (suave, real) | **quieta** | | `toque` c 451 | la marca en el 446 |
| **465–478** | ● | quieta | **Movimiento del compás 8**: M → **G `form`** (el formulario entero) | | — | |
| **480 · 495** | ● ● | **«M»** se llena · **«Sí»** se llena | quieta | | `toque` a 481 · b 496 | marcas en 476 · 491 |
| **510** | ● | **toque en «Seguir»** → el formulario cambia a **«2 de 2: {su esposo}» (real)** con los radios vacíos | quieta | | `toque` c 511 | la marca en el 506 |
| **540 · 555** | ● ● | **«L»** · **«No»** | quieta | | `toque` a 541 · b 556 | marcas en 536 · 551 |
| **570–583** | ● | quieta | **Movimiento del compás 10**: G → **M `botones-form`** («¿Es tu primera vez…?» con «No» y «Atrás · **Inscribir**») | | — | |
| 596 · 597–601 | | | | la frase 3 sale | | la marca sobre «Inscribir» en el 596 |
| **600** | **●●● 2.ª subida** | tramo `inscrito`: **toque en «Inscribir»** → el **sello** (la boleta en un círculo morado) entra con su resorte, **el confeti de la app**, **«¡Quedaste inscrito!»**, «Tu boleta ya está en Mis boletas: también se ve sin señal.», las dos filas **«{ella} · Inscrito» · «{su esposo} · Inscrito» (real)** y **«Ver boleta» · «Listo»** (la espera del servidor se corta: el resultado está en el 603) | **Movimiento del compás 11**: M → **G `resultado`**, 600–613 | — | **`toque` c (1,4) en el 601 · `confirmacion` (1,4) en el 603** | |
| 615–645 | ● ● ● | el confeti termina solo (real); el resultado quieto | quieta | | — | la marca sobre «Ver boleta» en el 656 |
| **660** | **●●● golpe** | tramo `boleta`: **toque en «Ver boleta»** → **«Mis boletas»**: la boleta del congreso con su borde de destacada: **«Congreso de Jóvenes»**, sus días (real), **el lugar (real)**, **«Tu boleta»**, **el QR**, **«Código ······» (real)**, «Descargar la boleta» | la pantalla nueva llega en **G `boleta`** | — | **`toque` a (1,4) en el 661 · `confirmacion` (1,0) en el 663** | **Corte sobre el toque:** en el 663 la pantalla ya es «Mis boletas» y entra 1,03 → 1,00 (`aterrizaje-app`, 663–673) |
| **690–698** | ● | quieta | **Punch** G → **M `qr`** (9 cuadros): el QR y el código a 44 px | — | — | |
| 716 | | | | | | la marca sobre el QR |
| **720** | **●●● golpe** | tramo `grande`: **toque en el QR** → **la boleta a pantalla completa, sobre blanco** (la app la trae en 220 ms, 0,96 → 1): el QR grande, **el nombre de la miembro (real)**, el código, «Congreso de Jóvenes», «Cerrar» | **Movimiento del compás 13**: M → **G `grande`** (el QR, el nombre y el código), 720–733 | **«Tu iglesia, en el *bolsillo* / de cada miembro»**: Tu 720 · iglesia, 722 · en 724 · el 726 · *bolsillo* 728 · de 730 · cada 732 · miembro 734. **La ceja sale 720–723** | `toque` b 721 · `aparicion` 723 | **La ventana se hace a un lado**: escala 1 → 0,92 + x (§1.4), 724–738 (9:16: 720–734); halo 1,08 → 1 (720–810) |
| 735–836 | 735 … 825 | quieta (la boleta real, la pantalla encendida) | quieta | frase 4 quieta 3,5 s | **`subida`** 796–853 (golpe en el 840) | |
| **837–839** | | — | — | — | — | **Dip** al 40 %, 3 cuadros |
| **840** | **●●● el más fuerte** | — | — | — | la música 0,7 → 0,224 (852) → 0 (870) | **Corte a la firma**: 4:5 `cierre-clip`, 9:16 `cierre-corto`; `{"llamado":"prueba","fondo":"azul","idioma":"es"}` |
| 846 · 853 ↓ | | la K sube; las 7 barras de la corona desde 0,45 s (`back.out(2.2)`) | | «Kingdom» 0,75 s; **«Prueba gratis 30 días»** 0,95 s | **Campanas en el 851** | |
| **914** | | último cuadro: la corona completa y el botón | | | silencio de música desde el 870 | fin |

### 2.2 Los siete planos

#### P1 · «¿Se enteró toda la iglesia?» — cuadros 0–119 (compases 1–2) · pulsos 0, 15, 30, 45, 60, 75, 90, 105

- **Grabación:** tramos `inicio` (Mi iglesia arriba, quieto 1,8 s; a 1×), `bajar` (el desplazamiento suave hasta la novedad, a la velocidad
  que lo haga caber en 60–75: si dura 0,9 s, a 1,8×) y el comienzo de `reaccion` (el toque en la flecha y el selector que se abre, a 1×).
- **Encuadre 4:5:** G `inicio` (CSS 0–439) quieto mientras la app baja; M `reacciones` desde el 103. **9:16:** G muestra 345 px CSS: el
  cuadro 0 queda en CSS 0–345 (la barra con el logo, que es la marca de la iglesia, el saludo, «Mis servicios» y «Mis Equipos»; la
  destacada no entra y no hace falta); M igual.
- **Cámara:** quieta hasta el 90; 90–103 a M `reacciones`. Nada más.
- **Texto:** frase 1 por pulsos (la primera landing ya puesta en el cuadro 0); sale 117–121.
- **Sonido:** desliz 63, toque 106, aparicion 108.
- **Transición:** ninguna; cierra con el toque del 120.
- **Válvula si el desplazamiento se ve como un salto** (Chrome a veces lo hace en dos tiempos): se toma solo su segunda mitad (la llegada a
  la novedad) en 66–75 y el 60 queda con la app quieta y el `desliz` en el 66.

#### P2 · «Llega a cada celular» — cuadros 120–179 (compás 3) · pulsos 120 (bajo), 135, 150, 165

- **Grabación:** tramo `reaccion` (el toque en «Amén», el salto y 1,5 s quieto).
- **Encuadre:** M `reacciones` y, desde el 163, M `tarjeta`. El selector abre hacia arriba **dentro** del encuadre (si en la grabación sale
  por encima de 403, la cámara del 90 se centra 30 px más arriba).
- **Cámara:** quieta en el toque; 150–163 a M `tarjeta`.
- **Texto:** frase 2 entra 120–126 (línea entera), sale 177–181.
- **Sonido:** toque 121 (1,4), aparicion 123 (1,4).
- **Transición:** ninguna dentro; la marca espera desde el 165; cierra con el iris del 180.

#### P3 · «El congreso» — cuadros 180–359 (compases 4–6) · pulsos 180 (pico), 195, 240, 300, 330

- **Grabación:** tramos `evento` (el toque en la tarjeta, la carga del evento —se corta— y 2,5 s quieto) e `inscripcion` (la app baja a
  «Inscripción», 1,5 s quieto). A 1× salvo el desplazamiento, que va al ritmo que lo haga caber en 300–315.
- **Encuadre:** G `evento` (180–239), M `datos` (253–299), M `inscripcion` (desde el 343). En 9:16, M muestra 247 px CSS: `datos` se centra en
  las fechas y los días; `inscripcion`, en el mensaje y el botón.
- **Cámara:** 240–253 y 330–343; quieta en el iris y mientras la app baja (300–315).
- **Texto:** la ceja «MI IGLESIA» 195–201; sin frase (el evento es el espectáculo).
- **Sonido:** toque 181 (1,4), aparicion 196, desliz 303.
- **Transición:** iris desde «Inscribirme» de la tarjeta (180–185).
- **Si asoma la K del cargador** al abrir el evento: el corte del 180 cae en la espera y el iris descubre el evento ya cargado.

#### P4 · «Y se inscribe con su familia» — cuadros 360–599 (compases 7–10) · pulsos 360, 375, 390, 420, 450, 465, 480, 495, 510, 540, 555, 570

- **Grabación:** tramos `familia` (el toque, la lista que entra, la casilla del esposo, «Seguir») y `formulario` (la app centra el formulario;
  M, Sí, «Seguir», L, No). A 1×; las pausas de la escena se recortan para que cada toque caiga en su pulso.
- **Encuadre:** M `inscripcion` hasta el 390; M `quienes` (403–464); G `form` (478–569); M `botones-form` (desde el 583). En 9:16 los mismos
  objetivos; `form` muestra 345 px CSS: se centra en las dos preguntas y deja «Atrás · Seguir» para el 570.
- **Cámara:** 390–403, 465–478 y 570–583 (compases 7, 8 y 10); el compás 9 es solo la app (tres toques). Quieta mientras la app centra el
  formulario (452–464).
- **Texto:** frase 3 entra 360–370 (seis palabras a 2 cuadros); sale 597–601.
- **Sonido:** toque 376, 421, 451, 481, 496, 511, 541, 556.
- **Transición:** ninguna (la lista y los formularios se deslizan dentro de la app).
- **Plan B (sin esposo, §3):** 375 «Inscribirme» → si sale la lista, 420 «Seguir» (sin marcar a nadie más); si no, el formulario entra
  directo en el 375. Un solo formulario: 480 «M», 510 «Sí», 570 la cámara a «Inscribir». La frase 3 pasa a **«Y se inscribe sin hacer
  fila»** («Y se inscribe / sin hacer fila»). El resultado tiene una fila y «Mis boletas», una boleta.

#### P5 · «¡Quedaste inscrito!» y la boleta — cuadros 600–719 (compases 11–12) · pulsos 600 (subida), 660 (golpe), 690

- **Grabación:** tramos `inscrito` (el toque, el resultado y el confeti, 3 s quieto) y `boleta` (el toque, la carga de «Mis boletas»
  —se corta— y 2,5 s quieto). A 1×; el confeti nunca se acelera (es una animación de la app: 615–645 a 1×).
- **Encuadre:** G `resultado` (613–659); G `boleta` (663–689); M `qr` (desde el 698).
- **Cámara:** 600–613 y el punch 690–698; en el 660 la pantalla nueva llega ya en G `boleta` bajo el aterrizaje.
- **Texto:** ninguno (las dos pruebas las da la app).
- **Sonido:** toque 601 (1,4), confirmacion 603 (1,4), toque 661 (1,4), confirmacion 663 (1,0).
- **Transición:** corte sobre el toque del 660 (`aterrizaje-app` 663–673).
- **Si la app no dibuja el confeti** (modo ligero o movimiento reducido en el navegador de la grabación): se queda el sello con su resorte;
  nada se agrega (regla 23).

#### P6 · «Tu iglesia, en el bolsillo de cada miembro» — cuadros 720–839 (compases 13–14) · pulsos 720 (golpe), 735 … 825

- **Grabación:** tramo `grande` (el toque en el QR y la boleta a pantalla completa, 4,5 s quieta a 1×).
- **Encuadre:** G `grande` con la ventana a 0,92 y corrida (§1.4): el QR, el nombre y el código; el cuerpo de la app a ≥ 31 px. En 9:16 la
  ventana se encoge desde abajo y su borde de arriba queda en 548.
- **Cámara:** 720–733 a G; después muerta de quieta. El halo se asienta 720–810.
- **Texto:** frase 4 entra 720–734 (*bolsillo* en itálica dorada); la ceja sale 720–723; la frase se sostiene 3,5 s.
- **Sonido:** toque 721, aparicion 723, subida 796–853.
- **Transición:** dip 837–839 y corte duro al 840.

#### P7 · «La firma» — cuadros 840–914

- 4:5: `identidad/cierre-clip.html`; 9:16: `identidad/cierre-corto.html`. Variables `{"llamado":"prueba","fondo":"azul","idioma":"es"}`.
- Campanas en 28,38 (cuadro 851). La música: 0,7 → 0,224 (852) → 0 (870).
- El único gesto de marca del clip.

---

## 3. La grabación: la escena `tools/ayuda/escenas/clips/mi-iglesia-boleta.mjs`

Una sola escena de **celular** (`movil: true`, 390×844 a 3× → **1170×2532**, 30 cps) sin el círculo del toque (`toque: false`), con
`capturar.mjs --modo video` sobre Kingdom Demo en español:

```bash
cd F:/Proyectos/KingdomApp/tools/ayuda
node capturar.mjs clips/mi-iglesia-boleta --idioma es --modo capturas   # primero: prueba el sql y las refs sin grabar
node capturar.mjs clips/mi-iglesia-boleta --idioma es --modo video
# → salida/video/es/clips/mi-iglesia-boleta/grabacion.mp4 + pasos.json (inicio/fin, tramo, accion, toques[], teclas[], caja, caja_video)
```

**Cuenta:** 105 = la cuenta de captura del **miembro** (`_demo_capturas.php`, línea 22: nivel `miembro`, sin módulos de servicio; líneas
113–114: su ficha es «un adulto casado, sin cargo y con correo»; en la demo, «Gabriela»). Es la persona del recorrido del Portal
(`_demo_portal_6_recorrido.php`, líneas 15–19 y 47–53): terminó la bienvenida, está en Jóvenes, tiene un objetivo al día y estaba inscrita en
el congreso. **Datos ficticios:** todo es de Kingdom Demo; la escena no escribe ningún dato personal (solo elige radios y casillas).

**Lo que la semilla garantiza** (verificado): la novedad «Inscripciones abiertas» con un bloque de texto y la tarjeta de un evento, en ese
orden (`_demo_portal_3_publicaciones.php`, línea 84); el «Congreso de Jóvenes» a 30 días, de dos días, categoría Encuentro visible en Mi
iglesia y con boletería, formulario «Talla de camiseta» (`talla`: s, m, l, xl; obligatoria) y «¿Es tu primera vez en el congreso?»
(`primera`: si, no), `max_por_cuenta` 4, la familia permitida (por omisión) y el mensaje de la inscripción (`_demo_eventos_inscripcion.php`,
líneas 39–66); el diseño de su boleta (`tools/ayuda/semillas/comunicaciones.php`, líneas 158–168); «Amén» 🙌 en el catálogo
(`backend/_datos/portal.php`, línea 34).

**Lo que la escena deja como lo necesita la historia** (su `sql`, que `capturar.mjs` corre sobre la base restaurada antes de las `refs`;
todo local, la base de las capturas se vuelve a restaurar en cada corrida):

1. La tarjeta de la novedad apunta al **primer evento activo con portada** (`_demo_portal_3_publicaciones.php`, línea 77), no al congreso:
   se repunta al congreso (`bloques[1].id` y `ref_id`, la tarjeta se resuelve en vivo: `poPubEventosResueltos`) y la novedad pasa a ser la
   más reciente del feed («hace 3 minutos»; el feed se ordena por `publicar_at`).
2. La miembro pudo haber reaccionado a esa novedad (la semilla reparte reacciones entre las primeras 150 fichas): se borra su reacción y se
   recuentan los conteos, para que «Amén» la ponga y no la quite.
3. La miembro está inscrita en el congreso (`comunicaciones.php`, línea 166) y su esposo puede estarlo: se borran esas inscripciones (con sus
   filas de reporte `em_inscritos` y `em_respuestas`, que no tienen llave; `ev_ingresos` y `ev_boletas_imagen` se van por su llave). Una
   cancelada no sirve: la pantalla la mostraría («Tú · Cancelado») y el botón diría «Inscribir a alguien más».
4. El congreso quedó **con el cupo lleno y con aprobación** (`_demo_eventos_inscripcion.php`, líneas 71–75): se abre sin cupo y sin
   aprobación, para que el resultado sea «¡Quedaste inscrito!» con su boleta y no «lista de espera» o «por aprobar».

**Selectores** (verificados en `frontend-v2/src/app/pages/mi/mi-inicio.page.ts`, `components/publicaciones/publicacion-tarjeta.component.ts`,
`components/publicaciones/reacciones.component.ts`, `components/bloques/tarjeta-ref.component.ts`, `pages/mi/evento.page.ts`,
`pages/membresia/formulario-responder.component.ts` y `pages/mi/boletas.page.ts`).

```js
// Grabación para el clip del sitio público «Se enteró toda la iglesia» (LegacyHyperframes/videos/kingdomapp/clip-sitio-mi-iglesia/SPEC.md §3).
// NO es una escena de un artículo de la ayuda: no se publica ni entra en la frescura. Una sola escena de CELULAR (390×844 a 3x = 1170×2532,
// 30 cps) grabada SIN el círculo del toque (`toque: false`): el montaje dibuja el suyo sobre toques[] y las cajas de pasos.json.
//   node capturar.mjs clips/mi-iglesia-boleta --idioma es --modo capturas   (prueba el sql y las refs)
//   node capturar.mjs clips/mi-iglesia-boleta --idioma es --modo video
//   → salida/video/es/clips/mi-iglesia-boleta/grabacion.mp4 + pasos.json
// Tramos: inicio (Mi iglesia arriba) · bajar · reaccion · evento · inscripcion · familia · formulario · inscrito · boleta · grande. Todo con la
// cuenta 105 (la miembro de las capturas; «Gabriela» en la demo), que se inscribe con su cónyuge al Congreso de Jóvenes de la semilla.
// Datos ficticios de Kingdom Demo; la escena no escribe datos personales (solo radios y casillas).
const KDEMO = `(SELECT id FROM kd_sedes WHERE codigo = 'KDEMO')`;
const CONGRESO = `(SELECT MAX(e.id) FROM ev_eventos e WHERE e.id_sede = ${KDEMO} AND e.nombre IN ('Congreso de Jóvenes', 'Youth Conference'))`;
const YO = `(SELECT us.id_persona FROM kd_usuario_sedes us WHERE us.id_usuario = 105 AND us.id_sede = ${KDEMO})`;
const NOVEDAD = `p.id_sede = ${KDEMO} AND p.ambito = 'iglesia' AND p.ref_tipo = 'evento' AND p.titulo IN ('Inscripciones abiertas', 'Registration is open')`;
const POST = '#mi-feed article[data-publicacion="{@post}"]';
const BOLETA = { es: '#boletas-lista li.boleta.destacada:has-text("Tu boleta")', en: '#boletas-lista li.boleta.destacada:has-text("Your ticket")' };
const enBoleta = sufijo => ({ es: `${BOLETA.es} ${sufijo}`, en: `${BOLETA.en} ${sufijo}` });
const radio = (pregunta, opcion) => `#mi-evento-form [data-pregunta="${pregunta}"] mat-radio-button[data-opcion="${opcion}"]`;

export default {
  articulo: 'clips/mi-iglesia-boleta',
  movil: true,
  toque: false,
  pantallas: [
    'frontend-v2/src/app/pages/mi/mi-inicio.page.ts',
    'frontend-v2/src/app/components/publicaciones/publicacion-tarjeta.component.ts',
    'frontend-v2/src/app/components/publicaciones/reacciones.component.ts',
    'frontend-v2/src/app/components/bloques/tarjeta-ref.component.ts',
    'frontend-v2/src/app/pages/mi/evento.page.ts',
    'frontend-v2/src/app/pages/membresia/formulario-responder.component.ts',
    'frontend-v2/src/app/pages/mi/boletas.page.ts',
  ],
  // Sobre la base restaurada (solo local), antes de las refs. Ver SPEC §3, puntos 1 a 4.
  sql: [
    // 1. La novedad «Inscripciones abiertas» lleva la tarjeta del congreso y es la más reciente del feed.
    `UPDATE po_publicaciones p
        SET p.ref_id = ${CONGRESO}, p.bloques = JSON_SET(p.bloques, '$.bloques[1].id', ${CONGRESO}), p.publicar_at = NOW() - INTERVAL 3 MINUTE
      WHERE ${NOVEDAD} AND p.estado = 'publicada' AND JSON_VALUE(p.bloques, '$.bloques[1].t') = 'evento'`,
    // 2. Sin la reacción de la miembro en esa novedad (el «Amén» del cuadro 120 la pone), con los conteos al día.
    `DELETE r FROM po_reacciones r JOIN po_publicaciones p ON p.id = r.id_publicacion WHERE ${NOVEDAD} AND r.id_persona = ${YO}`,
    `UPDATE po_publicacion_conteos c JOIN po_publicaciones p ON p.id = c.id_publicacion
        SET c.n = (SELECT COUNT(*) FROM po_reacciones r WHERE r.id_publicacion = c.id_publicacion AND r.codigo = c.codigo)
      WHERE ${NOVEDAD}`,
    // 3. Sin inscripciones de la miembro (ni las que ella hizo) ni de su cónyuge en el congreso, con sus filas de reporte (sin llave).
    `DELETE i, m, q FROM ev_inscritos i
       LEFT JOIN em_inscritos m ON m.id_inscrito = i.id
       LEFT JOIN em_respuestas q ON q.formulario = 'inscripcion' AND q.id_ref = i.id
      WHERE i.id_evento = ${CONGRESO}
        AND (i.id_persona = ${YO} OR i.inscrito_por_persona = ${YO}
             OR i.id_persona IN (SELECT IF(f.id_persona = ${YO}, f.id_pariente, f.id_persona) FROM mem_parentescos f
                                  WHERE f.tipo = 'conyuge' AND ${YO} IN (f.id_persona, f.id_pariente)))`,
    // 4. El congreso, abierto sin cupo y sin aprobación: el resultado es «¡Quedaste inscrito!» con la boleta.
    `UPDATE ev_inscripciones SET aprobacion = 0, cupo = NULL WHERE id_evento = ${CONGRESO}`,
  ],
  refs: {
    congreso: `SELECT ${CONGRESO}`,
    yo: `SELECT ${YO}`,
    // La novedad ya repuntada (si el sql 1 no la tocó, no hay valor y la escena se niega).
    post: `SELECT p.id FROM po_publicaciones p WHERE ${NOVEDAD} AND p.estado = 'publicada' AND p.ref_id = ${CONGRESO}
             AND JSON_VALUE(p.bloques, '$.bloques[1].id') = p.ref_id ORDER BY p.id DESC LIMIT 1`,
    // Su cónyuge, activo en la iglesia (la familia que la inscripción ofrece: evInsFamilia). Sin él, NULL: la escena se niega y entra el
    // plan B del SPEC (§3, notas).
    conyuge: `SELECT x.id FROM mem_parentescos f JOIN mem_personas x ON x.id = IF(f.id_persona = ${YO}, f.id_pariente, f.id_persona)
                WHERE f.tipo = 'conyuge' AND ${YO} IN (f.id_persona, f.id_pariente) AND x.id_sede = ${KDEMO} AND x.estado = 'activa'
                  AND x.eliminado_at IS NULL AND x.fusionada_en IS NULL LIMIT 1`,
    // El congreso quedó abierto, sin cupo y sin aprobación (sql 4).
    abierto: `SELECT IF(activa = 1 AND aprobacion = 0 AND cupo IS NULL, 1, NULL) FROM ev_inscripciones WHERE id_evento = ${CONGRESO}`,
  },
  pasos: [
    // 1-2. Mi iglesia arriba (cuadro 0 del clip): la barra con el logo, el saludo, «Mis servicios», «Mis Equipos» y la destacada.
    { tramo: 'inicio', como: 105, ir: '/mi', espera: POST },
    { pausa: 1800 },
    // 3. La app baja sola hasta la novedad del congreso (el desliz del 60): queda centrada.
    { tramo: 'bajar', ver: POST, pausa: 1500 },
    // 4-5. «Amén» (el toque del 120, el bajo): la flecha abre las reacciones y se elige «Amén».
    { tramo: 'reaccion', clic: '#reacciones-mas-{@post}', espera: `${POST} .selector .opcion[data-codigo="amen"]`, pausa: 700 },
    { clic: `${POST} .selector .opcion[data-codigo="amen"]`, oculto: `${POST} .selector`, pausa: 1500 },
    // 6. «Inscribirme» en la tarjeta de la novedad (el toque del 180, el pico): el evento en Mi iglesia.
    { tramo: 'evento', clic: `${POST} article[data-evento="{@congreso}"] button`, espera: '#mi-evento-nombre', pausa: 2500 },
    // 7. La app baja a «Inscripción» (el desliz del 300): el mensaje y «Inscribirme».
    { tramo: 'inscripcion', ver: '#mi-evento-inscripcion', pausa: 1500 },
    // 8-10. «Inscribirme» (el toque del 375): a quiénes; se marca al cónyuge (420) y «Seguir» (450).
    { tramo: 'familia', clic: '#btn-inscribirme', espera: '#mi-evento-quienes', pausa: 1200 },
    { marcar: '#mi-evento-quienes mat-checkbox[data-persona="{@conyuge}"]', pausa: 700 },
    { clic: '#btn-quienes-seguir', espera: '#mi-evento-form[data-persona="{@yo}"]' },
    // 11-16. Los dos formularios: la app centra el formulario (452–464); M y Sí para ella, «Seguir», L y No para él.
    { tramo: 'formulario', ver: '#mi-evento-form', pausa: 900 },
    { marcar: radio('talla', 'm'), pausa: 400 },
    { marcar: radio('primera', 'si'), pausa: 400 },
    { clic: '#btn-form-seguir', espera: '#mi-evento-form[data-persona="{@conyuge}"]', pausa: 700 },
    { marcar: radio('talla', 'l'), pausa: 400 },
    { marcar: radio('primera', 'no'), pausa: 900 },
    // 17. «Inscribir» (el toque del 600, la segunda subida): el sello, el confeti y «¡Quedaste inscrito!». Quieto 3 s.
    { tramo: 'inscrito', clic: '#btn-form-seguir', espera: '#mi-evento-resultado[data-estado="inscrito"] #btn-ver-boleta', pausa: 3000 },
    // 18. «Ver boleta» (el toque del 660, el golpe): Mis boletas con el QR.
    { tramo: 'boleta', clic: '#btn-ver-boleta', espera: enBoleta('.qr-boton svg.qr'), pausa: 2500 },
    // 19. El QR (el toque del 720): la boleta a pantalla completa, quieta 4,5 s para el final.
    { tramo: 'grande', clic: enBoleta('.qr-boton'), espera: '#boleta-grande .qr-g', pausa: 4500 },
  ],
};
```

Notas sobre la escena:

- **`ver` desplaza suave** (`block: 'center'`, 900 ms de espera) y es el único desplazamiento que se graba: el de la novedad (60–75), el de
  «Inscripción» (300–315) y el del formulario (452–464). En el celular la barra de la app es fija: nunca `bloque: 'start'`. Antes de cada
  `clic` y `marcar` el elemento ya está a la vista, así que el `scrollIntoViewIfNeeded` de la herramienta no salta. **Si el resultado del
  600 no cabe entero** (la app agrega el lugar del evento arriba al quedar inscrita), Chrome ancla el desplazamiento y no se mueve; si se
  moviera, el `clic` en «Ver boleta» saltaría y ese salto cae en el corte del 660.
- **Las cajas de la cámara** (§1.5) salen de `caja`/`caja_video` de los pasos que las nombran (`ver`, `clic`, `marcar`); las de `inicio`,
  `datos` y `grande` se miden sobre los cuadros de la grabación (no se agrega un `ver` solo para una caja: desplazaría la pantalla).
- La herramienta espera la red en reposo y 400 ms tras cada acción, más lo que diga `pausa`; `marcar` toca la etiqueta del radio o de la
  casilla (un toque real, con su marca en `toques[]`). Todo lo que sobra se corta en el montaje; nada se puede alargar: por eso las pausas
  largas sobre lo que se mira (1,5–3 s) y los 4,5 s finales.
- **Tiempos:** ≈ 1,8 + 2,4 + 2,1 + 3,0 + 4,5 + 2,4 + 2,6 + 2,1 + 1,4 + 1,9 + 1,9 + 1,9 + 2,3 + 1,9 + 2,4 + 4,6 + 4,5 + 5,9 ≈ **50 s de
  grabación** para 28 s de clip. No hace falta `consolaEsperada` (no hay tramo sin señal; el `wakeLock` de la boleta en grande falla en
  silencio si el navegador sin cabeza no lo da).
- **Plan B** (la `ref` `conyuge` da NULL): se quitan la `ref` y el paso del cónyuge; el `clic` en «Seguir» de la lista pasa a `clicSiHay`
  (la lista sale solo si hay otro familiar); se quitan los dos `marcar` y el `clic` del segundo formulario, y el `espera` del 17 queda igual.
  En el clip: P4 con un solo formulario y la frase 3 «Y se inscribe sin hacer fila» (§2.2, P4).
- **Para el still del iris:** el cuadro 179 de la ventana se exporta (`ffmpeg -ss <t> -frames:v 1`) desde la grabación al tiempo de origen
  correspondiente y va como `<img>` en `assets/stills/` (WebP si el PNG pesa en la vista previa, REVIEW de Membresía §7).
- **Inglés:** la misma escena con `--idioma en` (la novedad «Registration is open», el «Youth Conference», «Your ticket»); los selectores no
  dependen del idioma salvo `BOLETA`, que ya trae los dos textos.

---

## 4. Lo que se revisa en la vista previa

Cuadros a mirar: `npx hyperframes snapshot --at 0,1.5,2.0,2.5,3.0,3.4,3.5,3.6,4.0,4.1,4.5,5.4,5.5,6.0,6.2,6.5,8.0,8.5,10.0,10.5,11.5,12.0,12.4,12.6,13.5,14.0,15.0,15.6,16.0,16.5,17.0,18.0,18.5,19.5,20.0,20.2,21.0,22.0,22.2,23.3,24.0,24.5,27.9,28.0,28.4,30.4`
en las dos composiciones, y `snapshot --range 1.9,2.6 --frames 22` para el desplazamiento de la novedad, `--range 5.9,6.3 --frames 12` para
el iris y `--range 21.9,22.4 --frames 15` para el corte sobre el toque.

1. **Cuadro 0 (la miniatura):** Mi iglesia arriba con la barra «Kingdom Demo», el saludo con el nombre y «Iglesia Kingdom Demo 1»; «¿Se» en
   Fraunces ya puesta; «Datos de ejemplo» abajo a la izquierda. Nunca negro, nunca la marca. En 9:16, nada por encima de 168 ni por debajo de
   1330 salvo halo y puntos.
2. **45:** las cuatro landings de la frase 1 quietas. **60–75:** la app baja y la cámara no se mueve; en el 75 la novedad «Inscripciones
   abiertas · hace 3 minutos» con la tarjeta del congreso; ningún cuadro de página en blanco.
3. **103:** M sobre la tarjeta y las reacciones, «Inscribirme» y la barra a ≥ 44 px. **105–112:** el selector sube con las cuatro reacciones
   (real) y cabe en el encuadre.
4. **120–126:** «Amén» exactamente con el bajo; en el 123 el botón ya dice «🙌 Amén» y el total subió en uno; la frase 2 entera en el 126.
5. **163–179:** M sobre la tarjeta; la marca quieta sobre «Inscribirme» desde el 165.
6. **180–185:** el iris nace del botón «Inscribirme»; debajo, el evento ya cargado (sin la K del cargador); la ceja cae en el 195 y no antes.
7. **253:** las fechas y «Día 1 · Día 2» a 44 px. **300–315:** la app baja y la cámara no se mueve. **343:** el mensaje «Llega 30 minutos
   antes…» y «Inscribirme» enteros a 44 px.
8. **360–370:** la frase 3 palabra a palabra; **375–380:** «¿A quiénes inscribes?» entra con «Yo» marcado; **420:** el esposo marcado;
   **450–464:** «1 de 2: Tú» y la app centra el formulario con la cámara quieta; **478:** G con el formulario entero.
9. **480 · 495 · 510 · 540 · 555:** cada radio y cada botón en su pulso (±1 cuadro); en el 512 «2 de 2: {esposo}» con los radios vacíos.
   **583:** «Atrás · Inscribir» enteros (en Membresía el M de los botones pidió ×1,3: se acepta el mismo ajuste).
10. **600–613:** «Inscribir» con la segunda subida; el sello con su resorte y «¡Quedaste inscrito!» en el 603; el confeti real 603–645, sin
    acelerar; las dos filas «Inscrito».
11. **660–673:** «Ver boleta» en el golpe; «Mis boletas» con el QR y «Tu boleta» desde el 663, entrando 1,03 → 1,00. **698:** M sobre el QR y
    el código a 44 px: debe leerse de un vistazo.
12. **720–738:** la boleta en grande sobre blanco desde el 727; la frase 4 aterrizada en el 734 con *bolsillo* dorada; la ceja fuera; la
    ventana a 0,92 y corrida; ningún glifo de la frase toca la ventana en ningún cuadro (en 9:16 tampoco: la ventana baja 720–734). La
    primera línea de la frase 4 medida ≤ 888 px (si no, §1.2). **738–836:** nada se mueve salvo el halo; **837–839** el dip; **840** el primer
    cuadro de la firma sin noche vacía entre medias.
13. **Sonido (medido, no oído):** cada `toque` un cuadro después de su imagen; las dos `confirmacion` en 603 y 663; las campanas en el 851;
    la música a −10 dB en el 852 y a 0 en el 870; −16 LUFS, pico ≤ −1 dBTP; ningún tramo con dos sonidos de acción encimados salvo 106 + 108,
    121 + 123, 601 + 603, 661 + 663 y 721 + 723.
14. **Textos:** ninguna palabra que no esté en la app o en las cuatro frases; ningún texto de la app < 28 px; las frases en 2 líneas (3 en
    9:16 la cuarta); `npx hyperframes check` en 0 errores (contraste AA incluido); «Datos de ejemplo» desde el cuadro 0.
15. **La historia sin sonido:** se entiende con la pantalla en silencio (así se verá en el sitio): ¿se enteró? → la novedad del congreso en
    su celular → Amén → el evento → ella y su esposo → ¡Quedaste inscrito! → la boleta con QR → en el bolsillo → Kingdom.

---

## 5. Riesgos y lo que se decide al grabar

- **El cónyuge.** La miembro de las capturas es «un adulto casado» (`_demo_capturas.php`, línea 113) y la captura de la ayuda muestra
  «Inscribir a alguien más» (tiene familia que puede inscribir), pero el cónyuge tiene que estar activo en la iglesia. La `ref` `conyuge` lo
  exige; si falla, el plan B (§3, notas; P4) y la frase 3 «Y se inscribe sin hacer fila». Si la lista muestra más familiares (hijos), se
  dejan sin marcar: se ven y dicen lo mismo.
- **El `sql` de la escena.** Cuatro cambios sobre la base local de las capturas (se restaura en cada corrida). Se prueba primero con
  `--modo capturas`: las `refs` `post` y `abierto` fallan si la novedad no quedó repuntada o el congreso no quedó abierto. Ninguna
  subconsulta lee la tabla que se modifica (lo que MariaDB rechaza con el error 1093); si aun así alguna se queja, se reemplaza por un
  `JOIN` a `ev_eventos` y `kd_usuario_sedes` (cada `sql` corre en su propia llamada a `mariadb -e`: no hay variables de sesión entre ellas).
- **El cargador de la app** (`loading.wrap`, la K animada a los 150 ms) al abrir el evento (180), al inscribir (600) y en «Mis boletas»
  (660): con la API local no debería asomar; si asoma, se corta en la espera (los cortes de esos tres toques ya caen ahí).
- **El confeti** (`celebrar`) no sale con movimiento reducido ni en el modo ligero de la app; el Chrome de la grabación no pide ninguno de
  los dos. Si aun así no sale, se queda el sello (regla 23).
- **El desplazamiento largo del 60** (≈ 1.900 px CSS: la destacada, el calendario, los próximos eventos) puede durar más de 1 s en Chrome:
  a 3,5× como máximo cabe hasta 1,7 s en 15 cuadros; si dura más, la válvula de P1 (solo la llegada).
- **El selector de reacciones** sale hacia arriba desde la barra y puede taparse con la tarjeta si la novedad es corta: en la grabación se
  ve; si queda fuera de M `reacciones`, la cámara del 90 sube 30 px.
- **El foco** que la app devuelve al botón de reacciones después de «Amén» (`boton.focus()`) no debería pintar el anillo de foco (el último
  toque fue con el dedo); si lo pinta, es real y se deja.
- **El saludo** depende de la hora de la grabación («Buenos días» antes de las 12, «Buenas tardes» hasta las 7 p. m.): conviene grabar en la
  mañana para que el cuadro 0 diga «Buenos días», pero ninguna frase depende de eso. El nombre, las fechas del congreso, el lugar, los
  conteos y el código cambian con la semilla.
- **El QR** codifica el token local de la boleta de Kingdom Demo: no sirve fuera de la base de las capturas. Va con «Datos de ejemplo».
- **Densidad de 0–6 s:** cinco sonidos, cuatro toques, un desplazamiento y tres movimientos de cámara. Si en la vista previa va atropellado,
  se quita el movimiento del 150 (la marca del 165 espera sobre «Inscribirme» desde M `reacciones`, que también lo muestra).
- **Densidad de 375–600:** ocho toques en 7,5 s, a velocidad normal de la app. Es el respiro de la pista y la tarea de la frase 3; si se siente
  apurado, la primera pregunta de cada formulario («Talla») se deja y la segunda («¿Primera vez?») se quita de la escena (no es
  obligatoria): 480 «M», 510 «Seguir», 540 «L», 570 la cámara.
- **Kit:** usa tal cual lo ya construido para Membresía y Eventos (`cierre-clip`, `.k-ventana`, `.k-feed-*`, el modo video de celular con
  `toque: false` y `toques[]`). Nada nuevo de herramienta.
- **Si la serie pasa a 18 compases** (la propuesta de la ampliación de Membresía): lo de 0 a 24,0 no cambia; en el 24,0 la boleta en grande
  sin frase; en el 26,0 «Cerrar» y la barra de abajo → «Objetivos»; en el **28,0** (el golpe más fuerte) «Mis objetivos» con «Un devocional
  cada mañana» al día y sus «Objetivos de conexión» (la vida del miembro más allá del evento), con una cuarta frase nueva; en el 32,0 la
  frase del sitio; en el 36,0 la corona. Pide un tramo más en la escena (`ir: '/mi/objetivos'`, la escena `mi-iglesia/mis-objetivos.mjs` ya
  lo usa) y se decide entonces.
- **Lo que queda para el recorrido de 60–75 s** (la misma historia y después más funciones): la bienvenida por el QR (portada, el camino y
  «Cómo orar»), una comunidad (Jóvenes, su feed y «Conectar con un líder»), Mis objetivos y Mi ficha.
- **Idiomas (en, pt después):** la misma escena con `--idioma en` graba la interfaz en inglés; las frases se traducen y los saltos se vuelven
  a fijar; la firma lleva `idioma`.
