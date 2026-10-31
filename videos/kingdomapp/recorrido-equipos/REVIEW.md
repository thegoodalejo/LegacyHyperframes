# REVIEW · Recorrido de Equipos — «Falta uno en Parqueadero… y el domingo, cubierto» (16:9)

2026-10-30 · Construido en HyperFrames 0.8.221 a partir de [SPEC.md](SPEC.md) y [STORY.md](STORY.md). Usa la grabación del clip
(`assets/grabaciones/parqueadero/grabacion.mp4`) y las dos nuevas: `assets/grabaciones/celular.mp4` (1170×2532, 30 fps, 2416 cuadros) y
`assets/grabaciones/escritorio.mp4` (1920×1080, 30 fps, 760 cuadros), cada una con su `-pasos.json`. El dueño ya no revisa: se construyó, se
verificó y se renderizó sin paradas. **Entrega:** `renders/recorrido-equipos-16x9.mp4`.

## 1. Qué hay

| Archivo | Qué es |
|---|---|
| `index.html` | La raíz, **generada** por `_gen/gen.py` desde `_gen/index.tpl.html`. Tiene el formato (`--f-*`, `--e-*` y `window.KD`), los hosts de las escenas y `#escena`, la tira horizontal con las dos ventanas. Además: los 46 tramos de video, los 4 stills, las 18 marcas de toque, las 7 cámaras, los 3 iris, los látigos, los aterrizajes, la ventana que se hace a un lado, el dip, la música y los 42 sonidos |
| `compositions/fondo.html` | La noche del sitio. El halo se asienta en 0 · 180 · 720 · 840 · 1320 · 1800 · 2280 (a mano) |
| `compositions/frase-1…9.html`, `ceja.html` | Las nueve frases y la ceja «EQUIPOS» con sus dos lugares (generadas) |
| `identidad/cierre-comercial.html` | El cierre del Comercial del kit v1.1 (2760–2909), con `{"publico":"iglesia","llamado":"prueba","contacto":"sitio","fondo":"noche","idioma":"es"}` y las campanas en el 92,38 |
| `_gen/gen.py`, `_gen/index.tpl.html`, `_gen/README.md` | El generador: las tablas de tramos, marcas, sonidos y frases, y la plantilla con las cámaras |
| `assets/grabaciones/parqueadero/` | La grabación del clip y su `pasos.json`, copiadas sin cambios |
| `assets/stills/still-362.png`, `still-1132.png` | Los stills del clip, que van debajo de los iris del 120 y del 375 |
| `assets/stills/still-c1106.png` | El inicio de Servir de Jorge con la tarjeta «Cerrar el turno» a la vista (rec. 1106), de 1803 a 1926 |
| `assets/stills/still-c1486.png` | El cuadro justo antes del aviso de guardado sin señal (rec. 1486), de 2168 a 2175 |
| `assets/audio/toque-b.wav`, `toque-c.wav` | Las tomas b y c de `toque`, copiadas del clip |
| `assets/musica/product-launch-recorrido.wav` | «Product Launch» editada como en Academia (§5) |

```text
#escena (x 0 = celular · x −1920 = escritorio; látigos 830–840 y 1310–1320)
  #ventana-cel.k-ventana.k-ventana-16x9 (x 1104 · y 90 · 720×900)
    #tira (látigo vertical: −1000 en 356–366, 0 en 656–666, −1000 en 2270–2280)
      #m1 > #m1in    #cam1 · #iris1>#cam1b (clip, 0–840) · #cam3 · #iris3>#cam3b (celular.mp4, 1310–2281)
      #m2 > #m2in    #cam2 · #iris2>#cam2b (clip, 356–667) · #cam4 (celular.mp4, 2270–2760)
    #datos-cel · #dip
  #ventana-esc.k-ventana.k-ventana-escritorio (x 2160 · y 260 · 1440×760)
    #e1in > #camE1 (escritorio.mp4, 830–1320) · #datos-esc
```

## 2. Los planos

«rec.» es el cuadro de la grabación. **Todos los tramos van a 1×.**

