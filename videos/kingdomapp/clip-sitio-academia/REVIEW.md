# REVIEW · Clip del sitio: Academia — «La clase ya empezó» (4:5)

2026-10-30 · Construcción en HyperFrames 0.8.221 a partir de [SPEC.md](SPEC.md) con la grabación real `assets/grabaciones/grabacion.mp4`
(1170×2532, 30 fps, 95,07 s, sin círculo; tres cuentas de Kingdom Demo) y `pasos.json`. Plantilla: `../clip-sitio-membresia`. **Render de
entrega hecho**: `renders/clip-sitio-academia-4x5.mp4` (1080×1350, 30 fps, 915 cuadros, 30,5 s, H.264 + AAC 48 kHz estéreo, 7,9 MB).

## 1. Qué hay

| Archivo | Qué es |
|---|---|
| `index.html` | La raíz: el formato en un solo lugar (`--f-*` y `window.KD`), los hosts de las escenas, **la ventana** con la tira de dos ranuras, los 22 tramos de video, las tres cámaras, los dos iris, las marcas de toque, el cambio de ventana, el dip, la música y los 22 sonidos |
| `compositions/fondo.html` | La noche del sitio; el halo se asienta en 0, 120, 240, 360 y 720 |
| `compositions/frase-1.html` … `frase-4.html`, `ceja.html` | Las cuatro frases y la ceja «ACADEMIA», con sus entradas y salidas |
| `identidad/cierre-clip.html` | La firma del kit v1.1 (840–914), `{"llamado":"prueba","fondo":"azul","idioma":"es"}`; campanas en 28,38 |
| `assets/audio/toque-b.wav`, `toque-c.wav` | Las tomas b y c de `toque` (±3 % de tono), copiadas de Membresía |

Vista previa: `npm run dev` en `clip-sitio-academia/` (o el HyperFrames desktop app). Hojas: §5.

## 2. Los planos, con sus cuadros

Cuadros de la grabación = «grab.». Todos los tramos van **a 1×** (ningún tramo por debajo de 1×, así que el desfase de ~2 cuadros del
extractor no aplica: medido en el render, cada cambio cae en su cuadro). Cada corte cae en una pausa o una espera de la app.

