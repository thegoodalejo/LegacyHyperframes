# SPEC · Recorrido del módulo: Membresía — «Valeria llegó el domingo… y así con toda la iglesia»

2026-10-30 · Contrato de construcción de [STORY.md](STORY.md). El dueño ya no revisa guiones: esto se construye tal cual, se revisa contra
esto y se cambia aquí cuando la vista previa cambie la película. Hereda **todo** el sistema del clip ([SPEC v2](../clip-sitio-membresia/SPEC.md),
[REVIEW](../clip-sitio-membresia/REVIEW.md)): la paleta, las letras, las curvas, la ventana, las marcas de toque, el látigo en una tira, las
entradas un cuadro antes del pulso, los niveles del kit con +3 dB en los toques clave y la regla de los 28 px. **Del cuadro 0 al 959 el
cuerpo es el del clip** (mismos tramos de video, mismos toques, mismas frases 1–4, mismos sonidos) reencuadrado en 16:9; lo nuevo empieza en
el 960.

```text
GOAL:    Un pastor que no conoce Kingdom termina pensando «a Valeria la llamaron y tiene un camino; y yo veo así a cada persona de mi
         iglesia» y toca «Prueba gratis 30 días».
OUTPUT:  HyperFrames 0.8.221 · 1920×1080 (16:9: la página /membresia del sitio, YouTube, presentaciones) · 30 fps.
TIME:    97,0 s = 2910 cuadros: cuerpo 0–92,0 (cuadros 0–2759) + cierre-comercial 92,0–97,0 (2760–2909). 120 BPM = 15 cuadros por pulso,
         60 por compás; la grilla del video en §0.3 (48 compases).
LOOK:    la noche del sitio (#060D1F) con el halo y la retícula de puntos del kit; tinta #EAF0FF; un solo acento, el dorado #E8B95A, en tres
         papeles y no más (las cejas de capítulo, la palabra «ninguna», el botón del cierre). Fraunces 560 / −0,02 em para las frases (88 px
         en los mundos de celular, 84 px en los de escritorio); Inter 700 para las cejas; Inter 600 para «Datos de ejemplo». El medio: la app
         REAL de Kingdom Demo, grabada en celular (1170×2532) y en escritorio (1920×1080), dentro de UNA ventana (.k-ventana: anillo de 1 px,
         sombra 0 40 80 −24 al 70 %) que cambia de forma: 720×900 radio 28 a la derecha (celular) ↔ 1440×760 radio 20 abajo al centro
         (escritorio). Nunca un teléfono ni un monitor dibujado.
OBJECTS: la ventana (el celular de Jorge en el acto 1; el escritorio de Andrés en C1 y C4; el celular de Andrés en C2 y C3); el punto de
         toque de cada grabación; las nueve frases; las cinco cejas; la píldora «Datos de ejemplo»; la corona del cierre. Nada más.
MOTION:  curvas por papel (§1.5); un movimiento de cámara por compás (14 cuadros, power2.inOut), quieta después; cada toque y cada entrada
         en un pulso; cada cambio de mundo en un golpe (1080 · 1560 · 1920 · 2280 · 2760) con la ventana que cambia de forma o el látigo.
SHOTS:   trece planos (§2.7).
BANNED:  §1.7.
QA:      §4.
```

---

## 0. La música: la edición y la grilla

«Product Launch» (The_Mountain, `kit.json` → `musica.biblioteca.product-launch`): 86,05 s, 120 BPM, compases de 2 s desde el 2,05. La
historia del clip usa 14,05 → 50,05; el recorrido necesita ~92 s de cuerpo. **Se alarga repitiendo una vez el bloque respiro + segunda
subida + clímax (26,05 → 66,05, 40 s) y se cierra con el final real de la pista (82,05 → 86,05).**

### 0.1 La edición, exacta

Tres elementos `<audio>` de la misma pista (`assets/musica/product-launch-the-mountain.mp3`), en dos carriles para que puedan encimarse dos
cuadros. Volúmenes absolutos en el carril de volumen (`data-automation`, como el clip: REVIEW §4.9 de la v1); 0,7 = −18 LUFS.

| Id | Carril | `data-start` (video) | `data-media-start` (pista) | `data-duration` | Suena | Volumen |
|---|---|---|---|---|---|---|
| `musica-a` | 10 | **0** | **14,05** | **52,0** | pista 14,05 → 66,05 = video 0 → 52,0 | 0,7 constante; **0,7 en 51,933 → 0 en 52,000** (2 cuadros, lineal) |
| `musica-b` | 11 | **51,933333** | **25,983333** | **40,066667** | pista 25,983 → 66,05 = video 51,933 → 92,0 | **0 en 51,933 → 0,7 en 52,000**; 0,7 constante; **0,7 en 91,933 → 0 en 92,000** |
| `musica-c` | 10 | **91,933333** | **81,983333** | **4,066667** | pista 81,983 → 86,05 (fin del archivo) = video 91,933 → 96,0 | **0 en 91,933 → 0,7 en 92,000**; 0,7 hasta **92,20** → **0,25 en 92,40** (−9 dB, debajo de las campanas del 92,38) y así hasta el final; la pista se apaga sola (−36 LUFS en su 84,0, silencio en su 86,0) |

- **Los dos empalmes** caen en la cabeza de un compás: video **52,0** (pista 66,05 → 26,05) y video **92,0** (pista 66,05 → 82,05). El cruce
  de 2 cuadros ocurre **antes** de la cabeza (51,933–52,000 y 91,933–92,000): en el cuadro del golpe ya suena solo el segmento que entra, con
  su ataque entero. Los dos lados del cruce son la cola del cuarto compás de un ciclo, contenido parecido: no hay clic ni hueco.
- **Fórmulas** (segundos de la pista ↔ del video): `musica-a` pista = video + 14,05; `musica-b` pista = video − 25,95; `musica-c` pista =
  video − 9,95.
- **Lo que se oye:** entrada sin bajo → el bajo (4,0) → primera subida → respiro (12) → segunda subida con el 42,05 (28,0) → **clímax**
  (36) → **respiro** (52, el empalme suena a cambio de arreglo: del clímax al respiro, como en la pista del primer subidón al respiro) →
  segunda subida con el 42,05 **otra vez** (68,0) → **clímax otra vez** (76) → **el golpe final** de la pista y su cola (92, el cierre).

### 0.2 Por qué así (medido el 2026-10-30, no oído)

- **Los ciclos de 4 compases.** Todas las secciones de la pista empiezan en un compás ≡ 1 (mód 4) contado desde el 2,05: 2,05 (c1), 18,05
  (c9), 26,05 (c13), 34,05 (c17), 50,05 (c25), 66,05 (c33), 82,05 (c41). Los dos empalmes saltan del final del compás 32 (el cuarto de un
  ciclo) al compás 13 y al 41 (el primero de un ciclo): la armonía y la frase siguen.
- **La grilla del clímax.** `product-launch-the-mountain.pulsos.json` marca los pulsos en x,05 / x,55 hasta el 52,05 y en x,30 / x,80 del
  52,53 al 79,78 (con un redoble 52,53 · 52,98 · 53,41 · 53,87), y vuelve a x,05 en el 82,05. La pista no cambia de fase: el detector se
  engancha a los **contratiempos** (los sintetizadores del clímax van en corcheas a contratiempo). Lo prueban (a) la sonoridad momentánea por
  medio segundo, cuyos máximos del clímax caen en **54,0 · 58,0 · 62,0** (−11,8 / −11,8 / −11,9 LUFS), las cabezas de frase de 2 compases
  en la grilla x,05; (b) el plegado de los ataques módulo 0,5 s, que en el clímax da dos picos casi iguales (tiempo y contratiempo); (c) el
  final en el 82,05, exacto en la grilla de los tiempos (40 compases desde el 2,05). **Decisión: el video corta y cambia en la grilla x,05 en
  toda la pista; nunca en un contratiempo.**
- **Golpes del clímax** (sin pulso del detector en la grilla): cabeza 50,05 (0,93) · 52,05 (0,81) · **54,05** · **58,05** · **62,05** (las
  tres cabezas fuertes por sonoridad) · 56,05, 60,05 y 64,05 más suaves.
- **El final real** de la pista es un golpe en el 82,05 (ataque más fuerte que el del 42,05 en la medición de ataques) con una cola que se
  apaga: −15,8 LUFS en 82,0, −25,9 en 83,0, −36,1 en 84,0, silencio en 86. Es el cierre natural de la música, y queda bajo la corona.
- **Descartado:** dejar sonar la salida (66–82) bajo las capacidades (baja la energía justo cuando el recorrido crece y obliga a un final con
  fundido); repetir solo el clímax dos veces seguidas (el mismo brillo 32 s, sin respiro, y sin el 42,05 para la pirámide); empezar la pista
  antes del 14,05 (rompe la sincronía del acto 1 con el clip).

### 0.3 La grilla del video (48 compases)

Cuadro = segundo × 30; cada pulso se calcula desde su índice (múltiplos de 15), salvo el **284** del acto 1 (el 9,455 de la pista, ya en el
clip). Fuerza = la del mapa de pulsos; en el clímax, «cabeza» = cabeza de frase fuerte por sonoridad (§0.2). **Negrita** = golpe usado para un
cambio grande.