| Plano | Cuadros | Grabación y cámara |
|---|---|---|
| P1–P7 El clip | 0–719 | Los mismos 24 tramos, los mismos stills, cortes, iris y látigos del clip. Las cámaras usan `s' = max(s, 1,085)` (SPEC §2.1). La ceja entra en el 195 y se queda |
| P8 «Y el domingo, completo.» | 720–839 | El turno del líder quieto en `cierre`, que ahora es ×1,2 con **cy 350** (antes 362): en 16:9 el borde de arriba cortaba «Servicio General». Se ven «5 de 5», los botones, Parqueadero con Rut y Gabriela «Confirmado», y la píldora sobre «Entrada» |
| P9 «Lo que falta, antes del domingo.» | 840–1319 | **Látigo horizontal al escritorio** 830–840 (aterriza 1,04 → 1,00 en 840–850). Primero la cobertura arriba, rec. 48–117, en D `arriba` (CSS 180–891 × 229–605): el selector «Dom, 1 de nov…», «Solo lo que falta» y «13 de 19 confirmados (68 %)», con las pestañas fuera. **900: la app baja a Seguridad** (rec. 118, un salto real) y el encuadre cambia con ella a D `seguridad` (CSS 180–891 × 200–576): Seguridad, la barra verde llena, Rut y Gabriela «Confirmado», Entrada y Rondas, con «Redes sociales» fuera. 960 → D⁺ `gabrielaE` (×2,0) en la costura de la música. 1020 → D `cifraSeg` (CSS 515–1226 × 212–588): «5/5 · 100 %» y «1/1 · 100 %». **1080: la app vuelve arriba** (rec. 298) con la cámara quieta, y se ven el interruptor, PDF · Excel y «2/7 · 29 %» en rojo. 1095 → `arriba`. **1140: toque en «Solo lo que falta»** (rec. 422). En el 1143 corta (425→427) al interruptor encendido, sin Dirección ni Seguridad, solo con lo que falta. 1200 → D `faltaAlab`: Alabanza con «Por confirmar» en ámbar y Guitarra y Teclado «Vacante» en rojo |
| P10 «Cada equipo, con su chat.» | 1320–1799 | **Látigo horizontal de vuelta** 1310–1320. El chat de Alabanza (rec. 132–264) en G `chatTop`: «Alabanza · Integrante», el anuncio anclado «Gabriel Rodríguez Castro ¡Hola, equipo! Ensay…», Emilia y la encuesta. 1380 → ×1,25 `encuesta`. **1440: toque en «Way Maker»** (rec. 262). En el 1443 corta (265→269) a «Way Maker» marcada, 7 → 8 y «11 personas votaron». **1500: la app baja al ensayo** (rec. 336, salto real) con la cámara quieta. **1560: toque en «Asistiré»** (rec. 428), con el punch a C `asistire`. En el 1563 corta (431→440) al botón lleno y «Van 10 · no van 1». 1620 → G `caja`. **1680: toque en la caja** (rec. 601). Entre 1681 y 1739 se escribe «¡Cuenten conmigo el jueves!» a 1× (rec. 643–701). **1740: «Enviar»** (rec. 750). En el 1743 el mensaje ya está en el hilo (rec. 758). 1770 → G `barra`, con «Servir» a la derecha de la barra de abajo |
| P11 «Servir cuenta.» | 1800–2279 | **1800: toque en «Servir»** (rec. 876). Corte sobre el toque en el 1803 al inicio de Servir ya desplazado (still de la rec. 1106), en ×1,16 `servirCard` (CSS 27–363 × 11–431), con aterrizaje 1,03 → 1,00 desde el punto tocado. **1920: toque en la fila «Seguridad · Servicio General»** e iris 1920–1925 hacia «Cerrar el turno» (rec. 1188–1306), en G `cerrarCabeza` (CSS 14–373 × 156–606): «5 sirvieron · 0 no llegaron», Gilberto, Gabriela y Julián con «Sirvió». 1980 → G⁺ `gabrielaFila`. **2040: «No llegó»** de Julián (rec. 1307). En el 2043 (rec. 1362) Julián sale en rojo y «4 sirvieron · 1 no llegaron». 2100 → G `barraCerrar`. **2160: «Cerrar el turno»** (rec. 1479–1486) y el still de la rec. 1486 hasta el 2175. **2175: el aviso entero** (rec. 1502–1607) en G `avisoAbierto` y punch a ×1,18 `aviso` (2175–2184): «El turno quedó cerrado · 1 persona cumplió su objetivo de servir en la ruta. · Entendido» |
| P12 «Y da un paso en su ruta.» | 2280–2519 | **Látigo vertical** 2270–2280 al celular de Gabriela (rec. 1844–1919), en G `gabrielaTop`: «Buenas noches, Gabriela». 2310 → G `gabrielaBarra`, con «Objetivos» en la barra. **2340: toque en «Objetivos»** (rec. 1914). Corte sobre el toque en el 2346 (rec. 1927; la página en blanco 1922–1926 queda fuera). «Mis objetivos» sube y **el check de «Servir» se cierra en el 2355** (rec. 1936), con «Cumplido el vie, 30 de oct». 2400 → ×1,6 `servirOk` |
| P13 La frase del sitio | 2520–2759 | «Que cada puesto / de servicio / esté *cubierto*» de 2520 a 2532. La ceja se va en 2520–2523. La ventana se hace a un lado (0,92, +24) en 2524–2538. `subida` desde el 90,533. Dip 2757–2759 |
| P14 El cierre | 2760–2909 | `cierre-comercial`, con las campanas en el 92,38 |

