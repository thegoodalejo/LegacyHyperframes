# REVIEW · «Kingdom en un minuto» — «Del que llega al que sirve» (16:9)

2026-10-31 · Revisión del render contra [SPEC.md](SPEC.md). Historia en [STORY.md](STORY.md); generador en [_gen/](_gen/README.md).

## 1. Qué hay

- **59,0 s, 1920×1080, 30 fps** (1770 cuadros): cuerpo 0–1619 + `cierre-comercial` 1620–1769.
- **Render:** `renders/clip-sitio-en-un-minuto-16x9.mp4` (§6).
- `index.html` y `compositions/texto-0..7.html` los genera `_gen/gen.py` (42 tramos de video, 4 stills, 12 marcas, 36 sonidos de acción); el
  fondo (`compositions/fondo.html`) se edita a mano; la música la arma `_gen/musica.sh`.
- Las grabaciones son las de los seis clips aprobados (copiadas sin cambios a `assets/grabaciones/<modulo>.mp4`, con su `pasos.json`) y la de
  Tableros del recorrido de Membresía. Nada se grabó de nuevo. Stills: `eventos-1027` y `mi-iglesia-1258` (de los recorridos), y dos nuevos
  sacados de las grabaciones: `equipos-1392` (el primer cuadro de «Aceptar · No puedo», para el látigo de entrada) y `academia-0` (el primer
  cuadro del profesor, debajo del iris).

## 2. Los planos (lo construido)

| Plano | Cuadros | Lo que se ve | Cómo entra |
|---|---|---|---|
| P1 | 0–119 | «Cada punto / es *una persona.*» (132 px, centrada) | — (la palabra «Cada» en la miniatura) |
| P2 Membresía | 120–299 | «Muy contenta, viene el domingo» → «Marcar cumplido» (180) → «Llamada de bienvenida cumplido · Ahora va en…» (punch en 240) | la ventana sube 110–120 |
| P3 Eventos | 300–479 | «Total: 10 personas» → «Guardar asistencia» (360) → el reporte → «Enviar reporte» (420) → «¡Listo!» «Reportada» | látigo ← 290–300 |
| P4 Academia | 480–719 | 3 5 9 8 del profesor → látigo vertical (590–600) → los cuatro números (600–645) → «¡Listo! Quedó tu asistencia» (660) | iris 479–485 |
| P5 Mi iglesia | 720–959 | «No» → «Inscribir» (780) → «¡Quedaste inscrito!» → «Ver boleta» (840) → el QR (900) → la boleta entera | látigo ↑ 710–720 |
| P6 Comunicaciones | 960–1199 | la invitación (1020) → el reporte → «respondieron» (1080) → los nombres con «Leído» y «Allí estaré» | empuje 950–970 |
| P7 Equipos | 1200–1439 | «Aceptar» (1260) → «¡Gracias por servir! Tu líder ya lo sabe.» → látigo vertical al líder (1316–1326) → «Confirmado», «5 de 5» | látigo → 1190–1200 |
| P8 Síntesis | 1440–1619 | el tablero del pastor (1.324, 448, 145…) → el semáforo de actividad (1530); «Toda tu iglesia, en *una sola app.*» | morph 1434–1446 |
| P9 Cierre | 1620–1769 | `cierre-comercial`: «Kingdom es para toda la iglesia», «Prueba gratis 30 días» | dip 1617–1619 y corte |

Cinco clases de cambio de mundo (subida, látigo horizontal en los dos sentidos, iris, látigo vertical, empuje y morph) más los dos látigos
verticales internos de Academia y Equipos; ninguna clase se repite seguida en el mismo sentido.

## 3. Sincronía (medida, `python _gen/sincronia.py`)

Cada marca de toque contra el cuadro real del toque en su grabación (`pasos.json → toques[].cuadro`), a través del tramo que se ve en ese
cuadro del video; contra su sonido; y contra la grilla:

| Cuadro | Módulo · toque | Grab. vista → toque real | Sonido | Pulso |
|---|---|---|---|---|
| 180 | Membresía · «Marcar cumplido» | 2767 → 2767 (0) | 181 | sí (pico 0,87) |
| 360 | Eventos · «Guardar asistencia» | 1007 → 1007 (0) | 361 | sí |
| 375 | Eventos · «Muy bien» | 1154 → 1154 (0) | 376 | sí |
| 390 | Eventos · «Tema de la palabra» | 1203 → 1203 (0) | 391 | sí |
| 420 | Eventos · «Enviar reporte» | 1308 → 1308 (0) | 421 | sí |
| 735 | Mi iglesia · «No» | 1032 → 1032 (0) | 736 | sí |
| 780 | Mi iglesia · «Inscribir» | 1090 → 1090 (0) | 781 | sí |
| 840 | Mi iglesia · «Ver boleta» | 1259 → 1257 (**+2**) | 841 | sí (0,98) |
| 900 | Mi iglesia · el QR | 1398 → 1398 (0) | 901 | sí |
| 1020 | Comunicaciones · la invitación | 1188 → 1188 (0) | 1021 | sí |
| 1080 | Comunicaciones · «respondieron» | 1329 → 1329 (0) | 1081 | sí (1,09) |
| 1260 | Equipos · «Aceptar» | 1469 → 1469 (0) | 1261 | sí |

- **Imagen y sonido:** los 36 sonidos caen un cuadro después de su imagen (`data-start = cuadro / 30 − acento`); ninguno a más de 1 cuadro.
- **«Ver boleta» (+2):** heredado tal cual del clip aprobado de Mi iglesia. El clic quedó registrado en la grab. 1257, el mismo cuadro en que
  la app desplaza la página 84 px (`scrollIntoView`); el clip sostiene ese salto con el still de la 1258 (compensado por la cámara) y dibuja
  el toque donde el botón ya está quieto y responde (1259–1260). El toque dibujado y su sonido van juntos (840 / 841); lo que difiere es solo
  el registro del clic. No se tocó.
- **Grilla:** los ocho cambios de mundo (120 · 300 · 480 · 720 · 960 · 1200 · 1440 · 1620), todos los toques y todas las imágenes de los
  sonidos caen en múltiplos de 15; en el clímax, en la grilla de negras medida (la detección de pulsos se va a los contratiempos desde el
  1048, SPEC §0.3), nunca en un contratiempo.
- **Las ventanas:** cada momento es el tramo de su clip corrido un número entero de compases (−7, −4, +8, +3, +7 y +11): los tramos, las
  cámaras, las marcas y los sonidos conservan entre sí los cuadros del clip aprobado.

## 4. Desvíos del SPEC y del encargo, y su porqué

1. **La frase de apertura no es «Kingdom es para toda la iglesia».** El encargo la daba como ejemplo, pero el `cierre-comercial` del kit ya
   dice exactamente esa frase sobre el botón: con la síntesis («Toda tu iglesia…») habría sonado tres veces en un minuto. Se usó la otra
   frase del hero, la que el sitio revela al bajar: «Cada punto es una persona.», sobre los puntos del kit. Abre la anáfora de las frases de
   los módulos («Cada persona…», «Cada reunión…», …) y deja la frase del hero para el final, en el cierre.
2. **Las ventanas que entran con movimiento traen 12 cuadros de su clip antes del momento** (`pre` en `gen.py`): la primera vista previa
   mostraba la ventana en blanco durante la subida y los látigos, porque su video empezaba en el cuadro del golpe. En Equipos, el tramo
   anterior del clip es la pantalla desplazada a «Instrucciones»; ahí se usa un still del primer cuadro de «Aceptar · No puedo».
3. **Las frases salen 12 cuadros antes del cambio** (no 6): con 6 la ventana que sale con el látigo pasaba por encima de la frase mientras
   se desvanecía. La apertura sale en 105–109, antes de que suba la ventana.
4. **Limitador en el bus maestro.** Los toques clave caen a propósito en los golpes más fuertes, y la suma pasaba de 0 dBFS (§5). Se dejó un
   `truepeak` con el techo en −2,5 dBTP en `data-fx-chain` de `#root`.
5. **El toque de Membresía a 1,0** (su clip lo tenía a 1,4): el encargo pide toques a 1,0, y ese pico era el más alto de la mezcla.

## 5. La música, las costuras y la mezcla

