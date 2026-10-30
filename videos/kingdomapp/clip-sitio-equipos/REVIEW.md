# REVIEW · Clip del sitio: Equipos — «Falta uno en Parqueadero» (4:5)

2026-10-30 · Construcción en HyperFrames 0.8.221 a partir de [SPEC.md](SPEC.md) con la grabación real `assets/grabaciones/grabacion.mp4`
(1170×2532, 30 fps, 65,23 s, sin círculo de toque) y `pasos.json`. Plantillas: [Eventos](../clip-sitio-eventos/REVIEW.md) (tramos, `enc()`,
marcas, niveles de mezcla) y [Membresía](../clip-sitio-membresia/REVIEW.md) (el látigo en una sola tira). El dueño ya no revisa: construido,
verificado y renderizado sin paradas. **Entrega:** `renders/clip-sitio-equipos-4x5.mp4`.

## 1. Qué hay

| Archivo | Qué es |
|---|---|
| `index.html` | La raíz: el formato en un solo lugar (`--f-*` y `window.KD`), los hosts de las escenas, **la ventana con la tira de dos mundos**, los 24 tramos de video, los dos stills, las 8 marcas de toque, las cuatro cámaras, los dos iris, los dos látigos, el cambio de ventana, el dip, la música y los 20 sonidos |
| `compositions/fondo.html` | La noche del sitio; el halo se asienta en 0, 180 y 720 |
| `compositions/frase-1.html` … `frase-4.html`, `ceja.html` | Las cuatro frases y la ceja «EQUIPOS», con sus entradas y salidas |
| `identidad/cierre-clip.html` | La firma del kit v1.1 (840–914), `{"llamado":"prueba","fondo":"azul","idioma":"es"}`, campanas en 28,38 |
| `assets/stills/still-362.png` | El cuadro del toque en «Asignar» (grab. 362), debajo del iris del 120 |
| `assets/stills/still-1132.png` | El cuadro del toque en la tarjeta (grab. 1132), debajo del iris del 375 |
| `assets/audio/toque-b.wav`, `toque-c.wav` | Las tomas b y c de `toque` (±3 % de tono), copiadas de Eventos |

Estructura de la ventana (nueva respecto de Eventos, para que el iris nazca donde se tocó):

```text
#ventana.k-ventana
  #tira                      ← el látigo: sube 1100 px en 356–366, baja en 656–666
    #m1.mundo (top 0)        ← el celular de Jorge (103), recorta lo suyo
      #m1in                  ← aterrizajes: match cut 78 (1,03 → 1) y vuelta 660 (1,04 → 1)
        #cam1                ← la cámara antes del iris: tramos 0–121, still 121–127, marcas 75 y 120
        #iris1 > #cam1b      ← el iris en px de la ventana (nace donde estaba «Asignar»); dentro, la cámara ya en el encuadre nuevo
    #m2.mundo (top 1100)     ← el celular de Gabriela (105)
      #m2in > #cam2 · #iris2 > #cam2b   (lo mismo, con el iris del 375 desde la tarjeta)
  #datos · #dip
```

Los tramos, las marcas y los sonidos de `index.html` salen de una tabla (`gen.py` en el scratchpad del agente, como en Eventos); se pueden
editar a mano. Vista previa: `npm run dev` (o `npx hyperframes@0.8.221 preview --background`; se abrió para revisar y quedó detenida).

## 2. Los planos, con sus cuadros

«grab.» = cuadro de `grabacion.mp4`. **Todos los tramos a 1×** (no hizo falta ninguna rampa: el desfase del extractor por debajo de 1× no
aplica).

