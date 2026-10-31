# SPEC · Recorrido de Mi iglesia — «Se enteró toda la iglesia… y encontró su lugar» (16:9)

2026-10-30 · Contrato de construcción de la historia de [STORY.md](STORY.md). La parte 1 es el clip publicado
([clip-sitio-mi-iglesia](../clip-sitio-mi-iglesia/): su [SPEC](../clip-sitio-mi-iglesia/SPEC.md), su [REVIEW](../clip-sitio-mi-iglesia/REVIEW.md),
su `index.html` y su generador `_gen/`), llevado a 16:9 sin reabrirlo; la parte 2 es nueva. Mismo método que
[recorrido-academia](../recorrido-academia/SPEC.md): cada adjetivo es un número, los valores por defecto están prohibidos con nombre y los
planos van cuadro por cuadro. Se construye desde aquí, se revisa contra esto y se cambia aquí cuando la vista previa cambie la película.
«Igual que el clip» quiere decir: generado con `clip-sitio-mi-iglesia/_gen/` (copiado) con los cambios de §2.1.

```text
GOAL:    Un pastor que no conoce Kingdom termina pensando «con esto cada miembro encuentra su grupo, alguien lo acompaña, crece entre
         domingo y domingo, y yo sé a quién le llegó lo que anunciamos» y toca «Prueba gratis 30 días».
OUTPUT:  HyperFrames 0.8.221 · una composición 1920×1080 (16:9) · 30 fps. (La 9:16 queda para después; no se especifica aquí.)
TIME:    97,0 s = 2910 cuadros: cuerpo 0–92,0 (cuadros 0–2759) + cierre del Comercial 92,0–97,0 (2760–2909). 120 BPM = 15 cuadros
         por pulso en todo el video (la costura de la música conserva la grilla, §0).
LOOK:    la noche del sitio (#060D1F) con el halo y la retícula de puntos del kit; tinta #EAF0FF; un solo acento, el dorado #E8B95A, en
         tres lugares (la ceja «MI IGLESIA», la palabra «bolsillo» y el botón del cierre). Fraunces 560 84 px / −0,02 em para las frases;
         Inter para la ceja y «Datos de ejemplo». El medio: la app REAL de Kingdom Demo en dos ventanas del kit sobre la noche: el celular
         (`.k-ventana-16x9`, 720×900) y el escritorio (`.k-ventana-escritorio`, 1440×760); nunca un aparato dibujado.
OBJECTS: las dos ventanas; cuatro mundos de celular (Gabriela en el clip, Gabriela en sus comunidades, Gabriela acompañada y en su
         objetivo, Lucía en su bienvenida) y dos de escritorio (el pastor en Contactos, el pastor en el tablero y la novedad); el punto
         de toque; las once frases; la ceja; la píldora «Datos de ejemplo»; el cierre del Comercial. Nada más existe en el cuadro.
MOTION:  curvas por papel (§1.6); un movimiento de cámara por compás (14 cuadros, power2.inOut), quieto después; cada corte y cada
         entrada en un pulso; cada cambio de mundo en un golpe (840 · 960 · 1320 · 1560 · 2040 · 2280 · 2760).
SHOTS:   doce planos (§2).
BANNED:  §1.8.
QA:      §4.
```

---

## 0. La música: la edición y el reloj

### 0.1 La edición (una sola costura: la misma de Academia, medida otra vez)

«Product Launch» (The_Mountain, `_identidad/musica/product-launch-the-mountain.mp3`, 86,05 s, 120 BPM, compases de 2 s desde el 2,05;
`kit.json` → `musica.biblioteca.product-launch`) se alarga **repitiendo 24 s (12 compases): del 22,05 al 46,05 de la pista**. Se toca del
14,05 al 46,04 (el tramo del clip y dos compases más), se salta al 22,01 y se sigue hasta el final natural de la pista. Es **exactamente la
edición de [recorrido-academia §0.1](../recorrido-academia/SPEC.md)**: el clip de Mi iglesia usa el mismo tramo de la pista (14,05 → 42,05)
que el de Academia, así que su parte 1 suena idéntica y la parte 2 recibe la misma segunda subida, el mismo clímax y la misma salida. Por qué
ahí (la similitud de compases 0,61 y 0,65 en los bordes, el cruce de 30 ms que termina 5 ms antes del ataque del 22,05, la envolvente a
±0,4 dB y las alternativas descartadas) está medido y escrito en Academia; aquí no se repite.

```bash
# en recorrido-mi-iglesia/ (script "musica" del package.json): 31,99 s + 64,037 s − 0,03 s de cruce = 95,997 s
ffmpeg -hide_banner -y -i ../_identidad/musica/product-launch-the-mountain.mp3 -filter_complex \
  "[0:a]atrim=start=14.05:end=46.04,asetpts=PTS-STARTPTS[a];[0:a]atrim=start=22.01,asetpts=PTS-STARTPTS[b];[a][b]acrossfade=d=0.03:c1=tri:c2=tri[m]" \
  -map "[m]" -ar 44100 -c:a pcm_s16le assets/musica/product-launch-recorrido.wav
```

- **Si Academia ya la armó**, se copia `recorrido-academia/assets/musica/product-launch-recorrido.wav` (mismo comando, mismo archivo).
- **Comprobación al armarla** (hecha el 2026-10-30 con este comando): `ffprobe` da **95,997 s**. El cruce ocupa 31,960–31,990 del video.
  Mapa exacto: **video = pista − 14,05** hasta el 31,99 y **video = pista + 9,95** desde el 31,99.
- **Licencia:** la de Pixabay permite modificar la pista (`_identidad/licencias.md`); la pista editada no se redistribuye sola. Tiene
  Content ID: en YouTube puede llegar un reclamo de monetización, que se disputa con la licencia.

### 0.2 El reloj del video

| Video | Pista | Tramo de la pista (`kit.json` → `mapa`) | Lo que le toca al video |
|---|---|---|---|
| 0–4 | 14,05–18,05 | entrada sin bajo | El gancho del clip |
| 4–12 | 18,05–26,05 | primera subida (bajo en 18,05, pico en 20) | «Amén» → el evento |
| 12–20 | 26,05–34,05 | respiro | La inscripción con su familia |
| 20–28 | 34,05–42,05 | segunda subida (golpes 36 · 38 · 42,05) | «¡Quedaste inscrito!» → la boleta en grande |
| **28**–32 | 42,05–46,05 | el golpe más fuerte y su compás | «Cerrar» → Comunidades → Explorar |
| **32**–36 | 22,05–26,05 (repetido) | final de la primera subida | El iris a Jóvenes; los líderes |
| 36–44 | 26,05–34,05 (repetido) | respiro | Unirme, conectar, el mensaje, «Enviar» |
| **44**–60 | 34,05–50,05 (repetido hasta 46,05) | segunda subida otra vez (golpe más fuerte en el **52,0**) | El pastor toma el contacto; «te acompañará»; Mis objetivos |
| **60**–76 | 50,05–66,05 | clímax brillante (dos frases de 8 s) | «Lo hice»; el tablero y quién respondió |
| **76**–92 | 66,05–82,05 | salida tranquila | La bienvenida de quien llega; la frase del sitio |
| **92**–96 | 82,05–86,05 | el último acorde, que se apaga solo | El cierre del Comercial |

### 0.3 La grilla, pulso por pulso (medida para este video)

**Cuadros 0–839:** la de `clip-sitio-mi-iglesia/SPEC.md` §0, sin cambios.

**Cuadros 840–2760** (cuadro · fuerza). Medida el 2026-10-30 sobre la pista editada: hasta el **1875** la fuerza es la de
`product-launch-the-mountain.pulsos.json` en el instante de la pista (el pulso más cercano, a menos de 45 ms). **Desde el 1890 esa grilla
marca contratiempos**: sus pulsos pasan a 52,975, 53,415, 53,865… y desde el 55,295 quedan en x,295 / x,795 de la pista, es decir **un cuarto
de segundo (media negra) después** de las negras de 2,05 + 0,5·n. Se resolvió midiendo:

- **El bombo (30–120 Hz) no se corrió:** el pico de su energía cae a **+0,01–0,03 s** de la grilla de 2,05 + 0,5·n en la primera subida, en la
  segunda y **en el clímax** (perfil de energía por fase dentro del pulso, promediado por tramo).
- **Lo que se mueve al contratiempo son los platillos y el cuerpo** (150–400 Hz y 5–11 kHz): su pico cae a **+0,23–0,26 s** en **todos** los
  tramos, también donde la grilla del archivo es correcta. En el clímax esos golpes son los más fuertes (los 14 picos de flujo mayores entre el
  60 y el 76 están a +0,20–0,21 s de la negra, salvo tres) y el detector se pegó a ellos.
- **Conclusión:** las negras siguen en 2,05 + 0,5·n hasta el final; **nada del video cae en un contratiempo**. En la salida (76–92) el bajo
  pulsa al contratiempo y no hay bombo, pero los platillos guardan la misma relación que en el resto: el compás no se movió.

Desde el 1890 la fuerza que va abajo en *cursiva* es el **flujo espectral** en la negra (FFT de 1024 muestras a 22 050 Hz, salto de 256, flujo
positivo del logaritmo de la magnitud, máximo en ±35 ms, normalizado al percentil 99,5 de la pista entera y topado en 1,00): otra escala,
que solo sirve para comparar los pulsos entre sí.

| Compás | Cuadros | Pulsos (cuadro · fuerza) | Lo que le toca |
|---|---|---|---|
| 15 | 840–899 | **840 ·1,00** · 855 ·0,68 · 870 ·0,51 · 885 ·0,52 | **«Cerrar»** (corte a «Mis boletas»); 870 «Comunidades»; 885 la pantalla vacía |
| 16 | 900–959 | **900 ·0,84** · 915 ·0,82 · 930 ·0,75 · 945 ·0,66 | 900 «Explorar comunidades»; 915 Explorar; 930 la app baja a Jóvenes |
| 17 | 960–1019 | **960 ·0,92** (costura) · 975 ·0,77 · 990 ·0,58 · 1005 ·*0,48* | **Toque en Jóvenes → iris** |
| 18 | 1020–1079 | 1020 ·0,77 · 1035 ·0,74 · 1050 ·0,60 · 1065 ·0,58 | 1020 la cámara a «Conectar» y «Líderes» |
| 19 | 1080–1139 | **1080 ·0,76** · 1095 ·0,64 · 1110 ·0,50 · 1125 ·0,46 | **«Unirme»** y el confeti |
| 20 | 1140–1199 | **1140 ·0,75** · 1155 ·0,61 · 1170 ·0,49 · 1185 ·0,49 | 1140 «Conectar con un líder»; 1155 el diálogo; 1170 se escribe |
| 21 | 1200–1259 | 1200 ·0,67 · 1215 ·0,67 · 1230 ·0,54 · 1245 ·0,50 | El mensaje se termina de escribir (1246) |
| 22 | 1260–1319 | **1260 ·0,63** · 1275 ·0,56 · 1290 ·0,61 · 1305 ·0,68 | 1260 «Enviar»; 1275 «Pediste conectar con un líder» |
| 23 | 1320–1379 | **1320 ·0,93** · 1335 ·0,69 · 1350 ·0,52 · 1365 ·0,49 | **Látigo al escritorio: Contactos**; 1350 la cámara a «Tomar» |
| 24 | 1380–1439 | **1380 ·0,90** · 1395 ·0,89 · 1410 ·0,76 · 1425 ·0,68 | 1380 «Tomar»; 1383 el detalle con el confeti |
| 25 | 1440–1499 | **1440 ·0,96** · 1455 ·0,77 · 1470 ·0,59 · 1485 ·0,60 | 1440 la cámara a su mensaje y los botones |
| 26 | 1500–1559 | 1500 ·0,88 · 1515 ·0,74 · 1530 ·0,62 · 1545 ·0,60 | Quieto |
| 27 | 1560–1619 | **1560 ·1,00** · 1575 ·0,68 · 1590 ·0,51 · 1605 ·0,52 | **Látigo de vuelta: «Andrés … te acompañará»**; 1575 el punch |
| 28 | 1620–1679 | 1620 ·0,84 · 1635 ·0,82 · 1650 ·0,75 · 1665 ·0,66 | 1620 la cámara a «Líderes» y la barra |
| 29 | 1680–1739 | **1680 ·0,98** · 1695 ·0,74 · 1710 ·0,60 · 1725 ·0,57 | 1680 «Objetivos»; 1695 Mis objetivos |
| 30 | 1740–1799 | 1740 ·0,79 · 1755 ·0,75 · 1770 ·0,69 · 1785 ·0,67 | 1740 la tarjeta; 1755 el detalle con «Hoy» |
| 31 | 1800–1859 | **1800 ·0,93** · 1815 ·0,84 · 1830 ·0,63 · 1845 ·0,49 | **1800 «Lo hice»** (empieza el clímax) |
| 32 | 1860–1919 | 1860 ·0,81 · 1875 ·0,95 · 1890 ·*0,58* · 1905 ·*0,56* | 1860 la cámara al anillo |
| 33 | 1920–1979 | **1920 ·*1,00*** · 1935 ·*0,89* · 1950 ·*0,64* · 1965 ·*0,74* | 1920 la app baja a «Todos los pasos» |
| 34 | 1980–2039 | 1980 ·*0,55* · 1995 ·*1,00* · 2010 ·*0,73* · 2025 ·*0,56* | Quieto |
| 35 | 2040–2099 | **2040 ·*0,76*** · 2055 ·*0,57* · 2070 ·*0,44* · 2085 ·*0,54* | **Látigo al escritorio: el tablero** |
| 36 | 2100–2159 | **2100 ·*0,91*** · 2115 ·*0,76* · 2130 ·*0,53* · 2145 ·*0,52* | 2100 la app baja a «Publicaciones» |
| 37 | 2160–2219 | **2160 ·*1,00*** · **2175 ·*1,00*** · 2190 ·*0,66* · 2205 ·*0,64* | 2160 «Inscripciones abiertas»; 2175 «Quién reaccionó» |
| 38 | 2220–2279 | 2220 ·*0,47* · **2235 ·*1,00*** · 2250 ·*0,78* · 2265 ·*0,41* | 2220 🙌; **2235 «Gabriela Hinestroza Perea 🙌»** |
| 39 | 2280–2339 | **2280 ·*0,48*** · 2295 ·*0,36* · 2310 ·*0,32* · 2325 ·*0,36* | **Látigo de vuelta: la bienvenida de Lucía** (la salida empieza aquí aunque el pulso es suave) |
| 40 | 2340–2399 | 2340 ·*0,43* · 2355 ·*0,41* · 2370 ·*0,37* · 2385 ·*0,39* | La coreografía de la portada termina |
| 41 | 2400–2459 | **2400 ·*0,74*** · 2415 ·*0,43* · 2430 ·*0,40* · 2445 ·*0,33* | **«Empezar mis primeros pasos»** |
| 42 | 2460–2519 | 2460 ·*0,39* · 2475 ·*0,52* · 2490 ·*0,32* · 2505 ·*0,38* | 2460 la cámara al camino |
| 43 | 2520–2579 | **2520 ·*0,63*** · 2535 ·*0,44* · 2550 ·*0,40* · 2565 ·*0,37* | **La frase del sitio**; la ventana a un lado |
| 44 | 2580–2639 | 2580 ·*0,70* · 2595 ·*0,42* · 2610 ·*0,33* · 2625 ·*0,35* | Quieto |
| 45 | 2640–2699 | 2640 ·*0,69* · 2655 ·*0,34* · 2670 ·*0,36* · 2685 ·*0,32* | Quieto |
| 46 | 2700–2759 | 2700 ·*0,25* · 2715 ·0,49 · 2730 ·0,58 · 2745 ·0,60 | La subida (desde 2716); el dip 2757–2759 |
| — | **2760** | el último acorde (pista 82,05; 0,57) | **El cierre del Comercial** |

