# Generador del recorrido de Academia

`gen.py` arma `../index.html` desde `index.tpl.html` y escribe `../compositions/frase-4.html` … `frase-9.html`. Es la fuente de verdad de:

- `T`: los tramos de video (v01–v22 son el montaje del clip, tal cual, sobre `grabacion.mp4`; c01–c19, s01–s05 y f01 son `celular.mp4`;
  e01–e15 y t01–t03 son `escritorio.mp4`), cada uno con su contenedor (la cámara o el iris donde vive);
- `TOQUES`: las marcas de toque, en px del video (de `toques[]` de cada `pasos.json`);
- `SND`: los sonidos de acción (cuadro del sonido = cuadro de la imagen + 1);
- `FRASES`: las frases 4 a 9 (palabra a palabra, cada una en su cuadro).

```
python _gen/gen.py          # desde la raíz del proyecto
npx --yes hyperframes@0.8.221 check --json
```

Las cámaras (`enc()` y `comp()`), los látigos (vertical en el celular, horizontal entre escenarios), los iris, los aterrizajes y los
encuadres viven en el `<script>` de `index.tpl.html`. Las frases 1 a 3, la ceja y el fondo son archivos a mano en `compositions/`. El
`index.html` generado también se puede editar a mano o en el editor de HyperFrames, pero la próxima corrida de `gen.py` lo pisa.

Ayudas (desde la raíz): `mix.py` simula la mezcla con ffmpeg para elegir niveles antes de renderizar; `resumen_check.py` resume el último
`check`; `medir_render.py <mp4>` mide los cortes invisibles, la sonoridad y la costura de la música en el render; `rsheet.py <mp4> <salida.jpg>
<cols> <ancho> <cuadros…>` arma una hoja de cuadros del render.
