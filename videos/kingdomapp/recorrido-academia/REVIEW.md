# REVIEW · Recorrido del módulo: Academia — «La clase ya empezó… y lo que sigue» (16:9)

2026-10-30 · Construcción en HyperFrames 0.8.221 a partir de [SPEC.md](SPEC.md) y [STORY.md](STORY.md), con las grabaciones nuevas
`celular.mp4` (1170×2532) y `escritorio.mp4` (1920×1080) y el montaje del [clip](../clip-sitio-academia/REVIEW.md) para los cuadros 0–839.
El dueño ya no revisa: construido, verificado y renderizado sin paradas. **Entrega:** `renders/recorrido-academia-16x9.mp4`.

## 1. Qué hay

| Archivo | Qué es |
|---|---|
| `index.html` | **Generado** por `_gen/gen.py` desde `_gen/index.tpl.html`. La raíz: las variables de los dos escenarios, los hosts de las escenas, la **escena** de 3840 px con las dos ventanas (celular y escritorio), los 65 tramos de video, las 17 marcas de toque, las nueve cámaras, los dos látigos (vertical y horizontal), los tres iris, la música en dos `<audio>` y los 52 sonidos |
| `_gen/gen.py`, `_gen/index.tpl.html`, `_gen/README.md` | El generador: las tablas de tramos (`T`), marcas (`TOQUES`), sonidos (`SND`) y frases 4–9 (`FRASES`). `mix.py` simula la mezcla; `medir_render.py` mide el render; `resumen_check.py` resume el último `check`; `rsheet.py` hace hojas del render |
| `compositions/fondo.html` | La noche del sitio; el halo se asienta en 0, 120, 240, 360, 840, 1320, 1680, 2040 y 2280 |
| `compositions/frase-1..3.html` | Las tres frases del clip, pasadas a 16:9 (`.k-titular`, 84 px, columna izquierda en x 120 · y 460); la 3 se queda hasta el 826 |
| `compositions/frase-4..9.html` | Las frases nuevas (generadas): 5, 6, 8 y 9 en el escenario del celular (dos líneas), 4 y 7 sobre el escritorio (x 240 · y 132, una línea) |
| `compositions/ceja.html` | «ACADEMIA»: celular (x 120 · y 412) y escritorio (x 240 · y 92); sale con blur al arrancar cada látigo horizontal y entra en el otro escenario |
| `identidad/cierre-comercial.html` | El cierre del Comercial (2760–2909), `{"publico":"iglesia","llamado":"prueba","contacto":"sitio","fondo":"noche","idioma":"es"}`; campanas en 92,38 |
| `assets/grabaciones/grabacion.mp4`, `pasos.json` · `assets/audio/toque-b.wav`, `toque-c.wav` | Copiados del clip (parte 1 y la rotación del toque) |
| `assets/grabaciones/celular.mp4`, `escritorio.mp4` y sus `-pasos.json` | Las grabaciones nuevas (parte 2) |

## 2. Los planos, con sus cuadros

«grab.» = cuadro de la grabación. Todos los tramos a 1× salvo la escritura de las clases del paso 2 (2×, la del SPEC) y un tramo quieto del
paso 5 (1/3 sobre diez cuadros idénticos). Los cortes caen en esperas, cargadores o pantallas quietas.