| Compás | Cuadros | Pista | Sección | Pulsos (cuadro · fuerza) | Lo que le toca al video |
|---|---|---|---|---|---|
| 1–18 | 0–1079 | 14,05–50,05 | la del clip | la grilla del [SPEC del clip §0](../clip-sitio-membresia/SPEC.md#0-el-reloj-la-grilla-real-de-la-pista) | **El acto 1** (§2.1). Golpes **120 · 180 · 600 · 660 · 720 · 780 · 840 · 960** |
| 19 | 1080–1139 | 50,05 | clímax | **1080 ·0,93** · 1095 ·0,84 · 1110 · 1125 | **Cambio de mundo al escritorio**; ceja «COORDINAR»; frase 5 |
| 20 | 1140–1199 | 52,05 | clímax | 1140 ·0,81 · 1155 ·0,95 · 1170 · 1185 | Toque en «Nuevos»; la cámara a la lista y «Repartir» |
| 21 | 1200–1259 | 54,05 | clímax | **1200 · cabeza** · 1215 · 1230 · 1245 | **Toque en «Repartir»**: el diálogo; la cámara al texto |
| 22 | 1260–1319 | 56,05 | clímax | 1260 · 1275 · 1290 · 1305 | Toque en «Repartir» del diálogo |
| 23 | 1320–1379 | 58,05 | clímax | **1320 · cabeza** · 1335 · 1350 · 1365 | **«Se repartieron N personas.»** |
| 24 | 1380–1439 | 60,05 | clímax | 1380 · 1395 · 1410 · 1425 | Toque en «Quienes acompañan» |
| 25 | 1440–1499 | 62,05 | clímax | **1440 · cabeza** · 1455 · 1470 · 1485 | Las barras de carga |
| 26 | 1500–1559 | 64,05 | clímax | 1500 · 1515 · 1530 · 1545 | Vuelta al plano; la frase sale |
| 27 | 1560–1619 | **26,05** (empalme) | respiro | **1560 ·0,76** · 1575 ·0,64 · 1590 · 1605 | **Cambio de mundo al celular**; ceja «SEMÁFORO DE ACTIVIDAD»; frase 6 |
| 28 | 1620–1679 | 28,05 | respiro | 1620 ·0,75 · 1635 ·0,61 · 1650 · 1665 | «Agregar filtro»; la hoja; «Semáforo de actividad» |
| 29 | 1680–1739 | 30,05 | respiro | 1680 ·0,67 · 1695 ·0,67 · 1710 · 1725 | Los cuatro colores; toque en «Rojo» |
| 30 | 1740–1799 | 32,05 | respiro | 1740 ·0,63 · 1755 · 1770 ·0,61 · 1785 ·0,68 | «Aplicar»: la lista en rojo |
| 31 | 1800–1859 | 34,05 | 2.ª subida | **1800 ·0,93** · 1815 ·0,69 · 1830 · 1845 | **Toque en una persona: su ficha** |
| 32 | 1860–1919 | 36,05 | 2.ª subida | **1860 ·0,90** · 1875 ·0,89 · 1890 ·0,76 · 1905 ·0,68 | «Actividad: Rojo · hace N días» |
| 33 | 1920–1979 | 38,05 | 2.ª subida | **1920 ·0,96** · 1935 ·0,77 · 1950 · 1965 | **Látigo vertical: el discipulado**; ceja; frase 7 |
| 34 | 1980–2039 | 40,05 | 2.ª subida | 1980 ·0,88 · 1995 ·0,74 · 2010 · 2025 | La cámara a la primera cabeza de la pirámide |
| 35 | 2040–2099 | **42,05** | 2.ª subida | **2040 ·1,00 (el más fuerte)** · 2055 ·0,68 · 2070 · 2085 | **Toque: la pirámide se abre** |
| 36 | 2100–2159 | 44,05 | 2.ª subida | 2100 ·0,84 · 2115 ·0,82 · 2130 ·0,75 · 2145 | «N directos · M en total» y sus discípulos |
| 37 | 2160–2219 | 46,05 | 2.ª subida | **2160 ·0,98** · 2175 ·0,74 · 2190 · 2205 | **Toque: un nivel más abajo** |
| 38 | 2220–2279 | 48,05 | 2.ª subida | 2220 ·0,79 · 2235 ·0,75 · 2250 · 2265 | Las migas; la frase sale |
| 39 | 2280–2339 | 50,05 | clímax | **2280 ·0,93** · 2295 ·0,84 · 2310 · 2325 | **Cambio de mundo al escritorio: el tablero**; ceja; frase 8 |
| 40 | 2340–2399 | 52,05 | clímax | 2340 ·0,81 · 2355 ·0,95 · 2370 · 2385 | La cámara al semáforo de actividad |
| 41 | 2400–2459 | 54,05 | clímax | **2400 · cabeza** · 2415 · 2430 · 2445 | Acercamiento a la barra y a «Rojo» |
| 42 | 2460–2519 | 56,05 | clímax | 2460 · 2475 · 2490 · 2505 | La descarga: «PDF · Excel» |
| 43 | 2520–2579 | 58,05 | clímax | **2520 · cabeza** · 2535 · 2550 · 2565 | El crecimiento |
| 44 | 2580–2639 | 60,05 | clímax | 2580 · 2595 · 2610 · 2625 | Acercamiento al final de la curva |
| 45 | 2640–2699 | 62,05 | clímax | **2640 · cabeza** · 2655 · 2670 · 2685 | **Frase 9: «Que *ninguna* persona se pierda»** |
| 46 | 2700–2759 | 64,05 | clímax | 2700 · 2715 · 2730 · 2745 | La cámara abre; la `subida`; el dip 2757–2759 |
| 47–48+ | 2760–2909 | **82,05** (empalme) | final | **2760 ·0,57** (el golpe final) | **El cierre**; campanas en el 2771 (92,38) |

---

## 1. Los números del estilo

### 1.1 Paleta

La del clip (SPEC del clip §1.1), sin un color más: `--k-noche` #060D1F a sangre; `.k-halo` y `.k-puntos` del kit (los puntos nunca se
mueven); tinta `--k-noche-tinta` #EAF0FF para las frases; dorado `--k-noche-dorado` #E8B95A **solo** en las cejas, en *ninguna* y en el botón
del cierre; anillo `--k-noche-linea`; fondo de la ventana `--k-app-fondo` #FAF9FD (no se ve salvo en un cuadro de carga); placa de «Datos de
ejemplo» rgba(6,13,31,.72); dip rgba(6,13,31,.40). Los colores de la app (los puntos del semáforo, el azul #015BBE de los botones, la barra
del tablero) viven en la grabación y no se tocan.

### 1.2 Tipografía (16:9)

| Pieza | Clase | Letra | Tamaño | Interlínea · tracking | Reglas |
|---|---|---|---|---|---|
| Frase en mundo de celular | `.k-titular` | Fraunces 560; `<em>` itálica 500 dorada | **88 px** | 1,04 · −0,02 em | **2 líneas** con el salto fijado a mano; a la izquierda; `text-wrap: balance` apagado; sin sombra |
| Frase en mundo de escritorio | `.k-titular` + `font-size: 84px` | ídem | **84 px** | 1,04 · −0,02 em | **1 línea**, máx. 1440 px de ancho medido; si pasa, 80 px (nunca menos de 76 ni 2 líneas) |
| Ceja | `.k-ceja` | Inter 700, MAYÚSCULAS, dorado | **28 px** | 1 · +0,10 em | Una por capítulo: «MEMBRESÍA», «COORDINAR», «SEMÁFORO DE ACTIVIDAD», «DISCIPULADO», «TABLEROS» |
| Datos de ejemplo | `.k-datos-ejemplo.k-feed-datos` | Inter 600 | **28 px**, píldora de 52 px | — | Dentro de la ventana, abajo a la izquierda a 24 px, **desde el cuadro 0 hasta el 2759** (viaja con la ventana cuando cambia de forma). Se usa la de 28 px y no la de 22 px de 16:9 porque el recorrido también se ve en el celular (YouTube) |
| Texto de la app | (grabación) | Inter de la app, 14 px CSS el cuerpo | **≥ 28 px** en todo encuadre (§1.4) | — | El texto de 12 px CSS (los grises) puede quedar en 24–27 px, nunca siendo lo que el plano muestra |

Saltos fijados: «Valeria llegó / el domingo.» · «Registrada. / Aun sin señal.» · «Y ya tiene quién / la llame» · «Y una ruta / para crecer» ·
«Ves a tiempo / quién se aleja» · «Quién discipula / a quién». En una línea: «Nadie nuevo se queda sin llamada» · «Tu iglesia, de un vistazo» ·
«Que *ninguna* persona se pierda».

### 1.3 Disposición: una ventana, dos formas

| | Mundo de celular (acto 1, C2, C3) | Mundo de escritorio (C1, C4) |
|---|---|---|
| Ventana | `.k-ventana.k-ventana-16x9`: **left 1104 · top 90 · 720×900 · radio 28** (termina en 1824 × 990) | `.k-ventana.k-ventana-escritorio`: **left 240 · top 260 · 1440×760 · radio 20** (termina en 1680 × 1020) |
| Ceja | x 120 · y 428 (28 px → 456) | x 240 · y 76 (→ 104) |
| Frase | x 120 · y 476 · ancho 888 · 2 líneas de 91,5 px → 659 (el bloque ceja + frase queda centrado en el alto del cuadro, 428–659) | x 240 · y 118 · ancho ≤ 1440 · 1 línea → 205; 55 px de aire hasta la ventana |
| Lo que ocupa la ventana | 47 % del ancho y 83 % del alto | 75 % del ancho y 70 % del alto |

Cada frase y cada ceja es su propio elemento en su posición (las del escritorio no son las del celular movidas): ningún texto se desplaza.
La ventana **sí** cambia de forma en los cambios de mundo (§1.5, `morph`): se interpolan `left`, `top`, `width`, `height` y `border-radius`
del mismo `.k-ventana` (propiedades de caja, deterministas; nunca `scale` sobre la ventana).

### 1.4 La cámara dentro de la ventana: niveles

La cámara es `scale` + `x`/`y` sobre el envoltorio de cada mundo (`.k-ventana-camara`); el `<video>` nunca se transforma. Se mide en **ppc =
píxeles del cuadro por píxel CSS de la app**. Cada encuadre centra una **caja de `pasos.json`** (px CSS del viewport) y se sujeta a los
bordes de la grabación (nunca se ve fuera de ella).

**Celular** (ventana 720×900; grabación de 390×844 CSS a 3×; el ajuste al ancho daría 1,846 ppc = 25,8 px: no alcanza):

| Nivel | Ancho visible (CSS) | ppc | Escala sobre el ajuste al ancho | Alto visible (CSS) | Cuerpo 14 px → | Ampliación de la fuente |
|---|---|---|---|---|---|---|
| **G16** (el plano de reposo) | **360** | **2,000** | 1,0833 | 450 | **28,0 px** | 0,67× (nítida) |
| **F16** (la ficha: textos de x 32 a 357) | 339 | 2,124 | 1,1504 | 424 | 29,7 px | 0,71× |
| **M16** | 279 | 2,581 | 1,3978 | 349 | 36,1 px | 0,86× |
| **C16** | 217 | 3,318 | 1,7972 | 271 | 46,5 px | 1,11× |

**Del clip al recorrido:** cada encuadre del clip se traduce **conservando su ancho visible en px CSS** (ppc16 = 720 / ancho visible del
clip), con piso G16: el G del clip (390 de ancho) pasa a G16 (360, se recortan 15 px por lado: la tarjeta va de x 16 a 374 y cabe), su G⁺
(361) a G16, su M (279) a M16, su C (217) a C16, sus ×1,15 de la ficha (339) a F16, su ×1,35 (289) a 2,49 ppc y su punch ×1,5 (260) a 2,77
ppc. La ventana de 16:9 ve **más alto** que la de 4:5 en cada nivel (450 contra 439 CSS en G): ningún objetivo del clip queda cortado.

**Escritorio** (ventana 1440×760; grabación de 1280×720 CSS a 1,5× = 1920×1080). El escritorio se muestra **siempre como recorte**; la pantalla
entera (1,125 ppc, 15,8 px) está prohibida:

| Nivel | Visible (CSS) | ppc | Escala del `<video>` (base 2560×1440) | Cuerpo 14 px → | Ampliación de la fuente |
|---|---|---|---|---|---|
| **D** (reposo) | **720 × 380** | **2,000** | 1,000 | **28,0 px** | 1,33× |
| **D⁺** (acercamiento) | 640 × 338 | 2,250 | 1,125 | 31,5 px | **1,50× (el máximo; nunca más)** |

Encuadre (la `enc()` del clip, con origen 0 0): para poner el punto `(cx, cy)` en px CSS en el centro de una ventana `W × H` con `p` ppc,
`x = W/2 − p·cx` e `y = H/2 − p·cy`, sujetos a `W − p·anchoCSS ≤ x ≤ 0` y `H − p·altoCSS ≤ y ≤ 0` (la grabación nunca deja ver el fondo).
Escritorio: `W = 1440`, `H = 760`, `anchoCSS = 1280`, `altoCSS = 720`. Celular: `W = 720`, `H = 900`, `anchoCSS = 390`, `altoCSS = 844`, más
el desplazamiento de cada mundo (`off`) como en el clip.

