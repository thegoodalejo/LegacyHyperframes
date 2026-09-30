---
tipo: wiki
workflow: general-video
flow: automation
storyboard: yes
message: "Pon en marcha una sede nueva: la plantilla, tu equipo y sus accesos."
destination: wiki-legacyenterprise
aspect: 1920x1080
language: es, en
audience: Administrador de sede que abre una sede nueva
length: 90-150s
angle: how-to
narration: yes
---

## Intent

Tutorial de la wiki (formación, no promoción) de la guía «Poner en marcha la sede» / «Setting up the branch» (`implementacion/sede`, fase W4 de LegacyEnterprise).
Recorre, en el orden de la guía, las pantallas donde se configura y cómo se ven bien hechas. Tono calmado y claro, tuteo. Español con la voz
`em_alex` e inglés con `af_heart`.

## Assets

- `assets/captura/<idioma>/grabacion.mp4` + `pasos.json`: grabación REAL de la app (LegacyEnterprise `tools/ayuda`, escena
  `implementacion/sede`, semilla de la wiki): Ricardo Salazar, Administrador de la Sede Norte (recién abierta), con Andrés Ruiz esperando acceso.
- Kit `../_identidad/` montado en `identidad/`.

## Customizations

- **Con captura real:** las pantallas son la grabación. NO recrear ni ilustrar la interfaz.
- Llamadas de 1–4 palabras con los nombres exactos de la interfaz; subtítulos quemados + VTT.
- **Identidad:** intro y cierre del kit sin modificar (chip «Puesta en marcha», kit v1.1).

## Notes

- Fuente del guion: la guía de la wiki en los dos idiomas. Nada de plataforma: lo que hace el asesor de la app solo se nombra.
- Se genera con `../_herramientas/tutorial-wiki.mjs` (ver `../README.md`).
