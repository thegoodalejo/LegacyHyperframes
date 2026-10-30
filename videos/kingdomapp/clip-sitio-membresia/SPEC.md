# SPEC · Clip del sitio: Membresía — «Valeria llegó el domingo»

2026-10-30 · Paso 2 de la revisión en dos puntos ([BRIEF.md](BRIEF.md)). El dueño eligió la **Historia A tal cual** ([STORY.md](STORY.md) → §Historia A).
Este documento es el contrato de construcción: cada adjetivo es un número, los valores por defecto están prohibidos con nombre y los planos
van cuadro por cuadro. Se construye desde aquí, se revisa contra esto y se cambia aquí cuando la vista previa cambie la película.

```text
GOAL:    Un pastor que no conoce Kingdom termina pensando «llegó el domingo y el lunes alguien la llamó» y toca «Prueba gratis 30 días».
OUTPUT:  HyperFrames · dos composiciones de la misma línea de tiempo: 1080×1350 (4:5, sitio y feed) y 1080×1920 (9:16, Reels e historias) · 30 fps.
TIME:    30,5 s = 915 cuadros: cuerpo 0–28,0 (cuadros 0–839) + firma 28,0–30,5 (840–914). 120 BPM = 15 cuadros por pulso (grilla real abajo).
LOOK:    noche del sitio (#060D1F) con el halo y la retícula de puntos del kit; tinta #EAF0FF; un solo acento, el dorado #E8B95A, en tres
         lugares y no más (la ceja «MEMBRESÍA», la palabra «ninguna» y el botón de la firma). Fraunces 560 / −0,02 em para las frases;
         Inter para la ceja y «Datos de ejemplo». El medio: la app REAL de Kingdom Demo grabada en celular, nítida (1170 px de ancho),
         dentro de una ventana con radio 28, anillo de 1 px y sombra 0 40 80 −24 al 65 %; nunca un teléfono dibujado.
OBJECTS: la ventana (el celular de quien registra y, tras el látigo, el de quien acompaña); el punto de toque de la grabación; las cuatro
         frases; la ceja; la píldora «Datos de ejemplo»; la corona del cierre. Nada más existe en el cuadro.
MOTION:  curvas por papel (§1.6); un movimiento de cámara por compás (14 cuadros, power2.inOut), quieto después; cada corte y cada
         entrada en un pulso; cada cambio de mundo en un golpe (120 · 180 · 600 · 660 · 720 · 840).
SHOTS:   siete planos (§2).
BANNED:  §1.8.
QA:      §4.
```

---

## 0. El reloj: la grilla real de la pista

La música es «Product Launch» (The_Mountain) del 14,05 al 42,05 s. t = 0 del clip ↔ 14,05 de la pista. Los pulsos vienen del mapa
`beats/product-launch-the-mountain.mp3.json` restándoles 14,05 y redondeando a 30 fps: **todos caen en el múltiplo de 15 cuadros salvo
el 9,455 s, que cae en el cuadro 284** (uno antes del 285 ideal; no hay ningún evento ahí). Los cuadros de abajo son los que se usan; nunca
se suma 15 repetidamente (deriva), cada pulso se calcula desde su índice.

| Compás | Cuadros | Pulsos (cuadro · fuerza) | Intensidad del compás | Lo que le toca al video |
|---|---|---|---|---|
| 1 | 0–59 | 0 ·0,69 · 15 ·0,64 · 30 ·0,49 · 45 ·0,48 | 0,57 | El gancho: la app ya trabajando, la frase 1 palabra por pulso |
| 2 | 60–119 | 60 ·0,58 · 75 ·0,55 · 90 ·0,57 · 105 ·0,61 | 0,58 | Cierra un campo por pulso; la pantalla baja a «Registrar» |
| 3 | 120–179 | **120 ·0,93** (entra el bajo) · 135 · 150 · 165 | 0,66 | El toque en «Registrar»: Kingdom entra. Frase 2 |
| 4 | 180–239 | **180 ·0,87** (pico) · 195 ·0,83 · 210 · 225 | **0,77** | El látigo al otro celular; la tarjeta de Valeria; la ceja |
| 5 | 240–299 | **240 ·0,92** · 255 ·0,77 · 270 · 284 | 0,70 | Acercamiento 1 (la llamada, el semáforo) |
| 6 | 300–359 | 300 ·0,77 · 315 ·0,75 · 330 · 345 | 0,68 | Acercamiento 2 («Después: …») y vuelta |
| 7 | 360–419 | 360 ·0,76 · 375 ·0,64 · 390 · 405 | 0,59 | Frase 3; toque «Marcar cumplido» |
| 8 | 420–479 | 420 ·0,75 · 435 ·0,61 · 450 · 465 | 0,59 | El reporte: «Contestó» |
| 9 | 480–539 | 480 ·0,67 · 495 ·0,67 · 510 · 525 | 0,59 | El comentario se escribe |
| 10 | 540–599 | 540 ·0,63 · 555 · 570 ·0,61 · 585 ·0,68 | 0,62 | El dedo baja a «Enviar reporte» |
| 11 | 600–659 | **600 ·0,93** (segunda subida) · 615 ·0,69 · 630 · 645 | 0,66 | Toque «Enviar reporte»: cumplido. Frase 3 sale |
| 12 | 660–719 | **660 ·0,90** · 675 ·0,89 · 690 ·0,76 · 705 ·0,68 | **0,81** | Acercamiento a «Ahora va en: …» (la prueba más fuerte) |
| 13 | 720–779 | **720 ·0,96** · 735 ·0,77 · 750 · 765 | 0,73 | Toque «Listo»; frase 4; la ventana se hace a un lado |
| 14 | 780–839 | 780 ·0,88 · 795 ·0,74 · 810 · 825 | 0,71 | Quieto; la subida; el dip |
| — | **840** ·1,00 | el golpe más fuerte de la pista | — | **La firma.** La música se va debajo de las campanas |

Corrección al STORY (que decía «segunda subida 20–24, golpes en 22,0 y 24,0»): la segunda subida empieza en **20,0 (cuadro 600, 0,93)** y
el compás más fuerte del cuerpo es el 12 (22–24). El toque «Enviar reporte» del guion ya estaba en 20,0: ahora cae sobre un golpe real.

---

## 1. Los números del estilo

### 1.1 Paleta (tokens de `identidad/kit.css`; nada fuera de esta lista)

