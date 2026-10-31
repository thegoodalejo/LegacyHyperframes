# REVIEW · Recorrido del módulo: Eventos — «Terminó la reunión, y el lunes el pastor lo ve» (16:9)

2026-10-30 · Construcción en HyperFrames 0.8.221 a partir de [SPEC.md](SPEC.md) y [STORY.md](STORY.md), con las grabaciones nuevas
`sin-senal.mp4` (1170×2532) y `tablero.mp4` (1920×1080) y el montaje del [clip](../clip-sitio-eventos/REVIEW.md) para los cuadros 0–779.
El dueño ya no revisa: construido, verificado y renderizado sin paradas. **Entrega:** `renders/recorrido-eventos-16x9.mp4`.

## 1. Qué hay

| Archivo | Qué es |
|---|---|
| `index.html` | **Generado** por `_gen/gen.py` desde `_gen/index.tpl.html`. La raíz: las variables de los dos mundos, los hosts de las escenas, la **tira** de 3840 px con las dos ventanas (celular y computador), los 57 tramos de video, los dos stills, las 25 marcas de toque, las tres cámaras (`#cam-cel`, `#cam-esc` y `#cam-esc2` dentro del iris de la ficha), el látigo, los dos iris, la música en dos `<audio>` y los 42 sonidos |
| `_gen/gen.py`, `_gen/index.tpl.html`, `_gen/README.md` | El generador: las tablas de tramos (`T1`, `T2`), marcas (`TOQUES1`, `TOQUES2`), sonidos (`SND`) y frases 4–9 (`FRASES`). `mix.py` simula la mezcla; `resumen_check.py` resume el último `check`; `rsheet.py` hace hojas del render |
| `compositions/fondo.html` | La noche del sitio; el halo se asienta en 0, 180, 1080, 1560 y 2580 |
| `compositions/frase-1..3.html` | Las tres frases del clip, pasadas a 16:9 (`.k-titular`, 88 px, columna izquierda) |
| `compositions/frase-4..9.html` | Las frases nuevas (generadas): 4 y 5 en el celular (88 px, dos líneas), 6 a 9 sobre el computador (84 px, una línea) |
| `compositions/ceja.html` | «EVENTOS»: en el celular (x 96 · y 372) 195–1077; en el computador (x 240 · y 84) 1095–2583 |
| `identidad/cierre-comercial.html` | El cierre del Comercial (2760–2909), `{"publico":"iglesia","llamado":"prueba","contacto":"sitio","fondo":"noche","idioma":"es"}`; campanas en 92,38 |
| `assets/grabaciones/grabacion.mp4`, `pasos.json` | Copiados del clip (0–779) |
| `assets/stills/still-364.png`, `still-1027.png`, `assets/audio/toque-b.wav`, `toque-c.wav` | Copiados del clip |

## 2. Los planos, con sus cuadros

«grab.» = cuadro de la grabación. Todos los tramos nuevos a 1× (los cortes caen en esperas o en pantallas quietas; ninguna velocidad nueva).

