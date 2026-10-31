# SPEC · «Kingdom en un minuto» — «Del que llega al que sirve» (16:9)

2026-10-31 · Contrato de construcción de la historia de [STORY.md](STORY.md). Cada momento de módulo es el clip publicado de ese módulo
(`../clip-sitio-<modulo>/`), llevado a 16:9 tal como lo llevó su recorrido (`../recorrido-<modulo>/_gen/`: mismos tramos, mismos encuadres,
mismas marcas, mismos sonidos), recortado a una ventana y corrido un número entero de compases. Cada adjetivo es un número, los valores por
defecto están prohibidos con nombre y los planos van cuadro por cuadro. Se construye desde aquí (`_gen/`), se revisa contra esto
([REVIEW.md](REVIEW.md)) y se cambia aquí cuando la vista previa cambie la película.

```text
GOAL:    Un pastor que llega al sitio termina pensando «Kingdom acompaña a cada persona, reporta cada reunión, toma la asistencia de cada
         clase, le da a cada miembro su boleta, sabe quién respondió cada aviso y cubre cada puesto, y yo lo veo todo en un tablero», y toca
         «Prueba gratis 30 días».
OUTPUT:  HyperFrames 0.8.221 · una composición 1920×1080 (16:9) · 30 fps. (La 9:16 queda para después; no se especifica aquí.)
TIME:    59,0 s = 1770 cuadros: cuerpo 0–54,0 (cuadros 0–1619) + cierre del Comercial 54,0–59,0 (1620–1769). 120 BPM = 15 cuadros por pulso
         en todo el video (las dos costuras de la música conservan la grilla, §0).
LOOK:    la noche del sitio (#060D1F) con el halo y la retícula de puntos del kit; tinta #EAF0FF; un solo acento, el dorado #E8B95A: las seis
         cejas, «una persona.» de la apertura, «una sola app» de la síntesis y el botón del cierre. Fraunces 560 / −0,02 em para las frases
         (132 px la apertura, 84 px las demás); Inter 700 28 px para las cejas; Inter para «Datos de ejemplo». El medio: la app REAL de
         Kingdom Demo en las ventanas del kit sobre la noche: el celular (`.k-ventana-16x9`, 720×900 en 1104·90) y, una vez, el escritorio
         (`.k-ventana-escritorio`, 1440×760 en 240·260); nunca un aparato dibujado.
OBJECTS: seis ventanas de celular (una por módulo) y la ventana del escritorio en que se transforma la última; el punto de toque de cada
         grabación; la apertura, seis cejas con su frase y la síntesis; la píldora «Datos de ejemplo» en cada ventana; el cierre del
         Comercial. Nada más existe en el cuadro.
MOTION:  curvas por papel (§1.5); dentro de cada módulo, las cámaras de su clip (un movimiento por compás, quietas mientras la app cambia);
         entre módulos, un cambio de mundo en cada golpe medido (120 · 300 · 480 · 720 · 960 · 1200 · 1440 · 1620), de cinco clases:
         subida, látigo horizontal (dos, en sentidos opuestos), iris, látigo vertical, empuje y morph.
SHOTS:   nueve planos (§2).
BANNED:  §3.
QA:      §4.
```

---

## 0. La música: la edición y el reloj

### 0.1 La edición (dos costuras, medidas)

«Product Launch» (The_Mountain, `assets/musica/product-launch-the-mountain.mp3`, 86,05 s, 120 BPM, compases de 2 s desde el 2,05) se arma
en `assets/musica/product-launch-minuto.wav` (`_gen/musica.sh`, 57,997 s) con tres tramos y dos cruces triangulares de 30 ms que terminan
10 ms antes de la cabeza de compás (el ataque entra entero, como en `recorrido-academia`):

| Video | Pista | Qué es |
|---|---|---|
| 0–16 | 14,05–30,05 | La entrada (2 compases), la primera subida (4) y **la mitad del respiro** (2): el respiro corto del encargo |
| 16–54 | 34,05–72,05 | La segunda subida (8 compases), el clímax (8) y los tres primeros compases de la salida |
| 54–58 | 82,05–86,05 | El último acorde, que se apaga solo debajo del cierre |