(1383 no es un pulso: es la respuesta de la app al toque del 1380, como el 1803 de Academia.)

### 0.4 Nivel de la música

`<audio id="musica" src="assets/musica/product-launch-recorrido.wav" data-start="0" data-duration="96">`, **sin `data-volume`**: **0,75** en el
carril de volumen de principio a fin (el nivel del clip de Mi iglesia, que dio −17,1 LUFS con sus sonidos). **Sin fundido**: la pista
termina sola debajo del cierre (§0.2). Si en la vista previa las campanas del 92,38 quedan tapadas, el carril baja a 0,5 entre 92,0 y 92,3
(y se anota en el REVIEW); nada más se toca.

---

## 1. Los números del estilo

### 1.1 Paleta

La de `clip-sitio-mi-iglesia/SPEC.md` §1.1, tal cual (fondo `#060D1F`, halo, puntos que nunca se mueven, tinta `#EAF0FF`, dorado `#E8B95A`
solo en la ceja, «bolsillo» y el botón del cierre; anillo `rgba(234,240,255,.12)`; placa de «Datos de ejemplo» `rgba(6,13,31,.72)`; el azul
de marca solo dentro del cierre). Cambia: el **dip** va en los cuadros **2757–2759** sobre las dos ventanas; el **halo** se asienta
1,08 → 1,00 (`sine.out`, 90 cuadros) en 0 · 180 · 720 · 960 · 1320 · 1560 · 2040 · 2280. Los colores de la app (el morado de Jóvenes, el
semáforo verde de la bandeja, el azul del tema, el blanco de la boleta) viven dentro de la grabación y no se tocan ni se repiten fuera.

### 1.2 Tipografía (16:9)

| Pieza | Clase del kit | Familia · peso | Tamaño | Reglas |
|---|---|---|---|---|
| Frase | `.k-titular` con `font-size: 84px` | Fraunces 560; `<em>` itálica 500 dorada | **84 px** · interlínea 1,04 (87,4 px) · −0,02 em | Máx. 2 líneas en el escenario del celular, **1 línea** en el del escritorio; saltos fijados a mano; izquierda; `text-wrap: balance` apagado; sin sombra |
| Ceja | `.k-ceja` | Inter 700, MAYÚSCULAS, +0,10 em | **28 px** | Dos palabras: «MI IGLESIA» |
| Datos de ejemplo | `.k-datos-ejemplo` (la de 16:9) | Inter 600 | **22 px**, píldora de 40 px | En cada ventana, abajo a la izquierda, a 24 px |
| Texto de la app | (grabación) | la de la app | ≥ **28 px** en todo encuadre de lectura | §1.5 |

Saltos fijados: «¿Se enteró / toda la iglesia?» · «Llega a cada celular.» (una línea) · «Y se inscribe / con su familia» · «Su boleta, /
también sin señal.» · «Encuentra / su comunidad.» · «Su mensaje llega a los líderes.» (una línea, escritorio) · «Y un líder / la
acompaña.» · «Crece / paso a paso.» · «Y sabes quién respondió.» (una línea, escritorio) · «A quien llega, / una bienvenida.» · «Tu iglesia,
en el *bolsillo* / de cada miembro». La más ancha del celular es «Tu iglesia, en el bolsillo» (826 px a 80 px en el clip → ≈ 868 px a 84):
entra en la columna de 936 px. La más ancha del escritorio es «Su mensaje llega a los líderes.» (≈ 1 300 px desde x 240: termina antes del
1 824 del margen seguro). Si `check` marca desborde, la columna crece hacia la ventana (nunca se baja la letra de 84).

### 1.3 Radios y sombras

Los del kit: `.k-ventana` radio **28** (celular) y **20** (`.k-ventana-escritorio`), anillo y sombra de `kit.css`, `overflow: hidden`. Frases
y ceja sin sombra ni brillo.

### 1.4 Disposición: dos escenarios (la de Academia, sin cambios)

| | Escenario del celular | Escenario del escritorio |
|---|---|---|
| Ventana | `#ventana-cel.k-ventana.k-ventana-16x9`: **x 1104 · y 90 · 720 × 900** | `#ventana-esc.k-ventana.k-ventana-escritorio`: **x 240 · y 260 · 1440 × 760** |
| Ceja | x 120 · y 412 | x 240 · y 92 |
| Frase | x 120 · y 460 · ancho 936 · hasta 2 líneas → termina en 635 | x 240 · y 132 · una línea → termina en 219 |
| Datos de ejemplo | dentro de la ventana, abajo a la izquierda, a 24 px | ídem |
| Final (desde el 2524) | la ventana a escala **0,92** con origen «100% 50%» y x **+24** | — |

- **Las dos ventanas viven en una sola tira horizontal** (`#escena`): la del celular en x 1104 y la del escritorio en x 240 + 1920 = **2160**.
  `#escena` en x 0 muestra el celular; en x **−1920**, el escritorio.
- **Dentro de la ventana del celular no hay tira vertical** (no hay látigo vertical en este video): sus cuatro mundos son capas apiladas que
  se cambian con `autoAlpha` en el cuadro de su corte (840, en cuadro) o mientras la ventana está fuera (1320–1559 y 2040–2279).
- **Las frases y la ceja no viajan con el látigo:** salen con blur antes y entran después, en el lugar de su escenario (§1.6).
- El 90 % seguro para títulos (96 px a los lados, 54 arriba y abajo) se cumple en los dos escenarios.

`window.KD` (la de Academia; las variables `--f-*` se derivan de aquí):

```js
window.KD = {
  fps: 30,
  cel: { x: 1104, y: 90, w: 720, h: 900, hVis: 900 },          // --f-k = 720/1170 = 0.615385; --f-grab-alto = 1558.15px
  esc: { x: 240, y: 260, w: 1440, h: 760, hVis: 760 },         // K = 1440/1920 = 0.75; alto de la grabación ajustada = 810
  grabCel: { w: 1170, h: 2532, cssW: 390, cssH: 844 },         // celular 390×844 a 3×
  grabEsc: { w: 1920, h: 1080, cssW: 1280 },                   // escritorio 1280×720 a 1,5× (modo video de capturar.mjs)
  latigoH: 1920,                                               // la tira horizontal entre escenarios
  cambio: { escala: 0.92, x: 24, origen: '100% 50%' },         // la ventana del celular se hace a un lado (2524–2538)
};
```

### 1.5 La cámara: escalas de lectura

`enc(s, cx, cy)` del clip, una por ventana (con su `W`, `HV`, `PPC = W / cssW` y `VH`): pone el punto (cx, cy) en px CSS en el centro de lo
visible con la escala s, sin salirse de la grabación. **Una escala es de lectura si el texto de 14 px de la app queda en ≥ 28 px.**

**Celular (`#ventana-cel`, PPC 1,846):**

| Nivel | s | px del cuadro por px CSS | Visible (px CSS) | 14 px → |
|---|---|---|---|---|
| **G** | **1,085** | 2,003 | 359 × 449 | **28,0** |
| ×1,12 | 1,12 | 2,068 | 348 × 435 | 29,0 |
| ×1,18 | 1,18 | 2,178 | 330 × 413 | 30,5 |
| M | 1,40 | 2,585 | 279 × 348 | 36,2 |
| C | 1,80 | 3,323 | 217 × 271 | 46,5 |

G = 1,085 deja 15 px CSS fuera a cada lado (las tarjetas de la app van de x 16 a 374): es el plano general de todo el video. **Ningún encuadre
de lectura del celular baja de 1,085.**

**Las barras fijas de la app** (arriba 0–56 y abajo 769–844 px CSS) **no pueden estar en cuadro en un salto compensado** (`comp()` del clip):
la cámara deshace el salto del contenido, pero las barras no saltaron y se verían brincar. En 4:5 el clip lo cumplía con 439 px CSS de alto
visible; en 16:9 se ven 10 px más (449 a G, 435 a ×1,12, 413 a ×1,18), así que los encuadres que están en cuadro cuando hay compensación
**suben** hasta que su borde de abajo quede en 768 (§2.1, tabla de cámaras). Fuera de una compensación la barra de abajo puede estar en
cuadro (y debe, cuando se toca: 840–870 y 1620–1680).

**Escritorio (`#ventana-esc`, PPC 1,125):**

| Nivel | s | px del cuadro por px CSS | Visible (px CSS) | 14 px → |
|---|---|---|---|---|
| **D** | **1,80** | 2,025 | 711 × 375 | **28,4** |
| D⁺ | 2,00 | 2,250 | 640 × 338 | 31,5 |

El plano entero del escritorio (s = 1) solo existe durante el látigo. Ningún encuadre de escritorio pasa de 2,0.

### 1.6 Curvas y duraciones (cada tween con su curva por nombre)

