# REVIEW · Clip del sitio: Eventos — «Terminó la reunión» (4:5)

2026-10-30 · Construcción en HyperFrames 0.8.221 a partir de [SPEC.md](SPEC.md) con la grabación real `assets/grabaciones/grabacion.mp4`
(1170×2532, 30 fps, 53,1 s, sin círculo de toque) y `pasos.json`. Plantilla: [Membresía](../clip-sitio-membresia/REVIEW.md). El dueño ya no
revisa: construido, verificado y renderizado sin paradas. **Entrega:** `renders/clip-sitio-eventos-4x5.mp4`.

## 1. Qué hay

| Archivo | Qué es |
|---|---|
| `index.html` | La raíz: el formato en un solo lugar (`--f-*` y `window.KD`), los hosts de las escenas, **la ventana a la app** (un solo mundo), los 30 tramos de video, los dos stills, las 14 marcas de toque, la cámara (con las tres compensaciones de salto), el iris, el cambio de ventana, el dip, la música y los 24 sonidos |
| `compositions/fondo.html` | La noche del sitio; el halo se asienta en 0, 180 y 720 |
| `compositions/frase-1.html` … `frase-4.html`, `ceja.html` | Las cuatro frases y la ceja «EVENTOS», con sus entradas y salidas |
| `identidad/cierre-clip.html` | La firma del kit v1.1 (840–914), `{"llamado":"prueba","fondo":"azul","idioma":"es"}`, campanas en 28,38 |
| `assets/stills/still-364.png` | El cuadro de la grabación debajo del iris del 180 |
| `assets/stills/still-1027.png` | El paso ② con la barra al 15 %, sostenido 602–609 mientras la cámara sube (la app no cambia entre la 1026 y la 1029) |
| `assets/audio/toque-b.wav`, `toque-c.wav` | Las tomas b y c de `toque` (±3 % de tono), copiadas de Membresía |

Vista previa: `npm run dev` (o `npx hyperframes@0.8.221 preview --background`; quedó abierta en `http://localhost:3003/#project/clip-sitio-eventos`).
Para el 9:16: §8.

## 2. Los planos, con sus cuadros

«grab.» = cuadro de `grabacion.mp4`. Todos los tramos a 1× salvo los tres que se indican.

