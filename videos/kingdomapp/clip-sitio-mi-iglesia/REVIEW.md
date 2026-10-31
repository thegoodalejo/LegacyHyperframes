# REVIEW · Clip del sitio: Mi iglesia — «Se enteró toda la iglesia» (4:5)

2026-10-30 · Construcción en HyperFrames 0.8.221 a partir de [SPEC.md](SPEC.md) con la grabación real `assets/grabaciones/grabacion.mp4`
(1170×2532, 30 fps, 52,2 s, sin círculo de toque; cuenta 105, Gabriela Hinestroza Perea) y `pasos.json`. Plantilla: [Eventos](../clip-sitio-eventos/REVIEW.md).
El dueño ya no revisa: construido, verificado y renderizado sin paradas. **Entrega:** `renders/clip-sitio-mi-iglesia-4x5.mp4`.

## 1. Qué hay

| Archivo | Qué es |
|---|---|
| `index.html` | La raíz: el formato en un solo lugar (`--f-*` y `window.KD`), los hosts de las escenas, **la ventana a la app** (un solo mundo), los 32 tramos de video, los tres stills, las 14 marcas de toque, la cámara (con las tres compensaciones de salto), el iris, el cambio de ventana, el dip, la música y los 24 sonidos |
| `_gen/` | El generador: `gen.py` (las tablas de tramos, stills, marcas y sonidos), `index.tpl.html` (la plantilla con la cámara en su `<script>`) y las ayudas de revisión; cómo regenerar en `_gen/README.md` |
| `compositions/fondo.html` | La noche del sitio; el halo se asienta en 0, 180 y 720 |
| `compositions/frase-1.html` … `frase-4.html`, `ceja.html` | Las cuatro frases y la ceja «MI IGLESIA», con sus entradas y salidas |
| `identidad/cierre-clip.html` | La firma del kit v1.1 (840–914), `{"llamado":"prueba","fondo":"azul","idioma":"es"}`, campanas en 28,38 |
| `assets/stills/still-354.png` | El cuadro 179 (la tarjeta con «Inscribirme») debajo del iris del 180, en su propia capa con el encuadre de la tarjeta |
| `assets/stills/still-705.png` | La lista «¿A quiénes inscribes?» ya centrada (la app quieta 705–709), sostenida 389–419 |
| `assets/stills/still-1258.png` | El resultado ya desplazado con «Ver boleta» a la vista (un solo cuadro quieto antes del toque), sostenido 645–659 |
| `assets/audio/toque-b.wav`, `toque-c.wav` | Las tomas b y c de `toque` (±3 % de tono), copiadas de Eventos |

Para el 9:16: §8.

## 2. Los planos, con sus cuadros

«grab.» = cuadro de `grabacion.mp4`. **Todos los tramos van a 1×**: en vez de acelerar, se cortan las esperas y las pausas (la pantalla está
quieta, así que el corte no se ve).