| Plano | Cuadros | Grabación y cámara |
|---|---|---|
| P1 ¿Quién cubre el domingo? | 0–119 | grab. 81–158: el calendario ya desplazado al domingo (el desplazamiento real es un salto en la grab. 41, que queda fuera), toque en la fila en el 75 = grab. 156; **match cut** (el esqueleto 163–168 fuera) a grab. 169–210, el turno, con el aterrizaje 1,03 → 1,00 en 78–88. Cámara: M `semana` (×1,4, CSS 16–295 × 334–646) · 46–59 → C `porCubrir` (×1,8, CSS 17–233 × 328–572) · 78 corte a ×1,15 `turnoCabeza` (CSS 6–346 × 54–436) · 90–103 → G⁺ `parqueadero1` (CSS 14–376 × 237–643). La marca espera sobre «Asignar» desde el 105 |
| P2 Kingdom sugiere a quién poner | 120–179 | grab. 362 (el toque); **iris** 120–125 desde «Asignar» con el still de la grab. 362 debajo; dentro, grab. 379–407 (el diálogo ya puesto; su fundido y su esqueleto 363–378 fuera) en ×1,15 `sugerencias` (CSS 25–365 × 79–461); grab. 463 (toque en la casilla, 150); corte en la onda (464→470): la fila de Gabriela llena y «Asignar (1)» desde el 151 (grab. 470–498). Cámara 165–178 → G `pie` (CSS 345–784) |
| P3 Avisar | 180–355 | grab. 524 (toque en «Asignar (1)», 180); corte en la espera (525→539): el diálogo ya no está, 181–182 (grab. 539–540); en el 183 Gabriela «Sin avisar» y la barra «1 asignación sin avisar · Avisar a 1 persona» (grab. 542–598); grab. 689–690 (toque en «Avisar a 1 persona», 240); **corte en la espera y la K del cargador** (691→717): «Avisados» entero desde el 242 (grab. 717–774); grab. 805 (toque en «Entendido», 300); corte en el fundido (806→815): 301–302 sin diálogo, todavía «Sin avisar» (grab. 815–816); en el 303 «Por confirmar» y sin la barra (grab. 819–882). Cámara: 210–223 → ×1,25 `avisar` (CSS 16–328 × 429–780) · 240–253 → G⁺ `avisados` (CSS 14–376 × 219–625) · 300–313 → M `parqueadero2` (CSS 16–295 × 284–597) |
| P4 Y sabe a qué hora llegar | 356–599 | **Látigo de ida** 356–366 (el cambio de cuenta 910–993 fuera); Mi iglesia de Gabriela, grab. 1113–1131 en G `tarjeta` (CSS 56–495); grab. 1132 (toque en la tarjeta, 375); **iris** 375–380 con el still de la grab. 1132 debajo; dentro, grab. 1144–1217 (su servicio; el esqueleto 1141 fuera) en M `servicioCabeza` (CSS 21–300 × 105–418); **450: la app baja a «Instrucciones» en un cuadro** (grab. 1270, salto real) y sigue en grab. 1270–1359; **540: la app vuelve arriba en un cuadro** (grab. 1392, salto real), grab. 1392–1451. Cámara: 390–403 → C `llegada` (CSS 22–238 × 103–347) · 420–433 → G `servicio` · 480–493 → ×1,04 `paleta` (CSS 8–383 × 257–679) · 570–583 → G⁺ `botones` (CSS 14–376 × 169–575). Quieta en 450 y 540 |
| P5 Aceptar | 600–655 | grab. 1469–1470 (toque en «Aceptar», 600); **corte en la espera** (1471→1484): quedan fuera los botones apagados (1476) y el aviso «Tu respuesta quedó guardada: sale al volver la señal» que la app muestra un instante (1477–1481); en el 602 «¡Gracias por servir! Tu líder ya lo sabe.», «Confirmado» y «Ya no puedo» (grab. 1484–1548). Cámara quieta en `botones` |
| P6 Tu líder ya lo sabe | 656–719 | **Látigo de vuelta** 656–666 (el cambio de cuenta 1609–1647 fuera): el turno del líder recién abierto, grab. 1660–1843, en el mismo encuadre `parqueadero2` en que el mundo 1 se quedó en el 313, con «Confirmado» donde decía «Por confirmar». **Retroceso** 690–698 → ×1,2 `cierre` (CSS 14–339 × 179–545): aparecen «9:00 a. m.» y «5 de 5» |
| P7 Que cada puesto de servicio esté cubierto | 720–839 | El mismo tramo, quieto. La ventana a 0,92 y +48 px en 724–738; dip 837–839 |
| P8 La firma | 840–914 | `cierre-clip` (fondo azul, llamado «prueba»); campanas en el 851 |

