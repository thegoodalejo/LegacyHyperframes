---
tipo: comercial
subtipo: clip-del-sitio
storyboard: yes
flow: automation
message: "Con Kingdom, ninguna persona que llega a tu iglesia se pierde."
destination: sitio público (kingdom-sitio, escenario de módulos) + Reels e historias
aspect: 4:5 (1080×1350) principal + 9:16 (1080×1920)
language: es (en y pt después, grabados con la interfaz en ese idioma)
audience: pastores y líderes que no conocen Kingdom
length: 28 s de cuerpo + la firma de marca
---

# Clip del sitio: Membresía

Primero de seis clips de módulo (Membresía, Eventos, Academia, Mi iglesia, Comunicaciones y Equipos) más «Kingdom en un minuto».
Decisión 216 de KingdomApp (`docs/videos/README.md` → Tipo Comercial → Clip del sitio).

## Intent

- Sin voz. Texto en pantalla corto, 3 o 4 frases de pocas palabras: el problema, Kingdom resolviéndolo y el resultado. En el sitio,
  el detalle de las funciones va al lado del video, en HTML; el video cuenta la historia.
- **Mucho movimiento, y el movimiento sigue a la música** (pedido del dueño, 2026-10-30): cada corte y cada transición en un pulso; los
  cambios grandes en los picos de intensidad.
- Lo que dice el sitio de Membresía (`KingdomApp/sitio/src/data/modulos.ts`): «Que ninguna persona se pierda en tu iglesia». Puntos:
  ruta de crecimiento (el sistema propone el siguiente paso), Mi seguimiento con semáforo (nadie nuevo se queda sin llamada), funciona sin
  señal.

## Assets

- Música: `assets/musica/product-launch-the-mountain.mp3` («Product Launch», The_Mountain, Pixabay, Content ID Registered; licencia en
  `../_identidad/licencias.md`). **Tramo 14,05 → 42,05 s de la pista** (14 compases de 2 s, 120 BPM): entrada sin bajo 14–18; el bajo
  entra en el 18,05 (primer cambio grande, pico en el 20); respiro 26–34; segunda subida 34–42 con golpes en 36, 38 y 42,05 (el más
  fuerte de la pista). Mapa completo: `KingdomApp/docs/videos/identidad.md` → Música.
- La app real de v2 con Kingdom Demo, grabada en local con `KingdomApp/tools/ayuda/capturar.mjs --modo video` (escenas de
  `tools/ayuda/escenas/membresia/`). Capturas ya publicadas de la ayuda: `KingdomApp/frontend-v2/src/ayuda/medios.json`.
- Kit: `identidad/` (montado con `npm run kit`), `frame.md` (= `frame-comercial.md`): noche, Fraunces y dorado del sitio; la firma «la
  corona se levanta» y el sonido de marca «campanas».

## Customizations

- Formatos: 4:5 para el sitio y el feed; 9:16 para Reels e historias, de la misma historia.
- El cierre: la firma de la corona con las campanas. El kit no tiene pieza en 4:5 (solo 16:9 y 9:16): hace falta una (kit v1.1, con el
  OK del dueño).

## Notes

- Reglas de las directivas: la interfaz es la real (nunca redibujada, nunca un teléfono dibujado); solo datos ficticios, con «Datos de
  ejemplo» si se ven cifras; nada inventado; aprueba el dueño el guion visual y la vista previa.
- Revisión en dos puntos, como acordó el dueño: el guion visual (tres historias en palabras → la elegida → SPEC) y la vista previa.