| Plano | Cuadros | Grabación y cámara |
|---|---|---|
| P1 ¿Se enteró toda la iglesia? | 0–119 | grab. 0–59 (Mi iglesia arriba: «Buenas tardes, Gabriela», «Mis servicios», «Mis Equipos 3», la destacada); **60: la app baja a la novedad en un cuadro** (grab. 96, salto real del `ver`) y queda quieta (grab. 96–140); 105 toque en la flecha (grab. 180), corte en la espera quieta 182→186: el selector abierto en el 107. Cámara: G `inicio` (CSS 0–439) quieta hasta el 89 · 90–103 → ×1,08 `reacciones` (CSS 297–703: la novedad, la tarjeta, el selector y la barra con el total) |
| P2 Llega a cada celular | 120–179 | 120 toque en «Amén» (grab. 245); corte en la espera quieta 247→251: «🙌 Amén» y **57** en el 122; el 🙌 salta 125–134 (grab. 254–263); quieta hasta el 179. Cámara: 150–163 → M `tarjeta` (CSS 10–289 × 383–696, «Inscribirme» al centro); la marca espera sobre «Inscribirme» desde el 165 |
| P3 El congreso | 180–359 | **Iris** 180–185 desde «Inscribirme» con el still de la grab. 354 debajo (en su propia capa, con el encuadre de la tarjeta); dentro, el evento **ya cargado** (grab. 437–455 y 447–546; **la K del cargador, grab. 371–430, queda fuera**) y ya encuadrado en G `evento` (CSS 10–449). **300: la app baja a «Inscripción» en un cuadro** (grab. 547, salto real de 62 px CSS), grab. 557–630. Cámara: 240–253 → ×1,12 `datos` (CSS 232–624) · 330–343 → ×1,12 `inscripcion` (CSS 376–768) |
| P4 Y se inscribe con su familia | 360–599 | 375 «Inscribirme» (grab. 631); corte en la onda 633→638: «¿A quiénes inscribes? (hasta 4)» entra 377–386; **389: la app saltó 200 px (grab. 701–704), compensado** (still de la grab. 705) y 390–403 la cámara baja a la lista; 420 la casilla de Simón (grab. 710); 450 «Seguir» (grab. 754), corte en la onda 756→761: «1 de 2: Tú» entra 452–461; **464: la app saltó 136 px (grab. 814), compensado**; 480 «M» · 495 «Sí» · 510 «Seguir» → «2 de 2: Simón Ríos Arango» en el 512 · 540 «L» · 555 «No» (cada radio se llena desde el cuadro siguiente: los cuadros quietos entre el toque y el efecto se saltan). Cámara: 390–403 → ×1,18 `quienes` (CSS 28–358 × 396–768) · 465–478 → G `form` (CSS 321–760) · 570–583 → ×1,18 `botonesForm` (CSS 396–768) |
| P5 ¡Quedaste inscrito! y la boleta | 600–719 | 600 «Inscribir» (grab. 1090); **corte en la espera y la K del cargador** (1092→1111): el sello, «¡Quedaste inscrito!», las dos filas «Inscrito» y **el confeti real** en el 602 (grab. 1111–1153, a 1×); **645: la app saltó 84 px (grab. 1257), compensado** (still de la grab. 1258) y 646–658 la cámara baja a «Ver boleta»; 660 «Ver boleta» (grab. 1259); **corte en la carga de «Mis boletas»** (1261→1281): la boleta con su QR en el 662, entra 1,03 → 1,00 (662–672). Cámara: 600–613 → G `resultado` (CSS 328–767) · 646–658 → G `verBoleta` (CSS 326–765) · 662 G `boleta` (CSS 135–574, en el corte) · 690–698 punch → ×1,3 `qr` (CSS 288–624) |
| P6 Tu iglesia, en el bolsillo de cada miembro | 720–839 | 720 toque en el QR (grab. 1398); corte en la espera quieta 1400→1405: la boleta a pantalla completa entra con su animación 722–728 (grab. 1405–1522: el QR, «Gabriela Hinestroza Perea», «FM75UZ»). Cámara 720–733 → G `grande` (CSS 181–620); la ventana a 0,92 y +48 px en 724–738; dip 837–839 |
| P7 La firma | 840–914 | `cierre-clip` (fondo azul, llamado «prueba»); campanas en el 851 |

## 3. Sincronía: cada cosa con su cuadro y su pulso

«Imagen» es el primer cuadro en que se ve, **comprobado en el render** (cuadros extraídos con ffmpeg: `.hyperframes/artifacts/render-check/
render-cuadros-{1..5}.jpg`). El sonido cae un cuadro después; `hyperframes audio` detectó los 14 `toque` en 3,53 · 4,03 · 6,03 · 12,53 ·
14,03 · 15,03 · 16,03 · 16,53 · 17,03 · 18,03 · 18,53 · 20,03 · 22,03 · 24,03 s = cuadros 106 · 121 · 181 · 376 · 421 · 451 · 481 · 496 ·
511 · 541 · 556 · 601 · 661 · 721.

