# REVIEW · Clip del sitio: Membresía — «Valeria llegó el domingo» (4:5) · v2

2026-10-30 · **Versión 2, la ampliación** (SPEC v2, STORY §Ampliación): 38,5 s = 1155 cuadros, la firma en el 1080. Construida en HyperFrames
0.8.221 sobre el montaje v1 (que sigue igual de 0 a 719) con la grabación nueva `assets/grabaciones/grabacion-2.mp4` + `pasos-2.json` (G2,
1170×2532, 30 fps, 3416 cuadros) desde el 780. El dueño ya no revisa: construido, verificado, renderizado y entregado.
**Render de entrega:** `renders/clip-sitio-membresia-4x5.mp4` (reemplaza al v1; §6). Sin 9:16 todavía (§8).

## 1. Qué hay

| Archivo | Qué es |
|---|---|
| `index.html` | La raíz: el formato (`--f-*` y `window.KD`), los hosts de las escenas, **la ventana a la app** con los tres mundos, los 29 tramos de video (25 de G1, 4 de G2), los stills del iris, las marcas de toque, la cámara, el látigo, el cambio de ventana, el dip, la música y los 21 sonidos |
| `compositions/fondo.html` | La noche del sitio; el halo se asienta en 0, 180, 780 y 960 |
| `compositions/frase-1.html` … `frase-5.html`, `ceja.html` | Las cinco frases y la ceja. **`frase-4.html` es nueva** («Y una ruta / para crecer»); **`frase-5.html` es la frase 4 de la v1** («Que *ninguna* persona / se pierda») movida al 960 |
| `identidad/cierre-clip.html` | La firma del kit v1.1 (1080–1154), con el sonido de marca en 36,38 |
| `assets/stills/still-466.png`, `still-2401.png` | Los cuadros de G1 que quedan debajo del iris del 120 y del 375 (el del 780 no necesita still: debajo sigue `v25`, la tarjeta quieta) |
| `assets/audio/toque-b.wav`, `toque-c.wav` | Las tomas b y c de `toque` (±3 % de tono) |

## 2. Los planos, con sus cuadros

| Plano | Cuadros | Grabación y cámara |
|---|---|---|
| P1 La puerta | 0–119 | G1, sin cambios (ver la v1: 162–467 en ocho tramos) |
| P2 Guardada aun sin señal | 120–185 | G1, sin cambios. Iris 120–125 |
| Látigo | 176–186 | Sin cambios |
| P3 La tarjeta | 180–374 | G1 2207–2402, sin cambios. Cámara M (240), C (300), G (345) |
| P4 El reporte | 375–599 | G1, sin cambios. Iris 375–380 |
| P5 Cumplido | 600–719 | G1, sin cambios. ×1,35 (600), punch ×1,5 (660) |
| **P6 La tarjeta al día y la ficha** | **720–839** | G1 `v25` 2932–3017 (720–785: «Listo» en el 720, la tarjeta al día desde el 738). Cámara 720–733 → **G** sobre la tarjeta (0, 0; v1 iba a G⁺ ×1,05). **780: iris desde el nombre** con la cámara quieta; dentro, G2 `v26` desde el **2840** (la ficha limpia; el toque real es el 2820, la carga y el «Actualizando…» se cortan). 810–823 → ×1,15 sobre la fila «Avance» plegada |
| **P7 Avance: la ruta y los objetivos** | **840–959** | G2 `v27` 2938–2939 (el dedo en «Avance», 840–841); corte de la espera; `v28` desde el **2948** (la tarjeta abierta completa, 842). Desde el 840, debajo, `v29` 3135→ (la ficha ya desplazada, alineada al píxel: §4.1). Cámara 840–853 → ×1,15 de «Avance» a «Historial de pasos»; 900–913 → G⁺ centrado en «Objetivos de conexión» |
| **P8 Que ninguna persona se pierda** | **960–1079** | G2 `v29` (3135–3375, quieta, a 1×). Cámara 960–973 → G⁺ de «Avance» a la primera entrada del historial; la ventana a 0,92 y +48 (964–978); dip 1077–1079 |
| P9 La firma | 1080–1154 | `cierre-clip` (fondo azul, llamado «prueba»); campanas en el 1091 |

