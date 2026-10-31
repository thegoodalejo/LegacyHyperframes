# Generador del recorrido de Comunicaciones

`gen.py` arma `../index.html` desde `index.tpl.html` y escribe `../compositions/frase-1..8.html` y `../compositions/ceja.html`, a partir
de sus tablas:

- `TK`: los 19 tramos del clip (`assets/grabaciones/clip/grabacion.mp4`, tal cual el clip `clip-sitio-comunicaciones`);
- `TE1`, `TE2`: los tramos de `escritorio.mp4` (el chatbot con «Probar»; la automatización «Bienvenida a quien llega»);
- `TM`, `TC`: los tramos de `celular.mp4` (la ficha de Mariana; la campaña nueva para la red Timoteo);
- `ST_E1`, `ST_C`: los tres stills de `assets/stills/` (cuadros quietos de la grabación donde la app espera menos de lo que pide el pulso);
- `MARCAS`: las marcas de toque, en px del video (de `toques[]` de cada `pasos.json`);
- `SONIDOS`: los sonidos de acción (cuadro del sonido = cuadro de la imagen + 1);
- `FRASES`: las ocho frases, con sus cuadros de entrada y de salida.

```
python _gen/gen.py                                   # desde recorrido-comunicaciones/
npx --yes hyperframes@0.8.221 check --json
```

- Las cámaras (`enc()`, los encuadres `E` y `EE` en px CSS de la app), los látigos, los aterrizajes, las marcas y el final viven en el
  `<script>` de `index.tpl.html`. El detalle de cada encuadre y de cada corte está en `../REVIEW.md`.
- `fondo.html` no lo genera: se edita a mano.
- El `index.html` generado también se puede editar a mano (o en el editor de HyperFrames), pero el próximo `gen.py` lo reescribe: lo que se
  cambie a mano se pasa a las tablas o a la plantilla.

Ayudas (desde la raíz del proyecto):

- `sh _gen/musica.sh`: rehace `assets/musica/product-launch-recorrido.wav` desde `assets/musica/product-launch-the-mountain.mp3` (la edición de
  Academia, SPEC §0.1: una costura con cruce de 30 ms en el 31,99 del video). Sale idéntico, byte a byte, al de `recorrido-equipos`.
- `python _gen/mix.py [factor_musica]`: simula la mezcla de `index.html` con ffmpeg (las mismas fuentes, tiempos, niveles y carriles) y da
  la sonoridad integrada y el pico real antes de renderizar.
- Los stills se sacan de la grabación con
  `ffmpeg -i assets/grabaciones/escritorio.mp4 -vf "select=eq(n\,403)" -vframes 1 assets/stills/still-e403.png` (y 559 de `escritorio.mp4`,
  2060 de `celular.mp4`).
