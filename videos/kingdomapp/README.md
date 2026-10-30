# Videos de Kingdom

Videos de **Kingdom** (la app para iglesias) hechos con HyperFrames. Las directivas (tres tipos: Wiki, Comercial y Corto; la app real; datos
ficticios; aprobaciones) y la identidad viven en el repo de la app: `KingdomApp/docs/videos/README.md` y `KingdomApp/docs/videos/identidad.md`.
Este directorio tiene el **kit de identidad** que todos los videos montan y las muestras que lo prueban.

## Qué hay aquí

| Carpeta | Qué es |
|---|---|
| `_identidad/` | Kit de identidad **v1.1**: intro y cierre del Tipo Wiki, cierres de marca del Comercial (16:9), del Corto (9:16) y del clip (4:5), `kit.json`, `kit.css` (con `.k-ventana` y `.k-feed-*`), `frame-wiki.md`, `frame-comercial.md`, `frame-corto.md`, favicon, Inter y Fraunces, íconos de sección, `sonido-marca.mjs`, `sonidos-accion.mjs`, `musica/` (las pistas, fuera de git, y el mapa de pulsos de «Product Launch») y licencias. **No se edita por video** |
| `_herramientas/montar-kit.mjs` | Copia el kit en `<proyecto>/identidad/`, comprueba el favicon contra la app, genera el sonido de marca a −20 LUFS y los sonidos de acción con su nivel de mezcla |
| `muestra-kit/` | Muestra 16:9: intro Wiki → cuerpo con una captura real de la ayuda → cierre Wiki → cierre del Comercial |
| `muestra-corto/` | Muestra 9:16: una escena de Corto con los componentes de `kit.css` → cierre del Corto |
| `muestra-clip/` | Muestra 4:5 (v1.1): la app real en `.k-ventana` con la cámara dentro, una frase con `.k-feed-*`, sonidos de acción sobre «Product Launch» → `cierre-clip` |
| `<tipo>-<tema>/` | Un proyecto por video: `wiki-eventos-crear-y-editar`, `clip-sitio-membresia`, `comercial-iglesia-ordenada`, `corto-asistencia-sin-papel` |

Los videos anteriores (`../kingdomapp-promo`, `../kingdomapp-afirmar-nuevo`) son de antes del kit: recrean la app y usan otra marca. No se
toman como referencia visual.

En git va solo el código del video. Capturas, voces, música, renders, hojas de contacto y el `identidad/` montado quedan fuera (`.gitignore`).

## Requisitos de esta máquina

- Node 22, FFmpeg y el CLI fijado por `npx`: `hyperframes@0.8.62` en las muestras v1 y la Wiki (el mismo de los videos de
  LegacyEnterprise); `hyperframes@0.8.221` en los clips del sitio y `muestra-clip`.
- Voz: `../../.venv-tts/` y el modelo Kokoro (ver `../legacyenterprise/README.md`).
- KingdomApp al lado (`F:\Proyectos\KingdomApp`, o la variable `KINGDOMAPP_REPO`): `montar-kit.mjs` compara el favicon del kit con
  `frontend-v2/public/favicon.svg` y se detiene si la app cambió de marca.

## Usar el kit en un proyecto

1. Crear la carpeta `<tipo>-<tema>/` con `BRIEF.md` (con la línea `tipo:`), `hyperframes.json` y un `package.json` con el script
   `"kit": "node ../_herramientas/montar-kit.mjs"` (copiar los de `muestra-kit/`).
2. `npm run kit` → monta `identidad/` e imprime en qué segundo va el sonido de marca de cada pieza.
3. En el `<head>` del `index.html`, una sola vez (nunca dentro del `<template>` de una escena: ahí no carga):

   ```html
   <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
   <link rel="stylesheet" href="identidad/fuentes/fuentes.css" />
   <link rel="stylesheet" href="identidad/kit.css" />
   ```

