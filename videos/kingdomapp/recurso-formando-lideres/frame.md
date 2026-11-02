---
version: v1.3
name: Kingdom — Frame del Tipo Recurso (16:9, 5–7 min)
description: >
  Sistema visual de los videos «Recursos» de Kingdom (decisión 239): videos largos, de 5 a 7 minutos, que el dueño comparte por WhatsApp a
  pastores y líderes que ya usan la app. Son motion design puro con la marca, SIN la app grabada (excepción a la regla 1 de las directivas,
  decidida por el dueño): la noche del sitio con su halo y su retícula de puntos, Fraunces para titulares, Inter para el texto, íconos SVG
  de Material Symbols, diagramas abstractos y tipografía cinética que sigue la voz Kokoro, todo al pulso de «Product Launch» en bucle.
  Lo arma _herramientas/recurso.mjs desde guion.mjs; el kit trae intro-recurso, capitulo-recurso, cierre-recurso, recurso.js y kit.css.
unit: el cuadro — 1920×1080, 30 cps
principle: la marca es sagrada · el movimiento sigue a la música y a la voz · nada quieto · ningún dato inventado · la app no aparece en los Recursos de pastores; en «Para líderes» (v1.3) se recrea fiel

colors:
  noche: "#060D1F"
  noche-2: "#0C1A3A"
  tinta: "#EAF0FF"
  tinta-2: "#A9B6D6"
  dorado: "#E8B95A"
  azul-marca: "#3576DA"
  verde-suave: "#26A69A"
  linea: "rgba(234, 240, 255, 0.12)"
  punto-tenue: "rgba(169, 182, 214, 0.35)"
  claro: "#F7F8FC"
  claro-tinta: "#0E1A33"
  claro-tinta-2: "#46526D"
  claro-dorado: "#7D5800"

typography:
  marca:     { fontFamily: "Fraunces", px: 64, weight: 600, use: "solo en la intro y el cierre del kit" }
  titular:   { fontFamily: "Fraunces", px: 96, weight: 560, lineHeight: 1.04, tracking: "-0.02em", class: ".k-recurso-titular", max: "2 líneas" }
  frase:     { fontFamily: "Fraunces", px: 72, weight: 560, lineHeight: 1.1, class: ".k-recurso-frase", use: "tipografía cinética que sigue la voz" }
  gigante:   { fontFamily: "Fraunces", px: 168, weight: 560, class: ".k-recurso-gigante", use: "una palabra o una cifra de ejemplo que golpea en un pico" }
  enfasis:   { fontFamily: "Fraunces", italic: true, weight: 500, color: "dorado", use: "<em> o *palabra* en guion.mjs; 1–3 palabras" }
  ceja:      { fontFamily: "Inter", px: 28, weight: 700, tracking: "0.16em", upper: true, color: "dorado", class: ".k-recurso-ceja" }
  texto:     { fontFamily: "Inter", px: 40, weight: 500, lineHeight: 1.35, color: "tinta-2", class: ".k-recurso-texto" }
  etiqueta:  { fontFamily: "Inter", px: 30, weight: 600, color: "tinta-2", class: ".k-recurso-etiqueta" }
  contador:  { fontFamily: "Fraunces", px: 160, weight: 600, numerals: "tabular", class: ".k-recurso-contador" }
  datos:     { fontFamily: "Inter", px: 28, weight: 600, class: ".k-datos-ejemplo.k-recurso-datos", text: "Datos de ejemplo" }
  app:       { fontFamily: "Inter", use: "solo en la app recreada de «Para líderes» (v1.3): la tipografía de Material 3 de la app, en px lógicos (.k-app-t-*)" }