Cada corte de video cae dentro de una pausa de la grabación (G2: 2840–2944 quieto, 2948–3134 quieto, 3135–3416 quieto; medido cuadro a cuadro,
§5). Velocidades: todo G2 a 1×; G1 entre 0,467× y 3× (límite 0,35×–3,5×).

## 3. Sincronía v2: cada cosa con su cuadro y su pulso

Pulsos de la pista restando 14,05 (SPEC §0): todos en múltiplos de 15 salvo el 284. «Imagen» es el primer cuadro en que se ve; el sonido cae un
cuadro después de su imagen (regla del kit). Medido en la vista previa (snapshot cuadro a cuadro) y, el sonido, en el render (§6).

| Qué | Imagen (cuadro) | Pulso (fuerza) | Sonido (cuadro) | Desvío |
|---|---|---|---|---|
| «Valeria» puesta, la «V» en el campo | 0 | 0 | — | 0 |
| «llegó» · «el» · «domingo.» | 15 · 30 · 45 | 15 · 30 · 45 | — | 0 |
| Toque en «Apellidos» (grab. 211) | 60 | 60 | `toque` a 61 | 0 |
| Toque en «Cómo llegó» (grab. 279) | 90 | 90 | `toque` b 91 | 0 |
| Toque en «Servicio General» (grab. 306) | 105 | 105 | — | 0 |
| El chip «Servicio General» | 108 | — | `aparicion` 109 | como v1 |
| La cámara baja; la app salta a «Registrar» | 108–119 (114) | — | `desliz` 109–120 | 0 |
| **Toque en «Registrar»; iris; frase 2** | **120** | **120 (0,93, bajo)** | `toque` c 121 (+3 dB) · `confirmacion` 123 (+3 dB) | 0 |
| Toque en «Entendido» | 150 | 150 | `toque` a 151 | 0 |
| «1 sin enviar» | 165 | 165 | `aparicion` 166 | 0 |
| **Látigo; el mundo 2** | 176–186 (180) | **180 (0,87)** | `desliz` 174–185 (+3 dB) | 0 |
| Ceja «MEMBRESÍA» | 195 | 195 | `aparicion` 196 | 0 |
| Cámara → M · C · G | 240 · 300 · 345 | 240 · 300 · 345 | — | 0 |
| Frase 3 | 360–370 | 360 | — | 0 |
| **Toque en «Marcar cumplido»; iris** | **375** | **375** | `toque` b 376 | 0 |
| Cámara → «¿Cómo fue?» | 390 | 390 | — | 0 |
| Toque en «Contestó» | 450 | 450 | `toque` c 451 | 0 |
| Cámara → «Observaciones»; toque | 480 · 495 | 480 · 495 | `toque` a 496 | 0 |
| Cámara → botones | 570 | 570 | — | 0 |
| **Toque en «Marcar cumplido» del diálogo; el resultado** | **600** · 603 | **600 (0,93)** | `toque` b 601 (+3 dB) · `confirmacion` 603 (+3 dB) | 0 |
| **Punch a «Ahora va en: Mensaje de bienvenida»** | 660–668 | **660 (0,90)** | — | 0 |
| **Toque en «Listo»** (G1 2932, fuera de encuadre); cámara → G | **720** (–733) | **720 (0,96)** | `toque` c 721 | 0 |
| El diálogo se va; la tarjeta dice «Mensaje de bienvenida» | 729 · 738 | — | — | — |
| **Toque en el nombre** (marca en G2 510·1476 = el nombre de G1); **iris a la ficha**; el halo se asienta | **780** (–785) | **780 (0,88)** | `toque` a 781 | 0 |
| La ficha limpia dentro del círculo (G2 2840) | 781 | — | — | — |
| Cámara → la fila «Avance» | 810–823 | 810 | — | 0 |
| **Toque en «Avance»** (G2 2938) · **frase 4** («Y» 840 · una 842 · ruta 844 · para 846 · crecer 848) | **840** | **840 (1,00, el más fuerte)** | `toque` b 841 (+3 dB) | 0 |
| **La tarjeta abierta, completa** (G2 2948) | **842** | — | `aparicion` 843 (+3 dB) | 0 (SPEC: 842) |
| Cámara → el paso, «Después», «Marcar cumplido» | 840–853 | 840 | — | 0 |
| Frase 4 completa | 852 | — | — | 0 |
| Cámara → «Objetivos de conexión» | 900–913 | **900 (0,84)** | — | 0 |
| Frase 4 sale | 957–961 | — | — | 0 |
| **Frase 5** (Que 960 · *ninguna* 962 · persona 964 · se 966 · pierda 968); la ceja sale 960–963; el halo; cámara → la tarjeta | **960** (–973) | **960 (0,98)** | — | 0 |
| La ventana se hace a un lado | 964–978 | — | — | 0 (SPEC: 964) |
| `subida` | — | — | 1036–1093 (golpe 1081) | 0 |
| Dip | 1077–1079 | — | — | 0 |
| **La firma** | **1080** | **1080 (0,93, empieza el clímax)** | música 0,7 → 0,224 (1092) → 0 (1110); campanas 1091 | 0 |

