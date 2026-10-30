# REVIEW · Clip del sitio: Membresía — «Valeria llegó el domingo» (4:5)

2026-10-30 · Construcción en HyperFrames 0.8.221 a partir de [SPEC.md](SPEC.md) (Historia A) con la grabación real
`assets/grabaciones/grabacion.mp4` (1170×2532, 30 fps, 113,2 s) y `pasos.json`. **Sin render final**: el dueño aprueba antes la vista previa.
Hay un borrador de baja calidad en `renders/borrador-1.mp4` (solo para medir la mezcla y comprobar los cuadros del video; no se publica).

## 1. Qué hay

| Archivo | Qué es |
|---|---|
| `index.html` | La raíz: el formato en un solo lugar (`--f-*` y `window.KD`), los hosts de las escenas, **la ventana a la app** con los dos mundos, los 25 tramos de video, los stills del iris, las marcas de toque, la cámara, el látigo, el cambio de ventana, el dip, la música y los 18 sonidos |
| `compositions/fondo.html` | La noche del sitio; el halo se asienta en 0, 180 y 720 |
| `compositions/frase-1.html` … `frase-4.html`, `ceja.html` | Las cuatro frases y la ceja, con sus entradas y salidas |
| `identidad/cierre-clip.html` | La firma del kit v1.1 (840–914), con el sonido de marca en 28,38 |
| `assets/stills/still-466.png`, `still-2401.png` | Los cuadros de la grabación que quedan debajo del iris del 120 y del 375 |
| `assets/audio/toque-b.wav`, `toque-c.wav` | Las tomas b y c de `toque` (±3 % de tono, como pide el SPEC cuando el kit trae una sola) |

Cómo abrir la vista previa: `npm run dev` en `clip-sitio-membresia/` (o `npx hyperframes@0.8.221 preview --background` y
`preview --status`). Hojas de contacto en `.hyperframes/artifacts/snapshots/` (ver §5).

## 2. Los planos, con sus cuadros

| Plano | Cuadros | Grabación (cuadros de `grabacion.mp4`) y cámara |
|---|---|---|
| P1 La puerta | 0–119 | 162–176 a 0,467× («Valeria»); 176–211 a 1,167×; 211–245 a 1,36× («Cardona Ríos»); corte; 274–279; 279–306 a 1,8× (el selector abierto); 306–315 a 3× (el chip); 315–318; corte; 458–467 (la app salta a «Registrar» en el 114). Cámara: G arriba (0–45), **46–59 → G sobre Apellidos y el selector (CSS 200–639)**, 108–119 → G sobre el diálogo y «Registrar» (CSS 311–750) |
| P2 Guardada aun sin señal | 120–185 | 526–528; corte; 533–561 (el diálogo entra 122–129); 616–628 («Entendido», el formulario se limpia); 674–690 (la app vuelve arriba en el 165: «1 sin enviar»); 791–799 (ya sin el contador). Iris 120–125 desde «Registrar». Cámara 150–163 → G arriba |
| Látigo | 176–186 | La tira sube 1100 px (`power3.inOut`, 10 cuadros, el más rápido en el 181); el mundo 2 aterriza 1,04 → 1,00 (180–190) |
| P3 La tarjeta | 180–374 | 2207–2402 a 1× (quieta; el cursor del buscador parpadea). Cámara: G (tope de abajo), 240–253 → M (mitad alta de la tarjeta), 300–313 → C («Después: Mensaje de bienvenida»), 345–359 → G |
| P4 El reporte | 375–599 | 2402; corte; 2411–2435 (el diálogo entra 377–381); corte; 2463–2513 («Contestó» en el 450); 2513–2515; 2519–2542 (el punto se llena en el 456); corte; 2561–2581; **2581–2663 a 1,139× («Muy contenta, viene el domingo», 501–566)**; corte; 2734–2767. Iris 375–380. Cámara: 390–403 → M pregunta, 480–493 → M Observaciones, 570–583 → M botones (×1,3) |
| P5 Cumplido | 600–719 | 2767–2770; corte; 2797–2894 (el resultado desde el 603); corte; 2912–2932. Cámara: 600–613 → M bloque del resultado (×1,35), 660–668 → punch ×1,5 a «Ahora va en: Mensaje de bienvenida» |
| P6 Que ninguna persona se pierda | 720–839 | 2932–3052 a 1× («Listo» en el 720, el diálogo se va 729, la tarjeta actualizada desde el 738). Cámara 720–733 → G⁺ (×1,05) sobre la tarjeta; la ventana a 0,92 y +48 px (724–738); dip 837–839 |
| P7 La firma | 840–914 | `cierre-clip` (fondo azul, llamado «prueba»); campanas en el 851 |

