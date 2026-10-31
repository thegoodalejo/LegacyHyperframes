# SPEC · Recorrido de Comunicaciones — «Alguien nuevo escribe… y nadie se queda sin respuesta» (16:9)

2026-10-30 · Contrato de construcción de la historia de [STORY.md](STORY.md). La parte 1 es el clip publicado
([clip-sitio-comunicaciones](../clip-sitio-comunicaciones/): su [SPEC](../clip-sitio-comunicaciones/SPEC.md), su
[REVIEW](../clip-sitio-comunicaciones/REVIEW.md), su `index.html` y su `_gen/`), llevado a 16:9 sin reabrirlo; la parte 2 es nueva. El
sistema es el de [Academia](../recorrido-academia/SPEC.md) (el modelo: misma música, mismas ventanas, mismas curvas, mismos niveles de
lectura). Cada adjetivo es un número, los valores por defecto están prohibidos con nombre y los planos van cuadro por cuadro. Se construye
desde aquí, se revisa contra esto y se cambia aquí cuando la vista previa cambie la película. «Igual que el clip» quiere decir: copiado de
`clip-sitio-comunicaciones/index.html` (o de su `_gen/`) con los cambios de §2.1; «igual que Academia», copiado de lo que especifica
`recorrido-academia/SPEC.md` en la misma sección.

```text
GOAL:    Un pastor que no conoce Kingdom termina pensando «el chatbot contesta a cualquier hora, quien escribe queda en Membresía, la
         bienvenida sale sola y le hablo a cada red sin perder a nadie» y toca «Prueba gratis 30 días».
OUTPUT:  HyperFrames 0.8.221 · una composición 1920×1080 (16:9) · 30 fps. (La 9:16 queda para después; no se especifica aquí.)
TIME:    97,0 s = 2910 cuadros: cuerpo 0–92,0 (cuadros 0–2759) + cierre del Comercial 92,0–97,0 (2760–2909). 120 BPM = 15 cuadros
         por pulso en todo el video (la costura de la música conserva la grilla, §0).
LOOK:    la noche del sitio (#060D1F) con el halo y la retícula de puntos del kit; tinta #EAF0FF; un solo acento, el dorado #E8B95A, en
         tres lugares (la ceja «COMUNICACIONES», la palabra «nadie» y el botón del cierre). Fraunces 560 84 px / −0,02 em para las
         frases; Inter para la ceja y «Datos de ejemplo». El medio: la app REAL de Kingdom Demo en dos ventanas del kit sobre la noche:
         el celular (`.k-ventana-16x9`, 720×900) y el escritorio (`.k-ventana-escritorio`, 1440×760); nunca un aparato dibujado, nunca
         la marca ni el verde de WhatsApp fuera de la grabación.
OBJECTS: las dos ventanas; tres mundos de celular (el clip; la conversación de Mariana; la campaña nueva) y dos de escritorio (el
         chatbot con «Probar»; la automatización de bienvenida); el punto de toque; las ocho frases; la ceja; la píldora «Datos de
         ejemplo»; el cierre del Comercial. Nada más existe en el cuadro.
MOTION:  curvas por papel (§1.6); un movimiento de cámara por compás (14 cuadros, power2.inOut), quieto después; cada corte y cada
         entrada en un pulso; cada cambio de mundo en un golpe (120 · 180 · 600 · 660 · 840 · 1320 · 1680 · 2040 · 2760).
SHOTS:   doce planos: P1–P6, los del clip (§2.1; su P7, la firma, no va), y P8–P13, los nuevos (§2.3).
BANNED:  §1.8.
QA:      §4.
```

---

## 0. La música: la edición y el reloj

### 0.1 La edición (una sola costura, medida): la de Academia, al cuadro

Los dos recorridos parten de un clip de 28 s que usa la pista del 14,05 al 42,05, así que la edición de
[Academia §0.1](../recorrido-academia/SPEC.md#01-la-edición-una-sola-costura-medida) sirve **tal cual**: «Product Launch» (The_Mountain,
`_identidad/musica/product-launch-the-mountain.mp3`, 86,05 s, 120 BPM, compases de 2 s desde el 2,05) se alarga **repitiendo 24 s (12
compases): del 22,05 al 46,05 de la pista**. Se toca del 14,05 al 46,05, se salta al 22,05 y se sigue hasta el final natural de la pista.
Los porqués (similitud de los compases a los dos lados del salto, ataques de 0,98 y 0,92, cruce de 30 ms que termina 5 ms antes del golpe,
envolvente a ±0,4 dB, correlación 0,998 después de la costura) y lo descartado están medidos allí; no se repiten aquí.

```bash
# en recorrido-comunicaciones/ (script "musica" del package.json): 31,99 s + 64,037 s − 0,03 s de cruce = 95,997 s
# Si recorrido-academia/assets/musica/product-launch-recorrido.wav ya existe, se COPIA (es el mismo archivo, byte a byte) en vez de rehacerlo.
ffmpeg -hide_banner -y -i ../_identidad/musica/product-launch-the-mountain.mp3 -filter_complex \
  "[0:a]atrim=start=14.05:end=46.04,asetpts=PTS-STARTPTS[a];[0:a]atrim=start=22.01,asetpts=PTS-STARTPTS[b];[a][b]acrossfade=d=0.03:c1=tri:c2=tri[m]" \
  -map "[m]" -ar 44100 -c:a pcm_s16le assets/musica/product-launch-recorrido.wav
```

- **Comprobación al armarla:** `ffprobe` da **95,997 s** (±5 ms). Mapa exacto: **video = pista − 14,05** hasta el 31,99 y **video = pista +
  9,95** desde el 31,99. El cruce ocupa 31,960–31,990 del video.
- **Licencia:** la de Pixabay permite modificar la pista (`_identidad/licencias.md`); la pista editada no se redistribuye sola. Con Content
  ID, en YouTube puede llegar un reclamo de monetización, que se disputa con la licencia.

### 0.2 El reloj del video

| Video | Pista | Tramo de la pista (`kit.json` → `mapa`) | Lo que le toca al video |
|---|---|---|---|
| 0–4 | 14,05–18,05 | entrada sin bajo | El gancho del clip: la cola |
| 4–12 | 18,05–26,05 | primera subida (bajo en 18,05, pico en 20) | «Tomar», «/horarios», enviar |
| 12–20 | 26,05–34,05 | respiro | Volver, «Campañas», la invitación |
| 20–28 | 34,05–42,05 | segunda subida (golpes 36 · 38 · 42,05) | El reporte, «respondieron», los nombres |
| **28**–32 | 42,05–46,05 | el golpe más fuerte y su compás | Látigo al escritorio: el chatbot, «Probar» |
| **32**–36 | 22,05–26,05 (repetido) | final de la primera subida | «hola» y la respuesta del chatbot |
| 36–44 | 26,05–34,05 (repetido) | respiro | «Horarios» y el horario, que se lee |
| **44**–60 | 34,05–50,05 (repetido hasta 46,05) | segunda subida otra vez (golpe más fuerte en el **52,0**) | Mariana: de su chat a su ficha; la llegada a Automatizaciones |
| **60**–76 | 50,05–66,05 | clímax brillante (dos frases de 8 s) | La bienvenida que sale sola; el público con la red Timoteo |
| **76**–92 | 66,05–82,05 | salida tranquila | La plantilla y su vista previa; la frase del sitio |
| **92**–96 | 82,05–86,05 | el último acorde, que se apaga solo | El cierre del Comercial |

### 0.3 La grilla, pulso por pulso

**Cuadros 0–839:** la tabla de `clip-sitio-comunicaciones/SPEC.md` §0, sin cambios (todos los pulsos en múltiplos de 15 salvo el 284,
donde no pasa nada).