### 1.5 Curvas y duraciones (cada tween con su curva por nombre)

| Papel | Curva | Cuadros | Detalle |
|---|---|---|---|
| `entrada-palabra` | `power4.out` | 4 | `blur(6px) → 0` + opacidad 0 → 1, **sin desplazamiento**; palabras a 2 cuadros (0,067 s), salvo la frase 1 (una por pulso, el clip). Arranca un cuadro antes del pulso: el primer cuadro visible es el pulso |
| `entrada-linea` | `power4.out` | 6 | la línea entera, blur 8 → 0 (frase 2 y cejas) |
| `salida-texto` | `power3.in` | 4 | blur 0 → 8 + opacidad 1 → 0, la línea entera; empieza 3 cuadros antes del pulso (blur swap) |
| `camara` | `power2.inOut` | **14** | uno por compás; después quieta |
| `punch` | `power2.inOut` | **9** | los del 660 (clip), 1320, 1860, 2100, 2400 |
| `morph` (la ventana cambia de aparato) | `power3.inOut` | **12** | `left/top/width/height/border-radius` de la ventana entre las dos formas de §1.3, **centrado en el golpe**: 1074–1086, 1554–1566, 2274–2286. El cuadro más rápido es el del golpe |
| `cambio-contenido` (dentro del morph) | `power3.in` / `power3.out` | 6 + 6 | el mundo que se va: `x` 0 → −160 (salida, 6 cuadros antes del golpe); en el golpe **corte duro** de contenido (el que se va a `opacity: 0` con `set`, el que llega visible); el que llega: `x` +160 → 0 y escala 1,04 → 1,00 (`power3.out`, 10 cuadros). Con el desenfoque de movimiento, el corte cae en el cuadro más borroso |
| `latigo` (mismo celular) | `power3.inOut` | 10 | una tira, como el clip: 176–186 (acto 1) y **1914–1924** (C2 → C3, la tira sube `--f-latigo` = 1000 px); el que llega aterriza 1,04 → 1,00 (`power3.out`, 1920–1930) |
| `iris` | `power2.out` | 5 | `clip-path: circle(0 at X Y) → circle(1900px at X Y)` desde el centro del toque. Irises: 120, 375, 780 (clip) · **1200** (el diálogo de «Repartir») · **1800** (la ficha) · **2040** y **2160** (la pirámide) |
| `halo` | `sine.out` | 90 | 1,08 → 1,00 al entrar cada mundo: **0, 180, 780, 1080, 1560, 1920, 2280, 2640** |
| `dip` | escalón | 3 | `rgba(6,13,31,.40)` sobre la ventana, **2757–2759** |
| cierre | las del kit | 150 | `cierre-comercial`; **no se imita en el cuerpo** |
| resortes | ninguno | — | nada rebota salvo la corona del kit |
| velocidad de la grabación | `data-playback-rate` por tramo | — | **0,35× a 3,5×**; las rampas entre acciones, nunca durante un toque, una letra o un desplazamiento de la app |

Desenfoque de movimiento: `data-motion-blur="on"` y `data-motion-blur-shutter="180"` en la raíz (morph, látigo, cámara). **Nunca `filter:
blur()` sobre una grabación**; el blur de CSS es solo para el texto.

### 1.6 Sonido

| Capa | Fuente | Nivel | Regla |
|---|---|---|---|
| Música | §0.1 (tres segmentos) | 0,7 = −18 LUFS; bajo el cierre 0,25 | Los empalmes con cruce de 2 cuadros antes de la cabeza |
| Sonidos de acción (kit v1.1) | `toque` 75 ms · `aparicion` 220 ms · `desliz` 360 ms (acento 0,2) · `confirmacion` 320 ms (acento 0,1) · `subida` 1,9 s (acento 1,5) | `data-volume="1"`; **1,4 (+3 dB) en los marcados (+)** | El pico suena **un cuadro después** de su imagen: `data-start` = (cuadro del sonido / 30) − acento. Tres tomas rotadas de `toque` (a = `toque.wav`, b = +3 %, c = −3 % de tono: las del clip), de `aparicion` y de `desliz` (b y c nuevas, hechas igual que las de `toque`). **Sin tics de tecla** |
| Sonido de marca | `sonido-marca.wav` (campanas, −20 LUFS) | tal cual | En **92,38** (cuadro 2771): el inicio del cierre + 0,38 (`kit.json` → `piezas.cierre-comercial.sonido`) |
| Mezcla | — | **−17 a −16 LUFS** integrados, pico real **≤ −1 dBTP** | Medido con `npx hyperframes audio <render> --json`; si al normalizar el pico pasa de −1 dBTP, se limita o se bajan los 1,4 a 1,2 (lección del clip, REVIEW §6) |

**Los sonidos, en orden (cuadro del pico):**

- **Acto 1, los del clip sin cambios:** toque a 61 · toque b 91 · aparicion 109 · desliz 109–120 · toque c 121 (+) · confirmacion 123 (+) ·
  toque a 151 · aparicion 166 · desliz 174–185 (+, el látigo) · aparicion 196 (la ceja) · toque b 376 · toque c 451 · toque a 496 · toque b
  601 (+) · confirmacion 603 (+) · toque c 721 · toque a 781 · toque b 841 (+) · aparicion 843 (+). **Se quita la `subida` del clip
  (1036–1093)**: la única subida del recorrido va al cierre.
- **1080:** desliz a (+), pico 1080 (`data-start` 35,8).
- **C1:** aparicion a 1087 (la ceja) · toque c 1141 («Nuevos») · **toque a 1201 (+, «Repartir»)** · aparicion b 1204 (el diálogo) · toque b
  1291 («Repartir» del diálogo) · **confirmacion 1321 (+, «Se repartieron»)** · toque c 1381 («Quienes acompañan»).
- **1560:** desliz b, pico 1560.
- **C2:** aparicion b 1567 · toque a 1621 («Agregar filtro») · toque b 1666 («Semáforo de actividad») · toque c 1711 («Rojo») · toque a 1741
  («Aplicar») · aparicion c 1744 (el chip y la lista en rojo) · **toque b 1801 (+, la persona)**.
- **1920:** desliz c, pico 1920 (el látigo vertical).
- **C3:** aparicion c 1927 · **toque c 2041 (+, la cabeza de la pirámide)** · **aparicion a 2044 (+, la pirámide abierta)** · toque a 2161 (un
  nivel más).
- **2280:** desliz a (+), pico 2280.
- **C4:** aparicion a 2287 · toque b 2491 (la descarga) · aparicion b 2494 (el menú «PDF · Excel»).
- **Cierre:** `subida` con su golpe en el **2761** (`data-start` 90,533333) · campanas en el **2771** (92,38).

**46 eventos en 97 s, ninguno sin causa visible.** Ningún whoosh en los movimientos de cámara ni en los irises (el toque basta); el `desliz`
solo en los cuatro cambios de mundo y en el látigo del acto 1, rotado. Dos sonidos encimados solo en 121 + 123, 601 + 603, 841 + 843, 1201 +
1204, 2041 + 2044 y 2491 + 2494.

### 1.7 BANNED: los valores por defecto prohibidos, con nombre

1. **El fundido de 0,5 s con `power2.out` para todo.** Cada tween con su curva de §1.5; nada entra solo por opacidad.
2. **Fade + deslizarse hacia arriba** en el texto. Las palabras entran por blur, sin moverse.
3. **Zoom lineal**, `linear` en la cámara, **el acercamiento lento y arrastrado** (creeping scale) en cualquier tramo.
4. **Fundido cruzado entre mundos.** Solo: iris desde el toque, látigo (vertical en el mismo celular), morph con corte duro de contenido en su
   cuadro más rápido (cambio de aparato), dip + corte (al cierre).
5. **Teléfono o monitor dibujado** (también `.k-telefono`), bisel, barra de estado inventada, marco de navegador.
6. **El escritorio entero dentro de la ventana** (1,125 ppc, texto de 15,8 px). Siempre recorte D o D⁺.
7. **Una lista de funciones en pantalla**: viñetas, tarjetas con íconos de cada capacidad, «01 / 02 / 03», rejillas de KPI **dibujadas** por
   nosotros, título sobre una captura oscurecida. (Las cifras del tablero son la app real y se muestran como la app las muestra.)
8. **Cada capítulo entrando igual.** Los cuatro cambios de mundo alternan morph a escritorio, morph a celular, látigo vertical y morph a
   escritorio; el iris solo nace de un toque.
9. **Texto que se mueve mientras se lee**; frases que derivan después de aterrizar; «breathing» en frases, cejas o ventana.
10. **El logo en una esquina**, marca de agua, la corona antes del cuadro 2760.
11. **Brillo, neón, destellos, partículas, orbes, degradados nuevos, vidrio.** El halo del kit se asienta una vez por mundo y no late.
12. **Whoosh en cada corte** o en los movimientos de cámara; el mismo `toque`, `aparicion` o `desliz` sin rotar; dings ajenos al kit.
13. **Reproducción de la app por encima de 3,5× o por debajo de 0,35×.**
14. **Retocar un píxel de la app**: resaltados, flechas, cursor dibujado, animar lo que la app no anima (ni la barra del semáforo, ni la curva
    del crecimiento, ni los nodos de la pirámide). El punto de toque sale de `toques[]` de la grabación.
15. **Texto de la app por debajo de 28 px** como sujeto de un plano (§1.2).
16. **Centrarlo todo.** Las frases a la izquierda del margen de su mundo; solo la ventana del escritorio va centrada.
17. **Cifras sin «Datos de ejemplo»**: la píldora está del cuadro 0 al 2759.
18. **Más de 3 s sin un cambio visible** en el cuerpo. El tramo más quieto es 2715–2756 (1,4 s).
19. **Un compás sin toque ni movimiento de cámara** entre el 1080 y el 2759.
20. **Un desplazamiento de la app a la vista con la cámara quieta**: todo desplazamiento real de una grabación cae dentro de un movimiento de
    cámara (1170, 2340, 2520, 2640), como el salto a «Registrar» del clip.
21. **Un corte de música fuera de la cabeza de un compás**, un fundido de música audible a mitad de compás, o cortar en un contratiempo del
    clímax.
22. Del contrato de HyperFrames: `from()` en escenas (siempre `fromTo`), `autoAlpha`/`display` sobre un `.clip`, `transform` de CSS en un
    elemento que GSAP transforma, el `<video>` y su envoltorio con tiempo a la vez.

Después del primer render, cada valor por defecto que aparezca se nombra aquí y se corrige.

---

## 2. Los planos, cuadro por cuadro

> **Construido el 2026-10-30.** Lo que trajeron las grabaciones (cifras reales, cuadros de cada cambio, desplazamientos) y los encuadres que
> cambiaron al construir están en [REVIEW.md](REVIEW.md) §3–§5; donde esta tabla y el REVIEW difieren, manda el REVIEW (es lo que está en
> `index.html`, generado por `_gen/gen.py`).

### 2.0 Convenciones