Cada corte de video cae dentro de una pausa de la grabación (`huecos_de_pantalla`), así que ningún corte se ve: solo cambia lo que la
app hace. Las velocidades quedan entre 0,467× y 3× (límite del SPEC 0,35×–3,5×).

## 3. Sincronía: cada cosa con su cuadro y su pulso

Pulsos de la pista (§0 del SPEC): múltiplos de 15 (el 285 real cae en el 284; no hay nada ahí). «Imagen» es el primer cuadro en que se ve;
el sonido cae un cuadro después de su imagen (regla del kit).

| Qué | Imagen (cuadro) | Pulso | Sonido (cuadro) | Desvío |
|---|---|---|---|---|
| «Valeria» puesta, la «V» en el campo | 0 | 0 | — | 0 |
| «llegó» | 15 | 15 | — | 0 |
| «el» · «Valeria» completo | 30 | 30 | — | 0 |
| «domingo.» | 45 | 45 | — | 0 |
| Toque en «Apellidos» (grab. 211) | 60 | 60 | `toque` a 61 | 0 |
| Toque en «Cómo llegó» (grab. 279); el selector abre 95–97 | 90 | 90 | `toque` b 91 | 0 |
| Toque en «Servicio General» (grab. 306) | 105 | 105 | — (como el SPEC) | 0 |
| El chip «Servicio General» aparece (grab. 315) | 108 | — | `aparicion` 109 | el SPEC lo pone en el 108 |
| La cámara baja y la app salta a «Registrar» (grab. 461) | 108–119 (salto en el 114) | — | `desliz` 109–120 (acento 115) | 0 |
| Frase 1 sale | 117–121 | — | — | 0 |
| **Toque en «Registrar» (grab. 526); iris** | **120** | **120 (bajo)** | `toque` c 121 (+3 dB) | 0 |
| «Guardada en este dispositivo» (entra 122–129); frase 2 entera | 122 / 120–126 | — | `confirmacion` 123 (+3 dB) | 0 |
| Toque en «Entendido» (grab. 616) | 150 | 150 | `toque` a 151 | 0 |
| «1 sin enviar» (grab. 677) | 165 | 165 | `aparicion` 166 | 0 |
| «1 sin enviar» desaparece (grab. 791) | 178 | — | — | 0 (SPEC: 178) |
| Frase 2 sale | 177–181 | — | — | 0 |
| **Látigo; el mundo 2 llega** | 176–186 (180) | **180 (pico)** | `desliz` 174–185 (acento 180, +3 dB) | 0 |
| Ceja «MEMBRESÍA» | 195 | 195 | `aparicion` 196 | 0 |
| Cámara → M tarjeta | 240–253 | 240 | — | 0 |
| Cámara → C «Después: …» | 300–313 | 300 | — | 0 |
| Cámara → G | 345–359 | 345 | — | 0 |
| Frase 3, palabra a palabra | 360 · 362 · 364 · 366 · 368 · 370 | 360 | — | 0 |
| **Toque en «Marcar cumplido» (grab. 2402); iris** | **375** | **375** | `toque` b 376 | 0 |
| «Reporte del paso» entra | 377–381 | — | — | — |
| Cámara → M «¿Cómo fue?» | 390–403 | 390 | — | 0 |
| Toque en «Contestó» (grab. 2513); el punto se llena en el 456 | 450 | 450 | `toque` c 451 | 0 |
| Cámara → M «Observaciones» | 480–493 | 480 | — | 0 |
| Toque en «Observaciones» (grab. 2581) | 495 | 495 | `toque` a 496 | 0 |
| «Muy contenta, viene el domingo» (teclas reales) | 501–566 | 510…555 | — (sin tics, como el SPEC) | el SPEC decía 497–555 |
| Cámara → M botones | 570–583 | 570 | — | 0 |
| Frase 3 sale | 597–601 | — | — | 0 |
| **Toque en «Marcar cumplido» del diálogo (grab. 2767)** | **600** | **600 (2.ª subida)** | `toque` b 601 (+3 dB) | 0 |
| El resultado «“Llamada de bienvenida” cumplido · Ahora va en: …» (grab. 2797) | 603 | — | `confirmacion` 603 (+3 dB) | 0 |
| Cámara → M resultado | 600–613 | 600 | — | 0 |
| **Punch → «Ahora va en: Mensaje de bienvenida»** | 660–668 | **660 (golpe)** | — | 0 |
| **Toque en «Listo» (grab. 2932)**, fuera de encuadre | **720** | **720 (golpe)** | `toque` c 721 | 0 (no se dibuja: §4) |
| Frase 4, palabra a palabra; la ceja sale | 720 · 722 · 724 · 726 · 728 / 720–723 | 720 | — | 0 |
| Cámara → G⁺ tarjeta; la ventana a 0,92 | 720–733 / 724–738 | — | — | 0 |
| El diálogo se va; la tarjeta ya dice «Mensaje de bienvenida» | 729 / 738 | — | — | — |
| `subida` | — | — | 796–853 (golpe 840) | 0 |
| Dip | 837–839 | — | — | 0 |
| **La firma** | **840** | **840 (el más fuerte)** | música 1,00 → 0,32 (852) → 0 (870); campanas 851 | 0 |