| Papel | Curva | Cuadros | Detalle |
|---|---|---|---|
| `entrada-palabra` | `power4.out` | 4 | blur 6 → 0 + opacidad; sin desplazamiento; palabras a 2 cuadros (la frase 1, una por pulso, como el clip) |
| `entrada-linea` | `power4.out` | 6 | la línea entera, blur 8 → 0 (la frase 2 y cada entrada de la ceja) |
| `salida-texto` | `power3.in` | 4–5 | blur 0 → 8 + opacidad; empieza 3 cuadros antes del golpe del cambio |
| `camara` | `power2.inOut` | **14** | un movimiento por compás; después, quieta; nunca mientras la app se desplaza sola |
| `punch` | `power2.inOut` | **9** | 690 (el QR, del clip) y **1575** (la tarjeta «te acompañará») |
| `latigo-h` | `power3.inOut` | **10** | `#escena` 1920 px: **a la izquierda = al escritorio, a la derecha = de vuelta**; termina en el golpe (1310–1320, 1550–1560, 2030–2040, 2270–2280); la ventana que llega aterriza 1,04 → 1,00 (`power3.out`, 10 cuadros, desde su centro) |
| `iris` | `power2.out` | 5 | `clip-path: circle(0 → 1900px)` desde el centro del toque: 180 (del clip) y **960** (la tarjeta de Jóvenes → la comunidad) |
| `corte-toque` | escalón | 0 | el resultado de un toque aparece en el cuadro siguiente al pulso (la espera de la app se corta); la marca se va con el corte, como en el clip (`CORTE`) |
| `ventana-cambio` | `power2.inOut` | 15 | 2524–2538: escala 1 → 0,92, origen «100% 50%», x +24 |
| `halo` | `sine.out` | 90 | §1.1 |
| `dip` | escalón | 3 | `rgba(6,13,31,.40)` sobre las dos ventanas, 2757–2759 |
| marcas de toque | las del clip | — | aparecen 4 cuadros antes, se hunden en el cuadro, se van 6 después (o con el corte); la onda de 450 ms |
| velocidad de la grabación | `data-playback-rate` | — | **1×** en todo; nada se acelera ni se frena (las esperas se cortan) |
| cierre | las del kit | 150 | no se imita en el cuerpo |

`data-motion-blur="on"` y `data-motion-blur-shutter="180"` en la raíz (los látigos se ven con el borrón real). Nunca `filter: blur()` sobre
una grabación.

### 1.7 Sonido

| Capa | Fuente | Nivel | Regla |
|---|---|---|---|
| Música | `assets/musica/product-launch-recorrido.wav` (§0.1) | 0,75 en el carril | §0.4 |
| Sonidos de acción | kit v1.1 (`toque` en tres tomas a/b/c: `identidad/audio/toque.wav` y `assets/audio/toque-b.wav`, `toque-c.wav` del clip), `aparicion`, `desliz`, `subida`, `confirmacion` | `data-volume="1"`; **1,4** en los clave | `data-start = (cuadro de la imagen + 1) / 30 − acento` (toque 0 · aparicion 0 · desliz 0,2 · subida 1,5 · confirmacion 0,1) |
| Sonido de marca | `identidad/audio/sonido-marca.wav` | 1 | **92,38 s** (inicio del cierre + 0,38 de `kit.json`) |
| Mezcla de entrega | — | **−16 LUFS** integrada, pico real ≤ **−1 dBTP** | `npx hyperframes audio` sobre el render; si −16 pasa el pico, se bajan a 1,2 los sonidos de 1,4 antes que dejar la mezcla en −17 (el clip quedó en −17,1: se anota igual) |

**Los eventos de la parte 1 (0–839)** son los 22 de la tabla `SON` de `clip-sitio-mi-iglesia/_gen/gen.py`, sin cambios. **No van** la
`subida` del clip (796–853) ni las campanas del 851, ni el fundido de la música del 852.

**Los eventos de la parte 2** (cuadro de la imagen → `data-start` en s):

| Imagen | Sonido | `data-start` | Nivel | Causa en pantalla |
|---|---|---|---|---|
| 840 | `toque` a | 28,033 | 1 | «Cerrar» en la boleta |
| 870 | `toque` b | 29,033 | 1 | «Comunidades» en la barra |
| 900 | `toque` c | 30,033 | 1 | «Explorar comunidades» |
| 930 | `desliz` | 30,833 | 1 | La app baja hasta Jóvenes |
| 960 | `toque` a | 32,033 | 1 | La tarjeta de Jóvenes (el iris; la costura de la música cae aquí) |
| 1080 | `toque` b | 36,033 | **1,4** | «Unirme» |
| 1082 | `aparicion` | 36,100 | 1 | El confeti de la app |
| 1140 | `toque` c | 38,033 | 1 | «Conectar con un líder» |
| 1155 | `aparicion` | 38,533 | 1 | El diálogo |
| 1260 | `toque` a | 42,033 | 1 | «Enviar» |
| 1275 | `confirmacion` | 42,433 | 1 | «Pediste conectar con un líder» |
| 1320 | `desliz` | 43,833 | **1,4** | Látigo al escritorio |
| 1380 | `toque` b | 46,033 | **1,4** | «Tomar» |
| 1383 | `aparicion` | 46,133 | 1 | El detalle y el confeti de la fila |
| 1560 | `desliz` | 51,833 | 1 | Látigo de vuelta al celular |
| 1575 | `confirmacion` | 52,433 | **1,4** | El punch sobre «Andrés … te acompañará» |
| 1680 | `toque` c | 56,033 | 1 | «Objetivos» en la barra |
| 1740 | `toque` a | 58,033 | 1 | La tarjeta del devocional |
| 1800 | `toque` b | 60,033 | **1,4** | «Lo hice» |
| 1803 | `aparicion` | 60,133 | 1 | «¡Listo! Marcamos … como hecho.» |
| 1920 | `desliz` | 63,833 | 1 | La app baja a «Todos los pasos» |
| 2040 | `desliz` | 67,833 | 1 | Látigo al escritorio |
| 2100 | `desliz` | 69,833 | 1 | La app baja a «Publicaciones» |
| 2160 | `toque` c | 72,033 | 1 | «Inscripciones abiertas» |
| 2175 | `aparicion` | 72,533 | 1 | «Quién reaccionó» |
| 2220 | `toque` a | 74,033 | 1 | 🙌 |
| 2235 | `confirmacion` | 74,433 | **1,4** | «Gabriela Hinestroza Perea 🙌» |
| 2280 | `desliz` | 75,833 | 1 | Látigo de vuelta: la bienvenida |
| 2400 | `toque` b | 80,033 | 1 | «Empezar mis primeros pasos» |
| 2402 | `aparicion` | 80,100 | 1 | El camino de los primeros pasos |
| 2716–2773 | `subida` | **90,533** | 1 | Hacia el cierre (golpe en el 2761) |
| 2771 | marca | 92,38 | 1 | Las campanas del cierre |

Sin tics de tecla (ni en el mensaje). **Dos sonidos de acción nunca se enciman, salvo** un toque y su resultado (1080 + 1082, 1380 + 1383,
1800 + 1803, 2400 + 2402). **Tres `confirmacion`** en la parte 2, una por prueba: el pedido enviado (1275, a 1,0), el líder que la
acompaña (1575) y su nombre en «Quién reaccionó» (2235); las demás respuestas llevan `aparicion`. La `subida` es la única del video.

### 1.8 BANNED: los valores por defecto prohibidos, con nombre

Valen enteros los 20 de `clip-sitio-membresia/SPEC.md` §1.8 y, de `clip-sitio-mi-iglesia/SPEC.md` §1.8, el **21** (la cámara y el
desplazamiento de la app a la vez), el **23** (recrear o «ayudar» lo que hace la app: confeti, anillo, sello, QR), el **25** (marcas de toque
donde la grabación no tocó), el **26** (una notificación dibujada), el **27** (la entrada a la app en cualquier cuadro) y el **28** (el blanco
de la boleta a sangre). **No aplican** el 22 (aquí hay más pruebas y lleva su propia cuenta, §1.7), el 24 (aquí hay cuatro látigos con causa)
ni el 29 en su forma de 4:5 (las frases viven en su columna, §1.4). Además:

30. **Un látigo entre dos momentos de la misma persona en el mismo aparato.** Del clip a Comunidades (840), de la comunidad a Objetivos
    (1680) y de un objetivo a sus pasos (1920) se pasa con el toque o con la app; el látigo horizontal es solo cambio de aparato o de persona.
31. **Un cursor de ratón** en el escritorio. La grabación va sin cursor (`toque: false`) y el toque se marca con la misma marca del celular.
32. **Escribir encima de la app un nombre** («Andrés», «Gabriela», «Lucía») o un número (el alcance, el «57», el «93 %»): todo nombre y
    toda cifra salen de la grabación; ninguna cifra sin «Datos de ejemplo» a la vista.
33. **Que Lucía parezca Gabriela o al revés.** El último plano es de otra persona: su saludo dice su nombre y ninguna frase la llama «ella».
34. **Leer el formulario del mensaje letra por letra con la cámara encima.** El mensaje se escribe a 1× con la cámara quieta en G sobre el
    diálogo entero.
35. **Una transición que no sea de la serie.** Solo corte sobre el toque, iris desde el toque (180, 960), látigo horizontal (1320, 1560, 2040,
    2280) y dip + corte al cierre. Nunca un fundido entre mundos, nunca un zoom a través de un botón.
36. **El escritorio a menos de 1,8** en un encuadre de lectura, o a más de 2,0 en cualquiera.
37. **Cambiar la frase del sitio** («Tu iglesia, en el bolsillo de cada miembro») o el lema y el llamado del cierre.
38. **Un fundido de música** en la costura o al final, o un segundo corte.
39. **Las frases viajando con el látigo.** Salen con blur en su escenario y entran en el otro.
40. **La ventana del escritorio con un marco de navegador** o la del celular con la barra de estado de un teléfono.
41. **Una barra fija de la app en cuadro durante un salto compensado** (§1.5).

---

## 2. Los planos, cuadro por cuadro

### 2.0 Convenciones

- **Grabaciones:** **K** = la del clip (`assets/grabaciones/clip/grabacion.mp4`, 1170×2532, 52,2 s; sus cuadros como en el REVIEW del clip,
  «grab.»); **C** = la nueva de celular (`assets/grabaciones/celular/`, escena §3.2); **E** = la nueva de escritorio
  (`assets/grabaciones/escritorio/`, escena §3.3). «C·cerrar» = el tramo `cerrar` de C en su `pasos.json`; «+N» = N cuadros después de la
  acción de ese paso.
- **Niveles:** G, ×1,12, ×1,18, M, C (celular) y D, D⁺ (escritorio), de §1.5. «Sobre X» = la caja de X (`pasos.json` → `caja`, px CSS)
  centrada en lo visible. **«(real)»** = la posición no se conoce hasta grabar: se toma de `pasos.json` o del cuadro y se anota en el REVIEW.
- **Pulso:** el cuadro de §0.3; un evento «en el 1380» se ve en el 1380 y suena en el 1381.
- **Mundos del celular** (capas dentro de `#ventana-cel`, cada una con su cámara):

  | Capa | Visible | Grabación | Cámara |
  |---|---|---|---|
  | `#mK` | 0–839 | K (los 32 tramos y 3 stills del clip) | `#cam` y las capas del iris del clip (`#camT1`, `#camT2`, `#iris1`, `#m1in`) |
  | `#mC1` | 840–1319 | C·cerrar … C·enviar | `#camC1`; debajo del iris del 960, `#camC1s` con el still de C·buscar |
  | `#mC2` | 1560–2039 | C·acompana … C·pasos | `#camC2` |
  | `#mC3` | 2280–2759 | C·bienvenida, C·empezar | `#camC3` |

  La ventana del escritorio tiene dos capas en el mismo lugar: **`#mE1`** Contactos (E·fila … E·tomar, `#camE1`, visible 1310–1560) y
  **`#mE2`** el tablero y la novedad (E·tablero … E·amen, `#camE2`, visible 2030–2280).
- Las frases, siempre en el lugar de su escenario (§1.4); una a la vez; la ceja encima.

### 2.1 Parte 1 (0–839): el clip en 16:9

Se copia `clip-sitio-mi-iglesia/_gen/` a `recorrido-mi-iglesia/_gen/` y se cambia **solo** esto:

1. **Formato:** raíz 1920×1080, `data-duration="97"`. `#ventana` del clip → `#ventana-cel` con `.k-ventana-16x9` dentro de `#escena`, y su
   contenido en la capa `#mK`; `window.KD` de §1.4 (`W` 720, `HV` 900, `K` 0,615385, `PPC` 1,846, `VH` 1558,15). Las marcas de toque siguen
   en `calc(px * var(--f-k))` con el `--f-k` nuevo.
2. **Los mismos 32 tramos y 3 stills** (`TRAMOS` y `STILLS` de `gen.py`) desde `assets/grabaciones/clip/grabacion.mp4`, con sus mismos
   cuadros; el mismo iris (180–185) con sus dos capas; el mismo corte del 662 con su aterrizaje; las mismas 14 marcas (`TOQUES`) y las
   mismas tres compensaciones (389, 464, 645).
