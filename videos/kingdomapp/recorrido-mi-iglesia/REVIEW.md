# REVIEW · Recorrido de Mi iglesia — «Se enteró toda la iglesia… y encontró su lugar» (16:9)

2026-10-30 · Construido en HyperFrames 0.8.221 a partir de [SPEC.md](SPEC.md) y [STORY.md](STORY.md). Usa la grabación del clip
(`assets/grabaciones/clip/grabacion.mp4`) y las dos nuevas: `assets/grabaciones/celular.mp4` (1170×2532, 30 fps, 2884 cuadros) y
`assets/grabaciones/escritorio.mp4` (1920×1080, 30 fps, 1682 cuadros), cada una con su `-pasos.json` y su `-hoja.jpg`. El dueño ya no revisa: se
construyó, se verificó y se renderizó sin paradas. **Entrega:** `renders/recorrido-mi-iglesia-16x9.mp4`.

## 1. Qué hay

| Archivo | Qué es |
|---|---|
| `index.html` | La raíz, **generada** por `_gen/gen.py` desde `_gen/index.tpl.html`: el formato (`--f-*`, `--e-*` y `window.KD`), los hosts de las escenas y `#escena`, la tira horizontal con las dos ventanas; los 64 tramos de video, los 5 stills, las 28 marcas de toque, las 7 cámaras, los 2 iris, los 4 látigos, los aterrizajes, la ventana que se hace a un lado, el dip, la música y los 54 sonidos |
| `compositions/fondo.html` | La noche del sitio. El halo se asienta en 0 · 180 · 720 · 960 · 1320 · 1560 · 2040 · 2280 (a mano) |
| `compositions/frase-1…11.html`, `ceja.html` | Las once frases y la ceja «MI IGLESIA» con sus dos lugares (generadas) |
| `identidad/cierre-comercial.html` | El cierre del Comercial del kit v1.1 (2760–2909), `{"publico":"iglesia","llamado":"prueba","contacto":"sitio","fondo":"noche","idioma":"es"}`, campanas en el 92,38 |
| `_gen/gen.py`, `_gen/index.tpl.html`, `_gen/README.md` | El generador: las tablas de tramos, stills, marcas, sonidos y frases, y la plantilla con las cámaras |
| `_gen/musica.sh` | Regenera `assets/musica/product-launch-recorrido.wav` desde el mp3 (el `ffmpeg` del SPEC §0.1; `npm run musica`) |
| `assets/grabaciones/clip/` | La grabación del clip, su `pasos.json` y su hoja, copiadas sin cambios |
| `assets/stills/still-354.png`, `still-705.png`, `still-1258.png` | Los stills del clip (el iris del 180 y las dos compensaciones) |
| `assets/stills/still-c486.png` | La tarjeta de Jóvenes tocada (rec. 486), debajo del iris del 960 (961–966) |
| `assets/stills/still-c2277.png` | El primer cuadro pintado de la bienvenida de Lucía (rec. 2277), mientras llega el último látigo (2270–2279) |
| `assets/audio/toque-b.wav`, `toque-c.wav` | Las tomas b y c de `toque`, copiadas del clip |

```text
#escena (x 0 = celular · x −1920 = escritorio; látigos 1310–1320, 1550–1560, 2030–2040 y 2270–2280)
  #ventana-cel.k-ventana.k-ventana-16x9 (x 1104 · y 90 · 720×900)
    #mK   #camT1 (still 354) · #cam > #m1 > #m1in (el clip, 0–841) con #iris1 · #camT2 (la marca del 180)
    #mC1  #camC1 (celular.mp4, 841–961) · #irisC1 > #camC1b (961–1320)
    #mC2  #camC2 (celular.mp4, 1550–2040)
    #mC3  #camC3 (still c2277 2270–2280 · celular.mp4 2280–2760)
    #datos-cel · #dip
  #ventana-esc.k-ventana.k-ventana-escritorio (x 2160 · y 260 · 1440×760)
    #mE1 > #camE1 (escritorio.mp4, 1310–1560) · #mE2 > #camE2 (escritorio.mp4, 2030–2280) · #datos-esc
```

## 2. Los planos