| Papel | Token | Valor | Dónde puede aparecer |
|---|---|---|---|
| Fondo | `--k-noche` | `#060D1F` | A sangre, todo el cuerpo |
| Halo | `.k-halo` | azul `rgba(53,118,218,.45)` arriba a la derecha + dorado `rgba(217,162,52,.22)` abajo a la izquierda | Fondo, bajo todo |
| Puntos | `.k-puntos` | `rgba(169,190,235,.35)`, 2 px cada 42 px, desvanecidos hacia la izquierda (35 %) | Fondo; **nunca se mueven** |
| Tinta | `--k-noche-tinta` | `#EAF0FF` | Las frases |
| Tinta 2 | `--k-noche-tinta-2` | `#A9B6D6` | (`.k-feed-texto`; **no se usa en este clip**) |
| Acento | `--k-noche-dorado` | `#E8B95A` | Solo: la ceja «MEMBRESÍA», la palabra *ninguna*, el botón de la firma |
| Anillo | `--k-noche-linea` | `rgba(234,240,255,.12)` | El borde de la ventana |
| Fondo de la app | `--k-app-fondo` | `#FAF9FD` | Detrás de la grabación (nunca se ve, salvo un cuadro de carga) |
| Azul de marca | `--k-azul` | `#3576DA` | **Solo en la firma** (la baldosa) |
| Placa | `.k-datos-ejemplo` | `rgba(6,13,31,.72)` | La píldora «Datos de ejemplo» |
| Dip | — | `rgba(6,13,31,.40)` | Los 3 cuadros antes de la firma, solo sobre la ventana |

Los colores de la app (el verde del semáforo, el azul `#015BBE` de los botones) viven dentro de la grabación y no se tocan.

### 1.2 Tipografía

| Pieza | Clase (kit v1.1) | Familia · peso | 4:5 | 9:16 | Interlineado · tracking | Reglas |
|---|---|---|---|---|---|---|
| Frase | `.k-feed-frase` (`.k-titular` en 9:16 con `.k-vertical`) | Fraunces 560; `<em>` itálica 500 dorada | **80 px** | **104 px** | 1,04 · −0,02 em | Máx. **2 líneas**, saltos fijados a mano (§2.0). Izquierda, `text-wrap: balance` apagado (los saltos son nuestros). Sin sombra |
| Ceja | `.k-feed-ceja` (`.k-ceja`) | Inter 700, MAYÚSCULAS | **30 px** | **34 px** | 1 · +0,10 em | Una palabra: «MEMBRESÍA» |
| Datos de ejemplo | `.k-datos-ejemplo` | Inter 600 | 22 px, píldora de 40 px de alto, relleno 0 18 | igual | 1 · 0 | Blanca sobre la placa; dentro de la ventana, esquina superior derecha, a 24 px |
| Texto de la app | (grabación) | Inter de la app, 14 px CSS el cuerpo, 22 px los títulos | ≥ **31,6 px** en el cuadro | ≥ **34,5 px** | — | Nunca por debajo de 28 px en ningún encuadre (§1.5) |

Saltos de línea fijados (iguales en los dos formatos):
«Valeria llegó / el domingo.» · «Registrada. / Aun sin señal.» · «Y ya tiene quién / la llame» · «Que *ninguna* persona / se pierda».
Anchos estimados: 80 px ≈ 23 caracteres por línea en 888 px; 104 px ≈ 19 en 960 px. En 9:16 la frase 4 se parte «Que *ninguna* / persona se pierda».

### 1.3 Radios y sombras

| Pieza | Radio | Sombra / borde |
|---|---|---|
| `.k-ventana` | **28 px** | `0 0 0 1px var(--k-noche-linea)` + `0 40px 80px -24px rgba(0,0,0,.65)`; `overflow: hidden`; fondo `--k-app-fondo` |
| «Datos de ejemplo» | 999 px | ninguna |
| Frases y ceja | — | **ninguna** (nada de text-shadow ni brillo) |
| Firma | la del kit (`cierre-corto` / `cierre-clip`) | la del kit |

### 1.4 Disposición por formato

| | 4:5 (1080×1350) | 9:16 (1080×1920) |
|---|---|---|
| Márgenes | 96 a los lados, 72 arriba | 60 a los lados; banda útil **168–1330** (lo de la plataforma); debajo de 1330 solo halo y puntos |
| Ceja | x 96 · y 72 (30 px → termina en 108) | x 60 · y 188 (34 px → 229) |
| Frase | x 96 · y 124 · ancho 888 · 2 líneas de 83 px → termina en 290 | x 60 · y 236 · ancho 960 · 2 líneas de 108 px → 452 |
| Ventana | x 100 · y 360 · **880 × 1050**: **sangra 60 px por abajo** (se ve 880×990; las esquinas de abajo nunca aparecen) | x 60 · y 480 · **960 × 850** (480→1330), completa |
| Ventana al final (desde el cuadro 724) | escala **0,92** desde el centro inferior (la parte de arriba baja de 360 a 444) + x **+48** | escala 0,92 desde el centro superior (termina en 1262 < 1330) + x **+36** |
| Datos de ejemplo | dentro de la ventana, arriba a la derecha, a 24 px de los bordes | ídem |
| Firma | `cierre-clip` (kit v1.1, 1080×1350, 2,5 s) | `cierre-corto` (kit v1) |

La ventana ocupa el 81 % (4:5) y el 89 % (9:16) del ancho: la app es la protagonista; nunca un objeto chico en medio del vacío.

### 1.5 La cámara dentro de la ventana: escalas

La grabación llega a 3× (390×844 px CSS → **1170×2532 px**). Se mide en **ppc = píxeles del cuadro por píxel CSS del celular**. Tres niveles:

| Nivel | Qué se ve | 4:5: ppc (escala del video 3×) · ancho × alto visibles en px CSS | 9:16: ppc (escala) · visibles | Texto de la app 14 px → |
|---|---|---|---|---|
| **G** general | todo el ancho del celular | **2,256** (0,752) · 390 × 439 | **2,462** (0,821) · 390 × 345 | 31,6 px · 34,5 px |
| **G⁺** | el ancho de una tarjeta con sus márgenes | 2,436 (0,812) · 361 × 406 | 2,659 (0,886) · 361 × 320 | 34 px · 37 px |
| **M** medio | una zona de la tarjeta o del diálogo | **3,158** (1,053) · 279 × 313 | **3,446** (1,149) · 279 × 247 | 44 px · 48 px |
| **C** cerrado | una línea | **4,061** (1,354) · 217 × 244 | **4,431** (1,477) · 217 × 192 | 57 px · 62 px |

G = ×1,00 · G⁺ = ×1,08 · M = ×1,40 · C = ×1,80 sobre el general. En C la fuente de 3× se amplía 1,35–1,48×: aceptable en punch-ins de 1–2 s
(riesgo anotado en §5). Con la ventana a 0,92 (desde el cuadro 724) la cámara va en G⁺: el cuerpo de la app queda en 31,3 / 34 px (≥ 28).
El objetivo de cada movimiento es una **caja de `pasos.json`** (px CSS del viewport 390×844) centrada en la ventana, con la cámara
sujeta a los bordes del celular (nunca se ve fuera de la grabación). La cámara es un `scale` + `x`/`y` sobre un envoltorio dentro de la
ventana; el `<video>` nunca se transforma ni se busca.

### 1.6 Curvas y duraciones (cada tween lleva su curva por nombre)

