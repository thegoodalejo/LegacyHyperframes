---
version: v1
name: Kingdom — Frame del Tipo Corto (9:16)
description: >
  Sistema visual de los videos cortos de Kingdom para Reels, TikTok, Shorts e historias (6–30 s). Los mismos átomos del Comercial (noche del
  sitio, Fraunces para el titular con el énfasis dorado, Inter para lo demás, la app REAL), compuestos para detener el scroll: gancho en el
  primer segundo y medio, una sola idea, subtítulos grandes quemados y todo dentro de la zona segura. Cierra con cierre-corto.html (2,5 s):
  la baldosa azul llena la pantalla y la corona se levanta. Se copia como frame.md del proyecto.
unit: el cuadro — 1080×1920 principal; 1080×1080 y 1080×1350 si la campaña lo pide
principle: gancho primero · una sola idea · la app es la real · ningún dato inventado · nada fuera de la zona segura

colors:
  noche: "#060D1F"
  tinta: "#EAF0FF"
  tinta-2: "#A9B6D6"
  dorado: "#E8B95A"
  azul-marca: "#3576DA"
  azul-fuerte: "#1F56B8"
  placa: "rgba(6, 13, 31, 0.78)"
  halo-azul: "rgba(53, 118, 218, 0.45)"
  halo-dorado: "rgba(217, 162, 52, 0.22)"
  puntos: "rgba(169, 190, 235, 0.35)"

typography:
  gancho:    { fontFamily: "Fraunces", px: 104, weight: 560, lineHeight: 1.04, tracking: "-0.02em", color: "tinta", class: ".k-vertical .k-titular", maxLines: 3 }
  enfasis:   { fontFamily: "Fraunces", italic: true, weight: 500, color: "dorado" }
  ceja:      { fontFamily: "Inter", px: 34, weight: 700, tracking: "0.1em", upper: true, color: "dorado", class: ".k-vertical .k-ceja" }
  texto:     { fontFamily: "Inter", px: 46, weight: 500, lineHeight: 1.35, color: "tinta-2", class: ".k-vertical .k-texto" }
  subtitulo: { fontFamily: "Inter", px: 60, weight: 800, lineHeight: 1.18, color: "#FFFFFF", plate: "placa", class: ".k-subtitulo-corto", maxLines: 2 }
  palabra-activa: { color: "dorado", class: ".k-activa" }
  boton:     { fontFamily: "Inter", px: 50, weight: 700, class: ".k-vertical .k-boton" }

spacing:
  zona-segura: { top: 250, bottom: 420, left: 60, right: 60, class: ".k-segura" }
  subtitulos: { bottom: 440 }

radii:
  pill: "999px"
  telefono: "56px"

components:
  fondo:         ".k-noche.k-vertical con .k-halo y .k-puntos"
  telefono:      ".k-telefono: la grabación real del celular de referencia (360 px de ancho) a 720 px, radio 56; sin aparato dibujado"
  datos-ejemplo: ".k-datos-ejemplo cuando se ven cifras"
  cierre:        "identidad/cierre-corto.html (2,5 s): fondo azul (por defecto) o noche, y un llamado aprobado"
---

# Kingdom — Frame del Tipo Corto

## Adaptación de marca (LEER PRIMERO)

Los átomos son los de `frame-comercial.md` (y la fuente de verdad, KingdomApp `docs/videos/identidad.md`). Aquí cambian la unidad (vertical),
los tamaños y la estructura. **No se edita por video.**

## Overview

El Corto vive en el feed: casi todos lo ven sin sonido y deciden en un segundo y medio si se quedan. Por eso abre con el gancho (una pregunta,
un dolor reconocible de la iglesia o el resultado ya en pantalla), muestra **una sola** cosa de la app real y cierra con un llamado corto. Tono
directo y cálido, nunca alarmista.

## The Frame

- **Zona segura:** todo el texto y la app entre 250 px arriba y 420 px abajo, 60 px a los lados (`.k-segura`). Ahí no tapan la interfaz de
  Reels, TikTok ni Shorts.
- Arriba el gancho (ceja + titular), al centro la app en `.k-telefono` o un acercamiento a la pantalla, abajo los subtítulos.
- Fondo `noche` con halo y puntos, igual que el sitio. La app clara resalta sobre él.

## Typography

- Gancho en Fraunces 104 px, máximo 3 líneas, énfasis dorado en 1–3 palabras.
- **Subtítulos siempre quemados**: Inter 800 de 60 px sobre la placa, máximo 2 líneas, 3–6 palabras por golpe. La palabra que se dice va en
  dorado (`.k-activa`) si el corto tiene voz.

## Motion

- Ritmo rápido: un corte cada 1,5–3 s. Textos que entran en 0,25–0,4 s (`power3.out`).
- Acercamientos a la app real para que se lea (`/hyperframes-keyframes`).
- La firma de la corona solo en el cierre; **el Corto nunca abre con la marca**.

## Composition Rules

1. **Gancho en 1,5 s** → **una sola idea** con la app real → **llamado a la acción corto** → `cierre-corto.html` (2,5 s).
2. Duración total 6–30 s (lo normal, 15 s), contando el cierre.
3. **Variantes:** el mismo cuerpo con 2–3 ganchos. Cada variante es su propio archivo: `renders/corto-<tema>-gancho-a-9x16.mp4`.
4. Sin voz es válido (los subtítulos cuentan la historia); con voz, Kokoro con la voz del kit.

## Approved Entities

Las mismas de `frame-comercial.md`. En el cierre: `llamado` = `prueba` («Prueba gratis 30 días») o `asesoria` («Agenda una asesoría por
WhatsApp»); `fondo` = `azul` (por defecto: contraste máximo en el feed) o `noche`.

## Numerals & Claims (regla dura)

- Nada engañoso: cumplir las políticas de publicidad de cada plataforma.
- Toda cifra en pantalla con «Datos de ejemplo»; solo datos ficticios de Kingdom Demo.
- Ninguna promesa de resultados («duplica tu asistencia») ni precios no aprobados.

## Pre-Render Self-Audit

- [ ] `check` en 0 errores y ningún texto fuera de la zona segura (revisar la hoja de contacto).
- [ ] El gancho se entiende sin sonido en el primer segundo y medio.
- [ ] Subtítulos de 2 líneas como máximo, siempre legibles sobre la app.
- [ ] Cierre `cierre-corto.html` con su sonido de marca a +0,38 s.
- [ ] Música a −18 LUFS sin voz (o 18–24 dB bajo la voz); salida a −16 LUFS.
- [ ] El dueño aprobó cada variante antes de pautar.

## Known Gaps

- Música: la biblioteca de `kit.json` → `musica` (v1.1), con los sonidos de acción por debajo. En 4:5 hay cierre (`cierre-clip.html`, v1.1), `.k-ventana-4x5` y `.k-feed-*`; el cierre en 1:1 se hace con la primera campaña que lo pida.