| Qué | Imagen | Pulso | Sonido | Desvío |
|---|---|---|---|---|
| «¿Se» puesta (la miniatura) | 0 | 0 | — | 0 |
| «enteró» · «toda la» · «iglesia?» | 15 · 30 · 45 | 15 · 30 · 45 | — | 0 |
| **La app baja a la novedad** (grab. 96) | 60 | 60 | `desliz`, acento 61 | 0 |
| Cámara → `reacciones` | 90–103 | 90 | — | 0 |
| **Toque en la flecha** (grab. 5,99 s) | 105 | 105 | `toque` a 106 | 0 |
| El selector abierto con las cuatro reacciones | 107 | — | `aparicion` 108 | 0 (SPEC 107) |
| Frase 1 sale | 117–121 | — | — | 0 |
| **Toque en «Amén»** (grab. 8,15 s) | 120 | **120 (bajo)** | `toque` c 121 | 0 |
| Frase 2 entera | 120–126 | 120 | — | 0 |
| «🙌 Amén» puesto, el total 56 → 57 | 122 | — | `aparicion` 123 (1,4) | 0 |
| El 🙌 salta | 125–134 | 135 | — | 0 |
| Cámara → `tarjeta` | 150–163 | 150 | — | 0 |
| La marca se posa en «Inscribirme» y espera | 165 | 165 | — | 0 |
| Frase 2 sale | 177–181 | — | — | 0 |
| **Toque en «Inscribirme»** (grab. 11,84 s); iris | 180 / 180–185 | **180 (pico)** | `toque` b 181 | 0 |
| El evento ya cargado, en G | 181 | — | — | +1 (dentro del iris, como el SPEC) |
| Ceja «MI IGLESIA» | 195 | 195 | `aparicion` 196 | 0 |
| Cámara → `datos` | 240–253 | 240 | — | 0 |
| **La app baja a «Inscripción»** (grab. 547) | 300 | 300 | `desliz`, acento 301 | 0 |
| Cámara → `inscripcion` | 330–343 | 330 | — | 0 |
| Frase 3, palabra a palabra | 360 · 362 · 364 · 366 · 368 · 370 | 360 | — | 0 |
| **Toque en «Inscribirme»** (grab. 21,02 s) | 375 | 375 | `toque` a 376 | 0 |
| «¿A quiénes inscribes? (hasta 4)» con «Yo» | 377–386 | — | — | +2 (la lista se desliza, real) |
| Salto de la app (grab. 701–704) compensado · cámara → `quienes` | 389 · 390–403 | 390 | — | invisible |
| **Toque en la casilla del esposo** (grab. 23,44 s) · se marca | 420 · 420–422 | 420 | `toque` b 421 | 0 |
| **Toque en «Seguir»** (grab. 25,14 s) | 450 | 450 | `toque` c 451 | 0 |
| «1 de 2: Tú» entra | 452–461 | — | — | +2 (fundido real) |
| Salto de la app (grab. 814) compensado · cámara → `form` | 464 · 465–478 | 465 | — | invisible |
| «M» (grab. 28,99 s) · el radio se llena | 480 · 481 | 480 | `toque` a 481 | 0 |
| «Sí» (grab. 30,07 s) · el radio | 495 · 496 | 495 | `toque` b 496 | 0 |
| «Seguir» (grab. 31,48 s) · «2 de 2: Simón Ríos Arango» | 510 · 512 | 510 | `toque` c 511 | 0 |
| «L» (grab. 33,30 s) · el radio | 540 · 541 | 540 | `toque` a 541 | 0 |
| «No» (grab. 34,39 s) · el radio | 555 · 556 | 555 | `toque` b 556 | 0 |
| Cámara → `botonesForm` | 570–583 | 570 | — | 0 |
| Frase 3 sale | 597–601 | — | — | 0 |
| **Toque en «Inscribir»** (grab. 36,32 s) | 600 | **600 (2.ª subida)** | `toque` c 601 | 0 |
| El sello, el confeti, «¡Quedaste inscrito!» y las dos filas | 602 | — | `confirmacion` 603 (1,4) | 0 |
| Cámara → `resultado` | 600–613 | 600 | — | 0 |
| Salto de la app (grab. 1257) compensado · cámara → `verBoleta` | 645 · 646–658 | 645 | — | invisible |
| La marca sobre «Ver boleta» | 656 | — | — | 0 (SPEC 656) |
| **Toque en «Ver boleta»** (grab. 41,90 s) | 660 | **660 (golpe)** | `toque` a 661 | 0 |
| «Mis boletas» con el QR y «Código FM75UZ»; aterrizaje | 662 / 662–672 | — | `confirmacion` 663 (1,0) | 0 |
| Punch → `qr` | 690–698 | 690 | — | 0 |
| **Toque en el QR** (grab. 46,61 s); frase 4 «Tu»; la ceja sale | 720 / 720–723 | **720 (golpe)** | `toque` b 721 | 0 |
| La boleta a pantalla completa | 722–728 | — | `aparicion` 723 | 0 |
| Frase 4 completa; la ventana a 0,92 | 734 / 724–738 | 720 | — | 0 |
| `subida` | — | — | 796–853 (golpe en el 840) | 0 |
| Dip | 837–839 | — | — | 0 |
| **La firma** | **840** | **840** | música 0,75 → 0,24 (852) → 0 (870); campanas 851 | 0 |

**Ninguna acción cae a más de 1 cuadro de su pulso.** Los +2 son respuestas animadas de la app (la lista que se desliza, el formulario que
aparece con un fundido); el toque, su marca y su sonido sí van en el pulso.