- **Por qué esos saltos** (similitud por compás medida con un croma de 12 clases y un espectro de 24 bandas, `ana.py` de la revisión):
  - **30,05 → 34,05:** el compás que suena antes del salto (28,05–30,05) y el que sonaba antes del 34,05 en la pista (32,05–34,05) dan
    croma 0,82 y espectro 0,97, con la misma sonoridad (−17,3 / −17,1 dB RMS); el compás que se pierde y el que entra, 0,92 / 0,96. Saltar
    desde el 28,05 daba 0,87 pero dejaba el respiro en un solo compás.
  - **72,05 → 82,05:** croma 0,97 y espectro 0,98 (−17,9 / −18,4 dB): la salida se repite y el acorde final llega igual que en la pista.
    Mejor que el 66,05 → 82,05 del recorrido de Membresía (0,95 / 0,92, con un salto de 4 dB) y que 70,05 (0,87).
- **Comprobación:** `ffprobe` 57,997 s. Correlación del archivo editado contra la pista en ventanas de 0,5 s: 0,9991 en el 16,0 (pista
  34,05) y 0,9993 en el 54,0 (pista 82,05), **0 ms de desfase**. Mapa exacto: **video = pista − 14,05** hasta el 16; **video = pista −
  18,05** del 16 al 54; **video = pista − 28,05** desde el 54.
- **Licencia:** la de Pixabay permite modificar la pista (`../_identidad/licencias.md`); la pista editada no se redistribuye sola.

### 0.2 El reloj del video

| Video | Pista (tramo de `kit.json` → `mapa`) | Le toca |
|---|---|---|
| 0–4 | 14,05–18,05 · entrada sin bajo | P1 · la frase del sitio («Cada punto es una persona.») |
| **4**–10 | 18,05–24,05 · el bajo entra en el 4,0; pico en el 6,0 | P2 · Membresía |
| 10–16 | 24,05–30,05 · final de la subida y medio respiro | P3 · Eventos |
| **16**–24 | 34,05–42,05 · segunda subida (golpes 18,0 y 20,0) | P4 · Academia |
| **24**–32 | 42,05–50,05 · **el golpe más fuerte** (24,0) y su frase | P5 · Mi iglesia |
| **32**–40 | 50,05–58,05 · clímax | P6 · Comunicaciones |
| **40**–48 | 58,05–66,05 · clímax | P7 · Equipos |
| **48**–54 | 66,05–72,05 · la salida | P8 · la síntesis |
| **54**–59 | 82,05–86,05 · el último acorde | P9 · el cierre del Comercial |

### 0.3 La grilla, pulso por pulso

Los pulsos de `product-launch-the-mountain.pulsos.json` llevados al video con el mapa de §0.1 caen todos en múltiplos de 15 hasta el 1034
(salvo 226, 284, 374 y 734, a un cuadro, donde no pasa nada). **Desde el 1048 la detección se va a los contratiempos** (1048, 1061, 1074…
= pista 53,0, 53,4…, medio pulso corrido), como en los recorridos: en el clímax y la salida las negras siguen en la grilla de 2,05 + 0,5·n
de la pista (múltiplos de 15 en el video) y la fuerza es el flujo espectral medido en ese instante (1,00 = el 99,5 % más fuerte del archivo
editado). **Nada del video cae en un contratiempo.** Golpes (fuerza ≥ 0,85):

| Cuadro | Fuerza | Qué cae ahí |
|---|---|---|
| 120 | 0,93 (el bajo) | la primera ventana asienta |
| 180 | 0,87 (pico) | el toque «Marcar cumplido» de Membresía |
| 240 | 0,92 | el punch a «Ahora va en: Mensaje de bienvenida» |
| 480 | 0,93 (costura) | el iris a Academia |
| 540 · 555 | 0,90 · 0,89 | la cámara del profesor baja al contador |
| 600 | 0,96 | el látigo a la alumna y el «3» |
| 660 | 0,88 | «¡Listo! Quedó tu asistencia» |
| **720** | **1,00** | el látigo vertical a Mi iglesia |
| 840 | 0,98 | «Ver boleta» |
| 960 | 1,00 (*flujo*) | el empuje a Comunicaciones (arranca el clímax) |
| 1080 | 1,09 (*flujo*) | «respondieron» |
| 1200 | 1,05 (*flujo*) | el látigo a Equipos |
| 1320 | 1,06 (*flujo*) | el látigo vertical al líder: «Confirmado» |
| 1440 | 0,58 (*flujo*, la salida) | el morph al escritorio (la música se calma: el tablero se lee) |
| 1620 | el último acorde | el cierre, con la subida y las campanas |

Los otros toques de cada clip siguen en sus pulsos (múltiplos de 15) porque cada ventana se corre un número entero de compases (§2).