«grab.» es el cuadro de la grabación del clip; «rec.», el de `celular.mp4` o `escritorio.mp4`. **Todos los tramos van a 1×**: en vez de acelerar,
se cortan las esperas (la pantalla está quieta o es un esqueleto, un cargador o una página en blanco, así que el corte no se ve o cae con el
cambio de pantalla).

| Plano | Cuadros | Grabación y cámara |
|---|---|---|
| P1–P7 El clip | 0–719 | Los mismos 32 tramos, 3 stills, 14 marcas, el iris del 180, el corte del 662 y las tres compensaciones del clip (SPEC §2.1). Cámaras con `s' = max(s, 1,085)` y los centros de la tabla del SPEC (`inscripcion` 550, `quienes` y `botonesForm` 561, `resultado` y `verBoleta` 543). La ceja entra en el 195 |
| P8 «Su boleta, también sin señal.» | 720–869 | La boleta en grande del clip (grab. 1405–1523) en G `grande`; **780 → G `cerrarK`** (CSS 284–733): entran «Congreso de Jóvenes» y «Cerrar» por encima de la píldora. **840: toque en «Cerrar»** (la marca se posa en el 836) y **corte sobre el toque** en el 841 a «Mis boletas» de `celular.mp4` (rec. 153): el código **FM75UZ**, «Descargar la boleta» y la barra, en G `boletas` (CSS 395–844). «Datos de ejemplo» sube encima de la barra (841–872) para no tapar «Comunidades» |
| P9 «Encuentra su comunidad.» | 840–1319 | **870: «Comunidades»** (rec. 234); corte en el 873 a «Todavía no estás en una comunidad» (rec. 249; la carga y la página que todavía se pinta, 237–248, quedan fuera) en G `vacio` (CSS 121–570). **900: «Explorar comunidades»** (rec. 332); corte en el 903 a Explorar con Matrimonios «Para ti» (rec. 344). **930: la app baja a Jóvenes** (rec. 412, un salto) y el encuadre cambia con ella a G `jovenesCard`. **960: toque en la portada de Jóvenes** (rec. 486) e **iris** 960–965, con el still de la rec. 486 debajo; dentro, la comunidad ya pintada (rec. 505) en G `comunidad`. 1020 → G `lideres` (CSS 395–844): «Unirme», «Conectar con un líder» y Andrés en «Líderes». **1080: «Unirme»** (rec. 680); en el 1082 (rec. 691) el botón ya no está, «Miembros: 23» y el confeti de la app (691–745). **1140: «Conectar con un líder»** (rec. 816); en el 1143 el diálogo (rec. 830) en G `dialogo`. «Voy al congreso y quiero conocerlos.» se escribe a 1× entre el 1171 y el 1251 (rec. 885–965), con la cámara quieta. **1260: «Enviar»** (rec. 1011); en el 1263 «Pediste conectar con un líder · Un líder te escribirá pronto.» con el confeti de la tarjeta (rec. 1029) |
| P10 «Su mensaje llega a los líderes.» | 1320–1559 | **Látigo al escritorio** 1310–1320 (aterriza 1,04 → 1,00). Contactos (rec. 91–163) en D `fila` (CSS 205–916 × 345–720): Isabella, María José y **Gabriela «Jóvenes · hace 1 min» con su mensaje**. 1350 → D `tomar` (CSS 415–1126). **1380: «Tomar»** (rec. 161); corte en el 1383 (la K del cargador, rec. 169–323, queda fuera) al detalle (rec. 324) en D `detalle`: «Tomado · hace 1 min · Lo tomó Andrés Felipe Restrepo Gómez», su mensaje, «Llamar 5557877437», «Escribir por WhatsApp», con el confeti de la fila detrás. 1440 → D⁺ `detalleCerca` |
| P11 «Y un líder la acompaña.» | 1560–1679 | **Látigo de vuelta** 1550–1560 al celular de Gabriela: Jóvenes con **«Andrés Felipe Restrepo Gómez te acompañará · Te escribirá pronto para conocerte.»** (rec. 1544–1676) en G `acompana` (CSS 246–695). **1575: punch** a ×1,3 `acompanaM` sobre la tarjeta. 1620 → G `barraC2`, con «Objetivos» en la barra |
| P12 «Crece paso a paso.» | 1680–2039 | **1680: «Objetivos»** (rec. 1674); corte en el 1683 a «Mis objetivos» (rec. 1691) en G `objetivos`: «Un devocional cada mañana · Paso 13 de 14 · 86 %», «Hoy · Servir». **1740: la tarjeta** (rec. 1797); corte en el 1743 al objetivo (rec. 1808) en G `objetivo`. **1800: «Lo hice»** (rec. 1913); corte en el 1803 (rec. 1924): «¡Listo! Marcamos «Servir» como hecho.» entra 1804–1808 y **en el 1811 el anillo pasa a «Paso 14 de 14 · 93 %»** con «Mañana · Esperanza» (rec. 1932). 1860 → ×1,2 `anillo`. **1920: la app baja a «Todos los pasos»** (rec. 2085, un salto) y el encuadre cambia con ella a G `pasos`: Perdón, La palabra, Gozo, **Servir «Hoy»** y Esperanza «Mañana» |
| P13 «Y sabes quién respondió.» | 2040–2279 | **Látigo al escritorio** 2030–2040. El tablero del Portal (rec. 1010; la carga 666–1005 queda fuera) en D `cifras`: 21 terminaron la bienvenida, 41 objetivos en curso, 66 %, 90 personas en comunidades, 33 % y 730 inscritos. **2100: la app baja a «Las 21 más recientes»** (rec. 1248) y el encuadre cambia con ella a D `tabla`: «Inscripciones abiertas · Toda la iglesia», alcance 1.324. **2160: toque en «Inscripciones abiertas»** (rec. 1305); corte en el 2163 (la carga y el `ver` de la novedad, 1309–1455, quedan fuera) a «Quién reaccionó» (rec. 1456) en D `quien`: «Todas · 57», 👍 42, 8, 2, **🙌 5**. **2220: toque en 🙌** (rec. 1565); corte en el 2223 (la K 1571–1573 queda fuera) a la lista (rec. 1574): **«Gabriela Hinestroza Perea 🙌» primera**, «Isaac Gómez Sepúlveda». 2235 → ×1,9 `gabrielaLista` |
| P14 La bienvenida y el cierre | 2280–2909 | **Látigo de vuelta** 2270–2280 a otra persona: la bienvenida de **Lucía**. Mientras llega, el still de la rec. 2277 (el primer cuadro pintado); desde el 2280 (rec. 2278), la coreografía de la app: el logo con su resorte, «Hola, Lucía», «Hoy empieza algo hermoso», el texto y el botón, en G `portada` (CSS 201–650). **2400: «Empezar mis primeros pasos»** (rec. 2474); corte en el 2403 (rec. 2483): la portada se va y entra «Tus primeros pasos» con su animación, en G `camino` (CSS 76–525). La frase del sitio entra entre el 2519 y el 2533; la ceja se va en 2520–2523; la ventana pasa a 0,92 (+24) en 2524–2538; `subida` desde el 90,533; dip 2757–2759; **2760: `cierre-comercial`**, con las campanas en el 92,38 |