## 3. Sincronía: cada cosa con su cuadro y su pulso

Pulsos de la pista (SPEC §0): múltiplos de 15 (el 285 real cae en el 284; no hay nada ahí). «Imagen» es el primer cuadro en que se ve; el
sonido cae un cuadro después (`data-start` = cuadro del sonido / 30 − acento). **Los cuadros de imagen se comprobaron en el render final**
(los 915 cuadros extraídos con ffmpeg y mirados en hojas alrededor de cada toque, corte, iris y látigo), y los sonidos con
`hyperframes audio` sobre el render.

| Qué | Imagen | Pulso | Sonido | Desvío |
|---|---|---|---|---|
| «¿Quién» puesta (la miniatura) | 0 | 0 | — | 0 |
| «cubre» · «el» · «domingo?» | 15 · 30 · 45 | 15 · 30 · 45 | — | 0 |
| Cámara → `porCubrir` | 46–59 | 45 (compás 1) | — | +1 (como el SPEC) |
| **Toque en la fila del domingo** (grab. 156) | 75 | 75 | `toque` a 76 | 0 |
| Match cut: el turno entra 1,03 → 1,00 | 78–88 | — | — | 0 (SPEC 78) |
| Cámara → `parqueadero1` | 90–103 | 90 | — | 0 |
| La marca se posa sobre «Asignar» y espera | 105 | 105 | — | 0 |
| Frase 1 sale | 117–121 | — | — | 0 |
| **Toque en «Asignar»** (grab. 362); iris | 120 / 120–125 | **120 (bajo)** | `toque` c 121 | 0 |
| El diálogo «Asignar · Parqueadero» con la lista sugerida | 121 | — | — | +1 (dentro del iris que nace en el pulso) |
| Frase 2 entera | 120–126 | 120 | — | 0 |
| **Toque en la casilla de Gabriela** (grab. 463) · la fila se llena, «Asignar (1)» | 150 · 151 | 150 | `toque` a 151 | 0 |
| Cámara → `pie` | 165–178 | 165 | — | 0 |
| Frase 2 sale | 177–181 | — | — | 0 |
| **Toque en «Asignar (1)»** (grab. 524) · el diálogo se va | 180 · 181 | **180 (pico)** | `toque` b 181 | 0 |
| Gabriela «Sin avisar» y la barra «Avisar a 1 persona» | 183 | — | `aparicion` 184 | 0 (SPEC 183) |
| Ceja «EQUIPOS» | 195 | 195 | `aparicion` 196 | 0 |
| Cámara → `avisar` | 210–223 | 210 | — | 0 |
| **Toque en «Avisar a 1 persona»** (grab. 689) · cámara → `avisados` | 240 · 240–253 | 240 | `toque` c 241 | 0 |
| «Avisados · Le llegó el aviso a 1 persona…» | 242 | — | `confirmacion` 243 (1,0) | 0 (SPEC 243) |
| **Toque en «Entendido»** (grab. 805) · el diálogo se va · cámara → `parqueadero2` | 300 · 301 · 300–313 | 300 | `toque` a 301 | 0 |
| Gabriela «Por confirmar», sin la barra | 303 | — | `aparicion` 304 | 0 |
| **Látigo de ida** (el más rápido en el 361); Mi iglesia de Gabriela aterriza 1,04 → 1,00 | 356–366 / 360–370 | **360** | `desliz` 1,4, acento 360 | 0 |
| Frase 3, palabra a palabra | 360 · 362 · 364 · 366 · 368 · 370 | 360 | — | 0 |
| **Toque en la tarjeta «Tu próximo servicio»** (grab. 1132); iris; su servicio | 375 / 375–380 / 376 | 375 | `toque` b 376 | 0 |
| Cámara → `llegada` («Llega a las 7:45 a. m.» a 57 px) | 390–403 | 390 | — | 0 |
| Cámara → `servicio` | 420–433 | 420 | — | 0 |
| La app baja a «Instrucciones» (grab. 1270), cámara quieta | 450 | 450 | `desliz`, acento 451 | 0 |
| Cámara → `paleta` (Negro · Azul oscuro · Gris y el cronograma) | 480–493 | 480 | — | 0 |
| La app vuelve arriba (grab. 1392), cámara quieta | 540 | 540 | `desliz`, acento 541 | 0 |
| Cámara → `botones` | 570–583 | 570 | — | 0 |
| La marca sobre «Aceptar» · frase 3 sale | 596 · 597–601 | — | — | 0 |
| **Toque en «Aceptar»** (grab. 1469) | 600 | **600 (2.ª subida)** | `toque` c 601 | 0 |
| «¡Gracias por servir! Tu líder ya lo sabe.», «Confirmado», «Ya no puedo» (grab. 1484) | 602 | — | `confirmacion` 603 (1,4) | 0 |
| **Látigo de vuelta** (el más rápido en el 661); el turno del líder aterriza 1,04 → 1,00 | 656–666 / 660–670 | **660 (golpe)** | `desliz` 1,4, acento 660 | 0 |
| Gabriela «Confirmado» entra entera en la ventana | 661 | — | `confirmacion` 662 (1,0) | 0 (SPEC 663, ver §4.8) |
| Retroceso → `cierre`: «5 de 5» | 690–698 | 690 | — | 0 |
| Frase 4, palabra a palabra; la ceja sale | 720 · 722 · … · 732 / 720–723 | **720 (golpe)** | — | 0 |
| La ventana a 0,92 y +48 | 724–738 | — | — | 0 |
| `subida` | — | — | 796–853 (golpe en el 841) | 0 |
| Dip | 837–839 | — | — | 0 |
| **La firma** | **840** | **840 (el más fuerte)** | música 0,75 → 0,24 (852) → 0 (870); campanas 851 | 0 |