| Plano | Cuadros | Grabación y cámara |
|---|---|---|
| P1 El código en pantalla | 0–119 | grab. 0–119 a 1×: «3 5 9 8», la barra, el QR; el temporizador real cambia 4 veces (14:26 → 14:22). Cámara G sobre CSS 60–499; **60–73 → G sobre 405–844** («13 de 18 marcaron», «Faltan (5)») |
| Látigo arriba | 110–120 | La tira sube 1100 px (`power3.inOut`); la alumna aterriza 1,04 → 1,00 (120–130) |
| P2 Cuatro números | 100–179 | grab. 444–463 (casillas vacías); **corte en cada pausa entre teclas**: 464 («3», en el 120), 508 («5», 135), 552 («9», 150), 600 («8» + «Enviando…», 165). Cámara ×1,2 sobre las casillas |
| P3 ¡Listo! | 180–245 | corte en la espera (615 → 626): «¡Listo! Quedó tu asistencia» en el 180, el chequeo se dibuja 180–192 (grab. 626–690). Cámara 180–193 → ×1,2 sobre el chequeo y la frase |
| Látigo abajo | 230–240 | La tira baja 1100 px; el profesor (T3, ya montado y encuadrado desde el 200, fuera de cuadro) aterriza 240–250 |
| P4 El profesor lo ve | 200–365 | grab. 861–930 («14 de 18»); 931–933 (toque «Presente» de Andrea, 270); corte 934 → 952 («15 de 18» en el 273); 952–978; 1026–1028 (toque «Presente» de Camilo, 300); corte 1029 → 1036 («16 de 18» en el 303); 1036–1097. Cámara G⁺ (CSS 180–586); **330–343 → M alineado a la izquierda** (CSS 8–286 × 271–585) sobre «16 de 18 marcaron» y «Se cierra sola en 13:50» |
| Látigo arriba | 350–360 | La tira sube a la ranura 2, que desde el 340 tiene el mundo de quien coordina; aterriza 360–370 |
| P5 Por aprobar | 340–389 | grab. 1703–1743: Cursos con «Por aprobar 9 · 9 graduaciones en 1 lista» **sin desplazar**. Cámara G⁺ sobre la tarjeta. **375: toque e iris** desde la lista (CSS 195·300); dentro, corte en la carga (1822 → 1836): el grupo «Fundamentos bíblicos» |
| P6 Quien cumple, se gradúa | 375–599 | 1836–1850; **390: la app salta a la lista** (grab. 1905: «Se gradúan 9 · 9 no se gradúan», Andrea «Cumple los criterios») y la cámara la recibe (390–403 → ×1,1); **420: salta otra vez** (grab. 1969: Carolina «No cumple: promedio de 2,57 (pide 3)», Dayana «Cumple»), cámara quieta; 465–478 → G sobre la barra «Devolver al profesor \| Aprobar (9)»; **480 toque** (grab. 2036–2039); corte 2040 → 2044: «¿Aprobar la graduación?» entra 484–488 y se queda (2044–2159); 495–508 → ×1,15 sobre el diálogo entero |
| P7 Nueve graduados | 600–659 | **600 toque** en «Aprobar (9)» (grab. 2185–2187); corte en la espera (2188 → 2206: el diálogo se va y la K del cargador): «Graduado» y el aviso **«¡Listo! 9 graduados, con su certificado.»** en el 603; 600–613 → G⁺ con el aviso a la vista; **615: la app salta a los certificados** (grab. 2305: Andrea Perea López · 7YU79-NNB7A · Ver · Descargar · Anular, con el aviso aún abajo), cámara quieta; 645–658 → ×1,12 sobre la primera fila |
| P8 El certificado | 660–839 | **660 toque en «Ver»**, iris; dentro, corte en la carga (2504 → 2516): «Tu certificado» de Andrea Perea López, quieto (2516–2695). Cámara 660–669 → G sobre la tarjeta (con el iris); **punch 675–683 → ×1,35** sobre «otorga… · Andrea Perea López · por haber terminado…»; 720–733 → ×1,04 sobre «por haber terminado…» hasta «Copiar el enlace para verificarlo»; la ventana a 0,92 y +48 (724–738); dip 837–839 |
| La firma | 840–914 | `cierre-clip`; campanas en el 851 |

## 3. Sincronía: cada cosa con su cuadro y su pulso

«Imagen» es el primer cuadro en que se ve (comprobado en el render, `.hyperframes/artifacts/render-check/`). El sonido cae un cuadro
después de su imagen (`data-start = (imagen + 1) / 30 − acento`).

