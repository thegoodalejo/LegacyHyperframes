# REVIEW · Recorrido del módulo: Membresía (16:9)

2026-10-30 · Construido en HyperFrames 0.8.221 contra [SPEC.md](SPEC.md) (historia en [STORY.md](STORY.md)). 97,0 s = 2910 cuadros a 30 fps,
1920×1080: el cuerpo 0–2759 y el cierre del Comercial 2760–2909. El dueño ya no revisa: construido, verificado, renderizado y entregado.
**Render:** `renders/recorrido-membresia-16x9.mp4` (§7).

## 1. Qué hay

| Archivo | Qué es |
|---|---|
| `index.html` | **Generado** por `_gen/gen.py`. La raíz: los hosts de los textos y del cierre, **una sola `.k-ventana`** con sus cuatro mundos, los 57 tramos de video, las marcas de toque, la cámara, los iris, los látigos, los tres morph, el dip, la música en tres segmentos y los sonidos |
| `_gen/gen.py`, `_gen/index.tpl.html`, `_gen/README.md` | El generador: las tablas de tramos, marcas, sonidos y textos (gen.py) y la plantilla con los encuadres y el morph. Ayudas de revisión: `diff.py`, `shift.py`, `sheet.py`, `snap.py` |
| `compositions/fondo.html` | La noche con el halo y los puntos; el halo se asienta en 0, 180, 780, 960, 1080, 1560, 1920, 2280 y 2640 |
| `compositions/frase-1..9.html`, `ceja-1..5.html` | Las nueve frases y las cinco cejas, cada una en su lugar (celular: x 120, ceja y 428, frase y 476 a 88 px en 2 líneas; escritorio: x 240, ceja y 76, frase y 118 a 84 px en 1 línea) |
| `identidad/cierre-comercial.html` | El cierre del kit (92,0–97,0), campanas en el 92,38 |
| `assets/grabaciones/` | Las cuatro grabaciones nuevas y, copiadas del clip, `grabacion.mp4`, `grabacion-2.mp4`, `pasos.json`, `pasos-2.json` |
| `assets/stills/`, `assets/audio/` | Los stills del clip (466 y 2401); las tomas b/c de `toque` (del clip) y las nuevas b/c de `aparicion` y `desliz` (±3 % de tono, hechas igual: `asetrate` 1,03 / 0,97) |

## 2. Los planos

| Plano | Cuadros | Grabación · cámara |
|---|---|---|
| P1–P7 | 0–959 | El clip tal cual (G1 `v01`–`v25`, G2 `v26`–`v29`), con los mismos cuadros, toques, sonidos e irises; encuadres con el ancho visible del clip y piso G16 (§1.4 del SPEC) |
| P8 Su historia | 960–1079 | G2 `v29`. 960 → F16 sobre «Avance»; **1020 → F16 sobre «Historial de pasos»** («Empezó “Mensaje de bienvenida”», «Cumplió “Llamada de bienvenida”», «Reporte de…», «Empezó…» · 30-10-2026 17:14 · Jorge Gallego Gil). Frase 4 y ceja salen 1071–1075 |
| Morph | 1074–1086 | Celular → escritorio, corte de contenido en el 1080 |
| P9 Coordinar | 1080–1559 | R1 `coordinar.mp4`, recortes D/D⁺ |
| Morph | 1554–1566 | Escritorio → celular |
| P10 El semáforo | 1560–1919 | R2 `semaforo.mp4` |
| Látigo | 1914–1924 | La ficha de Sara sube, la pirámide llega de abajo |
| P11 El discipulado | 1920–2279 | R3 `discipulado.mp4` |
| Morph | 2274–2286 | Celular → escritorio |
| P12 Los tableros | 2280–2759 | R4 `tableros.mp4`; la página sin desplazar (capa A) y la desplazada (capa B) unidas en una sola |
| Dip | 2757–2759 | |
| P13 El cierre | 2760–2909 | `cierre-comercial` (iglesia, prueba, sitio, noche, es) |