components:
  fondo:      "identidad/fondo-recurso.html (kit), que monta el host debajo de todo el cuerpo: noche, halo que respira y puntos quietos; las escenas son transparentes"
  zona:       ".k-recurso-zona: 192 px a los lados, 108 px arriba y abajo (80 % seguro para títulos)"
  capitulo:   "identidad/capitulo-recurso.html (kit) con `capitulo: { numero, titulo, bajada, icono, fondo }` en guion.mjs; 3–6 s, sin voz"
  icono:      ".k-recurso-icono con --k-icono: url(identidad/iconos/<nombre>.svg) (toma el color del texto; .k-recurso-icono-oro). La regla de la máscara (`-webkit-mask` y `mask: var(--k-icono) center / contain no-repeat`) se repite en el <style> de cada composición: la de kit.css sale vacía en el render aunque el snapshot la muestre (ver kit.css)"
  punto:      ".k-recurso-punto (+ .k-oro, .k-azul, .k-verde, .k-tenue): una persona"
  nodo:       ".k-recurso-nodo (+ .k-oro): una red, una célula, un grupo, un equipo (con un ícono dentro)"
  linea:      ".k-recurso-linea (+ .k-oro) en un <svg>: vínculos, rutas; se dibujan con strokeDashoffset"
  tarjeta:    ".k-recurso-tarjeta: una idea, un paso o un dato sobre la noche (nunca una pantalla de la app)"
  grafica:    ".k-recurso-barra (+ .k-oro) sobre .k-recurso-eje; contadores con .k-recurso-contador; SIEMPRE .k-datos-ejemplo"
  palabra:    ".k-recurso-palabra (y .k-recurso-clave en dorado): una caja por palabra; el espacio es su margen"
  intro:      "identidad/intro-recurso.html (6 s), con el título y la ceja"
  cierre:     "identidad/cierre-recurso.html (9 s con «Sigue con», 6 s sin él), cuadro final del video"
  app:        "v1.3, solo «Para líderes»: .k-app-* (la app v2 recreada: barras, riel, pestañas, chips, campos, botones, tarjetas, filas, diálogo, hoja, cifras, barras de tablero, notificación) dentro de .k-telefono.k-app-telefono o .k-ventana.k-ventana-escritorio"
  dedo:       "v1.3: .k-dedo con su .k-dedo-onda (KRecurso.app.tocar)"
  foco:       "v1.3: .k-foco, el resto al 55 % y el anillo dorado (KRecurso.app.foco)"
---

# Kingdom — Frame del Tipo Recurso

## Adaptación de marca (LEER PRIMERO)

El frontmatter es normativo: los hex, las letras y los pesos se usan tal cual. La fuente de verdad es KingdomApp `docs/videos/identidad.md`
y `docs/videos/README.md` → «Tipo 5. Recurso». Este archivo se copia como `frame.md` del proyecto (queda montado en
`identidad/frame-recurso.md`) **antes** de entrar al flujo de HyperFrames, y **no se edita por video**: lo distinto de un video se resuelve
en sus composiciones.

## Overview

Un Recurso le habla a un pastor o a un líder que **ya usa Kingdom**: le explica una forma de trabajar (medir lo que pasa en la iglesia,
llevar un evento de ciudad, recibir a los nuevos) con calma y claridad, en 5 a 7 minutos. No vende ni enseña pantallas: muestra **ideas**.
El tono es pastoral y seguro; la noche del sitio da el aire de «presentación» y el movimiento, siempre al pulso de la música, mantiene la
atención durante minutos sin cansar.

## The Frame

- **Noche siempre.** El host monta `fondo-recurso` (noche, halo que respira, retícula de puntos quieta) debajo de todo el cuerpo; cada escena va
  transparente encima. Así no hay saltos de fondo entre escenas.
- **Capítulos en claro, solo como respiro.** La tarjeta de capítulo admite `fondo: 'claro'`; úsala a lo sumo dos veces por video, en el
  cambio de tema más grande (por ejemplo, el paso del problema a la forma de trabajar). Nunca escenas con voz en claro.