| Papel | Curva | Cuadros | Detalle |
|---|---|---|---|
| `entrada-palabra` | `power4.out` | 4 | `filter: blur(6px) → 0` + opacidad 0 → 1; **sin desplazamiento**. Palabras a 2 cuadros (0,067 s), salvo la frase 1 (una por pulso) |
| `entrada-linea` | `power4.out` | 6 | la línea entera, blur 8 → 0 + opacidad (frase 2 y ceja) |
| `salida-texto` | `power3.in` | 4–5 | blur 0 → 8 + opacidad 1 → 0, la línea entera. Empieza 2–3 cuadros antes del pulso para que la entrada caiga en el pulso («blur swap»: el fondo no corta) |
| `camara` | `power2.inOut` | **14** | un movimiento por compás; después, quieta |
| `punch` | `power2.inOut` | **9** | solo el del cuadro 660 |
| `latigo-sale` / `latigo-llega` | `power3.in` / `power3.out` | 5 / 6 | y: 0 → −1100 (4:5) ∕ −1000 (9:16); la llegada desde +1100/+1000 → 0, aterriza a escala 1,04 → 1,00 (`power3.out`, 10 cuadros) |
| `iris` | `power2.out` | 5 | `clip-path: circle(0 at X Y) → circle(1400px at X Y)`, X Y = el centro del botón tocado (caja de `pasos.json`) en coordenadas de la ventana |
| `ventana-cambio` | `power2.inOut` | 15 | escala 1 → 0,92 + x (§1.4), 4 cuadros después de la frase 4 (movimiento secundario) |
| `halo` | `sine.out` | 90 | escala 1,08 → 1,00 al entrar cada mundo (cuadros 0, 180, 720); los puntos no se mueven |
| `dip` | escalón | 3 | capa `rgba(6,13,31,.40)` sobre la ventana, cuadros 837–839, sin curva |
| firma | las del kit | 75 | `back.out(2.2)` de la corona y compañía; **no se imita en el cuerpo** |
| resortes | ninguno | — | nada rebota salvo la corona del kit |
| velocidad de la grabación | carril `rate` en `data-automation` | — | entre **0,35× y 3,5×**; las rampas van entre acciones, nunca durante una letra o un toque |

Desenfoque de movimiento: `data-motion-blur="on"` con `data-motion-blur-shutter="180"` en la raíz de las dos composiciones (látigo, cámara y
desplazamientos de la app). **Nunca `filter: blur()` sobre la grabación**; el blur de CSS es solo para el texto.

### 1.7 Sonido

| Capa | Fuente | Nivel | Regla |
|---|---|---|---|
| Música | `assets/musica/product-launch-the-mountain.mp3`, `data-media-start` 14,05, dura 29,0 s (cuadros 0–869) | cama a **−18 LUFS** (kit.json: sin voz) | Desvanece bajo la firma: carril de volumen **1,00 en el 840 → 0,32 (−10 dB) en el 852 → 0 en el 870** (30 cuadros; la primera campana del 851 ya se oye limpia) |
| Sonidos de acción (kit v1.1) | `toque` 60–90 ms · `aparicion` 150–250 ms · `desliz` 300–400 ms · `subida` 1,8 s · `confirmacion` ~300 ms | relativos a la cama en ese instante: `toque` **+3 dB** (los dos toques clave, 121 y 601, **+5 dB**) · `aparicion` +2 · `desliz` 0 · `confirmacion` +5 · `subida` de −14 a +4 en su golpe | El pico suena **un cuadro después** de su imagen. `toque` rota tres tomas (a, b, c; si el kit entrega una sola, ±3 % de tono). **Sin tics de tecla**: la música es fuerte y el kit no los trae; la escritura la carga la imagen |
| Sonido de marca | `sonido-marca.mjs` (campanas, −20 LUFS, acentos 0 · 0,20 · 0,52) | tal cual | Lo pone el host en **28,38 s** (cuadro 851: firma + 0,38) |
| Mezcla | — | **−16 LUFS** integrados, pico real ≤ **−1 dBTP** | `npx hyperframes normalize-audio` y se comprueba con `npx hyperframes audio <render> --json` (medido, no oído) |

Veinte eventos de sonido en 30 s, ninguno sin causa visible; 0–6 s lleva ocho (la parte más densa). Ningún whoosh en los movimientos de cámara.

### 1.8 BANNED: los valores por defecto prohibidos, con nombre

1. **El fundido de 0,5 s con `power2.out` (o la curva sin nombrar de GSAP) para todo.** Cada tween lleva su curva de §1.6; nada entra solo por opacidad.
2. **Fade + deslizarse hacia arriba** como entrada de texto. Las palabras entran por blur, sin moverse.
3. **Zoom lineal** o `linear` en la cámara (`linear` solo valdría para rotación o progreso, y aquí no hay).
4. **El acercamiento lento y arrastrado** (1,0 → 1,08 en 8 s, que el STORY proponía para 12–20): es el «creeping scale» que delata un video generado. Se reemplaza por movimientos discretos de 14 cuadros en pulsos (§2, P4).
5. **Fundido cruzado entre mundos.** Solo las tres transiciones con causa: iris desde el toque, látigo vertical, dip + corte.
6. **Teléfono dibujado** alrededor de la grabación (también `.k-telefono`), bisel, barra de estado inventada, marco negro.
7. **Texto que se mueve mientras se lee; titulares que siguen derivando** después de aterrizar; «breathing» o pulsos en títulos o en la ventana.
8. **El logo en una esquina**, marca de agua, la corona antes del cuadro 840.
9. **Brillo, neón, destellos, lens flare, partículas, orbes.** El halo del kit es un degradado fijo que se asienta una vez por mundo; nunca late.
10. **Degradados nuevos** (morados, azules, mesh), **tarjetas de vidrio**, fondos distintos de la noche.
11. **Tres tarjetas en fila, rejillas de KPI, título sobre captura oscurecida, etiquetas «01 / 02», corner brackets, HUD.**
12. **Whoosh en cada corte** o en los movimientos de cámara; el mismo `toque` sin rotar; dings, chimes o tonos ajenos al kit.
13. **Reproducción de la app por encima de 3,5× o por debajo de 0,35×** (parece un glitch o un error).
14. **Retocar un píxel de la app:** ni resaltados, ni flechas, ni cursor dibujado en posproducción. El punto de toque viene de la grabación.
15. **Texto de la app por debajo de 28 px.** Ningún encuadre de §1.5 baja de 31 px.
16. **Centrarlo todo.** Las frases van a la izquierda, al margen; solo la ventana (el sujeto) va centrada.
17. **Cifras sin «Datos de ejemplo».** La píldora está desde el cuadro 0.
18. **Más de 3 s sin un cambio visible** en el cuerpo (`sweep_static`): el tramo más quieto (735–836) lleva el asentamiento del halo y la subida.
19. **Un pulso vacío entre los cuadros 0 y 360.** O aterriza una palabra, o cierra un campo, o aparece algo real de la app.
20. Del contrato de HyperFrames: `from()` en escenas (siempre `fromTo`), `autoAlpha`/`display` sobre un `.clip`, `transform` de CSS en un elemento que GSAP transforma, el `<video>` con tiempo y su envoltorio con tiempo a la vez.

Después del primer render, cada valor por defecto que aun así aparezca se nombra aquí y se corrige.

---

## 2. Los planos, cuadro por cuadro

### 2.0 Convenciones

