# REVIEW · Clip del sitio: Comunicaciones — «Alguien nuevo escribe» (4:5)

2026-10-30 · Construcción en HyperFrames 0.8.221 a partir de [SPEC.md](SPEC.md) con la grabación real `assets/grabaciones/grabacion.mp4`
(1170×2532, 30 fps, 53,4 s, sin círculo de toque) y `pasos.json`. Plantilla: [Eventos](../clip-sitio-eventos/REVIEW.md). El dueño ya no
revisa: construido, verificado y renderizado sin paradas. **Entrega:** `renders/clip-sitio-comunicaciones-4x5.mp4`.

## 1. Qué hay

| Archivo | Qué es |
|---|---|
| `index.html` | La raíz: el formato en un solo lugar (`--f-*` y `window.KD`), los hosts de las escenas, **la ventana a la app** (un solo mundo), los 19 tramos de video (todos a 1×), las 8 marcas de toque, la cámara, el aterrizaje del 78, el cambio de ventana, el dip, la música y los 18 sonidos |
| `compositions/fondo.html` | La noche del sitio; el halo se asienta en 0, 180 y 720 |
| `compositions/frase-1.html` … `frase-4.html`, `ceja.html` | Las cuatro frases y la ceja «COMUNICACIONES», con sus entradas y salidas |
| `identidad/cierre-clip.html` | La firma del kit v1.1 (840–914), `{"llamado":"prueba","fondo":"azul","idioma":"es"}`, campanas en 28,38 |
| `assets/audio/toque-b.wav`, `toque-c.wav` | Las tomas b y c de `toque` (±3 % de tono), copiadas de Eventos |

Los tramos, las marcas y los sonidos salen de una tabla (`_gen/gen.py` + `_gen/index.tpl.html`; cómo regenerar en `_gen/README.md`); en `index.html` se
pueden editar a mano. Vista previa: `npm run dev`. Para el 9:16: §8.

## 2. Los planos, con sus cuadros

«grab.» = cuadro de `grabacion.mp4`. Todos los tramos a 1×: los huecos de pantalla quieta de `pasos.json` se recortan con cortes invisibles
(la pantalla es idéntica a los dos lados) y cada corte que cambia algo cae en una onda, una espera o un esqueleto de la app.

| Plano | Cuadros | Grabación y cámara |
|---|---|---|
| P1 Alguien nuevo escribe | 0–119 | grab. 40–117: la bandeja «Cola 4 · Mis chats 2 · Todas 8» quieta; toque en la fila de Mariana en el 75 (grab. 115). **Corte en la espera** («Cargando…» 121–125 fuera) a grab. 193–236: la conversación, con el aterrizaje 1,03 → 1,00 en 78–88. Cámara: G `cola` (CSS 173–612) hasta el 89, el match cut en el mismo encuadre · 90–103 → ×1,03 `hilo` (CSS 49–475). La marca espera sobre «Tomar» desde el 105 |
| P2 Todo tu equipo, un solo número | 120–179 | grab. 235–236 (toque en «Tomar»); corte en la onda (237→246): en el 122 «Atendiendo» y «Andrés Felipe Restrepo Gómez tomó la conversación · 18:33». Corte invisible 264→348. Cámara 150–163 → ×1,05 `compositor` (CSS 391–809) |
| P3 /horarios | 180–359 | grab. 388–389 (toque en el compositor); corte en el foco (390→394): «/» y las respuestas rápidas («/bienvenida», «/gracias», «/horarios», «/oracion») en el 182; corte invisible 422→476; grab. 506–507 (toque en «/horarios»); corte en la onda (508→512): el compositor lleno con el horario en el 242; corte invisible 540→590; grab. 620–621 (toque en enviar); corte en la espera (622→630): la respuesta en el hilo en el 302, con una palomita. Cámara 315–328 → ×1,04 `respuesta` (CSS 169–591) |
| P4 Y sabes quién leyó el aviso | 360–599 | Corte invisible 668→765; grab. 800–801 (toque en volver, fuera de cuadro); corte en la espera (802→808): «Cola 3 · Mis chats 3 · Todas 8» en el 377; corte invisible 831→894; grab. 914–915 (toque en «Campañas»); **corte en la espera y el esqueleto** (916→928): las tarjetas suben escalonadas 422–432 (la animación de la app); corte invisible 956→1011; **480: la lista salta hasta la invitación** (grab. 1041, salto real) y la cámara cambia de encuadre en el mismo cuadro; corte invisible 1071→1098. Cámara: 390–403 → G `arriba` (CSS 0–439) · 450–463 → ×1,08 `campanas` (CSS 118–524) · 480 → G `invitacion` (CSS 341–780) · 540–553 → ×1,08 `tarjeta` (CSS 377–783) |
| P5 115 leídos, 23 respondieron | 600–719 | grab. 1188–1189 (toque en la invitación); **corte en la espera y el esqueleto** (1190→1202): el reporte en el 602, ya encuadrado en G `kpis` (CSS 300–739); corte invisible 1230→1299; grab. 1329 (toque en «respondieron»); corte en la onda (1330→1335): el contorno en el 661; **675: la app salta a los nombres** (grab. 1396, salto real). Cámara 690–703 → ×1,06 `nombres` (CSS 186–600) |
| P6 Habla con tu iglesia, sin perder a nadie | 720–839 | grab. 1441–1560 quieta. Cámara 720–733 → ×1,08 `cierre` (CSS 262–668, seis filas); la ventana a 0,92 y +48 px en 724–738; dip 837–839 |
| P7 La firma | 840–914 | `cierre-clip` (fondo azul, llamado «prueba»); campanas en el 851 |

