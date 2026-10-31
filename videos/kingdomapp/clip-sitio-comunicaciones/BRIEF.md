---
tipo: comercial
subtipo: clip-del-sitio
storyboard: yes
flow: automation
message: "Con Kingdom, quien escribe por WhatsApp recibe respuesta y la iglesia ve quién respondió a su invitación."
destination: sitio público (kingdom-sitio, escenario de módulos) + Reels e historias
aspect: 4:5 (1080×1350) principal + 9:16 (1080×1920)
language: es (en y pt después, grabados con la interfaz en ese idioma)
audience: pastores y líderes que no conocen Kingdom
length: 28 s de cuerpo + la firma de marca (≈ 30,5 s)
---

# Clip del sitio: Comunicaciones — «Alguien nuevo escribe»

Quinto de seis clips de módulo (Membresía, Eventos, Academia, Mi iglesia, Comunicaciones y Equipos). Decisión 216 de KingdomApp
(`docs/videos/README.md` → Tipo Comercial → Clip del sitio). La historia, el reloj y los planos cuadro por cuadro están en
[STORY.md](STORY.md) y [SPEC.md](SPEC.md); este BRIEF solo resume.

## Intent

- Sin voz. Texto en pantalla corto, 4 frases: el problema, Kingdom resolviéndolo y el resultado. El detalle va en HTML al lado.
- El movimiento sigue a la música: cada corte y cada transición en un pulso; los cambios grandes en los picos.
- Lo que dice el sitio de Comunicaciones (`KingdomApp/sitio/src/data/modulos.ts`).

## Assets

- Música: `assets/musica/product-launch-the-mountain.mp3` (tramo 14,05 → 42,05 s de la pista; licencia en `../_identidad/licencias.md`).
- La app real de v2 con Kingdom Demo, grabada en local con `KingdomApp/tools/ayuda/capturar.mjs --modo video` (escena
  `tools/ayuda/escenas/clips/comunicaciones-alguien-nuevo.mjs`, cuenta 101, con Meta simulado): `assets/grabaciones/grabacion.mp4` + `pasos.json` + `hoja-grabacion.jpg`.
- Kit: `identidad/` (montado con `npm run kit`) y `frame.md` (= `frame-comercial.md`).

## Customizations

- Formatos: 4:5 para el sitio y el feed; 9:16 para Reels e historias, de la misma historia.
- Cierre: `cierre-clip` con la firma de la corona y las campanas.

## Notes

- La interfaz es la real (nunca redibujada, nunca un teléfono dibujado); solo datos ficticios, con «Datos de ejemplo» si se ven cifras.
- Revisión en dos puntos: el guion visual (ya elegido en STORY) y la vista previa.