- **G / G⁺ / M / C**: los niveles de §1.5. «Sobre X» = la caja de X (`pasos.json`) centrada en la ventana.
- **Pulso**: el cuadro de la grilla de §0. Un evento «en el 120» aterriza en el cuadro 120 (su sonido suena en el 121).
- **Grabación**: T1 (alta, cuenta 103), T3 (seguimiento, cuenta 103); T2 (asignar, cuenta 101) no sale en cámara (§3).
- **Textos de la app**: son los reales, verificados en `frontend-v2/public/i18n/es.json` y en la plantilla de Membresía
  (`backend/_datos/personas_catalogos.php`). Lo que no se puede saber hasta grabar lleva «(real)».
- Las frases siempre en el mismo lugar (§1.4); una frase a la vez; la ceja encima de la frase.
- **Corrección al STORY**: el flujo «Llegó a un culto» de la plantilla va `Llamada de bienvenida → Mensaje de bienvenida (automático) → Se
  conecta con una casa de paz → …`. Por eso «Después:» y «Ahora va en:» dicen **«Mensaje de bienvenida»**, no «Llega a la iglesia». Si en la
  demo el mensaje automático de WhatsApp está apagado, la ruta avanza sola al entrar al paso y dirá «Se conecta con una casa de paz». Las
  frases no dependen de ese texto; la cámara apunta a la línea, diga lo que diga.

### 2.1 Tabla maestra (todo lo que cambia, por cuadro)

| Cuadro | Pulso | La app (grabación) | Cámara | Texto | Sonido | Transición |
|---|---|---|---|---|---|---|
| **0** | ● | T1 · «Nueva persona»: el teléfono `5557654321` ya puesto (fuera de cámara), el campo «Nombres» con la **«V»** recién escrita, «Datos de ejemplo» en su esquina | G sobre la parte alta del formulario (título «Nueva persona», Nombres, Apellidos, Teléfono) | **«Valeria»** ya aterrizada (es la miniatura) | — | — |
| 5 · 10 · 15 · 20 · 25 · 30 | 15 ● | «a·l·e·r·i·a», una letra cada 5 cuadros (rate ≈ 0,42×); «Valeria» completo en el 30 | quieta | **«llegó»** en el 15 (entrada-palabra) | — | |
| 30 · 45 | 30 ● 45 ● | el punto de toque viaja a «Apellidos» (rate 2×) | quieta | **«el»** en el 30, **«domingo.»** en el 45. Frase 1 completa y muerta de quieta hasta el 117 | — | |
| **60** | ● | toque en «Apellidos»; «Cardona Ríos» a 2 cuadros por letra, 62–86 (rate ≈ 1,05×) | quieta | — | `toque` a (+3) en el 61 | |
| **90** | ● | toque en «Cómo llegó» → se abre el selector: grupo **«Eventos»** (Casa de Paz, Servicio General, Evangelismo, Discipulado, Encuentro) y **«Otras formas de llegar»** | quieta | — | `toque` b en el 91 | |
| 97 | | toque en la categoría del culto (**«Servicio General»**, nombre real en la demo) → aparece el nivel 2: **«¿A cuál Servicio General?»** con los eventos | quieta | — | — | |
| **105** | ● | toque en el evento **«Servicio General»** → el chip «elegido» (ícono `church` · Servicio General) | quieta | — | `aparicion` (+2) en el 108 | |
| 108–119 | | `sinRed: true` ya puesto: en la cabecera aparece el chip real **«Sin conexión: ves la última copia»**; la pantalla se desplaza suave hasta «Registrar» (rate 3×) | **Movimiento del compás 2**: G de la parte alta → G centrado en el centro del viewport (el diálogo aparecerá ahí), 108–119, 12 cuadros, power2.inOut | la frase 1 sale 117–121 (salida-texto) | `desliz` (0 dB) 109–120 | |
| **120** | **●●● bajo** | **toque en «Registrar»** | quieta (ya centrada) | **«Registrada. / Aun sin señal.»** entrada-linea 120–126 | **`toque` c (+5) en el 121**; `confirmacion` (+5) en el 123 | **Iris desde el toque** 120–125: debajo, un still del cuadro 119; encima, la grabación recortada por el círculo que crece desde el centro de «Registrar» |
| 125–149 | 135 ● | el diálogo real: **«Guardada en este dispositivo»** · «Valeria Cardona Ríos queda guardada aquí y se envía sola cuando haya señal.» · botón **«Entendido»** | quieta sobre el diálogo (G) | frase 2 quieta | — | |
| **150** | ● | toque en «Entendido» → el diálogo se cierra; el formulario queda listo para la siguiente persona | **Movimiento del compás 3**: G centrado → G sobre la cabecera (arriba), 150–163, 14 cuadros | | `toque` a en el 151 | |
| **165** | ● | en la cabecera aparece el botón real **«1 sin enviar»** (`#btn-pendientes`, ícono `schedule_send`) | quieta | | `aparicion` en el 166 | |
| 172–178 | | `sinRed: false`: vuelve la señal, el alta se envía sola y **«1 sin enviar» desaparece** (el chip «Sin conexión…» también) | quieta | la frase 2 sale 177–181 | — | |
| **176–186** | **180 ●●● pico** | el contenido del mundo 1 sube y se va (176–181, power3.in); el mundo 2 llega desde abajo (180–186, power3.out) y se asienta 1,04 → 1,00 (180–190). La ventana no se mueve: cambia lo que hay dentro | T3 llega en **G** sobre la tarjeta: encabezado «Mi seguimiento», pestaña **«Acompañados»**, el buscador con «Valeria», y la **tarjeta de Valeria Cardona Ríos**: paso **«Llamada de bienvenida»** (ícono `call`) · chip **«A tiempo»** (verde) · **«Desde hoy · vence en 3 días»** · **«Después: Mensaje de bienvenida»** · botones llamar, **«Marcar cumplido»**, «Dejar de acompañar» | — | **`desliz` (+3) en el 178** (el látigo) | **Látigo vertical**; halo a 1,08 → 1 (180–270) |
| **195** | ● | quieta (la tarjeta) | quieta | **«MEMBRESÍA»** entrada-linea 195–201 | `aparicion` (0) en el 196 | |
| **240** | ●● | quieta | **Movimiento del compás 5**: G → **M** sobre la mitad alta de la tarjeta (nombre, «Llamada de bienvenida», «A tiempo», «Desde hoy · vence en 3 días»), 240–253 | — | — | |
| **300** | ● | quieta | **Movimiento del compás 6**: M → **C** sobre la línea **«Después: Mensaje de bienvenida»**, 300–313 | — | — | |
| **345** | ● | quieta | vuelta C → **G** sobre la tarjeta (el botón «Marcar cumplido» a la vista), 345–359 | — | — | |
| **360** | ● | quieta | quieta | **«Y ya tiene quién / la llame»**: Y 360 · ya 362 · tiene 364 · quién 366 · la 368 · llame 370 (entrada-palabra; completa en el 374) | — | |
| **375** | ● | **toque en «Marcar cumplido»** | quieta | frase 3 quieta | `toque` b (+3) en el 376 | **Iris desde el toque** 375–380 (still del 374 debajo) |
| 380–389 | | el diálogo real **«Reporte del paso»** · «**Valeria Cardona Ríos** · Llamada de bienvenida» · sección «Llamada de bienvenida» · pregunta **«¿Cómo fue?»** con **Contestó / No contestó / Lo visité** · «Petición de oración» · «Observaciones» · **«Comentario (opcional)»** · botones **«Solo registrar el intento»** y **«Enviar reporte»** | quieta | | — | |
| **390** | ● | quieta | **Movimiento del compás 7**: G → **M** sobre «¿Cómo fue?» y sus tres opciones, 390–403 | | — | |
| **450** | ● | el punto de toque llega y **marca «Contestó»** (el radio se llena) | quieta | | `toque` c en el 451 | |
| **480** | ● | quieta | **Movimiento del compás 9**: M sobre la pregunta → **M** sobre «Comentario (opcional)», 480–493 | | — | |
| **495** | ● | toque en el campo | quieta | | `toque` a en el 496 | |
| 497–555 | 510 · 525 · 540 · 555 | se escribe **«Muy contenta, viene el domingo»** a 2 cuadros por letra (30 letras; rate ≈ 1,05×); la frase crece en el campo | **quieta** (ningún movimiento mientras se escribe) | frase 3 quieta | — (sin tics) | |
| **570** | ● | el punto de toque baja hacia los botones | **Movimiento del compás 10**: M del campo → **M** sobre los botones del diálogo, 570–583 | | — | |
| 585 | ● | el punto llega a «Enviar reporte» | quieta | | — | |
| **600** | **●●● 2.ª subida** | **toque en «Enviar reporte»** → el resultado: ícono `task_alt` · **««Llamada de bienvenida» cumplido»** (texto real, con comillas angulares) · **«Ahora va en: Mensaje de bienvenida»** · botón **«Listo»** (y «Elegir otro paso», real) | **Movimiento del compás 11**: M de los botones → **M** sobre el bloque del resultado (ícono, título, «Ahora va en», «Listo»), 600–613 | la frase 3 sale 597–601 | **`toque` b (+5) en el 601**; **`confirmacion` (+5) en el 603** | |
| **660** | **●●● golpe** | quieta | **Punch** M → **C** sobre la línea **«Ahora va en: Mensaje de bienvenida»** con el botón «Listo» a la vista, 660–668, 9 cuadros | — | — | |
| 690 | ● | el punto de toque va a «Listo» | quieta | | — | |
| **720** | **●●● golpe** | **toque en «Listo»** → el diálogo se cierra; la tarjeta ya dice **«Mensaje de bienvenida» · «A tiempo» · «Desde hoy · vence mañana» · «Después: Se conecta con una casa de paz»** | **Movimiento del compás 13**: C → **G⁺** sobre la tarjeta, 720–733 | **«Que *ninguna* persona / se pierda»**: Que 720 · *ninguna* 722 · persona 724 · se 726 · pierda 728 (completa en el 732). **La ceja sale 720–723** | `toque` c en el 721 | **La ventana se hace a un lado**: escala 1 → 0,92 + x (§1.4), 724–738; halo a 1,08 → 1 (720–810) |
| 735–836 | 735 · 750 … 825 | quieta (la tarjeta real) | quieta | frase 4 quieta ≥ 3,6 s | **`subida`** de −14 dB en el 786 a +4 dB en su golpe del 840 | |
| **837–839** | | — | — | — | — | **Dip**: la ventana al 40 % de oscuridad, 3 cuadros |
| **840** | **●●● el más fuerte** | — | — | — | la música cae de 1,00 a 0,32 (840–852) y a 0 (870) | **Corte a la firma**: 9:16 `cierre-corto`, 4:5 `cierre-clip`; variables `llamado: prueba`, `fondo: azul`, `idioma: es` |
| 846 · 853 ↓ | | la K sube (0,20 s de la firma); las 7 barras de la corona desde el 0,45 (cada 0,05 s, `back.out(2.2)`) | | «Kingdom» 0,75 s; botón **«Prueba gratis 30 días»** 0,95 s | **Campanas en el 851** (28,38 s); acentos 851 · 857 · 867 | |
| **914** | | último cuadro: la corona completa y el botón | | | silencio de música desde el 870 | fin |