## 3. Sincronía: cada cosa con su cuadro y su pulso

Pulsos de la pista (SPEC §0): múltiplos de 15 (el 285 real cae en el 284; no hay nada ahí). «Imagen» es el primer cuadro en que se ve; el
sonido cae un cuadro después (`data-start` = cuadro del sonido / 30 − acento). Los cuadros de imagen se comprobaron **en el render final**
(extraídos con ffmpeg), no solo en la vista previa.

| Qué | Imagen | Pulso | Sonido | Desvío |
|---|---|---|---|---|
| «Alguien» puesta (la miniatura), la bandeja «Cola 4» y «Datos de ejemplo» | 0 | 0 | — | 0 |
| «nuevo escribe.» · «¿Quién» · «contesta?» | 15 · 30 · 45 | 15 · 30 · 45 | — | 0 |
| **Toque en la fila de Mariana** (grab. 115) | 75 | 75 | `toque` a 76 | 0 |
| Match cut: la conversación entra 1,03 → 1,00 | 78–88 | — | — | 0 (SPEC 78) |
| Cámara → `hilo` | 90–103 | 90 | — | 0 |
| La marca se posa sobre «Tomar» y espera | 105 | 105 | — | 0 |
| Frase 1 sale | 117–121 | — | — | 0 |
| **Toque en «Tomar»** (grab. 235) | 120 | **120 (bajo)** | `toque` c 121 (1,0) | 0 |
| Frase 2 entera | 120–126 | 120 | — | 0 |
| «Atendiendo» y «… tomó la conversación · 18:33» (grab. 246) | 122 | — | `aparicion` 123 | 0 |
| Cámara → `compositor` | 150–163 | 150 | — | 0 |
| Frase 2 sale | 177–181 | — | — | 0 |
| **Toque en el compositor** (grab. 388) | 180 | **180 (pico)** | `toque` b 181 (1,0) | 0 |
| «/» y las respuestas rápidas (grab. 394) | 182 | — | — (el mismo toque) | +2 (la tecla, como el SPEC: ≈ 182) |
| Ceja «COMUNICACIONES» | 195 | 195 | `aparicion` 196 | 0 |
| **Toque en «/horarios»** (grab. 506) | 240 | 240 | `toque` a 241 | 0 |
| El compositor lleno con el horario (grab. 512) | 242 | — | `aparicion` 243 | 0 |
| **Toque en enviar** (grab. 620) | 300 | 300 | `toque` c 301 (1,0) | 0 |
| La respuesta en el hilo, una palomita (grab. 630) | 302 | — | `confirmacion` 303 (1,4) | 0 |
| Cámara → `respuesta`; quieta 328–359 (la excepción del BANNED 29) | 315–328 | 315 | — | 0 |
| Frase 3, palabra a palabra | 360 · 362 · 364 · 366 · 368 · 370 | 360 | — | 0 |
| **Toque en volver** (grab. 800, fuera de cuadro, sin marca) | 375 | 375 | `toque` b 376 | 0 |
| «Cola 3 · Mis chats 3 · Todas 8» (grab. 808) | 377 | — | — | +2 (SPEC 375: el corte cae después de la espera) |
| Cámara → `arriba` | 390–403 | 390 | — | 0 |
| **Toque en «Campañas»** (grab. 914) | 420 | 420 | `toque` a 421 | 0 |
| Las campañas; las tarjetas suben (la animación de la app) | 422 · 422–432 | — | — | 0 |
| Cámara → `campanas` | 450–463 | 450 | — | 0 |
| **La lista salta hasta la invitación** (grab. 1041) + el encuadre `invitacion` | 480 | 480 | `desliz`, acento 481 | 0 |
| Cámara → `tarjeta` | 540–553 | 540 | — | 0 |
| Frase 3 sale | 597–601 | — | — | 0 |
| **Toque en la invitación** (grab. 1188) | 600 | **600 (2.ª subida)** | `toque` b 601 (1,0) | 0 |
| El reporte: 139 · 137 · 137 · **115 leídos** · **23 respondieron** · 39 (grab. 1202), ya en `kpis` | 602 | — | `confirmacion` 603 (1,0) | 0 |
| **Toque en «respondieron»** (grab. 1329) | 660 | **660 (golpe)** | `toque` c 661 (1,0) | 0 |
| El contorno de «respondieron» (grab. 1335) | 661 | — | — | +1 |
| **Los nombres** con «Leído» y «↩ Allí estaré» (grab. 1396) | 675 | **675 (0,89)** | `confirmacion` 676 (1,4) | 0 |
| Cámara → `nombres` («Destinatarios (23)») | 690–703 | 690 | — | 0 |
| Frase 4, palabra a palabra; la ceja sale | 720 · 722 · … · 734 / 720–723 | **720 (golpe)** | — | 0 |
| Cámara → `cierre`; la ventana a 0,92 | 720–733 / 724–738 | 720 | — | 0 |
| `subida` | — | — | 796–853 (golpe en el 840) | 0 |
| Dip | 837–839 | — | — | 0 |
| **La firma** | **840** | **840 (el más fuerte)** | música 0,75 → 0,24 (852) → 0 (870); campanas 851 | 0 |