Ninguna acción cae a más de 1 cuadro de su pulso. La escritura del comentario termina en el 566 (el SPEC decía 555) porque usa las 30
teclas reales a 1,139×; la cámara no se mueve hasta el 570.

## 4. Desvíos del SPEC y su porqué

1. **La cámara se mueve una vez más, 46–59 (compás 1).** El selector «Cómo llegó» se abre *debajo* del campo (CSS 495–650) y el toque
   en «Servicio General» cae en CSS 525: desde el encuadre de arriba (0–439) no se verían ni el selector ni el toque del 105. La cámara
   baja a 200–639 mientras «el dedo viaja a Apellidos» (30–45 del SPEC), y el compás 2 conserva su único movimiento (108–119).
2. **El chip «Sin conexión: ves la última copia» no se ve.** Vive bajo el título «Nueva persona», en lo alto de la página, y solo existe
   en los cuadros 403–460 de la grabación, con la página arriba. En esos cuadros la cámara tiene que estar en 200–750 para los toques
   del 105 y del 120; después, la app se desplaza y el chip se va de la pantalla. Lo «sin señal» lo dicen la frase 2, el diálogo
   («se envía sola cuando haya señal») y «1 sin enviar».
3. **El desplazamiento a «Registrar» no es suave:** la grabación salta en un cuadro (460 → 461). El salto cae en el 114, el cuadro más
   rápido del movimiento de cámara 108–119, con el `desliz` encima: se lee como parte del mismo movimiento.
4. **Encuadres recalculados con las cajas reales**: G sobre el diálogo «Guardada» (CSS 310–537) y «Registrar» (708–748) caben justos
   (311–750); la tarjeta de Valeria no puede quedar a 24 px del borde porque debajo de ella solo quedan 96 px CSS de app (la barra
   inferior): el G del mundo 2 es el tope de abajo (CSS 405–844), y la tarjeta queda a 137 px del borde superior de la ventana.