**Ninguna acción cae a más de 1 cuadro de su pulso.** Las dos de +1 (la cámara del compás 1 y el diálogo del 121) son las del SPEC: la
cámara arranca después del último aterrizaje de la frase y el diálogo aparece dentro del iris que nace en el pulso. `hyperframes audio`
detecta los golpes en **2,53 · 4,03 · 5,03 · 6,03 · 8,03 · 10,03 · 12,53 · 20,03 s** = cuadros 76 · 121 · 151 · 181 · 241 · 301 · 376 · 601:
los 8 `toque`, cada uno un cuadro después de su imagen.

## 4. Desvíos del SPEC y su porqué

1. **Lo que la grabación cambió** (pedido): el diálogo del aviso dice **«Entendido»**, no «OK»; Gabriela ve **«Buenas tardes, Gabriela»**
   (la hora de la grabación); el calendario tiene arriba el aviso verde **«Tienes 6 asignaciones sin avisar: nadie las ha visto todavía.»**
   (real, de la semilla): los encuadres `semana` y `porCubrir` lo dejan fuera; el turno muestra «9:00 a. m. · Carrera 70 # 44-20,
   Laureles» y el chip «4 de 5» → «5 de 5». Ninguna frase depende de eso.
2. **Los desplazamientos de la app son saltos de un cuadro** (grab. 41, 1270 y 1392), no los 300 ms suaves del SPEC. El de la 41 (el
   calendario al domingo) queda fuera: el clip arranca ya desplazado. Los otros dos son «la app baja a las instrucciones» (450) y «vuelve
   arriba» (540) del SPEC: se dejan ver en su pulso, con su `desliz` y la cámara quieta (como el salto del 150 de Eventos). No hizo falta
   compensar ningún salto con la cámara (`comp()`): ninguno es accidental.
3. **Las esperas de la app se cortan:** el esqueleto del turno (163–168), el fundido y el esqueleto del diálogo «Asignar» (363–378), la
   onda de la casilla (464–469), el cierre del diálogo (525–538), **la K del cargador** después de «Avisar» (703–706) y el fundido de
   «Avisados» (707–716), el fundido del cierre de «Avisados» (806–814), el esqueleto del servicio de Gabriela (1133–1143) y, después de
   «Aceptar», los botones apagados (1476) y **el aviso de guardado sin señal** «Tu respuesta quedó guardada: sale al volver la señal»
   (1477–1481), que la app muestra un instante con la API local y contradice la historia. Cada acción visible cae en su pulso, con su
   marca y su sonido.
