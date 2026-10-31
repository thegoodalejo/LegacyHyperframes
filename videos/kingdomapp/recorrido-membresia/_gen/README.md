# Generador del recorrido de Membresía (16:9)

`gen.py` arma `../index.html` desde `index.tpl.html` y escribe `../compositions/` (el fondo, las nueve frases y las cinco cejas). Las tablas de
`gen.py` son la fuente de verdad de los tramos de video (`CLIP`: los 29 del clip, sin cambios; `NUEVOS`: los de coordinar, semaforo,
discipulado y tableros), las marcas de toque, los sonidos y los textos. Los encuadres, los iris, los látigos y el morph están en el `<script>`
de la plantilla.

```bash
python _gen/gen.py              # desde la raíz del proyecto
npx --yes hyperframes@0.8.221 check --json
```

El `index.html` generado se puede editar a mano o en el editor de HyperFrames, pero el siguiente `gen.py` lo pisa: los cambios van aquí.

Ayudas de revisión (trabajan sobre cuadros extraídos con `ffmpeg -i <grabación> -vf scale=<ancho CSS>:<alto CSS> fr/<nombre>/f%04d.png`):

| Script | Para qué |
|---|---|
| `diff.py <nombre>` | Lista los cuadros de una grabación en los que cambia algo (y dónde): las pausas, los toques y las cargas |
| `shift.py <nombre> a b y0 y1 x0 x1 rango` | Mide un desplazamiento vertical entre dos cuadros (el 387 de discipulado: 7 px; el 506 de tableros: 453 px) |
| `sheet.py <nombre> salida.jpg cols caja escala cuadros…` | Hoja de cuadros de una grabación (recortada) |
| `snap.py <carpeta de snapshot> prefijo [cols] [ancho] [por hoja]` | Hoja de los PNG de `hyperframes snapshot`, con el cuadro de cada uno |