- **Zonas seguras:** todo lo que se lee, dentro de `.k-recurso-zona` (192 px a los lados, 108 px arriba y abajo). Los subtítulos no se
  queman (van en el VTT), así que el tercio de abajo queda libre para la composición, pero nada clave pegado al borde.
- **Densidad:** una idea por escena. Como máximo un titular (o la frase cinética), un diagrama y una etiqueta. Si hacen falta tres bloques
  de texto, son dos escenas.
- **Dos columnas** como base: el texto a la izquierda (x 192–1050) y el diagrama a la derecha (x 1080–1728); para un golpe grande, una sola
  cosa centrada (`.k-recurso-gigante`, un contador, un nodo).
- **Contraste AA** en todo el texto (lo comprueba `check`): tinta y tinta-2 sobre la noche, el dorado solo en énfasis y cejas; sobre claro,
  el dorado de texto es `#7D5800`.

## La gramática de escenas (sin la app)

| Pieza | Para qué | Cómo |
|---|---|---|
| **Tarjeta de capítulo** | Abrir cada parte (3–5 por video) | `capitulo: { numero, titulo, bajada?, icono?, fondo? }`, 4 s, sin voz; entra en un compás y la música sube debajo |
| **Tipografía cinética que sigue la voz** | Que la idea se lea mientras se oye | Cada palabra en su `.k-recurso-palabra`, entrando en `T.palabra(i, j).inicio − 0,08`; las `*claves*` del guion en dorado (`.k-recurso-clave`). Mejor **solo las palabras clave** o una frase corta que resume, no el párrafo: los subtítulos completos van en el VTT |
| **Íconos** | Nombrar un módulo o una acción | SVG de Material Symbols de `identidad/iconos/` como máscara (`.k-recurso-icono`). Hay 74 (la lista está abajo). Otro ícono se baja de la misma fuente (`licencias.md`) y sube la versión del kit |
| **Personas como puntos** | Una iglesia, los nuevos, los que sirven | `.k-recurso-punto`; posiciones con semilla fija (nunca `Math.random()` sin semilla); el punto dorado es «la persona» del relato |
| **Redes y células como nodos** | Estructura, grupos, equipos, líderes | `.k-recurso-nodo` con un ícono dentro, unidos por `.k-recurso-linea` en un `<svg>` que se dibuja (`strokeDashoffset`) |
| **Rutas y embudos** | Un camino (llega → se afirma → sirve), un proceso | Nodos en fila con una línea que avanza; los puntos viajan por la ruta en pulsos; un embudo es una ruta que se estrecha. Etiquetas con los nombres de la app (Mi seguimiento, la ruta de crecimiento…) solo si existen |
| **Tableros y gráficas** | Que se vea que algo se puede medir | `.k-recurso-barra` sobre `.k-recurso-eje`, contadores `.k-recurso-contador` que suben (GSAP sobre un objeto con `onUpdate`). **Siempre** «Datos de ejemplo» (`.k-datos-ejemplo.k-recurso-datos`) mientras haya una cifra en pantalla |
| **Tarjetas** | Un paso, una pregunta, una idea | `.k-recurso-tarjeta`, entran una a una con `T.reparto(n, desde, hasta)` |
| **Golpe** | El cambio más grande del capítulo | Una palabra `.k-recurso-gigante` o el contador, en un pico de la música (`T.golpes`) |