## 3. Sincronía (parte 2; la parte 1 es la del clip, REVIEW del clip §3)

El sonido cae un cuadro después de la imagen: `data-start` = (imagen + 1) / 30 − acento.

| Qué | Imagen | Pulso (fuerza) | Sonido | Desvío |
|---|---|---|---|---|
| Látigo al escritorio; frase 5 palabra a palabra | 830–840 · 843–853 | **840 (1,00)** | `desliz` 1,4, acento 840 | 0 |
| La app baja a Seguridad | 900 | 900 (0,84) | `desliz` 901 | 0 |
| Cámara → Gabriela (D⁺) sobre **la costura de la música** | 960–973 | 960 (0,92) | — | 0 |
| Cámara → «5/5 · 100 %» | 1020–1033 | 1020 | — | 0 |
| La app vuelve arriba (cámara quieta) | 1080 | 1080 (0,76) | `desliz` 1081 | SPEC 1035 (§4.2) |
| Cámara → el interruptor y el total | 1095–1108 | 1095 | — | SPEC 1050 |
| **Toque en «Solo lo que falta»** · solo lo que falta | 1140 · 1143 | 1140 (0,75) | `toque` a 1141 · `aparicion` 1144 | SPEC 1080 · 1083 (§4.2) |
| Cámara → lo que falta en Alabanza | 1200–1213 | 1200 | — | 0 |
| Látigo de vuelta; frase 6 | 1310–1320 · 1322–1330 | **1320 (0,93)** | `desliz` 1,4, acento 1320 | 0 |
| Cámara → la encuesta | 1380–1393 | 1380 (0,90) | — | 0 |
| **Toque en «Way Maker»** · 7 → 8 | 1440 · 1443 | 1440 (0,96) | `toque` b 1441 | 0 |
| La app baja al ensayo | 1500 | 1500 (0,88) | `desliz` 1501 | 0 |
| **Toque en «Asistiré»** + punch · lleno y «Van 10» | 1560 · 1563 | **1560 (1,00)** | `toque` c 1561 · `aparicion` 1564 | 0 |
| Cámara → la caja | 1620–1633 | 1620 | — | 0 |
| **Toque en la caja** · se escribe | 1680 · 1681–1739 | 1680 (0,98) | `toque` a 1681 | 0 |
| **«Enviar»** · el mensaje en el hilo | 1740 · 1743 | 1740 | `toque` b 1741 · `aparicion` 1744 | 0 |
| Cámara → la barra con «Servir» | 1770–1783 | 1770 | — | 0 |
| **Toque en «Servir»** · corte sobre el toque; frase 7 | 1800 · 1803 · 1802–1804 | 1800 (0,93) | `toque` c 1801 | 0 (el corte a +3, como el 75→78 del clip) |
| Nada entre 1875 y 1915 (el redoble) | — | — | — | 0 |
| **Toque en la fila** · iris | 1920 · 1920–1925 | **1920 (1,00)** | `toque` a 1921 | 0 |
| Cámara → la fila de Gabriela | 1980–1993 | 1980 | — | 0 |
| **«No llegó»** · Julián en rojo | 2040 · 2043 | **2040 (1,00)** | `toque` b 2041 | 0 |
| Cámara → la barra | 2100–2113 | 2100 | — | 0 |
| **«Cerrar el turno»** | 2160 | **2160 (1,00)** | `toque` c 2161 | 0 |
| **El aviso «1 persona cumplió su objetivo…»** + punch | 2175 · 2175–2184 | **2175 (1,00)** | `confirmacion` 1,4, 2176 | 0 |
| Látigo vertical a Gabriela; frase 8 | 2270–2280 · 2282–2294 | 2280 | `desliz` 1,4, acento 2280 | 0 |
| Cámara → la barra con «Objetivos» | 2310–2323 | 2310 | — | 0 |
| **Toque en «Objetivos»** · corte sobre el toque | 2340 · 2346 | 2340 | `toque` a 2341 | 0 (el corte a +6, §4.4) |
| **El check de «Servir» se cierra** | 2355 | 2355 | `confirmacion` 1,4, 2356 | SPEC 2369 (§4.4) |
| Cámara → «Servir» cumplido | 2400–2413 | 2400 (0,76) | — | 0 |
| Frase del sitio · la ventana a un lado | 2520–2532 · 2524–2538 | 2520 (0,80) | — | 0 |
| `subida` | — | — | 90,533 (golpe en el 2761) | 0 |
| Dip · **el cierre** | 2757–2759 · **2760** | 2760 | campanas 92,38 | 0 |