4. Montar las piezas del kit como subcomposiciones y poner el sonido de marca en el host, en **inicio de la pieza + su `sonido`** de
   `kit.json` (una subcomposición no puede mover su audio según una variable):

   ```html
   <!-- Tipo Wiki -->
   <div id="intro-wiki" data-composition-id="intro-wiki" data-composition-src="identidad/intro-wiki.html"
     data-variable-values='{"titulo":"Crear, editar o inactivar un evento","seccion":"eventos","idioma":"es"}'
     data-start="0" data-duration="3" data-track-index="1" data-width="1920" data-height="1080"></div>
   <audio id="marca-intro" src="identidad/audio/sonido-marca.wav" data-start="0.38" data-duration="2.1" data-track-index="11"></audio>
   …
   <div id="cierre-wiki" data-composition-id="cierre-wiki" data-composition-src="identidad/cierre-wiki.html"
     data-variable-values='{"siguiente":"Aprobar solicitudes de eventos y reportes","seccion":"eventos","idioma":"es"}'
     data-start="T" data-duration="4" data-track-index="1" data-width="1920" data-height="1080"></div>
   <!-- sonido en T + 1.88; sin «siguiente»: data-duration="2.5" y sonido en T + 0.38 -->

   <!-- Tipo Comercial (al final) -->
   <div id="cierre-comercial" data-composition-id="cierre-comercial" data-composition-src="identidad/cierre-comercial.html"
     data-variable-values='{"publico":"iglesia","llamado":"prueba","contacto":"sitio","fondo":"noche","idioma":"es"}'
     data-start="T" data-duration="5" data-track-index="1" data-width="1920" data-height="1080"></div>
   <!-- sonido en T + 0.38 -->

   <!-- Tipo Corto (al final, en un proyecto 1080×1920) -->
   <div id="cierre-corto" data-composition-id="cierre-corto" data-composition-src="identidad/cierre-corto.html"
     data-variable-values='{"llamado":"prueba","fondo":"azul","idioma":"es"}'
     data-start="T" data-duration="2.5" data-track-index="1" data-width="1080" data-height="1920"></div>
   <!-- sonido en T + 0.38 -->

   <!-- Clip del sitio y feed en 4:5 (al final, en un proyecto 1080×1350): las mismas variables del Corto -->
   <div id="cierre-clip" data-composition-id="cierre-clip" data-composition-src="identidad/cierre-clip.html"
     data-variable-values='{"llamado":"prueba","fondo":"azul","idioma":"es"}'
     data-start="T" data-duration="2.5" data-track-index="1" data-width="1080" data-height="1350"></div>
   <!-- sonido en T + 0.38 -->
   ```

5. Comercial y Corto: copiar `identidad/frame-comercial.md` o `identidad/frame-corto.md` como `frame.md` del proyecto **antes** de entrar al
   flujo de HyperFrames (`/product-launch-video` o `/general-video`), para que el flujo use la marca y no invente otra. Cada escena es una
   subcomposición en `compositions/` que usa las clases `.k-*` (ver `muestra-corto/compositions/gancho.html`).
6. Revisión: `npm run check` (0 errores) → `npx --yes hyperframes@0.8.62 snapshot --at …` en la mitad de cada escena y revisar la hoja de
   contacto → render. Comercial y Corto: el visto bueno del dueño sobre el storyboard y el preview.

Cada pieza del kit se monta **una vez** por proyecto (los ids internos no se repiten). Para otra variante, otro proyecto.

## La app en 4:5, 9:16 y 16:9: `.k-ventana` (v1.1)

La grabación real de la app va **recortada y ampliada** dentro de una ventana con radio, anillo sutil y sombra sobre la noche. No es un
teléfono ni un marco de aparato (las directivas lo prohíben). La cámara es un envoltorio que GSAP escala y mueve; la ventana y la grabación
no se transforman:

```html
<div class="k-ventana k-ventana-4x5" id="escena-ventana" style="left: 100px; top: 400px">
  <div class="k-ventana-camara" id="escena-camara" data-layout-allow-overflow>
    <img class="k-ventana-grabacion" src="assets/captura/….webp" alt="" />   <!-- o <video muted playsinline> -->
  </div>
</div>
```

| Clase | Tamaño | Dónde va | Para qué |
|---|---|---|---|
| `.k-ventana-4x5` | 880 × 840, radio 28 | left 100, top 400 (debajo de la ceja y la frase) | Clip del sitio y feed, 1080×1350 |
| `.k-ventana-9x16` | 960 × 850, radio 28 | left 60, top 480 (zona segura del Corto) | Corto y Reels, 1080×1920 |
| `.k-ventana-16x9` | 720 × 900, radio 28 | left 1104, top 90 (columna derecha) | La grabación del celular en un video 16:9 |
| `.k-ventana-escritorio` | 1440 × 760, radio 20 | left 240, top 260 (el titular arriba) | Un recorte de una grabación de escritorio en 16:9 |

- **El plano:** la grabación llena el ancho de la ventana. Con la del celular (390 px a 3×, 1170 px de ancho, o al menos 1080), el plano
  de 4:5 la muestra a 2,26× del celular real: el texto de 14 px de la app queda en 32 px.
- **La cámara:** acercamientos de **1,6 a 2** sobre el plano (1,5 si el encuadre no cabe), uno por compás (0,4–0,6 s, `power3.inOut`) y
  quieta después. Con origen 0 0, para poner el punto `(cx, cy)` de la grabación ajustada en el centro con el acercamiento `z`:
  `x = ancho/2 − z·cx`, `y = alto/2 − z·cy`; o la esquina de arriba a la izquierda en `(ex, ey)`: `x = −z·ex`, `y = −z·ey`. A 2, cada píxel
  de una grabación de 1170 px ocupa 1,5 px: todavía nítida; más allá se nota.
- `data-layout-allow-overflow` en la cámara: la grabación es más grande que la ventana a propósito (si no, `check` avisa).
- Toda cifra visible lleva `.k-datos-ejemplo`; en 4:5 y 9:16, con `.k-feed-datos` (28 px, el mínimo que se lee en un celular).

## Textos en 4:5: `.k-feed-*` (v1.1)

Dentro del 80 % seguro para títulos: `.k-feed-zona` (108 px a los lados, 135 px arriba y abajo). En un celular el cuadro se ve a unos
390 px de ancho (×0,36).

| Clase | Letra | En el celular |
|---|---|---|
| `.k-feed-ceja` | Inter 700, 34 px, mayúsculas, dorado | 12 px |
| `.k-feed-frase` | Fraunces 560, 80 px, interlínea 1,04, máx. 2 líneas (~40 caracteres); `<em>` en itálica dorada, 1–3 palabras | 29 px |
| `.k-feed-texto` | Inter 500, 42 px, máx. 2 líneas | 15 px |

Con la ceja y la frase de dos líneas, el texto ocupa de 135 a ~360 px y la ventana empieza en 400. Usan los colores de `.k-noche` o
`.k-claro`. Ver `muestra-clip/compositions/cuerpo.html`.

## Sonidos de acción (v1.1)

Propios, generados por código (`_identidad/sonidos-accion.mjs`, el motor del sonido de marca: notas de Mi mayor y ruido con semilla fija).
`montar-kit.mjs` los deja en `identidad/audio/<nombre>.wav` con su nivel de mezcla; la huella de cada uno está en `kit.json` →
`sonidosAccion`.