Íconos en `identidad/iconos/`: `person`, `person_add`, `groups`, `groups_3`, `group_add`, `diversity_1`, `diversity_3`, `family_restroom`,
`church`, `home`, `door_open`, `waving_hand`, `handshake`, `volunteer_activism`, `favorite`, `event`, `event_available`, `calendar_month`,
`calendar_today`, `schedule`, `confirmation_number`, `qr_code_2`, `how_to_reg`, `stadium`, `school`, `menu_book`, `workspace_premium`,
`campaign`, `forum`, `chat`, `chat_bubble`, `mail`, `send`, `notifications`, `share`, `language`, `public`, `map`, `location_on`,
`person_pin_circle`, `travel_explore`, `route`, `flag`, `star`, `verified`, `check_circle`, `task_alt`, `done_all`, `edit_note`, `assignment`,
`badge`, `format_list_bulleted`, `filter_alt`, `dashboard`, `monitoring`, `insights`, `bar_chart`, `query_stats`, `trending_up`,
`stacked_line_chart`, `visibility`, `lightbulb`, `hub`, `account_tree`, `sync`, `wifi_off`, `celebration`, `arrow_forward`, `play_circle`,
`rocket_launch`, `cloud`, `tune`, `support_agent`, `construction`. Desde la v1.3 (los de la app recreada y su estrategia): `apps`, `help`,
`checklist`, `auto_awesome`, `cleaning_services`, `upload_file`, `error`, `phone_missed`, `assignment_late`, `fact_check`, `pause_circle`,
`person_remove`, `cottage`, `person_search`, `expand_more`, `arrow_drop_down`, `call`, `more_vert`, `search`, `close`, `hourglass_top`,
`download`, `add`, `sort`, `image`, `picture_as_pdf`, `content_copy`, `arrow_back`, `bolt`, `fullscreen`, `hearing`, `timer`, `event_busy`,
`smartphone`, `lock`, `all_inclusive`, `ring_volume`, `military_tech`, `table_view`, `filter_alt_off`, `radio_button_checked`,
`radio_button_unchecked` y `edit` (117 en total).

Recetas de movimiento que encajan (en `/hyperframes-animation`): `kinetic-type-beats`, `svg-path-draw`, `counting-dynamic-scale`,
`stat-bars-and-fills`, `constellation-hub`, `avatar-cloud-network`, `waterfall-entry`, `discrete-text-sequence`.

## Motion

- **Todo se programa con los tiempos, no con números a mano.** Al empezar el script de la escena: `const T = KRecurso.tiempos(window);`
  (`window` dentro de la escena es el suyo, con sus variables). Las frases, las palabras, los pulsos, los compases y los golpes están ahí.
- **Ritmo:** un cambio visual cada 2–4 s (una palabra que entra, un punto que aparece, una línea que se dibuja) y nada quieto más de ~6 s
  (si una frase es larga, que algo respire: el diagrama deriva, algo late en un pulso).
- **En la música:** cortes y transiciones en un **pulso** (`T.pulso(t)`); los cambios grandes (una escena nueva, un número que crece, el
  anillo que se forma) en un **compás** (`T.compas(t)`) o en un **golpe** (`T.golpes`). Las escenas ya empiezan en un pulso, y las tarjetas
  de capítulo en un compás.
- **Con la voz:** el texto entra un poco antes de oírse (−0,08 s) y sale justo antes de la frase siguiente (`T.frases[i + 1].inicio − 0,3`).
  La palabra que la voz enfatiza (las `*claves*`) puede iluminarse o disparar algo en el diagrama en el pulso más cercano.
- **Entradas:** subir 24–40 px con opacidad y un desenfoque de 6 px que se va, `power3.out` de 0,35 a 0,6 s; escalas con `back.out(1.8–2.4)`
  solo en cosas pequeñas (puntos, íconos). **Salidas** en los últimos 0,5 s de la escena (`T.salida()`): subir o ir a la izquierda con
  desenfoque, `power2.in`.
- **La firma** («la corona se levanta») solo en la intro y el cierre del kit; no se imita en el cuerpo.
- Nada de giros, rebotes grandes, destellos, partículas ni acercamientos bruscos. `fromTo` siempre, con `immediateRender: false` cuando se
  repite un `fromTo` sobre el mismo elemento.

## Estructura de un episodio (5–7 min)

1. `intro-recurso` (6 s; la arma el host).
2. **Apertura** (20–40 s, con voz): la situación del pastor o del líder, sin dramatizar.
3. **3–5 capítulos**, cada uno con su tarjeta (4 s) y 2–4 escenas con voz de 15–40 s.
4. **Resumen** (20–30 s): las ideas en tarjetas o en la ruta completa.
5. `cierre-recurso` (9 s con «Sigue con»; lo arma el host), con el llamado y el contacto.