**Ninguna acción cae fuera de su pulso.** Las tres que se movieron (el salto arriba, el toque en «Solo lo que falta» y el check) se movieron a
otro pulso, no a un contratiempo.


## 4. Desvíos del SPEC y su porqué

1. **Lo que trajo la grabación:** «Buenas noches, Gabriela»; «Cumplido el vie, 30 de oct»; el chat dice «Van 9 → Van 10» y «7 → 8 votos».
   El inicio de Servir de Jorge tiene, encima de «Cerrar el turno», la tarjeta **«Por cubrir · Seguridad · 1 por cubrir»**: en la base de
   la grabación de celular nadie llenó la vacante del próximo domingo. Ninguna frase depende de eso.
2. **El escritorio, reordenado dentro de sus compases.** En la grabación «5/5 · 100 %» está a la derecha de la tarjeta (x CSS ≈ 1190) y
   los nombres a la izquierda (x 200–480). En D (711 px CSS de ancho) no caben juntos. Por eso hay un encuadre propio para la cifra
   (`cifraSeg`, 1020). Para que se pueda leer más de un instante, la vuelta de la app arriba pasó del 1035 al **1080** y el toque en «Solo
   lo que falta», del 1080 al **1140** (la misma fuerza, 0,75 contra 0,76). Se quitó el encuadre aparte de «2/7 · 29 %» del SPEC, que era
   una cifra roja sobre un gris vacío. La cifra se ve en 1080–1094, cuando la app vuelve arriba con la cámara a la derecha. **Audiovisual
   (3/4 · 75 %)** no entra en ningún encuadre de lectura. Con «Solo lo que falta» encendido queda debajo del borde de la grabación (la
   escena no desplazó la página), y en `seguridad` está más abajo que Medios. El SPEC lo dejaba «si cabe».
3. **El celular no cabe en M** en casi ninguna pantalla de la parte 2: el texto va de x 16 a x 374. Por eso `encuesta` va a ×1,25 (las
   cuentas «0 · 7 · 3» están en x 290), `cerrarCabeza` y `barraCerrar` a G (×1,085) y `gabrielaFila` a G⁺. El texto de 14 px queda entre
   28 y 32 px. El SPEC pedía ≥ 36 px en la fila de Gabriela; quedan 30. En `asistire` (C, ×1,8) y `servirOk` (×1,6) llega a 46 y 41 px.
4. **El check de «Servir» se cierra en el 2355, no en el 2369.** En la grabación la página entra en blanco (1922–1926) y la lista y el check
   se animan juntos en 9 cuadros (1927–1936). Para que el check cerrara en el 2369, habría que dejar 23 cuadros de página en blanco o
   repetir el esqueleto. El corte sobre el toque va a +6 (2346, el primer cuadro con contenido) y el check se cierra en el 2355, un pulso
   de la grilla (0,50).