5. **«Ahora va en: Mensaje de bienvenida» mide 247 px CSS** (el SPEC calculaba C para 217): el punch del 660 va a **×1,5** (texto ≈ 51 px,
   la línea cabe con 6 px de margen) y centrado en el bloque ícono + «cumplido» + línea; **«Listo» queda fuera del encuadre** (no cabe
   con la línea a ningún aumento mayor que ×1,32). Por eso el toque del 720 **se oye pero no se dibuja**, y lo que se ve en el golpe es
   el diálogo que se cierra y la cámara que vuelve a la tarjeta. El resultado del 600 va a ×1,35 (a 1,4 se cortaba «Listo»), y los
   botones del diálogo (570) a ×1,3 (a 1,4 se cortaban «Cancelar» o «Marcar cumplido»).
6. **La espera de la app se recorta en vez de mostrarse:** tras «Marcar cumplido» la app atenúa el diálogo 23 cuadros antes del
   resultado (2774–2796); el clip corta 2770 → 2797 y el resultado aparece en el 603, con la `confirmacion`. Lo mismo con «Guardada»
   (528 → 533) y con «Reporte del paso» (2403 → 2411): los diálogos entran 2 cuadros después del toque, dentro del iris.
7. **Las entradas de texto arrancan un cuadro antes del pulso** (el tween de 4 cuadros con `power4.out` está al 68 % en el pulso): así el
   primer cuadro visible de cada palabra es el pulso. Las salidas van como el SPEC (2–3 cuadros antes).
8. **Niveles de los sonidos:** el kit calibra sus sonidos para quedar 4–10 dB *por debajo* de la música a `data-volume="1"`; el «+3 dB
   sobre la cama» del SPEC pediría +13 dB y recortaría. Se usa el nivel del kit, con +3 dB (1,4) en los dos toques clave (121 y 601),
   en las dos `confirmacion` y en el `desliz` del látigo.
9. **La música** va sin `data-volume` y con su nivel (0,7) dentro del carril de volumen: 0,7 → 0,224 (28,4) → 0 (29,0). Así vale igual
   si el carril reemplaza la ganancia o la multiplica (la documentación no lo dice).
10. **El látigo es una sola tira** con `power3.inOut` (176–186) en vez de dos curvas (salida `power3.in` 5 cuadros + llegada `power3.out`
    6 cuadros): con las dos curvas el cuadro 181 mostraba la ventana vacía entre los dos mundos; con la tira nunca hay hueco.
11. **La firma dura 2,5 s** (pieza aprobada del kit): `check` avisa que «Kingdom» (1,67 s) y «Prueba gratis 30 días» (1,5 s) duran
    menos de los 2 s que pide la regla general. Se deja como está: es la firma de toda la serie.
12. **«Datos de ejemplo» a 31 px** (el kit trae 28): con la ventana a 0,92 quedaba en 26 px, bajo el piso de lectura.

## 5. Lo que se revisó y lo que se midió

- `npx hyperframes check --json`: **0 errores**, 4 avisos: `composition_file_too_large` (la raíz lleva los 25 tramos de video a propósito,
  para que se vean y se puedan recortar en la línea de tiempo), `text_below_floor` (corregido, §4.12), `line_unread` ×2 (§4.11).
- `npx hyperframes snapshot --review`: `.hyperframes/artifacts/snapshots/9c859e39-…/review-beats-{1,2,3}.jpg`, `review-seam-01…32.jpg`,
  `review-phone-{1,2,3}.jpg`. Cuadros clave del SPEC §4 (`--at 0,1.5,3.6,4.0,4.2,5.5,6.0,6.2,8.5,10.5,12.5,13.3,15.1,18,20.0,20.1,22.3,24.0,
  24.5,27.9,28.0,28.4,30.4`): `.hyperframes/artifacts/snapshots/a37b26e2-…/contact-sheet-{1,2,3}.jpg`. El látigo cuadro a cuadro
  (`--range 5.8,6.3 --frames 16`): `.hyperframes/artifacts/snapshots/00b8a25a-…/contact-sheet-{1,2}.jpg`. Las hojas que se hagan después
  de la corrección del cuadro 0 (§6) quedan en carpetas nuevas de la misma ruta.