Ninguna acción cae a más de 1 cuadro de su pulso. Las de +2 son consecuencias de una acción que ya cayó en su pulso (la tecla «/» después
del toque, la lista después de la espera de volver), como en el SPEC; el contorno de «respondieron» va un cuadro después de su toque.

## 4. Desvíos del SPEC y su porqué

1. **La app no se desplaza suave: salta en un cuadro** (grab. 1041 y 1396), como en Eventos. El SPEC esperaba desplazamientos de 15–18
   cuadros. Los dos saltos son acciones con causa en el guion («la lista baja hasta la invitación» y «la app baja a los nombres») y caen en
   su pulso (480 y 675), con su sonido.
2. **El salto del 480 va con un cambio de encuadre en el mismo cuadro.** La lista de campañas trae el aviso real «Fuera del horario de envío
   (de 05:00 a 05:30): sigue sola a las 05:00» en la tarjeta «Noche de oración del viernes» (CSS 526–554 antes del salto, 181–197 después).
   Ningún encuadre de ≥ 406 px CSS alto lo deja fuera a los dos lados del salto, así que la cámara pasa de `campanas` (118–524) a
   `invitacion` (341–780) en el mismo cuadro en que la app salta: se lee como un solo corte y el aviso nunca queda en cuadro.
3. **El reporte entra ya encuadrado (602)**, sin el movimiento de cámara 600–613 del SPEC: la pantalla cambia entera en el corte, así que
   fijar el encuadre `kpis` en ese cuadro no se ve como movimiento y la cámara nunca se mueve mientras la app cambia.
4. **Sin movimiento en el compás 1** (la válvula de P1 del SPEC): el encuadre G `cola` contiene la fila de Mariana antes del corte y su
   burbuja después (CSS 231–320), así que el match cut del 78 aterriza en G. El primer acercamiento es el del 90.