5. **La fecha del turno cerrado nunca se ve** (BANNED 40 y el pedido del dueño):
   - En el inicio de Servir, la fila de la tarjeta trae «Dom, 25 de oct · 9:00 a. m.» (CSS 437–452) debajo del nombre (410–426). El
     encuadre `servirCard` (×1,16) pone el borde de abajo en el CSS 431: el nombre queda, la fecha no.
   - Arriba de «Cerrar el turno», la línea «Domingo, 25 de octubre» (CSS 140–154) queda encima del borde de `cerrarCabeza` (156).
   - El precio: la píldora «Datos de ejemplo» cae sobre «Seguridad · Servicio» en la fila de la tarjeta (se lee «General») y el toque se
     dibujó en la fila, 8 px CSS más arriba que en `pasos.json` (y 414 en vez de 422), para que no pise el borde que esconde la fecha. No
     hay encuadre de lectura (≥ 1,085) que muestre el nombre por encima de la píldora sin mostrar la fecha.
   - Por eso **no hay movimiento de cámara en el 1860** (el SPEC pedía M): cualquier encuadre más cerrado corta el texto de la tarjeta
     (x 30–357).
6. **Lo que se cortó de la app:** la carga del inicio de Servir (886–946); el esqueleto de «Cerrar el turno» (1112) y el desplazamiento
   previo al toque (1103–1105); el aviso «Quedó guardado en este dispositivo: se enviará solo al volver la señal» (rec. 1487–1494), que la app
   muestra con la API local y contradice la historia (lo tapa el still de la rec. 1486); la entrada del diálogo (1495–1501); el cambio de
   cuenta a Gabriela (1714–1790) y su página en blanco (1922–1926); la onda de «Asistiré» (431–439) y la de la vista (265–268).
7. **El aviso entra con un corte de encuadre.** Con la barra de abajo en cuadro, el título «El turno quedó cerrado» quedaba fuera, arriba,
   en el primer cuadro del aviso. En el 2175 la cámara salta a G sobre el aviso entero (es un corte con causa: la pantalla cambia) y el punch
   lo acerca a ×1,18.
8. **«Datos de ejemplo» a 31 px** (alto 56), no a los 22 del kit para 16:9. Es lo mismo que el clip: con la ventana a 0,92 (2524–2759)
   sigue en ≥ 28 px, el piso que mide `check`.
9. **El encadenado a 1×:** tramos de video, nunca acelerados. Las pausas de la app que no le tocan a ningún pulso se cortan en cuadros
   quietos de la grabación, sin que se vea el corte.

## 5. La música, la costura y la mezcla (medidas, no oídas)

- **La edición** es la de Academia (SPEC §0.1): pista 14,05–46,04 + 22,01–fin, con 30 ms de cruce. `ffprobe`: **95,997 s**. El
  `recorrido-academia` no tenía el `.wav`, así que se generó con el comando del SPEC.
- **La costura (31,99 del video, compás quieto de la cobertura, cuadro 960):**
  - El mayor salto entre muestras a ±45 ms del cruce es 0,032, contra un percentil 99,9 de 0,027 en el segundo anterior: no hay clic.
  - La energía en 400 ms pasa de −16,9 dB (antes) a −15,7 dB (después). Ese +1,2 dB es el golpe del compás, que cae en el 32,0.
  - `hyperframes audio … --only beats` da la grilla de 0,5 s pareja de punta a punta: 30,495 · 31,015 · 31,515 · 31,995 · 32,505 · 32,995 ·
    33,455. No hay pulso doble ni perdido entre el 31,0 y el 33,0.
  - **No se oyó.**
- **El render:** **−17,0 LUFS integrados, pico real −2,7 dBTP** (ffmpeg `ebur128` y `hyperframes audio` coinciden), sin recortes,
  LRA 2,8 LU y corto plazo máximo −15,4. Queda dentro del ±1 del SPEC (−16) y en el −17 del clip. No se normalizó: subir 1 dB dejaba
  1,7 dB de margen, pero el pedido era «en torno a −17».
- **Los golpes:** `hyperframes audio` sobre el render detecta los 18 `toque`, cada uno un cuadro después de su imagen:
  - parte 1: 76 · 121 · 151 · 181 · 241 · 301 · 376 · 601;
  - parte 2: **1141 · 1441 · 1561 · 1681 · 1741 · 1801 · 1921 · 2041 · 2161 · 2341**.
  - Las `aparicion`, `confirmacion` y `desliz` quedan por debajo del umbral del detector (están entre 4 y 10 dB bajo la música, como manda el
    kit). Su sitio está en la tabla de §3 y en `gen.py`.
- Música a 0,75 todo el video, sin fundido: el último acorde se apaga solo debajo del cierre. El silencio empieza en el 94,98.