| Plano | Cuadros | Grabación y cámara |
|---|---|---|
| P1 Terminó la reunión | 0–119 | grab. 23–100 (Servir quieto; toque en «Reportar» en el 75 = grab. 98); **corte en la espera** («Cargando…» 108–114 fuera) a grab. 170–212 (el reporte, «0 marcadas»), con el aterrizaje 1,03 → 1,00 en 78–88. Cámara: G `servir` (CSS 0–439) · 46–59 → ×1,15 `fila` (CSS 28–367 × 154–536) · el match cut en el mismo encuadre · 90–103 → G `lista` (CSS 380–819). La marca espera sobre «Igual que la última vez» desde el 105 |
| P2 Los de siempre, en un toque | 120–179 | grab. 212 (el toque); corte en la onda del botón (213→219); grab. 219–248 («7 marcadas» y las filas en ámbar en el 122, las casillas se llenan 123–128); **150: la app baja en un cuadro** (grab. 291, salto real de la app) a grab. 335–364: «Persona nueva», «Visitantes», «Total: 7 personas». Cámara quieta todo el compás |
| P3 Persona nueva | 180–359 | **Iris** 180–185 desde «Persona nueva» (still de la grab. 364 debajo); grab. 365, corte en el fundido de la hoja (366→380) y la hoja ya puesta desde el 181; grab. 406–468 («Ximena» 248–260); grab. 495–503; **grab. 503–536 a 1,18×** («Hoyos Vélez» 277–296); grab. 569–571; **grab. 571–578 a 0,467×** (el campo «Teléfono» se enfoca mientras la cámara baja); **grab. 578–600 a 0,8×** («5550198765» 316–342); grab. 635–647 («Mujer» se llena 346–352); grab. 666–687. Cámara: 180–193 → M `hojaAlta` (CSS 15–294 × 388–702) · 300–313 → C `telefono` (CSS 77–294 × 528–772) · 345–358 → G `hoja` (CSS 395–834) |
| P4 Y queda registrada | 360–599 | grab. 686–687 (toque en «Agregar»); corte en la onda (688→694): la hoja se va 377–378 y en el 379 la fila «Ximena Hoyos Vélez · Nueva», «Total: 8 personas»; grab. 754–815 (toque «+» en el 450); corte en la espera (816→821): «1», «Total: 9 personas» en el 452; grab. 844–863 (toque «+» en el 480); corte (864→870): «2», «Total: 10 personas» en el 482; grab. 870–918; **525: la app sube 62 px CSS (grab. 919), compensado por la cámara** (grab. 925–939); grab. 947–1008. Cámara: 390–403 → M `nuevaFila` (CSS 10–289 × 452–766) · 510–523 → C `total` (CSS 7–223 × 518–762) · 540–553 → ×1,3 `botones` (CSS 10–310 × 438–776) |
| P5 Guardar asistencia, enviar reporte | 600–719 | grab. 1007–1008 (toque en «Guardar asistencia»); **corte en la espera y la K del cargador** (1009→1026): el paso ② en el 602; still de la grab. 1027 en 602–608; grab. 1029–1034 (la barra 15 → 66 % en 610–614); **615: la app baja 66 px (grab. 1090), compensado**: grab. 1154–1155 (toque en «Muy bien»); corte en la onda (1156→1160), el radio se llena 618–621; grab. 1195–1204 (toque en «Tema de la palabra» en el 630); **grab. 1213–1232 a 1,5×** («El perdón» 633–643); **645: la app sube 66 px (grab. 1257), compensado**: grab. 1293–1309 (toque en «Enviar reporte» en el 660); **corte en la espera y la K del cargador** (1310→1328): «¡Listo!» en el 662, la barra 66 → 100 % en 663–672. Cámara: 600–608 → G `formulario` (CSS 155–594) · 646–658 → G `enviar` (CSS 311–750) · 660–673 → G `listo` (CSS 218–658) · 690–698 punch → ×1,13 `tarjeta` (CSS 374–762) |
| P6 Cada reunión cuenta, y cuenta bien | 720–839 | grab. 1386–1505 quieta (el «¡Listo!» real). Cámara 720–733 → ×1,12 `cierre` (CSS 215–605); la ventana a 0,92 y +48 px en 724–738; dip 837–839 |
| P7 La firma | 840–914 | `cierre-clip` (fondo azul, llamado «prueba»); campanas en el 851 |

Las velocidades quedan entre 0,467× y 1,5× (límite del SPEC 0,35×–3,5×). Cada corte de video cae en una espera, una onda de botón o una pausa
de la grabación: el único corte que se ve como tal es el «la app baja» del 150, que es el salto real de la app y cae en su pulso.

## 3. Sincronía: cada cosa con su cuadro y su pulso

Pulsos de la pista (SPEC §0): múltiplos de 15 (el 285 real cae en el 284; no hay nada ahí). «Imagen» es el primer cuadro en que se ve; el
sonido cae un cuadro después (`data-start` = cuadro del sonido / 30 − acento). Los cuadros de imagen se comprobaron en el render final
(extraídos con ffmpeg), no solo en la vista previa.