### 2.2 Los siete planos

#### P1 · «La puerta» — cuadros 0–119 (compases 1–2) · pulsos 0, 15, 30, 45, 60, 75, 90, 105

- **Grabación:** T1 desde el cuadro de la tecla «V» en «Nombres» hasta el final del desplazamiento a «Registrar». Rampas: 0,42× en «Valeria»,
  2× en el viaje del dedo, 1,05× en «Cardona Ríos», 1× en el selector, 3× en el desplazamiento. Entrada y salida se ajustan al grabar.
- **Encuadre 4:5:** G, la ventana muestra 439 px CSS de alto: el título «Nueva persona», Nombres, Apellidos, Teléfono. **9:16:** G, 345 px CSS:
  el título y los tres campos; si no caben, la cámara arranca 40 px más abajo para que entren Nombres y Apellidos.
- **Cámara:** quieta hasta el 108; del 108 al 119 baja al centro del viewport (compás 2). Nada más.
- **Texto:** frase 1 por pulsos (la primera palabra ya puesta en el cuadro 0); sale 117–121.
- **Sonido:** toque 61, toque 91, aparicion 108, desliz 109–120.
- **Transición:** ninguna dentro; cierra con el toque del 120.
- **Válvula si en la vista previa va atropellado:** «Cómo llegó» pasa a estar elegido antes del cuadro 0 (como el teléfono) y el compás 2 se
  queda con «Apellidos» y el desplazamiento. La frase y los pulsos no cambian.

#### P2 · «Guardada aun sin señal» — cuadros 120–179 (compás 3) · pulsos 120 (bajo), 135, 150, 165

- **Grabación:** T1 desde el toque en «Registrar» hasta que desaparece «1 sin enviar». Rampas: 1× en el diálogo, 2× en las esperas.
- **Encuadre:** G centrado en el diálogo (120–149); G sobre la cabecera (desde el 163). Igual en los dos formatos; en 9:16 el diálogo entra
  completo porque mide ≈ 300 px CSS.
- **Cámara:** quieta en el iris; un movimiento (150–163) hacia la cabecera para que «1 sin enviar» aparezca ya encuadrado.
- **Texto:** frase 2 entra 120–126 (línea entera), sale 177–181.
- **Sonido:** toque 121 (+5), confirmacion 123, toque 151, aparicion 166.
- **Transición:** iris desde «Registrar» (120–125) al entrar; látigo (176–186) al salir.

#### P3 · «Mi seguimiento: la tarjeta» — cuadros 180–359 (compases 4–6) · pulsos 180 (pico), 195, 240, 300, 345

- **Grabación:** T3 desde la tarjeta de Valeria ya en pantalla (después de buscar «Valeria», fuera de cámara) hasta antes del toque en
  «Marcar cumplido». La toma es estática: 3,5 s grabados cubren 6,5 s del clip a 0,5× sin que se note (nada se mueve en la app).