3. **Las mismas cámaras** con `s' = max(s, 1,085)` y, donde hay compensación, el centro subido para que el borde de abajo quede en 768
   (§1.5). Todos los encuadres nuevos contienen lo que mostraba el del clip (se ve un poco más):

   | Encuadre del clip | s del clip | s en 16:9 | (cx, cy) en 16:9 | Visible (px CSS, alto) |
   |---|---|---|---|---|
   | inicio | 1 | **1,085** | 195 · 224,5 | 0–449 |
   | reacciones | 1,08 | **1,085** | 195 · 500 | 276–724 |
   | tarjeta | 1,4 | 1,4 | 150 · 540 | 366–714 |
   | evento | 1 | **1,085** | 195 · 229,4 | 5–454 |
   | datos | 1,12 | 1,12 | 186 · 428 | 210–646 |
   | inscripcion | 1,12 | 1,12 | 195 · **550** (era 572) | 332–768 |
   | quienes | 1,18 | 1,18 | 193 · **561** (era 582) | 355–768 |
   | form | 1 | **1,085** | 195 · 540 | 315–765 |
   | botonesForm | 1,18 | 1,18 | 193 · **561** (era 582) | 355–768 |
   | resultado | 1 | **1,085** | 195 · **543** (era 548) | 318–768 |
   | verBoleta | 1 | **1,085** | 195 · **543** (era 545,6) | 318–768 |
   | boleta | 1 | **1,085** | 195 · 354,6 | 130–579 |
   | qr (punch 690) | 1,3 | 1,3 | 195 · 456 | 268–644 |
   | grande | 1 | **1,085** | 195 · 400 | 175–625 |
   | **cerrarK** (nuevo, 780) | — | **1,085** | 195 · 470 (real: «Cerrar» entero por arriba del borde, medido en la grab. 1522) | 245–695 |

4. **Las frases** van a la columna izquierda (§1.4): la 1, la 2 y la 3 en sus cuadros del clip; **la frase 4 del clip (la del sitio) no va
   aquí**: pasa al 2520. En su lugar, **«Su · boleta, / también · sin · señal.»** palabra a palabra 720 · 722 · 724 · 726 · 728, sale
   837–841. La ceja entra en el 195 como en el clip y se queda.
5. **Se quitan:** la ventana a un lado del 724–738, la `subida` del 796, el dip del 837–839, la firma del 840, sus campanas y el fundido de la
   música (0,75 → 0,24 → 0).
6. **Del 720 al 839:** la cámara va a `grande` en 720–733 (como el clip) y, en el **780** (un movimiento en el compás 14), a **`cerrarK`**
   (780–793): el QR sube un poco y entran «Gabriela Hinestroza Perea», «FM75UZ», «Congreso de Jóvenes» y el botón **«Cerrar»**. La marca del
   840 se posa sobre «Cerrar» en el 836.

### 2.2 Parte 2 (840–2909): tabla maestra

| Cuadro | Pulso | La app (grabación) | Cámara | Texto | Sonido | Transición |
|---|---|---|---|---|---|---|
| **840** | ● 1,00 | toque «Cerrar» (la marca sobre K grab. 1522, en la caja de C·cerrar) | — | frase 4 sale 837–841; «Encuentra / su · comunidad.» 842 · 844 · 846 | `toque` a | **corte sobre el toque**: `#mK` → `#mC1` en el 841 |
| 841–869 | | C·cerrar +N, ya sin la boleta en grande: **«Mis boletas»** con la tarjeta del congreso («Tu boleta», el QR, «Código FM75UZ») y **la barra de abajo** (Inicio · Comunidades · Cursos · Objetivos) | set `boletas` G (195 · 620 → 395–844) en el 841 | | | |
| 870 | ● | toque **«Comunidades»** (C·comunidades) | quieta | | `toque` b | marca |
| 885 | ● | corte en la espera: «Comunidades» · «Mis comunidades \| Explorar» · **«Todavía no estás en una comunidad»** · «Las comunidades son el lugar para conocer gente de tu iglesia, crecer juntos y servir. Encuentra la tuya.» · «Explorar comunidades» (C·comunidades +N) | set `vacio` G (195 · 300, real) | | | corte |
| **900** | ● 0,84 | toque «Explorar comunidades» (C·explorar) | quieta | | `toque` c | marca |
| 915 | ● | corte en la espera: Explorar, las tarjetas con «Para ti» primero (real: Mujeres, Matrimonios…) | set `explorar` G (195 · 422) | | | corte |
| 930 | ● | C·buscar: la app baja hasta la tarjeta de **Jóvenes** (el `ver`: si es suave, 930–945; si salta, en el 930) | **quieta** | | `desliz` | |
| 946–959 | | quieto: la tarjeta de Jóvenes: su portada morada con el ícono, «Jóvenes», «Un lugar para crecer juntos en la fe, hacer amigos y servir. Nos vemos los sábados.», los avatares de sus líderes, «Miembros: N», «Unirme» | quieta | | | |
| **960** | ● 0,92 | toque en la portada de la tarjeta (C·jovenes) | `#camC1` set `comunidad` G (195 · 224,5) dentro del iris | | `toque` a | **iris** 960–965 desde el toque; debajo, `#camC1s` con el still del último cuadro de C·buscar en `explorar` |
| 965–1019 | | dentro del iris, corte en la carga: la comunidad ya pintada (C·jovenes +N, después de su entrada `k-subir`): la portada, **«Jóvenes»**, «Miembros: N», la descripción, «Unirme», «Conectar con un líder» | quieta | | | |
| 1020 | ● 0,77 | quieto | 1020–1033 → G `lideres` (195 · 420, real): «Unirme», **«Conectar con un líder · Un líder te escribirá para conocerte y acompañarte.»** y **«Líderes»: Andrés Felipe Restrepo Gómez · David Moreno Hinestroza** | | | |
| **1080** | ● 0,76 | toque **«Unirme»** (C·unirme): el confeti de la app (40 partículas, toda la pantalla), el botón se va, «Miembros: N+1»; la página se acomoda sin el botón (real) | quieta | | `toque` b (1,4) · `aparicion` 1082 | marca |
| **1140** | ● 0,75 | toque «Conectar con un líder» (C·conectar) | quieta (si la página subió y «Conectar» quedó a medias, la marca va donde dice `pasos.json`) | | `toque` c | marca |
| 1155 | ● | corte en la espera: el diálogo **«Conectar con un líder»** · «Los líderes de Jóvenes recibirán tu pedido y uno te escribirá. Si quieres, cuéntales algo de ti o en qué te pueden ayudar.» · «Mensaje (opcional)» · «Cancelar · Enviar» | set `dialogo` G (195 · 422, real: el diálogo entero) | | `aparicion` | corte |
| 1170–1246 | | **«Voy al congreso y quiero conocerlos.»** se escribe a 1× (C·mensaje; 36 teclas a 70 ms) con su contador «36 / 500» | quieta | | — | |
| **1260** | ● 0,63 | toque «Enviar» (C·enviar) | quieta | | `toque` a | marca |
| 1275 | ● | corte en la espera: **«Pediste conectar con un líder» · «Un líder te escribirá pronto.»** (el diálogo de la app, encima de la tarjeta que acaba de celebrar) | quieta (si el diálogo no cae en `dialogo`, se encuadra en el corte) | | `confirmacion` | corte |
| 1310–1320 | | `#mC1` sale a la izquierda con `#escena`; `#mE1` llega: E·fila | `#camE1` llega en **D** sobre la fila de Gabriela, lado izquierdo (real) | frase 5 y ceja salen 1317–1320 | `desliz` (1,4) | **Látigo horizontal a la izquierda**; aterriza 1,04 → 1,00 (1320–1330); halo |
| **1320** | ● 0,93 | E·fila: «Contactos» · «Pendientes: 5 · Tomados: N» (real) y, al final de los pendientes (van del más viejo al más nuevo), **la fila nueva**: avatar «G», **«Gabriela Hinestroza Perea»**, «Jóvenes», el punto verde y **«hace 1 min»**, **«"Voy al congreso y quiero conocerlos."»**, «Tomar» | D | ceja arriba (1322–1328); «Su · mensaje · llega · a · los · líderes.» 1323 · 1325 · 1327 · 1329 · 1331 · 1333 | | |
| 1350 | ● | quieto | 1350–1363 → D sobre el final de la fila: el mensaje y **«Tomar»** (real; la fila mide hasta 832 px CSS y D ve 711) | | | |
| **1380** | ● 0,90 | toque **«Tomar»** (E·tomar) | quieta | | `toque` b (1,4) | marca |
| 1383 | | corte en la espera: **el detalle** entra con su animación y, detrás, la fila celebra (24 partículas): avatar, «Gabriela Hinestroza Perea / Jóvenes», **«Tomado · hace 1 min · Lo tomó Andrés Felipe Restrepo Gómez»**, su mensaje en cita, «Llamar …» y «Escribir por WhatsApp» (si su ficha tiene teléfono, real), «Ver su ficha (Membresía)», «Cerrar · Atendido» | set D sobre el título y el estado (real) | | `aparicion` | corte |
| **1440** | ● 0,96 | quieto | 1440–1453 → D sobre la cita y los botones (real) | | | |
| 1500 | ● | quieto | quieta | | | |
| 1550–1560 | | `#mE1` sale a la derecha; vuelve el celular con `#mC2`: C·acompana | `#camC2` llega en G `acompana` (195 · 300, real) | frase 6 y ceja salen 1557–1560 | `desliz` | **Látigo horizontal a la derecha**; aterriza 1560–1570; halo |
| **1560** | ● 1,00 | C·acompana: Jóvenes con «Miembros: N+1» y la tarjeta **«Andrés Felipe Restrepo Gómez te acompañará · Te escribirá pronto para conocerte.»** con su avatar | G | ceja a la izquierda (1562–1568); «Y · un · líder / la · acompaña.» 1562 · 1564 · 1566 · 1568 · 1570 | | |
| 1575 | ● | quieto | **punch** 1575–1583 → C (1,8) sobre `#po2-contacto` | | `confirmacion` (1,4) | |
| 1620 | ● 0,84 | quieto | 1620–1633 → G `barraC2` (195 · 620 → 395–844, real): «Líderes» (Andrés, David) y **la barra de abajo** | | | |
| **1680** | ● 0,98 | toque **«Objetivos»** (C·objetivos) | quieta | frase 7 sale 1677–1681; «Crece / paso · a · paso.» 1682 · 1684 · 1686 · 1688 | `toque` c | marca |
| 1695 | ● | corte en la espera: **«Mis objetivos»**: la tarjeta con su anillo, **«Un devocional cada mañana»**, **«Paso 13 de 14 · 86 %»** (real), «Hoy» y el título del paso, «Lo hice · Aplazar» | set `objetivos` G (195 · 260, real) | | | corte |
| 1740 | ● 0,79 | toque en la tarjeta (C·objetivo) | quieta | | `toque` a | marca |
| 1755 | ● | corte en la espera: el detalle: el anillo grande, «Un devocional cada mañana», «Paso 13 de 14 · 86 %», **«Hoy»**, el título del paso y su texto (real: p. ej. «Servir · Marcos 10:45. Busca a quién ayudar hoy.»), **«Lo hice»**, «Aplazar», «Próximo recordatorio: …» | set `objetivo` G (195 · 330, real: del anillo a «Lo hice») | | | corte |
| **1800** | ● 0,93 | toque **«Lo hice»** (C·lo-hice) | quieta | | `toque` b (1,4) · `aparicion` 1803 | marca |
| 1802–1859 | | corte en la espera (la respuesta del servidor): **«¡Listo! Marcamos «{paso}» como hecho.»** entra con su escala; el anillo late (1 → 1,12 → 1 con resorte) y, al recargar, **crece a 93 %** con su transición; «Paso 14 de 14 · 93 %» y el paso siguiente con «Mañana» (real) | quieta | | | |
| 1860 | ● 0,81 | quieto | 1860–1873 → M (1,4) sobre el anillo, «Paso 14 de 14 · 93 %» y «¡Listo!…» (real) | | | |
| **1920** | ● *1,00* | C·pasos: la app baja a **«Todos los pasos»** (si es suave, 1920–1935) | **set** G `pasos` (195 · y real) en el 1920 si la app salta (es un corte); si baja suave, la cámara salta a G `pasos` en el 1936, cuando la app ya paró | | `desliz` | |
| 1921–2029 | | quieto: «Todos los pasos»: los hechos con ✓ y su día («Hace N días», «Ayer», **«Hoy»**), el siguiente marcado (real) | quieta | | | |
| 2030–2040 | | `#mC2` sale a la izquierda; `#mE2` llega: E·tablero | `#camE2` llega en D sobre las cifras (real) | frase 8 y ceja salen 2037–2040 | `desliz` | **Látigo horizontal a la izquierda**; aterriza 2040–2050; halo |
| **2040** | ● *0,76* | E·tablero: el tablero del Portal: el periodo y las cifras (Bienvenida, Objetivos, Comunidades, Publicaciones, Comunicados; real), «Datos de ejemplo» en la ventana | D | ceja arriba (2042–2048); «Y · sabes · quién · respondió.» 2043 · 2045 · 2047 · 2049 | | |
| **2100** | ● *0,91* | E·publicaciones: la app baja a «Publicaciones» y su tabla «Las N más recientes» | set D sobre la primera fila en el cuadro en que la app llega (como el 1920): **«Inscripciones abiertas» · «Toda la iglesia · {fecha}» · Alcance · Reacciones · Respuesta** (con su barra y su %; real) | | `desliz` | |
| **2160** | ● *1,00* | toque en **«Inscripciones abiertas»** (E·novedad) | quieta | | `toque` c | marca |
| 2175 | ● *1,00* | corte en la espera: la novedad ya bajada a **«Quién reaccionó»** (E·quien, después de su `ver`): «Todas · N» y un botón por reacción con su número (real: 👍 · 🙏 · 😮 · **🙌 57**) | set D sobre la sección (real) | | `aparicion` | corte |
| 2220 | ● | toque en **🙌** (E·amen) | quieta | | `toque` a | marca |
| **2235** | ● *1,00* | corte en la espera: la lista de 🙌, de la más reciente a la más vieja: **«Gabriela Hinestroza Perea 🙌»** primero | 2235–2248 → D⁺ (2,0) sobre su fila y las dos siguientes (real) | | `confirmacion` (1,4) | |
| 2270–2280 | | `#mE2` sale a la derecha; vuelve el celular con `#mC3`: C·bienvenida **desde su primer cuadro pintado** (la coreografía de la portada empieza con el aterrizaje) | `#camC3` llega en G `portada` (195 · 422, real) | frase 9 y ceja salen 2277–2280 | `desliz` | **Látigo horizontal a la derecha**; aterriza 2280–2290; halo |
| **2280** | ● *0,48* | C·bienvenida, la portada: el logo de la iglesia entra con su resorte, **«Hola, Lucía»**, el título palabra por palabra, «Empezar mis primeros pasos», «N pasos cortos · a tu ritmo»; detrás, dos luces que flotan (real) | G | ceja a la izquierda (2282–2288); «A · quien · llega, / una · bienvenida.» 2282 · 2284 · 2286 · 2288 · 2290 | | |
| **2400** | ● *0,74* | toque **«Empezar mis primeros pasos»** (C·empezar) | quieta | | `toque` b · `aparicion` 2402 | marca |
| 2402–2459 | | corte en la espera: **el camino de sus primeros pasos** entra con su animación (real) | set `camino` G (real) | | | corte |
| 2460 | ● | quieto | 2460–2473 → G sobre el camino entero (real; si ya cabe, quieta) | | | |
| **2520** | ● *0,63* | quieto | quieta | la ceja sale 2520–2523; «Tu · iglesia, · en · el · *bolsillo* / de · cada · miembro» 2519 · 2521 · … · 2533 | | |
| 2524–2538 | | | | | | **La ventana a un lado**: 0,92, origen «100% 50%», x +24 |
| 2539–2756 | | quieto (C·empezar, el final de su pausa) | quieta | la frase sostenida 7,9 s | `subida` desde 90,533 | |
| 2757–2759 | | | | | | **dip** sobre la ventana |
| **2760** | ● | — | — | — | marca en 92,38 | **corte al cierre del Comercial** (`#escena` oculta) |