| Qué | Imagen | Pulso | Sonido | Desvío |
|---|---|---|---|---|
| «Terminó» puesta (la miniatura) | 0 | 0 | — | 0 |
| «la reunión.» · «¿Quién» · «vino?» | 15 · 30 · 45 | 15 · 30 · 45 | — | 0 |
| Cámara → `fila` | 46–59 | 45 (compás 1) | — | +1 (como el SPEC) |
| **Toque en «Reportar»** (grab. 98) | 75 | 75 | `toque` a 76 | 0 |
| Match cut: el reporte entra 1,03 → 1,00 | 78–88 | — | — | 0 (SPEC 78) |
| Cámara → `lista` | 90–103 | 90 | — | 0 |
| La marca se posa sobre «Igual que la última vez» y espera | 105 | 105 | — | 0 |
| Frase 1 sale | 117–121 | — | — | 0 |
| **Toque en «Igual que la última vez»** (grab. 212) | 120 | **120 (bajo)** | `toque` c 121 | 0 |
| Frase 2 entera | 120–126 | 120 | — | 0 |
| Filas en ámbar, «7 marcadas» (grab. 220) | 122 | — | `confirmacion` 123 (1,4) | 0 |
| La app baja al final de la lista (grab. 291) | 150 | 150 | `desliz`, acento 151 | 0 |
| Frase 2 sale | 177–181 | — | — | 0 |
| **Toque en «Persona nueva»** (grab. 365); iris | 180 / 180–185 | **180 (pico)** | `toque` b 181 | 0 |
| La hoja «Persona nueva» (grab. 380) | 181 | — | — | +1 |
| Cámara → `hojaAlta` | 180–193 | 180 | — | 0 |
| Ceja «EVENTOS» | 195 | 195 | `aparicion` 196 | 0 |
| Toque en «Nombres» (grab. 446) · «Ximena» | 240 · 248–260 | 240 | `toque` a 241 | 0 |
| Toque en «Apellidos» (grab. 503) · «Hoyos Vélez» | 270 · 277–296 | 270 | `toque` b 271 | 0 |
| Toque en «Teléfono» (grab. 571) · cámara → `telefono` | 300 · 300–313 | 300 | `toque` c 301 | 0 |
| «5550198765» (cámara quieta) | 316–342 | 315… | — (sin tics, como el SPEC) | 0 |
| Toque en «Mujer» (grab. 637), el botón se llena · cámara → `hoja` | 345 · 346–352 · 345–358 | 345 | `toque` a 346 | 0 |
| Frase 3, palabra a palabra | 360 · 362 · 364 · 366 · 368 · 370 | 360 | — | 0 |
| **Toque en «Agregar»** (grab. 686) | 375 | 375 | `toque` b 376 | 0 |
| La hoja se va; la fila «Ximena Hoyos Vélez · Nueva», «Total: 8 personas» | 377–378 / 379 | — | `aparicion` 380 | 0 (SPEC 379) |
| Cámara → `nuevaFila` | 390–403 | 390 | — | 0 |
| Toque en «+» (grab. 814) · «1», «Total: 9 personas» | 450 · 452 | 450 | `toque` c 451 · `aparicion` 453 | 0 |
| Toque en «+» (grab. 862) · «2», «Total: 10 personas» | 480 · 482 | 480 | `toque` a 481 · `aparicion` 483 | 0 |
| Cámara → `total` | 510–523 | 510 | — | 0 |
| Salto de la app (grab. 919) compensado | 525 | — | — | invisible |
| Cámara → `botones` | 540–553 | 540 | — | 0 |
| Frase 3 sale | 597–601 | — | — | 0 |
| **Toque en «Guardar asistencia»** (grab. 1007) | 600 | **600 (2.ª subida)** | `toque` b 601 | 0 |
| El paso ② «Reporte de la casa de paz (2)» (grab. 1026) | 602 | — | `confirmacion` 603 (1,0) | 0 |
| Cámara → `formulario` · la barra 15 → 66 % | 600–608 · 610–614 | 600 | — | 0 |
| Salto de la app (grab. 1090) compensado | 615 | — | — | invisible |
| Toque en «Muy bien» (grab. 1154) · el radio se llena | 615 · 618–621 | 615 | `toque` c 616 | 0 |
| Toque en «Tema de la palabra» (grab. 1203) · «El perdón» | 630 · 633–643 | 630 | `toque` a 631 | 0 |
| Salto de la app (grab. 1257) compensado · cámara → `enviar` | 645 · 646–658 | — | — | invisible |
| **Toque en «Enviar reporte»** (grab. 1308) | 660 | **660 (golpe)** | `toque` b 661 | 0 |
| «¡Listo!» con «10 personas.» y «Reportada» (grab. 1328) | 662 | — | `confirmacion` 663 (1,4) | 0 |
| La barra 66 → 100 % · cámara → `listo` | 663–672 · 660–673 | 660 | — | 0 |
| Punch → `tarjeta` | 690–698 | 690 | — | 0 |
| Frase 4, palabra a palabra; la ceja sale | 720 · 722 · 724 · 726 · 728 · 730 / 720–723 | **720 (golpe)** | — | 0 |
| Cámara → `cierre`; la ventana a 0,92 | 720–733 / 724–738 | 720 | — | 0 |
| `subida` | — | — | 796–853 (golpe en el 840) | 0 |
| Dip | 837–839 | — | — | 0 |
| **La firma** | **840** | **840 (el más fuerte)** | música 0,75 → 0,24 (852) → 0 (870); campanas 851 | 0 |