- Mirado en las hojas: el cuadro 0 con «Valeria», la ventana y «Datos de ejemplo»; las cuatro palabras quietas en el 45; el iris desde
  «Registrar» y el diálogo entero en el 129; «1 sin enviar» en el 165; el látigo sin ningún cuadro con la ventana vacía; la ceja en el
  195; M y C sobre la tarjeta (texto ≥ 44 y ≥ 50 px); la frase 3 sobre la tarjeta quieta; «Reporte del paso» desde el toque; «Contestó»
  marcado; la escritura a ≥ 44 px con la cámara quieta; el resultado con el ícono; la línea «Ahora va en» a ≈ 51 px; la frase 4 con
  *ninguna* dorada y la ventana a 0,92; el dip; el primer cuadro de la firma sin noche vacía; la hoja del celular (360 px) legible.
- **La mezcla (medida, no oída):** la cama sola, 14,05–42,05 s con 0,7, da **−17,9 LUFS** (pico −6 dBFS). El borrador
  `renders/borrador-1.mp4`: ver §6 (integrada, pico real y los golpes de los sonidos con `npx hyperframes audio`). La salida final a
  −16 LUFS / −1 dBTP se deja a `npx hyperframes normalize-audio` sobre el render de entrega, que no se ha hecho.
- Nadie oyó el sonido; nadie vio el movimiento a velocidad real salvo en el borrador.

## 6. El borrador y lo que falta mirar en la vista previa

**`renders/borrador-1.mp4`** (`-q draft`, 4,4 MB, 915 cuadros, 30,5 s; hecho antes de la corrección del cuadro 0, así que sus cuadros 0–2
no traen la «V»; lo demás es igual). Sirvió para tres cosas:

1. **El extractor de cuadros atrasa ~2 cuadros en los tramos a menos de 1×** (en el borrador la «V» aparecía en el 3; en snapshot, en
   el 2) y es exacto a 1× (el salto de la app cae en el 114, el toque de «Registrar» en el 120 y «1 sin enviar» en el 165, al cuadro).
   Corregido en `v01` (arranca en 164,0 en vez de 162,3) y `v02` (1,11×): en la vista previa el cuadro 0 ya muestra la «V».
2. **La mezcla, medida:** integrada **−17,7 LUFS** (ffmpeg ebur128; `hyperframes audio` da −17,6), pico real **−1,4 dBTP**, sin recortes,
   LRA 2,0 LU. `hyperframes audio` detecta los golpes en **2,03 · 3,03 · 4,03 · 5,03 · 12,53 · 15,03 · 16,53 · 20,03 · 24,03 s** = cuadros
   61 · 91 · 121 · 151 · 376 · 451 · 496 · 601 · 721: cada `toque` un cuadro después de su imagen. Sonoridad momentánea: −19,6 en 1,0 s;
   −14,7 en 4,03 (bajo + toque + confirmación); −15,2 en 6,0 (látigo); −15,3 en 20,03; −14,3 en 28,1 (golpe + `subida`); −19,5 en 28,4
   (la música ya a −10 dB, las campanas empiezan); −17,1 en 29,0; −21,8 en 29,5; −31,8 en 30,3 (solo la cola de las campanas). La firma
   (28–30,5) queda en −19,7 LUFS. **Para la entrega:** `normalize-audio` a −16 LUFS sube ≈ +1,7 dB y el pico real llegaría a +0,3 dBTP, así
   que el normalizador tendrá que limitar (o se bajan a 1,0 los refuerzos de 1,4 de los toques clave): decidirlo sobre el render final.
