---
tipo: wiki
workflow: general-video
flow: automation
storyboard: yes
message: "De WhatsApp a una cita: de punta a punta entre módulos."
destination: wiki-legacyenterprise
aspect: 1920x1080
language: es, en
audience: equipo y Administrador de sede que usan varios módulos juntos
length: 40-90s
angle: how-to
narration: yes
---

## Intent

Tutorial de la wiki (formación, no promoción) del flujo «De WhatsApp a una cita» / «From WhatsApp to an appointment» (`flujos/de-whatsapp-a-una-cita`, fase W4.3 de LegacyEnterprise). Tono
calmado y claro, tuteo. Español con la voz `em_alex` e inglés con `af_heart`.

## Assets

- `assets/captura/<idioma>/grabacion.mp4` + `pasos.json`: grabación REAL de la app (LegacyEnterprise `tools/ayuda`, escena `flujos/de-whatsapp-a-una-cita`, semilla
  de la wiki, Clínica Aurora).
- Kit `../_identidad/` montado en `identidad/`.

## Customizations

- **Con captura real:** las pantallas son la grabación. NO recrear ni ilustrar la interfaz. Intro y cierre del kit sin modificar.

## Notes

- Fuente del guion: el artículo del flujo en los dos idiomas. Se genera con `../_herramientas/tutorial-wiki.mjs`.