## 4. Desvíos del SPEC y su porqué

1. **Lo que la grabación cambió** (pedido): el saludo dice «Buenas tardes, Gabriela»; el congreso es del 29 al 30 de noviembre en «Finca La
   Esperanza, vía Caldas»; «Amén» pasa de 56 a 57; la lista ofrece «Yo» (marcada), «Martha Ríos Hinestroza» (sin marcar) y «Simón Ríos
   Arango» (el esposo, que se marca); el código es FM75UZ. Ninguna frase depende de eso. El plan B no hizo falta.
2. **Los desplazamientos de la app son saltos de un cuadro, no suaves.** Los cinco `ver`/`scrollIntoView` de la grabación (96, 547, 701–704,
   814, 1257) saltan. Los dos que cuentan algo (la novedad del 60 y la «Inscripción» del 300) se ven en su pulso con la cámara quieta y su
   `desliz`, como en Eventos. Los otros tres los provoca la herramienta antes de un toque y **la cámara los compensa en el mismo cuadro**
   (`comp()`) y luego baja en su compás: se lee como el desplazamiento suave que pedía el SPEC (452–464 y el «Ver boleta», que sin eso quedaba
   detrás de la barra inferior de la app). Para sostener esas pantallas hacen falta dos stills (grab. 705 y 1258): la app solo las deja
   quietas 5 y 1 cuadros antes del toque siguiente.
3. **La espera de la app se corta, no se muestra:** la K del cargador del evento (grab. 371–430), la de «Inscribir» (1099–1110), la carga de
   «Mis boletas» (1265–1280) y las ondas de Material entre cada toque y su efecto. Los cuadros quietos entre un toque y su efecto se saltan,
   así que cada radio, casilla y pantalla responde en el cuadro siguiente al pulso.
4. **El 60 es un salto y no un desplazamiento de 15 cuadros:** el pulso 75 queda sin suceso propio (la app ya llegó en el 60). Es el único
   pulso vacío entre 0 y 6 s; la cámara del 90 y la marca del 101 lo siguen de cerca.
5. **El iris del 180 descubre el evento ya encuadrado en G** (como pide el SPEC) gracias a dos capas fijas con el encuadre de la tarjeta:
   `#camT1` (el still del 179, debajo) y `#camT2` (la marca del 180, encima). La cámara salta a G en el 180 sin que se vea y el centro del
   círculo se calcula en sus coordenadas. La primera versión (la cámara moviéndose 180–193, como en Eventos) abría el evento a ×1,4 con las
   fechas cortadas: corregido.
6. **Encuadres recalculados con las posiciones reales** (las del SPEC eran estimaciones): `reacciones` a ×1,08 (G⁺) para que entren el
   selector y el total «57» (a ×1,4 se cortaba el contador); `tarjeta` en M; `datos` e `inscripcion` a ×1,12; `quienes` y `botonesForm` a
   ×1,18 (a 1,4 se cortaban «Seguir» e «Inscribir»; a 1,15 el borde cortaba «Inscripción» o «Talla de camiseta» a media letra); `form`,
   `resultado`, `verBoleta`, `boleta` y `grande` en G; el punch del QR a ×1,3 (a 1,4 «Datos de ejemplo» tapaba «Código»). Ningún encuadre
   con salto compensado alcanza las barras fijas de la app (si no, la barra saltaría).
7. **«Datos de ejemplo» abajo a la izquierda** (la posición que pidió el dueño) cae en tres momentos sobre algo real: «Yo» en 377–389 (la
   lista entra pegada a la barra inferior), «Inscrito» de Simón en 603–645 y el borde de «Congreso de Jóvenes» bajo el código de la boleta
   grande (722–839). Lo que cuenta la historia (el QR, el nombre y FM75UZ) queda libre.
8. **«Llega a cada celular.» va en una línea** (731 px) y la primera línea de la frase 4 mide **826 px** (≤ 888, medida en el snapshot):
   la frase 4 queda en dos líneas en su lugar de siempre, sin la válvula del SPEC §1.2.
9. **Los radios del segundo formulario se apagan en 512–514**: la app muestra «2 de 2» con los radios del primero que se vacían en 3 cuadros
   (grab. 952–954). Es real y se deja.
10. **Los niveles del sonido** son los de Eventos (§5).
11. **La firma dura 2,5 s** (pieza del kit): `check` avisa `line_unread` en «Kingdom» y «Prueba gratis 30 días», igual que en toda la serie.

## 5. La mezcla (medida, no oída)

