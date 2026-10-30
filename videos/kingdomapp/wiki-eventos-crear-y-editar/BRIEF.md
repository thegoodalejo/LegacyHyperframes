---
tipo: wiki
workflow: general-video
flow: automation
storyboard: yes
message: "Crea una casa de paz en Eventos: categoría, nombre, horario, ubicación y responsables; y sabe cómo inactivarla."
destination: ayuda-kingdom
aspect: 1920x1080
language: es, en
audience: quien coordina Eventos en una iglesia (servidor con Eventos «Coordina») y el administrador
length: 60-120s
angle: how-to
narration: yes
---

## Intent

Tutorial de la ayuda (formación, no promoción) del artículo «Crear, editar o inactivar un evento» (`eventos/crear-y-editar`), el primero
de Kingdom con la herramienta nueva. Tono calmado, claro y cálido, tuteo. Español con la voz `em_alex` e inglés con `af_heart`
(`../_identidad/kit.json`). El inglés se hace solo cuando el español quedó completo y en verde.

## Assets

- `assets/captura/<idioma>/grabacion.mp4` + `pasos.json`: grabación REAL de la app (KingdomApp `tools/ayuda`, escena
  `eventos/crear-y-editar`, modo video, Kingdom Demo: coordina Eventos crea una casa de paz).
- Kit `../_identidad/` montado en `identidad/` por `montar-kit.mjs`.

## Customizations

- **Con grabación real:** las pantallas son la app. NO recrear ni ilustrar la interfaz.
- Llamadas de 2–5 palabras con los nombres exactos de la interfaz; subtítulos quemados + VTT.
- **Identidad:** intro con `titulo` «Crear, editar o inactivar un evento», `seccion` `eventos`; cierre con `siguiente`
  «Ver mis eventos y su ficha». No modificarlas (kit v1).
- La voz empieza después de la intro («En este video vas a…»).

## Notes

- Fuente del guion: el artículo de la ayuda. Nada que no esté en él ni en la grabación; nada de plataforma ni del ministerio.
- La escena graba crear el evento y abrir «Inactivar» (sin confirmar). Editar, la portada y reactivar se nombran y se remiten al artículo.
- Se genera con `../_herramientas/tutorial-wiki.mjs` (ver `../README.md`).