| Qué | Imagen (cuadro) | Pulso | Sonido (cuadro) | Desvío |
|---|---|---|---|---|
| «La» puesta, el código «3 5 9 8» | 0 | 0 | — | 0 |
| «clase» · «ya» · «empezó.» | 15 · 30 · 45 | 15 · 30 · 45 | — | 0 |
| Cámara → «13 de 18 marcaron» | 60–73 | 60 | — | 0 |
| Frase 1 sale | 117–121 | — | — | 0 |
| **Látigo arriba; la alumna llega** | 110–120 | **120 (bajo)** | `desliz` acento 121 (1,4) | 0 |
| **«3»** en su casilla (grab. 464); frase 2 entera en el 126 | **120** / 120–126 | **120** | `aparicion` 121 | 0 |
| «5» (grab. 508) | 135 | 135 | `aparicion` 136 | 0 |
| «9» (grab. 552) | 150 | 150 | `aparicion` 151 | 0 |
| «8» y «Enviando…» (grab. 600) | 165 | 165 | `aparicion` 166 | 0 |
| **«¡Listo! Quedó tu asistencia»** (grab. 626) | **180** | **180 (pico)** | `confirmacion` acento 181 (1,4) | 0 |
| Ceja «ACADEMIA» | 195 | 195 | `aparicion` 196 | 0 |
| **Látigo abajo; «14 de 18 marcaron»** | 230–240 | **240** | `desliz` acento 241 | 0 |
| Toque «Presente» (grab. 931) | 270 | 270 | `toque` a 271 | 0 |
| «15 de 18» (grab. 952) | 273 | — | `aparicion` 274 | 0 (SPEC: 273) |
| Toque «Presente» (grab. 1026) | 300 | 300 | `toque` b 301 | 0 |
| «16 de 18» (grab. 1036) | 303 | — | `aparicion` 304 | 0 (SPEC: 303) |
| Cámara → «16 de 18» de cerca | 330–343 | 330 | — | 0 |
| Frase 2 sale | 357–361 | — | — | 0 |
| **Látigo arriba; «Por aprobar 9»** | 350–360 | **360** | `desliz` acento 361 | 0 |
| «Quien» · «cumple,» · «se» · «gradúa.» | 360 · 362 · 364 · 366 | 360 | — | 0 |
| **Toque en la lista; iris** | **375** | **375** | `toque` c 376 | 0 |
| La app salta a «Se gradúan 9 · 9 no se gradúan»; cámara 390–403 | 390 | 390 | — | 0 |
| La app salta a «No cumple» | 420 | 420 | `desliz` acento 421 | 0 |
| Cámara → la barra | 465–478 | 465 | — | 0 |
| **Toque «Aprobar (9)»** (grab. 2036) | **480** | **480** | `toque` a 481 | 0 |
| «¿Aprobar la graduación?» entra | 484–488 | — | — | +1 (SPEC: 483–488) |
| Cámara → el diálogo | 495–508 | 495 | — | 0 |
| Frase 3 sale | 597–601 | — | — | 0 |
| **Toque «Aprobar (9)» del diálogo** (grab. 2185) | **600** | **600 (2.ª subida)** | `toque` b 601 (1,4) | 0 |
| **«¡Listo! 9 graduados, con su certificado.»** (grab. 2206) | 603 | — | `confirmacion` acento 604 (1,4) | 0 |
| La app salta a los certificados | 615 | 615 | `desliz` acento 616 | 0 |
| Cámara → la fila de Andrea con «Ver» | 645–658 | 645 | — | 0 |
| **Toque «Ver»; iris al certificado** (grab. 2504 → 2516) | **660** | **660 (golpe)** | `toque` c 661 (1,4) | 0 |
| Punch al nombre | 675–683 | 675 | — | 0 |
| **Frase 4** palabra a palabra; la ceja sale | 720 … 734 / 720–723 | **720 (golpe)** | — | 0 |
| Cámara → el código; la ventana a un lado | 720–733 / 724–738 | 720 | — | 0 |
| `subida` | — | — | 796–853 (golpe 841) | 0 |
| Dip | 837–839 | — | — | 0 |
| **La firma** | **840** | **840** | música 0,7 → 0,224 (852) → 0 (870); campanas 851 | 0 |

Ninguna acción cae a más de 1 cuadro de su pulso (la única a +1 es la entrada del diálogo, que no tiene pulso propio). `hyperframes audio`
sobre el render detecta los golpes en **9,03 · 10,03 · 12,53 · 16,03 · 20,03 · 22,03 s** = cuadros 271 · 301 · 376 · 481 · 601 · 661: cada
`toque` un cuadro después de su imagen. Las `aparicion`, `desliz` y `confirmacion` son suaves y no salen como golpes; su posición es la
calculada.

## 4. Desvíos del SPEC y su porqué

1. **El código es 3 · 5 · 9 · 8** en el profesor y en la alumna (comprobado cuadro a cuadro: T1 grab. 0 y T2 grab. 464–600).
2. **Ningún tramo se acelera ni se frena.** En vez de 1,6–2× entre teclas, las pausas se cortan: entre una tecla y la siguiente la pantalla
   está quieta (sin cursor que parpadee), así que cada número entra en su pulso con un corte invisible y el tramo va a 1×. Igual con las
   esperas: «Enviando…» (615 → 626), los «Presente» (934 → 952 y 1029 → 1036), la carga del grupo (1822 → 1836), el diálogo (2040 → 2044),
   la K del cargador tras aprobar (2188 → 2206) y la carga del certificado (2504 → 2516).
3. **La tira tiene dos ranuras, no tres.** El mundo de quien coordina va en la ranura de la alumna desde el 340 (la válvula de SPEC §2.0):
   los tres látigos son de una ranura y alternan arriba / abajo / arriba (BANNED 23). **Cada mundo tiene su propia cámara** (`#cam1`, `#cam2`,
   `#cam3`) y su ranura recorta, así que un encuadre nunca se asoma al otro mundo en el látigo.
