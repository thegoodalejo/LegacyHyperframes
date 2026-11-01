# REVIEW — Eventos de ciudad, sin perder a nadie

- `check` (hyperframes@0.8.221): 0 errores, 0 avisos; contraste AA en los 43 textos.
- Tres rondas de snapshots en la mitad de cada escena (hojas de contacto). Corregido:
  - Campañas: la pista de estaciones dejaba ver la estación anterior en el borde → la ventana va de 192 a 1728 px; los públicos y las
    automatizaciones aparecen tenues al llegar la cámara y se encienden en su palabra (antes, 3 s de estación vacía).
  - Reportes: rótulos de columnas de 26 px y encimados → 30 px y columnas de 140 px.
  - Línea: el rótulo «Chatbot» se escalaba a 18 px → se apaga en vez de escalarse.
  - Testimonios: las tres etapas aparecen tenues al empezar la frase (el lado derecho quedaba vacío).
  - Ingreso: «¡Bienvenido!» tapado por la línea del escáner → a la derecha; fila más densa (22) y una cola que espera.
  - Textos cinéticos: la puntuación tras un `<em>` quedaba como palabra suelta («campaña ,», «nadie ?») → se pega a la palabra anterior.
  - Avisos `line_unread` (nota de Membresía, botones de la plantilla, «Con pocas personas») → más tiempo en pantalla.
- **Íconos vacíos en el primer render** (en los snapshots sí salían): `.k-recurso-icono` de `identidad/kit.css` declara
  `mask: var(--k-icono)` y en el render la `url(identidad/iconos/…)` se resuelve contra la hoja (`identidad/identidad/…`). Cada escena
  vuelve a declarar la máscara en su propio `<style>`, como `capitulo-recurso`. Segundo render revisado: íconos bien. Es un fallo del kit
  v1.2 que afecta a todo recurso que use `.k-recurso-icono`.
- Nada de la app, ni teléfonos ni pantallas redibujadas; toda cifra con «Datos de ejemplo»; sin precios ni estado de la demo.
