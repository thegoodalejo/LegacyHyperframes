# frame-wiki — sistema visual del Tipo Wiki (kit v1)

Derivado de KingdomApp `docs/videos/identidad.md` (fuente de verdad). Lo aplica cada tutorial de la ayuda: **no se reescribe por proyecto**.
Cambiarlo es cambiar el kit (decisión del dueño, sube la versión). Los componentes están en `kit.css` (clases `.k-*`).

## Lienzo

- 1920×1080, 30 cps. Fondo de la app `#FAF9FD` en la intro y el cierre (tema claro de v2).
- Tipografía local (`fuentes/fuentes.css`): **Inter** para todo y **Fraunces** solo para la palabra «Kingdom». Nada de fuentes del
  sistema ni de íconos como fuente: los íconos son SVG de Material Symbols (`iconos/`).
- El host enlaza `identidad/fuentes/fuentes.css` y `identidad/kit.css` en su `<head>`, una sola vez.

## Estructura de un tutorial

| Parte | Duración | Qué se ve |
|---|---|---|
| Intro (`intro-wiki.html`) | 3,0 s | La corona se levanta en el centro: baldosa azul, sube la K y las 7 barras de la corona, una tras otra (sonido de marca a 0,38 s). El favicon va a la izquierda junto a «Kingdom» (Fraunces) / «Ayuda» o «Help», el chip de la sección y el título con su subrayado |
| Cuerpo | 1–4 min | Escenas de la grabación real de la app (Kingdom Demo) sobre el escenario. Cortes directos entre escenas |
| Cierre (`cierre-wiki.html`) | 4,0 s (2,5 s sin «Sigue con») | Tarjeta «Sigue con:» / «Up next:» con el artículo siguiente y el chip; luego la corona se levanta otra vez junto a «Kingdom» y «Encuentra esta guía y más en la Ayuda de la app»; se funde al fondo. Sin URL |

Variables de la intro: `titulo` (el del artículo), `seccion` (`empieza`, `mi-iglesia`, `membresia`, `eventos`, `equipos`, `academia`,
`portal`, `comunicaciones`, `archivos`, `ajustes`, `soporte`, `puesta`; las de `frontend-v2/src/ayuda/secciones.json`) e `idioma` (`es`,
`en`). El cierre: `siguiente` (vacío = sin tarjeta), `seccion` e `idioma`.

## Escenario del cuerpo (`kit.css`)

| Elemento | Clase | Posición | Estilo |
|---|---|---|---|
| Fondo | `.k-escenario` | todo el lienzo | `#EEF1F8` (el segundo fondo del sitio) |
| Grabación de la app | `.k-pantalla` | x 192, y 72, 1536×864 (0,8 de 1920×1080) | Radio 16 px, borde `#C4C6D0` de 1 px y sombra `0 10px 32px rgba(14,26,51,.12)` |
| Llamada | `.k-llamada > span` | x 192, y 14, alto 46 px (encima de la grabación, sin taparla) | Píldora `#015BBE` (primario de la app), texto blanco Inter 600 30 px; entra con 0,3 s de bajada y opacidad |
| Subtítulos | `.k-subtitulo > span` | franja inferior (14 px del borde, 96 px a cada lado) | Inter 500 40 px, interlineado 1,3, blanco sobre `#1B1B1F` al 80 %, radio 12 px, máximo 2 líneas (≈84 caracteres), centrados |

- La llamada dice el **nombre exacto** que muestra la pantalla («Nuevo evento», «Guardar»), como los artículos.
- La llamada usa el primario en todas las secciones; el color de la sección va en el chip y el subrayado de la intro y en el chip del cierre.
- Contraste: la llamada (blanco sobre `#015BBE`, 6,5:1) y los subtítulos pasan WCAG AA (lo verifica `check`).
- Sin acercamientos en v1: a 0,8 el texto de la app se lee a 1080p. Los acercamientos se agregan cuando una guía los necesite, con
  `/hyperframes-keyframes`.
- Tareas de celular (1080×1920): la grabación del celular de referencia en `.k-telefono` y los textos de `frame-corto.md`, con la intro y el
  cierre de este tipo adaptados cuando se haga el primero (sube la versión).

## Audio

- Voz Kokoro local por idioma (`kit.json`: `ef_dora` a 1,1 en español, `af_heart` a 1,0 en inglés), −16 LUFS; 0,25 s entre frases. La voz empieza **después** de la intro.
- Sonido de marca (`sonido-marca.mjs`, propio) a −20 LUFS, solo en la intro y el cierre, en los segundos de `kit.json`.
- Sin música en el Tipo Wiki.
- Salida final: AAC 160 kbps, 48 kHz, −16 LUFS integrados.