## 6. Lo que se revisó

- `npx hyperframes check --json`: **0 errores**. Hay 1 aviso que se deja a propósito: `composition_file_too_large` (634 líneas). La raíz
  lleva los 46 tramos para que se vean y se recorten en la línea de tiempo, como en el clip. Lo genera `gen.py`.
- `npx hyperframes snapshot --review`: `.hyperframes/artifacts/snapshots/0002d1a9-b596-4388-a5d0-270cd17e8385/` (`review-beats-1…6.jpg`,
  55 `review-seam-*.jpg`, `review-phone-1…6.jpg`). Notas que salieron de las hojas y de dos rondas de cuadros clave, ya corregidas:
  - **P0:** la píldora tapaba «Asistiré» y su toque en `encuesta`. Ahora es ×1,25 con cy 485 y los botones quedan encima de la píldora.
  - **P0:** el mensaje «¡Cuenten conmigo el jueves!» se cortaba a la derecha en `caja` y `barra`. Ahora x llega a 381.
  - **P1:** «Servicio General» cortado arriba en `cierre`, «Cerrar el turno» cortado a la izquierda en `cerrarCabeza` y «Emilia» cortado en
    `chatTop`.
  - **P1:** el título del aviso cortado en su primer cuadro (§4.7).
  - **P1:** dos encuadres de cifra sobre gris vacío en el escritorio (§4.2).
  - **P1:** la «d» de «Por red» asomaba arriba a la izquierda de `cifraSeg`, que ahora empieza en x 515 y en y 212.
- La hoja del celular (360 px) lee las frases; el texto de la app a esa escala es textura, como en todo 16:9 de la serie.
- **El render final, cuadro a cuadro** (los 2910 cuadros extraídos con ffmpeg y mirados en hojas alrededor de cada toque, corte, iris,
  látigo y del cierre):
  - cada marca de toque cae en su pulso, sobre su botón;
  - el toggle está encendido y sin Dirección en el 1143, «Way Maker 8» en el 1443, «Asistiré» lleno y «Van 10» en el 1563, el mensaje en el
    hilo en el 1743 y el inicio de Servir en el 1803;
  - la fecha del turno no aparece en ningún cuadro (1803–1920 y desde el 1921);
  - Julián sale en rojo en el 2043, el aviso entero en el 2175, el check cerrado en el 2355 y el dip en 2757–2759;
  - en el escritorio, las pestañas y «Redes sociales» no aparecen en ningún cuadro de lectura (las pestañas solo cruzan en el látigo, 830–840
    y 1310–1320).
- `ffprobe` del render: H.264 1920×1080, 30 fps, **2910 cuadros, 97,000 s**; AAC 48 kHz estéreo; 16,9 MB. Tardó 10 min 26 s en renderizar.
- **El primer cuadro del cierre (2760) es noche sin nada:** la baldosa de la K del kit entra con opacidad 0 → 1 en 0,35 s. En la muestra
  del kit es igual, y el kit no se edita por video. Desde el 2763 ya se ve la K, centrada. El `snapshot` la dibuja abajo a la derecha (mide
  el favicon antes de que el host sea visible); el render la pone bien.
- La vista previa del editor no se abrió: nadie la iba a mirar y el render se verificó cuadro a cuadro.
- Nadie oyó el sonido ni vio el movimiento a velocidad real.

## 7. El plano más débil y qué cambiaría con más tiempo

- **El inicio de Servir (1803–1919):** la tarjeta «Por cubrir · Seguridad · 1 por cubrir» domina la mitad de arriba y contradice un poco
  el «5 de 5» del clip. Además, la píldora tapa el nombre de la fila. Con más tiempo: volver a grabar la escena de celular con la vacante
  del próximo domingo llenada (el mismo `INSERT` de la escena de escritorio) y con `ver` dejando la fila a mitad de pantalla. Así la fecha
  queda lejos del borde y el encuadre puede bajar a M.
- **El escritorio de cerca deja grandes grises** (`cifraSeg`): las tarjetas de la cobertura son anchas y casi vacías a la derecha. Una
  grabación de escritorio a 1024 px de ancho de ventana pondría cifra y nombres juntos en un D.
- **«Por red»** no se ve en ningún cuadro de lectura; las pestañas quedan siempre encima del borde (CSS 224 contra 229).