Ninguna acción cae a más de 1 cuadro de su pulso. Las dos de +1 (la cámara del compás 1 y la hoja del 181) son las del SPEC: la cámara
arranca después del último aterrizaje de la frase y la hoja aparece dentro del iris que nace en el pulso.

## 4. Desvíos del SPEC y su porqué

1. **Lo que la grabación cambió** (pedido): la escena empieza en Servir con la tarjeta (el toque en «Reportar» es la grab. 98); «Igual que la
   última vez» marca **7**: con Ximena, «Total: 8»; con los dos visitantes, **9 y 10** (el SPEC decía 5, 6 y 7); el «¡Listo!» dice
   «Casa de Paz Laureles 1, miércoles, 28 de octubre: 10 personas.»; la hoja «Persona nueva» es un **modal** que oscurece la lista y no
   sube: aparece con un fundido de 5 cuadros. Ninguna frase depende de esos números.
2. **El formulario trae un cuarto campo**, «Personas que aceptaron a Cristo». El encuadre `formulario` (CSS 155–594) lo deja fuera; solo
   se ve en 602–604 (el paso ② entra con la cámara todavía abajo) y en 646–661 (el encuadre `enviar` lo tiene que cruzar para llegar a
   «Enviar reporte», que está debajo).
3. **Las esperas de la app se cortan:** «Cargando…» (grab. 108–114), la K del cargador después de «Guardar asistencia» (1021–1024) y de
   «Enviar reporte» (1320–1326), y las ondas de Material entre el toque y su efecto (213–219, 366–380, 688–694, 816–821, 864–870,
   1156–1160). Cada acción visible cae en su pulso y la marca de toque y su sonido van en el mismo cuadro.
4. **La app no se desplaza suave: salta en un cuadro** (grab. 291, 919, 1090 y 1257). El del 291 es «la app baja al final de la lista» del
   SPEC y se deja ver en su pulso (150) con el `desliz`. Los otros tres (62, 66 y 66 px CSS, medidos por correlación) los provoca el
   guion de la grabación (`ver` del total, de la pregunta y de «Enviar reporte») y no cuentan nada: **la cámara los compensa en el mismo
   cuadro** (`comp()` en `index.html`), así que en pantalla nada se mueve. La marca de «Muy bien», que aparece antes del salto del 615, va
   corrida esos 66 px hasta el salto.
5. **La barra 15 → 66 % del 600 se sostiene con un still.** En la grabación crece 4 cuadros después de la pantalla nueva; con la cámara
   subiendo 600–613 (SPEC) el crecimiento quedaba fuera de cuadro. La cámara sube más rápido (600–608, 9 cuadros) y un still de la grab.
   1027 (la app idéntica entre 1026 y 1029) sostiene la barra al 15 % hasta el 609; crece en 610–614 con la cámara ya quieta.
