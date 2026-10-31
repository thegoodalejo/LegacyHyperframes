---
tipo: wiki
workflow: general-video
flow: automation
storyboard: yes
message: "Pon en marcha una iglesia celular con «Tu arranque»: responde el cuestionario, haz tus primeros pasos y mira cómo se marcan solos."
destination: ayuda-kingdom
aspect: 1920x1080
language: es, en
audience: el administrador de una iglesia que empieza con Kingdom
length: 120-200s
angle: how-to
narration: yes
---

## Intent

Tutorial de la ayuda (formación, no promoción) de la guía de puesta en marcha «Pon en marcha Kingdom en tu iglesia»
(`puesta/pon-en-marcha-kingdom`), con el recorrido de una iglesia celular: abrir «Tu arranque» desde Servir, responder el cuestionario eligiendo
«Celular», recorrer «Tu iglesia», «Tu gente» y «Tu equipo» y hacer dos pasos de verdad (la marca y una red con su líder) para ver cómo la ruta los
marca sola. Tono calmado, claro y cálido, tuteo. Voces del kit (`../_identidad/kit.json`): `ef_dora` en español y `af_heart` en inglés.

## Assets

- `assets/captura/<idioma>/grabacion.mp4` + `pasos.json`: grabación REAL de la app (KingdomApp `tools/ayuda`, escena
  `puesta/pon-en-marcha-kingdom`, modo video, de escritorio, Kingdom Demo: el administrador, cuenta 101).
- Kit `../_identidad/` montado en `identidad/` por `montar-kit.mjs`.

## Customizations

- **Con grabación real:** las pantallas son la app. NO recrear ni ilustrar la interfaz.
- Llamadas de 2–5 palabras con los nombres exactos de la interfaz; subtítulos quemados + VTT.
- **Identidad:** intro con `titulo` «Pon en marcha una iglesia celular», `seccion` `puesta`; cierre con `siguiente`
  «Responder el cuestionario y recorrer tu ruta de arranque». No modificarlas (kit v1).
- La voz empieza después de la intro («En este video vas a…»).

## Notes

- Fuente del guion: los artículos `puesta/pon-en-marcha-kingdom` y `puesta/ruta-de-arranque`. Nada que no esté en ellos ni en la grabación; nada
  de plataforma ni del ministerio.
- El vocabulario por modelo lo tiene que confirmar el dueño: la voz no lista las palabras. Con «Celular» la app no propone palabras distintas a
  las que la iglesia ya usa, así que el paso «Revisa las palabras» se cierra con «Están bien así» (no aparece la pantalla de «Usar este vocabulario»).
- La demo ya tiene redes, personas y equipo: la escena (`sql`) la deja sin redes propias y con la ubicación puesta para que «Tu iglesia» se complete
  con la marca y «Tu gente» tenga una red por crear. Los pasos de «Tu equipo» que aparecen con «Hecho» son de la demo; la voz solo dice qué pide cada uno.
- Se genera con `../_herramientas/tutorial-wiki.mjs` (ver `../README.md`).