| Plano | Cuadros | Grabación y cámara |
|---|---|---|
| P1–P8 El clip | 0–839 | Los 22 tramos, las seis marcas, los iris del 375 y el 660, los tres látigos verticales y los aterrizajes del clip, tal cual; la ventana pasa a `.k-ventana-16x9` (720×900 en 1104·90), las frases y la ceja a la columna izquierda y cada encuadre a `s' = max(s, 1,085)`. Sin la ventana a un lado del 724, sin la subida ni la firma. 720–733 cámara a `E3.codigo`: «Código de verificación · 7YU79-NNB7A» queda 3,6 s |
| P9 Un curso, en cinco pasos | 840–1319 | **830–840** látigo horizontal a la izquierda; escritorio grab. 33 (`catalogo`, D) · **870** toque en «Nuevo curso» (grab. 83); **877** la app cambia a las opciones (grab. 90) y la cámara se reencuadra con ella (`opciones`) · 885 corte en la espera (98→155) · **900** toque en «En blanco», **iris 900–905**; dentro, «Paso 1 de 5» (grab. 182); cámara → `pasos` 900–913 · **915** toque en el nombre (grab. 240), «Matrimonios fuertes» 915–957 a 1× · **960** corte: «Paso 2 de 5» (grab. 741) · 975–997 «Escuchar con amor» y 997–1020 «Hablar con verdad» a 2× · **1020** corte: el paso 2 completo, la app ya bajó (grab. 1440: «Finanzas en casa», «El presupuesto familiar») · **1080** «Paso 3 de 5» (grab. 1530) · **1140** «Paso 4 de 5» con «Asistencia mínima» marcada (grab. 2180); 1155–1168 cámara → `criterios` · **1200** «Paso 5 de 5» (grab. 2283), la cámara vuelve a `pasos` en el corte · **1230** la app ya bajó 100 px al pie (grab. 2390, compensado) y la cámara baja a `pie` · **1260** toque en «Publicar» (grab. 2400) · 1264 corte en «Cargando…» (2404–2405 fuera): **«¡Publicado!»** entra 1264–1268 (grab. 2406–2410); cámara → `dialogo` 1268–1281 |
| P10 Exámenes que se califican solos | 1320–1679 | **1310–1320** látigo a la derecha; celular grab. 77 (`examen`, G): «Pregunta 1 de 3» con el reloj en 1:08 · **1380** «Cuatro» (grab. 157; marcada 1382, grab. 164) · 1395 «Siguiente» (grab. 237; fuera de cuadro) → **1396 «Pregunta 2 de 3»** · 1410 corte en la espera · **1440** «Verdadero» · 1455 «Siguiente» → 1456 «Pregunta 3 de 3» · 1470 corte · **1500** «Pablo» · 1515 «Revisar» → 1516 «Respondiste 3 de 3 · No hay que entregar…» con el reloj en 0:53 · **1530** corte con el salto de tiempo a la vista: la misma vista con el reloj en **«0:01»** (grab. 2105; los 70 s de espera, fuera) · 1530–1543 cámara → `todas` · **1545** «La evaluación cerró. Calculando tu nota…» (grab. 2160) · **1560 «Tu nota · 5 / 5 · Alcanzó la nota mínima (3)»** (grab. 2223), punch 1560–1568 a `nota` (×1,5) · **1620** la lista ya bajada (grab. 2840), cámara → `lista`: «2 · Correcta» y «3 · Correcta» |
| P11 Sabes quién va en riesgo | 1680–2039 | **1670–1680** látigo vertical hacia abajo, de vuelta al profesor; grab. 3166 (`sabana`, G): el encabezado «Quiz de los evangelios» y **«Lucía Ruiz Montoya · 4 · 5»** · **1740** corte a la pestaña arriba con los filtros (grab. 3083), cámara → `filtros` · **1800** toque en «En riesgo · 1» (grab. 3271) · **1803** el filtro marcado (grab. 3274) · **1860** la tabla bajó y se corrió hasta «Final» (grab. 3354): **«Ester Gil Mesa · 3 · 1,67 · ⚠ 2,8»**, con la misma cámara |
| P12 Toda tu escuela, de un vistazo | 2040–2279 | **2030–2040** látigo a la izquierda; escritorio grab. 2620 (`cifras`, D): 6 grupos en curso, 86 personas cursando, 80 %, 4 / 5, 43 %, 0 por aprobar, 89 graduados · **2100** la app baja a «Alumnos en riesgo» (grab. 2754), reencuadre en el corte (`riesgo`) · **2160** toque en «Jhon Fredy Lezcano Montoya» (grab. 2871); la ficha entra 2163–2165 · 2175–2188 cámara → `ficha`: «No cumple · 67 % de asistencia · 3,96 / 5 · Asistencia: 66,7 %; se pide 75 %» |
| P13 Y cualquiera lo verifica | 2280–2519 | **2270–2280** látigo a la derecha; `/verificar` en una sola toma a 1× (grab. 3608–4107, `inicio`, G) · **2310** toque en el campo (grab. 3658), «7YU79-NNB7A» 2316–2340 · **2385** toque en «Verificar» (grab. 3733), «Buscando…» 2392 · **2397 «Certificado válido · Andrea Perea López · Fundamentos bíblicos · Iglesia Kingdom Demo 1 · 30 de octubre de 2026 · 7YU79-NNB7A»** · 2400–2413 cámara → `valido` (×1,15) · 2460–2473 → `tarjeta` |
| P14 La frase del sitio | 2520–2759 | Frase 9 palabra a palabra 2519–2533 (*líderes* dorada en el 2525); la ceja sale 2520–2523; la ventana a 0,92 con origen «100% 50%» y x +24 (2524–2538); quieto; dip 2757–2759 |
| P15 Cierre del Comercial | 2760–2909 | `cierre-comercial`; la escena se oculta en el 2760 |

