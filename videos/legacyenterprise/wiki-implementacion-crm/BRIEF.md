---
tipo: wiki
workflow: general-video
flow: automation
storyboard: yes
message: "El embudo, el catálogo, el historial de ventas y las metas, en ese orden."
destination: wiki-legacyenterprise
aspect: 1920x1080
language: es, en
audience: Administrador de sede que configura el CRM
length: 90-150s
angle: how-to
narration: yes
---

## Intent

Tutorial de la wiki (formación, no promoción) de la guía «Poner en marcha el CRM» / «Setting up the CRM» (`implementacion/crm`, fase W4 de LegacyEnterprise).
Recorre, en el orden de la guía, las pantallas donde se configura y cómo se ven bien hechas. Tono calmado y claro, tuteo. Español con la voz
`em_alex` e inglés con `af_heart`.

## Assets

- `assets/captura/<idioma>/grabacion.mp4` + `pasos.json`: grabación REAL de la app (LegacyEnterprise `tools/ayuda`, escena
  `implementacion/crm`, semilla de la wiki): Carolina Méndez en los Ajustes del CRM, Ventas, Metas y el tablero de la Clínica Aurora.
- Kit `../_identidad/` montado en `identidad/`.

## Customizations

- **Con captura real:** las pantallas son la grabación. NO recrear ni ilustrar la interfaz.
- Llamadas de 1–4 palabras con los nombres exactos de la interfaz; subtítulos quemados + VTT.
- **Identidad:** intro y cierre del kit sin modificar (el kit v1 no tiene un chip «Puesta en marcha»: la sede y la libreta usan «base»).

## Notes

- Fuente del guion: la guía de la wiki en los dos idiomas. Nada de plataforma: lo que hace el asesor de la app solo se nombra.
- Se genera con `../_herramientas/tutorial-wiki.mjs` (ver `../README.md`).
