# Generador del index.html

`gen.py` arma `../index.html` desde `index.tpl.html` y sus tablas de tramos (cuadro del clip → cuadro de la grabación), marcas de toque
(`pasos.json` → `toques[]`) y sonidos (cuadro del sonido, acento, nivel). Desde la carpeta del proyecto:

```
python _gen/gen.py index.html _gen/index.tpl.html
```

Sin argumentos usa esas mismas rutas. El `index.html` generado también se puede editar a mano (o en el editor de HyperFrames), pero una
regeneración lo pisa: lo que cambie a mano, llévalo a `gen.py` o a la plantilla.

Ayudas de revisión (Python con numpy y Pillow, y ffmpeg en el PATH):
- `diff.py <video>`: cuadro a cuadro de la grabación con el cambio medio y las filas CSS que cambian (para hallar toques, esperas y saltos).
- `sheet.py <salida.jpg> <cuadros,separados,por,coma>`: hoja de cuadros de la grabación (390×844 cada uno, con su número).
- `rsheet.py <salida.jpg> <cuadros>`: hoja de cuadros del render de entrega.