- **G16 / F16 / M16 / C16** (celular) y **D / D⁺** (escritorio): §1.4. «Sobre X» = la caja de X centrada en la ventana.
- **Pulso**: un evento «en el 1200» aterriza en el cuadro 1200 (su sonido, en el 1201).
- **Grabaciones:** **G1** y **G2** = las del clip (§3.1); **R1** coordinar, **R2** semáforo, **R3** discipulado, **R4** tableros = las nuevas
  (§3.2). «R1·`nuevos`» = el tramo de esa escena; «toques[0]» = el cuadro del dedo apoyado en ese paso de su `pasos.json`.
- **Textos de la app:** verificados en `frontend-v2/public/i18n/es.json` y en los componentes de `frontend-v2/src/app/pages/membresia/`. Las
  cifras, los nombres de las personas y el vocabulario de la iglesia (`{v_acompanante}`, `{v_discipulado}`) salen de Kingdom Demo y llevan
  «(real)»: se leen en la grabación.
- **Corte de esperas:** como en el clip, la espera real entre un toque y su resultado se corta para que el resultado completo caiga en el
  cuadro indicado; si la espera es más corta, el cuadro anterior al resultado se estira con una tasa de 0,35–1×.

### 2.1 Acto 1 · «Valeria llegó el domingo» — cuadros 0–1079 (compases 1–18)

