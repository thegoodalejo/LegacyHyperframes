# Generador del recorrido de Mi iglesia

`gen.py` arma `../index.html` desde `index.tpl.html` y escribe `../compositions/frase-1..11.html` y `../compositions/ceja.html`, a partir de sus
tablas:

- `K_TRAMOS`, `K_STILLS` y `K_MARCAS`: la parte 1 (0–840), copiadas de `clip-sitio-mi-iglesia/_gen/gen.py`; el último tramo llega al 841 y
  hay una marca más, la de «Cerrar» en el 840;
- `C1A`, `C1B`, `C2` y `C3`: los tramos de `celular.mp4` (Gabriela en Comunidades, dentro del iris del 960, acompañada y en su objetivo, y la
  bienvenida de Lucía); `E1` y `E2`: los de `escritorio.mp4` (Contactos, el tablero y quién reaccionó);
- `MARCAS`: las marcas de toque de la parte 2, en px del video (de `toques[]` de cada `pasos.json`);
- `SONIDOS`: los sonidos de acción, por el cuadro en que suenan (imagen + 1);
- `FRASES`: las once frases, con sus cuadros de entrada y de salida.

```
python _gen/gen.py        # desde recorrido-mi-iglesia/ (o npm run gen)
sh _gen/musica.sh         # regenera assets/musica/product-launch-recorrido.wav desde el mp3 (o npm run musica)
npx --yes hyperframes@0.8.221 check --json
```

- Las cámaras (`enc()` y `comp()`, los encuadres `E` y `EE` en px CSS de la app), los iris, los látigos, los aterrizajes y las marcas viven en
  el `<script>` de `index.tpl.html`.
- `fondo.html` no lo genera: se edita a mano.
- El `index.html` generado también se puede editar a mano (o en el editor de HyperFrames), pero el próximo `gen.py` lo reescribe: lo que se
  cambie a mano se pasa a las tablas o a la plantilla.
- Los cuadros de cada grabación (`rec`) se midieron con sus cuadros extraídos (cambios por diferencia de cuadros y reglas en px CSS); el
  detalle está en `../REVIEW.md`. Los stills `assets/stills/still-c486.png` y `still-c2277.png` son los cuadros 486 y 2277 de `celular.mp4`
  (`ffmpeg -i assets/grabaciones/celular.mp4 -vf "select=eq(n\,486)" -frames:v 1 assets/stills/still-c486.png`).