## 3. Las grabaciones medidas (cuadro a cuadro, `_gen/diff.py`)

| Grabación | Cuadros | Lo que cambia y cuándo |
|---|---|---|
| R1 coordinar (1920×1080, 872) | | quieto 0–158 · lista 162–165 · «Repartir» se hunde 317 · diálogo 321–327 · botón del diálogo 418 · cierre 422–425 · la K del cargador 430–508 · resultado 509 con «Actualizando…» hasta el 521, **limpio desde el 522** · «Quienes acompañan» 709 · una barra parpadea 713–758 · quieto 759–871 |
| R2 semaforo (1170×2532, 1117) | | quieto 0–412 · «Agregar filtro» 415–420 · la hoja sube 422–427 · fila 504 · el editor 509 · «Rojo» 622–628 · «Aplicar» 683–687 · la hoja se va 689–691 · lista filtrada 692 · fila 919 · «Cargando…» 928 · ficha con «Actualizando…» 933 · **ficha limpia 936** |
| R3 discipulado (1170×2532, 657) | | «Discipulado» 60–65 · pirámide 235 · **desplazamiento de 7 px CSS en el 387** (`ver` del paso 5) · nivel nuevo 441 |
| R4 tableros (1920×1080, 683) | | quieto 0–376 · el menú 384–386 · se cierra 453–456 · **desplazamiento instantáneo de 453 px CSS en el 506** (medido con `shift.py`: error medio 1,0) |

Los toques de `pasos.json` (cuadro del dedo) y su imagen: en R1 y R4 el botón se hunde en el mismo cuadro del toque; en R2 la onda de la app
aparece 2 cuadros después (415 por 413) y la casilla «Rojo» se marca 7 después (622 por 615, al soltar). El montaje pone el pulso en el cuadro
del toque y corta la espera hasta el resultado.

## 4. Sincronía: cada cosa con su cuadro y su pulso

Acto 1 (0–959): sin cambios respecto del clip (REVIEW del clip §3), comprobado en la vista previa (0, 195, 603, 783, 975). Lo nuevo, medido en
snapshots cuadro a cuadro (`--at` en f/30 + 0,001) y, el sonido, en el render (§7):