**Igual que el clip** ([SPEC v2 §2.1](../clip-sitio-membresia/SPEC.md#21-tabla-maestra-todo-lo-que-cambia-por-cuadro) y
[REVIEW v2 §2–3](../clip-sitio-membresia/REVIEW.md)) del cuadro 0 al 959: los 29 tramos de video (G1 `v01`–`v25`, G2 `v26`–`v29`) con sus
`data-start`, `data-media-start` y tasas **sin cambios**, los stills del 466 y del 2401 bajo los irises, las marcas de toque, el látigo vertical
176–186, los irises 120, 375 y 780, las frases 1–4 con sus cuadros, la ceja «MEMBRESÍA» (entra 195) y los 19 sonidos. Lo que cambia:

| Pieza | Clip (4:5) | Recorrido (16:9) |
|---|---|---|
| Disposición | ventana 880 × 1050 desde (100, 360), frases arriba | ventana `.k-ventana-16x9` 720×900 en (1104, 90); ceja y frase a la izquierda (§1.3) |
| Variables de formato | `--f-ventana-w` 880, `--f-ventana-hvis` 990, `--f-k` 0,752137, `--f-grab-alto` 1904,41, `--f-latigo` 1100 | **`--f-ventana-w` 720, `--f-ventana-h` 900, `--f-ventana-hvis` 900, `--f-k` 0,615385, `--f-grab-alto` 1558,15 px, `--f-latigo` 1000**; `window.KD.ventana = { w: 720, h: 900, hVis: 900 }`, `latigo: 1000` |
| Cámara | niveles G / G⁺ / M / C del clip | **los mismos objetivos** con el ancho visible conservado (§1.4); el reposo (lo que en el clip era escala 1, x 0, y 0) es **G16** = `enc(1,0833, 195, …)` con la misma fila de arriba o de abajo de cada mundo |
| Frases 1–4 | 80 px arriba | 88 px a la izquierda; mismos cuadros de entrada |
| Frase 4 | sale 957–961 | **se queda hasta el 1071**; sale 1071–1075 |
| Frase 5 del clip («Que ninguna persona se pierda», 960) | sí | **no** (pasa al final del recorrido, 2640) |
| Ceja «MEMBRESÍA» | sale 960–963 | **se queda hasta el 1071**; sale 1071–1075 |
| La ventana se hace a un lado (964–978) | sí | **no** |
| Cámara del compás 18 | quieta 975–1076 | **1020–1033: F16 sobre «Historial de pasos»** (`ul.historial` de la ficha desplazada `#m3post`: la caja del paso 40 de `pasos-2.json`, CSS 32·501 326×184, más el `h4` de arriba): «Empezó “Mensaje de bienvenida”», «Cumplió “Llamada de bienvenida”», «Empezó “Llamada de bienvenida”» con «hoy, HH:MM · Jorge Gallego Gil» (real). La ficha cuenta lo que ya pasó con Valeria |
| `subida` 1036–1093 y dip 1077–1079 | sí | **no** (la subida va al 2761; el dip al 2757) |
| 1080 | la firma `cierre-clip` | **el morph al escritorio** (abajo) |

**Del 960 al 1079, cuadro por cuadro:**

| Cuadro | Pulso | La app | Cámara | Texto | Sonido | Transición |
|---|---|---|---|---|---|---|
| **960** | ●●● 0,98 | G2 `v29`: la ficha de Valeria desplazada, quieta | F16 sobre la tarjeta «Avance» entera (de la fila «Avance» a la primera entrada del historial; CSS 139–563) — el plano del 960 del clip | frase 4 quieta | — | halo 1,08 → 1 (960–1050) |
| **1020** | ● 0,79 | quieta | **F16 sobre «Historial de pasos»** (1020–1033) | frase 4 quieta | — | |
| 1071–1075 | | quieta | quieta | **frase 4 y ceja salen** (`salida-texto`) | — | |
| **1074–1086** | **1080 ●●● 0,93** | 1074–1079: G2 `v29` se va (`x` 0 → −160); **1080: corte de contenido** a R1 (el «Resumen» de Coordinar) que entra `x` +160 → 0 y 1,04 → 1,00 (1080–1090) | la de R1 llega en D (abajo) | — | **desliz a (+), pico 1080** | **Morph** celular → escritorio (§1.5): la ventana va de (1104, 90, 720×900, r28) a (240, 260, 1440×760, r20); halo 1,08 → 1 (1080–1170) |

### 2.2 C1 · «Coordinar» — cuadros 1080–1559 (compases 19–26) · escritorio, cuenta 101 · grabación R1

| Cuadro | Pulso | La app (R1) | Cámara | Texto | Sonido |
|---|---|---|---|---|---|
| **1080** | ●●● 0,93 | R1·`resumen`, quieta: la cabecera de Membresía, las pestañas **«Resumen · Nuevos (n) · Quienes acompañan (n) · Por aprobar (n)»** y los indicadores (`#indicadores`): «En rojo», «Sin llamar a tiempo», «Reportes vencidos», «Por aprobar», **«Nuevos sin acompañante»** (resaltado en alerta), con sus cifras (real) | **D** sobre la unión de `nav.vistas` y `#ind-nuevos` (las pestañas arriba, la primera fila de indicadores entera) | — | (desliz del morph) |
| 1086 | | quieta | quieta | **«COORDINAR»** `entrada-linea` 1086–1092 | aparicion a 1087 |
| **1095** | ● 0,84 | quieta | quieta | **frase 5** «Nadie nuevo se queda sin llamada»: Nadie 1095 · nuevo 1097 · se 1099 · queda 1101 · sin 1103 · llamada 1105 (completa en el 1109) | — |
| **1140** | ● 0,81 | **toque en «Nuevos»** (`#sec-nuevos`, R1·`nuevos` toques[0]) → **1142**: la lista reemplaza a los indicadores: «**257 personas nuevas esperan Acompañante.**» (real, R1) · botón **«Repartir»** · filas con foto, nombre, «Culto o evento · 27 oct · Red …» (real) y «Asignar» | quieta (la pestaña y lo nuevo bajo el lente) | frase 5 quieta | toque c 1141 |
| **1170** | ● | quieta | **D** sobre la unión de `#btn-repartir` y las 4 primeras filas de `#bolsa-nuevos` (1170–1183) | | — |
| **1200** | **●●● cabeza** | **toque en «Repartir»** (`#btn-repartir`, R1·`repartir` toques[0]) → **1203**: el diálogo **«Repartir»** · «Se reparten de forma pareja entre los disponibles con cupo (misma red y mismo género si se configuró). Cada uno recibe un aviso.» · «Cancelar» · **«Repartir»** | quieta | | **toque a (+) 1201** · aparicion b 1204 | **Iris desde el toque** 1200–1205 (debajo, el still del 1199) |
| **1230** | ● | quieta (el diálogo) | **D⁺** sobre el texto del diálogo y sus botones (`mat-dialog-container`), 1230–1243: «de forma pareja» a 31,5 px | | — |
| **1290** | ● | **toque en «Repartir» del diálogo** (`#btn-confirm`, R1·`confirmar` toques[0]) → el diálogo se cierra (1291–1296, la app); 1297–1319 la lista todavía con sus nuevos (el último cuadro antes de la respuesta, estirado si hace falta) | quieta | | toque b 1291 | |
| **1320** | **●●● cabeza** | **el resultado, de golpe**: la lista vacía **«Todos los nuevos tienen quién los acompañe.»** (`#nuevos-vacio`) y el aviso **«Se repartieron N personas.»** (`#aviso-coordinar`, real). La pestaña «Nuevos» ya sin cifra | **punch D⁺** sobre la unión de `#nuevos-vacio` y `#aviso-coordinar` (1320–1328) | | **confirmacion (+) 1321** |
| **1380** | ● | **toque en «Quienes acompañan»** (`#sec-acompanantes`, R1·`acompanan` toques[0]) → **1383**: filas con foto, nombre, **«Acompaña a 11 de 12 · Red Timoteo»** (real, R1), los chips «1 en rojo», «1 sin llamar» (si los hay) y la **barra de carga** de cada uno | quieta 1380–1394; **1395–1408: D** sobre las tres primeras filas de `#bolsa-acompanantes` | | toque c 1381 |
| **1440** | **●●● cabeza** | quieta | **D⁺** sobre las dos primeras filas: «Acompaña a … de …» y su barra (1440–1453) | | — |
| **1500** | ● | quieta | **D** sobre las cuatro primeras filas (1500–1513): todos con su carga | | — |
| 1551–1555 | | quieta | quieta | **frase 5 y ceja salen** | — |
| **1554–1566** | **1560 ●●● 0,76** | 1554–1559: R1 se va (`x` 0 → −160); **1560: corte** a R2 | — | — | **desliz b, pico 1560** |

**Qué debe leerse de un vistazo:** en el 1150, «personas nuevas esperan» y «Repartir»; en el 1243, «de forma pareja»; **en el 1328, «Se
repartieron N personas.» y «Todos los nuevos tienen quién los acompañe.»**; en el 1453, «Acompaña a 11 de 12» y su barra.

### 2.3 C2 · «El semáforo de actividad» — cuadros 1560–1919 (compases 27–32) · celular, cuenta 101 · grabación R2

| Cuadro | Pulso | La app (R2) | Cámara | Texto | Sonido | Transición |
|---|---|---|---|---|---|---|
| **1554–1566** | **1560 ●●● 0,76** | **1560:** R2·`lista`, quieta: «Personas» de toda la iglesia: el buscador, **«Agregar filtro»**, el contador «N de N» (`#contador-personas`, real) y las filas, cada una con **su punto de color** antes del nombre (verde, amarillo, rojo o el anillo gris) | **G16** sobre la parte alta de la lista (CSS 0–450): «Agregar filtro» y 6–7 filas | — | (desliz) | **Morph** escritorio → celular: (240, 260, 1440×760, r20) → (1104, 90, 720×900, r28); R2 entra `x` +160 → 0, 1,04 → 1,00; halo 1560–1650 |
| 1566 | | quieta | quieta | **«SEMÁFORO DE ACTIVIDAD»** 1566–1572 | aparicion b 1567 | |
| **1575** | ● 0,64 | quieta | quieta | **frase 6** «Ves a tiempo / quién se aleja»: Ves 1575 · a 1577 · tiempo 1579 · quién 1581 · se 1583 · aleja 1585 (completa en el 1589) | — | |
| **1620** | ● 0,75 | **toque en «Agregar filtro»** (`#btn-agregar-filtro`) → la hoja sube desde abajo (la app, ≈ 6 cuadros, a 1×): «Persona»: «Estado», **«Semáforo de actividad»**, «Género», «Edad»… | quieta | | toque a 1621 | |
| **1635** | ● 0,61 | quieta (la hoja) | **G16** más abajo, centrado en la fila «Semáforo de actividad» (`#lista-tipos-filtro [data-filtro="actividad"]`), 1635–1648 | | — | |
| **1665** | ● | **toque en «Semáforo de actividad»** → **1668**: el editor del filtro: **«Verde · 0 a 10 días»**, **«Amarillo · 11 a 30 días»**, **«Rojo · 31 a 50 días»**, **«Sin actividad · más de 50 días»**, cada uno con su punto, y «Aplicar» (los días son los de la iglesia: real) | quieta | | toque b 1666 | |
| **1680** | ● 0,67 | quieta | **M16** sobre las cuatro opciones (`#editor-filtro`), 1680–1693 | | — | |
| **1710** | ● | **toque en «Rojo · 31 a 50 días»** (`mat-checkbox[data-opcion="3"]`): la casilla se marca (la app) | quieta | | toque c 1711 | |
| **1740** | ● 0,63 | **toque en «Aplicar»** (`#btn-aplicar-filtro`) → la hoja baja → **1744**: la lista filtrada: el chip **«Semáforo de actividad: Rojo»** (`[data-chip="actividad"]`), el contador **«62 de 1.324»** (real, R2) y **solo puntos rojos** | quieta | | toque a 1741 · aparicion c 1744 | |
| **1755** | ● | quieta | **G16** sobre lo alto de la lista filtrada (el chip, el contador y 5 filas), 1755–1768 | | — | |
| **1800** | **●●● 0,93** | **toque en la primera persona** (`#lista-personas a.fila >> nth=0`) → **1803**: su ficha: la foto, el nombre, el chip **«Actividad: Rojo · hace N días»** (`#chip-actividad[data-color="rojo"]`, real), «Llegó el …» y **«Llamar» · «WhatsApp» · «Editar»** | quieta (la ficha bajo el lente, como el 780 del clip) | | **toque b (+) 1801** | **Iris desde el toque** 1800–1805 |
| **1860** | **●●● 0,90** | quieta | **punch C16** sobre `#chip-actividad` (1860–1868): «Actividad: Rojo · hace N días» a 46 px | | — | |
| **1890** | ● 0,76 | quieta | **M16** sobre el chip y los botones «Llamar» · «WhatsApp» (1890–1903): lo que se hace con lo que se ve | | — | |
| 1911–1915 | | quieta | quieta | **frase 6 y ceja salen** | — | |

**Qué debe leerse:** en el 1693, los cuatro colores con sus días; en el 1768, el chip «Rojo» y el contador; **en el 1868, «Actividad: Rojo ·
hace N días»**.

### 2.4 C3 · «El discipulado» — cuadros 1920–2279 (compases 33–38) · celular, cuenta 101 · grabación R3

| Cuadro | Pulso | La app (R3) | Cámara | Texto | Sonido | Transición |
|---|---|---|---|---|---|---|
| **1914–1924** | **1920 ●●● 0,96** | 1920: R3·`cabezas`, quieta: Membresía → «Estructura», el botón **«Discipulado»** activo, «Empezar desde una persona», **«Quienes encabezan la pirámide (n)»** y los nodos (`#org-hijos li.nodo`): una o dos caras, el nombre (o la pareja), **«N directos · M en total»** (real) | **G16** sobre lo alto (CSS 0–450) | — | **desliz c, pico 1920** | **Látigo vertical** (una tira: la ficha de C2 sube y R3 llega de abajo, `--f-latigo` 1000), R3 aterriza 1,04 → 1,00 (1920–1930); halo 1920–2010 |
| 1926 | | quieta | quieta | **«DISCIPULADO»** 1926–1932 (el vocabulario de la demo, real) | aparicion c 1927 | |
| **1950** | ● | quieta | quieta | **frase 7** «Quién discipula / a quién»: Quién 1950 · discipula 1952 · a 1954 · quién 1956 (completa en el 1960) | — | |
| **1980** | ● 0,88 | quieta | **M16** sobre el primer nodo (`#org-hijos li.nodo >> nth=0`: la cabeza con más personas), 1980–1993: su nombre y «N directos · M en total» a 36 px | | — | |
| **2040** | **●●● 1,00** | **toque en ese nodo** (`button.entrar`) → **2043**: su pirámide: arriba la raíz (`#org-raiz`: las caras grandes, el nombre o la pareja, **«N directos · M en total»**, «Ver ficha», «Agregar discípulos»), debajo **«Sus discípulos directos (N)»** y sus nodos | quieta | | **toque c (+) 2041** · **aparicion a (+) 2044** | **Iris desde el toque** 2040–2045 |
| **2055** | ● 0,68 | quieta | **M16** sobre `#org-raiz` (2055–2068) | | — | |
| **2100** | ● 0,84 | quieta | **M16** más abajo: «N directos · M en total» arriba del encuadre, «Sus discípulos directos (N)» y los dos primeros nodos (2100–2113) | | — | |
| **2160** | **●●● 0,98** | **toque en el primer discípulo que discipula** (`#org-hijos li.nodo:has(a[mat-icon-button]) >> nth=0 >> button.entrar`) → **2163**: un nivel más abajo: **las migas «Inicio › (la cabeza) › (el discípulo)»** (`#org-migas`), su raíz con «N directos · M en total» y sus discípulos | quieta | | toque a 2161 | **Iris desde el toque** 2160–2165 |
| **2175** | ● 0,74 | quieta | **G16** sobre lo alto: las migas, la raíz y los primeros nodos (2175–2188) | | — | |
| **2220** | ● 0,79 | quieta | **C16** sobre las migas (`#org-migas`), 2220–2228: el camino de la cabeza hasta aquí | | — | |
| 2271–2275 | | quieta | quieta | **frase 7 y ceja salen** | — | |

**Qué debe leerse:** en el 1993, «N directos · M en total» de la primera cabeza; **en el 2068, la raíz con sus cifras**; en el 2228, «Inicio
› … › …».

### 2.5 C4 · «Los tableros» — cuadros 2280–2759 (compases 39–46) · escritorio, cuenta 101 · grabación R4

| Cuadro | Pulso | La app (R4) | Cámara | Texto | Sonido | Transición |
|---|---|---|---|---|---|---|
| **2274–2286** | **2280 ●●● 0,93** | **2280:** R4·`resumen`, quieta: «Tableros» → **«Resumen»**: las vistas («Resumen · Ruta · Por evento · Personas · Acompañantes · Logros»), «Toda la iglesia», el período, la descarga y las cifras (`#tablero-kpis`): **«Membresía»**, nuevas, en ruta, conectadas, «En rojo en la ruta», acompañadas, con su cambio «+N % · en 30 días» (real) | **D** sobre `#tablero-kpis` (la primera fila de cifras con las vistas arriba) | — | **desliz a (+), pico 2280** | **Morph** celular → escritorio; R4 entra `x` +160 → 0, 1,04 → 1,00; halo 2280–2370 |
| 2286 | | quieta | quieta | **«TABLEROS»** 2286–2292 | aparicion a 2287 | |
| **2295** | ● 0,84 | quieta | quieta | **frase 8** «Tu iglesia, de un vistazo»: Tu 2295 · iglesia, 2297 · de 2299 · un 2301 · vistazo 2303 (completa en el 2307) | — | |
| **2340** | ● 0,81 | quieta (si la tarjeta del semáforo está debajo de la primera vista, R4 se desplaza **aquí**, dentro del movimiento) | **D** sobre la tarjeta **«Semáforo de actividad»** (`#tablero-actividad`): la barra de cuatro colores y la lista «Verde · N · %», «Amarillo», «Rojo», «Sin actividad» (real), 2340–2353 | | — | |
| **2400** | **●●● cabeza** | quieta | **punch D⁺** sobre la barra y la fila **«Rojo»** (`#tablero-actividad-lista`), 2400–2408: los mismos rojos de C2, ahora como cifra de la iglesia | | — | |
| **2460** | ● | quieta (R4 vuelve arriba si se desplazó: dentro del movimiento) | **D** sobre el extremo derecho de la barra de filtros: «Toda la iglesia», el período y el botón de descarga (`#btn-exportar-tablero`), con la primera fila de cifras debajo (2460–2473) | | — | |
| **2490** | ● | **toque en la descarga** → **2493**: el menú **«PDF» · «Excel»** (`#exportar-tablero-pdf`, `#exportar-tablero-xlsx`) | quieta | | toque b 2491 · aparicion b 2494 | |
| **2520** | **●●● cabeza** | R4·`crecimiento`: el menú se cierra (Escape) y la página baja hasta **el crecimiento** (`#tablero-crecimiento`, el desplazamiento real de 300 ms cae en 2521–2530) | **D** sobre la gráfica del crecimiento, 2520–2533 (el movimiento esconde el desplazamiento) | | — | |
| **2580** | ● | quieta | **D⁺** sobre el tramo final de la curva (los últimos días), 2580–2593 | | — | |
| **2636–2640** | **2640 ●●● cabeza** | quieta | quieta | **frase 8 y ceja salen** 2636–2640 (blur swap); **frase 9** «Que *ninguna* persona se pierda»: Que 2640 · *ninguna* 2642 · persona 2644 · se 2646 · pierda 2648 (completa en el 2652). **La única palabra dorada del cuerpo** | — | halo 2640–2730 |
| **2700** | ● | quieta | **D** abre sobre la gráfica entera (2700–2713) | frase 9 quieta (4 s) | **`subida`** 2714–2771 (golpe en el 2761) | |
| **2757–2759** | | — | — | — | — | **Dip** al 40 % sobre la ventana |
| **2760** | **●●● golpe final** | — | — | — | (golpe final de la pista) | **Corte al cierre** |

**Qué debe leerse:** en el 2307, las cifras y la frase 8; en el 2408, «Rojo» y su cifra; en el 2493, «PDF» y «Excel»; **del 2652 al 2756, «Que
*ninguna* persona se pierda» sobre el crecimiento**.

### 2.6 El cierre — cuadros 2760–2909

`identidad/cierre-comercial.html` (kit v1.1, 1920×1080, 5 s), `data-start` **92,0**, `data-duration` 5, variables
`{"publico":"iglesia","llamado":"prueba","contacto":"sitio","fondo":"noche","idioma":"es"}`: la corona se levanta (0–1 s), el favicon sube
junto a **Kingdom**, la ceja «La app para iglesias» y el lema «Kingdom es para *toda la iglesia*» (1,1–2,3 s), el botón **«Prueba gratis 30
días»** y `kingdom-sitio.web.app` (2,3–2,9 s), quieto hasta el 97,0. Campanas en el **92,38**. La música es el golpe final de la pista y su
cola, a 0,25 desde el 92,40 (§0.1). **Nada del cuerpo imita la corona.**

### 2.7 Los trece planos

| Plano | Cuadros | Grabación | El movimiento héroe | Lo que se lee | Pasa al siguiente por |
|---|---|---|---|---|---|
| P1 La puerta | 0–119 | G1 | la app escribe «Valeria» | frase 1 | el toque en «Registrar» (iris) |
| P2 Guardada aun sin señal | 120–179 | G1 | el diálogo «Guardada en este dispositivo» | frase 2 | látigo vertical |
| P3 Mi seguimiento | 180–359 | G1 | la tarjeta de Valeria, tres movimientos | ceja «MEMBRESÍA» | el toque en «Marcar cumplido» (iris) |
| P4 El reporte | 360–599 | G1 | «Contestó» y las observaciones | frase 3 | el toque en el botón del diálogo |
| P5 Cumplido | 600–719 | G1 | punch a «Ahora va en: Mensaje de bienvenida» | (la app) | «Listo» |
| P6 La tarjeta al día y la ficha | 720–839 | G1 → G2 | el iris desde el nombre | — | el toque en «Avance» |
| P7 Avance | 840–959 | G2 | la tarjeta se abre en el golpe más fuerte | frase 4 | la cámara |
| **P8 Su historia** | **960–1079** | G2 | F16 a «Avance» y al historial | frase 4 | **morph al escritorio** |
| **P9 Coordinar** | **1080–1559** | R1 | «Repartir» → «Se repartieron» | ceja, frase 5 | **morph al celular** |
| **P10 El semáforo** | **1560–1919** | R2 | el filtro «Rojo» → la ficha | ceja, frase 6 | **látigo vertical** |
| **P11 El discipulado** | **1920–2279** | R3 | la pirámide se abre en el 2040 | ceja, frase 7 | **morph al escritorio** |
| **P12 Los tableros** | **2280–2759** | R4 | el semáforo de la iglesia y el crecimiento | ceja, frases 8 y 9 | **dip + corte** |
| P13 El cierre | 2760–2909 | kit | la corona | el lema y «Prueba gratis 30 días» | fin |

---

## 3. Las grabaciones

### 3.1 Las que se reusan (del clip, sin volver a grabar)

Se copian de `../clip-sitio-membresia/assets/` a `assets/` de este proyecto:

| Archivo | Qué es | Cuadros del recorrido | Tramos |
|---|---|---|---|
| `grabaciones/grabacion.mp4` + `pasos.json` (**G1**, 113,2 s, 1170×2532) | alta sin señal, asignación (no sale), Mi seguimiento, el reporte, «Listo» | **0–785** | `v01`–`v25` del `index.html` del clip, con sus `data-start`, `data-media-start` y tasas tal cual (de `v01` 5,466667 a 0,466667× hasta `v25` 97,076667 a 1×) |
| `grabaciones/grabacion-2.mp4` + `pasos-2.json` (**G2**, 113,9 s) | la misma escena con la ficha y «Avance» (T5) | **780–1079** | `v26` (desde el 2840), `v27` (2938–2939), `v28` (desde el 2948) y **`v29` (3135 → 3375, la ficha desplazada, a 1×, hasta el 1080)**: los del clip tal cual |
| `stills/still-466.png`, `still-2401.png` | los cuadros bajo los irises del 120 y del 375 | 120–125, 375–380 | — |
| `audio/toque-b.wav`, `toque-c.wav` | las tomas b y c de `toque` | todo el video | — |

Para el plano nuevo del 1020 (el historial) **no hace falta grabar**: `v29` ya trae la ficha desplazada con «Historial de pasos» completo
(medido en el clip, REVIEW §4.1 y §4.5).

### 3.2 Las escenas nuevas (listas para copiar)

Cuatro escenas en `F:\Proyectos\KingdomApp\tools\ayuda\escenas\clips\`, todas con `toque: false` (el montaje dibuja sus propios toques sobre
`toques[]`) y la cuenta **101** (Andrés Felipe Restrepo Gómez, el administrador de Kingdom Demo: coordina y ve a toda la iglesia). Dos de
**escritorio** (1280×720 a 1,5× = 1920×1080; sin `movil`) y dos de **celular** (`movil: true`, 390×844 a 3× = 1170×2532). Se graban con:

```bash
cd F:/Proyectos/KingdomApp/tools/ayuda
node capturar.mjs clips/recorrido-membresia-coordinar   --idioma es --modo video
node capturar.mjs clips/recorrido-membresia-semaforo    --idioma es --modo video
node capturar.mjs clips/recorrido-membresia-discipulado --idioma es --modo video
node capturar.mjs clips/recorrido-membresia-tableros    --idioma es --modo video
# → salida/video/es/clips/recorrido-membresia-<x>/grabacion.mp4 + pasos.json
#   se copian como assets/grabaciones/r1-coordinar.mp4 + r1-coordinar.pasos.json, r2-semaforo…, r3-discipulado…, r4-tableros…
```

Cada corrida restaura el volcado de Kingdom Demo (la de Coordinar reparte de verdad: no contamina a las otras). Las pausas son las que el
montaje necesita quietas; lo que sobra se corta (§2.0) y nada se puede alargar más allá de 0,35×.

**Selectores verificados** (2026-10-30) en `frontend-v2/src/app/pages/membresia/`: `coordinar.page.ts` (`#indicadores`, `#ind-nuevos`,
`#sec-nuevos`, `#sec-acompanantes`, `#bolsa-nuevos li[data-persona]`, `#btn-repartir`, `#nuevos-vacio`, `#aviso-coordinar`,
`#bolsa-acompanantes li.acomp`), `components/app-dialog.component.ts` (`#btn-confirm`), `membresia.page.ts` (`#lista-personas a.fila`,
`#contador-personas`), `membresia-filtros.component.ts` (`#btn-agregar-filtro`, `#filtros-membresia [data-chip]`), `filtro-editor.component.ts`
(`#lista-tipos-filtro [data-filtro="actividad"]`, `#editor-filtro[data-tipo]`, `mat-checkbox[data-opcion]` con Rojo = 3 por el orden de
`COLORES_ACTIVIDAD`, `#btn-aplicar-filtro`), `persona.page.ts` (`#chip-actividad[data-color]`), `estructura.page.ts` (`button.est-tab-discipulado`),
`estructura-discipulado.component.ts` (`#org-hijos li.nodo`, `button.entrar`, `a[mat-icon-button]` solo en los nodos con discípulos,
`#org-raiz`, `#org-migas [data-miga]`), `tableros.page.ts` (`#btn-exportar-tablero`, `#exportar-tablero-pdf`), `tablero-resumen.component.ts`
(`#tablero-kpis`, `#tablero-actividad`, `#tablero-crecimiento`) y `tablero-actividad.component.ts` (`#tablero-actividad-lista`); los pasos,
como en las escenas de la ayuda `membresia/coordinar-el-seguimiento.mjs`, `buscar-y-filtrar.mjs`, `estructura.mjs` y `tableros.mjs`.