### 2.3 Los planos de la parte 2

#### P8 · «Su boleta, también sin señal» → el toque que cierra — 720–869
La boleta en grande del clip se queda con su frase nueva (la del sitio espera al final). En el 780 la cámara baja lo justo para que se vea
«Cerrar»; en el 840, el golpe más fuerte de la pista, **la persona cierra su boleta** y la app vuelve a «Mis boletas» con su barra: el video
no cambia de persona ni de aparato, cambia de tema. 870: «Comunidades».

#### P9 · «Encuentra su comunidad» — 840–1319 (compases 15–22)
La pantalla vacía dice lo mismo que la frase («Encuentra la tuya»). Explorar, la app baja a Jóvenes y, **en la costura de la música**, el toque
en la tarjeta abre la comunidad con el único iris de la parte 2. 1020: la cámara planta a **Andrés** en «Líderes» (vuelve en el 1320 y en el
1560). 1080: «Unirme» con el confeti de la app; 1140–1275: el pedido de un líder, con su mensaje escrito a velocidad real (es el dato que
viaja) y la respuesta de la app. Respiro de la música, cámara casi quieta: la app es la que se mueve.

#### P10 · «Su mensaje llega a los líderes» — 1320–1559 (compases 23–26)
El látigo es la puerta al escritorio del pastor. Su mensaje está ahí, el último de la bandeja, con «hace 1 min» en verde. La cámara va de su
nombre a «Tomar» (1350), el toque en un golpe fuerte (1380) y el detalle con su teléfono (1383–1559): el pastor ya puede escribirle.

#### P11 · «Y un líder la acompaña» — 1560–1679 (compases 27–28)
**El golpe más fuerte de la parte 2.** El látigo vuelve al celular de ella y la primera imagen es la respuesta: «Andrés Felipe Restrepo Gómez
te acompañará». Punch a la tarjeta (1575) y la cámara baja a «Líderes» y a la barra (1620), donde está el siguiente toque.

#### P12 · «Crece paso a paso» — 1680–2039 (compases 29–34)
«Objetivos» en la barra, la tarjeta del devocional, el detalle con su paso de **hoy**. **El primer golpe del clímax (1800) es su toque en «Lo
hice»**: la app confirma y el anillo crece. 1860: M sobre el anillo y la cifra; 1920: la app baja a «Todos los pasos», una fila de ✓.

#### P13 · «Y sabes quién respondió» — 2040–2279 (compases 35–38)
Segundo viaje al escritorio, en la segunda frase del clímax. El tablero del Portal (2040), la tabla de publicaciones con el anuncio del clip
arriba, su alcance y su respuesta (2100), el toque en su título (2160), «Quién reaccionó» (2175), el 🙌 (2220) y **su nombre, primero de la
lista (2235)**: el «Amén» del cuadro 120 volvió. De una persona a toda la iglesia y de la iglesia otra vez a una persona.

#### P14 · «A quien llega, una bienvenida» y el cierre — 2280–2909
El último látigo no vuelve a Gabriela: es el celular de **alguien que acaba de llegar**, con la bienvenida que su iglesia armó, en la salida
tranquila de la música (la coreografía de la portada es de la app). 2400: «Empezar mis primeros pasos» y su camino. «Tu iglesia, en el
*bolsillo* de cada miembro» palabra a palabra en el 2520; la ceja se va; la ventana se hace a un lado (2524–2538) y todo queda quieto salvo
el halo; la `subida` empieza en el 90,533 y su golpe cae con el cierre. Dip 2757–2759. **2760: `cierre-comercial`**:

```html
<div id="cierre-comercial" data-composition-id="cierre-comercial" data-composition-src="identidad/cierre-comercial.html"
  data-variable-values='{"publico":"iglesia","llamado":"prueba","contacto":"sitio","fondo":"noche","idioma":"es"}'
  data-start="92" data-duration="5" data-track-index="6" data-width="1920" data-height="1080"></div>
<audio id="marca-cierre" src="identidad/audio/sonido-marca.wav" data-start="92.38" data-duration="2.1" data-track-index="26" data-volume="1"></audio>
```

---

## 3. Las grabaciones

### 3.1 Lo que se reusa

- **La grabación del clip, entera y sin cambios:** `clip-sitio-mi-iglesia/assets/grabaciones/grabacion.mp4` (1170×2532, 30 fps, 52,2 s),
  `pasos.json` y `hoja-grabacion.jpg` → `recorrido-mi-iglesia/assets/grabaciones/clip/`. Nada de la parte 1 se vuelve a grabar.
- **Los stills del clip:** `clip-sitio-mi-iglesia/assets/stills/still-354.png`, `still-705.png`, `still-1258.png` → `assets/stills/`.
- **Los sonidos del clip:** `clip-sitio-mi-iglesia/assets/audio/toque-b.wav` y `toque-c.wav` → `assets/audio/`.
- **El generador del clip:** `clip-sitio-mi-iglesia/_gen/` → `recorrido-mi-iglesia/_gen/` (`gen.py`, `index.tpl.html` y las ayudas de
  revisión `diff.py`, `shift.py`, `hoja.py`, `regla.py`, `mont.py`, `rcheck.py`). `gen.py` suma las tablas de la parte 2 (`TRAMOS_C`,
  `TRAMOS_E`, `STILLS_C`, `TOQUES_C`, `TOQUES_E`, sonidos) y la plantilla, las capas de §2.0, las cámaras nuevas y los látigos de Academia.
- **La música:** la misma de Academia (§0.1).
- **El kit:** `npm run kit` (monta `identidad/` con `cierre-comercial.html`, los sonidos de acción y el sonido de marca); `frame.md` =
  `identidad/frame-comercial.md`.

Dos escenas nuevas, una por dispositivo, sobre Kingdom Demo en español, con `capturar.mjs --modo video` y `toque: false`:

```bash
cd tools/ayuda
node capturar.mjs clips/recorrido-mi-iglesia-celular --idioma es --modo capturas      # prueba el sql y las refs
node capturar.mjs clips/recorrido-mi-iglesia-celular --idioma es --modo video         # → salida/video/es/clips/recorrido-mi-iglesia-celular/
node capturar.mjs clips/recorrido-mi-iglesia-escritorio --idioma es --modo capturas
node capturar.mjs clips/recorrido-mi-iglesia-escritorio --idioma es --modo video      # → salida/video/es/clips/recorrido-mi-iglesia-escritorio/
# cada una: grabacion.mp4 + pasos.json; se copian a recorrido-mi-iglesia/assets/grabaciones/celular/ y …/escritorio/
```

Lo que la herramienta ya hace y las escenas usan (sin nada nuevo): `como` e `ir` del primer paso antes de grabar; `como` a mitad de la
escena (otra cuenta: `__kv2Dev.login`); `escribir` a 70 ms por tecla; `ver` (con `bloque`, por defecto `center`; suave en video);
`clic` con `espera` u `oculto`; `tecla`; `pausa` sin tope en video; `sql` tras restaurar el volcado; `refs` consultadas una vez, en orden,
justo antes de abrir Chrome (cada una debe dar un valor: sin valor, la escena no arranca). Cada escena restaura su volcado: lo que hace una
no lo ve la otra, por eso las dos dejan a Gabriela en el mismo estado con su `sql`.

### 3.2 La escena de celular: `tools/ayuda/escenas/clips/recorrido-mi-iglesia-celular.mjs`