4. **El iris nace donde se tocó, en la pantalla.** En Eventos el círculo vivía dentro de la cámara; aquí la cámara salta a un encuadre nuevo
   dentro del iris (SPEC §1.6), y con el círculo dentro de la cámara habría nacido en otro lugar que el dedo. Por eso cada mundo tiene dos
   cámaras (`#cam1` antes del iris, `#cam1b` dentro) y el recorte del iris va en px de la ventana (§1).
5. **Encuadres recalculados con las cajas reales** (las del SPEC eran estimaciones). El texto de la app va de x 16 a x 374: en M (×1,4,
   279 px CSS) no cabe una fila entera, así que `turnoCabeza` es ×1,15, `parqueadero1` G⁺ (el botón «Asignar» llega a x 374), `sugerencias`
   ×1,15, `avisados` y `botones` G⁺, `paleta` ×1,04 (a ×1,08 «Colores» y las horas del cronograma tocaban el borde) y `tarjeta` G (para que
   el aterrizaje 1,04 del látigo no corte «Buenas tardes»). `semana` (la miniatura) sí es M: el chevrón queda fuera, pero «1 por cubrir» se
   lee a 35 px. `parqueadero2` es M (los chips «Por confirmar» y «Confirmado» a 35 px).
6. **«Datos de ejemplo» manda en el plano final.** La píldora está fija abajo a la izquierda (pedido del dueño) y en el `cierre` de
   ×1,14 del SPEC caía sobre el chip «Confirmado» de Gabriela. `cierre` es ×1,2 desde «9:00 a. m.»: **«Servicio General» queda fuera** del
   plano final (se vio en 78–89); «5 de 5», los dos botones, Parqueadero «2 de 2», Rut y Gabriela «Confirmado» quedan por encima de la
   píldora. El chip «5 de 5» (11 px CSS) queda en ~27 px con la ventana a 0,92, uno por debajo del piso de 28; los nombres y «Confirmado»
   en 30–37.
7. **Las marcas de toque que quedarían sobre otra pantalla** (75, 120, 180, 240, 300, 375, 600) se van con el corte en vez de seguir 6
   cuadros, como en Eventos.
8. **La `confirmacion` de «Confirmado» va en el 662, no en el 663:** la fila de Gabriela entra entera en la ventana en el 661 (el cuadro
   más rápido del látigo) y la regla es imagen + 1.
9. **El sonido:** los tres toques clave (121, 181 y 601) van a **1,0**, no a 1,4: con 1,4 el pico real pasaba de −1 dBTP en
   Eventos (su REVIEW §5). Se mantienen a 1,4 los dos `desliz` de los látigos y la `confirmacion` del 603. La música va a **0,75** (el nivel
   que en Eventos dio −17 LUFS sin normalizar).
10. **La firma dura 2,5 s** (pieza aprobada del kit): `check` avisa que «Kingdom» (1,67 s) y «Prueba gratis 30 días» (1,5 s) duran menos de
    2 s. Se deja: es la firma de toda la serie (igual que en Membresía y Eventos).

## 5. La mezcla (medida, no oída)

Render final: **−17,1 LUFS integrados, pico real −2,7 dBTP** (ffmpeg `ebur128` y `hyperframes audio` coinciden), sin recortes, LRA 2,2 LU,
sonoridad de corto plazo máxima −15,5. El render no tuvo que bajar nada. Con un solo toque clave por compás (Eventos tenía confirmación y
toque a 1,4 juntos), el pico quedó con 1,7 dB de margen sobre −1 dBTP.

## 6. Lo que se revisó

- `npx hyperframes check --json`: **0 errores**, 3 avisos: `composition_file_too_large` (la raíz lleva los 24 tramos de video a propósito,
  para que se vean y se recorten en la línea de tiempo, como Eventos) y `line_unread` ×2 (§4.10).
