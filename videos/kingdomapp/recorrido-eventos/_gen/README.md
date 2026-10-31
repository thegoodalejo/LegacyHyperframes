# Generador del recorrido de Eventos

`gen.py` arma `../index.html` desde `index.tpl.html` y escribe `../compositions/frase-4.html` … `frase-9.html`. Es la fuente de verdad de:

- `T1`: los tramos del celular (v01–v30 son el montaje del clip, tal cual; s00–s09 son `sin-senal.mp4`);
- `T2`: los tramos del computador (`tablero.mp4`; d01–d15 bajo la cámara del tablero y e01–e02 dentro del iris de la ficha);
- `TOQUES1` / `TOQUES2`: las marcas de toque, en px del video (de `toques[]` de cada `pasos.json`);
- `SND`: los sonidos de acción (cuadro del sonido = cuadro de la imagen + 1);
- `FRASES`: las frases 4 a 9 (palabra a palabra, cada una en su pulso).

```
python _gen/gen.py          # desde la raíz del proyecto
npx --yes hyperframes@0.8.221 check --json
```

Las cámaras (`enc()` y `comp()`), el látigo, los iris y los objetivos de encuadre viven en el `<script>` de `index.tpl.html`. Las frases 1 a 3, la ceja
y el fondo son archivos a mano en `compositions/`. El `index.html` generado también se puede editar a mano o en el editor de HyperFrames, pero
la próxima corrida de `gen.py` lo pisa.

Ayudas (desde la raíz): `mix.py` simula la mezcla con ffmpeg para elegir niveles antes de renderizar; `resumen_check.py` resume el último
`check`; `medir_render.py <mp4>` mide los cortes invisibles y la sonoridad del render; `rsheet.py <mp4> <salida.jpg> <cols> <ancho> <cuadros…>`
arma una hoja de cuadros del render.