## 3. Sincronía: cada cosa con su cuadro y su pulso

Pulsos: múltiplos de 15 cuadros (SPEC §0.3). «Imagen» es el primer cuadro en que se ve; el sonido cae un cuadro después. Los cuadros de
0 a 719 son los del clip (su REVIEW §3, sin cambios).

| Qué | Imagen | Pulso | Sonido | Desvío |
|---|---|---|---|---|
| Frase 3 sale · la ceja sale · **látigo al escritorio** | 826–830 · 826–829 · 830–840 | **840 (1,00)** | `desliz` 841 (1,4) | salidas −11 (§4.10) |
| Ceja arriba · «Un · curso, · en · cinco · pasos.» | 842–848 · 843…851 | 840 | — | 0 |
| **Toque en «Nuevo curso»** · las opciones | 870 · 877 | 870 | `toque` a 871 | 0 (las opciones a 1×, no en el 885) |
| **Toque en «En blanco»** · iris | 900 · 900–905 | **900** | `toque` b 901 | 0 |
| **Toque en el nombre** · «Matrimonios fuertes» | 915 · 915–957 | 915 | `toque` c 916 | (nuevo) |
| «Paso 2 de 5» (la costura de la música) | 960 | **960 (0,92)** | `toque` a 961 | 0 |
| El paso 2 completo | 1020 | 1020 | — | 0 |
| «Paso 3 de 5» · «Paso 4 de 5» · «Paso 5 de 5» | 1080 · 1140 · 1200 | 1080 · 1140 · 1200 | `toque` b 1081 · c 1141 · a 1201 | 0 |
| **Toque en «Publicar»** · «¡Publicado!» entero | 1260 · 1268 | 1260 | `toque` b 1261 · `confirmacion` 1269 (1,4) | **−7** (SPEC 1275) |
| Frase 4 y ceja salen · **látigo de vuelta** · frase 5 | 1306–1310 · 1310–1320 · 1322…1330 | **1320 (0,93)** | `desliz` 1321 | 0 |
| **«Cuatro»** · «Siguiente» → pregunta 2 | 1380 · 1395 → 1396 | 1380 · 1395 | `toque` c 1381 · a 1396 | 0 |
| **«Verdadero»** · «Siguiente» → pregunta 3 | 1440 · 1455 → 1456 | 1440 · 1455 | `toque` b 1441 · c 1456 | 0 |
| **«Pablo»** · «Revisar» → «Respondiste 3 de 3» | 1500 · 1515 → 1516 | 1500 · 1515 | `toque` a 1501 · b 1516 | 0 |
| El reloj en «0:01» · «Calculando tu nota…» | 1530 · 1545 | 1530 · 1545 | — | 0 |
| **«Tu nota · 5 / 5»** · punch | 1560 · 1560–1568 | **1560 (1,00)** | `confirmacion` 1561 (1,4) | 0 |
| Las «Correcta» | 1620 | 1620 | — | 0 |
| **Látigo hacia abajo** · Lucía con su 5 · frase 6 | 1670–1680 · 1680 · 1682…1690 | **1680 (0,98)** | `desliz` 1681 | 0 |
| Los filtros | 1740 | 1740 | — | 0 |
| **Toque en «En riesgo»** · el filtro marcado | 1800 · 1803 | **1800 (clímax)** | `toque` c 1801 · `aparicion` 1804 | 0 |
| La tabla en «Final»: Ester Gil Mesa, 2,8 | 1860 | 1860 | `desliz` 1861 | 0 |
| Frase 6 y ceja salen · **látigo al escritorio** · frase 7 | 2026–2030 · 2030–2040 · 2043…2053 | **2040** | `desliz` 2041 | 0 |
| «Alumnos en riesgo» | 2100 | 2100 | `desliz` 2101 | (nuevo) |
| **Toque en Jhon Fredy** · la ficha entera | 2160 · 2165 | **2160** | `toque` a 2161 · `aparicion` 2166 | ficha −10 (SPEC 2175: la animación real dura 5 cuadros) |
| Frase 7 y ceja salen · **látigo de vuelta** · frase 8 | 2266–2270 · 2270–2280 · 2282…2288 | **2280** | `desliz` 2281 | 0 |
| **Toque en el campo** · el código | 2310 · 2316–2340 | 2310 | `toque` b 2311 | 0 |
| **Toque en «Verificar»** · «Certificado válido» | 2385 · 2397 | 2385 | `toque` c 2386 · `confirmacion` 2398 (1,4) | toque +45 (SPEC 2340) · resultado −3 (SPEC 2400) |
| Frase 9 · la ceja sale · la ventana a un lado | 2519…2533 · 2520–2523 · 2524–2538 | **2520** | — | 0 |
| `subida` · dip · **cierre** | 2716–2773 · 2757–2759 · **2760** | 2760 | golpe 2761 · campanas 92,38 | 0 |