- **La edición** (SPEC §0.1): pista 14,05–30,05 + 34,05–72,05 + 82,05–fin, cruces de 30 ms que terminan 10 ms antes del compás. Costuras
  medidas: correlación 0,9991 y 0,9993 con la pista en el 16,0 y el 54,0, desfase 0 ms; la similitud de compases que eligió cada salto está en
  el SPEC (croma 0,82 / espectro 0,97 en el 16,0, en el respiro; 0,97 / 0,98 en el 54,0, al acorde final). La primera cae dentro del iris a
  Academia, con su `desliz`; la segunda en el corte al cierre, debajo de la subida.
- **Niveles:** música 0,75 en el carril de volumen; toques 1,0; confirmaciones clave 1,4 (las intermedias 1,0, como en sus clips); `desliz`
  1,4 en los cuatro cambios grandes y 1,0 en los demás; la subida y las campanas a 1,0.
- **Antes de renderizar** (`python _gen/mezcla.py`, las mismas fuentes, tiempos y niveles, sin el limitador): −16,7 LUFS, pico real
  +0,3 dBTP con el toque de Membresía a 1,4; con él a 1,0, −16,7 LUFS y −1,1 dBTP. Los picos estaban en los toques que caen en golpes: 180,
  780, 1020 y 1260.
- **El render:** **−16,7 LUFS integrados, pico real −2,1 dBTP, LRA 2,9 LU** (ffmpeg `ebur128=peak=true`), sin recortes: el
  «en torno a −17» del encargo con el pico por debajo de −1 dBTP; no se normalizó. La música del render contra la pista editada: correlación
  1,000 y 0 ms de desfase en el 1,5 · 15,2 · 16,3 · 31,0 · 47,0. `hyperframes audio` encuentra los toques en 6,03 · 12,03 · 12,53 · 13,03 ·
  14,03 · 26,03 · 28,03 · 30,03 · 34,03 · 36,03 · 42,03: cada uno un cuadro después de su imagen (181, 361, 376, 391, 421, 781, 841, 901, 1021,
  1081, 1261).

## 6. Lo que se revisó

- `npx hyperframes@0.8.221 check --json`: **0 errores**; 1 aviso (`composition_file_too_large`, el `index.html` generado: 674 líneas con
  los seis mundos; se deja así, como los recorridos, porque lo arma `gen.py` y no se edita a mano) y ninguna nota de layout, contraste,
  craft ni audio.
- `snapshot --review`: las hojas de cada escena, las costuras y las de 360 px de ancho; todas las frases se leen en el celular. Y tiras
  propias de ±0,2 s en cada cambio de mundo (−6, −3, 0, +3 y +8 cuadros): la subida, los dos látigos horizontales, el iris, el látigo
  vertical, el empuje y el morph se ven con la app ya puesta en la ventana que entra, sin cuadros en blanco, y con el texto fuera antes del
  movimiento.
- **El render:** `ffprobe`: H.264 1920×1080, 30 fps, 1770 cuadros, 59,000 s; AAC 48 kHz estéreo, 59,000 s; 13,5 MB
  (1,83 Mb/s). Cuadros sacados del MP4 en 2,0 · 6,1 · 8,0 · 14,1 · 18,0 · 21,8 · 26,1 · 30,1 · 36,5 · 44,5 · 52,0 · 55,5: coinciden con la
  vista previa (la apertura, cada momento con su ceja y su frase, la síntesis sobre el tablero y el cierre). El render pasó por el modo de
  captura por pantallazos (el desenfoque de movimiento lo pide) y avisó de GOP largos en dos grabaciones (solo afecta la búsqueda en la vista
  previa, no el render).
- **No se oyó:** las costuras y la mezcla se midieron, no se escucharon.

## 7. El plano más débil y qué cambiaría con más tiempo

- **P3 Eventos** es el momento más cargado de toques (cuatro en 60 cuadros) y su texto de app es el más pequeño (la cámara a ×1,0 del clip,
  26 px el texto de 14 px): se lee, pero es el que menos respira. Con más tiempo le daría el compás 10–12 al «¡Listo!» quieto con un punch.
- **P1** es texto solo durante 4 s (la entrada sin bajo). Funciona como portada en el sitio, pero un primer cuadro con la app también
  serviría de miniatura; se dejó así para que el video empiece donde termina el hero.
- **El 9:16** de la misma historia queda para después (los momentos y la música sirven igual; cambian las ventanas y los textos).
