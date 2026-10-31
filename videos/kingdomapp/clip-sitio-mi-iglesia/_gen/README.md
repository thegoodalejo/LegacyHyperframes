# Generador del index.html

`gen.py` arma `../index.html` desde `index.tpl.html` (el HTML con la cámara, el iris y las marcas en su `<script>`) y sus tablas de tramos de
video, stills, marcas de toque y sonidos:

```
python _gen/gen.py index.html _gen/index.tpl.html
```

El `index.html` generado también se puede editar a mano (o en el editor de HyperFrames); si se regenera, esos cambios se pierden salvo que
se lleven a `gen.py` o a la plantilla. Los demás `.py` son ayudas de revisión de la grabación (corren con Python 3, numpy y Pillow, desde una
carpeta de trabajo): `diff.py` (qué cambia en cada cuadro, sobre `frames.gray` = `ffmpeg -i grabacion.mp4 -vf scale=390:844,format=gray -f
rawvideo frames.gray`), `shift.py` (cuántos px CSS saltó la app entre dos cuadros), `hoja.py` y `regla.py` (hojas de cuadros con número y con
regla en px CSS; ojo: la regla marca 30 px de más), `mont.py` (hoja de snapshots con el número de cuadro del clip) y `rcheck.py` (cuadros sueltos del render con su número).