## 3. Sincronía (parte 2; la parte 1 es la del clip, REVIEW del clip §3)

El sonido cae un cuadro después de la imagen: `data-start` = (imagen + 1) / 30 − acento. Cada resultado entra en el corte de su espera, 1 a 3
cuadros después del toque (como en Equipos), y su sonido (`aparicion` o `confirmacion`) cae un cuadro después.

| Qué | Imagen | Pulso (fuerza) | Sonido | Desvío del SPEC |
|---|---|---|---|---|
| **Toque en «Cerrar»** · «Mis boletas»; sale la frase 4 y entra «Encuentra» | 840 · 841 · 842 | **840 (1,00)** | `toque` a 841 | 0 |
| **«Comunidades»** · «Todavía no estás en una comunidad» | 870 · 873 | 870 | `toque` b 871 | resultado 885 → 873 |
| **«Explorar comunidades»** · Explorar | 900 · 903 | 900 (0,84) | `toque` c 901 | resultado 915 → 903 |
| La app baja a Jóvenes (la cámara con ella) | 930 | 930 | `desliz` 931 | 0 |
| **Toque en Jóvenes** + iris, **en la costura de la música** | 960–965 | **960 (0,92)** | `toque` a 961 | 0 |
| Cámara → «Líderes» | 1020–1033 | 1020 | — | 0 |
| **«Unirme»** · el confeti y «Miembros: 23» | 1080 · 1082 | 1080 (0,76) | `toque` b 1081 · `aparicion` 1083 | toque a 1,0 (SPEC 1,4) |
| **«Conectar con un líder»** · el diálogo | 1140 · 1143 | 1140 (0,75) | `toque` c 1141 · `aparicion` 1144 | diálogo 1155 → 1143 |
| El mensaje se escribe | 1171–1251 | — | — | 0 (SPEC 1170–1246) |
| **«Enviar»** · «Pediste conectar con un líder» | 1260 · 1263 | 1260 (0,63) | `toque` a 1261 · `confirmacion` 1264 | 1275 → 1263 |
| Látigo al escritorio; frase 6 | 1310–1320 · 1323–1333 | **1320 (0,93)** | `desliz` 1,4, acento 1320 | 0 |
| Cámara → «Tomar» | 1350–1363 | 1350 | — | 0 |
| **«Tomar»** · el detalle | 1380 · 1383 | 1380 (0,90) | `toque` b 1381 · `aparicion` 1384 | toque a 1,0 |
| Cámara → D⁺ sobre el detalle | 1440–1453 | 1440 (0,96) | — | 0 |
| Látigo de vuelta; «… te acompañará»; frase 7 | 1550–1560 · 1562–1570 | **1560 (1,00)** | `desliz` 1561 | 0 |
| Punch sobre la tarjeta | 1575–1583 | 1575 | `confirmacion` 1,4, 1576 | ×1,3 (SPEC C = 1,8) |
| Cámara → la barra | 1620–1633 | 1620 (0,84) | — | 0 |
| **«Objetivos»** · «Mis objetivos» | 1680 · 1683 | 1680 (0,98) | `toque` c 1681 | 1695 → 1683 |
| **La tarjeta** · el objetivo | 1740 · 1743 | 1740 | `toque` a 1741 | 1755 → 1743 |
| **«Lo hice»** · «¡Listo!…» · el anillo a 93 % | 1800 · 1803 · 1811 | **1800 (0,93)** | `toque` b 1801 · `aparicion` 1804 | toque a 1,0 |
| Cámara → el anillo | 1860–1873 | 1860 | — | ×1,2 (SPEC M) |
| La app baja a «Todos los pasos» (la cámara con ella) | 1920 | **1920 (1,00)** | `desliz` 1921 | 0 |
| Látigo al escritorio; frase 9 | 2030–2040 · 2043–2049 | 2040 | `desliz` 2041 | 0 |
| La app baja a la tabla (la cámara con ella) | 2100 | 2100 (0,91) | `desliz` 2101 | 0 |
| **«Inscripciones abiertas»** · «Quién reaccionó» | 2160 · 2163 | **2160 (1,00)** | `toque` c 2161 · `aparicion` 2164 | 2175 → 2163 |
| **🙌** · «Gabriela Hinestroza Perea 🙌» primera | 2220 · 2223 | 2220 | `toque` a 2221 · `confirmacion` 1,4, 2224 | 2235 → 2223 |
| Cámara → su fila (×1,9) | 2235–2248 | **2235 (1,00)** | — | ×1,9 (SPEC D⁺) |
| Látigo de vuelta: la bienvenida de Lucía; frase 10 | 2270–2280 · 2282–2290 | 2280 | `desliz` 2281 | 0 |
| **«Empezar mis primeros pasos»** · el camino | 2400 · 2403 | 2400 (0,74) | `toque` b 2401 · `aparicion` 2404 | 0 |
| Frase del sitio · la ventana a un lado | 2519–2533 · 2524–2538 | 2520 | — | 0 |
| `subida` · dip · **el cierre** | 90,533 · 2757–2759 · **2760** | 2760 | campanas 92,38 | 0 |