- **Encuadre 4:5:** G con la tarjeta a 24 px del borde superior de la ventana (encabezado + pestañas + buscador quedan arriba, recortados si
  hace falta). **9:16:** G, la tarjeta ocupa el centro; el encabezado puede quedar fuera.
- **Cámara:** llega con el látigo (1,04 → 1,00); 240–253 a M (mitad alta de la tarjeta); 300–313 a C («Después: …»); 345–359 vuelve a G.
- **Texto:** la ceja «MEMBRESÍA» 195–201; sin frase (los movimientos de cámara son el espectáculo).
- **Sonido:** desliz 178 (látigo), aparicion 196 (ceja).
- **Transición:** látigo al entrar; ninguna al salir (la frase 3 cae sobre la misma imagen).

#### P4 · «El reporte» — cuadros 360–599 (compases 7–10) · pulsos 360, 375, 390, 450, 480, 495, 570, 585

- **Grabación:** T3 desde el toque en «Marcar cumplido» hasta el cuadro anterior al toque en «Enviar reporte». Rampas: 1× en los toques y en
  la escritura (ya es 70 ms por tecla), 2–3× en las pausas de la herramienta.
- **Encuadre:** el diálogo «Reporte del paso» no cabe entero en la ventana (≈ 600 px CSS): la cámara lo recorre **por partes y en pulsos**,
  nunca en un paneo continuo: M sobre la pregunta (390), M sobre el comentario (480), M sobre los botones (570). En 9:16 los mismos objetivos.
- **Cámara:** tres movimientos de 14 cuadros, uno por compás (7, 9 y 10); el compás 8 es solo la app marcando «Contestó».
- **Texto:** frase 3 entra 360–374 (seis palabras a 2 cuadros); sale 597–601.
- **Sonido:** toque 376, toque 451, toque 496.
- **Transición:** iris desde «Marcar cumplido» (375–380).

#### P5 · «Cumplido y el siguiente paso» — cuadros 600–719 (compases 11–12) · pulsos 600 (subida), 660 (golpe), 690

- **Grabación:** T3 desde el toque en «Enviar reporte» hasta el cuadro anterior al toque en «Listo» (el resultado se graba con 3 s de pausa).
- **Encuadre:** M sobre el bloque del resultado (600–613); C sobre «Ahora va en: …» con «Listo» a la vista (660–668). En 9:16 igual; a C se
  ven 192 px CSS de alto: la línea y el botón caben (≈ 120 px CSS).
- **Cámara:** el movimiento del compás 11 (600–613) y el punch del 660 (9 cuadros). Quieta el resto.
- **Texto:** ninguno (la prueba la da la app).
- **Sonido:** toque 601 (+5), confirmacion 603.
- **Transición:** ninguna; cierra con el toque del 720.

#### P6 · «Que ninguna persona se pierda» — cuadros 720–839 (compases 13–14) · pulsos 720 (golpe), 735, 750, 765, 780, 795, 810, 825

- **Grabación:** T3 desde el toque en «Listo» hasta el final (la tarjeta actualizada, 4 s de pausa grabada; se sostiene a 1×).
- **Encuadre:** G⁺ sobre la tarjeta actualizada, con la ventana a 0,92 y corrida (§1.4). En 4:5 la ventana baja (la parte de arriba a 444) y
  deja aire bajo la frase; en 9:16 se encoge desde arriba y termina en 1262.
- **Cámara:** 720–733 a G⁺; después muerta de quieta. El halo se asienta 720–810.
- **Texto:** frase 4 entra 720–732 (*ninguna* en itálica dorada: el único dorado del cuerpo junto a la ceja); la ceja sale 720–723; la frase
  se sostiene 3,6 s.
- **Sonido:** toque 721; subida 786–840.
- **Transición:** dip 837–839 y corte duro al 840.
- **Opcional (si la tarjeta final no se lee bien):** la ficha de Valeria con su tarjeta «Avance» (T4 de §3) en vez de la tarjeta de la lista.
  Cambia solo esta grabación; la frase, la cámara y los tiempos quedan.

#### P7 · «La firma» — cuadros 840–914

- 9:16: `identidad/cierre-corto.html`; 4:5: `identidad/cierre-clip.html` (kit v1.1, misma línea de tiempo: baldosa 0–0,45 s, K 0,20, corona
  desde 0,45 cada 0,05 s, «Kingdom» 0,75, botón 0,95). Variables `{"llamado":"prueba","fondo":"azul","idioma":"es"}`.
- Campanas en 28,38 (cuadro 851). La música: 1,00 → 0,32 (840–852) → 0 (870).
- Es el único gesto de marca del clip. Nada del cuerpo imita la corona.

---

## 3. Las grabaciones: la escena `tools/ayuda/escenas/clips/membresia-valeria.mjs`

Una sola escena de **celular** (`movil: true`: viewport 390×844 a 3× → cuadros de **1170×2532 px**, 30 cps), con `capturar.mjs --modo video`
sobre Kingdom Demo en español (`node capturar.mjs clips/membresia-valeria --idioma es --modo video`). Sale
`salida/video/es/clips/membresia-valeria/grabacion.mp4` + `pasos.json` (inicio y fin de cada paso, su `tramo` y la **caja** del elemento: de
ahí salen los objetivos de la cámara). Datos ficticios; «Valeria Cardona Ríos» y su teléfono `5557654321` no existen en la demo.

**Lo que este clip necesita del modo video de celular (en construcción):**

1. Cuadros a la densidad real (3×), como ya hace el escritorio con `--force-device-scale-factor`; JPEG 95 → H.264 CRF 16 a 30 cps.
2. **Un punto de toque en vez de la flecha** de `cursor.js`: círculo de 20 px CSS, relleno `rgba(27,27,31,.28)`, borde 1,5 px blanco al 70 %,
   visible desde 4 cuadros antes del toque hasta 6 después, más la onda que ya existe (36 → 58 px, 450 ms, `#015BBE` al 90 %). Sin flecha.
3. `pasos.json` con `caja` en px CSS del viewport 390×844 y los `tramo`; `sinRed` como hoy (`context.setOffline`).
4. La carpeta `escenas/clips/` (el patrón `<seccion>/<articulo>` ya acepta `clips/membresia-valeria`); `pantallas` y `refs` como en las de la ayuda.
5. Tema claro, zona horaria de la sede, idioma de la cuenta; la entrada del primer paso antes de grabar (como hoy).

**Cuentas:** 101 = el administrador (Andrés Felipe Restrepo Gómez), que coordina; 103 = el servidor (Jorge Gallego Gil), acompañante.

**refs** (consultas sobre la base restaurada; cambian con la semilla del día):
- `jorge`: `SELECT id_persona FROM kd_usuario_sedes WHERE id_usuario = 103 AND estado = 'activo' LIMIT 1`.
- `catCulto` y `evCulto`: la categoría y el id del evento **«Servicio General»** (`ev_eventos` de la sede KDEMO); en la demo la categoría del culto
  se llama como el evento (`_demo_plantilla.php`). Si el nombre difiere, el selector usa `[data-categoria="{@catCulto}"]` y `[data-evento="{@evCulto}"]`.