### 0.4 Nivel de la música

`<audio id="musica" src="assets/musica/product-launch-minuto.wav" data-start="0" data-duration="57.99">` con **0,75** en el carril de
volumen de principio a fin (el de los recorridos), **sin fundido**: el último acorde se apaga solo debajo del cierre.

---

## 1. Los números del estilo

### 1.1 Paleta

La de los clips: fondo `#060D1F` con el halo (`.k-halo`) y los puntos (`.k-puntos`) del kit; los puntos nunca se mueven; el halo se asienta
1,08 → 1,00 (`sine.out`, 90 cuadros) en 0 · 120 · 300 · 480 · 720 · 960 · 1200 · 1440. Tinta `#EAF0FF`. Dorado `#E8B95A` solo en las cejas,
en las itálicas de la apertura y de la síntesis y en el botón del cierre. Anillo y sombra de `.k-ventana` del kit. Placa de «Datos de
ejemplo» `rgba(6,13,31,.72)`. El **dip** (`#060D1F` al 40 %) en 1617–1619 sobre las ventanas. Los colores de la app (el azul del tema, los
estados) viven solo dentro de las grabaciones.

### 1.2 Letras

| Pieza | Letra | Lugar |
|---|---|---|
| La apertura | Fraunces 560, **132 px**, interlínea 1,04, −0,02 em, centrada; «una persona.» en itálica dorada | y 372 (dos líneas: 372–647) |
| Las cejas | Inter 700, 28 px, mayúsculas, dorada (`.k-feed-ceja` a 28 px) | x 120 · y 412 (celular) / x 240 · y 92 (escritorio) |
| Las frases | Fraunces 560, 84 px, interlínea 1,04, −0,02 em (`.k-feed-frase` a 84 px), dos líneas de ≤ 14 caracteres | x 120 · y 460, 936 de ancho |
| La síntesis | la misma frase, una línea; «una sola app.» en itálica dorada | x 240 · y 132, 1440 de ancho |
| «Datos de ejemplo» | `.k-datos-ejemplo`, 31 px, 56 de alto | en cada ventana, abajo a la izquierda, a 24 px |

### 1.3 Las ventanas

- **Celular** (P2–P7): `.k-ventana-16x9` (720×900, radio 28) en 1104·90. La grabación (1170×2532) ajustada al ancho: 0,615385 px por px
  del video, 1,846 px de la ventana por px CSS de la app; 1558,15 de alto. Cada módulo tiene su ventana (`#w1`…`#w6`); las de Academia y
  Equipos llevan dentro la **tira vertical** de su clip: dos ranuras a 1000 px.
- **Escritorio** (P8): `.k-ventana-escritorio` (1440×760, radio 20) en 240·260, a la que llega la caja de `#w6` por el morph. La grabación
  `tableros.mp4` (1920×1080, la página de 1280×720 a 1,5×) a 2560×1440: 2 px por px CSS (nivel D, el del recorrido de Membresía).
- **Encuadres:** `enc(s, cx, cy)` pone la caja de centro (cx, cy) en px CSS en el centro de la ventana con la escala s sobre el plano, sin
  salirse de la grabación (`comp()` deshace en el mismo cuadro los saltos de la app). Los números son los de cada recorrido (§2), que ya
  pasaron su revisión: s ≥ 1,0 (Eventos) o 1,085 (los demás) en el plano; acercamientos de 1,3 a 1,5.

### 1.4 Los cambios de mundo (cinco clases, todas en un golpe)

| Cuadros | Clase | Números |
|---|---|---|
| 110–120 | **Subida** | `#w1` y: 1080 → 0, 10 cuadros, `power3.out` (asienta en el bajo) |
| 290–300 | **Látigo horizontal** ← | `#w1` x 0 → −1920 y `#w2` x 1920 → 0 a la vez (una tira), 10 cuadros, `power3.inOut`; `#w2in` aterriza 1,04 → 1 (10, `power3.out`) |
| 479–485 | **Iris** | `#w3` clip-path círculo con centro en el centro de la ventana (360·450), radio 0 → 600 en 6 cuadros, `power2.out`; `none` en el 486 |
| 710–720 | **Látigo vertical** ↑ | `#w3` y 0 → −1080 y `#w4` y 1080 → 0, 10 cuadros, `power3.inOut`; `#w4in` aterriza 1,04 → 1 |
| 950–970 | **Empuje** | `#w4` escala 1 → 1,22 (10, `power2.in`) y se va en el 960; `#w5` está en el 960 y asienta 1,08 → 1 (10, `power3.out`) |
| 1190–1200 | **Látigo horizontal** → | el de 290 en el otro sentido: `#w5` x 0 → 1920, `#w6` x −1920 → 0; `#w6cel` aterriza 1,04 → 1 |
| 1434–1446 | **Morph** | la caja de `#w6` va de la del celular a la del escritorio (left/top/ancho/alto/radio, `power3.inOut`, 12 cuadros calculados uno a uno); el celular sale con −160 px (`power3.in`), el tablero entra con +160 px y 1,04 → 1 (`power3.out`, 10); el contenido cambia en el 1440 (el morph de `recorrido-membresia`) |
| 1617–1620 | **Dip y corte** | el dip al 40 % en 1617–1619; en el 1620 la escena se apaga y entra el cierre |