| Qué | Imagen (cuadro) | Pulso | Sonido (pico) | Desvío |
|---|---|---|---|---|
| F16 → «Historial de pasos» | 1020–1033 | 1020 | — | 0 |
| Frase 4 y ceja salen | 1071–1075 | — | — | 0 |
| **Morph al escritorio; corte de contenido** | 1074–1086 (1080) | **1080** | desliz a 1080 (+3 dB) | 0 |
| «COORDINAR» · frase 5 | 1086 · 1095–1105 | 1095 | aparicion a 1087 | 0 |
| Toque «Nuevos» (R1 159) · la lista completa (R1 165) | 1140 · 1142 | 1140 | toque c 1141 | 0 |
| Cámara → «Repartir» | 1170–1183 | 1170 | — | 0 |
| **Toque «Repartir»** (R1 318) · iris · el diálogo completo (R1 330) | **1200** · 1203 | **1200** | toque a 1201 (+3 dB) · aparicion b 1204 | 0 |
| Cámara D⁺ → el diálogo | 1230–1243 | 1230 | — | 0 |
| Toque «Repartir» del diálogo (R1 418); se cierra (422–424) | 1290 · 1294–1296 | 1290 | toque b 1291 | 0 |
| **«Se repartieron 257 personas.» y «Todos los nuevos tienen quién los acompañe.»** (R1 522) · punch D⁺ | **1320** (–1328) | **1320** | confirmacion 1321 (+3 dB) | 0 |
| Toque «Quienes acompañan» (R1 707) · la lista (R1 759) | 1380 · 1383 | 1380 | toque c 1381 | 0 |
| Cámara D · D⁺ · D sobre la carga | 1395 · 1440 · 1500 | 1395 · 1440 · 1500 | — | 0 |
| Frase 5 y ceja salen | 1551–1555 | — | — | 0 |
| **Morph al celular** | 1554–1566 (1560) | **1560** | desliz b 1560 | 0 |
| «SEMÁFORO DE ACTIVIDAD» · frase 6 | 1566 · 1575–1585 | 1575 | aparicion b 1567 | 0 |
| Toque «Agregar filtro» (R2 414) · la hoja sube | 1620 · 1628–1633 | 1620 | toque a 1621 | 0 |
| Cámara → «Semáforo de actividad» | 1635–1648 | 1635 | — | 0 |
| Toque «Semáforo de actividad» (R2 502) · el editor (R2 509) · cámara → los colores | 1665 · 1668 · 1665–1678 | 1665 | toque b 1666 | 0 |
| Toque «Rojo» (R2 621) · la casilla se marca | 1710 · 1711–1713 | 1710 | toque c 1711 | 0 |
| Toque «Aplicar» (R2 683) · la lista roja «62 de 1.324» (R2 692) | 1740 · 1744 | 1740 | toque a 1741 · aparicion c 1744 | 0 |
| Cámara → la lista filtrada | 1755–1768 | 1755 | — | 0 |
| **Toque en Sara Yepes Muñoz** (R2 918) · iris · la ficha limpia (R2 936) | **1800** · 1803 | **1800** | toque b 1801 (+3 dB) | 0 |
| Punch → «Actividad: Rojo · hace 31 días» | 1860–1868 | 1860 | — | 0 |
| Cámara → «Llamar» · «WhatsApp» | 1890–1903 | 1890 | — | 0 |
| **Látigo vertical** | 1914–1924 (1920) | **1920** | desliz c 1920 | 0 |
| «DISCIPULADO» · frase 7 | 1926 · 1950–1956 | 1950 | aparicion c 1927 | 0 |
| Cámara → la cabeza «24 directos · 725 en total» | 1980–1993 | 1980 | — | 0 |
| **Toque en la cabeza** (R3 232) · iris · la pirámide (R3 238) | **2040** · 2043 | **2040 (1,00)** | toque c 2041 · aparicion a 2044 (+3 dB los dos) | 0 |
| Cámara → la raíz · → «Sus discípulos directos (12)» | 2055 · 2100 | 2055 · 2100 | — | 0 |
| **Toque «PA Hernán… y PA Luz Elena…»** · iris · el nivel nuevo (R3 443) | **2160** · 2163 | **2160** | toque a 2161 | 0 |
| Cámara → el nivel · → las migas | 2175 · 2220 | 2175 · 2220 | — | 0 |
| Frase 7 y ceja salen | 2271–2275 | — | — | 0 |
| **Morph al escritorio** | 2274–2286 (2280) | **2280** | desliz a 2280 (+3 dB) | 0 |
| «TABLEROS» · frase 8 | 2286 · 2295–2303 | 2295 | aparicion a 2287 | 0 |
| Cámara → el semáforo · punch → 954 · 165 · **62** · 143 | 2340 · 2400 | 2340 · 2400 | — | 0 |
| Cámara → la descarga · toque (R4 380) · «PDF · Excel» (R4 386) | 2460 · 2490 · 2493 | 2490 | toque b 2491 · aparicion b 2494 | 0 |
| Escape (R4 453) · cámara → el crecimiento (la capa B) | 2520 · 2520–2533 | 2520 | — | 0 |
| Cámara D⁺ → el final de la curva | 2580–2593 | 2580 | — | 0 |
| Frase 8 y ceja salen · **frase 9** (Que 2640 … pierda 2648) | 2636–2640 · 2640 | **2640** | — | 0 |
| Cámara → la gráfica abierta | 2700–2713 | 2700 | subida 2714–2771 | 0 |
| Dip · **cierre** | 2757–2759 · **2760** | **2760** | golpe de la subida 2761 · campanas 2771 | 0 |

Ninguna acción a más de 1 cuadro de su pulso. Ningún compás del 1080 al 2759 sin toque o movimiento, salvo el 45 (2640–2699), que tiene la
entrada de la frase 9 y el halo, como pide el SPEC.