| Plano | Cuadros | Grabación y cámara |
|---|---|---|
| P1–P5 La historia del clip | 0–719 | Los 30 tramos, los dos stills, las 14 marcas, el iris del 180 y la cámara del clip, tal cual (sus objetivos y sus tres compensaciones de salto); cambian solo la ventana (`.k-ventana-16x9`, 720×900 en 1104·90), la ceja y las frases en la columna izquierda. El tramo v30 («¡Listo!», grab. 1328–1445) llega al 779 |
| P6 ¿Sin señal? | 720–1079 | 720–733 cámara → `listoBotones` (×1,13). **780** toque en «Volver a la lista» (sin-senal grab. 1051, idéntica a la 1445 del clip: diferencia media 0,17/255) · **781** match cut a la lista con el chip «Sin señal» ya puesto (grab. 1167; la lista sin chip 1060–1126 queda fuera), G16 · **810** toque en la casa (grab. 1196) · **813** el reporte de la vencida del 21 de oct (grab. 1274): «Vencida» y la nota «Sin señal: la asistencia se guarda en este dispositivo…» · **840** toque en «Igual que la última vez» (grab. 1301), corte en la onda (1302→1308), **842** «8 marcadas» y las filas en ámbar · 846–859 cámara → `listaMarcada` · **870** la app baja (salto real, grab. 1379, aquí desde la 1424) · **900** toque en «Guardar asistencia» (grab. 1454), corte en la onda (1456→1460) · **903** paso ②: «Sin señal», «1 sin enviar», «Espera señal», «Guardado en este dispositivo…» (grab. 1461) · 900–913 → `enCola`, 930–943 → `chips` (×1,08), **960** vuelve la señal: el primer cuadro sin chips ya asentado (grab. 1607; los de transición 1599–1606 quedan fuera), «Falta el reporte» · 990–1003 → `enCola` |
| P7 El látigo y «El pastor lo ve todo» | 1080–1319 | **1080–1088** la tira −1920 px (`power3.inOut`); tablero grab. 817: las cifras cuentan 1080–1098 (69 · 14.827 · 17,8 · 93 % · 27 / 69 · ↗20 ↘14). Cámara E-G `kpisIzq`; **1200** la grabación pasa a la que subió 32 px (grab. 988), la cámara arranca compensada y va a E-M `kpisDer` («Al día 27 / 69 · 22 retrasados» y «Tendencia») · 1260 → `vistas` · la marca espera sobre «Mapa» desde el 1305 |
| P8 Y dónde falta una reunión | 1320–1799 | **1320** toque en «Mapa» (grab. 1108) · **1321** match cut al mapa con teselas (grab. 1299; la carga 1109–1253 queda fuera), E-A `mapa` · **1380** «Dónde viven» (grab. 1358), **1381** la capa ya dibujada (grab. 1371) · 1440 → E-G `centro` · 1500 → `mapa` · **1560** «Zonas sin evento» (grab. 1507), **1561** la zona ya dibujada (grab. 1521) · 1620 → E-M `zona` · 1680 → `mapa` · **1740** la app sube a las pestañas (salto real, grab. 1796) · 1755 → E-G `tabla` |
| P9 Cuál crece y cuál necesita apoyo | 1800–2099 | **1800** «Eventos» (grab. 1884), **1801** la lista (grab. 1887): «Sin reportar» y «Retrasado» arriba · 1860 → `tablaDer` · **1920** «Tendencia» (grab. 2037), **1922** reordenada · **1950** la app sube al buscador (grab. 2111) · 1965 → E-M `buscar` · **1980** toque en el buscador (grab. 2199), «Jorge Gallego» **1982–2012** a 1× · **2025** filtrada (grab. 2248): 4 eventos · **2040** baja a sus filas (grab. 2334) · 2055 → `filasJorge` |
| P10 La ficha | 2100–2579 | **2100** toque en «Casa de Paz Laureles 1» (grab. ≈ 2421) · **iris 2100–2105** desde el enlace; la lista sigue debajo (no hace falta still) · la ficha con portada (grab. 2430), E-A `fichaCabeza` · **2160** la app baja a la tarjeta «Asistencia» (grab. 2531) · 2175 → `asistencia` (E-G) · 2220 → `ultima` (×1,75) · 2280 → `tendenciaMeta` (×1,75) · 2340 → `quienes` (×1,8) · **2400–2408** punch → `ximena` (E-M) · 2460 → `asistencia` · 2520 → `cierre` (×1,71) |
| P11 Cada reunión cuenta | 2580–2759 | La ficha quieta (grab. hasta la 3130, sin still). Frase 9; la ceja sale 2580–2583; la ventana a 0,96 en 2640–2654; dip 2757–2759 |
| P12 Cierre del Comercial | 2760–2909 | `cierre-comercial`; la tira se oculta en el 2760 |

## 3. Sincronía: cada cosa con su cuadro y su pulso

Pulsos: múltiplos de 15 cuadros (SPEC §0.2). «Imagen» es el primer cuadro en que se ve; el sonido cae un cuadro después. Los cuadros de
0 a 719 son los del clip (su REVIEW §3, sin cambios). Comprobado en el render: `hyperframes audio` detecta los golpes de los toques en
**2,53 · 4,03 · 6,03 · 8,03 · 9,03 · 10,03 · 11,53 · 12,53 · 15,03 · 16,03 · 20,03 · 20,53 · 21,03 · 22,03 · 26,03 · 27,03 · 28,03 · 30,03 ·
44,03 · 46,03 · 52,03 · 60,03 · 64,03 · 66,03 · 70,03 s** = cuadros 76 · 121 · 181 · 241 · 271 · 301 · 346 · 376 · 451 · 481 · 601 · 616 · 631 ·
661 · **781 · 811 · 841 · 901 · 1321 · 1381 · 1561 · 1801 · 1921 · 1981 · 2101**: los 25 toques, cada uno un cuadro después de su imagen.

