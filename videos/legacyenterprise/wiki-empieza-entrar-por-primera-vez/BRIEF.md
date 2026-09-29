---
tipo: wiki
workflow: general-video
flow: automation
storyboard: yes
message: "Entra a la app por primera vez con tu código de sede, y como administrador invita y da acceso."
destination: wiki-legacyenterprise
aspect: 1920x1080
language: es, en
audience: persona nueva de un equipo que entra por primera vez, y el administrador de sede que la aprueba
length: 60-75s
angle: how-to
narration: yes
---

## Intent

Tutorial de la wiki (formación, no promoción) del artículo «Entrar por primera vez» (`empieza/entrar-por-primera-vez`), piloto de la fase WM.
Tono calmado y claro, tuteo. Español con la voz `em_alex` e inglés con `af_heart`.

## Assets

- `assets/captura/<idioma>/grabacion.mp4` + `pasos.json`: grabación REAL de la app (LegacyEnterprise `tools/ayuda`, escena
  `empieza/entrar-por-primera-vez`, semilla de la wiki: Clínica Aurora, Andrés Ruiz entra y Carolina Méndez lo aprueba).
- Kit `../_identidad/` montado en `identidad/`.

## Customizations

- **Con captura real:** las pantallas son la grabación. NO recrear ni ilustrar la interfaz.
- La ventana de Google no se graba: se muestra el botón «Continuar con Google» y la voz lo explica (decisión del dueño, 2026-09-29).
- Llamadas de 2–5 palabras con los nombres exactos de la interfaz; subtítulos quemados + VTT.
- **Identidad:** intro con `titulo` «Entrar por primera vez» / «Signing in for the first time», `modulo` base; cierre con `siguiente`
  «Roles y qué puede hacer cada uno» / «Roles and what each one can do». No modificarlas.

## Notes

- Fuente del guion: el artículo de la wiki en los dos idiomas. Nada de plataforma. En el cuerpo la voz dice «la app».
- Se genera con `../_herramientas/tutorial-wiki.mjs` (ver `../README.md`).