Con los niveles que funcionaron en Eventos: los cuatro toques clave (121, 181, 601, 661) a **1,0**; la `confirmacion` del 603 y la
`aparicion` del 123 a **1,4**; la `confirmacion` del 663 y el resto del kit a 1,0; **la música a 0,75** en su carril (0,24 en el 852, 0 en el
870).

**Render final: −17,1 LUFS integrados, pico real −1,8 dBTP** (ffmpeg ebur128 y `hyperframes audio` coinciden), pico de muestra −1,9 dBFS,
**0 recortes**, LRA 2,0 LU, corto plazo máximo −15,5 LUFS. El render no tuvo que bajar nada y no se normalizó. Nadie lo oyó.

## 6. Lo que se revisó

- `npx hyperframes check --json`: **0 errores**, 3 avisos: `composition_file_too_large` (la raíz lleva los 32 tramos a propósito, para que se
  vean y se recorten en la línea de tiempo) y `line_unread` ×2 (§4.11).
- `npx hyperframes snapshot --review`: `.hyperframes/artifacts/snapshots/ea30074f-436a-449e-8755-9c3c6f84f11e/` (`review-beats-{1..4}.jpg`,
  `review-seam-01…33.jpg`, `review-phone-{1..4}.jpg`). Notas que salieron de ahí, ya corregidas: el iris abría a medio encuadre (P1, §4.5);
  «Datos de ejemplo» tapaba «Código» en el punch (P1, §4.6); los bordes cortaban «Inscripción» y «Talla de camiseta» a media letra (P2).
  Abierta a propósito (P2): en 119–121 la frase 1 sale y la frase 2 entra en el mismo lugar con desenfoque (el «blur swap» del SPEC).
- Los saltos compensados (389, 464, 645) en sus costuras: el cuadro anterior y el siguiente son iguales (`review-seam-14`, `-18`, `-27`).
- Cuadros clave en la vista previa: `snapshots/8e9c9a09-…/` (52 cuadros); el iris corregido en `snapshots/dae9b3db-…/`.
- **El render, cuadro a cuadro** (84 cuadros): `.hyperframes/artifacts/render-check/render-cuadros-{1..5}.jpg`.
- `ffprobe`: h264 1080×1350, 30/1, **915 cuadros**, AAC 48 kHz estéreo, **30,500 s**, 6 295 735 bytes.
- Nadie oyó el sonido ni vio el movimiento a velocidad real fuera del render.

## 7. El plano más débil y qué cambiaría con más tiempo

- **377–389**: la lista entra pegada a la barra inferior de la app y «Yo» queda bajo «Datos de ejemplo» hasta que la cámara baja en el 390.
  Con una regrabación: un `ver` suave a la lista después de «Inscribirme» (o grabar sin el `scrollIntoView` antes de marcar).
- **El salto del 60** se ve como un corte (es el salto real del `ver`). Una regrabación con desplazamiento suave lo haría deslizar en 60–75,
  como pedía el SPEC, y llenaría el pulso 75.
- **603–645**: la fila de Simón queda medio tapada por la píldora. Si molesta: `resultado` a ×1,06 centrado más arriba deja las dos filas
  enteras pero corta «Inscripción».
- **El sello entra ya puesto** en el 602 (su resorte ocurre durante la K del cargador, 1105–1110, que se corta); se ve el confeti real.

## 8. Para 9:16

Igual que Eventos (su REVIEW §8): en `_gen/index.tpl.html` cambiar las variables `--f-*` (1080×1920; márgenes 60; ceja 188 / 34 px; frase 236
/ 960 / 104 px; ventana 60·480·960×850 con `--f-ventana-h: 850px`, `--f-ventana-hvis: 850px`, `--f-k: 0.820513`, `--f-grab-alto: 2077.54px`) y
`window.KD` (ventana 960×850, `cambio` con origen «50% 0%», x +36 y arranque en el 720), la firma por `identidad/cierre-corto.html`,
`data-width/height` de los hosts y de las escenas, y la frase 4 en tres líneas («Tu iglesia, / en el *bolsillo* / de cada miembro»); luego
`python _gen/gen.py index.html _gen/index.tpl.html`. Los tramos, los stills, los sonidos y los saltos compensados no cambian; los encuadres
se recalculan con `enc()`, pero en 9:16 G muestra 345 px CSS de alto: revisar `form`, `resultado`, `verBoleta`, `boleta` y `grande`, que en
4:5 usan casi los 439, y que ningún encuadre con salto compensado alcance las barras de la app.