| Qué | Imagen | Pulso | Sonido | Desvío |
|---|---|---|---|---|
| Frase 4, palabra a palabra; cámara → `listoBotones` | 720 · 722 · … · 730 / 720–733 | **720 (golpe 0,96)** | — | 0 |
| La marca sobre «Volver a la lista» | 776 | — | — | 0 |
| **Toque en «Volver a la lista»** | 780 | 780 | `toque` a 781 | 0 |
| Match cut: la lista con «Sin señal» (1,03 → 1,00) | 781–791 | — | — | 0 (SPEC 781) |
| **Toque en la casa** | 810 | 810 | `toque` b 811 | 0 |
| El reporte de la vencida con la nota «Sin señal: …» | 813–823 | — | — | 0 (SPEC 813) |
| **Toque en «Igual que la última vez»**, sin señal | 840 | **840 (1,00)** | `toque` c 841 | 0 |
| Las filas en ámbar, «8 marcadas» | 842 | — | `aparicion` 843 | 0 |
| Cámara → `listaMarcada` | 846–859 | — | — | (nuevo, §4.4) |
| La app baja a «Guardar asistencia» | 870 | 870 | `desliz` 871 | 0 |
| **Toque en «Guardar asistencia»** | 900 | **900 (la costura)** | `toque` a 901 | 0 |
| «Sin señal · 1 sin enviar · Espera señal · Guardado en este dispositivo…» | 903 | — | `aparicion` 904 | 0 |
| Cámara → `enCola` · → `chips` | 900–913 · 930–943 | 900 · 930 | — | 0 |
| Frase 4 sale | 956–960 | — | — | 0 |
| **Vuelve la señal: los chips se van**, «Falta el reporte» | 960 | **960 (0,92)** | `confirmacion` 961 (1,4) | 0 |
| Frase 5, palabra a palabra | 960 · 962 · … · 974 | 960 | — | 0 |
| Cámara → `enCola` | 990–1003 | 990 | — | 0 |
| Frase 5 sale · la ceja sale | 1072–1076 · 1074–1077 | — | — | 0 |
| **El látigo** (la tira −1920 px) | 1080–1088 | **1080 (respiro)** | `desliz` 1081 | 0 |
| Las cifras cuentan · quietas | 1080–1098 · 1099 | — | — | −1 (SPEC 1081–1099) |
| La ceja en el computador | 1095–1098 | 1095 | — | 0 |
| Frase 6 | 1140 · … · 1148 | 1140 | — | 0 |
| Cámara → `kpisDer` (con la compensación del salto de 32 px) · → `vistas` | 1200–1213 · 1260–1273 | 1200 · 1260 | — | 0 |
| La marca espera sobre «Mapa» | 1305 | 1305 | — | 0 |
| **Toque en «Mapa»** · el mapa con teselas | 1320 · 1321 | **1320 (0,93)** | `toque` b 1321 | −1 (SPEC 1322) |
| **Toque en «Dónde viven»** · la capa | 1380 · 1381 | 1380 | `toque` c 1381 | 0 |
| Cámara → `centro` · → `mapa` | 1440–1453 · 1500–1513 | 1440 · 1500 | — | 0 |
| **Toque en «Zonas sin evento»** · la zona | 1560 · 1561 | **1560 (1,00)** | `toque` a 1561 · `aparicion` 1562 | −1 |
| Frase 7 | 1560 · … · 1568 | 1560 | — | 0 |
| Cámara → `zona` · → `mapa` | 1620–1633 · 1680–1693 | 1620 · 1680 | — | 0 (sin punch, §4.5) |
| La app sube a las pestañas · cámara → `tabla` | 1740 · 1755–1768 | 1740 | `desliz` 1741 | 0 |
| **Toque en «Eventos»** · la lista | 1800 · 1801 | **1800 (clímax)** | `toque` b 1801 | −1 (SPEC 1802) |
| Frase 7 sale · frase 8 entra | 1796–1800 · 1800 · … · 1810 | 1800 | — | 0 |
| Cámara → `tablaDer` | 1860–1873 | 1860 | — | 0 |
| **Toque en «Tendencia»** · reordenada | 1920 · 1922 | 1920 | `toque` c 1921 | 0 |
| La app sube al buscador · cámara → `buscar` | 1950 · 1965–1978 | 1950 | — | 0 |
| **Toque en el buscador** · «Jorge Gallego» | 1980 · 1982–2012 | 1980 | `toque` a 1981 | +2 al terminar (SPEC 2010) |
| La lista filtrada · la app baja · cámara → `filasJorge` | 2025 · 2040 · 2055–2068 | 2025 · 2040 | — | 0 |
| Frase 8 sale | 2070–2074 | — | — | 0 |
| **Toque en «Casa de Paz Laureles 1»** · iris · la ficha | 2100 · 2100–2105 · 2101 | **2100** | `toque` b 2101 | 0 |
| La app baja a «Asistencia» · cámara → `asistencia` | 2160 · 2175–2188 | 2160 | — | 0 |
| Cámara → `ultima` · `tendenciaMeta` · `quienes` | 2220 · 2280 · 2340 (+13) | 2220 · 2280 · 2340 | — | 0 |
| Punch → «Ximena Hoyos Vélez» | 2400–2408 | 2400 | — | 0 |
| Cámara → `asistencia` · → `cierre` | 2460 · 2520 (+13) | 2460 · 2520 | — | 0 |
| Frase 9 (*reunión* dorada en el 2582) · la ceja sale | 2580 · … · 2590 / 2580–2583 | **2580** | — | 0 |
| La ventana a 0,96 | 2640–2654 | 2640 | — | 0 |
| `subida` | — | — | 2716–2773 (golpe 2761) | 0 |
| Dip | 2757–2759 | — | — | 0 |
| **El cierre del Comercial** | **2760** | **2760 (acorde final)** | música −10 dB en 2772, 0 en 2820; campanas 92,38 | 0 |

