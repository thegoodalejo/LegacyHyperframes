# Licencias del kit de identidad de Kingdom (v1.3)

| Recurso | Archivo | Origen | Licencia |
|---|---|---|---|
| Favicon de Kingdom (baldosa, corona y K) | `favicon.svg`; sus piezas dentro de `intro-wiki.html` y `cierre-*.html` | Propio: KingdomApp `frontend-v2/public/favicon.svg` (= `logo.svg` y `sitio/public/favicon.svg`, sha256 `2d3dcdff…`) | Propiedad de Legacy Software S.A.S. |
| Inter | `fuentes/inter-latin.woff2`, `fuentes/inter-latin-ext.woff2` | Google Fonts (`fonts.gstatic.com/s/inter/v20`), los mismos archivos que cargan la app v2 y el sitio | SIL Open Font License 1.1 |
| Fraunces | `fuentes/fraunces.woff2`, `fuentes/fraunces-italica.woff2` | Copia de KingdomApp `sitio/public/fuentes/` (Undercase Type, fuente variable, solo latin) | SIL Open Font License 1.1 |
| Íconos (los 12 de sección; desde la v1.2, 62 más para el Tipo Recurso, y desde la v1.3, 43 más para la app recreada de «Para líderes»: 117; lista en `frame-recurso.md`) | `iconos/*.svg` | Material Symbols Outlined (Google), 48 px, bajados de `fonts.gstatic.com/s/i/short-term/release/materialsymbolsoutlined/<nombre>/default/48px.svg` (la misma fuente que el kit de LegacyEnterprise) | Apache License 2.0 |
| Sonido de marca | `sonido-marca.mjs` (genera el WAV; el WAV no va a git) | Propio: síntesis en código, sin muestras de terceros | Propiedad de Legacy Software S.A.S. Exclusivo de Kingdom |
| Sonidos de acción (v1.1): `toque`, `aparicion`, `desliz`, `subida`, `confirmacion` | `sonidos-accion.mjs` (genera los WAV con el motor de `sonido-marca.mjs`; los WAV no van a git) | Propio: síntesis en código (tonos en Mi mayor y ruido de un generador con semilla fija), sin muestras de terceros | Propiedad de Legacy Software S.A.S. Exclusivo de Kingdom |
| Mapa de pulsos de «Product Launch» | `musica/product-launch-the-mountain.pulsos.json` | Propio: sacado con `hyperframes beats` de la pista (2026-10-30) | Dato derivado, propiedad de Legacy Software S.A.S.; la pista sigue con su licencia de Pixabay |
| Voz | Generada en local con Kokoro-82M (`kokoro-v1.0.onnx`, `voices-v1.0.bin`) | hexgrad/Kokoro-82M, el mismo modelo del kit de LegacyEnterprise | Apache License 2.0 |

## Música (biblioteca elegida por el dueño el 2026-10-30, decisión 217 de KingdomApp)

| Pista | Archivo | Origen | Licencia |
|---|---|---|---|
| «Education Piano», The_Mountain, 1:09 (publicada el 2023-06-27) | `musica/education-piano-the-mountain.mp3` (fuera de git) | https://pixabay.com/music/small-emotions-education-piano-155572/ | Pixabay Content License: gratis, sin atribución, se puede modificar; no se puede distribuir la pista sola. **Content ID Registered** |
| «Product Launch», The_Mountain, 1:26 (publicada el 2023-06-14) | `musica/product-launch-the-mountain.mp3` (fuera de git) | https://pixabay.com/music/modern-classical-product-launch-153648/ | Pixabay Content License (ídem). **Content ID Registered** |

«Content ID Registered»: un video en YouTube con estas pistas puede recibir un reclamo de monetización, que se disputa con la licencia de
Pixabay. Junto a cada archivo se guardan la fecha de descarga y el enlace de la pista. No se usan en la serie Estrategia (monetizada).