#### R1 · `tools/ayuda/escenas/clips/recorrido-membresia-coordinar.mjs` (escritorio)

```js
// Grabación para el RECORRIDO del módulo Membresía (LegacyHyperframes/videos/kingdomapp/recorrido-membresia/SPEC.md §2.2 y §3.2, R1).
// NO es una escena de un artículo de la ayuda: no se publica ni entra en la frescura. ESCRITORIO (1280×720 a 1,5x = 1920×1080, 30 cps),
// SIN el círculo del toque (`toque: false`): el montaje dibuja el suyo sobre toques[] y las cajas de pasos.json.
//   node capturar.mjs clips/recorrido-membresia-coordinar --idioma es --modo video
// La cuenta del administrador (101) coordina: «Resumen» → «Nuevos» → «Repartir» → confirmar → «Quienes acompañan». Kingdom Demo deja
// nuevos sin repartir a propósito (escena de la ayuda membresia/coordinar-el-seguimiento). Si no hubiera nuevos o nadie tuviera cupo, la
// escena se detiene sola: `#bolsa-nuevos li[data-persona]` no aparece o «Repartir» queda deshabilitado y el clic no se puede dar.
export default {
  articulo: 'clips/recorrido-membresia-coordinar',
  toque: false,
  pantallas: [
    'frontend-v2/src/app/pages/membresia/coordinar.page.ts',
    'frontend-v2/src/app/pages/membresia/ruta-persona-item.component.ts',
    'frontend-v2/src/app/components/app-dialog.component.ts',
  ],
  pasos: [
    // 1-3. «Resumen»: las pestañas y los indicadores, quietos (cuadros 1080–1139 del recorrido).
    { tramo: 'resumen', como: 101, ir: '/servir/membresia/coordinar', espera: '#indicadores' },
    { ver: '#ind-nuevos', bloque: 'nearest', pausa: 2500 },        // solo la caja del indicador «Nuevos sin acompañante» (no desplaza)
    // 4-5. «Nuevos» (el toque del 1140): la lista con «Repartir».
    { tramo: 'nuevos', clic: '#sec-nuevos', espera: '#bolsa-nuevos li[data-persona]', pausa: 1500 },
    { ver: '#btn-repartir', bloque: 'nearest', pausa: 1500 },     // caja del botón (objetivo del 1170)
    // 6. «Repartir» (el toque del 1200): el diálogo de confirmación.
    { tramo: 'repartir', clic: '#btn-repartir', espera: '#btn-confirm', pausa: 2000 },
    // 7-8. Confirmar (el toque del 1290): «Se repartieron N personas.» y la lista vacía (el 1320).
    { tramo: 'confirmar', clic: '#btn-confirm', oculto: 'mat-dialog-container' },
    { espera: '#aviso-coordinar', pausa: 2500 },
    { ver: '#bolsa-nuevos', bloque: 'nearest', pausa: 200 },      // caja de la lista (vacía: «Todos los nuevos tienen quién los acompañe.»)
    // 9-10. «Quienes acompañan» (el toque del 1380): la carga de cada uno, quieta hasta el final del capítulo.
    { tramo: 'acompanan', clic: '#sec-acompanantes', espera: '#bolsa-acompanantes li.acomp', pausa: 3500 },
    { ver: '#bolsa-acompanantes li.acomp >> nth=0', bloque: 'nearest', pausa: 200 },
  ],
};
```

Montaje de R1: `resumen` (quieto, a 0,5–1×) → 1080–1139 · `nuevos` toques[0] → **1140** (la lista completa en el 1142) · `repartir`
toques[0] → **1200** (el diálogo abierto en el 1203; still del 1199 bajo el iris) · `confirmar` toques[0] → **1290**; el primer cuadro con
`#aviso-coordinar` → **1320** · `acompanan` toques[0] → **1380**, quieto a 0,6–0,7× hasta el 1559. Si el reparto deja nuevos sin asignar
(nadie más con cupo), la lista muestra a los que quedan y el punch del 1320 va al aviso solo.

#### R2 · `tools/ayuda/escenas/clips/recorrido-membresia-semaforo.mjs` (celular)