Ninguna acción cae a más de un cuadro de su pulso. Los −1 son los match cut del computador (la pantalla nueva ya estaba lista).

## 4. Desvíos del SPEC y su porqué

1. **Lo que trajo la grabación** (pedido): «Igual que la última vez» sin señal deja **8 marcadas** (las 7 de siempre y Ximena); al volver la
   señal el estado pasa a **«Falta el reporte»** y se abre el paso ② del formulario (el SPEC no decía qué quedaba); el tablero dice
   **27 / 69** al día (el SPEC decía 28) y la leyenda «Zonas sin evento: 1». Ninguna frase depende de esos números.
2. **El toque de la ficha cae en la grab. ≈ 2421, no en la 2296** que decía el pedido: en la 2296 la lista filtrada está quieta;
   `tablero-pasos.json` pone el clic en la 2421 y la ficha empieza a pintarse en la 2424 (portada en la 2429). Se usó la 2421.
3. **Cortes en las esperas y en pantallas quietas.** Las grabaciones tienen pausas largas entre acciones; en vez de bajar la velocidad se corta
   dentro de tramos idénticos (sin-senal 1199→1274 y 1337→1424; tablero 936→988 con la compensación, 1460→1418, 1610→1573, 1946→1978,
   2066→2111…). La lista sin el chip «Sin señal» (1060–1126), el mapa gris cargando (1109–1253), el dibujo de cada capa (1359–1370,
   1508–1520), los cuadros de transición al volver la señal (1599–1606) y la carga de la ficha (2422–2429) quedan fuera.