6. **Encuadres recalculados con las cajas reales** (las del SPEC eran estimaciones): `fila` a ×1,15 y no M (a 1,4 se cortaban «Casa de
   Paz…» o «Reportar»); `telefono` es C (×1,8) en vez de `hoja-baja` (M): los números a 57 px y «Mujer» dentro; `botones` a ×1,3 para que
   «Guardar asistencia» quede por encima de «Datos de ejemplo» (a 1,4 la píldora tapaba el botón que se toca en el 600); `tarjeta` a
   ×1,13 y no M: la frase del «¡Listo!» mide 327 px CSS y a 1,4 se cortaba por los dos lados (el texto queda a 36 px, no a 44); `cierre` a
   ×1,12 (de «Reportada» a «Volver a la lista», texto a 32 px con la ventana a 0,92).
7. **El iris del 180 es de 1 cuadro visible:** la hoja real entra con un fundido; el clip corta a la hoja ya puesta (grab. 380) dentro del
   iris, que la abre desde el botón en 0,17 s. Las marcas de toque que quedarían sobre otra pantalla (75, 180, 375, 600, 660) se van con el
   corte en vez de seguir 6 cuadros (la del 180 caía sobre «Nombres»).
8. **Tres tramos fuera de 1×:** «Hoyos Vélez» a 1,18× (a 1× terminaba en el 301, encima del toque del 300), el enfoque de «Teléfono» a
   0,467× (la cámara baja mientras nadie escribe) y «El perdón» a 1,5× (para que termine antes del salto del 645 y la cámara llegue a
   «Enviar reporte» en el 658). El desfase del extractor por debajo de 1× (~2 cuadros en Membresía) **no apareció**: en el render los
   dígitos del teléfono caen en su cuadro calculado (6 en el 330, 9 en el 341, 10 en el 342).
9. **El sonido:** ver §5.
10. **La firma dura 2,5 s** (pieza aprobada del kit): `check` avisa que «Kingdom» (1,67 s) y «Prueba gratis 30 días» (1,5 s) duran menos de
    2 s. Se deja: es la firma de toda la serie (igual que en Membresía).

## 5. La mezcla (medida, no oída)

Primer render con los niveles del SPEC (música 0,7, los cuatro toques clave a 1,4): **−17,6 LUFS con el pico real en −0,1 dBTP**; el
render lo bajó solo 1,4 dB («Audio lowered by 1.4 dB to stay under −1 dBTP») y quedó en **−19,0 LUFS**. Los picos eran los cuatro toques a
1,4 (4,0 · 6,0 · 20,0 · 22,0 s). Con una simulación de la mezcla en ffmpeg (las mismas fuentes, tiempos y niveles) se eligió:

- **Los cuatro toques clave (121, 181, 601, 661) a 1,0** (la válvula del SPEC §1.7 decía 1,2: a 1,2 el pico seguía en −0,6 dBTP). Las
  `confirmacion` del 123 y del 663 siguen a 1,4.
- **La música a 0,75** en el carril de volumen (0,24 en el 852 = −10 dB, 0 en el 870): +0,6 dB sobre el 0,7 del kit, para llegar a −17 sin
  normalizador.

Simulación: −17,1 LUFS · −1,4 dBTP. **Render final:** **−17,1 LUFS integrados, pico real −1,4 dBTP** (ffmpeg ebur128 y
`hyperframes audio` coinciden), sin recortes, LRA 2,0 LU, sonoridad de corto plazo máxima −15,5; el render ya no tuvo que bajar nada.
`hyperframes audio` detecta los golpes en **2,53 · 4,03 · 6,03 · 8,03 · 9,03 · 10,03 · 11,53 · 12,53 · 15,03 · 16,03 · 20,03 · 20,53 · 21,03 ·
22,03 s** = cuadros 76 · 121 · 181 · 241 · 271 · 301 · 346 · 376 · 451 · 481 · 601 · 616 · 631 · 661: los 14 `toque`, cada uno un cuadro
después de su imagen.

## 6. Lo que se revisó

- `npx hyperframes check --json`: **0 errores**, 3 avisos: `composition_file_too_large` (la raíz lleva los 30 tramos de video a propósito,
  para que se vean y se recorten en la línea de tiempo) y `line_unread` ×2 (§4.10).