```js
// Grabación para el RECORRIDO de Mi iglesia (LegacyHyperframes/videos/kingdomapp/recorrido-mi-iglesia/SPEC.md §3.2): la parte 2 en CELULAR.
// NO es una escena de un artículo de la ayuda: no se publica ni entra en la frescura. Una sola escena de CELULAR (390×844 a 3x = 1170×2532,
// 30 cps) grabada SIN el círculo del toque (`toque: false`): el montaje dibuja el suyo sobre las cajas y los toques de pasos.json.
//   node capturar.mjs clips/recorrido-mi-iglesia-celular --idioma es --modo capturas   (prueba el sql y las refs)
//   node capturar.mjs clips/recorrido-mi-iglesia-celular --idioma es --modo video
//   → salida/video/es/clips/recorrido-mi-iglesia-celular/grabacion.mp4 + pasos.json
// Tres cuentas, en este orden:
//   1. Gabriela (105, la miembro del clip): cierra su boleta, entra a Comunidades, explora, se une a Jóvenes y pide un líder con su mensaje.
//   (fuera de cuadro) El pastor (101, líder de Jóvenes) toma el contacto desde su celular: así la tarjeta de ella dice quién la acompaña. La
//      toma que se VE es la del escritorio (escena hermana, §3.3).
//   2. Gabriela otra vez: «… te acompañará»; Mis objetivos; «Lo hice» en el paso de hoy; «Todos los pasos».
//   3. Lucía (104): la bienvenida desde el comienzo y «Empezar mis primeros pasos».
// Estado previo por SQL (sobre la base restaurada, solo local): la boleta de Gabriela con el código del clip; Gabriela sin comunidades ni
// contactos; el pastor como líder de Jóvenes; el paso de su objetivo en curso con fecha de hoy; Lucía sin bienvenida empezada.
// Datos ficticios de Kingdom Demo; la escena escribe un mensaje corto y nada personal.
const KDEMO = `(SELECT id FROM kd_sedes WHERE codigo = 'KDEMO')`;
const CONGRESO = `(SELECT MAX(e.id) FROM ev_eventos e WHERE e.id_sede = ${KDEMO} AND e.nombre IN ('Congreso de Jóvenes', 'Youth Conference'))`;
const ficha = cuenta => `(SELECT us.id_persona FROM kd_usuario_sedes us WHERE us.id_usuario = ${cuenta} AND us.id_sede = ${KDEMO})`;
const YO = ficha(105);       // Gabriela Hinestroza Perea
const PASTOR = ficha(101);   // Andrés Felipe Restrepo Gómez
const LUCIA = ficha(104);    // Lucía Ruiz Montoya
const JOVENES = `(SELECT c.id FROM po_comunidades c WHERE c.id_sede = ${KDEMO} AND c.activa = 1 AND c.nombre IN ('Jóvenes', 'Young adults') ORDER BY c.id LIMIT 1)`;
// Su objetivo en curso que todavía no está en el último paso; primero el devocional.
const OBJETIVO = `SELECT pp.id FROM po_persona_planes pp JOIN po_planes pl ON pl.id = pp.id_plan
                   WHERE pp.id_persona = ${YO} AND pp.estado = 'activo' AND pp.paso_actual + 1 < pp.total_pasos
                   ORDER BY (pl.tipo = 'devocional') DESC, pp.id LIMIT 1`;
// El día de la iglesia (Kingdom Demo vive en America/Bogota, sin horario de verano).
const HOY = `DATE(CONVERT_TZ(UTC_TIMESTAMP(), '+00:00', '-05:00'))`;
const BOLETA = '#boletas-lista li.boleta.destacada:has-text("Tu boleta")';
const MENSAJE = 'Voy al congreso y quiero conocerlos.';
const SU_FILA = '#po2-contactos article.contacto:has-text("{@nombre}")';
const TARJETA = '#po2-explorar [data-explorar="{@jovenes}"]';

export default {
  articulo: 'clips/recorrido-mi-iglesia-celular',
  movil: true,
  toque: false,
  pantallas: [
    'frontend-v2/src/app/layout/shell/shell.component.html',
    'frontend-v2/src/app/pages/mi/boletas.page.ts',
    'frontend-v2/src/app/pages/mi/comunidades.page.ts',
    'frontend-v2/src/app/pages/mi/comunidad.page.ts',
    'frontend-v2/src/app/pages/mi/comunidad-mensaje.component.ts',
    'frontend-v2/src/app/pages/portal/contactos.page.ts',
    'frontend-v2/src/app/pages/mi/objetivos-en-curso.component.ts',
    'frontend-v2/src/app/pages/mi/objetivo.page.ts',
    'frontend-v2/src/app/pages/mi/bienvenida.page.ts',
    'frontend-v2/src/app/pages/mi/bienvenida/portada.component.ts',
    'frontend-v2/src/app/pages/mi/bienvenida/camino.component.ts',
  ],
  sql: [
    // 1. La boleta del clip: la inscripción de Gabriela en el congreso, inscrita y con el código que se ve en la grabación del clip (FM75UZ,
    //    REVIEW del clip §4.1). Si la semilla la dejó en espera o por aprobar, pasa a inscrita.
    `UPDATE ev_inscritos SET estado = 'inscrito', codigo_corto = 'FM75UZ'
      WHERE id_evento = ${CONGRESO} AND id_persona = ${YO} AND estado IN ('inscrito', 'espera', 'por_aprobar')`,
    // 2. Gabriela empieza sin comunidades ni contactos (la semilla la dejó en Jóvenes con un contacto tomado), y sin el acompañamiento que
    //    dejó ese contacto: el «Tomar» de la escena lo vuelve a crear.
    `DELETE FROM po_contactos WHERE id_persona = ${YO}`,
    `DELETE FROM po_comunidad_personas WHERE id_persona = ${YO} AND rol = 'miembro'`,
    `UPDATE mem_acompanamientos SET estado = 'terminado', terminado_at = NOW(), motivo_fin = 'manual'
      WHERE activo_de = ${YO} AND origen = 'comunidad'`,
    // 3. El pastor (101) es líder de Jóvenes (la semilla lo pone primero si su ficha es la primera con cuenta; aquí se asegura).
    `INSERT INTO po_comunidad_personas (id_comunidad, id_persona, rol, estado, por, created_at)
       SELECT ${JOVENES}, ${PASTOR}, 'lider', 'activa', 101, NOW() - INTERVAL 60 DAY FROM DUAL
       ON DUPLICATE KEY UPDATE rol = 'lider', estado = 'activa'`,
    // 4. El paso actual de su objetivo es de HOY (la app dice «Hoy»; si ya hizo el de hoy, el siguiente decía «Mañana»).
    `UPDATE po_persona_planes SET paso_dia = ${HOY} WHERE id = (SELECT id FROM (${OBJETIVO}) x)`,
    // 5. Lucía ve la bienvenida desde el comienzo (como la escena de la ayuda mi-iglesia/la-bienvenida).
    `DELETE b FROM po_persona_bienvenida b JOIN kd_usuario_sedes us ON us.id_persona = b.id_persona AND us.id_sede = b.id_sede
      WHERE us.id_usuario = 104`,
  ],
  refs: {
    // El nombre del clip: si la semilla cambió, el corte del 840 uniría dos personas distintas (la escena se niega).
    nombre: `SELECT p.nombre_completo FROM mem_personas p WHERE p.id = ${YO} AND p.nombre_completo = 'Gabriela Hinestroza Perea'`,
    boleta: `SELECT i.id FROM ev_inscritos i WHERE i.id_evento = ${CONGRESO} AND i.id_persona = ${YO} AND i.estado = 'inscrito' AND i.codigo_corto = 'FM75UZ'`,
    jovenes: `SELECT ${JOVENES}`,
    lider: `SELECT p.nombre_completo FROM po_comunidad_personas cp JOIN mem_personas p ON p.id = cp.id_persona
             WHERE cp.id_comunidad = ${JOVENES} AND cp.id_persona = ${PASTOR} AND cp.rol = 'lider' AND cp.estado = 'activa'`,
    sinComunidad: `SELECT IF(COUNT(*) = 0, 1, NULL) FROM po_comunidad_personas WHERE id_persona = ${YO} AND estado IN ('activa', 'solicitada')`,
    objetivo: OBJETIVO,
    hoy: `SELECT IF(pp.paso_dia = ${HOY}, 1, NULL) FROM po_persona_planes pp WHERE pp.id = (${OBJETIVO})`,
    bienvenida: `SELECT IF(COUNT(*) = 0, 1, NULL) FROM po_persona_bienvenida b WHERE b.id_persona = ${LUCIA}`,
  },
  pasos: [
    // ── 0. La boleta (P8). La entrada se hace antes de grabar: el video abre en «Mis boletas». La grande se abre fuera del montaje solo para
    //       que el toque de «Cerrar» quede en pasos.json (el 840 lo dibuja sobre la grabación del clip).
    { tramo: 'boletas', como: 105, ir: '/mi/boletas', espera: BOLETA, pausa: 1000 },
    { tramo: 'grande', clic: `${BOLETA} .qr-boton`, espera: '#boleta-grande .g-cerrar', pausa: 1500 },
    { tramo: 'cerrar', clic: '#boleta-grande .g-cerrar', oculto: '#boleta-grande', pausa: 1500 },                     // 840 → 841–869
    // ── 1. Comunidades (P9).
    { tramo: 'comunidades', clic: '#nav-comunidades', espera: '#po2-vacio #po2-ir-explorar', pausa: 1200 },          // 870 → 885–899
    { tramo: 'explorar', clic: '#po2-ir-explorar', espera: TARJETA, pausa: 900 },                                     // 900 → 915–929
    { tramo: 'buscar', ver: TARJETA, pausa: 1200 },                                                                   // 930–959
    { tramo: 'jovenes', clic: `${TARJETA} a.enlace`, espera: '#po2-unirme', pausa: 4200 },                           // 960 → 965–1079
    { tramo: 'unirme', clic: '#po2-unirme', oculto: '#po2-unirme', pausa: 2200 },                                     // 1080 → 1081–1139
    { tramo: 'conectar', clic: '#po2-conectar', espera: '#po2-mensaje', pausa: 600 },                                 // 1140 → 1155–1169
    { tramo: 'mensaje', escribir: { en: '#po2-mensaje', texto: MENSAJE }, pausa: 600 },                              // 1170–1246
    { tramo: 'enviar', clic: '#po2-mensaje-enviar', espera: '#po2-contacto[data-estado="pendiente"]', pausa: 1800 },  // 1260 → 1275–1319
    { clic: '#btn-ok', oculto: '#btn-ok' },                                                                           // fuera de cámara
    // ── Fuera de cuadro: el pastor toma el contacto (la toma que se ve es la del escritorio).
    { tramo: 'toma-fuera', como: 101, ir: '/servir/portal/contactos', espera: `${SU_FILA} [data-tomar]` },
    { clic: `${SU_FILA} [data-tomar]`, espera: 'mat-dialog-container #po2-atender' },
    { tecla: 'Escape', oculto: 'mat-dialog-container' },
    // ── 2. Acompañada (P11) y su objetivo (P12).
    { tramo: 'acompana', como: 105, ir: '/mi/comunidades/{@jovenes}', espera: '#po2-contacto[data-estado="tomado"]', pausa: 4400 },  // 1560–1679
    { tramo: 'objetivos', clic: '#nav-objetivos', espera: '#obj-lista li[data-objetivo="{@objetivo}"] [data-accion="completar"]', pausa: 1800 },  // 1680 → 1695–1739
    { tramo: 'objetivo', clic: '#obj-lista li[data-objetivo="{@objetivo}"] a.cabeza', espera: '#btn-lo-hice', pausa: 1800 },  // 1740 → 1755–1799
    { tramo: 'lo-hice', clic: '#btn-lo-hice', espera: '#objetivo-hecho[data-hecho="completado"]', pausa: 4200 },     // 1800 → 1802–1919
    { tramo: 'pasos', ver: '#objetivo-pasos', pausa: 4200 },                                                          // 1920–2039
    // ── 3. Quien llega (P14): la bienvenida de Lucía desde su portada.
    { tramo: 'bienvenida', como: 104, ir: '/mi/bienvenida', espera: '#bv-empezar', pausa: 4500 },                    // 2280–2399
    { tramo: 'empezar', clic: '#bv-empezar', espera: '#bv-camino', pausa: 12500 },                                   // 2400 → 2402–2759
  ],
};
```

**Comprobaciones obligatorias al grabar** (si una falla, se vuelve a grabar):
1. El cuadro de C·cerrar justo después de la acción muestra «Mis boletas» con **«FM75UZ»** y la barra de abajo; su caja de `cerrar` cae
   donde está «Cerrar» en la grab. 1522 del clip (mismo aparato, misma pantalla: se comparan las dos hojas).
2. En Explorar aparece la tarjeta de Jóvenes con «Unirme» (abierta) y, en la comunidad, «Líderes» nombra a **Andrés Felipe Restrepo Gómez**
   (`refs.lider` da su nombre).
3. «Unirme» dibuja el confeti en la grabación (si el modo ligero o `prefers-reduced-motion` lo apagó, se graba otra vez con el celular de
   referencia sin ellos; no se agrega en el montaje, BANNED 23).
4. C·acompana dice **«Andrés Felipe Restrepo Gómez te acompañará»**.
5. C·objetivo dice **«Hoy»** encima del paso y C·lo-hice muestra «¡Listo! Marcamos «…» como hecho.» con el anillo más lleno que antes.
6. C·bienvenida saluda a **Lucía** (nunca a Gabriela) y su portada termina su coreografía antes del cuadro equivalente al 2399.

### 3.3 La escena de escritorio: `tools/ayuda/escenas/clips/recorrido-mi-iglesia-escritorio.mjs`