**Ninguna acción cae fuera de su pulso.** Los toques del SPEC están todos en su cuadro; lo que se movió son los resultados, que entran en el
corte de la espera (2–3 cuadros después del toque) y no en el pulso siguiente. Así ninguna espera de la app queda en pantalla y los
cargadores (la K de la novedad, la de «Tomar» y la de la lista de 🙌) quedan fuera. Los toques rotan a · b · c sin repetir: 841 a, 871 b, 901 c,
961 a, 1081 b, 1141 c, 1261 a, 1381 b, 1681 c, 1741 a, 1801 b, 2161 c, 2221 a, 2401 b.

## 4. Desvíos del SPEC y su porqué

1. **Lo que trajo la grabación** (con lo que se ajustó el SPEC): la boleta grande se abre en la rec. 57 y «Cerrar» en la 146; el mensaje se
   escribe desde la 878 (la primera letra en la 885) y se envía en la 1011; de la 1177 a la 1477 el pastor toma el contacto fuera de cámara (no
   se usa) y **la tarjeta «… te acompañará» aparece en la rec. 1484, no en la 1438** (1438–1477 todavía es la bandeja del pastor en el celular,
   con su avatar «AF»). «Lo hice» pasa de «Paso 13 de 14 · 86 %» a «Paso 14 de 14 · 93 %». En el escritorio, **la K del cargador de «Tomar» va
   de la rec. 169 a la 323** (no 270–330) y el detalle aparece en la 324; el tablero termina de cargar en la 1005; el `ver` de las
   publicaciones pasa primero por la mitad de la tabla (rec. 1143) y llega a «Las 21 más recientes» en la 1248; «Quién reaccionó» dice
   **Todas · 57 y 🙌 5**.