## 4. Desvíos del SPEC y su porqué

1. **Lo que trajo la grabación** (pedido): la alumna es **Lucía Ruiz Montoya** (cuenta 104); su fila en la sábana dice «4 · 5» y el filtro
   «En riesgo · 1» deja solo a **Ester Gil Mesa (2,8)**, que la tabla muestra ya corrida hasta «Final». La nota llegó **en el grab. 2223**, no
   en el 2746 que decía el pedido (la escena esperó de sobra; el tramo `nota` de `pasos.json` empieza tarde): «Calculando tu nota…» va de la
   2160 a la 2222 y el reloj está en «0:01» hasta la 2127. El tablero dice 6 · 86 · 80 % · 4 / 5 · 43 % · 0 · 89 y la ficha, 67 %, «No cumple»
   y 3,96 / 5, como el pedido.
2. **Las esperas y los cargadores, fuera:** el asistente tiene 2,4 s de grabación por cada segundo de video en el paso 2 y esperas de 1–3 s
   entre pasos; el examen, 70 s de reloj; el tablero, la carga de las cifras (2614–2619). Se corta dentro de pantallas quietas y se saltan
   «Cargando…» (2404–2405) y la carga del tablero. La app tarda 5–7 cuadros en marcar una opción y 7 en cambiar de pregunta: el toque
   queda en su pulso y se corta del toque a la pantalla ya cambiada (como en el clip).
3. **Los «Siguiente» y «Revisar» del examen y del asistente quedan fuera de cuadro:** el pie de la pantalla (CSS 777–829 en el celular,
   691 en el escritorio) no cabe en ningún encuadre de lectura junto con la pregunta o la barra. Se oye el toque (como el «Siguiente» del
   960 del SPEC) y la pantalla cambia en el cuadro siguiente; no se dibuja marca donde no se ve el botón.
4. **Encuadres con las cajas reales:**
   - La «Datos de ejemplo» de 52 px tapa abajo a la izquierda de cada ventana. `pasos` baja a CSS 281–656 (la barra arriba, sin el título
     del paso ni «Paso N de 5»: no cabían con lo que se llena) y el paso 4 lleva un movimiento propio (1155 → `criterios`) para que
     «Asistencia mínima ✓ 80 %» quede por encima de la píldora; en el corte del 1200 la cámara vuelve a `pasos`.
   - `examen` a CSS 161–610 (G) para que la opción D quede por encima de la píldora; `todas` a 76–525; el punch de la nota a ×1,5 (no C):
     a 1,8 la píldora «Alcanzó la nota mínima (3)» se cortaba.
   - La sábana no admite M: la columna de nombres (x 16) y la de «Final» (hasta x 374) solo caben juntas en G. Sin el punch del 1920.
   - El tablero: `cifras` (CSS 185–896 × 113–488) deja ver seis de las nueve cifras y las tres de abajo por encima de la píldora; en el salto
     del 2100 la cámara se reencuadra con la app (`riesgo`) para que Jhon Fredy quede entero arriba.
   - En el 877 (las opciones) y el 2100 la app cambia de pantalla entera: la cámara se reencuadra en ese cuadro, sin moverse.
