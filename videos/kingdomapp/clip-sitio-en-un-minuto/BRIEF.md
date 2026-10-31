---
tipo: comercial
subtipo: clip-del-sitio
storyboard: yes
flow: automation
message: "Kingdom es para toda la iglesia: toda tu iglesia, en una sola app."
destination: sitio público (kingdom-sitio, justo debajo del hero), en silencio y en bucle con botón de sonido; también YouTube y presentaciones
aspect: 16:9 (1920×1080); el 9:16 de la misma historia queda para después
language: es
audience: pastores y líderes que no conocen Kingdom
length: 54 s de cuerpo + el cierre del Comercial (5 s) = 59 s
---

# Clip del sitio: «Kingdom en un minuto»

La pieza insignia de la serie de clips del sitio (decisión 216 de KingdomApp, `docs/videos/README.md` → Tipo Comercial → Clip del sitio):
recorre los seis módulos con el mejor instante de cada clip ya aprobado y publicado. La historia está en [STORY.md](STORY.md), el contrato
cuadro por cuadro en [SPEC.md](SPEC.md) y la revisión en [REVIEW.md](REVIEW.md).

## Intent

- Sin voz. Texto quemado: una frase de apertura (la del hero), una ceja y una frase de 2 a 5 palabras por módulo, y una frase de síntesis.
- «Product Launch» con su forma: entrada → primera subida → respiro corto → segunda subida → clímax; cada corte y cada transición en un pulso
  medido, y los cambios de mundo en los golpes.
- Mucho movimiento entre módulos (látigos, iris, un empuje y un morph del celular al escritorio), con los sonidos de acción del kit.

## Assets

- Música: `assets/musica/product-launch-the-mountain.mp3` editada en `assets/musica/product-launch-minuto.wav` (`npm run musica`).
- La app real de Kingdom Demo: las grabaciones de los seis clips (`assets/grabaciones/<modulo>.mp4` y `<modulo>-pasos.json`, copiadas de
  `clip-sitio-<modulo>/`) y la de Tableros del recorrido de Membresía (`tableros.mp4`). Nada se grabó de nuevo.
- Kit v1.1: `identidad/` (`npm run kit`), `frame.md` (= `frame-comercial.md`), las tomas b y c de los sonidos en `assets/audio/`.

## Customizations

- Formato 16:9 con el celular en `.k-ventana-16x9` (columna derecha, el texto a la izquierda) y el escritorio en `.k-ventana-escritorio`.
- Cierre: `cierre-comercial` (público iglesia, llamado «prueba», contacto el sitio, fondo noche).

## Notes

- La interfaz es la real; solo datos ficticios, con «Datos de ejemplo» abajo a la izquierda de cada ventana.
- Se construye con el generador `_gen/` (ver `_gen/README.md`).