2. **Cada resultado entra en el corte de su espera** (2–3 cuadros después del toque), no en el pulso siguiente como planeaba el SPEC
   (885, 915, 1155, 1275, 1695, 1755, 2175, 2235). Es el pedido «corta las esperas» y es lo que hace Equipos. Los toques no se movieron.
3. **Lo que se cortó de la app:** las páginas en blanco y los esqueletos (243–248, 339–343, 495–504, 1682–1690, 1805–1807), el botón gris de
   «Unirme» (687–690), el diálogo que se va y la tarjeta que cambia antes de «Pediste…» y su fundido de entrada (1019–1028), **el aviso «Lo que marcaste espera señal
   para enviarse.»** de la API local (rec. 1921–1923, con un 93 % optimista que después vuelve a 86 %: contradice la historia), el cambio de
   cuenta a Lucía con su K (2238–2276) y, en el escritorio, las tres K del cargador y las cargas del tablero y de la novedad.
4. **«Datos de ejemplo» tapa lo que queda abajo a la izquierda** de cada encuadre. Los encuadres se eligieron para que nunca tape un toque
   ni el dato de la frase: `vacio` deja «Explorar comunidades» encima (por eso el título «Comunidades» queda fuera), `comunidad` deja «Unirme»
   encima, `acompana` deja a Andrés encima (David queda debajo), `pasos` deja «Esperanza · Mañana» encima y `fila` empieza en el x 205 para
   que el mensaje de Gabriela quede a la derecha de la píldora. En `boletas` el toque es en «Comunidades», debajo de la píldora: **la píldora
   sube 150 px, encima de la barra de la app, entre el 841 y el 872** (los dos cambios caen en cortes). Donde no hubo otra salida: en `tomar`
   la píldora tapa el comienzo del mensaje (ya leído en `fila`), en `portada` tapa «5 pa» de «5 pasos cortos» y en la lista de 🙌 tapa a Isaac.
5. **El punch del 1575 va a ×1,3, no a C (1,8):** la tarjeta mide 340 px CSS y en M (279 visibles) quedaban fuera el avatar o el «te»; a
   ×1,3 entra entera y el texto queda en 34 px. **El 1860 va a ×1,2** (no M) por lo mismo: el anillo y «Un devocional cada mañana» van de x 19
   a 341. **La lista de 🙌 va a ×1,9** (no D⁺): a 2,0 no entran a la vez el avatar y el 🙌 de la derecha.
6. **El escritorio no cabe entero en un encuadre de lectura** (D = 711 px CSS de ancho): la fila de Gabriela va primero por su nombre y su
   mensaje (`fila`) y después a «Tomar» (`tomar`); en la tabla se ven el título y el alcance (1.324), no las reacciones ni la respuesta (la
   fila mide 1.080 px); en el tablero entran seis cifras de ocho (quedan fuera «4 Contactos esperando» y «489 Reacciones»). Detrás del
   detalle, la bandeja sigue diciendo «Pendientes: 5» bajo el velo: la app no recarga la lista hasta cerrar el diálogo, y «Pendientes: 4 ·
   Tomados: 2» aparece después de la rec. 546, que no se usa.