- `npx hyperframes snapshot --review`: `.hyperframes/artifacts/snapshots/15d6d9b2-719b-46f9-a38f-9912cb143a8b/` (`review-beats-{1,2,3}.jpg`,
  `review-seam-*.jpg`, `review-phone-{1,2,3}.jpg`). Notas que salieron de las hojas, ya corregidas: «Domingo», «Servicio General» y
  «Buenas tardes» cortados por el borde izquierdo con el aterrizaje (P1, `turnoCabeza` y `tarjeta`); el aviso verde del calendario cortado
  arriba en `porCubrir` (P2); «Mis servicios» cortado arriba en `servicioCabeza` (P2); «Colores» y las horas del cronograma en el borde
  (P2, `paleta`); la miniatura con «1 por cubrir» a 26 px (P1, `semana` pasó a M). Abierta a propósito (P2): en 119–121 la frase 1 sale y la
  frase 2 entra en el mismo lugar con desenfoque (el «blur swap» del SPEC).
- Cuadros clave en la vista previa (51 + 45, a mitad de cuadro: `(n + 0,3) / 30`, porque `--at` redondea a milésimas y `4,033` cae en el
  cuadro 120, no en el 121).
- **El render final cuadro a cuadro** (extraído con ffmpeg): cada toque con su marca en su pulso; el turno en el 78; el diálogo en el 121;
  la fila llena en el 151; el diálogo fuera en el 181 y la barra en el 183; «Avisados» en el 242; «Por confirmar» en el 303; los dos
  látigos sin un cuadro con la ventana vacía ni con la pantalla de carga de la cuenta (el hueco de 50 px entre mundos es el fondo de la
  app); los saltos del 450 y del 540 con la cámara quieta; «¡Gracias por servir!» en el 602 sin el aviso de guardado; «Confirmado» en el
  661; «5 de 5» en el 699; la firma en el 840.
- Mirado: el cuadro 0 (el domingo con «4 de 5 · 1 por cubrir», «¿Quién», «Datos de ejemplo»); ninguna frase sobre la app; la frase 4 con
  *cubierto* dorada; el primer cuadro de la firma sin noche vacía.
- Nadie oyó el sonido ni vio el movimiento a velocidad real fuera del render.

## 7. El plano más débil y qué cambiaría con más tiempo

- **181–182:** al cerrarse el diálogo, la app muestra dos cuadros el puesto todavía «Vacante» con «Asignar» antes de poner a Gabriela «Sin
  avisar» (183). Es la app real y dura 66 ms, pero puede leerse como un parpadeo hacia atrás. Alternativa: cortar directo de la grab. 524 a
  la 542 en el 181 (la barra y la fila juntas con el pico; la `aparicion` pasaría al 182).
- **El plano final no muestra «Servicio General»** (§4.6). Si se quiere el título, la píldora tendría que ir a la derecha o la ventana a
  0,92 desde otro origen; las dos cosas tocan el sistema de la serie.
- **«5 de 5» a ~27 px** en el plano final. Un `cierre` más cerrado lo sube, pero entonces Gabriela queda bajo la píldora.
- **Los saltos de 450 y 540** se ven como cortes, no como desplazamientos. Una regrabación con pasos de desplazamiento suave los haría
  deslizar.

## 8. Para 9:16

Igual que en Eventos: cambiar en `index.html` las variables `--f-*` (1080×1920; márgenes 60; ceja 188 / 34 px; frase 236 / 960 / 104 px;
ventana 60·480·960×850 con `--f-ventana-h: 850px`, `--f-ventana-hvis: 850px`, `--f-k: 0.820513`, `--f-grab-alto: 2077.54px`,
`--f-latigo: 1000px`) y `window.KD` (ventana 960×850, `latigo: 1000`, `cambio` escala 0,92 con origen «50% 0%» y x +36), la firma por
`identidad/cierre-corto.html` y `data-width/height` de los hosts y de las escenas; la frase 4 en tres líneas («Que cada puesto / de
servicio / esté *cubierto*»). Los tramos, los sonidos y los tiempos no cambian; la cámara y los iris se recalculan con `enc()` y
`enVentana()`. En 9:16 M muestra 247 px CSS de alto: revisar `avisar` (la fila y la barra, 315 px), `avisados` (el diálogo, 200 px) y
`cierre` (que en 4:5 usa 366 px y en 9:16 pierde el «9:00 a. m.» o la fila de Gabriela; con la ventana completa la píldora queda en otra
altura y quizás vuelva «Servicio General»).