La voz `ef_dora` a 1,1 va rápida (de 3,5 a 4,9 palabras por segundo en la muestra), así que el guion usa frases cortas y `pausa` de 0,5 a
0,8 s entre ideas; 6 minutos llevan unas 800–1000 palabras. Una escena con voz de más de ~40 s se parte en dos.

## Para líderes (v1.3, decisión 241)

Variante del Tipo Recurso para los **líderes de departamento** (el primero, afirmación o consolidación; el segundo, este, Academia). Mezcla lo estratégico (las escenas
de siempre, en motion design) con lo técnico: **la app de Kingdom v2 recreada en HTML, fiel**, y manipulada con animación (un dedo que
toca, campos que se escriben, la cámara que se acerca y se mueve, un foco que oscurece el resto, hojas y diálogos que suben). No es una
grabación de pantalla: es la interfaz rearmada con las piezas `.k-app-*` de `kit.css` y movida con `KRecurso.app` de `recurso.js`. El dueño
la aprobó el 2026-11-01 (decisión 241); antes estaba prohibida. En `guion.mjs`: `para: ['lideres']`, `seccion: 'lideres'` y
`departamento` (lista cerrada en `recurso.mjs`, hoy `afirmacion` y `academia`; este video lleva `academia`).

### Reglas de fidelidad (obligatorias)

1. **Estructura y textos de las capturas reales** de la ayuda (Kingdom Demo; las URL están en KingdomApp
   `frontend-v2/src/ayuda/medios.json`), copiadas al proyecto en `assets/referencias/` (fuera de git).
   - Se copian iguales el orden de los elementos, las etiquetas, los íconos (Material Symbols Outlined), las pestañas, los chips y los botones.
   - Los textos salen de la captura o de `frontend-v2/public/i18n/es.json`, **nunca de memoria**. Donde la clave lleva `{v_acompanante}`, va
     «Acompañante» (el vocabulario por defecto).
   - Lo que no tiene captura se arma con los componentes y los textos de la ayuda y de i18n (y se dice en el SPEC), nunca se inventa.
2. **Colores y forma de la marca por defecto** (`frontend-v2/src/styles/_tokens.scss`, tema claro), que es lo que ve una iglesia sin
   colores propios: primario `#015BBE` y su contenedor `#D7E2FF`; secundario `#7D5800` y su contenedor `#FFDEA9` (el chip elegido);
   superficie `#FAF9FD`, texto `#1B1B1F`, contenedor de superficie `#EFEDF1` y borde `#C4C6D0`. Inter; tarjetas de radio 16, diálogos de 28,
   chips en píldora. Las capturas de Kingdom Demo son violetas porque esa iglesia tiene marca propia: esa diferencia es la única de color
   permitida. En la barra superior, el logo K de Kingdom y el nombre de la iglesia.
3. **Celular:** `.k-telefono.k-app-telefono`, 390 × 812 px lógicos a 1,05 (409 × 853 en el cuadro). Barra superior (logo, nombre, apps,
   campana, ayuda y la cuenta) y barra inferior (Inicio, Mi iglesia y Perfil). **Nunca un teléfono con el aparato dibujado.**
4. **Computador:** `.k-ventana.k-ventana-escritorio` (1440 × 760) con 1440 × 760 px lógicos a 1 (las capturas de escritorio son de 1440 px): riel izquierdo (Inicio, Ajustes, Mi
   iglesia, Perfil), barra superior y las pestañas del módulo.