7. **El camino de Lucía no cabe entero** (84–806 px CSS): `camino` muestra el título y los tres primeros pasos y no se mueve en el 2460 (el
   SPEC lo dejaba «si cabe»). Así el cuadro final, al lado de la frase del sitio, lleva el título «Tus primeros pasos».
8. **El último látigo llega con un still:** mientras el celular entra (2270–2279) se ve el primer cuadro pintado de la bienvenida (rec.
   2277, el fondo con «Lo haré después»), porque los cuadros de antes son la cuenta de Gabriela con el avatar de Lucía y la K del cargador. La
   coreografía de la app empieza en el aterrizaje (2280 = rec. 2278).
9. **Niveles** (el pedido manda sobre el SPEC): toques a 1,0 (el SPEC ponía 1,4 en «Unirme», «Tomar» y «Lo hice»), confirmaciones clave a
   1,4 (la de «Pediste…» a 1,0, como dice el SPEC), el primer látigo a 1,4 y la música a 0,75.
10. **«Datos de ejemplo» a 31 px** (alto 56), no a los 22 del kit para 16:9: lo mismo que el clip y Equipos (con la ventana a 0,92 sigue en
    ≥ 28 px).

## 5. La música, la costura y la mezcla

- **La edición** es la de Academia y Equipos (SPEC §0.1), regenerable con `_gen/musica.sh` (`npm run musica`): pista 14,05–46,04 +
  22,01–fin, con 30 ms de cruce. `ffprobe`: **95,997 s**. El archivo es idéntico byte a byte al de `recorrido-equipos` (`cmp`).
- **La costura (31,96–31,99 del video), medida:** el mayor salto entre muestras a ±45 ms del cruce es 0,032, contra un percentil 99,9 de 0,027 en
  el segundo anterior: no hay clic. La energía en 400 ms pasa de −16,9 dB a −15,6 dB: es el golpe del compás, que cae en el 32,0, con el toque
  en Jóvenes y su iris encima. La grilla de 0,5 s sigue pareja entre el 31,0 y el 33,0 (medida en Equipos sobre el mismo archivo). **No se oyó.**
- **Los niveles:** música a 0,75 en el carril de volumen de principio a fin, sin fundido (el último acorde se apaga solo debajo del cierre);
  toques a 1,0; `aparicion` a 1,0 (1,4 la del «Amén» del clip); `confirmacion` a 1,4 en el punch de «… te acompañará» y en «Gabriela
  Hinestroza Perea 🙌» (y en el «¡Quedaste inscrito!» del clip), a 1,0 en «Pediste…»; `desliz` a 1,4 en el primer látigo y a 1,0 en los
  demás; `subida` y campanas a 1,0.
- **Antes de renderizar** se simuló la mezcla con `ffmpeg` (`recorrido-eventos/_gen/mix.py`, las mismas fuentes, tiempos y carriles): −17,0 LUFS,
  pico real −1,7 dBTP.
- **El render:** **−17,0 LUFS integrados, pico real −1,8 dBTP, LRA 2,8 LU** (`ffmpeg ebur128=peak=true`), sin recortes. Es el «en torno a
  −17» del pedido, con el pico por debajo de −1 dBTP; no se normalizó (el SPEC pedía −16: se dejó en −17 como el clip y Equipos). El silencio
  empieza en el 95,74 (el último acorde y las campanas se apagan solos).

## 6. Lo que se revisó

- `npx --yes hyperframes@0.8.221 check --json`: **0 errores**. Un aviso que se deja a propósito: `composition_file_too_large` (790 líneas).
  La raíz lleva los 64 tramos para que se vean y se recorten en la línea de tiempo, como el clip y Equipos; la genera `gen.py`.