Y dentro de dos módulos, los látigos verticales de sus clips: Academia 590–600 (del profesor a la alumna) y Equipos 1316–1326 (de
Gabriela al líder), con la ranura que llega aterrizando 1,04 → 1.

### 1.5 Curvas por papel

| Papel | Curva | Duración |
|---|---|---|
| Entrada de palabra | blur 6 → 0 + opacidad, `power4.out`, sin desplazarse | 4 cuadros, una palabra cada 2 |
| Entrada de ceja | blur 8 → 0 + opacidad, `power4.out` | 6 cuadros |
| Salida de texto | blur 0 → 8 + opacidad, `power3.in` | 4 cuadros, 12 antes del cambio de mundo (antes de que arranque el látigo) |
| Cámara | `power2.inOut` | 14 cuadros (9 en los punches, 13 en los que lo pidió el clip) |
| Látigo | `power3.inOut` | 10 cuadros |
| Aterrizaje | `power3.out` | 10 cuadros |
| Marca de toque | aparece 4 cuadros antes (0,6 → 1), se hunde a 0,86 en el cuadro y se va en 6; la onda 1 → 1,62 en 0,45 s; si la pantalla cambia antes, se va con el corte | — |

### 1.6 Sonido

- **Música:** §0.4.
- **Sonidos de acción del kit** (`identidad/audio/`, y las tomas b = +3 % y c = −3 % de tono en `assets/audio/`): `data-start = cuadro del
  sonido / 30 − acento`; el sonido cae un cuadro después de su imagen. `toque`, `aparicion` y `desliz` rotan sus tres tomas en orden de
  tiempo, nunca la misma dos veces seguidas.
  - **Toques a 1,0**, en cada toque real de cada clip (los suyos, en sus cuadros).
  - **Confirmaciones a 1,4** donde algo queda hecho y es la prueba del módulo («cumplido», «¡Listo!», «¡Quedaste inscrito!», los nombres
    que respondieron, «¡Gracias por servir!»); a 1,0 las intermedias (como en cada clip).
  - **`desliz`** en los siete cambios de mundo y en los dos látigos internos (1,4 en la subida del 120, el látigo del 720, el del 1320 y el
    morph del 1440; 1,0 en los demás).
  - **`subida`** una sola vez: 1576–1633, con su golpe en el 1621 (un cuadro después del corte al cierre).
  - **El sonido de marca** en 54,38 (inicio del cierre + 0,38, `kit.json` → `piezas.cierre-comercial.sonido`).
- **Mezcla:** en torno a **−17 LUFS integrados**, pico real **≤ −1 dBTP**. Los toques clave caen a propósito en los golpes más fuertes de
  la pista y la suma pasa de 0 dBFS en cuatro instantes (180, 780, 1020, 1260); el bus maestro (`data-fx-chain` de `#root`) lleva un
  limitador de pico real (`truepeak`) con el techo en −2,5 dBTP, que solo actúa en esos transitorios. Se simula con `_gen/mezcla.py` y se
  mide el render con `ebur128=peak=true`.

---

## 2. Los planos

Cada módulo: **ventana del clip** (cuadros del clip) → cuadros del video, el corrimiento en compases y lo que se ve; la ceja y la frase
entran en el cuadro del cambio + 1 (una palabra cada 2 cuadros) y salen 12 cuadros antes del siguiente cambio. Las ventanas que entran con
movimiento (P2, P3, P5 y P7) traen 12 cuadros de su clip antes del momento, para que el látigo no muestre una ventana vacía.

### P1 · «Cada punto es una persona.» — 0–119