5. **Encuadres recalculados con las cajas reales.** Esta app usa todo el ancho del celular: la burbuja de Mariana empieza en x 12 y la
   píldora «En la cola» termina en x 382; las tarjetas, los KPI y las filas de destinatarios van de 16 a 374 con su ficha a la derecha.
   M (×1,40, 279 px CSS de ancho) las cortaba todas, así que los encuadres van de ×1,00 a ×1,08 y el texto de 14 px queda entre 31,6 y
   34 px (los nombres de los destinatarios, de 16 px, entre 38 y 39 px). El de `cierre` es ×1,08 y no M⁻: a ×1,12 los nombres y las fichas
   «Leído» tocaban los bordes; la línea «•••• 8588 · fecha · ↩ Allí estaré» mide 12,4 px en la grabación y queda en 27,8 px con la ventana
   a 0,92.
6. **Los textos reales que cambió la grabación:** las respuestas rápidas van en el orden «/bienvenida · /gracias · /horarios · /oracion»;
   la cola tiene a Juan Rivera González, Carolina Mejía Arango, Mariana Ospina y Camilo Ríos; la hora de la nota es «18:33»; la lista de
   campañas trae «Bienvenida a los nuevos de octubre · Borrador», «Noche de oración del viernes · Fuera de horario», «Recordatorio:
   Congreso de Jóvenes · Programada», «Boletas del Congreso de Jóvenes · Programada» y la invitación «Completada» con «137 enviados · 100 %
   entregados · 84 % leídos · 23 respondieron · 39 clics · 2 fallidos». Ninguna frase depende de ellos.
7. **Las esperas de la app se cortan:** «Cargando…» (grab. 121–125), los esqueletos de Campañas (922–927) y del reporte (1197–1201, que
   muestran «Nueva campaña» como título mientras cargan), y las ondas entre cada toque y su efecto (237–245, 390–393, 508–511, 622–629,
   802–807, 1330–1334). Las marcas de toque que quedarían sobre otra pantalla (75, 120, 240, 420, 600) se van con el corte.
8. **Los nombres llegan en el 675 con una sola `confirmacion` (1,4) en el 676**, en vez del `desliz` del 672 y la `confirmacion` del 688 del
   SPEC: con el salto en un cuadro, la imagen y su sonido van juntos en el pulso 675 (0,89), y un `desliz` encima subía el pico. El
   `desliz` queda en el 481, con la lista que baja hasta la invitación.
9. **El bloque rojo «Por qué no les llegó» y su «WhatsApp»** (texto real de la app) quedan fuera de todos los encuadres (CSS 88–178; los
   encuadres después del 675 empiezan en 186). Tampoco aparecen créditos, saldos, precios ni el costo en Meta.
10. **El sonido:** ver §5.
11. **La firma dura 2,5 s** (pieza aprobada del kit): `check` avisa que «Kingdom» (1,67 s) y «Prueba gratis 30 días» (1,5 s) duran menos de
    2 s. Se deja: es la firma de toda la serie.

## 5. La mezcla (medida, no oída)

Niveles de Eventos desde el principio (sin la ronda de prueba): los cinco toques clave (121, 181, 301, 601, 661) a **1,0**, las
`confirmacion` de las pruebas a **1,4** (303 y 676; la del 603, a 1,0, como el SPEC) y la música a **0,75** en el carril de volumen (0,24 en
el 852 = −10 dB, 0 en el 870). Hay 16 sonidos de acción, la `subida` y las campanas.

**Render final:** **−17,1 LUFS integrados, pico real −2,7 dBTP** (ffmpeg ebur128 y `hyperframes audio` coinciden), sin recortes, LRA
2,2 LU, sonoridad de corto plazo máxima −15,5; el render no tuvo que bajar nada. `hyperframes audio` detecta los golpes en **2,53 · 4,03 ·
6,03 · 8,03 · 10,03 · 12,53 · 14,03 · 20,03 · 22,03 s** = cuadros 76 · 121 · 181 · 241 · 301 · 376 · 421 · 601 · 661: los nueve `toque`,
cada uno un cuadro después de su imagen. Las `aparicion`, las `confirmacion` y el `desliz` son más suaves y no salen como golpes; sus
`data-start` están en la tabla de §3. Nadie lo oyó: está medido.

## 6. Lo que se revisó

- `npx hyperframes check --json`: **0 errores**, 3 avisos: `composition_file_too_large` (la raíz lleva los 19 tramos de video a propósito,
  para que se vean y se recorten en la línea de tiempo) y `line_unread` ×2 (§4.11). Contraste, disposición, movimiento y audio: 0 y 0.