4. **«Por aprobar» va sin desplazar.** La grabación toca la lista con la página desplazada (1745 → 1822), donde el encabezado «Por aprobar 9»
   queda bajo la barra. El clip usa la página sin desplazar (1703–1743), dibuja el toque sobre la lista en su lugar (CSS 195·300) y corta
   a la página del grupo dentro del iris.
5. **Los «desplazamientos» de la app son saltos.** `ver` en la grabación salta en un cuadro (1904 → 1905, 1968 → 1969, 2304 → 2305): no hay
   900 ms de desplazamiento suave. El 390 (a la lista) cae con el movimiento de cámara; el 420 («No cumple») y el 615 (los certificados) caen
   con la cámara quieta y su `desliz`, como pedía BANNED 24.
6. **No se ve «Certificados (9)» ni «Descargar todos (para imprimir)».** En la grabación el `ver` deja ese encabezado bajo la barra de la
   app (solo asoma el borde del botón). Lo que se ve es la lista de certificados con nombre, código, «Ver · Descargar · Anular» y el aviso.
7. **El aviso se encuadra con un margen abajo.** «¡Listo! 9 graduados, con su certificado.» es lo último de la pantalla (CSS 790–835) y,
   con la grabación pegada al borde, quedaba debajo de «Datos de ejemplo». Del 600 al 645 la cámara deja 34 px CSS del fondo de la app debajo
   de la grabación (la píldora queda sobre ese margen y el aviso entero encima).
8. **Escalas por contenido, no por nivel.** M (×1,4) muestra 279 px CSS de ancho y cortaba los textos a 390 px: las casillas y «¡Listo!»
   van a ×1,2 (38 px el texto de 14 px), la lista a ×1,1, el diálogo a ×1,15, los certificados a ×1,12, el nombre del certificado a ×1,35
   (43 px; el nombre mide 269 px CSS) y el código final a ×1,04 (×0,92 de la ventana = 30 px el cuerpo, ≈ 39 px el código monoespaciado).
   «16 de 18 marcaron» va a ×1,4 **alineado a la izquierda** (centrado cortaba el «1»).
9. **El 660 tiene un movimiento de 10 cuadros con el iris** (de la lista a la tarjeta del certificado) antes del punch del 675: es lo que
   permite que en el 665–674 se vea el certificado entero (SPEC: «G sobre la tarjeta») y que el punch sea un acercamiento corto.
10. **El certificado final no necesita desplazamiento:** «Tu certificado» cabe entero en la pantalla de 844 px (tarjeta, «Descargar
    certificado», «Código de verificación 7YU79-NNB7A» y «Copiar el enlace para verificarlo», este último medio tapado por la barra de la
    app, que es real). La cámara hace el recorrido del 720.
11. **Las marcas de toque del 270, 300 y 600 se apagan en 3 cuadros** (la onda llega a ×1,3): en el cuadro siguiente al corte la fila o el
    diálogo ya no están, y una onda de 450 ms quedaba sobre otro botón. Las del 375 y 660 duran lo normal (se abren con el iris).
12. **Sin stills para los iris:** debajo de cada iris sigue el mismo video quieto (v13 hasta el 381, v21 hasta el 666), que es el cuadro
    anterior al toque. No hacen falta PNG.
13. **Niveles del sonido** como Membresía: kit a `data-volume="1"`, 1,4 en los cinco clave (desliz 120, confirmacion 181 y 604, toque 601 y
    661); la música sin `data-volume`, 0,7 en su carril. Las cuatro `aparicion` del 120–165 quedan a 1 (no se oyó si suenan a máquina; la
    válvula del SPEC es bajar las del 136 y el 151 a 0,7).
14. **La firma dura 2,5 s** (pieza del kit): `check` avisa `line_unread` en «Kingdom» y «Prueba gratis 30 días», igual que en Membresía.

## 5. Lo que se revisó y lo que se midió

- `npx hyperframes check --json`: **0 errores**, 3 avisos: `composition_file_too_large` (la raíz lleva los 22 tramos a propósito, para que se
  vean y se puedan recortar en la línea de tiempo) y `line_unread` ×2 (§4.14).