## 5. Desvíos del SPEC y su porqué

1. **Las cifras reales** reemplazan las del SPEC: «257 personas nuevas esperan Acompañante.» y «Se repartieron 257 personas.»; «Acompaña a
   11 de 12 · Red Timoteo» (no «3 de 4»); el filtro «Rojo» deja «62 de 1.324» y la ficha es la de Sara Yepes Muñoz, «Actividad: Rojo · hace 31
   días»; una sola cabeza («Pr Andrés … y Pr Carolina … · 24 directos · 725 en total») y abajo «PA Hernán … y PA Luz Elena … · 12 directos ·
   162 en total» con las migas; Membresía 1.324 (+49,8 %) y el semáforo Verde 954, Amarillo 165, Rojo 62, Sin actividad 143.
2. **El escritorio, siempre recortado (D = 720×380 CSS, D⁺ = 640×338).** La página de la app mide 1024 px CSS de ancho útil (184–1208): ningún
   recorte la cabe entera. Por eso: en el 1170 la cámara va a la derecha («Repartir» y la columna de «Asignar»; los nombres quedan fuera) y en el
   1203 el diálogo nace a medias dentro del encuadre hasta que la cámara llega a él en el 1230; en el 1500 se vuelve a la izquierda de las cuatro
   filas («Acompaña a N de 12» y el arranque de la barra) en vez del final de las barras (que sin los nombres no decía nada); en los tableros el
   semáforo se lee en dos planos sobre las mismas filas: 2340 a la izquierda («Verde · Amarillo · Rojo · Sin actividad») y el punch del 2400 a
   la derecha (la barra y 954 · 165 · **62** · 143 con su %). «La gráfica entera» del 2700 es el centro de la gráfica (título, «2.000», la curva y
   las fechas), no sus 992 px CSS.
3. **El desplazamiento de los tableros (453 px CSS, instantáneo en el R4 506) lo hace la cámara**, como el de la ficha en el clip: la página
   sin desplazar (capa A) y la desplazada (capa B, 453 px más abajo, sin su barra fija de 57 px CSS) son una sola página de 1173 px CSS; la
   cámara del 2520 la recorre de la descarga al crecimiento sin un salto (el SPEC suponía un desplazamiento suave de 300 ms). En 2524–2528 el
   encuadre pasa por el centro vacío de la tarjeta del semáforo (las etiquetas quedan a la izquierda y las cifras a la derecha): es un cuadro
   de paso con desenfoque, no un hueco de la grabación (comprobado ocultando cada capa).
4. **El desplazamiento de 7 px del discipulado (R3 387) no se usa:** del 2043 al 2162 corre la pirámide de antes (238–357) y el nivel nuevo
   (443→) entra en el 2163; la marca del toque del 2160 va 7 px CSS más abajo que `toques[]` (en la imagen de antes del desplazamiento).
5. **Se cortan las esperas reales:** la K del cargador de «Repartir» (R1 430–508) y el «Actualizando…» (509–521) — el resultado entra limpio en
   el 1320 con el R1 522; el parpadeo de una barra de «Quienes acompañan» (713–758) — de 708 a 759; «Cargando…» y «Actualizando…» de la ficha
   (R2 928–935); la salida de la hoja del filtro (689–691) — de la onda de «Aplicar» a la lista roja completa en el 1744.
6. **«Datos de ejemplo» a 28 px (píldora de 52)** dentro de la ventana, abajo a la izquierda, del 0 al 2759, viajando con la ventana en los
   morph (el clip usaba 31 px por su ventana a 0,92; aquí no hay ese paso).
