# Generador del recorrido de Equipos

`gen.py` arma `../index.html` desde `index.tpl.html` y escribe `../compositions/frase-1..9.html` y `../compositions/ceja.html`, a partir de sus
tablas: los tramos de video de cada grabación (`M1A`…`M2B` del clip, `C3A`, `C3B` y `C4` de `celular.mp4`, `E1` de `escritorio.mp4`), las
marcas de toque (`MARCAS`, en px del video), los sonidos (`SONIDOS`, por el cuadro en que suenan) y las frases (`FRASES`, con sus cuadros de
entrada y de salida).

```
python _gen/gen.py        # desde recorrido-equipos/
```

- La parte 1 (0–839) es la del clip `clip-sitio-equipos` (sus tablas, copiadas tal cual); la parte 2 (840–2759), la nueva.
- Las cámaras, los iris, los látigos y los aterrizajes viven en el `<script>` de `index.tpl.html` (los encuadres `E` y `EE`, en px CSS de la app).
- `fondo.html` no lo genera: se edita a mano.
- El `index.html` generado también se puede editar a mano (o en el editor de HyperFrames), pero el próximo `gen.py` lo reescribe: lo que se
  cambie a mano se pasa a las tablas o a la plantilla.
- Los cuadros de cada grabación (`rec`) se midieron con sus cuadros extraídos (cambios por diferencia de cuadros y reglas en px CSS); el
  detalle está en `../REVIEW.md`.