La noche con el halo y la retícula de puntos del kit. Centrada, en dos líneas a 132 px: «Cada punto / es *una persona.*», la frase que el
hero del sitio revela al bajar (el video va justo debajo). «Cada» ya está en el cuadro 0 (la miniatura); «punto» en el 15, «es una» en el 30,
«persona.» en el 45 (un grupo por pulso). Quieta 49–104 (1,9 s para 5 palabras); sale 105–109, antes de que suba la ventana. Sin sonido de
acción: la entrada de la pista sola. **«Kingdom es para toda la iglesia», la frase del título del hero, no va aquí:** es la que dice el
cierre del Comercial, y con la síntesis habría sonado tres veces. Así abre la anáfora de los módulos («Cada persona…», «Cada reunión…»).

### P2 · MEMBRESÍA — «Cada persona, / acompañada.» — 120–299

Clip 540–720 → 120–300 (−7 compases). La ventana sube y asienta en el 120 (el bajo; `desliz` 1,4). Valeria Cardona Ríos: el reporte de la
llamada de bienvenida con «Muy contenta, viene el domingo» ya escrito (cámara en `observaciones`, ×1,4); 150 la cámara a los botones;
**180 toque «Marcar cumplido» en el pico**, 183 «Llamada de bienvenida cumplido · Ahora va en: Mensaje de bienvenida» (confirmación 1,4);
180 la cámara al resultado; **240 el punch a «Ahora va en»** (×1,5, 9 cuadros) en el golpe. Tramos m21–m25 (`membresia.mp4`, la
grabación pegada abajo: `off = 900 − 1558,15`). Marca en 180 (808·2088 del video), se va con el corte del 183.

### P3 · EVENTOS — «Cada reunión, / reportada.» — 300–479

Clip 540–720 → 300–480 (−4 compases). Látigo horizontal 290–300. La Casa de Paz Laureles 1: «Visitantes 2 · Total: 10 personas» y
«Guardar asistencia» (cámara `botones`, ×1,3); **360 toque «Guardar asistencia»**, 362 el paso ② (still de la grab. 1027 en 362–369; la
barra crece 369–375), 375 «Muy bien», 390 «Tema de la palabra», «El perdón» a 1,5× (392–405), **420 «Enviar reporte»**, 422 «¡Listo!» con
«10 personas.» y «Reportada» (confirmación 1,4); 450 la cámara a la tarjeta (9 cuadros).

### P4 · ACADEMIA — «Cada clase, / sin papel.» — 480–719

Clip 0–240 → 480–720 (+8 compases). Iris 479–485 sobre la costura de la música. El celular del profesor: «Marquen su asistencia con este
código · 3 5 9 8» con su barra y el QR (cámara `codigo`); **540 la cámara baja al contador** («13 de 18 marcaron», en el golpe 0,90);
**590–600 látigo vertical** a la alumna (la tira del clip); 600 el «3», 615 el «5», 630 el «9», 645 el «8» (una `aparicion` por número);
**660 «¡Listo! Quedó tu asistencia»** (confirmación 1,4; la cámara a `listo`, ×1,2), quieta hasta el 709.

### P5 · MI IGLESIA — «Cada miembro, / con su boleta.» — 720–959

Clip 540–780 → 720–960 (+3 compases). Látigo vertical 710–720 en **el golpe más fuerte** (`desliz` 1,4). Gabriela inscribe a Simón: 735
«No»; 750 la cámara a los botones; **780 «Inscribir»**, 782 el sello, el confeti y «¡Quedaste inscrito!» con las dos filas «Inscrito»
(confirmación 1,4); 825 still de la grab. 1258 (el salto de la app compensado); **840 «Ver boleta»** (0,98), 842 «Mis boletas» con el QR,
entra 1,03 → 1,00; 870 el punch al QR (×1,3); **900 toque en el QR**, 902 la boleta a pantalla completa con «Código FM75UZ»; 900 la cámara
abre (`grande`).

### P6 · COMUNICACIONES — «Cada aviso, / con su respuesta.» — 960–1199

Clip 540–780 → 960–1200 (+7 compases). Empuje 950–970 en el arranque del clímax. La tarjeta «Invitación: culto de jóvenes del domingo»
(cámara `tarjeta`); **1020 toque en la invitación**, 1022 el reporte: 139 total, 137 entregados, 115 leídos, 23 respondieron, 39 clics
(cámara `kpis`); **1080 toque «respondieron»** en el golpe 1,09; 1095 «Destinatarios (23)» con cada nombre, «Leído» y «Allí estaré»
(confirmación 1,4); 1110 la cámara a los nombres, 1140 a `cierre`.