7. **Encuadres del celular que no son el nivel del SPEC:** 1680 → F16 y no M16 (M16 cortaba «Aplicar», que se toca en el 1740) y la cámara
   baja **en el 1665**, con el toque, porque el editor aparece en el 1668 debajo del encuadre de la hoja; el punch del 1860 es ×1,70 (44 px) y
   no C16 (C16 cortaba «días»); 2055 → F16 (el nombre de la raíz va de x 24 a 330 CSS: M16 lo cortaba); 2220 → F16 sobre las migas enteras
   (24–336 CSS; C16 las cortaría). El 1980 encuadra «Quienes encabezan la pirámide (1)» y la cabeza (CSS 230–580): la demo tiene una sola cabeza
   y debajo la página está vacía.
8. **El morph** se escribe cuadro a cuadro (valores calculados y unidos en línea recta, seek-safe): la ventana interpola su caja con
   `power3.inOut` en 12 cuadros y cada mundo se escala desde el centro lo justo para cubrir la ventana más su corrimiento de ±160 px; en ningún
   cuadro se ve el fondo de la ventana (mirado en el render: 1072–1090, 1552–1566, 2272–2290). `check` no marcó la animación de la caja.
9. **El látigo C2 → C3** usa dos ranuras de 720×900 en una tira (`--f-latigo` 1000): entre las dos queda una franja de 100 px del fondo de la
   app que solo se ve, borrosa, en 1918–1921 (como la del clip).
10. **Sonidos nuevos:** `aparicion-b/c` y `desliz-b/c` (±3 % de tono con `asetrate`, como las tomas de `toque`); el acento de `desliz` b/c se
    corrige con el tono (0,194 / 0,206 s). Se quitó la `subida` del 1036 (la única va al cierre).

## 6. La música: la edición y la costura medida

| Segmento | `data-start` | `data-media-start` | Dura | Volumen (carril, t del clip) |
|---|---|---|---|---|
| `musica-a` | 0 | 14,05 | 52,0 | 0,7 · 0,7 en 51,933 → 0 en 52,0 |
| `musica-b` | 51,933333 | 25,983333 | 40,066667 | 0 → 0,7 en 0,0667 · 0,7 hasta 40,0 → 0 en 40,0667 |
| `musica-c` | 91,933333 | 81,983333 | 4,066667 | 0 → 0,7 en 0,0667 · 0,7 hasta 0,2667 (92,2) → 0,25 en 0,4667 (92,4) |

Tal cual el SPEC §0.1. **Medido en el render** (ebur128, sonoridad momentánea cada 100 ms): 51,5 −17,7 · 51,8 −17,8 · 51,9 −17,6 · **52,0 −16,8**
· 52,1 −16,7 · 52,2 −16,1 · 52,4 −17,4 (sin hueco; la subida de 52,0–52,3 es el ataque del compás más el `desliz` b del morph, pico en el 52,0).
91,5 −17,6 · 91,8 −17,0 · **92,0 −16,2** · 92,2 −17,3 · 92,4 −20,6 · 92,5 −21,1 · 92,7 −19,0 (el golpe final con la `subida`, y la caída a 0,25 debajo
de las campanas del 92,38). **El clic, en la música sola** (los tres segmentos mezclados con ffmpeg con las mismas ganancias y rampas por
muestra): salto máximo entre muestras 0,025 en 51,8–52,2 contra 0,017–0,035 en los compases vecinos, y 0,024 en 91,8–92,2; pico de muestra
0,40 en el empalme contra 0,36–0,37 de los vecinos (+0,7 dB, el ataque del compás 13). **Sin clic ni hueco**: no hizo falta el cruce de 4
cuadros. `hyperframes audio` no detecta silencio en el cuerpo; el único silencio es la cola 94,39–97,0, debajo del cierre quieto (la pista se
apaga sola, como pide el SPEC).

## 7. Check, revisión, render y mezcla

- **`npx hyperframes check --json`: 0 errores**, 1 aviso que se deja a propósito: `composition_file_too_large` (la raíz lleva los 57 tramos de
  video para que se vean y se recorten en la línea de tiempo; la fuente de verdad es `_gen/gen.py`). Runtime, layout, motion, contraste (25/25),
  craft (599 muestras) y audio sin avisos.