Ninguna acción a más de 1 cuadro de su pulso; ningún pulso del 0 al 360 vacío; del 975 al 1076 solo se mueven el halo (960–1050) y la subida (sonido).

## 4. Desvíos del SPEC v2 y su porqué

1. **El desplazamiento de la ficha lo hace la cámara, no un corte.** La grabación salta en un cuadro (3134 → 3135) y se desplaza **484 px CSS**
   (1452 px del video, medido por correlación de las dos imágenes: error medio 0,15 niveles). En vez de esconder el salto en el movimiento
   del 900, la ficha sin desplazar (`#m3pre` / `#m3abierta`) va **encima** de la misma ficha ya desplazada (`#m3post`, 1452 px más abajo), las
   dos quietas y alineadas al píxel; la de arriba se recorta 7 filas antes de su barra inferior. Así el mundo 3 es una sola página de 1328 px
   CSS y la cámara la recorre como si la app se desplazara; nunca se ve un salto. La barra inferior de la app, que estaba debajo de la fila
   «Avance», desaparece **en el 842**, el mismo cuadro en que la tarjeta se abre (todo lo de debajo de la fila cambia en ese cuadro).
2. **Sin desplazar no se ven «Después» ni «Marcar cumplido».** La nota del pedido decía que sí; medido en los cuadros 2948–3133, la barra
   inferior (fila 2307 del video, CSS 769) tapa todo lo que está debajo de «● A tiempo · Desde hoy · vence mañana». Por eso la ficha
   desplazada entra ya en el 840 (no en el 900): sin ella el plano del 853 no tendría «Después: Se conecta con una casa de paz».
3. **«M» en la ficha es ×1,15 (36 px), no ×1,4.** Los textos de la tarjeta van de x 32 a 357 px CSS (el chevrón, «Marcar cumplido»); M (279
   px de ancho) los corta y en el primer intento ×1,25 cortaba «Avance» y el chevrón. Los planos de la ficha: 810 ×1,15 (fila), 840 ×1,15
   (paso), 900 G⁺ ×1,08 (objetivos), 960 G⁺ con la ventana a 0,92 (31 px). Ninguno baja de 31 px.
4. **La cabecera (780–809) no muestra la fila «Avance».** En 4:5 el G del tope (CSS 0–439) termina en «Llegó el 30 de oct de 2026…»; la fila
   está en CSS 643–691 y la trae la cámara del 810.