**Pasos** (la herramienta espera 900 ms tras cada acción salvo `pausa`; 1,5 s sobre cada `captura`). Lo marcado «fuera de cámara» se graba pero
no se usa:

| # | Tramo | Paso | Qué se ve / ritmo | Dura ≈ |
|---|---|---|---|---|
| 1 | `alta` | `{ como: 103, ir: '/servir/membresia/nueva', espera: '#campo-nombres' }` | el formulario vacío (antes de grabar) | — |
| 2 | | `{ escribir: { en: '#campo-telefono', texto: '5557654321' }, pausa: 300 }` | **fuera de cámara**: el teléfono queda puesto (sin duplicados: el 555 no existe) | 1,2 s |
| 3 | | `{ clicSiHay: '#genero-F', pausa: 300 }` | **fuera de cámara**, solo si «Registrar» exige género | 0,6 s |
| 4 | | `{ escribir: { en: '#campo-nombres', texto: 'Valeria' }, pausa: 300 }` | **cuadro 0 del clip = la «V»**; 70 ms por tecla (el montaje la baja a 0,42×) | 1,0 s |
| 5 | | `{ escribir: { en: '#campo-apellidos', texto: 'Cardona Ríos' }, pausa: 300 }` | 12 teclas | 1,4 s |
| 6 | | `{ elegir: { en: '#campo-forma', opcion: 'Servicio General' } }` | se abre el selector («Eventos» / «Otras formas de llegar»), se toca la categoría; 600 ms abierto | 2,0 s |
| 7 | | `{ clic: '.nivel2 button.evento[data-evento="{@evCulto}"]' }` | «¿A cuál Servicio General?» → el evento → el chip elegido | 1,5 s |
| 8 | | `{ sinRed: true }` | el chip «Sin conexión: ves la última copia» en la cabecera | 0,3 s |
| 9 | | `{ ver: '#btn-guardar-persona' }` | desplazamiento suave (900 ms) hasta «Registrar» | 1,8 s |
| 10 | | `{ clic: '#btn-guardar-persona', espera: 'mat-dialog-container', captura: 'guardada' }` | **el toque del 120**; el diálogo «Guardada en este dispositivo» se queda 1,5 s | 2,5 s |
| 11 | | `{ clic: 'mat-dialog-container #btn-ok', oculto: 'mat-dialog-container' }` | «Entendido»; el formulario se limpia | 1,2 s |
| 12 | | `{ espera: '#btn-pendientes', pausa: 1200 }` | «1 sin enviar» en la cabecera | 1,5 s |
| 13 | | `{ sinRed: false }`, `{ oculto: '#btn-pendientes', pausa: 1200 }` | vuelve la señal; la cola envía; el contador se va | 1,5–3 s |
| 14 | `asignar` | `{ como: 101, ir: '/servir/membresia/coordinar', espera: '#indicadores' }` | **fuera de cámara** (todo el tramo) | 2 s |
| 15 | | `{ clic: '#sec-nuevos', espera: '#bolsa-nuevos li' }` | «Nuevos»: Valeria sin acompañante | 1,5 s |
| 16 | | `{ clic: '#bolsa-nuevos li:has-text("Valeria Cardona") button.asignar', espera: '#dialogo-asignar' }` | «¿Quién acompaña a Valeria Cardona Ríos?» | 1,5 s |
| 17 | | `{ marcar: '#dialogo-asignar mat-radio-button[data-acompanante="{@jorge}"]' }` | Jorge Gallego Gil («Acompaña a n de m»; si dice «Sin cupo» igual se puede elegir) | 1,2 s |
| 18 | | `{ clic: '#btn-confirmar-asignar', oculto: '#dialogo-asignar' }` | asignado | 1,2 s |
| 19 | `seguimiento` | `{ como: 103, ir: '/servir/membresia/seguimiento', espera: '#lista-seguimiento app-ruta-persona-item' }` | Mi seguimiento → «Acompañados» | 2 s |
| 20 | | `{ escribir: { en: '#buscar-seguimiento', texto: 'Valeria' }, espera: 'app-ruta-persona-item:has-text("Valeria Cardona")' }` | **fuera de cámara**: la tarjeta sube a lo alto de la lista | 1,5 s |
| 21 | `tarjeta` | `{ ver: 'app-ruta-persona-item:has-text("Valeria Cardona")', bloque: 'start', pausa: 3500 }` | **el mundo 2 empieza aquí (cuadro 180)**: la tarjeta quieta 3,5 s («Llamada de bienvenida» · «A tiempo» · «Desde hoy · vence en 3 días» · «Después: Mensaje de bienvenida») | 4,4 s |
| 22 | | `{ ver: 'app-ruta-persona-item:has-text("Valeria Cardona") p.detalle:has-text("Después")', pausa: 200 }` | solo para la **caja** de la línea «Después: …» (objetivo del 300; la tarjeta tiene dos `p.detalle`: la primera es «Desde hoy · vence en 3 días») | 1,1 s |
| 23 | `reporte` | `{ clic: 'app-ruta-persona-item:has-text("Valeria Cardona") button.cumplido', espera: '#dialogo-reporte .pregunta', pausa: 1500 }` | **el toque del 375**; «Reporte del paso» | 2,5 s |
| 24 | | `{ marcar: '#dialogo-reporte .pregunta >> nth=0 >> mat-radio-button >> nth=0', pausa: 1200 }` | «Contestó» (el toque del 450) | 2,0 s |
| 25 | | `{ escribir: { en: '#campo-comentario', texto: 'Muy contenta, viene el domingo' }, pausa: 1200 }` | «Comentario (opcional)»; 30 teclas a 70 ms | 3,5 s |
| 26 | `resultado` | `{ ver: '#btn-enviar-reporte', pausa: 400 }` | el dedo baja a los botones (caja de «Enviar reporte») | 1,3 s |
| 27 | | `{ clic: '#btn-enviar-reporte', espera: '#resultado-reporte', captura: 'cumplido', pausa: 3000 }` | **el toque del 600**; «“Llamada de bienvenida” cumplido» · «Ahora va en: Mensaje de bienvenida» · «Listo»; quieto 3 s | 4,5 s |
| 28 | | `{ ver: '#siguiente-propuesto', pausa: 200 }` | solo para la **caja** de «Ahora va en: …» (objetivo del 660) | 1,1 s |
| 29 | `tarjeta-final` | `{ clic: '#btn-aceptar-siguiente', oculto: '#dialogo-reporte' }` | **el toque del 720**; la lista se refresca | 1,5 s |
| 30 | | `{ ver: 'app-ruta-persona-item:has-text("Valeria Cardona")', bloque: 'start', pausa: 4000 }` | la tarjeta actualizada («Mensaje de bienvenida» · «A tiempo» · «Desde hoy · vence mañana» · «Después: Se conecta con una casa de paz»), 4 s quieta | 5 s |
| 31 | `ficha` (opcional) | el menú de la tarjeta → «Ver ficha» (`a[mat-menu-item]:has-text("Ver ficha")`), `espera: '#ficha-nombre'`, `pausa: 3000` | la ficha de Valeria con su tarjeta «Avance», por si P6 la prefiere | 5 s |