5. **«¡Publicado!» en el 1268, no en el 1275:** entre el toque y el diálogo la grabación solo tiene la carga; el diálogo entra completo en
   cinco cuadros. Su `confirmacion` va con la imagen (1269).
6. **La verificación en una sola toma a 1×:** del toque en el campo (2310) al de «Verificar» hay exactamente 75 cuadros de grabación, así
   que el toque cae en el pulso 2385 sin cortar; el resultado llega 12 cuadros después, en el **2397** (no en el 2400). Se añadió el toque del
   campo (2310), que el SPEC no tenía.
7. **Sonidos añadidos:** `toque` c en el nombre del curso (915), `desliz` en el salto a «Alumnos en riesgo» (2100); la `aparicion` de la
   ficha va en el 2166 (la ficha ya entró en el 2165).
8. **Niveles:** los del pedido y el recorrido de Eventos, no los del SPEC §1.7: toques a 1,0 (también los clave del clip), confirmaciones y el
   látigo del 840 a 1,4, la música a **0,75** en dos `<audio>` (la costura hecha en la línea de tiempo, no un `.wav` aparte) con −10 dB debajo
   de las campanas (92,4) y 0 en el 94,0.
9. **«Datos de ejemplo» del celular a 30,5 px** (no 22): con la ventana a 0,92 sigue en 28 px, el piso de lectura del `check`.
10. **Las frases y la ceja salen al arrancar cada látigo horizontal** (826–830, 1306–1310, 2026–2030 y 2266–2270), no 3 cuadros antes del
    golpe: el borrón de movimiento del render (obturador 180) se pinta por encima de todo, también del texto, y en el primer render la
    ventana que cruza la columna izquierda tapaba «Quien cumple» y «Un curso» a medio salir (se vio en el render, cuadros 835 y 1315). Las
    frases nuevas siguen entrando en el +2/+3 del golpe. En el látigo vertical (1670–1680) la ventana no cruza el texto y la frase 5 sale
    en 1677–1681, como el SPEC.

## 5. La mezcla y la costura

- **Niveles:** toques a 1,0 (los 24, también los clave del clip); las cinco `confirmacion` (181 y 604 del clip, 1269, 1561 y 2398) y el
  `desliz` de los látigos 121 y 841 a 1,4; `aparicion`, `desliz` y `subida` a 1,0; la música a **0,75** en el carril de volumen
  (0,24 en el 92,4 y 0 en el 94,0, debajo de las campanas).
- **Simulación** con `_gen/mix.py` antes del render: −17,0 LUFS · −2,6 dBTP.
- **Render final:** **−17,0 LUFS integrados, pico real −2,7 dBTP** (ffmpeg `ebur128` y `hyperframes audio` coinciden), sin recortes
  (`clipping.count` 0), LRA 2,8 LU, sonoridad de corto plazo máxima −15,6. No hizo falta bajar nada.
- **La costura de la música** (SPEC §0.1, hecha en la línea de tiempo con dos `<audio>` sobre el mismo mp3, como en Eventos): música A
  pista 14,05 → 46,04 (video 0 → 31,99), cruce de 30 ms 0,75 → 0 en 31,96–31,99; música B desde la pista 22,01 en el video 31,96 (0 → 0,75
  en 30 ms). El golpe del 22,05 cae en el **32,0 (cuadro 960)**. Medido en el render: `hyperframes audio` ve un solo golpe en el **32,03**
  (fuerza 0,74: el toque del 960 sobre el golpe de la pista) y ningún ataque entre el 30,53 y el 32,03. Sonoridad momentánea cada 100 ms:
  31,7 −17,2 · 31,8 −16,4 · 31,9 −15,7 · **32,0 −15,3** · 32,1 −14,6 · 32,2 −14,6 · 32,3 −14,8 LUFS: sube sin escalón hacia el golpe, igual
  que el golpe del 28,0 (−15,5 → −14,0 → −13,8). El máximo del golpe de la costura (−14,6) queda 0,8 dB por debajo del 28,2 (−13,8): dentro de
  ±1,5 dB. **Medida, no oída.**