```js
// Grabación para el RECORRIDO del módulo Membresía (recorrido-membresia/SPEC.md §2.3 y §3.2, R2). No es de la ayuda: no se publica.
// CELULAR (390×844 a 3x = 1170×2532, 30 cps), SIN el círculo del toque (`toque: false`).
//   node capturar.mjs clips/recorrido-membresia-semaforo --idioma es --modo video
// La cuenta del administrador (101, ve a toda la iglesia) filtra «Personas» por el semáforo de actividad en «Rojo» y abre a la primera
// persona: su ficha dice «Actividad: Rojo · hace N días». Kingdom Demo siembra la sección «semaforo» (docs/modulos/membresia.md): personas en
// los cuatro colores, ≈ 33 en rojo de 1 000.
const SEDE = `(SELECT id_sede FROM kd_usuario_sedes WHERE id_usuario = 101 AND estado = 'activo' LIMIT 1)`;

export default {
  articulo: 'clips/recorrido-membresia-semaforo',
  movil: true,
  toque: false,
  pantallas: [
    'frontend-v2/src/app/pages/membresia/membresia.page.ts',
    'frontend-v2/src/app/pages/membresia/membresia-filtros.component.ts',
    'frontend-v2/src/app/pages/membresia/filtro-editor.component.ts',
    'frontend-v2/src/app/pages/membresia/filtros-lista.ts',
    'frontend-v2/src/app/pages/membresia/persona.page.ts',
    'frontend-v2/src/app/services/membresia/actividad.ts',
  ],
  refs: {
    // El filtro «Rojo» (31 a 50 días con los umbrales de fábrica) tiene que dejar al menos 5 personas; si no, la consulta da NULL y
    // capturar.mjs se niega antes de grabar. Si la demo cambió los umbrales (mem_config.actividad), se ajustan los días aquí.
    rojas: `SELECT IF(COUNT(*) >= 5, COUNT(*), NULL) FROM mem_persona_actividad a JOIN mem_personas p ON p.id = a.id_persona
            WHERE p.id_sede = ${SEDE} AND p.estado = 'activa' AND p.eliminado_at IS NULL
              AND a.dia BETWEEN CURDATE() - INTERVAL 50 DAY AND CURDATE() - INTERVAL 31 DAY`,
  },
  pasos: [
    // 1-3. «Personas» de toda la iglesia. La primera vez el celular descarga la lista (1 000 personas): fuera de cámara, se le da tiempo.
    { tramo: 'lista', como: 101, ir: '/servir/membresia', espera: '#btn-agregar-filtro' },
    ...Array.from({ length: 6 }, () => ({ pausa: 1500 })),
    { espera: '#lista-personas a.fila', pausa: 2500 },             // la lista con sus puntos de color, quieta (cuadros 1560–1619)
    // 4. «Agregar filtro» (el toque del 1620): la hoja sube desde abajo.
    { tramo: 'agregar', clic: '#btn-agregar-filtro', espera: '#lista-tipos-filtro [data-filtro="actividad"]', pausa: 1500 },
    // 5. «Semáforo de actividad» (el toque del 1665): los cuatro colores con sus días.
    { tramo: 'semaforo', clic: '#lista-tipos-filtro [data-filtro="actividad"]', espera: '#editor-filtro[data-tipo="actividad"]', pausa: 1500 },
    { ver: '#editor-filtro', bloque: 'nearest', pausa: 200 },      // caja de las opciones (objetivo del 1680)
    // 6. «Rojo · 31 a 50 días» (el toque del 1710). Rojo es la opción 3 (COLORES_ACTIVIDAD: verde, amarillo, rojo, gris).
    { tramo: 'rojo', marcar: '#editor-filtro mat-checkbox[data-opcion="3"]', pausa: 1200 },
    // 7-10. «Aplicar» (el toque del 1740): la lista solo con los rojos, el chip del filtro y el contador.
    { tramo: 'aplicar', clic: '#btn-aplicar-filtro', oculto: 'mat-dialog-container' },
    { espera: '#filtros-membresia [data-chip="actividad"]', pausa: 2500 },
    { ver: '#contador-personas', bloque: 'nearest', pausa: 200 },
    { ver: '#lista-personas a.fila >> nth=0', bloque: 'nearest', pausa: 200 },
    // 11-12. La primera persona (el toque del 1800): su ficha con «Actividad: Rojo · hace N días», quieta hasta el látigo del 1914.
    { tramo: 'ficha', clic: '#lista-personas a.fila >> nth=0', espera: '#chip-actividad[data-color="rojo"]', pausa: 3500 },
    { ver: '#chip-actividad', bloque: 'nearest', pausa: 200 },     // caja del chip (objetivo del 1860)
  ],
};
```

Montaje de R2: `lista` (lo último antes de `agregar`) → 1560–1619 · `agregar` toques[0] → **1620** (la hoja sube a 1×) · `semaforo` toques[0]
→ **1665** (el editor en el 1668) · `rojo` toques[0] → **1710** · `aplicar` toques[0] → **1740** (la lista filtrada completa en el 1744) ·
`ficha` toques[0] → **1800** (la ficha completa en el 1803, el cargador cortado), quieta hasta el 1924.

#### R3 · `tools/ayuda/escenas/clips/recorrido-membresia-discipulado.mjs` (celular)

```js
// Grabación para el RECORRIDO del módulo Membresía (recorrido-membresia/SPEC.md §2.4 y §3.2, R3). No es de la ayuda: no se publica.
// CELULAR (390×844 a 3x = 1170×2532, 30 cps), SIN el círculo del toque (`toque: false`).
//   node capturar.mjs clips/recorrido-membresia-discipulado --idioma es --modo video
// La cuenta del administrador (101) abre Estructura → Discipulado (el organigrama pensado para el celular: un nivel a la vez, «directos
// y total»), entra en la cabeza con más personas (cuidadoOrganigrama ordena «los de más personas primero») y baja un nivel más por el
// primer discípulo que discipula (solo esos nodos traen el enlace a la ficha `a[mat-icon-button]`).
const SEDE = `(SELECT id_sede FROM kd_usuario_sedes WHERE id_usuario = 101 AND estado = 'activo' LIMIT 1)`;

export default {
  articulo: 'clips/recorrido-membresia-discipulado',
  movil: true,
  toque: false,
  pantallas: [
    'frontend-v2/src/app/pages/membresia/estructura.page.ts',
    'frontend-v2/src/app/pages/membresia/estructura-discipulado.component.ts',
  ],
  refs: {
    // La pirámide de la demo tiene que tener al menos tres niveles (alguien con discipulador que a su vez discipula); si no, NULL y no graba.
    nietos: `SELECT IF(COUNT(*) > 0, COUNT(*), NULL) FROM mem_discipulado_arbol t JOIN mem_personas p ON p.id = t.descendiente
             WHERE t.profundidad = 2 AND p.id_sede = ${SEDE} AND p.estado = 'activa'`,
  },
  pasos: [
    // 1-3. Estructura → Discipulado: las cabezas de la pirámide, quietas (cuadros 1920–2039).
    { tramo: 'estructura', como: 101, ir: '/servir/membresia/estructura', espera: 'button.est-tab-discipulado' },
    { tramo: 'cabezas', clic: 'button.est-tab-discipulado', espera: '#org-hijos li.nodo', pausa: 2500 },
    { ver: '#org-hijos li.nodo >> nth=0', bloque: 'nearest', pausa: 200 },   // caja de la primera cabeza (objetivo del 1980)
    // 4-5. La cabeza (el toque del 2040, el golpe más fuerte): su pirámide, con «N directos · M en total» y sus discípulos.
    { tramo: 'cabeza', clic: '#org-hijos li.nodo >> nth=0 >> button.entrar', espera: '#org-raiz', pausa: 2500 },
    { ver: '#org-raiz', bloque: 'nearest', pausa: 200 },                       // caja de la raíz (objetivo del 2055)
    { ver: '#org-hijos li.nodo >> nth=1', bloque: 'nearest', pausa: 200 },    // caja de los dos primeros discípulos (objetivo del 2100)
    // 6-8. Un nivel más (el toque del 2160): las migas «Inicio › … › …», quieto hasta el final del capítulo.
    { tramo: 'bajar', clic: '#org-hijos li.nodo:has(a[mat-icon-button]) >> nth=0 >> button.entrar', espera: '#org-migas [data-miga]', pausa: 3500 },
    { ver: '#org-migas', bloque: 'nearest', pausa: 200 },                      // caja de las migas (objetivo del 2220)
    { ver: '#org-raiz', bloque: 'nearest', pausa: 200 },
  ],
};
```

Montaje de R3: `cabezas` (después de que aparecen los nodos) → 1920–2039, a 0,7–1× · `cabeza` toques[0] → **2040** (la pirámide completa en el
2043; el iris la descubre) · `bajar` toques[0] → **2160** (el nivel nuevo en el 2163) · quieto hasta el 2286. El toque del 2160 tiene que
caer dentro del encuadre del 2100: si el primer nodo con discípulos no es el primero ni el segundo de la lista, el encuadre del 2100 se
centra en la caja de ese nodo (`toques[0]` del paso `bajar` dice dónde está).

#### R4 · `tools/ayuda/escenas/clips/recorrido-membresia-tableros.mjs` (escritorio)

```js
// Grabación para el RECORRIDO del módulo Membresía (recorrido-membresia/SPEC.md §2.5 y §3.2, R4). No es de la ayuda: no se publica.
// ESCRITORIO (1280×720 a 1,5x = 1920×1080, 30 cps), SIN el círculo del toque (`toque: false`).
//   node capturar.mjs clips/recorrido-membresia-tableros --idioma es --modo video
// La cuenta del administrador (101): Tableros → «Resumen» (las cifras y el semáforo de actividad), el menú de descarga «PDF · Excel» (se
// abre y se cierra con Escape: no se descarga nada) y el crecimiento, quieto para la frase final. Las cifras se calculan una vez al día:
// el volcado de Kingdom Demo ya las trae (escena de la ayuda membresia/tableros).
export default {
  articulo: 'clips/recorrido-membresia-tableros',
  toque: false,
  pantallas: [
    'frontend-v2/src/app/pages/membresia/tableros.page.ts',
    'frontend-v2/src/app/pages/membresia/tablero-resumen.component.ts',
    'frontend-v2/src/app/pages/membresia/tablero-actividad.component.ts',
  ],
  pasos: [
    // 1-4. «Resumen», quieto (cuadros 2280–2489): las cifras y el semáforo. Los `ver` con 'nearest' solo anotan cajas; si la tarjeta del
    // semáforo no cabe en la primera vista, el segundo desplaza una vez y el montaje lo esconde en el movimiento del 2340.
    { tramo: 'resumen', como: 101, ir: '/servir/membresia/tableros', espera: '#tablero-actividad' },
    { pausa: 3500 },
    { ver: '#tablero-kpis', bloque: 'nearest', pausa: 200 },
    { ver: '#tablero-actividad', bloque: 'nearest', pausa: 2500 },
    { ver: '#tablero-actividad-lista', bloque: 'nearest', pausa: 200 },
    // 5-6. La descarga (el toque del 2490): «PDF · Excel». Se cierra con Escape sin descargar (el 2520).
    { ver: '#btn-exportar-tablero', bloque: 'nearest', pausa: 600 },
    { tramo: 'descargar', clic: '#btn-exportar-tablero', espera: '#exportar-tablero-pdf', pausa: 1500 },
    { tecla: 'Escape', oculto: '#exportar-tablero-pdf' },
    // 7. El crecimiento (2520): un desplazamiento real, dentro del movimiento de cámara; quieto para la frase final (hasta el 2759).
    { tramo: 'crecimiento', ver: '#tablero-crecimiento', bloque: 'center', pausa: 5000 },
  ],
};
```