| Sonido | Dura | Acento | Pico montado | Bajo la música | Cuándo |
|---|---|---|---|---|---|
| `toque` | 75 ms | 0 | −7 dBFS | −10 dB | Un toque real en la app |
| `aparicion` | 220 ms | 0 | −13 dBFS | −8 dB | Una tarjeta, una píldora, un contador o la ventana que aparecen |
| `desliz` | 360 ms | 0,2 s | −13 dBFS | −8 dB | Un corte rápido, el látigo entre dos mundos, un movimiento grande de cámara |
| `subida` | 1,9 s | 1,5 s (el golpe) | −11 dBFS | −4 dB | Una vez por video, hacia el cambio más grande |
| `confirmacion` | 320 ms | 0,1 s | −14 dBFS | −7 dB | Algo que queda hecho («Guardado», «cumplido») |

- **Nivel:** con la música a −18 LUFS (la pista de la biblioteca con su `volumen`), los sonidos van con `data-volume="1"`. «Bajo la música»
  es la sonoridad momentánea (400 ms) del sonido solo menos la de la música en ese instante, medida con «Product Launch». Si la música va
  más baja o más alta, se mueven lo mismo.
- **Cuándo:** el acento cae un cuadro después de su imagen: `data-start = momento visible + 0,033 − acento`. Para la subida hacia la firma:
  `data-start = T − 1,467`.
- **Pocos y exactos:** cada uno con una causa en pantalla; `desliz` nunca en todos los cortes; `subida` una sola vez.

```html
<audio id="snd-toque" src="identidad/audio/toque.wav" data-start="1.533" data-duration="0.075" data-track-index="13" data-volume="1"></audio>
```

## Música

La biblioteca está en `_identidad/musica/` (los mp3 fuera de git) y en `kit.json` → `musica.biblioteca`: archivo, licencia, `volumen` para
−18 LUFS sin voz, pulsos y mapa. Cada proyecto copia la suya a `assets/musica/` (`npm run musica` en `muestra-clip`).

- **«Product Launch»** (`product-launch`, 120 BPM, `volumen` 0,7): todos los clips del sitio. Compases de 2 s desde el 2,05: entrada sin bajo
  hasta el 18; el bajo entra en el 18,05 (pico en el 20); respiro del 26 al 34; segunda subida desde el 34 con golpes en el 36, el 38 y el
  42,05 (el más fuerte); clímax del 50 al 66; salida del 66 al 82; final en el 84. Los pulsos, en `musica/product-launch-the-mountain.pulsos.json`.
  Los clips de módulo usan 14,05 → 42,05 y la firma arranca en el golpe del 42,05 (`data-media-start`, `data-fade-out="1"`).
- **«Education Piano»** (`education-piano`, `volumen` 0,83): en la biblioteca, sin uso por ahora.

## Probar el kit

```bash
cd muestra-kit && npm run captura && npm run kit && npm run check && npm run render   # renders/muestra-kit-16x9.mp4 (16 s)
cd ../muestra-corto && npm run kit && npm run check && npm run render  # renders/muestra-corto-9x16.mp4 (5 s)
cd ../muestra-clip && npm run captura && npm run musica && npm run kit && npm run check && npm run render  # renders/muestra-clip-4x5.mp4 (6,5 s)
```

## Tutoriales de la wiki

`_herramientas/tutorial-wiki.mjs` arma un tutorial narrado desde la grabación real de la app (`KingdomApp/tools/ayuda`,
`node capturar.mjs <seccion/articulo> --idioma es --modo video`) y su `guion.mjs`: monta el kit con `montar-kit.mjs`, toma de `kit.json` →
`piezas` las duraciones y los segundos del sonido de marca, genera la voz (Kokoro), las escenas, el `index.html`, el VTT y `SCRIPT.md`, y
`entregar` deja el MP4 a −16 LUFS, el póster y el VTT en `KingdomApp/tools/ayuda/salida/tutorial/<idioma>/<articulo>/`. Piloto:
`wiki-eventos-crear-y-editar/` (`npm run preparar:es`, `npm run check`, `npm run render:es`, `npm run entregar:es`; lo mismo con `en`).
Proceso y lista de revisión: `KingdomApp/docs/ayuda/videos.md`.