### P7 · EQUIPOS — «Cada puesto, / cubierto.» — 1200–1439

Clip 540–780 → 1200–1440 (+11 compases). Látigo horizontal → 1190–1200. El celular de Gabriela: su servicio en Parqueadero con «Aceptar ·
No puedo» (cámara `botones`); **1260 toque «Aceptar»**, 1262 «¡Gracias por servir! Tu líder ya lo sabe.» y «Confirmado» (confirmación
1,4); **1316–1326 látigo vertical** al celular del líder Jorge (golpe 1,06 en el 1320): el turno con Gabriela «Confirmado» (confirmación
1,0 en el 1322); 1350 el retroceso a `cierre` (×1,2, 9 cuadros): «5 de 5».

### P8 · La síntesis — «Toda tu iglesia, en *una sola app.*» — 1440–1619

El morph 1434–1446 (`desliz` 1,4): la caja del celular se vuelve la del escritorio y dentro aparece el tablero del pastor (Tableros ›
Resumen, «Toda la iglesia»: Membresía 1.324, +49,8 %, 448 nuevas, 145 en ruta, 16 conectadas, 12 en rojo, 32 acompañadas, 522 pasos
cumplidos), cámara `cifras` (D). La ceja «DEL PASTOR AL MIEMBRO MÁS NUEVO» (la bajada del hero) entra en el 1446 y la frase, palabra a
palabra, desde el 1447; **1530 la cámara baja al semáforo de actividad** (la barra verde, amarilla, roja y gris con 954 · 165 · 62 · 143).
Quieta hasta el corte. Dip 1617–1619.

### P9 · El cierre del Comercial — 1620–1769

`identidad/cierre-comercial.html` (público iglesia, llamado «prueba», contacto el sitio, fondo noche): la corona, «Kingdom» y «Prueba gratis
30 días». La subida acaba en el 1621; las campanas en 54,38; el último acorde se apaga debajo.

---

## 3. BANNED

Lo de `references/spec.md` («BANNED by default») y, con nombre, para esta pieza:

1. Un teléfono, una laptop o cualquier aparato dibujado; la app redibujada o una pantalla inventada.
2. Datos reales; una cifra sin «Datos de ejemplo» a la vista.
3. Un corte, una entrada o un toque fuera de un pulso; un cambio de mundo fuera de un golpe; cualquier cosa en un contratiempo.
4. Dos cambios de mundo seguidos de la misma clase en el mismo sentido; un `desliz` igual dos veces seguidas.
5. Texto que se mueve mientras se lee; frases de más de 5 palabras en los módulos; cejas que no sean el nombre del módulo.
6. El dorado fuera de las cejas, las itálicas de la apertura y la síntesis, y el botón del cierre.
7. Tarjetas de función, íconos de módulo, listas de características: cada módulo se muestra haciendo algo.
8. Fundidos lentos entre módulos (todo cambio de mundo dura 10 cuadros o menos, salvo el empuje y el morph, de 12 a 20).
9. La cámara moviéndose mientras la app escribe, se desplaza o carga.
10. La espera de la app (cargadores, esqueletos, la K) a la vista: los tramos de cada clip ya la recortan.

## 4. QA

- `npx hyperframes check --json`: **0 errores**.
- `snapshot --review` y hojas propias en: 2,0 (la apertura entera) · 6,1 (el toque de Membresía) · 8,0 (el punch) · 12,8 · 14,1 («¡Listo!»
  de Eventos) · 18,0 (el código) · 21,8 («¡Listo!» de Academia) · 26,1 · 28,1 · 30,1 (la boleta) · 34,1 · 36,5 (los nombres) · 42,1 ·
  44,5 (el líder) · 48,5 · 52,0 (la síntesis) · 55,5 (el cierre); y una tira de ±0,2 s en cada cambio de mundo.
- Sincronía: cada toque dibujado en el cuadro de su sonido −1; cada sonido a menos de 1 cuadro de su imagen; cada cambio de mundo en su golpe.
- Las costuras de la música medidas (§0.1) y escuchadas en el render como tales (no se pueden oír aquí: se miden).
- El render: `ffprobe` (1920×1080, 30 fps, 59,0 s, AAC), −17 LUFS ± 1 y pico real ≤ −1 dBTP con `ebur128=peak=true`.