**Cuadros 840–2760** (cuadro · fuerza): los mismos de [Academia §0.3](../recorrido-academia/SPEC.md#03-la-grilla-pulso-por-pulso), porque la
pista y la edición son las mismas. Se volvieron a medir aquí con `product-launch-the-mountain.pulsos.json` llevado al video (pista − 14,05
hasta el 46,04; pista + 9,95 desde el 22,0): todos los pulsos caen en múltiplos de 15 hasta el 1860 (salvo el 1004, la pista 23,505, donde
no pasa nada). **Desde el 1875 la detección se va a los contratiempos** (marca 1888, 1901, 1914, 1928, 1942… = pista 52,975, 53,415,
53,865, 54,305, 54,795…, medio pulso corrido): en el clímax y la salida las negras siguen en la grilla de 2,05 + 0,5·n y la fuerza que va en
*cursiva* es el flujo espectral medido en ese instante (la de Academia; 1,00 = el 99,5 % más fuerte de la pista). **Nada del video cae en
un contratiempo.**

| Compás | Cuadros | Pulsos (cuadro · fuerza) | Lo que le toca |
|---|---|---|---|
| 15 | 840–899 | **840 ·1,00** · 855 ·0,68 · 870 ·0,51 · 885 ·0,52 | **Látigo al escritorio**: el lienzo; 870 la cámara a «Probar» y las palabras |
| 16 | 900–959 | **900 ·0,84** · 915 ·0,82 · 930 ·0,75 · 945 ·0,66 | **900 toque «Probar»**; 905 el simulador (corte) y la cámara a él |
| 17 | 960–1019 | **960 ·0,92** (costura) · 975 ·0,77 · 990 ·0,58 · 1005 ·0,52 | 960 toque en «Escribe como la persona…» y «hola»; 990 toque «Enviar» |
| 18 | 1020–1079 | 1020 ·0,77 · 1035 ·0,74 · 1050 ·0,60 · 1065 ·0,58 | **1020 el chatbot contesta** (el saludo y el menú) |
| 19 | 1080–1139 | 1080 ·0,76 · 1095 ·0,64 · 1110 ·0,50 · 1125 ·0,46 | 1080 la cámara al menú (respiro) |
| 20 | 1140–1199 | 1140 ·0,75 · 1155 ·0,61 · 1170 ·0,49 · 1185 ·0,49 | **1140 toque «Horarios»**; 1155 el horario |
| 21 | 1200–1259 | 1200 ·0,67 · 1215 ·0,67 · 1230 ·0,54 · 1245 ·0,50 | 1200 la cámara al horario |
| 22 | 1260–1319 | 1260 ·0,63 · 1275 ·0,56 · 1290 ·0,61 · 1305 ·0,68 | Quieto: se lee |
| 23 | 1320–1379 | **1320 ·0,93** · 1335 ·0,69 · 1350 ·0,52 · 1365 ·0,49 | **Látigo de vuelta: la conversación de Mariana** |
| 24 | 1380–1439 | **1380 ·0,90** · **1395 ·0,89** · 1410 ·0,76 · 1425 ·0,68 | 1380 toque en el ícono de la persona → el panel; 1395 la cámara al panel |
| 25 | 1440–1499 | **1440 ·0,96** · 1455 ·0,77 · 1470 ·0,59 · 1485 ·0,60 | **1440 toque «Crear ficha»**; 1455 el formulario |
| 26 | 1500–1559 | **1500 ·0,88** · 1515 ·0,74 · 1530 ·0,62 · 1545 ·0,60 | 1500 «¿Cómo llegó?»; 1515 las opciones; 1530 la forma; 1545 «Crear ficha» |
| 27 | 1560–1619 | **1560 ·1,00** · 1575 ·0,68 · 1590 ·0,51 · 1605 ·0,52 | **La ficha de Mariana Ospina** (punch) |
| 28 | 1620–1679 | 1620 ·0,84 · 1635 ·0,82 · 1650 ·0,75 · 1665 ·0,66 | 1620 la cámara al panel entero |
| 29 | 1680–1739 | **1680 ·0,98** · 1695 ·0,74 · 1710 ·0,60 · 1725 ·0,57 | **Látigo al escritorio: Automatizaciones** |
| 30 | 1740–1799 | 1740 ·0,79 · 1755 ·0,75 · 1770 ·0,69 · 1785 ·0,67 | 1740 la cámara a la tarjeta «Bienvenida a quien llega» |
| 31 | 1800–1859 | **1800 ·*1,00*** · 1815 ·*0,98* · 1830 ·*0,77* · 1845 ·*0,81* | **1800 toque en la tarjeta** (empieza el clímax); 1803 la vista previa del mensaje |
| 32 | 1860–1919 | 1860 ·*0,71* · 1875 ·*0,97* · 1890 ·*0,71* · 1905 ·*0,69* | Quieto: el mensaje se lee |
| 33 | 1920–1979 | **1920 ·*1,00*** · 1935 ·*0,92* · 1950 ·*0,67* · 1965 ·*0,76* | **1920 «Envíos»** (se oye); 1923 los nombres |
| 34 | 1980–2039 | 1980 ·*0,62* · 1995 ·*1,00* · 2010 ·*0,69* · 2025 ·*0,68* | 1980 la cámara a las filas |
| 35 | 2040–2099 | **2040 ·*1,00*** · 2055 ·*1,00* · 2070 ·*0,83* · 2085 ·*0,83* | **Látigo de vuelta: la campaña nueva, «A quién va»** |
| 36 | 2100–2159 | 2100 ·*0,71* · 2115 ·*0,87* · 2130 ·*0,73* · 2145 ·*0,71* | 2100 «Un público»; 2130 «Agregar filtro»; 2145 la lista |
| 37 | 2160–2219 | **2160 ·*1,00*** · **2175 ·*1,00*** · 2190 ·*0,58* · 2205 ·*0,68* | 2160 «Red»; 2175 las redes; 2190 «Red Timoteo» |
| 38 | 2220–2279 | 2220 ·*0,54* · **2235 ·*1,00*** · 2250 ·*0,68* · 2265 ·*1,00* | 2220 «Aplicar»; **2235 el chip y la cifra** |
| 39 | 2280–2339 | **2280 ·*0,77*** · 2295 ·*0,46* · 2310 ·*0,41* · 2325 ·*0,43* | 2280 la app sube al mensaje; 2310 «Plantilla aprobada»; 2325 la lista |
| 40 | 2340–2399 | 2340 ·*0,46* · 2355 ·*0,50* · 2370 ·*0,46* · 2385 ·*0,47* | **2340 «invitacion_culto»**: la vista previa se llena |
| 41 | 2400–2459 | **2400 ·*0,76*** · 2415 ·*0,51* · 2430 ·*0,44* · 2445 ·*0,40* | 2400 la app sube a la vista previa (si hace falta, §2.2) |
| 42 | 2460–2519 | 2460 ·*0,46* · 2475 ·*0,57* · 2490 ·*0,39* · 2505 ·*0,42* | 2460 la cámara a la burbuja |
| 43 | 2520–2579 | **2520 ·*0,80*** · 2535 ·*0,51* · 2550 ·*0,45* · 2565 ·*0,43* | **La frase del sitio**; la ventana a un lado |
| 44 | 2580–2639 | 2580 ·*0,94* · 2595 ·*0,47* · 2610 ·*0,38* · 2625 ·*0,45* | Quieto |
| 45 | 2640–2699 | 2640 ·*0,78* · 2655 ·*0,48* · 2670 ·*0,40* · 2685 ·*0,42* | Quieto |
| 46 | 2700–2759 | 2700 ·*0,34* · 2715 ·*0,67* · 2730 ·*0,41* · 2745 ·*0,98* | La subida (desde 2716); el dip 2757–2759 |
| — | **2760** | el último acorde (pista 82,05) | **El cierre del Comercial** |

### 0.4 Nivel de la música

`<audio id="musica" src="assets/musica/product-launch-recorrido.wav" data-start="0" data-duration="96">`, **sin `data-volume`**: **0,75** en
el carril de volumen de principio a fin (el nivel del clip de Comunicaciones, REVIEW del clip §5, para que la parte 1 suene igual). **Sin
fundido**: la pista termina sola debajo del cierre. Si en la vista previa las campanas del 92,38 quedan tapadas, el carril baja a 0,5 entre
92,0 y 92,3 (y se anota en el REVIEW); nada más se toca.

---

## 1. Los números del estilo

### 1.1 Paleta

La de `clip-sitio-comunicaciones/SPEC.md` §1.1, tal cual (fondo `#060D1F`, halo, puntos que nunca se mueven, tinta `#EAF0FF`, dorado
`#E8B95A` solo en la ceja, «nadie» y el botón del cierre; anillo `rgba(234,240,255,.12)`; placa de «Datos de ejemplo» `rgba(6,13,31,.72)`;
el azul de marca solo dentro del cierre). Cambia: el **dip** va en los cuadros **2757–2759** sobre las dos ventanas; el **halo** se asienta
1,08 → 1,00 (`sine.out`, 90 cuadros) en 0 · 180 · 840 · 1320 · 1680 · 2040 · 2520. Los colores de la app (el azul del tema, los estados
«Leído» y «Encendida», los chips) viven dentro de la grabación y no se tocan ni se repiten fuera.

### 1.2 Tipografía (16:9)

| Pieza | Clase del kit | Familia · peso | Tamaño | Reglas |
|---|---|---|---|---|
| Frase | `.k-titular` con `font-size: 84px` | Fraunces 560; `<em>` itálica 500 dorada | **84 px** · interlínea 1,04 (87,4 px) · −0,02 em | Máx. 2 líneas en el escenario del celular, **1 línea** en el del escritorio; saltos fijados a mano; izquierda; `text-wrap: balance` apagado; sin sombra |
| Ceja | `.k-ceja` | Inter 700, MAYÚSCULAS, +0,10 em | **28 px** | Una palabra: «COMUNICACIONES» |
| Datos de ejemplo | `.k-datos-ejemplo` (la de 16:9) | Inter 600 | **22 px**, píldora de 40 px | En cada ventana, abajo a la izquierda, a 24 px |
| Texto de la app | (grabación) | la de la app | ≥ **28 px** en todo encuadre de lectura | §1.5 |

Saltos fijados: «Alguien nuevo escribe. / ¿Quién contesta?» · «Todo tu equipo, / un solo número.» · «Y sabes quién / leyó el aviso» ·
«Responde a cualquier hora.» (una línea, ≈ 1050 px) · «De un chat / a su ficha.» · «La bienvenida sale sola.» (una línea, ≈ 970 px) ·
«Cada aviso, / a quien lo necesita.» · «Habla con tu iglesia, / sin perder a *nadie*». Las más anchas de la columna son «Alguien nuevo
escribe.» y «Habla con tu iglesia,» (≈ 890 y 850 px a 84 px, medidas con la de Academia: «que tu visión necesita» ≈ 890): entran en 936 px;
si `check` marca desborde, la columna crece hacia la ventana (nunca se baja la letra de 84).

### 1.3 Radios y sombras

Los del kit: `.k-ventana` radio **28** (celular) y **20** (`.k-ventana-escritorio`), anillo y sombra de `kit.css`, `overflow: hidden`. Frases
y ceja sin sombra ni brillo.

### 1.4 Disposición: dos escenarios

Igual que Academia §1.4:

| | Escenario del celular | Escenario del escritorio |
|---|---|---|
| Ventana | `#ventana-cel.k-ventana.k-ventana-16x9`: **x 1104 · y 90 · 720 × 900** | `#ventana-esc.k-ventana.k-ventana-escritorio`: **x 240 · y 260 · 1440 × 760** |
| Ceja | x 120 · y 412 | x 240 · y 92 |
| Frase | x 120 · y 460 · ancho 936 · hasta 2 líneas → termina en 635 | x 240 · y 132 · una línea → termina en 219 |
| Datos de ejemplo | dentro de la ventana, abajo a la izquierda, a 24 px | ídem |
| Final (desde el 2524) | la ventana a escala **0,92** con origen «100% 50%» y x **+24** | — |

- **Las dos ventanas viven en una tira horizontal** (`#escena`): el celular en x 1104 y el escritorio en x 240 + 1920 = **2160**. `#escena`
  en x 0 muestra el celular; en x **−1920**, el escritorio.
- **Sin tira vertical.** Cada ventana tiene **una sola ranura**; su contenido se cambia **solo mientras la ventana está fuera de cuadro**:
  | Ventana | 0–840 | 1310–1680 | 2030–2760 |
  |---|---|---|---|
  | celular | el clip (K), `#camK` | **la conversación de Mariana** (C·hilo…ficha), `#camM` | **la campaña nueva** (C·publico…preview), `#camC` |

  | Ventana | 830–1320 | 1670–2040 |
  |---|---|---|
  | escritorio | **el chatbot** (E·lienzo…horarios), `#camE1` | **la automatización** (E·autos…envios), `#camE2` |
- **Las frases y la ceja no viajan con el látigo:** salen con blur antes y entran después, en el lugar de su escenario (§1.6).
- El 90 % seguro para títulos (96 px a los lados, 54 arriba y abajo) se cumple en los dos escenarios.

```js
window.KD = {
  fps: 30,
  cel: { x: 1104, y: 90, w: 720, h: 900, hVis: 900 },          // --f-k = 720/1170 = 0.615385; --f-grab-alto = 1558.15px
  esc: { x: 240, y: 260, w: 1440, h: 760, hVis: 760 },         // K = 1440/1920 = 0.75; alto de la grabación ajustada = 810
  grabCel: { w: 1170, h: 2532, cssW: 390 },                    // celular 390×844 a 3×
  grabEsc: { w: 1920, h: 1080, cssW: 1280 },                   // escritorio 1280×720 a 1,5× (modo video de capturar.mjs)
  latigoH: 1920,                                               // la tira horizontal entre escenarios
  cambio: { escala: 0.92, x: 24, origen: '100% 50%' },         // la ventana del celular se hace a un lado (2524–2538)
};
```

### 1.5 La cámara: escalas de lectura

`enc(s, cx, cy)` del clip, una por ventana (con su `W`, `HV`, `PPC = W / cssW` y `VH`): pone el punto (cx, cy) en px CSS en el centro de lo
visible con la escala s, sin salirse de la grabación. **Una escala es de lectura si el texto de 14 px de la app queda en ≥ 28 px.**

**Celular (PPC 1,846):** G **1,085** (359 × 449 px CSS visibles; 14 px → 28,0) · G⁺ 1,15 (29,7) · **F 1,18** (330 × 413; 30,5; el final,
para que con la ventana a 0,92 el texto quede en 28,1) · M 1,40 (36,2) · C 1,80 (46,5). **Ningún encuadre de lectura del celular baja de
1,085.**

**Escritorio (PPC 1,125):** **D 1,80** (711 × 375 px CSS; 14 px → 28,4; un píxel de la grabación → 1,35 px) · D⁺ 2,00 (640 × 338; 31,5; el
tope). El plano entero del escritorio (s = 1) **solo existe durante el látigo**: el mundo aterriza ya en D.

### 1.6 Curvas y duraciones (cada tween con su curva por nombre)

| Papel | Curva | Cuadros | Detalle |
|---|---|---|---|
| `entrada-palabra` | `power4.out` | 4 | blur 6 → 0 + opacidad; sin desplazamiento; arranca un cuadro antes del pulso; palabras a 2 cuadros (la frase 1, una landing por pulso, como el clip) |
| `entrada-linea` | `power4.out` | 6 | la línea entera, blur 8 → 0 (la frase 2 y cada entrada de la ceja) |
| `salida-texto` | `power3.in` | 4–5 | blur 0 → 8 + opacidad; empieza 3 cuadros antes del golpe del cambio de mundo |
| `camara` | `power2.inOut` | **14** | un movimiento por compás; después, quieta; nunca mientras la app se desplaza sola |
| `camara-corte` | escalón | 1 | `tl.set` del encuadre en el **mismo cuadro** de un corte en que cambia la pantalla entera: 480 y 602 (del clip), **1803** y **1923** |
| `punch` | `power2.inOut` | **9** | **1560** (la ficha de Mariana) |
| `latigo-h` | `power3.inOut` | **10** | `#escena` 1920 px: **a la izquierda = al escritorio, a la derecha = de vuelta**; termina en el golpe (830–840, 1310–1320, 1670–1680, 2030–2040); la ventana que llega aterriza 1,04 → 1,00 (`power3.out`, 10 cuadros, desde su centro) |
| `match-cut` | — | — | el del clip (78–88, 1,03 → 1,00), sin cambios |
| `ventana-cambio` | `power2.inOut` | 15 | 2524–2538: escala 1 → 0,92, origen «100% 50%», x +24 |
| `halo` | `sine.out` | 90 | §1.1 |
| `dip` | escalón | 3 | `rgba(6,13,31,.40)` sobre las dos ventanas, 2757–2759 |
| marcas de toque | las del clip | — | aparece 4 cuadros antes, se hunde en el cuadro, se va 6 después; la onda de 450 ms (3 cuadros donde la pantalla cambia debajo del dedo) |
| velocidad de la grabación | `data-playback-rate` | — | **1×** en todo; nada se acelera ni se frena |
| cierre | las del kit | 150 | no se imita en el cuerpo |

`data-motion-blur="on"` y `data-motion-blur-shutter="180"` en la raíz (los látigos se ven con el borrón real). Nunca `filter: blur()` sobre
una grabación.

### 1.7 Sonido

| Capa | Fuente | Nivel | Regla |
|---|---|---|---|
| Música | `assets/musica/product-launch-recorrido.wav` (§0.1) | 0,75 en el carril | §0.4 |
| Sonidos de acción | kit v1.1 (`toque` en tres tomas a/b/c: `identidad/audio/toque.wav` y `assets/audio/toque-b.wav`, `toque-c.wav` del clip), `aparicion`, `desliz`, `subida`, `confirmacion` | **1,0**; **1,4** solo en las tres pruebas y el primer látigo | `data-start = (cuadro de la imagen + 1) / 30 − acento` (toque 0 · aparicion 0 · desliz 0,2 · subida 1,5 · confirmacion 0,1) |
| Sonido de marca | `identidad/audio/sonido-marca.wav` | 1 | **92,38 s** (inicio del cierre + 0,38 de `kit.json`) |
| Mezcla de entrega | — | **−16 LUFS** integrada, pico real ≤ **−1 dBTP** | `npx hyperframes audio` sobre el render; si −16 pasa el pico, se bajan a 1,2 los sonidos de 1,4 antes que dejar la mezcla más baja (el clip quedó en −17,1: se anota igual) |

**Los eventos de la parte 1 (0–839)** son los 16 del clip (`clip-sitio-comunicaciones/_gen/gen.py` → `SONIDOS`: nueve `toque`, tres
`aparicion`, tres `confirmacion` y un `desliz`, con sus niveles), **sin** la `subida` del 796 ni el sonido de marca del 851.

**Los eventos de la parte 2** (cuadro de la imagen → `data-start` en s):

| Imagen | Sonido | `data-start` | Nivel | Causa en pantalla |
|---|---|---|---|---|
| 840 | `desliz` | 27,833 | **1,4** | Látigo al escritorio |
| 900 | `toque` a | 30,033 | 1 | «Probar» |
| 960 | `toque` b | 32,033 | 1 | «Escribe como la persona…» (el toque del campo; las teclas de «hola» no suenan) |
| 990 | `toque` c | 33,033 | 1 | «Enviar» |
| 1020 | `aparicion` | 34,033 | 1 | El chatbot contesta: el saludo y el menú |
| 1140 | `toque` a | 38,033 | 1 | «Horarios» |
| 1155 | `confirmacion` | 38,433 | **1,4** | El horario (la primera prueba de la parte 2) |
| 1320 | `desliz` | 43,833 | 1 | Látigo de vuelta al celular |
| 1380 | `toque` b | 46,033 | 1 | El ícono de la persona → el panel |
| 1440 | `toque` c | 48,033 | 1 | «Crear ficha» (panel) |
| 1500 | `toque` a | 50,033 | 1 | «¿Cómo llegó?» |
| 1530 | `toque` b | 51,033 | 1 | La forma de llegada |
| 1545 | `toque` c | 51,533 | 1 | «Crear ficha» (formulario) |
| 1560 | `confirmacion` | 51,933 | **1,4** | La ficha de Mariana Ospina |
| 1680 | `desliz` | 55,833 | 1 | Látigo al escritorio |
| 1800 | `toque` a | 60,033 | 1 | La tarjeta «Bienvenida a quien llega» |
| 1803 | `aparicion` | 60,133 | 1 | La automatización con la vista previa del mensaje |
| 1920 | `toque` b | 64,033 | 1 | «Envíos» (fuera de cuadro: se oye y no se dibuja) |
| 1923 | `aparicion` | 64,133 | 1 | Los nombres |
| 2040 | `desliz` | 67,833 | 1 | Látigo de vuelta al celular |
| 2100 | `toque` c | 70,033 | 1 | «Un público» |
| 2130 | `toque` a | 71,033 | 1 | «Agregar filtro» |
| 2160 | `toque` b | 72,033 | 1 | «Red» |
| 2190 | `toque` c | 73,033 | 1 | «Red Timoteo» |
| 2220 | `toque` a | 74,033 | 1 | «Aplicar» |
| 2235 | `confirmacion` | 74,433 | **1,4** | «Red: Red Timoteo» y la cifra (la tercera prueba) |
| 2280 | `desliz` | 75,833 | 1 | La app sube al mensaje (cámara quieta) |
| 2310 | `toque` b | 77,033 | 1 | «Plantilla aprobada» |
| 2340 | `toque` c | 78,033 | 1 | «invitacion_culto» |
| 2343 | `aparicion` | 78,133 | 1 | La vista previa de WhatsApp se llena |
| 2400 | `desliz` | 79,833 | 1 | La app sube a la vista previa (**solo si** la grabación sube: §2.2) |
| 2716–2773 | `subida` | **90,533** | 1 | Hacia el cierre (golpe en el 2761) |
| 2771 | marca | 92,38 | 1 | Las campanas del cierre |

Sin tics de tecla (ni en «hola» ni en ningún campo). **Dos sonidos de acción nunca se enciman, salvo** 1800 + 1803, 1920 + 1923 y 2340 +
2343 (toque y su resultado). La `subida` es la única del video.

### 1.8 BANNED: los valores por defecto prohibidos, con nombre

Valen enteros los de `clip-sitio-membresia/SPEC.md` §1.8, los de `clip-sitio-comunicaciones/SPEC.md` §1.8 y los 27, 30, 31, 33, 34, 35,
36 y 37 de `recorrido-academia/SPEC.md` §1.8 (cursor de ratón; transiciones fuera de la serie; escritorio fuera de 1,8–2,0; cambiar la
frase del sitio o el cierre; fundido de música; frases viajando con el látigo; números dibujados o cifras sin «Datos de ejemplo»; marcos de
navegador o de teléfono). Además:

38. **Un crédito, un saldo, un cupo, un precio, un tope o un costo de Meta en cuadro** (decisión 215). Nunca entran: la sección «6 Revisar y
    enviar» de la campaña («Calcular», «Enviar ahora», el cálculo), la sección «5 Revisar y encender» de la automatización (el estimado,
    «Cambiar el tope»), la pestaña «Uso» ni el diálogo del costo. Si un encuadre los roza, se sube o se corta antes; nunca se tapan con algo
    dibujado.
39. **Hacer pasar «Probar» por WhatsApp real.** El primer encuadre del simulador (905–959) deja legibles «Probar el flujo» y «Es una prueba:
    no se envía nada por WhatsApp ni queda nada guardado»; la frase dice «Responde a cualquier hora», nunca «Te escribió…».
40. **Sugerir que Mariana recibió la bienvenida.** Ningún gráfico, flecha, resaltado ni corte la pone en la lista de envíos; la lista es la
    de la grabación (las cuatro personas de la semilla).
41. **Mostrar la búsqueda de la persona de prueba.** El corte del 905 salta de la acción de «Probar» al cuadro con «Probando como Carolina
    Mejía Arango»: es un ajuste de la prueba. Es el único salto sobre una acción de la parte 2; todo lo demás se ve tocar (o, en el 1920,
    se oye: «Envíos» queda fuera del encuadre del mensaje).
42. **Un látigo vertical.** En este recorrido nadie cambia de persona: solo látigo horizontal, el match cut del clip, los cortes de la app y
    el dip al cierre. Tampoco hay iris: el panel, el diálogo de la ficha y las hojas de los filtros entran con su propia animación (o en un
    corte en la espera), y el montaje no les agrega nada.
43. **Leer cada paso del formulario de la ficha o del editor de públicos.** Un toque por pulso, la cámara quieta; se lee el resultado
    (la ficha, el chip y la cifra), no los campos.
44. **Mover la cámara mientras la app se desplaza o re-acomoda** (la lista de envíos que entra, la cifra que corre, la página que sube en
    2280 y 2400, la vista previa que crece en 2343).

---

## 2. Los planos, cuadro por cuadro

### 2.0 Convenciones

- **Grabaciones:** **K** = la del clip (`assets/grabaciones/clip/grabacion.mp4`, 1170×2532, 53,4 s; sus cuadros como en el REVIEW del
  clip); **C** = la nueva de celular (`assets/grabaciones/celular/`, escena §3.2); **E** = la nueva de escritorio
  (`assets/grabaciones/escritorio/`, escena §3.3). «C·ficha» = el tramo `ficha` de C en su `pasos.json`; «+N» = N cuadros después de la
  acción de ese paso.
- **Niveles:** G, G⁺, F, M, C (celular) y D, D⁺ (escritorio), de §1.5. «Sobre X» = la caja de X (`pasos.json` → `caja`, px CSS) centrada en
  lo visible. **«(real)»** = la caja no se conoce hasta grabar: se toma de `pasos.json` o del cuadro y se anota en el REVIEW.
- **Pulso:** el cuadro de §0.3; un evento «en el 1380» se ve en el 1380 y suena en el 1381.
- **Cortes:** «corte en la espera» = el cuadro siguiente salta sobre la carga, la onda o el esqueleto de la app (nunca se ve «Cargando…», la
  K del cargador ni un esqueleto); «corte invisible» = la pantalla es idéntica a los dos lados.
- Las frases, siempre en el lugar de su escenario (§1.4); una a la vez; la ceja encima.

### 2.1 Parte 1 (0–839): el clip en 16:9

Se copia `clip-sitio-comunicaciones/index.html` (o se regenera con su `_gen/gen.py` y una plantilla 16:9) y se cambia **solo** esto:

1. **Formato:** raíz 1920×1080, `data-duration="97"`. `#ventana` del clip → `#ventana-cel` con `.k-ventana-16x9` dentro de `#escena`;
   `window.KD` de §1.4 (`W` 720, `HV` 900, `K` 0,615385, `PPC` 1,846, `VH` 1558,15). Las marcas de toque siguen en `calc(px * var(--f-k))`
   con el `--f-k` nuevo.
2. **Los mismos 19 tramos de video** (v01–v19 de `gen.py` → `TRAMOS`), con sus mismos `data-start`, `data-duration` y `data-media-start`,
   desde `assets/grabaciones/clip/grabacion.mp4`; las mismas 8 marcas (`MARCAS`); el mismo match cut (78–88).
3. **Las cámaras, con el piso de lectura de 16:9** (`s' = max(s, 1,085)`). A 1,085 se ven 359 × 449 px CSS: el mismo alto que el clip a
   s = 1 (439) más 10 px, y 31 px menos de ancho. Los centros se corrigen solo donde un borde que el REVIEW del clip dejó fuera volvería a
   entrar:

   | Encuadre | Clip (s · cx · cy → CSS visible) | 16:9 (s · cx · cy) | CSS visible | Por qué |
   |---|---|---|---|---|
   | `cola` | 1 · 195 · 392,4 → 173–612 | 1,085 · 195 · **397,7** | 173–622 | El borde de «Tomar» (171) sigue fuera |
   | `hilo` | 1,03 · 197 · 262 → 49–475 × 8–386 | 1,085 · 197 · 262 | 37–487 × 17–377 | La burbuja (desde x 12) y «En la cola» (hasta 382) pierden ≤ 5 px de su borde, **ninguna letra** (el texto empieza en ≈ 22 y termina en ≈ 372): se revisa (§4.1) |
   | `compositor` | 1,05 · 196,5 · 600 → 391–809 | 1,085 · 196,5 · 600 | 375–825 | Ídem en los bordes del compositor y de enviar |
   | `respuesta` | 1,04 · 196 · 380 → 169–591 | 1,085 · 196 · **393,7** | 169–618 | El subrayado de la pestaña (sobre 169) sigue fuera al volver |
   | `arriba` | 1 · 195 · 219,5 → 0–439 | 1,085 · 195 · **224,7** | 0–449 | — |
   | `campanas` | 1,08 · 195 · 321 → 118–524 | 1,085 · 195 · **300,3** | 76–525 | El aviso «Fuera del horario de envío» (526–554) sigue fuera; entra un poco más arriba |
   | `invitacion` | 1 · 195 · 560 → 341–780 | 1,085 · 195 · 560 | 335–785 | (el aviso, en 181–197 después del salto, fuera) |
   | `tarjeta` | 1,08 · 195 · 580 → 377–783 | 1,085 · 195 · 580 | 355–805 | — |
   | `kpis` | 1 · 195 · 520 → 300–739 | 1,085 · 195 · 520 | 295–745 | El bloque «Por qué no les llegó» (88–178) sigue fuera |
   | `nombres` | 1,06 · 195 · 393 → 186–600 | 1,085 · 195 · **410,7** | 186–635 | Ídem |
   | `cierre` | 1,08 · 195 · 465 → 262–668 | 1,085 · 195 · 465 | 240–690 | Seis nombres con «Leído» y «↩ Allí estaré» |

   Los mismos movimientos y en los mismos cuadros (90, 150, 315, 390, 450, 540, 690, 720) y los mismos `tl.set` (480 y 602). Con todas a
   1,085, los movimientos del clip entre ×1,00 y ×1,08 quedan como paneos: está bien (la cámara sigue moviéndose una vez por compás).
4. **Las frases** van a la columna izquierda (§1.4): la 1 y la 2 igual que en el clip; **la 3 se queda hasta el 837** (sale 837–841, con el
   látigo horizontal); la 4 del clip (la del sitio) **no va aquí**: pasa al 2520. La ceja entra en el 195 como en el clip y se queda.
5. **Se quitan:** la ventana a un lado del 724–738, la `subida` del 796, el dip del 837–839, la firma del 840 y su sonido de marca.
6. **Del 720 al 839:** la cámara va a `cierre` en el 720–733 (como el clip) y se queda: los nombres con «Allí estaré» quedan 3,6 s en
   pantalla (el «Allí estaré» vuelve en el 2340).

### 2.2 Parte 2 (840–2909): tabla maestra

| Cuadro | Pulso | La app (grabación) | Cámara | Texto | Sonido | Transición |
|---|---|---|---|---|---|---|
| 830–840 | | el celular (K, los nombres) sale a la izquierda con `#escena`; e1 llega desde la derecha: **E·lienzo**, el editor de «Bienvenida con menú»: la cabecera (el nombre, «Lienzo», «Palabras de activación», «Probar»), el lienzo con sus pasos y, a la derecha, el panel de las palabras («hola», «menu», «buenas») | e1 llega en **D** sobre el paso **«Botones · ¿En qué te podemos ayudar?»** y sus tres salidas «Horarios · Oración · Hablar con alguien», con lo que quepa de los pasos a los que llevan (real) | frase 3 sale 837–841; la ceja sale 837–840 | `desliz` acento 841 (1,4) | **Látigo horizontal a la izquierda**; e1 aterriza 1,04 → 1,00 (840–850); halo |
| **840** | ● 1,00 | E·lienzo quieto | D | ceja arriba (`entrada-linea`, 842–848); «Responde · a · cualquier · hora.» 843 · 845 · 847 · 849 | | |
| 870 | ● | quieto | 870–883 → **D** sobre «Probar» y el panel de las palabras, con «hola» a la vista (real) | | | |
| **900** | ● 0,84 | toque «Probar» (E·probar, la acción) | quieta | | `toque` a | marca de toque |
| 905 | | **corte (BANNED 41):** el cuadro de E·como +N en que ya se lee **«Probando como Carolina Mejía Arango»**: el panel es el simulador: «Probar el flujo» · «Es una prueba: no se envía nada por WhatsApp ni queda nada guardado.» · «Probando como…» · «Toca «Empezar este flujo» o escribe una palabra de activación.» · «Empezar este flujo» · «Escribe como la persona…» | 905–918 → **D⁺** sobre el simulador, de su título al campo de abajo (real; si no cabe entero, el título, el aviso y «Probando como…» mandan, y el campo entra en el 960) | | | |
| **960** | ● 0,92 | toque en «Escribe como la persona…» y **«hola» se escribe** (E·hola: 4 teclas a 70 ms, 961–975) | quieta | | `toque` b | marca (la costura de la música cae aquí) |
| 990 | ● | toque «Enviar» (E·enviar, la acción): «hola» queda a la derecha | quieta | | `toque` c | marca |
| **1020** | ● 0,77 | corte en la espera: **«Empezó el flujo «Bienvenida con menú»»** · **«¡Hola Carolina! Bienvenido a Kingdom Demo.»** · **«¿En qué te podemos ayudar?»** con **Horarios · Oración · Hablar con alguien** (E·enviar +N, real) | quieta | | `aparicion` | |
| **1080** | ● 0,76 | quieto | 1080–1093 → **D⁺** sobre el menú y sus tres botones (real) | | | |
| **1140** | ● 0,75 | toque «Horarios» (E·horarios, la acción) | quieta | | `toque` a | marca |
| 1155 | ● | corte en la espera: «Horarios» (de Carolina, a la derecha) · **«Nos reunimos los domingos a las 8:00 a. m. y a las 10:30 a. m., y los miércoles a las 7:00 p. m. ¡Te esperamos!»** · «El flujo terminó» (E·horarios +N, real) | quieta | | `confirmacion` (1,4) | |
| **1200** | ● 0,67 | quieto | 1200–1213 → **D⁺** sobre la burbuja del horario y «El flujo terminó» (real) | | | |
| 1214–1309 | | quieto: el horario se lee 3,2 s | quieta | | | |
| 1310–1320 | | e1 sale a la derecha; vuelve el celular con **C·hilo**: la conversación de Mariana | m llega en **G** sobre la cabecera, su burbuja, la nota «… tomó la conversación» y la respuesta (real) | frase 4 y ceja salen 1317–1320 | `desliz` | **Látigo horizontal a la derecha**; aterriza 1320–1330; halo |
| **1320** | ● 0,93 | C·hilo: «Mariana Ospina» · «Sin ficha · +575550123987 · Línea principal» · **«Atendiendo»** · «Hola, buenas noches. ¿A qué hora es el culto del domingo? Es mi primera vez y quiero ir con mi esposo.» · «Andrés Felipe Restrepo Gómez tomó la conversación» · **«Nos reunimos los domingos a las 8:00 a. m. y a las 10:30 a. m., y los miércoles a las 7:00 p. m.»** con una palomita | G | ceja a la izquierda (1322–1328); «De · un · chat / a · su · ficha.» 1322 · 1324 · 1326 · 1328 · 1330 | | |
| **1380** | ● 0,90 | toque en el ícono de la persona (`#btn-panel`, C·panel): el panel «La persona» se superpone desde la derecha (su animación real) | quieta (el ícono está en la cabecera: a la vista desde el 1320) | | `toque` b | marca |
| **1395** | ● 0,89 | quieto: el panel: «La persona» · «Mariana Ospina» · «+575550123987» · «Este número no está en Membresía. Vincúlalo a una persona o crea su ficha (Kingdom revisa que no esté repetida).» · «Vincular a una persona» · **«Crear ficha»** | 1395–1408 → **G** sobre lo alto del panel (real; el panel ocupa x 38–390: el encuadre llega al borde derecho de la grabación) | | | |
| **1440** | ● 0,96 | toque «Crear ficha» (C·crear, la acción) | quieta | | `toque` c | marca |
| 1455 | ● | corte en la espera: el diálogo **«Crear ficha»** · «Con el número +575550123987. Completa lo demás desde Membresía cuando quieras.» · Nombres **Mariana** · Apellidos **Ospina** · Género · «¿Cómo llegó?» (C·crear +N) | 1455–1468 → **G** sobre el diálogo (real) | | | |
| **1500** | ● 0,88 | toque «¿Cómo llegó?» (C·forma) | quieta | | `toque` a | marca |
| 1515 | ● | corte en la espera: las formas de llegada (real) | quieta | | | |
| 1530 | ● | toque en la forma (C·forma-opcion: la de la `ref` `forma`): el campo queda con ella | quieta | | `toque` b | marca (3 cuadros: la lista se cierra) |
| 1545 | ● | toque «Crear ficha» del diálogo (C·guardar; si la escena tuvo que tocar «Crear de todos modos», la marca va sobre ese botón y su cuadro: §3.2) | quieta | | `toque` c | marca |
| **1560** | ● 1,00 | corte en la espera: el diálogo se fue; **el panel es el de la ficha: «Mariana Ospina»**, su número y **«Ver ficha»**; la cabecera del hilo ya no dice «Sin ficha» (C·ficha) | **punch** 1560–1568 → **M** sobre el nombre en el panel | | `confirmacion` (1,4) | |
| **1620** | ● 0,84 | quieto | 1620–1633 → **G** sobre el panel entero (el nombre, el número, «Ver ficha» y lo que siga, p. ej. «Campañas por WhatsApp · Recibe las campañas de la iglesia.», real) | | | |
| 1670–1680 | | el celular sale a la izquierda; e2 llega: **E·autos**, «Automatizaciones» | e2 llega en **D** sobre las dos primeras tarjetas (real) | frase 5 y ceja salen 1677–1680 | `desliz` | **Látigo horizontal a la izquierda**; aterriza 1680–1690; halo |
| **1680** | ● 0,98 | E·autos: **«Bienvenida a quien llega · Encendida»** · «Cuando llega una persona nueva (1 h después)» · la fuente · **«Hoy: 4 enviados · 0 omitidos»**; al lado, «Feliz cumpleaños · Encendida» (real) | D | ceja arriba (1682–1688); «La · bienvenida · sale · sola.» 1683 · 1685 · 1687 · 1689 | | |
| **1740** | ● 0,79 | quieto | 1740–1753 → **D⁺** sobre la tarjeta «Bienvenida a quien llega» | | | |
| **1800** | ● *1,00* | toque en la tarjeta (E·abrir, la acción) | quieta | | `toque` a | marca |
| 1803 | | corte en la espera: la automatización: la banda «Encendida · Hoy: 4 enviados · 0 omitidos», las pestañas «Configuración · Envíos · Historial» y, a la derecha, **la vista previa: «Hola Ana, gracias por visitarnos en Kingdom Demo. Alguien del equipo te escribirá para acompañarte. Si necesitas algo, responde a este mensaje.»** (E·abrir +N) | **`camara-corte` en el 1803 → D⁺ sobre la vista previa** (real) | | `aparicion` 1804 | |
| 1804–1919 | | quieto: el mensaje se lee 3,9 s | quieta | | | |
| **1920** | ● *1,00* | toque «Envíos» (E·envios; **fuera de cuadro: se oye y no se dibuja**) | quieta | | `toque` b | — |
| 1923 | | corte en la espera: la configuración y la vista previa se van; **los envíos**: «Mateo Arango Vélez», «Sara Lucía Bermúdez Ríos», «Tomás Cano Ochoa», «Isabela Muñoz Salazar», cada uno con **«Leído»** o «Entregado» y su línea (de qué salió, cuándo; real) | **`camara-corte` en el 1923 → D** sobre las pestañas y la lista (real) | | `aparicion` 1924 | |
| **1980** | ● *0,62* | quieto | 1980–1993 → **D⁺** sobre las cuatro filas (nombre y estado) | | | |
| 2030–2040 | | e2 sale a la derecha; vuelve el celular con **C·publico**: una campaña nueva, ya en **«2 A quién va»**: «Membresía · Por evento», «Toda la iglesia · Un público» y la cifra de toda la iglesia «≈ N personas · M con WhatsApp» | m llega en **G** sobre la sección 2 entera (real) | frase 6 y ceja salen 2037–2040 | `desliz` | **Látigo horizontal a la derecha**; aterriza 2040–2050; halo |
| **2040** | ● *1,00* | quieto | G | ceja a la izquierda (2042–2048); «Cada · aviso, / a · quien · lo · necesita.» 2042 · 2044 · 2046 · 2048 · 2050 · 2052 | | |
| **2100** | ● | toque **«Un público»** (C·publico): aparece «Agregar filtro» y «Agrega al menos un filtro. Mientras tanto, va a toda la iglesia.» | quieta | | `toque` c | marca |
| 2130 | ● | toque **«Agregar filtro»** (C·agregar) | quieta | | `toque` a | marca |
| 2145 | ● | corte en la espera: la hoja «Agregar filtro» con sus grupos y **«Red»** (real) | quieta | | | |
| **2160** | ● *1,00* | toque **«Red»** (C·red) | quieta | | `toque` b | marca |
| **2175** | ● *1,00* | corte en la espera: el editor «Red» con las redes de la iglesia y su casilla (real) | quieta | | | |
| 2190 | ● | toque **«Red Timoteo»** (C·timoteo): la casilla se marca | quieta | | `toque` c | marca |
| 2220 | ● | toque **«Aplicar»** (C·aplicar) | quieta | | `toque` a | marca |
| **2235** | ● *1,00* | corte en la espera: la hoja se fue; el chip **«Red: Red Timoteo»**, el resumen en palabras y **la cifra que corre** (la animación de la app) hasta **«≈ N personas · M con WhatsApp»** de la red (C·cifra; se espera M = 139, el «139 Total» del reporte de la parte 1; real) | 2235–2248 → **G⁺** sobre el chip, el resumen y la cifra (real; la cámara se mueve sobre el bloque, que no se desplaza: lo que corre son los dígitos) | | `confirmacion` (1,4) | |
| **2280** | ● *0,77* | **la app sube** hasta «1 El mensaje» (C·subir: el desplazamiento suave de la app, ≈ 27 cuadros) | **quieta** (BANNED 44) | | `desliz` | |
| 2310 | ● | toque **«Plantilla aprobada»** (C·plantilla) | quieta (el campo queda en el centro de la vista después de subir) | | `toque` b | marca |
| 2325 | ● | corte en la espera: las plantillas aprobadas, con su categoría (real) | quieta | | | |
| **2340** | ● | toque **«invitacion_culto · marketing»** (C·invitacion): la lista se cierra y **la vista previa de WhatsApp, arriba, se llena** (la app re-acomoda la página) | quieta | | `toque` c · `aparicion` 2344 | marca |
| **2400** | ● *0,76* | si la vista previa quedó fuera de la vista: **la app sube a ella** (C·preview, desplazamiento suave); si ya está a la vista, quieto | quieta | | `desliz` (solo si sube) | |
| **2460** | ● | quieto: «Vista previa» · la burbuja **«Hola Ana, este domingo celebramos la Santa Cena. Te esperamos a las 10:30 a. m. con toda tu familia.»** · los botones **«Allí estaré»** y «Cómo llegar» (real) | 2460–2473 → **F (1,18)** sobre la burbuja y sus botones (real; si la burbuja no cabe en 330 px CSS, G⁺ 1,15 y se anota) | | | |
| **2520** | ● *0,80* | quieto | quieta | la ceja sale 2520–2523; «Habla · con · tu · iglesia, / sin · perder · a · *nadie*» 2519 · 2521 · … · 2533 (dos cuadros entre palabras) | | |
| 2524–2538 | | | | | | **La ventana a un lado**: 0,92, origen «100% 50%», x +24 |
| 2539–2756 | | quieto (C·preview, el final de su pausa) | quieta | la frase sostenida 7,9 s | `subida` desde 90,533 | |
| 2757–2759 | | | | | | **dip** sobre la ventana |
| **2760** | ● | — | — | — | marca en 92,38 | **corte al cierre del Comercial** (`#escena` oculta) |

### 2.3 Los planos de la parte 2

#### P8 · «Responde a cualquier hora» — 840–1319 (compases 15–22)
El látigo horizontal lleva de una conversación al lugar donde la iglesia arma lo que contesta sola: el lienzo del flujo. Dos segundos de
lienzo (el menú y sus tres salidas, las palabras «hola · menu · buenas»), «Probar» en el 900 y, en el corte, el simulador ya listo como
Carolina. **«hola» cae en la costura (960)**; el chatbot contesta en el 1020 con el saludo y el menú; **«Horarios» en el 1140** y, un
pulso después, **el mismo horario que Andrés le mandó a Mariana**. El respiro deja leer: la cámara se mueve una vez por compás (1080, 1200)
y nada más.

#### P9 · «De un chat a su ficha» — 1320–1679 (compases 23–28)
De vuelta al celular, **la misma conversación de la parte 1**, ya atendida y respondida. Cuatro toques en cuatro golpes (1380 el panel ·
1440 «Crear ficha» · 1500 y 1530 «¿Cómo llegó?» · 1545 «Crear ficha») y, en el golpe más fuerte de la parte 2 (**1560**), el panel con la
ficha de **Mariana Ospina**: el punch va a su nombre. 1620 abre al panel entero. Lectura: el diálogo con «Mariana» y «Ospina» ya puestos
se ve 1,5 s (1455–1499); lo que importa es que nadie los escribió.

#### P10 · «La bienvenida sale sola» — 1680–2039 (compases 29–34)
Segundo viaje al escritorio, a la primera frase del clímax. Las automatizaciones de la iglesia (la de la bienvenida y la del cumpleaños); la
cámara elige la de la bienvenida, que se dispara **«cuando llega una persona nueva»** —lo que acaba de pasar con Mariana—. **1800: toque** y,
en el corte, la vista previa del mensaje («gracias por visitarnos… alguien del equipo te escribirá para acompañarte»), que se lee casi 4 s.
**1920: «Envíos»** se oye y, en el corte, los cuatro nombres de quienes llegaron antes, con «Leído». El video no dice que Mariana es la
siguiente: lo deja a quien mira (BANNED 40).

#### P11 · «Cada aviso, a quien lo necesita» — 2040–2279 (compases 35–38)
De vuelta al celular, a la segunda frase del clímax: una campaña nueva, en «A quién va». **Cinco toques, uno por pulso** (2100 · 2130 · 2160
· 2190 · 2220) arman el público con un filtro de Membresía —«Red: Red Timoteo»— y en el **2235** la cifra en vivo corre desde toda la
iglesia hasta la red: la misma red y, se espera, el mismo 139 de la invitación de la parte 1. La cámara se mueve una vez, sobre el bloque
quieto.

#### P12 · «… y la vista previa» — 2280–2519 (compases 39–42)
La salida de la música, tranquila a propósito: la app sube al mensaje (2280), se elige la plantilla de la invitación (2310 · 2340) y la
vista previa de WhatsApp se llena arriba con el botón **«Allí estaré»** —el mismo de los nombres de la parte 1—. 2400, si hace falta, la app
sube a ella; 2460, la cámara se acerca a la burbuja. Nada se calcula ni se envía (BANNED 38): el mensaje y su público están listos.

#### P13 · La frase del sitio y el cierre — 2520–2909
«Habla con tu iglesia, sin perder a *nadie*» palabra a palabra en el 2520; la ceja se va; la ventana se hace a un lado (2524–2538) y todo
queda quieto salvo el halo; la `subida` empieza en el 90,533 y su golpe cae con el cierre. Dip 2757–2759. **2760: `cierre-comercial`**:

```html
<div id="cierre-comercial" data-composition-id="cierre-comercial" data-composition-src="identidad/cierre-comercial.html"
  data-variable-values='{"publico":"iglesia","llamado":"prueba","contacto":"sitio","fondo":"noche","idioma":"es"}'
  data-start="92" data-duration="5" data-track-index="6" data-width="1920" data-height="1080"></div>
<audio id="marca-cierre" src="identidad/audio/sonido-marca.wav" data-start="92.38" data-duration="2.1" data-track-index="26" data-volume="1"></audio>
```

---

## 3. Las grabaciones

### 3.1 Lo que se reusa

- **La grabación del clip, entera y sin cambios:** `clip-sitio-comunicaciones/assets/grabaciones/grabacion.mp4` (1170×2532, 30 fps, 53,4 s)
  y su `pasos.json` → `recorrido-comunicaciones/assets/grabaciones/clip/`. Se usan los mismos 19 tramos, las mismas 8 marcas y los mismos 16
  sonidos (§2.1, §1.7); nada de la parte 1 se vuelve a grabar.
- **El generador del clip:** `clip-sitio-comunicaciones/_gen/` (`gen.py`, `index.tpl.html`, `diff.py`, `sheet.py`, `rsheet.py`) →
  `recorrido-comunicaciones/_gen/`. `gen.py` suma tres tablas para la parte 2 (los tramos de C y de E con su grabación, sus marcas y sus
  sonidos de §1.7) y la plantilla pasa a 16:9 con las dos ventanas; `diff.py` y `sheet.py` sirven igual para hallar toques, esperas y saltos
  en las grabaciones nuevas.
- **Los sonidos del clip:** `clip-sitio-comunicaciones/assets/audio/toque-b.wav` y `toque-c.wav` → `recorrido-comunicaciones/assets/audio/`.
- **La música:** `recorrido-academia/assets/musica/product-launch-recorrido.wav` si ya existe (§0.1); si no, el `ffmpeg` de §0.1.
- **El kit:** `npm run kit` (monta `identidad/` con `cierre-comercial.html`, los sonidos de acción y el sonido de marca); `frame.md` =
  `identidad/frame-comercial.md`.

Dos escenas nuevas, una por dispositivo, sobre Kingdom Demo en español, con `capturar.mjs --modo video` y `toque: false`. La API de las
capturas va con Meta simulado, como pide `KingdomApp/docs/ayuda/capturas.md` → «Entorno» (`COM_GRAPH_FAKE=1`, `COM_DESPERTAR_WORKER=0`,
`COM_GRAPH_FAKE_PLANTILLAS=F:/dev/kingdom-local/ayuda_capturas_fake_plantillas.json`); sin ellas, la bandeja no envía. **Sin `COMO_IGLESIA`**:
con la sede en demo nada se cobra y nada de lo que se ve cambia (decisión 215).

```bash
cd F:/Proyectos/KingdomApp/tools/ayuda
node capturar.mjs clips/recorrido-comunicaciones-celular --idioma es --modo video      # → salida/video/es/clips/recorrido-comunicaciones-celular/
node capturar.mjs clips/recorrido-comunicaciones-escritorio --idioma es --modo video   # → salida/video/es/clips/recorrido-comunicaciones-escritorio/
# cada una: grabacion.mp4 + pasos.json; se copian a recorrido-comunicaciones/assets/grabaciones/celular/ y …/escritorio/
```

Lo que la herramienta ya hace y las escenas usan (sin nada nuevo): `como` e `ir` del primer paso antes de grabar; `ir` a mitad de la
escena; `escribir` a 70 ms por tecla (toca el campo primero); `ver` con desplazamiento suave (`block: 'center'`); `marcar` (toca la etiqueta
de la casilla); `clicSiHay` (espera 3 s); `espera` y `oculto`; `pausa` sin tope en video; `{ es, en }` en cualquier valor; `refs` con
`{@nombre}` (se consultan una vez, en orden, justo antes de abrir Chrome; sin valor, la escena no arranca). Cada corrida restaura el
volcado del día (y lo siembra de nuevo si no es de hoy): las dos escenas parten de la misma Kingdom Demo y no se pisan.

### 3.2 La escena de celular: `tools/ayuda/escenas/clips/recorrido-comunicaciones-celular.mjs`

```js
// Grabación para el RECORRIDO de Comunicaciones (LegacyHyperframes/videos/kingdomapp/recorrido-comunicaciones/SPEC.md §3.2): la parte 2 en
// CELULAR. NO es una escena de un artículo de la ayuda: no se publica ni entra en la frescura. Una sola escena de CELULAR (390×844 a 3x =
// 1170×2532, 30 cps) grabada SIN el círculo del toque (`toque: false`): el montaje dibuja el suyo sobre las cajas y los toques de pasos.json.
//   node capturar.mjs clips/recorrido-comunicaciones-celular --idioma es --modo video
//   → salida/video/es/clips/recorrido-comunicaciones-celular/grabacion.mp4 + pasos.json
// Todo con la cuenta 101 (el administrador, la única de Kingdom Demo con Comunicaciones) y la API de las capturas con Meta SIMULADO
// (COM_GRAPH_FAKE=1, COM_DESPERTAR_WORKER=0, COM_GRAPH_FAKE_PLANTILLAS: docs/ayuda/capturas.md → «Entorno»). Sin COMO_IGLESIA (decisión 215).
//   0. Fuera de cámara (se graba y no se usa): la conversación de Mariana queda como la deja la parte 1 del video (tomada y respondida con
//      «/horarios»), igual que en clips/comunicaciones-alguien-nuevo.mjs.
//   1. P9 (1320–1679): el panel «La persona», «Crear ficha» con «¿Cómo llegó?» y la ficha de Mariana Ospina en el panel.
//   2. P11–P13 (2040–2759): una campaña nueva: «Un público» con el filtro «Red: Red Timoteo» y su cifra; después, la plantilla
//      «invitacion_culto» y su vista previa de WhatsApp. NADA se calcula, se prueba ni se envía (la sección 6 nunca se toca).
// Datos ficticios de semillas/comunicaciones.php: Mariana Ospina (575550123987, sin ficha), la respuesta rápida «/horarios», la red Timoteo
// y la plantilla aprobada «invitacion_culto» («Allí estaré» · «Cómo llegar»).
import { CONV, SEDE } from '../../lib/escenas-comunicaciones.mjs';

const MARIANA = '#bandeja-lista .item[data-id="{@mariana}"]';
const HORARIOS = '#respuestas-sugeridas button.sug[data-atajo="horarios"]';
// La respuesta enviada: el horario dice «8:00» en los dos idiomas; Mariana no lo escribió.
const RESPUESTA = '.hilo .msg.sale:has-text("8:00")';
const FORMA = 'mat-option:has-text("{@forma}")';
const PLANTILLA = { es: 'mat-option:has-text("invitacion_culto")', en: 'mat-option:has-text("sunday_invitation")' };

export default {
  articulo: 'clips/recorrido-comunicaciones-celular',
  movil: true,
  toque: false,
  pantallas: [
    'frontend-v2/src/app/pages/comunicaciones/bandeja.page.ts',
    'frontend-v2/src/app/pages/comunicaciones/bandeja-hilo.component.ts',
    'frontend-v2/src/app/pages/comunicaciones/bandeja-panel.component.ts',
    'frontend-v2/src/app/pages/comunicaciones/bandeja-crear-ficha.component.ts',
    'frontend-v2/src/app/pages/comunicaciones/campana.page.ts',
    'frontend-v2/src/app/pages/comunicaciones/wa-preview.component.ts',
    'frontend-v2/src/app/components/segmento-editor/segmento-editor.component.ts',
    'frontend-v2/src/app/components/segmento-editor/segmento-filtro.component.ts',
    'frontend-v2/src/app/pages/membresia/filtro-editor.component.ts',
  ],
  refs: {
    // Mariana, en la cola y con la ventana de 24 h abierta (escribió hace menos de 20 h): la misma regla del clip. Si no, la escena se niega.
    mariana: `${CONV.sinFicha} AND estado = 'cola' AND ultimo_entrante_at > NOW() - INTERVAL 20 HOUR`,
    // Nadie con su número ni con su nombre en Membresía: «Crear ficha» no debería encontrar fichas parecidas (si las encuentra igual, abajo).
    nueva: `SELECT IF(COUNT(*) = 0, 1, NULL) FROM mem_personas WHERE id_sede = ${SEDE}
              AND (whatsapp_e164 IN ('575550123987', '+575550123987') OR (nombres = 'Mariana' AND apellidos = 'Ospina'))`,
    // La forma de llegada que se elige en «¿Cómo llegó?»: la de WhatsApp o redes sociales si la demo la tiene; si no, la primera activa.
    forma: `SELECT nombre FROM mem_formas_llegada WHERE id_sede = ${SEDE} AND activa = 1
              ORDER BY (nombre LIKE '%WhatsApp%') DESC, (nombre LIKE '%edes%') DESC, orden, id LIMIT 1`,
    // La red de la invitación del clip (la casilla del filtro «Red» lleva su id en data-opcion).
    timoteo: `SELECT id FROM mem_redes WHERE id_sede = ${SEDE} AND nombre IN ('Red Timoteo', 'Timothy Network') LIMIT 1`,
  },
  pasos: [
    // ── 0. Fuera de cámara: la conversación de Mariana como la deja la parte 1 (se graba con pausas cortas y se descarta).
    { como: 101, ir: '/servir/comunicaciones/bandeja', espera: MARIANA, pausa: 300 },
    { clic: MARIANA, espera: '#btn-tomar', pausa: 300 },
    { clic: '#btn-tomar', espera: '#hilo-estado[data-estado="atencion"]', pausa: 300 },
    { escribir: { en: '#compositor', texto: '/' }, espera: HORARIOS, pausa: 300 },
    { clic: HORARIOS, oculto: '#respuestas-sugeridas', pausa: 300 },
    { clic: '#btn-enviar', espera: RESPUESTA, pausa: 300 },

    // ── 1. P9 · De un chat a su ficha.
    { tramo: 'hilo', ver: RESPUESTA, pausa: 2600 },                                                          // 1320–1379 (el hilo quieto)
    { tramo: 'panel', clic: '#btn-panel', espera: '#btn-panel-crear-ficha', pausa: 2200 },                  // 1380 → 1395–1439
    { tramo: 'crear', clic: '#btn-panel-crear-ficha', espera: '#ficha-forma', pausa: 1800 },                // 1440 → 1455–1499
    { tramo: 'forma', clic: '#ficha-forma', espera: FORMA, pausa: 900 },                                    // 1500 → 1515
    { tramo: 'forma-opcion', clic: FORMA, oculto: '.mat-mdc-select-panel', pausa: 900 },                    // 1530
    { tramo: 'guardar', clic: '#btn-ficha-crear', pausa: 400 },                                             // 1545
    // Plan B: si aun así hay fichas parecidas, «Crear de todos modos» (el montaje marca este toque en el 1545 en lugar del anterior).
    { clicSiHay: '#btn-ficha-forzar' },
    { tramo: 'ficha', espera: '#panel-ficha', pausa: 3500 },                                                // 1560–1679

    // ── 2. P11–P13 · La campaña nueva. La entrada y la bajada a «A quién va» se graban y no se usan (el mundo llega en el 2040 ya ahí).
    { ir: '/servir/comunicaciones/campanas/nueva', espera: '#camp-publico-uno', pausa: 300 },
    { ver: '#camp-publico', pausa: 900 },
    { tramo: 'publico', clic: '#camp-publico-uno', espera: '#camp-publico-agregar', pausa: 1600 },          // 2040–2129 (la cifra de toda la iglesia, 2100 el toque)
    { tramo: 'agregar', clic: '#camp-publico-agregar', espera: '#po-lista-filtros [data-filtro="red"]', pausa: 900 },  // 2130 → 2145
    { tramo: 'red', clic: '#po-lista-filtros [data-filtro="red"]', espera: '#editor-filtro[data-tipo="red"]', pausa: 900 },   // 2160 → 2175
    { tramo: 'timoteo', marcar: '#editor-filtro mat-checkbox[data-opcion="{@timoteo}"]', pausa: 900 },      // 2190
    { tramo: 'aplicar', clic: '#btn-aplicar-filtro', oculto: '#editor-filtro', pausa: 300 },                // 2220
    // La cifra se pide 400 ms después del último cambio y corre con su animación: se espera de sobra (2235–2279).
    { tramo: 'cifra', espera: '#camp-publico [data-chip="red"]', pausa: 3200 },
    { tramo: 'subir', ver: '#camp-plantilla', pausa: 1200 },                                                // 2280 (la app sube)
    { tramo: 'plantilla', clic: '#camp-plantilla', espera: PLANTILLA, pausa: 900 },                         // 2310 → 2325
    { tramo: 'invitacion', clic: PLANTILLA, oculto: '.mat-mdc-select-panel', pausa: 1500 },                 // 2340 (la vista previa se llena)
    // La vista previa (arriba del formulario en el celular): si quedó fuera de la vista, la app sube a ella (2400). Quieta hasta el final.
    { tramo: 'preview', ver: 'app-wa-preview', pausa: 12500 },                                              // 2400–2759
  ],
};
```

**Comprobaciones obligatorias al grabar** (si una falla, se vuelve a grabar):
1. En el primer cuadro del tramo `hilo`, la cabecera dice «Sin ficha» y «Atendiendo», y el hilo trae la pregunta de Mariana, la nota «…
   tomó la conversación» y la respuesta con el horario (una palomita).
2. El panel del tramo `ficha` dice **«Mariana Ospina»** con «Ver ficha» (`#panel-ficha`). Si en `pasos.json` el paso del `clicSiHay` trae
   un toque, hubo fichas parecidas: el REVIEW lo anota y el toque del 1545 se dibuja sobre «Crear de todos modos» (su cuadro se toma de ese
   paso). El diálogo con «Ya hay fichas parecidas» **no se corta**: si apareció, se ve en el 1545.
3. El chip dice **«Red: Red Timoteo»** y la cifra terminó de correr antes del final del tramo `cifra`; el número se anota en el REVIEW
   (ninguna frase lo nombra).
4. Ningún cuadro usado (1320–1679 y 2040–2759) muestra la sección «6 Revisar y enviar», «Calcular», ni un número de cupo o créditos.
5. La vista previa trae la burbuja con «Allí estaré» y «Cómo llegar»; el REVIEW anota si el tramo `preview` tuvo que subir (decide el
   `desliz` del 2400).

### 3.3 La escena de escritorio: `tools/ayuda/escenas/clips/recorrido-comunicaciones-escritorio.mjs`

```js
// Grabación para el RECORRIDO de Comunicaciones (LegacyHyperframes/videos/kingdomapp/recorrido-comunicaciones/SPEC.md §3.3): la parte 2 en
// ESCRITORIO. NO es una escena de un artículo de la ayuda. En video el escritorio es 1280×720 a 1,5x (1920×1080 reales, 30 cps), sin cursor
// ni círculo (`toque: false`): el montaje dibuja su marca de toque sobre las cajas de pasos.json.
//   node capturar.mjs clips/recorrido-comunicaciones-escritorio --idioma es --modo video
//   → salida/video/es/clips/recorrido-comunicaciones-escritorio/grabacion.mp4 + pasos.json
// Una cuenta: 101, el administrador. API de las capturas con Meta SIMULADO; sin COMO_IGLESIA (decisión 215).
//   1. chatbot (P8, 840–1319): el flujo «Bienvenida con menú» en el lienzo; «Probar» como Carolina (la persona de la semilla que llegó a la
//      cola por este flujo), «hola», el menú y «Horarios» → el horario. «Probar» no envía ni guarda nada (comBotProbar).
//   2. automatización (P10, 1680–2039): la lista, «Bienvenida a quien llega» con su vista previa y la pestaña «Envíos» (las cuatro
//      personas nuevas de la semilla). Nada se enciende, se estima ni se guarda.
import { REF } from '../../lib/escenas-comunicaciones.mjs';

// Carolina: la persona que escribió «Hola» → «Hablar con alguien» → «Quiero saber cómo puedo servir en el grupo de alabanza».
const CAROLINA = `(SELECT c.id_persona FROM com_conversaciones c WHERE c.id = (SELECT id_conversacion FROM com_mensajes
                   WHERE direccion = 'entrante' AND (texto LIKE '%alabanza%' OR texto LIKE '%worship%') ORDER BY id LIMIT 1))`;
const CANDIDATA = '.candidatos button:has-text("{@carolina-apellido}")';
const HORARIOS_BOT = { es: '#sim-chat button.op:has-text("Horarios")', en: '#sim-chat button.op:has-text("Service times")' };

export default {
  articulo: 'clips/recorrido-comunicaciones-escritorio',
  toque: false,
  pantallas: [
    'frontend-v2/src/app/pages/comunicaciones/chatbot-editor.page.ts',
    'frontend-v2/src/app/pages/comunicaciones/chatbot-simulador.component.ts',
    'frontend-v2/src/app/pages/comunicaciones/automatizaciones.page.ts',
    'frontend-v2/src/app/pages/comunicaciones/automatizacion.page.ts',
    'frontend-v2/src/app/pages/comunicaciones/auto-actividad.component.ts',
    'frontend-v2/src/app/pages/comunicaciones/wa-preview.component.ts',
  ],
  refs: {
    flujo: REF.flujoBienvenida,
    carolina: `SELECT nombres FROM mem_personas WHERE id = ${CAROLINA}`,
    'carolina-apellido': `SELECT SUBSTRING_INDEX(apellidos, ' ', 1) FROM mem_personas WHERE id = ${CAROLINA}`,
    auto: REF.autoBienvenida,
    // Los envíos de la bienvenida que dejó la semilla (las cuatro personas nuevas): al menos tres en campaña, o la escena se niega.
    envios: `SELECT IF(COUNT(*) >= 3, COUNT(*), NULL) FROM com_auto_disparos WHERE id_automatizacion = (${REF.autoBienvenida}) AND estado = 'en_campana'`,
  },
  pasos: [
    // ── 1. El chatbot (P8). La entrada se hace antes de grabar: el video abre en el editor del flujo, con el lienzo y las palabras.
    { tramo: 'lienzo', como: 101, ir: '/servir/comunicaciones/chatbot/{@flujo}', espera: '#btn-probar', pausa: 2600 },   // 830–899
    { tramo: 'probar', clic: '#btn-probar', espera: '#sim-buscar-persona', pausa: 500 },                                // 900
    // Fuera de cámara (BANNED 41): probar como Carolina; el montaje salta del 900 al cuadro con «Probando como …».
    { escribir: { en: '#sim-buscar-persona', texto: '{@carolina}' }, espera: CANDIDATA, pausa: 300 },
    { tramo: 'como', clic: `${CANDIDATA} >> nth=0`, espera: '.como:has-text("{@carolina-apellido}")', pausa: 2000 },    // 905–959
    { tramo: 'hola', escribir: { en: '#sim-texto', texto: { es: 'hola', en: 'hello' } }, pausa: 600 },                  // 960–989
    { tramo: 'enviar', clic: '#btn-sim-enviar', espera: '#sim-chat button.op', pausa: 3200 },                           // 990 → 1020–1139
    { tramo: 'horarios', clic: HORARIOS_BOT, espera: '#sim-chat .bot:has-text("8:00")', pausa: 5500 },                  // 1140 → 1155–1319

    // ── 2. La automatización de bienvenida (P10). Al salir del editor no hay cambios sin guardar («Probar» no toca el flujo).
    { tramo: 'autos', ir: '/servir/comunicaciones/automatizaciones', espera: '#auto-abrir-{@auto}', pausa: 4200 },      // 1680–1799
    { tramo: 'abrir', clic: '#auto-abrir-{@auto}', espera: 'app-wa-preview', pausa: 4500 },                             // 1800 → 1803–1919
    { tramo: 'envios', clic: '#auto-tab-actividad', espera: '#auto-envios li[data-estado]', pausa: 4500 },              // 1920 → 1923–2039
  ],
};
```

**Comprobaciones al grabar:**
1. El simulador dice «Probando como **Carolina Mejía Arango**» (o el nombre que tenga la persona de la `ref`, que se anota) y el saludo
   «¡Hola Carolina! Bienvenido a Kingdom Demo.»; nunca «¡Hola Persona!».
2. El chatbot **no pregunta el idioma** (la demo tiene uno); si lo pregunta, la escena toca «Español» antes de `horarios` y el REVIEW lo
   anota.
3. La respuesta de «Horarios» es el horario completo con «¡Te esperamos!» y debajo «El flujo terminó».
4. La tarjeta de la bienvenida dice «Encendida», «Cuando llega una persona nueva (1 h después)» y «Hoy: N enviados» con N ≥ 3 (si el
   volcado no es de hoy, `capturar.mjs` lo siembra de nuevo); ningún cuadro usado muestra la sección «5 Revisar y encender» ni un
   estimado.
5. La pestaña «Envíos» trae las cuatro personas nuevas con «Leído» o «Entregado».

### 3.4 Selectores, verificados el 2026-10-30 en `frontend-v2/src/app/`

- **Bandeja** (`pages/comunicaciones/`): `#bandeja-lista .item[data-id]` (`bandeja.page.ts`); `#btn-tomar`, `#hilo-estado[data-estado]`,
  `#compositor`, `#respuestas-sugeridas button.sug[data-atajo]`, `#btn-enviar`, **`#btn-panel`** (el ícono de la persona en la cabecera
  del hilo), `.hilo .msg.sale` (`bandeja-hilo.component.ts`); el panel `#bandeja-panel` (superpuesto con menos de 840 px), `#panel-sin-ficha`,
  **`#btn-panel-crear-ficha`**, `#btn-panel-vincular`, **`#panel-ficha`**, `#btn-panel-ver-ficha` (`bandeja-panel.component.ts`, que solo
  ofrece los botones si `c.puede.escribir`: por eso la escena toma la conversación primero). **Crear ficha**
  (`bandeja-crear-ficha.component.ts`): `#ficha-nombres`, `#ficha-apellidos`, `#ficha-genero` (opcional), **`#ficha-forma`** (obligatoria),
  **`#btn-ficha-crear`**, `#ficha-duplicados` y **`#btn-ficha-forzar`** («Crear de todos modos»).
- **Chatbot** (`chatbot-editor.page.ts`): la ruta `/servir/comunicaciones/chatbot/:id`; el lienzo es la vista por defecto (`vista` =
  `'lienzo'`) y, desde 1100 px, el panel de la derecha muestra las palabras (`#panel-flujo`); **`#btn-probar`**, `#vista-lienzo`,
  `[data-nodo]`. **Simulador** (`chatbot-simulador.component.ts`): `#sim-titulo`, **`#sim-buscar-persona`**, `.candidatos button`, `.como`
  («Probando como {nombre}»), **`#sim-texto`**, **`#btn-sim-enviar`**, **`#sim-chat`** con `.yo`, `.bot`, `.nota` y los botones
  **`button.op`**.
- **Automatizaciones**: `#auto-lista li.tarjeta[data-id]`, **`#auto-abrir-{id}`**, `#auto-hoy-{id}` (`automatizaciones.page.ts`); en la
  automatización (`automatizacion.page.ts`), `#auto-banda`, las pestañas **`#auto-tab-config`**, **`#auto-tab-actividad`** («Envíos» en una
  de suceso), `#auto-tab-historial`, la vista previa `app-wa-preview` dentro de `aside.lado` (solo en la pestaña «Configuración») y la
  sección `#auto-p5` (nunca en cuadro); los envíos (`auto-actividad.component.ts`): **`#auto-envios li[data-estado]`** y sus filtros
  `#auto-envios-{todos|enviado|…}`.
- **Campaña** (`campana.page.ts`; la ruta `/servir/comunicaciones/campanas/:id` acepta `nueva`): **`#camp-plantilla`** (las opciones dicen
  «{nombre} · {categoría}»), `#camp-p1`, `#camp-p2`, `#camp-fuente-segmento`, `#camp-p6` y `#btn-camp-calcular` (nunca en cuadro), la vista
  previa `app-wa-preview` en `aside.lado` (en el celular, **arriba** del formulario: `.lado { order: -1 }` con menos de 960 px). **Editor de
  públicos** (`components/segmento-editor/segmento-editor.component.ts`, `idBase="camp-publico"`): `#camp-publico`, **`#camp-publico-uno`**
  («Un público»), **`#camp-publico-agregar`** («Agregar filtro»), los chips `[data-chip="red"]`, `.resumen`, la cifra `.cifra` (con
  `[data-cargando]` mientras pide). **La lista de filtros** (`segmento-filtro.component.ts`): **`#po-lista-filtros [data-filtro="red"]`**
  («red» está en `TIPOS_DE_MEMBRESIA` y Campañas solo oculta `bienvenida` y `cuenta`). **El editor de la red**
  (`pages/membresia/filtro-editor.component.ts`): **`#editor-filtro[data-tipo="red"]`**, cada red `mat-checkbox[data-opcion="{id}"]`,
  **`#btn-aplicar-filtro`**.
- **SQL:** `com_conversaciones` (`wa_id`, `estado`, `ultimo_entrante_at`, `id_persona`), `com_mensajes` (`direccion`, `texto`,
  `id_conversacion`), `com_flujos` y `com_automatizaciones` (por `lib/escenas-comunicaciones.mjs` → `REF`), `com_auto_disparos`
  (`id_automatizacion`, `estado`), `mem_personas` (`id_sede`, `nombres`, `apellidos`, `whatsapp_e164`), `mem_formas_llegada` (`id_sede`,
  `activa`, `orden`, `nombre`), `mem_redes` (`id_sede`, `nombre`); todas las usa ya `tools/ayuda/semillas/comunicaciones.php`.

### 3.5 El proyecto

`recorrido-comunicaciones/` con `BRIEF.md` (`tipo: comercial`, `subtipo: clip-del-sitio`, `recorrido: comunicaciones`, `aspect: 16:9`),
`frame.md` (= `identidad/frame-comercial.md`), `hyperframes.json` y `package.json` copiados del clip con dos scripts: `"kit"` y `"musica"`
(§0.1). `assets/grabaciones/{clip,celular,escritorio}/`, `assets/audio/` (toque-b y toque-c), `assets/musica/product-launch-recorrido.wav`,
`_gen/` (§3.1). Composiciones: `fondo`, `frase-1` … `frase-8`, `ceja` (con sus dos lugares); en la raíz, `#escena` con las dos ventanas, los
tramos de video, las cámaras (`#camK`, `#camM`, `#camC`, `#camE1`, `#camE2`), las marcas, el cambio de ventana, el dip, la música y los
sonidos. Si `check` avisa `composition_file_too_large`, se deja (como el clip) o cada mundo pasa a una subcomposición del tamaño de su
ventana; la línea de tiempo no cambia.

**Entregables:** `renders/recorrido-comunicaciones-16x9.mp4` (1920×1080, 30 fps, 2910 cuadros, H.264 + AAC 48 kHz, −16 LUFS) para YouTube
y presentaciones, y para la página `/comunicaciones` una versión **1280×720** (H.264 y WebM) con su póster (el cuadro 0) en AVIF y WebP, con
`preload="none"` (lo decide la entrega del sitio, como Academia).

---

## 4. Lo que se revisa en la vista previa

Cuadros a mirar: `npx hyperframes snapshot --at 0,1.5,2.6,4.1,6.1,8.1,10.1,12.6,14.1,16.0,20.1,22.6,24.5,27.9,28.0,28.4,29.5,30.4,31.9,32.0,33.1,34.1,36.5,38.1,38.6,40.5,43.9,44.0,44.5,46.2,47.0,48.6,50.6,51.1,51.6,52.0,52.4,54.5,55.9,56.0,56.5,58.5,60.0,60.2,62.0,64.0,64.2,66.5,67.9,68.0,68.5,70.1,71.6,72.1,72.6,73.1,74.1,74.6,75.5,76.0,77.1,77.6,78.1,79.0,80.5,82.5,84.0,84.5,90.0,91.9,92.0,92.4,96.9`,
y `snapshot --range` de 16 cuadros sobre cada látigo: **27.6–28.1, 43.6–44.1, 55.6–56.1, 67.6–68.1**.

1. **Parte 1 (0–27,9):** lo mismo que el §4 del clip, con la ventana del celular a la derecha y las frases a la izquierda; todo encuadre a
   1,085 (el texto de 14 px a 28 px); en `hilo` (2,6–5,0) y `compositor` (5,4–10,4) la burbuja, «En la cola», el compositor y enviar
   pierden a lo sumo el borde (**ninguna letra** cortada: si una se corta, ese encuadre corre su centro hasta que entre, nunca baja de
   1,085); el aviso «Fuera del horario de envío» y el bloque «Por qué no les llegó» nunca en cuadro; la frase 3 quieta del 12,2 al 27,9; en
   el **24,5** seis nombres con «Leído» y «Allí estaré».
2. **Los látigos** (28,0 · 44,0 · 56,0 · 68,0): ningún cuadro con las dos ventanas vacías ni con una ventana a medio camino quieta; a la
   izquierda al escritorio, a la derecha de vuelta; la frase anterior ya no está en el golpe y la nueva empieza en el +2; la ceja cambia de
   lugar con blur, nunca se desliza.
3. **El chatbot (28–44):** el lienzo con el menú y sus salidas en el 28,4; el toque de «Probar» en el 30,0; en el 30,4 se leen «Probar el
   flujo», «Es una prueba: no se envía nada…» y «Probando como Carolina…» (BANNED 39); «hola» enviado en el 33,1; el saludo y el menú en el
   34,1; «Horarios» en el 38,0 y **el horario entero en el 38,6**, legible (≥ 31 px) en el 40,5; texto ≥ 28 px en todo el plano.
4. **La ficha (44–56):** la conversación de Mariana con su respuesta en el 44,5; el panel en el 46,2; el formulario con «Mariana» y
   «Ospina» en el 48,6; la forma elegida en el 51,1; **«Mariana Ospina» en el panel en el 52,0** con el punch terminado en el 52,3; la
   cabecera sin «Sin ficha» en el 54,5.
5. **La bienvenida (56–68):** las tarjetas con «Encendida», «Cuando llega una persona nueva (1 h después)» y «Hoy: N enviados» en el 56,5;
   la tarjeta en D⁺ en el 58,5; la vista previa del mensaje legible en el 60,2–64,0; **ningún cuadro con la sección 5 ni un estimado**; los
   cuatro nombres con «Leído»/«Entregado» en el 64,2 y en D⁺ en el 66,5.
6. **La campaña (68–92):** «A quién va» con la cifra de toda la iglesia en el 68,5; cada toque en su golpe (70,0 · 71,0 · 72,0 · 73,0 ·
   74,0); **«Red: Red Timoteo» y la cifra en el 74,6**, con «Datos de ejemplo» a la vista; la cámara quieta mientras la app sube
   (76,0–76,9); la vista previa con «Allí estaré» en el 78,1–82,5; **nunca «Calcular», cupo, créditos ni costo** (BANNED 38); la frase del
   sitio entera en el 84,5 con *nadie* dorada y la ventana a 0,92 (la burbuja ≥ 28 px); nada se mueve del 85,0 al 91,8 salvo el halo; dip
   91,9; **92,0 el primer cuadro del cierre** sin noche vacía.
7. **La música (oída, no solo medida):** la costura del **32,0** no se oye (se escucha 28–36 con audífonos dos veces; si se oye, se prueba
   el corte a 20 ms y a 50 ms del golpe antes de tocar el lugar); el último acorde se apaga debajo del cierre sin cortarse; las campanas se
   oyen en el 92,38. `npx hyperframes beats assets/musica/product-launch-recorrido.wav`: la grilla de 0,5 s sigue sin un pulso doble ni uno
   perdido entre el 31,0 y el 33,0.
8. **Sonido (medido):** cada `toque` y cada `aparicion` un cuadro después de su imagen; los golpes de `hyperframes audio` sobre el render
   en los toques de §1.7; **−16 LUFS** integrada (±1), pico real ≤ −1 dBTP; ningún par de sonidos encimado salvo 1800 + 1803, 1920 + 1923 y
   2340 + 2343.
9. **Textos:** ninguna palabra que no esté en la app, en las ocho frases o en el cierre; las frases en sus líneas fijadas; «Datos de
   ejemplo» en cada ventana con nombres o cifras; `npx hyperframes check` en 0 errores.
10. **La historia sin sonido** (así se ve en el sitio hasta que se toca el botón): alguien nuevo escribe → el equipo la toma y le responde
    → el reporte dice quién leyó y quién va → el chatbot contesta lo mismo a cualquier hora → la conversación de Mariana se vuelve su ficha
    → la bienvenida sale sola a cada persona nueva → se arma un aviso para una red con su vista previa → Kingdom.

---

## 5. Riesgos y lo que se decide al grabar

- **La ventana de 24 horas de Mariana.** La escena de celular le responde fuera de cámara; la `ref` `mariana` exige que haya escrito hace
  menos de 20 horas (el volcado se siembra el mismo día). Sin ventana, el compositor ofrece «Enviar plantilla» y la escena se detiene: se
  vuelve a sembrar.
- **Fichas parecidas.** La `ref` `nueva` descarta lo obvio (mismo número o mismo nombre); la regla de Membresía también compara el nombre
  sin tildes. Si aparecen, la escena sigue con «Crear de todos modos» y el plano lo muestra (comprobación 2 de §3.2): es lo que haría
  alguien del equipo.
- **El escritorio se lee solo de cerca** (D = 1,8 deja ver 711 × 375 px CSS): el lienzo, el simulador (352 px de ancho a la derecha), las
  tarjetas, la vista previa y la lista se encuadran con la grabación y se anotan en el REVIEW. Si el lienzo a 1280 px no deja ver el menú y
  sus salidas en un D, se encuadra el paso «Botones» solo (sus tres salidas son lo que importa).
- **El toque «fuera de cuadro» del 1920** (y los cortes del 1803 y el 1923, con la cámara fijada en el corte): se revisan cuadro a cuadro
  alrededor de cada uno. Si el cambio de encuadre del 1923 se lee como un salto, la válvula es esta: el mensaje se lee 1803–1859 (1,9 s), en
  el 1860 la cámara va a **D sobre la banda y las pestañas** y el toque del 1920 **se dibuja** sobre «Envíos»; la lista entra debajo, ya en
  cuadro, y el 1980 sigue igual. Se anota en el REVIEW.
- **La vista previa de la campaña en el celular está arriba del formulario.** Al elegir la plantilla puede crecer fuera de la vista (el
  navegador ancla el campo); el tramo `preview` sube a ella y el montaje lo usa en el 2400 con su `desliz`. Si ya está a la vista, el 2400
  queda quieto y sin sonido.
- **La cifra de la red Timoteo** depende de la semilla del día; se espera 139 con WhatsApp (los destinatarios de la invitación) y ninguna
  frase lo nombra. Si la cifra tarda en llegar (`data-cargando`), el corte del 2235 se toma del primer cuadro con los dígitos corriendo.
- **Los envíos de la bienvenida** («Hoy: N enviados») son de la hora de la semilla; con un volcado de otro día dirían «Hoy: 0»: la `ref`
  `envios` no lo detecta (cuenta todos), así que la comprobación 4 de §3.3 lo mira en la grabación.
- **La costura de la música** está medida (Academia §0.1), pero nadie la ha oído: es lo primero que se escucha en la vista previa (§4.7).
- **Densidad:** la parte 2 tiene un toque por pulso en 70–74 (cinco toques en 4 s) y en 50–51,5 (tres en 1,5 s). Si en la vista previa va
  atropellado, la válvula es quitar el sonido de «Agregar filtro» (2130) y de la forma (1530): la marca se queda.
- **El README pide 60–75 s para el recorrido**; este dura 97 por decisión del dueño (~100 s), como Academia. Se anota en
  `KingdomApp/docs/videos/README.md` al publicar.
- **Idiomas (en, pt después):** las dos escenas con `--idioma en` graban la interfaz en inglés («hello», «Service times»,
  «sunday_invitation», «Timothy Network» ya están en los selectores y las `refs`); Carolina saluda con su nombre igual. Las frases se
  traducen y los saltos se vuelven a fijar; el cierre lleva `idioma`.