3. Los pulsos de las palabras y la ceja, el encuadre de los botones (×1,3) y el cuadro 0 se volvieron a mirar en snapshot después de las
   correcciones: `.hyperframes/artifacts/snapshots/bfa55e44-…/contact-sheet-{1,2}.jpg` (0 · 0,033 · 0,5 · 0,967 · 1,0 · 1,467 · 1,5 · 3,967 ·
   4,0 · 6,467 · 6,5 · 11,967 · 12,0 · 12,333 · 19,5 · 23,967 · 24,0 · 24,267). Las hojas de `--review` regeneradas con la versión final
   están en la carpeta más nueva de `.hyperframes/artifacts/snapshots/`.

`check` después de las correcciones: **0 errores**, 3 avisos (`composition_file_too_large`, `line_unread` ×2; §4.11).

**Lo que el dueño debe mirar en la vista previa** (a velocidad real, que nadie vio):

- 0–4 s: si «Valeria» a 0,47× se siente lenta y si el tramo 105–120 (chip, bajada de cámara, salto a «Registrar», toque) va atropellado.
- 4,0: el iris desde «Registrar» y el diálogo que entra 2 cuadros después; 5,5: «1 sin enviar».
- 5,9–6,2: el látigo (un solo barrido; el mundo 2 aterriza con un leve exceso de 1,04).
- 8,0–12,0: los tres movimientos de cámara sobre la tarjeta (M, C y vuelta) y la ceja.
- 16,5–19: la escritura a ≥ 44 px con la cámara quieta.
- 20,0: «Marcar cumplido» → el resultado en 3 cuadros con la confirmación; 22,0: el punch a «Ahora va en: Mensaje de bienvenida» (con
  el título «Reporte del paso» cortado a la izquierda: §7).
- 24,0: el golpe con «Listo» fuera de encuadre, la frase 4 con *ninguna* dorada, la ventana que se hace a un lado y la tarjeta ya en
  «Mensaje de bienvenida» (24,6).
- 27,9–28,4: el dip, el corte a la firma y las campanas.
- El sonido completo: si los toques del kit se oyen (están 7–10 dB bajo la música) o conviene subirlos.

## 7. El plano más débil y qué cambiaría con más tiempo

- **660–720**: el punch a «Ahora va en» corta el título «Reporte del paso» por la izquierda (es un acercamiento real, pero el texto cortado
  en el borde es la única arista del clip) y «Listo» no se ve tocarse. Alternativa si al dueño le molesta: quedarse en M (×1,35) con el
  bloque entero y hacer del 660 un acercamiento de 9 cuadros a ×1,4 (más suave, con «Listo» a la vista y el toque dibujado).
- **105–120** sigue siendo el tramo más apretado: chip, cámara, salto de la app y toque en medio segundo. Si en la vista previa va
  atropellado, la válvula del SPEC (P1) sigue abierta: elegir «Cómo llegó» antes del cuadro 0 y dejar el compás 2 para «Apellidos» y el
  desplazamiento (pide regrabar o tomar «Servicio General» ya elegido desde el cuadro 318).
- Los stills del iris son PNG de 1170×2532 (0,5–0,8 MB); si pesan en la vista previa, se bajan a WebP.

## 8. Para 9:16

Cambiar en `index.html` las variables `--f-*` (1080×1920; márgenes 60; ceja 188 / 34 px; frase 236 / 960 / 104 px; ventana 60·480·960×850
con `--f-ventana-hvis: 850px`, `--f-k: 0.820513`, `--f-grab-alto: 2077.54px`, `--f-latigo: 1000px`) y `window.KD` (ventana 960×850,
`latigo` 1000, `cambio` escala 0,92 con origen «50% 0%» y x +36), la firma por `cierre-corto`, y `data-width/height` de los hosts y de las
escenas. Los tramos de video, los sonidos, las cajas de la cámara y los tiempos no cambian: la cámara se recalcula sola con `enc()`.