```js
// Grabación para el RECORRIDO de Mi iglesia (LegacyHyperframes/videos/kingdomapp/recorrido-mi-iglesia/SPEC.md §3.3): la parte 2 en ESCRITORIO.
// NO es una escena de un artículo de la ayuda. En video el escritorio es 1280×720 a 1,5x (1920×1080 reales, 30 cps), sin cursor ni círculo
// (`toque: false`): el montaje dibuja su marca de toque sobre las cajas de pasos.json.
//   node capturar.mjs clips/recorrido-mi-iglesia-escritorio --idioma es --modo capturas   (prueba el sql y las refs)
//   node capturar.mjs clips/recorrido-mi-iglesia-escritorio --idioma es --modo video
//   → salida/video/es/clips/recorrido-mi-iglesia-escritorio/grabacion.mp4 + pasos.json
// Una cuenta: 101, el administrador (el pastor Andrés, líder de Jóvenes).
//   1. contactos (P10): la bandeja con el pedido que Gabriela acaba de hacer en su celular (el mismo mensaje) y «Tomar».
//   2. tablero (P13): el tablero del Portal, la tabla de publicaciones, la novedad del clip y «Quién reaccionó» filtrado por 🙌.
// Estado previo por SQL: lo que Gabriela hizo en la escena del celular (en Jóvenes y con su pedido de hace un minuto) y lo que hizo en el
// clip (la novedad «Inscripciones abiertas» repuntada al congreso, la más reciente, y su «Amén», el más reciente). Datos ficticios.
const KDEMO = `(SELECT id FROM kd_sedes WHERE codigo = 'KDEMO')`;
const CONGRESO = `(SELECT MAX(e.id) FROM ev_eventos e WHERE e.id_sede = ${KDEMO} AND e.nombre IN ('Congreso de Jóvenes', 'Youth Conference'))`;
const ficha = cuenta => `(SELECT us.id_persona FROM kd_usuario_sedes us WHERE us.id_usuario = ${cuenta} AND us.id_sede = ${KDEMO})`;
const YO = ficha(105);
const PASTOR = ficha(101);
const JOVENES = `(SELECT c.id FROM po_comunidades c WHERE c.id_sede = ${KDEMO} AND c.activa = 1 AND c.nombre IN ('Jóvenes', 'Young adults') ORDER BY c.id LIMIT 1)`;
const NOVEDAD = `p.id_sede = ${KDEMO} AND p.ambito = 'iglesia' AND p.ref_tipo = 'evento' AND p.titulo IN ('Inscripciones abiertas', 'Registration is open')`;
const POST = `SELECT p.id FROM po_publicaciones p WHERE ${NOVEDAD} AND p.estado = 'publicada' AND p.ref_id = ${CONGRESO}
               AND JSON_VALUE(p.bloques, '$.bloques[1].id') = p.ref_id ORDER BY p.id DESC LIMIT 1`;
const MENSAJE = 'Voy al congreso y quiero conocerlos.';
const FILA = '#po2-contactos article.contacto[data-contacto="{@contacto}"]';

export default {
  articulo: 'clips/recorrido-mi-iglesia-escritorio',
  toque: false,
  pantallas: [
    'frontend-v2/src/app/pages/portal/contactos.page.ts',
    'frontend-v2/src/app/pages/portal/contacto-dialog.component.ts',
    'frontend-v2/src/app/pages/portal/tablero.page.ts',
    'frontend-v2/src/app/pages/portal/tablero/cifras.component.ts',
    'frontend-v2/src/app/pages/portal/tablero/publicaciones.component.ts',
    'frontend-v2/src/app/pages/portal/novedad-editar.page.ts',
  ],
  sql: [
    // 1. La novedad del clip (lo mismo que el punto 1 de escenas/clips/mi-iglesia-boleta.mjs): lleva la tarjeta del congreso y es la más
    //    reciente, así queda primera en la tabla de publicaciones del tablero.
    `UPDATE po_publicaciones p
        SET p.ref_id = ${CONGRESO}, p.bloques = JSON_SET(p.bloques, '$.bloques[1].id', ${CONGRESO}), p.publicar_at = NOW() - INTERVAL 3 MINUTE
      WHERE ${NOVEDAD} AND p.estado = 'publicada' AND JSON_VALUE(p.bloques, '$.bloques[1].t') = 'evento'`,
    // 2. Su «Amén» del clip, el más reciente de la novedad, con los conteos al día.
    `DELETE r FROM po_reacciones r JOIN po_publicaciones p ON p.id = r.id_publicacion WHERE ${NOVEDAD} AND r.id_persona = ${YO}`,
    `INSERT INTO po_reacciones (id_publicacion, id_persona, codigo, at)
       SELECT p.id, ${YO}, 'amen', NOW() - INTERVAL 2 MINUTE FROM po_publicaciones p
        WHERE ${NOVEDAD} AND p.estado = 'publicada' AND p.ref_id = ${CONGRESO} ORDER BY p.id DESC LIMIT 1`,
    `INSERT IGNORE INTO po_publicacion_conteos (id_publicacion, codigo, n) SELECT p.id, 'amen', 0 FROM po_publicaciones p WHERE ${NOVEDAD}`,
    `UPDATE po_publicacion_conteos c JOIN po_publicaciones p ON p.id = c.id_publicacion
        SET c.n = (SELECT COUNT(*) FROM po_reacciones r WHERE r.id_publicacion = c.id_publicacion AND r.codigo = c.codigo)
      WHERE ${NOVEDAD}`,
    // 3. Lo que hizo en el celular: está en Jóvenes y pidió un líder hace un minuto, con su mensaje (pendiente, el más nuevo de la bandeja).
    `DELETE FROM po_contactos WHERE id_persona = ${YO}`,
    `DELETE FROM po_comunidad_personas WHERE id_persona = ${YO} AND rol = 'miembro'`,
    `UPDATE mem_acompanamientos SET estado = 'terminado', terminado_at = NOW(), motivo_fin = 'manual'
      WHERE activo_de = ${YO} AND origen = 'comunidad'`,
    `INSERT INTO po_comunidad_personas (id_comunidad, id_persona, rol, estado, created_at)
       SELECT ${JOVENES}, ${YO}, 'miembro', 'activa', NOW() - INTERVAL 2 MINUTE FROM DUAL`,
    `INSERT INTO po_contactos (id_sede, id_comunidad, id_persona, mensaje, estado, created_at)
       SELECT ${KDEMO}, ${JOVENES}, ${YO}, '${MENSAJE}', 'pendiente', NOW() - INTERVAL 1 MINUTE FROM DUAL`,
    // 4. El pastor (101) es líder de Jóvenes (como en la escena del celular).
    `INSERT INTO po_comunidad_personas (id_comunidad, id_persona, rol, estado, por, created_at)
       SELECT ${JOVENES}, ${PASTOR}, 'lider', 'activa', 101, NOW() - INTERVAL 60 DAY FROM DUAL
       ON DUPLICATE KEY UPDATE rol = 'lider', estado = 'activa'`,
  ],
  refs: {
    nombre: `SELECT p.nombre_completo FROM mem_personas p WHERE p.id = ${YO} AND p.nombre_completo = 'Gabriela Hinestroza Perea'`,
    lider: `SELECT p.nombre_completo FROM po_comunidad_personas cp JOIN mem_personas p ON p.id = cp.id_persona
             WHERE cp.id_comunidad = ${JOVENES} AND cp.id_persona = ${PASTOR} AND cp.rol = 'lider' AND cp.estado = 'activa'`,
    contacto: `SELECT k.id FROM po_contactos k WHERE k.id_persona = ${YO} AND k.id_comunidad = ${JOVENES} AND k.estado = 'pendiente'`,
    post: POST,
    // Su reacción es la más reciente de la novedad: la lista de 🙌 la pone primera (portalQuienReacciono ordena por `at` DESC).
    amen: `SELECT IF(MAX(r.at) = (SELECT r2.at FROM po_reacciones r2 WHERE r2.id_publicacion = (${POST}) AND r2.id_persona = ${YO} AND r2.codigo = 'amen'), 1, NULL)
             FROM po_reacciones r WHERE r.id_publicacion = (${POST}) AND r.codigo = 'amen'`,
  },
  pasos: [
    // ── 1. Contactos (P10). La entrada se hace antes de grabar: el video abre en la bandeja.
    { tramo: 'contactos', como: 101, ir: '/servir/portal/contactos', espera: FILA, pausa: 600 },
    { tramo: 'fila', ver: FILA, pausa: 2200 },                                                                        // 1320–1379
    { tramo: 'tomar', clic: `${FILA} [data-tomar]`, espera: 'mat-dialog-container #po2-atender', pausa: 6200 },      // 1380 → 1383–1559
    { tecla: 'Escape', oculto: 'mat-dialog-container' },                                                              // fuera de cámara
    // ── 2. El tablero y la novedad (P13).
    { tramo: 'tablero', ir: '/servir/portal/tablero', espera: '#tab-publicaciones', pausa: 2400 },                    // 2040–2099
    { tramo: 'publicaciones', ver: '#po7-pub-tabla', pausa: 2200 },                                                   // 2100–2159
    { tramo: 'novedad', clic: '#po7-pub-tabla tr[data-publicacion="{@post}"] a', espera: '#novedad-quien' },         // 2160
    { tramo: 'quien', ver: '#novedad-quien', pausa: 1800 },                                                           // 2175–2219
    { tramo: 'amen', clic: '#novedad-quien .reac[data-codigo="amen"]', espera: '#novedad-quien ul.personas li', pausa: 2000 },  // 2220 → 2235–2279
  ],
};
```

**Comprobaciones al grabar:** la fila de Gabriela dice «hace 1 min» y su mensaje entero (la línea se corta a dos: `-webkit-line-clamp: 2`);
el detalle dice «Lo tomó Andrés Felipe Restrepo Gómez»; en la tabla del tablero, «Inscripciones abiertas» es **la primera fila** (si no, el
periodo del tablero no incluye hoy: se toca el atajo de los últimos 30 días, `#po7-atajo-…`, antes del tramo `publicaciones`); en
«Quién reaccionó», el botón 🙌 dice el mismo número que el «Amén» del clip (57) y la primera persona de su lista es **Gabriela Hinestroza
Perea**. Si el número no es 57, la semilla cambió: se anota en el REVIEW (ninguna frase depende de él).

### 3.4 Selectores, verificados el 2026-10-30 en `frontend-v2/src/app/`

- **Barra de abajo** (`layout/shell/shell.component.html` y `navegacion.ts`): `nav.inferior a[id]` con `#nav-inicio`, `#nav-comunidades`,
  `#nav-cursos`, `#nav-objetivos` (los textos «Inicio», «Comunidades», «Cursos», «Objetivos» de `nav.*`).
- **Mis boletas** (`pages/mi/boletas.page.ts`): `#boletas-lista li.boleta.destacada` («Tu boleta»), `.qr-boton`, `#boleta-grande` con
  `.g-cerrar` («Cerrar», `evi.cerrar`); la boleta en grande se cierra con su botón o tocando la pantalla.
- **Comunidades** (`pages/mi/comunidades.page.ts`): `#po2-vacio` («Todavía no estás en una comunidad», `po2.vacio_titulo`), `#po2-ir-explorar`,
  `#po2-explorar`, `[data-explorar="{id}"]` con su `a.enlace` (la portada) y `#po2-unirme-{id}`. **Una comunidad** (`pages/mi/comunidad.page.ts`):
  `#titulo-comunidad`, `#po2-unirme` (el confeti: `celebrar(null, { particulas: 40 })`), `#po2-conectar`, `#po2-contacto[data-estado]`
  («Pediste conectar con un líder» / «{lider} te acompañará»: `po2.contacto_enviado`, `po2.te_acompanara`), `#t-lideres`. **El diálogo**
  (`comunidad-mensaje.component.ts`): `#po2-mensaje` (`maxlength` 500 y su contador), `#po2-mensaje-enviar`; el aviso de éxito es el de
  `components/app-dialog.component.ts` con `#btn-ok`.
- **Contactos** (`pages/portal/contactos.page.ts`, ruta `/servir/portal/contactos` con `portal.comunidades`): `#po2-conteos`, `#po2-contactos
  article.contacto[data-contacto][data-semaforo]`, `[data-tomar]` (el confeti de la fila: `celebrar(fila, { particulas: 24 })`, y después el
  detalle). **El detalle** (`contacto-dialog.component.ts`): `#po2-llamar`, `#po2-whatsapp`, `#po2-ver-ficha`, `#po2-atender` (solo cuando ya
  está tomado). La bandeja ordena los pendientes por `created_at` ascendente (`portalContactosSql`, `backend/_datos/portal_comunidades.php`).
- **Objetivos** (`pages/mi/objetivos-en-curso.component.ts`): `#obj-lista li[data-objetivo]`, su `a.cabeza`, `[data-accion="completar"]`.
  **Un objetivo** (`pages/mi/objetivo.page.ts`): `#titulo-objetivo`, `#btn-lo-hice`, `#objetivo-hecho[data-hecho]` («¡Listo! Marcamos «{paso}»
  como hecho.», `po3.hecho_completado`), `#objetivo-pasos li[data-paso][data-estado-paso]`. El avance es `paso_actual / total_pasos` y «Hoy»
  sale de `paso_dia` (`backend/_datos/portal_objetivos.php`).