5. **Gestos y cámara** (todo con `KRecurso.app`, sobre la única línea de tiempo en pausa, determinista y buscable):
   - `tocar()`: el `.k-dedo` cae en el elemento, se hunde con su onda y el elemento queda presionado 120 ms.
   - `escribir()`: el campo se enfoca, la etiqueta sube y el texto aparece letra por letra con su cursor.
   - `camara()`: acercamientos de 1,0 a 1,8 y paneos, `power2.inOut` de 0,8 a 1,2 s; `desliz()` es el desplazamiento de la página.
   - `foco()`: el resto de la pantalla al 55 % y un anillo dorado redondeado sobre el elemento.
   - `hoja()`: las hojas suben y los diálogos aparecen como en Material 3, con su velo.
   - El gesto cae en el pulso de la palabra que lo nombra (`T.pulso(H.palabra(f, /…/).inicio)`).
6. **Los datos:** personas ficticias (las del BRIEF) y fechas en el formato de la app. Toda cifra visible (cupos, conteos, embudo) lleva
   `.k-datos-ejemplo` en la escena.
7. **Prohibido:** pantallas o funciones que no estén en las capturas ni en la ayuda; teléfonos con el aparato dibujado; logos de terceros
   (Google y WhatsApp se nombran, no se dibujan); y lo que el BRIEF del video pida no nombrar.

### Antes del render: la hoja de fidelidad

Snapshot de cada escena de la app en sus momentos clave y una hoja de contacto con **cada snapshot junto a su captura de referencia**
(`snapshots/fidelidad-*.png`). Se revisa y se corrige hasta que coincidan textos, orden, íconos y forma; solo quedan las diferencias
permitidas (el color de la marca, los datos de ejemplo y lo que el SPEC arma con los textos de la ayuda). Y después del render, un fotograma
de cada escena sacado del MP4 con ffmpeg: las máscaras de los íconos (`.k-recurso-icono`, `.k-app-icono`) se repiten en el `<style>` de
cada composición porque las de `kit.css` salen vacías en el render aunque el snapshot las muestre.

### Composición de una escena de la app

- La app ocupa una columna (el celular a la derecha, x ≈ 1150–1560) y el texto cinético corto la otra; o la ventana del computador debajo
  de un titular. La cámara mueve la app, no la escena.
- Las piezas de la app se escriben en el HTML de la escena (se leen y se comparan con la captura); el script solo arma la línea de tiempo.
- El texto de la app es pequeño (14–16 px lógicos): `check` avisa `text_below_floor` en esas escenas y es esperado (la app se ve como es);
  lo que importa se acerca con la cámara y el foco. Todo texto del kit encima de la app sigue con su piso de 28 px.

## Approved Entities

- Nombre: **Kingdom** (nunca «Kingdom App»). Módulos con su nombre en la app: Membresía, Eventos, Academia, Mi iglesia, Portal,
  Comunicaciones, Equipos, Eventos masivos, Archivos y Compartir. Solo funciones que existen (KingdomApp `docs/modulos-app.md` y la ayuda).
- Llamados del cierre (`llamado`): `acompanamiento` («Te acompañamos a mejorar los procesos de tu iglesia»), `compartir` («Comparte este
  video con tu equipo») o `ninguno`. Contacto (`contacto`): `whatsapp` (+57 300 471 2642, el del sitio), `sitio` o `ninguno`.

## Qué NO hacer

- **Nada de la app en los Recursos de pastores:** ni grabaciones, ni pantallas redibujadas, ni teléfonos o computadores dibujados, ni
  «interfaces» inventadas que se parezcan a la app. La variante «Para líderes» (v1.3, decisión 241) sí la recrea, fiel a las capturas y con
  las reglas de arriba; nunca grabada, nunca inventada y nunca dentro de un aparato dibujado.
- **Nada inventado:** ninguna cifra de resultados («crecimos un 40 %»), ningún testimonio, ninguna iglesia ni persona real, ninguna función
  que no exista. Las cifras que ilustran un tablero son de ejemplo y lo dicen («Datos de ejemplo»).