- `npx hyperframes snapshot --review`: `.hyperframes/artifacts/snapshots/3ba4bfa0-7fb8-4226-a2e4-e002095cd5a2/`
  (`review-beats-{1,2,3}.jpg`, `review-seam-01…35.jpg`, `review-phone-{1,2,3}.jpg`). Notas que salieron de ahí, ya corregidas: la píldora
  «Datos de ejemplo» tapaba «Guardar asistencia» (P0, §4.6); la marca del 180 quedaba sobre «Nombres» (P1, §4.7); la barra del 600 crecía
  fuera de cuadro (P1, §4.5); «fila» cortaba «Hola, Jorge…» y «Demo 1» por el borde (P2); `tarjeta` cortaba los nombres de los pasos (P2).
  Abierta a propósito (P2): en 119–121 la frase 1 sale y la frase 2 entra en el mismo lugar con desenfoque (el «blur swap» del SPEC).
- Cuadros clave en la vista previa (56 + 22 tras las correcciones): `.hyperframes/artifacts/snapshots/6a9b4e15-…/` y `448a348d-…/`.
- **El render final cuadro a cuadro** (60 cuadros extraídos con ffmpeg alrededor de cada corte, toque y salto compensado): cada toque con
  su marca en su pulso, «7 marcadas» en el 122, la hoja en el 181, «Total: 9» en el 452 y «Total: 10» en el 482, el paso ② en el 602, la
  barra 610–614, el radio en el 618, «¡Listo!» en el 662; los saltos de 525, 615 y 645 sin ningún movimiento entre el cuadro anterior y el
  siguiente.
- Mirado: el cuadro 0 (Servir con «2 vencidas», «Terminó», «Datos de ejemplo»); ninguna frase sobre la hoja; la frase 4 con *reunión*
  dorada; el primer cuadro de la firma sin noche vacía.
- Nadie oyó el sonido ni vio el movimiento a velocidad real fuera del render.

## 7. El plano más débil y qué cambiaría con más tiempo

- **602–661**: el compás más denso (guardar, la barra, «Muy bien», el tema y «Enviar reporte» en 2 s) pide dos encuadres que cruzan el
  campo «Personas que aceptaron a Cristo». Si estorba, la válvula del SPEC sigue abierta: no escribir el tema (615 «Muy bien», 630 el
  dedo baja, 660 «Enviar reporte») y quedarse en `formulario` hasta el 645.
- **El punch del 690** es suave (×1,13): la frase del «¡Listo!» no cabe más grande sin cortarse. Alternativa: un punch a ×1,4 sobre
  «¡Listo!» y «10 personas.» con la primera línea cortada, o regrabar con un nombre de casa más corto.
- **«Datos de ejemplo» roza el borde de «Volver a la lista»** en el plano final (720–839): es la posición que pidió el dueño; si molesta,
  `cierre` a ×1,2 deja «Volver a la lista» fuera.
- El salto del 150 es real y se ve como un corte; una regrabación con `ver` en pasos de desplazamiento suave lo haría deslizar.

## 8. Para 9:16

Cambiar en `index.html` las variables `--f-*` (1080×1920; márgenes 60; ceja 188 / 34 px; frase 236 / 960 / 104 px; ventana 60·480·960×850
con `--f-ventana-h: 850px`, `--f-ventana-hvis: 850px`, `--f-k: 0.820513`, `--f-grab-alto: 2077.54px`) y `window.KD` (ventana 960×850,
`cambio` escala 0,92 con origen «50% 0%» y x +36), la firma por `identidad/cierre-corto.html` y `data-width/height` de los hosts y de las
escenas; la frase 4 en tres líneas («Cada *reunión* / cuenta, / y cuenta bien»). Los tramos de video, los sonidos, los saltos compensados
y los tiempos no cambian: la cámara se recalcula sola con `enc()` y `comp()`. En 9:16 se ven 345 px CSS en G: revisar `formulario`
(la barra y los radios), `enviar` y `listo`, que en 4:5 usan casi los 439.