- **Snapshots** (`.hyperframes/artifacts/snapshots/`): la grilla de §4 del SPEC en dos pasadas; los cambios de la app cuadro a cuadro
  (52 cuadros: 1139–1142, 1199–1203, 1289–1297, 1319–1320, 1379–1383, 1619–1633, 1664–1668, 1709–1713, 1739–1744, 1799–1803, 2039–2043,
  2159–2163, 2489–2493, 2519–2526) y `--review` (`07a23c4f-…/review-beats-1..7.jpg`, `review-seam-01..82.jpg`, `review-phone-1..7.jpg`).
  A 360 px se leen las frases, las cejas y «Datos de ejemplo»; el escritorio en D se lee como recorte.
- **Lo que la revisión corrigió:** la ranura de la pirámide quedaba vacía en el 2040 (el tramo de abajo terminaba con el toque: ahora sigue
  hasta el 2046, debajo del iris); el punch del chip cortaba «días» (×1,70); la raíz y las migas se cortaban a la izquierda (F16); el editor de
  colores aparecía fuera del encuadre (la cámara baja con el toque del 1665); «Tableros» cortado arriba en el 2280 (y 265); el plano del 1500
  mostraba solo barras (vuelve a los nombres); la gráfica del 2700 (centro).
- **El render** se miró entero cada 45 cuadros y cuadro a cuadro en los tres morph, el látigo, el iris de la pirámide, el desplazamiento de los
  tableros, el dip y el cierre.

**Render:** `renders/recorrido-membresia-16x9.mp4` — `render --quality high`, 22,0 MB, H.264 1920×1080 a 30 fps, **2910 cuadros, 97,000 s** (ffprobe), AAC 48 kHz estéreo, en 8 min 35 s (captura por capturas de pantalla: el desenfoque de movimiento lo pide). Un render anterior (antes de los últimos seis encuadres) dio la misma mezcla al decimal.

**La mezcla (medida, no oída):** integrada **−17,2 LUFS**, pico real **−1,4 dBTP**, pico de muestra −1,6 dBFS, **0 recortes**, máximo de corto plazo −15,9 LUFS. Queda en «en torno a −17» y bajo −1 dBTP: **no se normalizó** (subir a −16 llevaría el pico real por encima de −1 y obligaría a limitar). Niveles: toques clave y confirmaciones a 1,4, el resto a 1,0, música a 0,7 (0,25 bajo el cierre). `hyperframes audio` encuentra los golpes en los cuadros **61 · 91 · 121 · 151 · 376 · 451 · 496 · 601 · 721 · 781 · 841 · 1141 · 1201 · 1291 · 1381 · 1621 · 1666 · 1711 · 1741 · 1801 · 2041 · 2161 · 2491**: exactamente la lista del SPEC §4.12, cada toque un cuadro después de su imagen.

## 8. Lo que conviene mirar

- **El sonido nadie lo oyó**: los golpes, la sonoridad y los empalmes están medidos (§6, §7); conviene escuchar los dos empalmes (52,0 y 92,0)
  y la caída de la música debajo de las campanas del 92,38.
- **Los planos de escritorio** son el punto más débil: la app de escritorio tiene 1024 px CSS de ancho útil y D solo ve 720, así que en el 1170
  («Repartir» con filas vacías a la izquierda) y en el paso del 2524–2528 (el centro de la tarjeta del semáforo) el recorte muestra más fondo de
  tarjeta que texto. Con más tiempo: grabar el escritorio a 1024×576 CSS o a 2× (SPEC §5) para que D vea la página entera.
- **El látigo del 1914** deja ver, borrosa, la franja de 100 px entre las dos ranuras (1918–1921), igual que el del clip.
- **La cola**: del 94,39 al 97,0 no hay música (la pista termina sola); el cierre queda quieto en silencio 2,6 s.
- **Directivas:** `KingdomApp/docs/videos/README.md` todavía dice 60–75 s para el clip del sitio; este recorrido dura 97 s (SPEC §5).
- **9:16 y otros idiomas** quedan para después (SPEC §5).
