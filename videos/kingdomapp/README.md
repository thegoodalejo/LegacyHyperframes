# Videos de Kingdom

Videos de **Kingdom** (la app para iglesias) hechos con HyperFrames. Las directivas (tres tipos: Wiki, Comercial y Corto; la app real; datos
ficticios; aprobaciones) y la identidad viven en el repo de la app: `KingdomApp/docs/videos/README.md` y `KingdomApp/docs/videos/identidad.md`.
Este directorio tiene el **kit de identidad** que todos los videos montan y las muestras que lo prueban.

## Qué hay aquí

| Carpeta | Qué es |
|---|---|
| `_identidad/` | Kit de identidad v1: intro y cierre del Tipo Wiki, cierres de marca del Comercial (16:9) y del Corto (9:16), `kit.json`, `kit.css`, `frame-wiki.md`, `frame-comercial.md`, `frame-corto.md`, favicon, Inter y Fraunces, íconos de sección, `sonido-marca.mjs` y licencias. **No se edita por video** |
| `_herramientas/montar-kit.mjs` | Copia el kit en `<proyecto>/identidad/`, comprueba el favicon contra la app y genera el sonido de marca a −20 LUFS |
| `muestra-kit/` | Muestra 16:9: intro Wiki → cuerpo con una captura real de la ayuda → cierre Wiki → cierre del Comercial |
| `muestra-corto/` | Muestra 9:16: una escena de Corto con los componentes de `kit.css` → cierre del Corto |
| `<tipo>-<tema>/` | Un proyecto por video: `wiki-eventos-crear-y-editar`, `comercial-iglesia-ordenada`, `corto-asistencia-sin-papel` |

Los videos anteriores (`../kingdomapp-promo`, `../kingdomapp-afirmar-nuevo`) son de antes del kit: recrean la app y usan otra marca. No se
toman como referencia visual.

En git va solo el código del video. Capturas, voces, música, renders, hojas de contacto y el `identidad/` montado quedan fuera (`.gitignore`).

## Requisitos de esta máquina

- Node 22, FFmpeg y el CLI fijado `hyperframes@0.8.62` (por `npx`), el mismo de los videos de LegacyEnterprise.
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
   ```

5. Comercial y Corto: copiar `identidad/frame-comercial.md` o `identidad/frame-corto.md` como `frame.md` del proyecto **antes** de entrar al
   flujo de HyperFrames (`/product-launch-video` o `/general-video`), para que el flujo use la marca y no invente otra. Cada escena es una
   subcomposición en `compositions/` que usa las clases `.k-*` (ver `muestra-corto/compositions/gancho.html`).
6. Revisión: `npm run check` (0 errores) → `npx --yes hyperframes@0.8.62 snapshot --at …` en la mitad de cada escena y revisar la hoja de
   contacto → render. Comercial y Corto: el visto bueno del dueño sobre el storyboard y el preview.

Cada pieza del kit se monta **una vez** por proyecto (los ids internos no se repiten). Para otra variante, otro proyecto.

## Probar el kit

```bash
cd muestra-kit && npm run captura && npm run kit && npm run check && npm run render   # renders/muestra-kit-16x9.mp4 (16 s)
cd ../muestra-corto && npm run kit && npm run check && npm run render  # renders/muestra-corto-9x16.mp4 (5 s)
```

## Tutoriales de la wiki

`_herramientas/tutorial-wiki.mjs` arma un tutorial narrado desde la grabación real de la app (`KingdomApp/tools/ayuda`,
`node capturar.mjs <seccion/articulo> --idioma es --modo video`) y su `guion.mjs`: monta el kit con `montar-kit.mjs`, toma de `kit.json` →
`piezas` las duraciones y los segundos del sonido de marca, genera la voz (Kokoro), las escenas, el `index.html`, el VTT y `SCRIPT.md`, y
`entregar` deja el MP4 a −16 LUFS, el póster y el VTT en `KingdomApp/tools/ayuda/salida/tutorial/<idioma>/<articulo>/`. Piloto:
`wiki-eventos-crear-y-editar/` (`npm run preparar:es`, `npm run check`, `npm run render:es`, `npm run entregar:es`; lo mismo con `en`).
Proceso y lista de revisión: `KingdomApp/docs/ayuda/videos.md`.