- `npx hyperframes snapshot --review`: `.hyperframes/artifacts/snapshots/3a924b09-db44-4e11-93c9-7d0632540ad7/` (`review-beats-1…7.jpg`,
  75 `review-seam-*.jpg`, `review-phone-1…7.jpg`), sin notas del revisor. Antes, una ronda de 52 cuadros clave (`c6afbdbf…`). Lo que salió de
  las dos rondas y del primer render, ya corregido:
  - **P0:** el logo de la bienvenida de Lucía cortado arriba y el título «Tus primeros pasos» fuera del encuadre del camino. Las medidas de
    esos dos encuadres estaban corridas 20 px CSS; se midieron otra vez por píxel (logo 227–284, título 84–105) y se corrigieron `portada`
    y `camino`.
  - **P0 (primer render):** tres cortes caían en un cuadro todavía sin pintar. En el 873 se veía la página en blanco, en el 1683 el esqueleto de
    «Mis objetivos» y en el 1263 el fundido cruzado de «Pediste…». Los tramos empiezan ahora 2 a 3 cuadros después (rec. 249, 1691 y 1029).
  - **P1:** el punch de «… te acompañará» cortaba el avatar o el final del texto (M = 1,4). Ahora va a ×1,3, centrado en el contenido de la
    tarjeta (x 44–326).
  - **P1:** «Un devocional cada mañana» cortado a la derecha en `anillo` (×1,25). Ahora es ×1,2 y llega al x 343.
  - **P1:** «Datos de ejemplo» sobre «Comunidades» en el toque del 870 (§4.4) y sobre «Explorar comunidades» en el encuadre vacío.
  - **P2:** el 🙌 de la derecha al borde en la lista (×1,9, cx 494 → 500).
- **El render, cuadro a cuadro** (cuadros extraídos con `ffmpeg` alrededor de cada toque, corte, iris, látigo y del cierre):
  - cada marca de toque cae en su pulso, sobre su botón;
  - el 841 ya es «Mis boletas» con FM75UZ y la barra; el 873 «Todavía no estás en una comunidad»; el 903 Explorar; el 961–965 el iris;
  - en el 1082 el botón «Unirme» ya no está y empieza el confeti; en el 1143 el diálogo; el mensaje se escribe entre el 1171 y el 1251; en el
    1263 «Pediste conectar con un líder»;
  - en el escritorio, el 1383 es el detalle con «Lo tomó Andrés Felipe Restrepo Gómez», sin la K;
  - el 1560 es «Andrés Felipe Restrepo Gómez te acompañará»; el 1683 es «Mis objetivos»; el 1803 es «¡Listo!…» y el 1811 «93 %»;
  - el 2163 es «Quién reaccionó · Todas · 57 · 🙌 5» y el 2223 la lista con Gabriela primera;
  - el 2280 es la bienvenida de Lucía, el 2403 el camino, el dip cae en 2757–2759 y el cierre en el 2760.
- `ffprobe` del render: H.264 1920×1080, 30 fps, **2910 cuadros, 97,000 s**; AAC 48 kHz estéreo; unos 17 MB.
- **El primer cuadro del cierre (2760) es noche sin nada:** la baldosa de la K del kit entra con opacidad 0 → 1. En Equipos y en la muestra
  del kit es igual, y el kit no se edita por video. El `snapshot` dibuja la K abajo a la derecha (mide antes de que el host sea visible); el
  render la pone bien.
- La vista previa del editor no se abrió: nadie la iba a mirar y el render se verificó cuadro a cuadro. **Nadie oyó el sonido ni vio el
  movimiento a velocidad real.**
- El disco C: quedó con menos de 1 GB libre y el render se negaba («Low disk space»). Los temporales del render se mandaron a
  `.hyperframes/tmp-render` (en F:) con `TMP`/`TEMP`, y la carpeta se borró al terminar.

## 7. Lo que conviene mirar

- **La costura del 32,0**, con audífonos: está medida, nadie la ha oído. Encima caen el toque en Jóvenes y el iris.
- **El ritmo de los resultados:** los resultados entran 2 a 3 cuadros después del toque, no en el pulso siguiente (§4.2). Si se siente
  apurado, la válvula es dejar ver la espera real de la app en los toques que la tienen corta (la de «Conectar con un líder» dura 14 cuadros y
  caería en el pulso 1155 sin cortar nada).
- **El escritorio de cerca:** la tabla de publicaciones se ve sin «Reacciones 57 · 4 %» y el tablero sin «4 Contactos esperando». Una
  grabación de escritorio a 1024 px de ancho los pondría en un solo encuadre D.
- **El confeti de «Unirme»** nace en el botón y sube a la portada, fuera del encuadre `lideres`. Se ve cuando cae (1090–1130), no cuando
  estalla.
- **«Pendientes: 5»** sigue detrás del detalle, bajo el velo (§4.6).