4. **Encuadres recalculados con las cajas reales:**
   - `listoBotones` a ×1,13 y no M16: la frase del «¡Listo!» mide 330 px CSS y a más se corta por los lados.
   - `reporteSinRed` baja a CSS 106–594 para que «0 marcadas · Igual que la última vez» quede **por encima de «Datos de ejemplo»** (en el
     primer intento la píldora lo tapaba: P0). Se pierde «Reportar» con su chip arriba; el chip ya se vio en la lista del 781 y la nota
     dice «Sin señal».
   - **Un movimiento de cámara extra en el compás 15** (846–859 → `listaMarcada`): el salto real de la app en el 870 baja 419 px CSS y con el
     encuadre del SPEC «Guardar asistencia» quedaba fuera de la ventana. Con este, la cámara queda quieta en el 870 y el botón se ve.
   - `chips` a ×1,08 (G16⁺) y no M16: a 1,4 se cortaba «Reportar» o «1 sin enviar».
   - `kpisDer` a **E-M** y sin «Metas logradas»: en E-G la mitad derecha de arriba quedaba vacía (las pestañas y los filtros de esa altura
     están a la izquierda) y «Metas logradas» está en la segunda fila, a la izquierda, lejos de «Al día».
   - La ficha: `ultima` y `tendenciaMeta` a ×1,75 (1,97 px por px CSS) y no E-M: a 2,25 la columna del medio quedaba cortada a media
     palabra («…portar»); `quienes` a ×1,8. «Ximena Hoyos Vélez» queda a **31,5 px** en el punch (E-M, el límite de 2,25 px por px CSS
     del BANNED 30), no a 35 px: más grande pixelaría la grabación de 1,5×.
   - La lista del tablero muestra 4 filas, no 7: la página de 1280×720 no tiene más a la vista.
5. **La capa «Zonas sin evento» con poco tiempo** (pedido): una sola zona (el cuadro rosado junto a San Cristóbal). Se ve en el golpe del
   1560 en el plano abierto, un compás cerca (1620–1679, E-M con los círculos 3, 1, 15 y 6 alrededor) y la cámara vuelve a abrir en el 1680.
   En vez del punch del 1680 del SPEC, la cámara se aleja; el salto a la leyenda («Zonas sin evento: 1», grab. 1663) no se usa.
6. **Los match cut del desktop caen un cuadro después del toque** (1321 y 1801, como el 781 del celular), no dos (1322, 1802): la pantalla
   nueva ya estaba lista en la grabación.
7. **El iris de la ficha** usa la lista real debajo (d15 sigue hasta el 2106) en vez de un still, y la ficha vive en una cámara propia
   (`#cam-esc2`) para que el círculo nazca en el enlace mientras la lista no se mueve.
8. **Sonido:** `aparicion` de las zonas en el 1562 (imagen 1561), no en el 1564; ver §5.
9. **El largo del recorrido** (97 s) sigue sin llevarse a `KingdomApp/docs/videos/README.md` («de 60 a 75 s», líneas 62 y 147): queda
   para quien coordina la serie (SPEC §8), para no pisar a los otros recorridos que se construyen en paralelo.

## 5. La mezcla (medida, no oída)

- **Niveles:** los del clip y del pedido: los toques clave a 1,0; las tres `confirmacion` (123, 663, 961) a 1,4 y la del 603 a 1,0; la música
  a 0,75 en el carril de volumen (0,24 en el 92,4 y 0 en el 94,0).
- **Simulación** con `_gen/mix.py` antes del render: −17,1 LUFS · −1,4 dBTP.
- **Render final:** **−17,1 LUFS integrados, pico real −1,4 dBTP** (ffmpeg `ebur128` y `hyperframes audio` coinciden), sin recortes, LRA 2,8 LU,
  sonoridad de corto plazo máxima −15,5; el render no tuvo que bajar nada. Silencio desde el 94,37 (las campanas y la música terminan).
- **La costura de la música** (29,945–29,975, SPEC §0.1), medida en el render: `hyperframes audio` ve **un solo golpe en el 30,03** (fuerza
  0,97: el toque del 900 sobre el golpe del 20,045 de la pista) y, antes, solo el ataque débil (0,10) del 29,73, el mismo que aparece en
  20,73 · 24,73 · 44,73 · 48,73 (el charles de la pista, no la costura). Sonoridad momentánea cada 100 ms: 29,8 −17,8 · **29,9 −17,3 ·
  30,0 −17,1** · 30,1 −16,0 · 30,2 −15,5 · 30,3 −15,1 · 30,4 −14,9 LUFS: 0,2 LU entre el 29,9 y el 30,0; la subida del 30,0 al 30,1 (1,1 LU)
  es el ataque del golpe, igual que en el 28,0 (−15,7 → −14,6). Máximo del golpe del 30,0: −14,9, contra −13,9 en el 28,2 y −13,6 en el
  32,2 (−1,0 y −1,3 dB: dentro de ±1,5 dB). No hizo falta alargar el cruce.

## 6. Lo que se revisó