Totales: T1 ≈ 17 s, T2 ≈ 8 s (no sale), T3 ≈ 28 s, T4 ≈ 5 s → ≈ 60 s de grabación para 28 s de clip. `consolaEsperada: ['ERR_INTERNET_DISCONNECTED']`.
`pantallas`: `nueva.page.ts`, `origen-campo.component.ts`, `membresia-cabecera.component.ts`, `coordinar.page.ts`, `ruta-asignar.component.ts`,
`seguimiento.page.ts`, `ruta-persona-item.component.ts`, `ruta-reporte.component.ts`, `formulario-responder.component.ts`.

**Plan B para el tramo `asignar`:** si Coordinar no se usa bien a 390 px, la escena se parte en dos archivos y la segunda (`seguimiento`) crea
y asigna a Valeria con el gancho `sql` de la escena (corre tras restaurar el volcado) antes de sus pasos: `mem_personas` + `mem_persona_ruta`
(flujo «Llegó a un culto», paso «Llamada de bienvenida», `paso_desde = NOW()`) + `mem_acompanamientos` con `{@jorge}`. Se pierde la
continuidad del alta real en la misma corrida, pero no se ve en cámara.

**Para la vista previa de los stills del iris:** los cuadros 119 y 374 de cada ventana se exportan (`ffmpeg -ss <t> -frames:v 1`) desde la
grabación al tiempo de origen correspondiente y van como `<img>` propios (`assets/stills/`).

---

## 4. Lo que se revisa en la vista previa (el dueño mira esto)

Cuadros a mirar: `npx hyperframes snapshot --at 0,1.5,3.6,4.0,4.2,5.5,6.0,6.2,8.5,10.5,12.5,13.3,15.1,18,20.0,20.1,22.3,24.0,24.5,27.9,28.0,28.4,30.4`
en las dos composiciones, y `snapshot --range 5.8,6.3 --frames 16` para el látigo.

1. **Cuadro 0 (la miniatura):** la ventana con «Nueva persona» y la «V» escrita, «Valeria» en Fraunces ya puesta, «Datos de ejemplo» en su
   esquina. Nunca negro, nunca la marca. En 9:16, nada por encima de 168 ni por debajo de 1330 salvo halo y puntos.
2. **Cuadro 45:** las cuatro palabras aterrizadas y muertas de quietas; «Valeria» completo en el campo. **Cuadro 108:** el chip real «Sin
   conexión: ves la última copia» en la cabecera.
3. **Cuadro 120:** el toque en «Registrar» exactamente con el bajo; el círculo del iris nace del botón; la frase 2 entera en el 126.
   **165:** «1 sin enviar» a la vista; **178:** ya no está.
4. **176–186:** el látigo: ningún cuadro muestra los dos mundos a medias con el marco roto; la ventana no se mueve, solo lo de adentro. La
   ceja cae en el 195 y no antes.
5. **Cuadro 253:** M sobre la tarjeta: «Valeria Cardona Ríos», «Llamada de bienvenida», «A tiempo» en verde, «Desde hoy · vence en 3 días»,
   todo ≥ 44 px. **313:** C sobre «Después: Mensaje de bienvenida» (o lo que la app diga).
6. **360–374:** la frase 3 palabra a palabra sobre la tarjeta quieta; **380:** «Reporte del paso» abierto desde el toque.
7. **451:** «Contestó» marcado; **497–555:** la escritura se lee a ≥ 44 px y **la cámara no se mueve** mientras se escribe.
8. **600–613:** el toque en «Enviar reporte» con la segunda subida; `task_alt` y «“Llamada de bienvenida” cumplido»; la frase 3 ya no está.
9. **668:** C sobre «Ahora va en: …» a ≥ 57 px con «Listo» visible. Es la prueba más fuerte: debe leerse de un vistazo.
10. **720–738:** «Listo» en el golpe; la frase 4 aterrizada en el 732 con *ninguna* dorada; la ceja fuera; la ventana ya a 0,92 y corrida en el 738.
11. **738–836:** nada se mueve salvo el halo que se asienta; la frase 4 quieta ≥ 3,6 s. **837–839:** el dip al 40 %. **840:** el primer cuadro de la
    firma (la baldosa creciendo), sin un cuadro de noche vacía entre medias.
12. **Sonido (medido, no oído):** cada `toque` un cuadro después de su imagen; las campanas en el 851; la música a −10 dB en el 852 y a 0 en el
    870; −16 LUFS, pico ≤ −1 dBTP; ningún tramo con dos sonidos de acción encimados salvo 601 + 603.
13. **Textos:** ninguna palabra que no esté en la app o en las cuatro frases; ningún texto de la app < 28 px; las frases en 2 líneas en los dos
    formatos; `npx hyperframes check` en 0 errores (contraste AA incluido); las cifras siempre con «Datos de ejemplo».
14. **La historia sin sonido:** se entiende con la pantalla en silencio (así se verá en el feed): llegó → registrada sin señal → alguien la
    llama → el siguiente paso → ninguna se pierde → Kingdom.

---

## 5. Riesgos y lo que se decide al grabar

- **El siguiente paso real es «Mensaje de bienvenida»** (automático), no «Llega a la iglesia» como decía el STORY. Lo honesto es dejarlo: muestra
  que Kingdom hace solo el mensaje. Si el dueño prefiere «Llega a la iglesia», la única forma de llegar de la plantilla que lo da de segundo
  es «Evangelismo en la calle» o la forma «Otra» (flujo General), y Valeria «llegó el domingo»: cambiaría el gancho. Decisión del dueño.
- **Coordinar a 390 px** (tramo `asignar`, fuera de cámara): puede renderizar apretado; hay plan B con `sql` (§3). Jorge (103) es «el
  acompañante con más personas a cargo» y puede estar «Sin cupo»: el radio se deja elegir igual.
- **Los textos de hoy en la tarjeta** («Desde hoy · vence en 3 días») se confirman en la grabación: dependen de `plazo_dias = 3` del paso.
- **Densidad de 0–6 s:** ocho sonidos y cinco acciones en seis segundos. La válvula de P1 y quitar el `toque` del 151 están listas.
- **La ampliación en C** (1,35–1,48× de la fuente de 3×) se ve blanda en 1–2 s; si molesta, C baja a ×1,6 (texto ≥ 50 px, sigue sobrado).
- **Dos cosas nuevas del kit v1.1 y una de la herramienta** antes de construir: `cierre-clip` (4:5), `.k-ventana`, `.k-feed-*`, los cinco
  sonidos de acción, y el modo video de celular con el punto de toque. Sin el modo video de celular no hay grabación; sin `cierre-clip` el 4:5
  no cierra.
- **Las cifras de Kingdom Demo cambian con cada semilla**: ninguna frase depende de un número; el contador «1 sin enviar» siempre será 1.
- **Idiomas (en, pt después):** la misma escena con `--idioma en` graba la interfaz en inglés; las frases se traducen y los saltos de línea se
  vuelven a fijar; la firma lleva `idioma`.