5. **Las cámaras de los objetivos y del cierre** van por las líneas medidas en el cuadro 3135, no solo por las cajas: 900 → CSS desplazado
   211–617 (de «Flujo» a la tercera entrada del historial, los chips en el centro); 960 → 139–545 (de «Avance» a la primera entrada). Los
   bordes caen en huecos entre líneas.
6. **«Datos de ejemplo» tapa el arranque de una línea del historial** en los planos de 840, 900 y 960 (abajo a la izquierda, como pidió el
   dueño). Nada clave queda debajo: el paso, «Después», los objetivos y sus chips quedan libres.
7. **Las marcas de toque del 780 y del 840 van en una capa del mundo 3, encima del iris** (el SPEC ponía la del 780 en el mundo 2): así el
   círculo del iris nace debajo del dedo y no lo tapa.
8. **`v29` (la ficha desplazada) arranca en el 840**, dos cuadros antes de la apertura: el movimiento de cámara del 840 pasa 1–2 px CSS por debajo
   del borde de la ficha sin desplazar en su primer cuadro; con `v29` debajo se ve la app y no el fondo de la ventana.
9. **La frase 5 va en la pista 7** (la 5 la ocupa la frase 4 hasta el 961 y se pisan dos cuadros en el blur swap).

Se mantienen los de la v1: el extractor atrasa ~2 cuadros los tramos a menos de 1× (corregido en `v01`, `v02`), el látigo en una tira, la
espera de la app cortada en vez de mostrada, las entradas de texto un cuadro antes del pulso, los niveles del kit con +3 dB en los toques clave,
«Datos de ejemplo» a 31 px y la firma de 2,5 s.

## 5. Lo que se revisó y lo que se midió

- `npx hyperframes check --json`: **0 errores**, 3 avisos que se dejan a propósito: `composition_file_too_large` (la raíz lleva los 29 tramos
  de video para que se vean y se recorten en la línea de tiempo) y `line_unread` ×2 («Kingdom» 1,67 s y «Prueba gratis 30 días» 1,5 s: es la
  firma aprobada del kit, igual en toda la serie).
- **G2 cuadro a cuadro** (diferencia entre cuadros sobre los 2836–3416): cambia solo en 2840 (se va «Actualizando…»), 2945 (la tarjeta se
  abre; el chevrón termina de girar en el 2948) y 3135 (el desplazamiento). Lo demás, quieto: los cortes de `v26`–`v29` no se ven.
- Hojas (todas en `.hyperframes/artifacts/snapshots/`):
  - `cb3eebf4-…/contact-sheet-{1,2,3}.jpg`: 720, 733, 738, 779, 780, 782, 785, 786, 809, 823, 839–842, 846, 853, 899, 913, 959, 960, 972, 978,
    1076, 1078, 1080 (primera pasada; mostró el corte de «Avance» a ×1,25 y una raya en la costura de las dos fichas, corregidos);
  - `0216f88c-…/contact-sheet.jpg`: 823, 839, 846, 853, 899, 959 después de las correcciones;
  - `2575d4b8-…/contact-sheet-{1,2}.jpg`: la apertura de «Avance» cuadro a cuadro (27,9–28,5 s, 18 cuadros);
  - `--review` (versión final): `77013e14-…/review-beats-{1,2,3,4}.jpg`, `review-seam-01…37.jpg` (la costura G1 → G2 es la 30, en el 26,0;
    la apertura de «Avance», la 33) y `review-phone-{1,2,3,4}.jpg` (los planos nuevos están en la 3: a 360 px se leen «Avance», el paso,
    «Después» y los tres objetivos).
- Mirado: la cámara quieta en 779 → 780; el círculo nace en el nombre «Valeria Cardona Ríos» y la ficha llega limpia; la fila «Avance» a 36 px
  en el 823; el toque en el 840 con el golpe y la tarjeta abierta entera en el 842 (en el 841 todavía plegada); en el 853 «Flujo: Llegó a un
  culto», «Mensaje de bienvenida», «● A tiempo · Desde hoy · vence mañana», «Después: Se conecta con una casa de paz» y «Marcar cumplido»; en
  el 913 «Objetivos de conexión» con «Casa de paz · ¿cuál?», «Servir» y «Clases de la visión» enteros en el centro; la frase 4 sobre la tarjeta;
  el blur swap 957–961; *ninguna* dorada; la ventana a 0,92 en el 978; el dip; el primer cuadro de la firma.