- `npx hyperframes snapshot --review`: `.hyperframes/artifacts/snapshots/6bcbf852-c3be-46a4-bf51-fbf683b0286f/`
  (`review-beats-{1,2,3}.jpg`, `review-seam-NN.jpg`, `review-phone-{1,2,3}.jpg`). Notas que salieron de las dos rondas de cuadros clave
  anteriores, ya corregidas: «Datos de ejemplo» tapaba la fila de Mariana en el cuadro 0 (P0: `cola` bajó a CSS 173); el borde de «Tomar»
  asomaba arriba después del match cut (P2: `cola` empieza debajo de 171); la píldora «En la cola» y la burbuja tocaban los bordes (P2:
  `hilo` a ×1,03); el subrayado de la pestaña asomaba sobre «Cola 3» (P2: `respuesta` a CSS 169); `campanas` cortaba el título
  «Campañas» (P2: CSS 118–524); los nombres y las fichas «Leído» tocaban los bordes en `nombres` y `cierre` (P1: ×1,06 y ×1,08). El
  movimiento del compás 1 se quitó (§4.4).
- **El render final cuadro a cuadro** (64 cuadros extraídos con ffmpeg alrededor de cada corte, toque y salto; `_gen/rsheet.py`): cada toque
  con su marca en su pulso, «Atendiendo» y la nota en el 122, las respuestas en el 182, el horario en el 242, la respuesta en el 302,
  «Cola 3» en el 377, las campañas en el 422, el salto en el 480, el reporte en el 602, el contorno en el 661, los nombres en el 675, el dip
  837–839 y la firma en el 840.
- Mirado: el cuadro 0 (la bandeja con «Cola 4», Mariana con «Sin ficha» y su globo, «Alguien», «Datos de ejemplo»); ningún cuadro con
  «Cargando…», la K del cargador ni un esqueleto; la respuesta con una palomita gris; el aviso «Fuera del horario de envío» y el bloque
  «Por qué no les llegó» nunca en cuadro; ningún crédito, saldo ni precio; el único número a la vista es el ficticio de Mariana
  (+575550123987); la frase 4 con *nadie* dorada; el primer cuadro de la firma sin noche vacía.
- Nadie oyó el sonido ni vio el movimiento a velocidad real fuera del render.

## 7. El plano más débil y qué cambiaría con más tiempo

- **El compositor (163–314)** muestra mucho espacio vacío arriba (la conversación de Mariana es corta): el encuadre tiene que tener la lista
  de respuestas y el compositor a la vez. Un encuadre más bajo dejaría ver la barra de navegación de la app.
- **El cambio de encuadre del 480** se lee como un corte duro dentro del mismo celular. Si se regraba la escena con la campaña «Noche de
  oración del viernes» dentro del horario de envío (o con `ver` en pasos de desplazamiento suave), la cámara podría quedarse y la lista
  bajaría sola.
- **«Datos de ejemplo»** tapa la parte izquierda de la fila de Diego en el plano final y de la fila de Carolina en el 403–421: es la posición
  que pidió el dueño.
- La salida de la frase 1 y la entrada de la frase 2 se cruzan con desenfoque en 119–121 (el «blur swap» del SPEC), igual que en Eventos.

## 8. Para 9:16

Cambiar en `index.html` las variables `--f-*` (1080×1920; márgenes 60; ceja 188 / 34 px; frase 236 / 960 / 104 px; ventana 60·480·960×850
con `--f-ventana-h: 850px`, `--f-ventana-hvis: 850px`, `--f-k: 0.820513`, `--f-grab-alto: 2077.54px`) y `window.KD` (ventana 960×850,
`cambio` escala 0,92 con origen «50% 0%» y x +36), la firma por `identidad/cierre-corto.html` y `data-width/height` de los hosts y de las
escenas; las frases 1 y 4 en tres líneas («Alguien nuevo / escribe. / ¿Quién contesta?», «Habla con / tu iglesia, / sin perder a *nadie*»).
Los tramos de video, los sonidos y los tiempos no cambian: la cámara se recalcula sola con `enc()`. En 9:16 se ven 345 px CSS de alto en G:
revisar `cola` (Mariana entera por encima de la píldora), `compositor` (lista y compositor: 468–755), `campanas` (que el aviso de 526 siga
fuera), `kpis` y `cierre`.