- `npx hyperframes snapshot --review`: `.hyperframes/artifacts/snapshots/f4845229-c5e0-4405-b5fb-27a219d3c5db/review-beats-{1,2,3}.jpg`,
  `review-seam-01…32.jpg`, `review-phone-{1,2,3}.jpg` (hecha antes de las dos últimas correcciones: §4.7 y §4.11). Las correcciones se
  miraron en `.hyperframes/artifacts/snapshots/952662f3-def0-43a1-a5a1-e9a788331ded/contact-sheet.jpg` y los bordes de cada corte en
  `.hyperframes/artifacts/snapshots/6b867c38-24a8-4b16-80a5-1eaf22d750ca/contact-sheet-{1,2,3}.jpg`.
- **El render, cuadro a cuadro** (60 cuadros extraídos con ffmpeg): `.hyperframes/artifacts/render-check/render-cuadros-{1,2}.jpg`. Cada
  número de la alumna entra exactamente en el 120, 135, 150 y 165; «¡Listo!» en el 180; «15» y «16» en el 273 y 303; el grupo en el 389, la
  lista en el 390, «No cumple» en el 420, el diálogo desde el 484, el aviso en el 603, los certificados en el 615, el certificado en el 661;
  la frase 4 completa en el 738; el dip 837–839 y la firma en el 840.
- `ffprobe`: h264 1080×1350, 30/1, **915 cuadros**, AAC 48 kHz estéreo, **30,500 s**, 7 915 343 bytes.
- **La mezcla (medida, no oída):** integrada **−17,6 LUFS** (ffmpeg ebur128 y `hyperframes audio` coinciden), pico real **−1,1 dBTP**, pico de
  muestra −1,2 dBFS, **0 recortes**, LRA 2,2 LU, corto plazo máximo −16,3 LUFS. Los dos picos son los toques clave del 601 (−1,1) y del 661
  (−1,3); el resto queda bajo −3,9 dBTP. Es la misma mezcla que Membresía publicada (−17,5 / −1,4), así que **no se normalizó**: subirla a
  −16 pasaría el pico de −1 dBTP salvo que se bajen esos dos toques a 1,0.
- Nadie oyó el sonido ni vio el movimiento a velocidad real fuera del render.

## 6. El plano más débil y qué cambiaría con más tiempo

- **375–420**: el grupo «Fundamentos bíblicos» se ve medio segundo (375–389, la mitad dentro del iris) antes de que la app salte a la lista;
  el que no conoce la app puede no leer que es «el grupo». Con una regrabación: que el `ver` a `[data-lista]` sea suave (o grabar sin ese
  paso y dejar que la cámara baje por la página del grupo).
- **615–659**: la lista de certificados sin su encabezado «Certificados (9)». Se arregla en la escena con `bloque: 'center'` en el `ver` de
  `#ac-grad-certificados`.
- **El salto del 390 con la cámara en movimiento** puede leerse como un corte. Si molesta: cámara quieta en el 390 y el movimiento al 405.
- Las tres esperas recortadas del profesor (934 → 952, 1029 → 1036) hacen que la fila desaparezca y el contador suba en el mismo cuadro: es
  lo que pide el pulso, pero la app real tarda medio segundo.

## 7. Para 9:16

Igual que Membresía (su REVIEW §8): cambiar en `index.html` las variables `--f-*` (1080×1920; márgenes 60; ceja 188 / 34 px; frase 236 / 960 /
104 px; ventana 60·480·960×850 con `--f-ventana-hvis: 850px`, `--f-k: 0.820513`, `--f-grab-alto: 2077.54px`, `--f-latigo: 1000px`) y
`window.KD` (ventana 960×850, `latigo` 1000, `cambio` con origen «50% 0%» y x +36), la firma por `cierre-corto`, `data-width/height` de los
hosts y de las escenas, y la frase 4 en tres líneas («Forma a los *líderes* / que tu visión / necesita»). Los encuadres se recalculan solos
con `enc()`, pero los que dependen del ancho (§4.8) hay que mirarlos: en 9:16 la ventana muestra 345 px CSS de alto en G.