- **Los toques en el render** (`hyperframes audio`, golpes detectados): 29,03 · 30,03 · 30,53 · 32,03 · 36,03 · 38,03 · 40,03 · 42,03 ·
  46,03 · 46,53 · 48,03 · 48,53 · 50,03 · 50,53 · 60,03 · 72,03 · 77,03 · 79,53 s = cuadros 871 · 901 · 916 · 961 · 1081 · 1141 · 1201 · 1261 ·
  1381 · 1396 · 1441 · 1456 · 1501 · 1516 · 1801 · 2161 · 2311 · 2386: cada uno un cuadro después de su imagen. Las `confirmacion`,
  `aparicion` y `desliz` son más suaves que el umbral de golpes y no aparecen en la lista; su posición sale de `index.html`.

## 6. Lo que se revisó

- `npx hyperframes check --json`: **0 errores**, 1 aviso: `composition_file_too_large` (la raíz lleva los 65 tramos de video a propósito, para
  que se vean y se recorten en la línea de tiempo, como el clip y Eventos).
- `npx hyperframes snapshot --review`: `.hyperframes/artifacts/snapshots/2dff8ccb-bd4d-4877-b84b-3c3d54d60fdf/` (`review-beats-1…7`,
  `review-seam-01…83`, `review-phone-1…7`), más tres tandas de `--at` (los 60 cuadros del SPEC §4 y los látigos 27,6–28,2, 43,85–44,2,
  67,85–68,2 y 75,85–76,2).
- **Notas que salieron de ahí, ya corregidas:** (P0) «Hablar con verdad» y «Asistencia mínima» quedaban debajo de «Datos de ejemplo» →
  `pasos` más abajo y el movimiento del paso 4 a `criterios`; (P0) el borrón del látigo horizontal tapaba la frase 3 y la 4 a medio salir →
  las frases y la ceja salen al arrancar el látigo (§4.10); (P1) las opciones del 877 a medias bajo el encuadre del catálogo → reencuadre en el
  cambio de pantalla; (P1) la opción D, «3 · Correcta», «43 %» y la fila de Lucía junto a la píldora → `examen`, `lista`, `cifras` y `sabana`
  recalculados; (P2) `pie` mostraba 200 px vacíos a la derecha.
- **El render cuadro a cuadro:** hojas de 44 cuadros (`_gen/rsheet.py`). Los cortes dentro de pantallas quietas no se ven: diferencia media
  entre el cuadro anterior y el del corte **0,01–0,02/255** en el 885, 1410, 1470, 1530 (el salto de 70 s del reloj: solo cambia «0:53» →
  «0:01») y 1260.
- `ffprobe`: H.264 1920×1080, 30 fps, **2910 cuadros, 97,000 s**; AAC 48 kHz estéreo; 18,7 MB.
- La hoja a 360 px: las frases se leen; la app del escritorio no (es 16:9 para computador, YouTube y presentaciones).
- **Nadie oyó el sonido ni vio el movimiento a velocidad real fuera del render:** el sonido está medido, no oído. La vista previa no se abrió
  (sin paradas).
- Mirado: el primer cuadro del cierre (2760) es la noche del kit antes de que suba la corona; es la pieza aprobada del kit.

## 7. El plano más débil y qué cambiaría con más tiempo

- **El asistente (840–1319):** el escritorio se lee solo de cerca, así que la barra de cinco segmentos queda arriba sin «Paso N de 5» ni el
  título del paso, y los «Siguiente» no se ven. Lo que se lee es lo que se llena (el nombre, las materias, «Asistencia mínima ✓»). Con más
  tiempo: regrabar con el asistente en una ventana de 1280×600 o con `ver` sobre la barra antes de cada «Siguiente», para que el toque se
  vea.
- **El examen:** las respuestas se tocan en pantalla, pero el avance de pregunta no (el botón queda fuera del encuadre de lectura).
- **La sábana** no tiene punch (no cabe M con nombres y «Final»): el clímax del 1800 es el toque en el filtro, no un acercamiento.
- **El tablero** muestra seis de las nueve cifras; «En riesgo o no cumplen · 5» queda al borde derecho.
- **La píldora «Datos de ejemplo»** tapa a ratos lo de abajo a la izquierda (la barra de navegación del celular, «Buscar alumno», el pie de
  la tarjeta de verificación): es la posición pedida; nunca tapa lo que se toca ni el dato del plano.