- Nada de emojis, degradados de «IA», logos de terceros (WhatsApp se nombra, no se dibuja), fotos de banco ni ilustraciones de personas.
- Nada de texto bajo 28 px (salvo el de la app recreada de «Para líderes», que va a su tamaño real), de párrafos en pantalla ni de
  subtítulos quemados (van en el VTT).
- Ningún `Math.random()` sin semilla, `Date.now()`, temporizador o animación infinita.

## Pre-Render Self-Audit

- [ ] `npx --yes hyperframes@0.8.221 check` en 0 errores (contraste AA incluido). `line_unread` en una frase cinética es un aviso: la frase
      se lee mientras se oye; si molesta, deja solo las palabras clave.
- [ ] Snapshot en la mitad de cada escena (los segundos los imprime `preparar`) y la hoja de contacto revisada: nada de la app (o, en «Para líderes», la
      hoja de fidelidad con cada captura al lado), todas las cifras con «Datos de ejemplo», nada quieto.
- [ ] `preparar` dice que la música queda 18–24 dB por debajo de la voz; `entregar` verifica −16 LUFS y pico ≤ −1,5 dBTP.
- [ ] Duración total entre 5 y 7 min.

## Este video: «Formando líderes con Kingdom» (Para líderes · Academia)

Lo de arriba es el frame del kit (`identidad/frame-recurso.md`), igual para todos los Recursos. Lo propio de este video, que se resuelve en
sus composiciones sin cambiar el kit:

- **Para quién:** el líder de la academia (clases de la visión, escuela bíblica, instituto) de una iglesia que ya usa Kingdom, y sus
  profesores. Estrategia sobre 2 Timoteo 2:2, en palabras propias: en pantalla solo la cita «2 Timoteo 2:2», nunca el texto de una versión.
- **Escenas y dónde va la app:**

| Escena | Forma | Pantallas (capturas en `assets/referencias/academia__*`) |
|---|---|---|
| `gancho`, `formar`, `resumen`, `llamado` | Motion design | — (`formar`: las cuatro generaciones Pablo → Timoteo → fieles → otros y la escalera Miembro → Discípulo → Líder) |
| `orden` | Escritorio | Cursos (catálogo con chips de categoría), Ajustes → Categorías y Programas, Inscribir → «Pueden tomarlo» |
| `curso` | Escritorio | El asistente de cinco pasos, el diálogo del pensum de Excel (sin captura: `pensum-dialog.component.ts`), «Pegar texto» del banco y el material |
| `enlinea` | Escritorio y celular | El constructor de lecciones y la lección del alumno |
| `asistencia`, `calificar`, `alumno` | Celular | Hoy, el código de cuatro números, notas, evaluaciones, entregas, Faltaron; Mis cursos del alumno |
| `aplazar` | Escritorio y celular | «Fechas», el diálogo «Aplazar o mover» y el aviso «Tu clase cambió de fecha» |
| `graduar` | Escritorio | Cerrar y graduar, Por aprobar y el certificado con QR |
| `multiplicar` | Escritorio y motion design | El Tablero de Academia, el profesor del grupo y vuelve el gráfico de las generaciones |

- **Colores:** la marca por defecto (azul) en toda la app recreada. Las categorías conservan **su propio color** (el que la iglesia les da:
  Visión `#6A1B9A`, Servicio `#00897B`, Biblia `#1565C0` en la demo); eso no es la marca de Kingdom Demo y se respeta.
- **Íconos que el kit no trae:** los de la app de Academia que faltan en `identidad/iconos/` (por ejemplo `local_library`, `settings`) van
  en `assets/iconos/`, bajados de la misma fuente del kit (Material Symbols Outlined, 48 px, `licencias.md`). Propuesta: subirlos al kit en
  su próxima versión.
- **Personas de ejemplo:** el profesor Jorge Gallego Gil, la alumna Lucía Ruiz Montoya, y Andrea Perea, Camilo Carmona, Mariana Arias y
  Esteban Ospina. Toda cifra en pantalla, con «Datos de ejemplo».