- **Tablero** (`pages/portal/tablero.page.ts` y `tablero/`): `#tab-publicaciones`, `#po7-pub-tabla tr[data-publicacion]` con el título
  enlazado a `/servir/portal/novedades/:id` (solo las de la iglesia), `li[data-cifra]`, `#po7-atajo-{a}`.
- **Novedad** (`pages/portal/novedad-editar.page.ts`): `#novedad-quien` (solo si tiene reacciones), `.reac[data-codigo]`, `#btn-ver-quien`,
  `ul.personas li`; la lista sale de `portalQuienReacciono` ordenada por `r.at DESC`.
- **Bienvenida** (`pages/mi/bienvenida/portada.component.ts`; la usa `escenas/mi-iglesia/la-bienvenida.mjs`): `#bv-empezar` («Empezar mis
  primeros pasos», `po4.empezar`), «Hola, {nombre}» (`po4.hola`), `#bv-camino`, `#bv-paso-0`.
- **SQL:** `po_comunidad_personas` (única por comunidad y persona), `po_contactos` (`abierto_de` generado; uno abierto por persona y
  comunidad), `po_reacciones` (llave de publicación y persona), `po_publicacion_conteos`: migración `054_po_portal.sql`;
  `po_persona_planes.paso_dia`: `056_po_objetivos.sql`; `mem_acompanamientos.origen`: `027_mem_m10.sql` y `054`; `ev_inscritos.codigo_corto`
  (único por evento).

### 3.5 El proyecto

`recorrido-mi-iglesia/` con `BRIEF.md` (`tipo: comercial`, `subtipo: clip-del-sitio`, `recorrido: mi-iglesia`, `aspect: 16:9`), `frame.md`
(= `identidad/frame-comercial.md`), `hyperframes.json` y `package.json` copiados del clip con dos scripts: `"kit"` y `"musica"` (el `ffmpeg`
de §0.1). `assets/grabaciones/{clip,celular,escritorio}/`, `assets/stills/` (los tres del clip y el de C·buscar para el iris del 960),
`assets/audio/` (toque-b y toque-c), `assets/musica/product-launch-recorrido.wav`, `_gen/`. Composiciones: `fondo`, `frase-1` … `frase-11`,
`ceja` (con sus dos lugares); en la raíz, `#escena` con las dos ventanas y sus capas, los tramos de video, las cámaras, los iris, las marcas,
el cambio de ventana, el dip, la música y los sonidos. Si `check` avisa `composition_file_too_large`, se deja (como el clip).

**Entregables:** `renders/recorrido-mi-iglesia-16x9.mp4` (1920×1080, 30 fps, 2910 cuadros, H.264 + AAC 48 kHz, −16 LUFS) para YouTube y
presentaciones, y para la página `/mi-iglesia` una versión **1280×720** (H.264 y WebM) con su póster (el cuadro 0) en AVIF y WebP, con
`preload="none"` (lo decide la entrega del sitio).

---

## 4. Lo que se revisa en la vista previa

Cuadros a mirar: `npx hyperframes snapshot --at 0,1.5,4.0,6.0,12.5,20.1,22.1,24.0,24.5,26.6,27.9,28.0,28.1,29.0,29.6,30.0,30.6,31.0,31.6,32.0,32.2,34.6,36.0,36.3,38.0,38.6,40.0,41.6,42.0,42.6,43.9,44.0,44.5,45.6,46.0,46.2,48.5,51.9,52.0,52.3,52.8,54.5,55.9,56.0,56.6,58.0,58.6,60.0,60.2,61.5,62.5,64.0,64.5,67.9,68.0,68.5,70.0,70.5,72.0,72.6,74.0,74.6,75.9,76.0,77.0,79.9,80.2,82.5,84.0,84.5,90.0,91.9,92.0,92.4,96.9`,
y `snapshot --range` de 16 cuadros sobre cada costura: **27.8–28.3** (el corte del clip a la parte 2), **31.9–32.3** (el iris), y sobre
cada látigo **43.6–44.1, 51.6–52.1, 67.6–68.1, 75.6–76.1**.

1. **Parte 1 (0–27,9):** lo mismo que el §6 del REVIEW del clip, con la ventana del celular a la derecha y las frases a la izquierda; el texto
   de la app ≥ 28 px en todos los encuadres (el general a 1,085); **en los saltos compensados (12,97 · 15,47 · 21,5) las barras de la app no
   están en cuadro** y el cuadro anterior y el siguiente son iguales; «Su boleta, también sin señal.» entera en el 24,5; «Cerrar» entero en el
   26,6.
2. **El corte del 28,0:** el 27,9 es la boleta en grande del clip con la marca sobre «Cerrar»; el 28,0 (o el 28,03) ya es «Mis boletas» con
   «FM75UZ» y la barra; el nombre y el código no cambian entre las dos grabaciones; la frase 4 ya no está y «Encuentra» entra en el 28,07.
3. **Comunidades (28–44):** «Todavía no estás en una comunidad» legible en el 29,6; la tarjeta de Jóvenes entera en el 31,6; el iris abre
   desde el toque y descubre la comunidad ya encuadrada (32,2); «Líderes» con Andrés legible en el 34,6; el confeti de la app en el 36,3; el
   diálogo entero en el 38,6; el mensaje entero en el 41,6; «Pediste conectar con un líder» en el 42,6.
4. **Los látigos** (44,0 · 52,0 · 68,0 · 76,0): ningún cuadro con las dos ventanas vacías ni con una ventana a medio camino quieta; a la
   izquierda al escritorio, a la derecha de vuelta; la frase anterior ya no está en el golpe y la nueva empieza en el +2; la ceja cambia de
   lugar con blur, nunca se desliza.
5. **El pastor (44–52):** en el 44,5 la fila de Gabriela con «hace 1 min» y su mensaje, legible (D = 1,8); «Tomar» en cuadro en el 45,6; el
   detalle con «Lo tomó Andrés Felipe Restrepo Gómez» en el 46,2 y su mensaje y botones en el 48,5.
6. **Acompañada (52–56):** en el 52,0 **«Andrés Felipe Restrepo Gómez te acompañará»**; el punch terminado en el 52,3 (C = 1,8, el texto a
   ≥ 46 px); en el 54,5 la barra de abajo con «Objetivos» en cuadro.
7. **El objetivo (56–68):** «Paso 13 de 14 · 86 %» (o lo que diga la grabación) y «Hoy» en el 58,6; en el 60,2 «¡Listo! Marcamos…»; el anillo
   más lleno y «Paso 14 de 14» en el 62,5; «Todos los pasos» con sus ✓ en el 64,5; la cámara no se mueve mientras la app baja.
8. **El tablero y la novedad (68–76):** las cifras con «Datos de ejemplo» a la vista en el 68,5; la fila «Inscripciones abiertas» con su
   alcance y su respuesta en el 70,5; «Quién reaccionó» con 🙌 57 en el 72,6; **«Gabriela Hinestroza Perea 🙌» primera en el 74,6**, legible.
9. **La bienvenida (76–92):** el logo y «Hola, Lucía» en el 77,0 (la coreografía de la app, no del montaje); el camino en el 80,2; la frase del
   sitio entera en el 84,5 con *bolsillo* dorada y la ventana a 0,92; nada se mueve del 85,0 al 91,8 salvo el halo; dip 91,9; **92,0 el primer
   cuadro del cierre** sin noche vacía.
10. **La música (oída, no solo medida):** la costura del **32,0** no se oye (se escucha 28–36 con audífonos dos veces; el toque y el iris
    caen encima); el último acorde se apaga debajo del cierre sin cortarse; las campanas se oyen en el 92,38.
    `npx hyperframes beats assets/musica/product-launch-recorrido.wav`: la grilla de 0,5 s sigue sin un pulso doble ni uno perdido entre el
    31,0 y el 33,0.
11. **Sonido (medido):** cada `toque` y cada `aparicion` un cuadro después de su imagen; los golpes de `hyperframes audio` sobre el render en
    los toques de §1.7; **−16 LUFS** integrada (±1), pico real ≤ −1 dBTP; ningún par encimado salvo los cuatro de §1.7.
12. **Textos:** ninguna palabra que no esté en la app, en las once frases o en el cierre; las frases en sus líneas fijadas; «Datos de
    ejemplo» en cada ventana con cifras; `npx hyperframes check` en 0 errores.
13. **La historia sin sonido** (así se ve en el sitio hasta que se toca el botón): el anuncio → «Amén» → se inscribe con su esposo → la boleta
    → cierra la boleta → no tiene comunidad → Jóvenes → se une → pide un líder con su mensaje → el pastor lee ese mensaje y lo toma → «Andrés
    te acompañará» → «Lo hice» y el anillo crece → a cuántos llegó el anuncio y quién respondió: ella → alguien nuevo, con su bienvenida →
    Kingdom.

---

## 5. Riesgos y lo que se decide al grabar

- **Gabriela tiene 35 años y entra a Jóvenes** (el público de Jóvenes es de 14 a 30, así que la app no se la sugiere «Para ti»; por eso la
  app baja hasta ella en el 930). Es la comunidad de la semilla y la del congreso; la edad no se ve. Si al ver el render no convence, la
  variante es **Mujeres con una líder con cuenta**: la escena hace líder de Mujeres a la ficha de 104 y la toma la hace 104 en el escritorio
  (antes se prueba que 104 abra `/servir/portal/contactos`: la ruta pide `portal.comunidades`); 101 queda fuera de esta historia.
- **La toma del contacto se graba dos veces** (en el celular fuera de cuadro y en el escritorio en cuadro), porque cada escena restaura su
  volcado. Las dos las hace 101 sobre la misma demo y con el mismo mensaje: lo que se ve es coherente. La hora («hace 1 min») sale del `sql`.
- **La boleta de la parte 2 es la fila de la semilla ajustada** (inscrita y con el código FM75UZ del clip). Si la semilla no la inscribió
  (`refs.boleta` vacía), la escena se niega: el plan B es agregar al principio de la escena los pasos de inscripción del clip
  (`escenas/clips/mi-iglesia-boleta.mjs`, tramos `evento` a `inscrito`, fuera de cuadro) y fijar después el código con el mismo `UPDATE`.
  El QR de la lista no es el mismo dibujo que el de la boleta en grande del clip (el token cambia); se ve 1 s, a la mitad del tamaño, después
  de un cambio de pantalla: se acepta y se anota.
- **«Hoy» depende del día de la iglesia:** el `sql` fija `paso_dia` en hoy con el desfase de Bogotá (−05:00). Si Kingdom Demo tuviera otra
  zona, se cambia el desfase; `refs.hoy` se niega si no quedó. Después de «Lo hice» el motor calcula el paso siguiente: si queda «Atrasado»
  (la semilla la dejó irregular), se elige otro objetivo o se anota.
- **La bienvenida de 104** depende de que su público tenga pasos visibles; si no los tiene, `/mi/bienvenida` la manda al Inicio y la espera
  de `#bv-empezar` falla. Plan B: la cuenta 106 con el mismo `DELETE`.
- **Los desplazamientos de la app pueden ser saltos** (como en el clip, REVIEW §4.2): 930, 1920 y 2100 se ven en su pulso con su `desliz` y la
  cámara quieta (1920 y 2100: la cámara salta con la app en el mismo cuadro, que es un corte). Los `ver` fuera del montaje no importan.
- **El confeti** depende del modo ligero y de `prefers-reduced-motion` de la app: si no sale en la grabación, se graba otra vez; no se agrega.
- **El escritorio se lee solo de cerca** (D = 1,8 deja ver 711 × 375 px CSS): cada encuadre (la fila, «Tomar», el detalle, las cifras, la
  fila de la tabla, «Quién reaccionó», la lista) se elige con la grabación y se anota en el REVIEW.
- **Densidad de frases:** once en 92 s; la 7 vive 4 s (1560–1679) y tiene cinco palabras (≥ 2,0 s de lectura): alcanza. Si en la vista
  previa se siente atropellado, la válvula es que la frase 6 («Su mensaje llega a los líderes.») no entre y la ceja sola acompañe el
  escritorio hasta el 1560.
- **La costura de la música** está medida dos veces (Academia y aquí), pero nadie la ha oído: es lo primero que se escucha en la vista previa
  (§4.10).
- **El README pide 60–75 s para el recorrido**; este dura 97 por decisión del dueño (~100 s, como los otros tres). Se anota en
  `KingdomApp/docs/videos/README.md` al publicar.
- **Idiomas (en, pt después):** las dos escenas con `--idioma en` graban la interfaz en inglés («Young adults», «Registration is open»); el
  nombre de Gabriela y el código FM75UZ no cambian; las frases se traducen y los saltos se vuelven a fijar; el cierre lleva `idioma`.