Montaje de R4: `resumen` quieto a 0,5–1× → 2280–2489 (el desplazamiento, si lo hay, dentro del 2340–2353 o del 2460–2473) · `descargar`
toques[0] → **2490** (el menú en el 2493) · la `tecla` → **2520**, y el desplazamiento suave de `crecimiento` en 2521–2530, dentro del
movimiento 2520–2533 · el crecimiento quieto a 0,6–1× hasta el 2759.

---

## 4. Lo que se revisa en la vista previa

Cuadros a mirar: `npx hyperframes snapshot --at 0,1.5,4.0,6.2,12.5,20.1,22.3,26.1,28.07,30.5,32.5,34.5,35.7,36.0,36.3,37.0,38.1,40.2,41.0,43.1,44.0,44.3,46.5,48.5,50.5,51.9,52.0,52.3,53.0,54.6,56.5,57.1,58.6,59.0,60.2,62.3,63.6,64.0,64.3,65.4,66.5,68.1,68.8,70.4,72.1,73.0,74.3,75.9,76.0,76.3,77.0,78.6,80.3,82.4,83.2,84.3,86.5,88.4,90.0,91.9,92.0,92.5,93.5,96.9`;
`snapshot --range` 35.7,36.4 (21 cuadros: el primer morph), 51.7,52.4 (el morph de vuelta y el empalme de la música), 63.7,64.4 (el látigo
vertical), 67.9,68.3 (el iris de la pirámide), 75.7,76.4 (el último morph), 91.7,92.6 (dip, empalme y cierre). Más `--review` al final.

1. **0–959 igual que el clip**, reencuadrado: ningún texto de la app < 28 px en G16; la tarjeta de Valeria entera de lado a lado en el 180–359;
   las frases 1–4 a la izquierda, sin tocar la ventana.
2. **1020–1033:** «Historial de pasos» con «Cumplió “Llamada de bienvenida”» a ≥ 29 px. **1071–1075:** frase 4 y ceja se van antes del morph.
3. **1074–1086 (el morph):** ningún cuadro con la ventana vacía, con fondo de la app a la vista ni con dos contenidos encimados; el contenido
   cambia en el 1080, el cuadro más borroso; la ventana termina exacta en (240, 260, 1440×760, r20).
4. **1086–1109:** «COORDINAR» y la frase 5 en **una** línea dentro de 1440 px; el escritorio en D, texto del cuerpo ≥ 28 px; nunca el
   escritorio entero.
5. **1142, 1203, 1320, 1383:** el cambio de la app completo en ese cuadro (nada a medias); **1320** con «Se repartieron N personas.» y la lista
   vacía legibles en el 1328.
6. **1554–1566:** el morph de vuelta: la ventana termina en (1104, 90, 720×900, r28); «SEMÁFORO DE ACTIVIDAD» y la frase 6 en dos líneas.
7. **1620–1744:** la hoja sube (la app), los cuatro colores se leen en el 1693, «Rojo» marcado en el 1712, la lista solo con puntos rojos en
   el 1744. **1868:** «Actividad: Rojo · hace N días» a ≥ 44 px.
8. **1914–1924:** el látigo vertical en una tira, sin ventana vacía. **2040:** el toque con el golpe más fuerte; la pirámide completa en el
   2043; **2068:** «N directos · M en total» a ≥ 36 px. **2160:** el toque dentro del encuadre; **2228:** las migas enteras.
9. **2274–2286:** el morph al escritorio. **2307:** «Tu iglesia, de un vistazo» en una línea; las cifras con «Datos de ejemplo». **2408:** la
   fila «Rojo». **2493:** «PDF» y «Excel». **2521–2530:** el desplazamiento de la app dentro del movimiento de cámara (nunca con la cámara
   quieta).
10. **2640–2756:** «Que *ninguna* persona se pierda» en una línea con *ninguna* dorada y ninguna ceja; quieta ≥ 3,5 s. **2757–2759:** el dip.
    **2760:** el primer cuadro del cierre, sin noche vacía entre medias.
11. **Ningún compás sin toque o movimiento** entre el 1080 y el 2759; ningún tramo de más de 3 s sin un cambio visible.
12. **El sonido (medido, no oído):** `npx hyperframes audio <render> --json` encuentra los golpes de los toques un cuadro después de cada
    imagen (61 · 91 · 121 · 151 · 376 · 451 · 496 · 601 · 721 · 781 · 841 · **1141 · 1201 · 1291 · 1381 · 1621 · 1666 · 1711 · 1741 · 1801 ·
    2041 · 2161 · 2491**); la `confirmacion` del 1321; las campanas en el 92,38; la sonoridad momentánea sin hueco ni salto en 51,9–52,1 y en
    91,9–92,1 (los empalmes; `ffmpeg -af astats` en esos 200 ms: sin un pico de muestra mayor que el de los compases vecinos, que sería un
    clic); −17 a −16 LUFS integrados; pico real ≤ −1 dBTP.
13. **La música en la grilla:** `npx hyperframes beats` sobre el audio del render: los pulsos de 0–52 y de 52–92 en múltiplos de 0,5 s desde el
    0 del video (con la misma corrida a contratiempo en los clímax que da la pista sola: si aparece **fuera** del clímax, un empalme quedó
    corrido).
14. **Textos:** ninguna palabra que no esté en la app, en las nueve frases, en las cinco cejas o en el cierre del kit; `npx hyperframes check`
    en 0 errores (contraste AA incluido); «Datos de ejemplo» del 0 al 2759.
15. **La historia sin sonido:** se entiende con la pantalla en silencio: llegó → sin señal → la llaman → su ruta → los nuevos se reparten →
    los que se alejan se ven → el discipulado → la iglesia entera → ninguna se pierde → Kingdom, prueba gratis.
16. **A 360 px de ancho** (`--review` → `review-phone`): las frases y «Datos de ejemplo» se leen; el escritorio en D se lee como recorte.

---

## 5. Riesgos y lo que se decide al grabar

- **La grilla del clímax** (§0.2). La evidencia dice x,05; si al mirar el render con la música (`snapshot` + `audio`) los acentos del clímax
  se sienten corridos medio pulso respecto de los toques de C1 y C4, se corren **solo los toques y las frases** de esos dos capítulos +8
  cuadros (nunca los cambios de mundo ni los empalmes, que están en cabezas de compás).
- **Los empalmes.** Si el cruce de 2 cuadros deja un clic (medido con `astats`) o un hueco de energía, se prueba un cruce de 4 cuadros
  (51,867–52,000) y, si no basta, cortar en el cruce por cero más cercano al 52,000 dentro de ±5 ms. El del 92,0 queda debajo del golpe final
  y del cierre.
- **Las campanas sobre la cola del final:** la tonalidad de la pista no está medida; si la cola choca con las campanas (Mi mayor), la música
  baja a 0,15 en el 92,30 en vez de 0,25 en el 92,40.
- **El escritorio a 1,5×:** D amplía la fuente 1,33× y D⁺ 1,5× (el límite de nitidez del kit). Si un texto clave del escritorio no se lee en
  D⁺, no se acerca más: se encuadra la línea en D⁺ con menos contexto. Una mejora de herramienta (grabar escritorio a 2×) queda anotada,
  no se pide para este video.
- **Una línea en el escritorio:** «Nadie nuevo se queda sin llamada» mide ≈ 1340 px a 84 px (estimado); se mide al construir; si pasa de
  1440, 80 px.
- **Las cifras de Kingdom Demo** (cuántos nuevos, cuánta carga, cuántos en rojo, el tamaño de la pirámide, el crecimiento) salen de la
  grabación; ninguna frase depende de ellas. Si «Repartir» no reparte a todos (falta cupo), el plano del 1320 se queda con el aviso.
- **El reparto en la grabación** dispara avisos a los acompañantes (la cola de notificaciones local): no se ven y no fallan la escena; si la
  consola de la app los reporta como error, se agrega `consolaEsperada` con ese texto exacto.
- **La hoja del filtro en el celular** sube con su animación: si dura más de 8 cuadros, se acelera ese tramo (≤ 3,5×), nunca se corta a la
  mitad.
- **Las migas de la pirámide:** se asume que en el primer nivel no hay migas con `data-miga` (la raíz es la cabeza). Si las hubiera, la
  `espera` del paso `bajar` pasa a `#org-migas [data-miga] >> nth=1`.
- **El tablero** se calcula una vez al día: si el volcado no trae la foto de un día anterior, la tarjeta del semáforo dice «El cambio en el
  período aparece cuando haya una foto de un día anterior…» (real). Se deja; el encuadre del 2340 va a la barra y la lista.
- **La duración del recorrido:** las directivas (`KingdomApp/docs/videos/README.md` → Clip del sitio) todavía dicen 60–75 s; el pedido del
  dueño de este video es ~100 s. Hay que actualizar esa línea (60–100 s).
- **9:16** (la otra pieza del recorrido según las directivas) queda para después: la misma línea de tiempo con la ventana de 960×850 del
  clip para el celular y, en los capítulos de escritorio, recortes D de 480×425 CSS (dos movimientos por capítulo más).
- **Inglés y portugués:** las cuatro escenas con `--idioma en` graban la interfaz en inglés; las frases se traducen y los saltos se vuelven a
  fijar; el cierre lleva `idioma`.

---

## 6. Para quien construye

- **Proyecto:** esta carpeta, con `BRIEF.md` (`tipo: comercial`, `subtipo: clip-del-sitio`, recorrido; 16:9; 97 s), `hyperframes.json` y
  `package.json` copiados del clip (HyperFrames 0.8.221, scripts `kit`, `check`, `render`); `npm run kit`; `identidad/frame-comercial.md`
  copiado como `frame.md`; la música en `assets/musica/`; las grabaciones y lo reusado en `assets/` (§3).
- **`index.html`:** se parte del `index.html` del clip. La raíz pasa a 1920×1080 y `data-duration` 97; las variables `--f-*` y `window.KD` de
  §2.1; la ventana es **una sola** `.k-ventana` con sus mundos dentro (el acto 1 con sus mundos 1–3 como en el clip; R1, R2 + R3 en una tira
  para el látigo vertical, R4) y el morph sobre ella; los textos son subcomposiciones (`compositions/frase-1…9.html`, `ceja-1…5.html`,
  `fondo.html`); el cierre es el host `cierre-comercial` en 92,0 con el sonido de marca en 92,38.
- **Tramos nuevos de video:** uno por cada intervalo de §2.2–§2.5 entre acciones (`data-start`, `data-media-start` = segundo del cuadro de la
  grabación + 0,01, `data-playback-rate`), cada corte dentro de una pausa de la grabación, medida cuadro a cuadro como en el clip (REVIEW §5).
- **Revisión:** `npm run check` (0 errores) → los `snapshot` de §4 → `--review` → render `--quality high` → `npx hyperframes audio --json`.
  Lo que se desvíe de este SPEC se anota con su porqué en `REVIEW.md`, como en el clip.
