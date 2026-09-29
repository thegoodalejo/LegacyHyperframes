# Videos de LegacyEnterprise

Videos de la app **LegacyEnterprise** hechos con HyperFrames. Las directivas (tres tipos: Wiki, Comercial y Corto; interfaz real; favicon como
marca; voz Kokoro fija) y el detalle viven en el repo de la app: `LegacyEnterprise/docs/videos/` y `LegacyEnterprise/docs/ayuda/videos.md`.

## Qué hay aquí

| Carpeta | Qué es |
|---|---|
| `_identidad/` | Kit de identidad v1: intro y cierre del Tipo Wiki (subcomposiciones con variables), `kit.json`, `frame-wiki.md`, favicon, logo, Inter, íconos y licencias. **No se edita por video** |
| `_herramientas/tutorial-wiki.mjs` | Genera un tutorial de la wiki desde su `guion.mjs` y la grabación real de la app |
| `wiki-<seccion>-<articulo>/` | Un tutorial de la wiki por artículo. Piloto: `wiki-empieza-entrar-por-primera-vez` |

En git va solo el código del video. Grabaciones, voces, renders, snapshots y lo generado quedan fuera (`.gitignore`); lo publicable va al bucket
de ayuda de LegacyEnterprise.

## Requisitos de esta máquina

- Node 22, FFmpeg y el CLI fijado `hyperframes@0.8.62` (por `npx`).
- Voz: `../../.venv-tts/` (Python 3.11 con `../../requirements-tts.txt`) y el modelo Kokoro en `%USERPROFILE%\.cache\hyperframes\tts\`
  (si falta: `node tools/ayuda/respaldar-voz.mjs --bajar` en LegacyEnterprise).
- LegacyEnterprise al lado (`F:\Proyectos\LegacyEnterprise`, o la variable `LEGACYENTERPRISE_REPO`), con la grabación del artículo hecha:
  `node capturar.mjs <seccion/articulo> --idioma todos --modo video` en `tools/ayuda/`.

## Hacer un tutorial de la wiki

1. Copiar la carpeta del piloto con el nombre `wiki-<seccion>-<articulo>` y reescribir `guion.mjs`, `BRIEF.md` y `STORYBOARD.md` (el contenido
   sale del artículo final; no inventar funciones ni números).
2. En la carpeta del proyecto, por cada idioma:

   ```bash
   npm run preparar:es          # voz, escenas, index.html, VTT, SCRIPT.md
   npm run check                # 0 errores
   npx --yes hyperframes@0.8.62 snapshot --at <mitad de cada escena, intro y cierre>   # revisar snapshots/contact-sheet*.jpg
   npm run render:es
   npm run entregar:es          # −16 LUFS + póster → LegacyEnterprise/tools/ayuda/salida/tutorial/es/<articulo>/
   ```

3. En LegacyEnterprise: `node tools/ayuda/publicar.mjs <seccion/articulo>` y `![texto alternativo](medio:tutorial "pie")` en el artículo.

Revisión antes de publicar: la lista de `LegacyEnterprise/docs/ayuda/videos.md` → *Lista de revisión de un tutorial*.