## 6. La mezcla y el render

**`renders/clip-sitio-membresia-4x5.mp4`** (reemplaza al v1): `render --quality high`, 8,3 MB, H.264 1080×1350 a 30 fps, **1155 cuadros,
38,500 s** (ffprobe), audio AAC 48 kHz estéreo. El primer intento falló al ensamblar («ffprobe deadline», un tiempo de espera de la máquina
cargada); el segundo salió limpio sin cambiar nada.

**La mezcla (medida, no oída):** integrada **−17,5 LUFS** (ffmpeg ebur128 y `hyperframes audio` coinciden), pico real **−1,4 dBTP**, pico de
muestra −1,6 dBFS, **0 recortes**, LRA 2,0 LU, máximo de corto plazo −16,4 LUFS. Queda dentro de «−17/−16» y bajo −1 dBTP, así que **no se
normalizó**: subir a −16 llevaría el pico real a ≈ +0,1 dBTP y obligaría a limitar (como anotó la v1).
`hyperframes audio` detecta los golpes en **2,03 · 3,03 · 4,03 · 5,03 · 12,53 · 15,03 · 16,53 · 20,03 · 24,03 · 26,03 · 28,03 s** = cuadros 61 ·
91 · 121 · 151 · 376 · 451 · 496 · 601 · 721 · **781 · 841**: cada `toque` un cuadro después de su imagen, también los dos nuevos. Sonoridad
momentánea: −14,9 en 28,0 y −13,8 en 28,2 (el golpe más fuerte + toque + aparición), −15,4 en 28,4; −16,1 en 35,8 y −14,6 en 36,0 (la subida y el
clímax); **−19,5 en 36,4** (la música ya a −10 dB, entran las campanas del 36,38), −17,1 en 37,0 (las campanas solas, la música en 0), −24 en 38,0 y
−35,9 en 38,4 (la cola). Las campanas quedan limpias: no hizo falta adelantar la caída al 1088 (SPEC §5).
Nadie oyó el sonido ni vio el render a velocidad real.

## 7. El plano más débil y qué cambiaría con más tiempo

- **900 → 960:** los dos planos finales se parecen (G⁺, uno centrado en los objetivos, el otro corrido 50 px CSS hacia arriba); el cambio
  real del 960 es la ventana que se encoge. Con una grabación nueva se podría plegar el historial o grabar en un viewport más alto para que la
  tarjeta entera quepa en G⁺.
- **780–809:** la cabecera de la ficha a G no muestra todavía «Avance»; son 1 s de ficha general antes del acercamiento.
- Heredado de la v1: el punch del 660 corta «Reporte del paso» por la izquierda y «Listo» no se ve tocarse; el tramo 105–120 va apretado.

## 8. Para 9:16

Como en la v1: cambiar las variables `--f-*` (1080×1920; márgenes 60; ceja 188 / 34 px; frase 236 / 960 / 104 px; ventana 60·480·960×850 con
`--f-ventana-hvis: 850px`, `--f-k: 0.820513`, `--f-grab-alto: 2077.54px`, `--f-latigo: 1000px`) y `window.KD` (ventana 960×850, `latigo` 1000,
`cambio` 0,92 con origen «50% 0%» y x +36), la firma por `cierre-corto`, y `data-width/height` de los hosts y de las escenas. El mundo 3
(`#m3in`, `#m3post` a 1452 px del video, el recorte en la fila 2300) va en px del video × `--f-k`, así que se ajusta solo; las cámaras del mundo 3
se recalculan con `enc`/`enc3`, pero con 345 px CSS de alto en G conviene revisar los encuadres del 810 (la fila) y del 960.
