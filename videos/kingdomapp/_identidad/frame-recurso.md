---
version: v1.2
name: Kingdom — Frame del Tipo Recurso (16:9, 5–7 min)
description: >
  Sistema visual de los videos «Recursos» de Kingdom (decisión 239): videos largos, de 5 a 7 minutos, que el dueño comparte por WhatsApp a
  pastores y líderes que ya usan la app. Son motion design puro con la marca, SIN la app grabada (excepción a la regla 1 de las directivas,
  decidida por el dueño): la noche del sitio con su halo y su retícula de puntos, Fraunces para titulares, Inter para el texto, íconos SVG
  de Material Symbols, diagramas abstractos y tipografía cinética que sigue la voz Kokoro, todo al pulso de «Product Launch» en bucle.
  Lo arma _herramientas/recurso.mjs desde guion.mjs; el kit trae intro-recurso, capitulo-recurso, cierre-recurso, recurso.js y kit.css.
unit: el cuadro — 1920×1080, 30 cps
principle: la marca es sagrada · el movimiento sigue a la música y a la voz · nada quieto · ningún dato inventado · la app no aparece

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
`rocket_launch`, `cloud`, `tune`, `support_agent`, `construction`.

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

## Approved Entities

- Nombre: **Kingdom** (nunca «Kingdom App»). Módulos con su nombre en la app: Membresía, Eventos, Academia, Mi iglesia, Portal,
  Comunicaciones, Equipos, Eventos masivos, Archivos y Compartir. Solo funciones que existen (KingdomApp `docs/modulos-app.md` y la ayuda).
- Llamados del cierre (`llamado`): `acompanamiento` («Te acompañamos a mejorar los procesos de tu iglesia»), `compartir` («Comparte este
  video con tu equipo») o `ninguno`. Contacto (`contacto`): `whatsapp` (+57 300 471 2642, el del sitio), `sitio` o `ninguno`.

## Qué NO hacer

- **Nada de la app:** ni grabaciones, ni pantallas redibujadas, ni teléfonos o computadores dibujados, ni «interfaces» inventadas que se
  parezcan a la app.
- **Nada inventado:** ninguna cifra de resultados («crecimos un 40 %»), ningún testimonio, ninguna iglesia ni persona real, ninguna función
  que no exista. Las cifras que ilustran un tablero son de ejemplo y lo dicen («Datos de ejemplo»).
- Nada de emojis, degradados de «IA», logos de terceros (WhatsApp se nombra, no se dibuja), fotos de banco ni ilustraciones de personas.
- Nada de texto bajo 28 px, de párrafos en pantalla ni de subtítulos quemados (van en el VTT).
- Ningún `Math.random()` sin semilla, `Date.now()`, temporizador o animación infinita.

## Pre-Render Self-Audit

- [ ] `npx --yes hyperframes@0.8.221 check` en 0 errores (contraste AA incluido). `line_unread` en una frase cinética es un aviso: la frase
      se lee mientras se oye; si molesta, deja solo las palabras clave.
- [ ] Snapshot en la mitad de cada escena (los segundos los imprime `preparar`) y la hoja de contacto revisada: nada de la app, todas las
      cifras con «Datos de ejemplo», nada quieto.
- [ ] `preparar` dice que la música queda 18–24 dB por debajo de la voz; `entregar` verifica −16 LUFS y pico ≤ −1,5 dBTP.
- [ ] Duración total entre 5 y 7 min.
