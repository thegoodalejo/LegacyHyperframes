# Generador de «Kingdom en un minuto»

`gen.py` arma `../index.html` desde `index.tpl.html` y escribe `../compositions/texto-0..7.html` (la apertura, la ceja y la frase de cada
módulo y la síntesis), a partir de sus tablas:

- `MOD`: los seis módulos. Cada uno es una **ventana** del clip de su módulo (`ini`–`fin`, en cuadros del clip) corrida `off` cuadros
  (siempre un número entero de compases: 60 cuadros). De cada clip se copian, tal cual, los tramos de video (`tramos`, con su
  `data-media-start` y su tasa), las cámaras (`cam`: encuadre inicial y movimientos), las marcas de toque (`marcas`, en px del video, de
  `toques[]` de cada `pasos.json`) y los sonidos (`sonidos`). La fuente de cada tabla es el `_gen/gen.py` y el `index.tpl.html` del
  **recorrido** del mismo módulo (su parte 1 es el clip en 16:9: mismas ventanas, mismos encuadres). `recorte()` corta cada tramo a la
  ventana y corrige su `data-media-start` (media + cuadros recortados / 30 × tasa).
- `SINTESIS_TRAMO`: el tablero del pastor (`tableros.mp4` del recorrido de Membresía, «Resumen» quieto).
- `SONIDOS_FIJOS`: los `desliz` de cada cambio de mundo. `sonidos_html()` ordena todos los sonidos y rota las tres tomas de `toque`,
  `aparicion` y `desliz` (a, b, c), nunca la misma dos veces seguidas.
- `TEXTOS`: los ocho textos, con sus cuadros de entrada y de salida.

```
python _gen/gen.py                                   # desde clip-sitio-en-un-minuto/ (o npm run gen)
sh _gen/musica.sh                                    # rehace assets/musica/product-launch-minuto.wav (o npm run musica)
npx --yes hyperframes@0.8.221 check --json
```

- Las transiciones entre módulos (la subida del 110–120, los látigos, el iris, el empuje, el morph), los encuadres (`E1`…`E7`, con los
  números de cada recorrido) y las marcas viven en el `<script>` de `index.tpl.html`.
- `../compositions/fondo.html` no lo genera: se edita a mano.
- El `index.html` generado se puede editar a mano (o en el editor de HyperFrames), pero el próximo `gen.py` lo reescribe: lo que se cambie a
  mano se pasa a las tablas o a la plantilla.
- `mezcla.py` simula la mezcla de `index.html` con ffmpeg (las mismas fuentes, tiempos y niveles) y da la sonoridad integrada y el pico
  real antes de renderizar: `python _gen/mezcla.py`.