- `npx hyperframes check --json`: **0 errores**, 1 aviso: `composition_file_too_large` (la raíz lleva los 57 tramos de video a propósito,
  para que se vean y se recorten en la línea de tiempo, como el clip). En el camino se corrigieron: la música B compartía pista con los
  toques (`duplicate_audio_track` ×8), el estado inicial de la ceja del computador (`gsap_timeline_set_initial_hide`) y «Datos de ejemplo»
  a 26,9 px con la ventana a 0,96 (`text_below_floor`; ahora 29,2 px → 28 px).
- `npx hyperframes snapshot --review`: `.hyperframes/artifacts/snapshots/acd0224c-45d2-419d-81dc-e90afa0e0f7e/` (`review-beats-1…7`,
  `review-seam-01…66`, `review-phone-1…7`). Además, los 50 cuadros del SPEC §6 y los cuatro rangos (`--range` 25,9–26,4, 35,9–36,4,
  69,9–70,3 y 29,8–30,3).
- **Notas que salieron de ahí, ya corregidas:** la píldora tapaba «0 marcadas» y «8 marcadas» en el 813–869 (P0, §4.4); «Guardar asistencia»
  quedaba fuera de la ventana tras el salto del 870 (P0, §4.4); `kpisDer` mostraba media ventana vacía (P1, §4.4); `ultima` y
  `tendenciaMeta` cortaban la columna del medio a media palabra, y `ultima` y `asistencia` dejaban ver la barra fija de la app arriba (P2);
  `chips` mostraba media barra de la app (P2); la frase del «¡Listo!» tocaba los bordes a ×1,18 (P2).
- **El render cuadro a cuadro:** 16 cuadros clave extraídos con ffmpeg (780 la marca sobre «Volver a la lista», 842 «8 marcadas», 903 el
  paso ②, 960 sin chips y «Y», 1084 el látigo con su desenfoque, 1099 las cifras quietas, 1562 la zona, 1802 la lista, 1922 reordenada,
  2012 «Jorge Gallego», 2233 «10 personas», 2408 Ximena, 2654 la ventana a 0,96, 2758 el dip, 2760 y 2909 el cierre). Los cortes dentro de
  pantallas quietas no se ven: diferencia media entre el cuadro anterior y el del corte **0,00/255** en el 1471 y el 1651 y 0,01 en el 900;
  1,76 en el 1200 y 1,35 en el 1861 son el primer cuadro del movimiento de cámara que arranca ahí, no un salto de la app.
- `ffprobe`: H.264 1920×1080, 30 fps, **2910 cuadros, 97,000 s**; AAC 48 kHz estéreo; 22,3 MB.
- La hoja a 360 px: las frases se leen; la app del computador no (es 16:9 para computador, YouTube y presentaciones).
- **Nadie oyó el sonido ni vio el movimiento a velocidad real fuera del render:** el sonido está medido, no oído.
- Mirado: el primer cuadro del cierre (2760) es la noche del kit antes de que suba la corona; es la pieza aprobada del kit, no un hueco del
  montaje.

## 7. El plano más débil y qué cambiaría con más tiempo

- **La zona sin evento** (1560–1679): una sola zona de un cuadro chico; el golpe más fuerte de la música cae sobre una capa pobre. Con
  más tiempo: regrabar con 5 personas (plan B del SPEC) para que salgan varias zonas, o dar el golpe del 1560 a «Dónde viven» y cambiar la
  frase 7 por «Y dónde vive tu gente» (riesgo previsto en el SPEC §7).
- **`kpisDer`** (1200–1259): las cuatro tarjetas ocupan el tercio del medio de la ventana y arriba y abajo hay blanco de la app.
- **El texto del computador en el celular:** en la hoja a 360 px (`review-phone`) la app del computador no se lee; las frases sí. Es el
  formato pedido (16:9 para el sitio, YouTube y presentaciones).
- **La píldora «Datos de ejemplo»** tapa a ratos contenido de la app abajo a la izquierda (el inicio de una fila de la lista, «El reporte
  necesita señal…»): es la posición que pidió el dueño; nunca tapa lo que se toca ni la cifra del plano.
- Los encuadres heredados del clip (0–719) cortan lo mismo que en el clip («Hombre» en `hojaAlta`); no se tocaron, por pedido.
