# frame-wiki — sistema visual del Tipo Wiki (kit v1)

Derivado de LegacyEnterprise `docs/videos/identidad.md` (fuente de verdad). Lo aplica `../_herramientas/tutorial-wiki.mjs` al generar cada
tutorial: **no se reescribe por proyecto**. Cambiarlo es cambiar el kit (decisión del dueño, sube la versión).

## Lienzo

- 1920×1080, 30 cps. Fondo de la app `#FBF8FD` en la intro y el cierre.
- Tipografía **Inter** local (`identidad/fuentes/inter.css`), pesos 400–700. Nada de fuentes del sistema ni de íconos como fuente.

## Estructura de un tutorial

| Parte | Duración | Qué se ve |
|---|---|---|
| Intro (`intro-wiki.html`) | 3,0 s | El favicon se arma pieza por pieza (baldosa, tres bloques blancos, círculo menta + sonido de marca a 0,95 s), va a la izquierda junto a «Legacy Enterprise» / «Ayuda» (o «Help»), el chip del módulo y el título con su subrayado |
| Cuerpo | 1–4 min | Escenas de la grabación real sobre el escenario (abajo). Cortes directos entre escenas |
| Cierre (`cierre-wiki.html`) | 4,0 s (2,5 s sin «Sigue con») | Tarjeta «Sigue con:» / «Up next:» con el artículo siguiente y el chip; luego el favicon armado (sonido de marca) con «Legacy Enterprise» y «Encuentra esta guía y más en la Ayuda de la app»; se funde al fondo. Sin URL |

## Escenario del cuerpo

| Elemento | Posición | Estilo |
|---|---|---|
| Fondo | todo el lienzo | `#ECEAF1` |
| Grabación de la app | x 192, y 72, 1536×864 (0,8 de 1920×1080) | Radio 16 px, borde `#C7C5D0` de 1 px y sombra `0 10px 32px rgba(27,27,31,.12)` |
| Llamada | x 192, y 14, alto 46 px (encima de la grabación, sin taparla) | Píldora `#4555B7` (primario de la app), texto blanco Inter 600 30 px; entra con 0,3 s de subida y opacidad |
| Subtítulos | franja inferior (14 px del borde, 96 px a cada lado) | Inter 500 40 px, interlineado 1,3, blanco sobre `#1B1B1F` al 80 %, radio 12 px, máximo 2 líneas (≈84 caracteres), centrados |

- Contraste: la llamada (`#FFFFFF` sobre `#4555B7`) y los subtítulos pasan WCAG AA (lo verifica `check`).
- La llamada usa el primario en todos los módulos; el color del módulo va en el chip de la intro y del cierre.
- Sin acercamientos en v1: a 0,8 el texto de la app se lee a 1080p. Los acercamientos (punch-in con las cajas de `pasos.json`) se agregan cuando
  una guía los necesite, siguiendo `/hyperframes-keyframes`.

## Audio

- Voz Kokoro local por idioma (`kit.json`: `em_alex` / `af_heart`, velocidad 1,0), −16 LUFS.
- Sonido de marca (Kenney `confirmation_002`, CC0) a −20 LUFS, solo en la intro y el cierre.
- Sin música en el Tipo Wiki.
- Salida final: AAC 160 kbps, 48 kHz, −16 LUFS integrados.
