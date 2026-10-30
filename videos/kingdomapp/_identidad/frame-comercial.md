---
version: v1
name: Kingdom — Frame del Tipo Comercial (16:9)
description: >
  Sistema visual de los videos comerciales de Kingdom (la app para iglesias), a escala de cuadro. Es la identidad del sitio público
  (kingdom-sitio.web.app) llevada a video: noche azul profunda con el halo azul y dorado y la retícula de puntos, la palabra «Kingdom» y los
  titulares en Fraunces con el énfasis en itálica dorada, todo lo demás en Inter, y la app REAL (grabada con Kingdom Demo) dentro de una
  pantalla con sombra. La firma es «la corona se levanta» (las 7 barras de la corona del favicon suben una tras otra). Se copia como
  frame.md del proyecto; el kit montado (identidad/kit.css) trae los componentes.
unit: el cuadro — 1920×1080 principal; 1080×1080 y 1080×1350 para redes (ver «Formatos»)
principle: la marca es sagrada (colores, letras, favicon, sonido) · la composición es libre · la app es la real · ningún dato inventado

colors:
  noche: "#060D1F"
  noche-2: "#0C1A3A"
  tinta: "#EAF0FF"
  tinta-2: "#A9B6D6"
  dorado: "#E8B95A"
  dorado-marca: "#D9A234"
  azul-marca: "#3576DA"
  azul-fuerte: "#1F56B8"
  verde-marca: "#00897B"
  linea: "rgba(234, 240, 255, 0.12)"
  halo-azul: "rgba(53, 118, 218, 0.45)"
  halo-dorado: "rgba(217, 162, 52, 0.22)"
  puntos: "rgba(169, 190, 235, 0.35)"
  claro: "#F7F8FC"
  claro-tinta: "#0E1A33"
  claro-tinta-2: "#46526D"
  claro-dorado: "#7D5800"

typography:
  marca:    { fontFamily: "Fraunces", px: 92, weight: 600, tracking: "-0.02em", color: "tinta" }
  titular:  { fontFamily: "Fraunces", px: 88, weight: 560, lineHeight: 1.04, tracking: "-0.02em", color: "tinta", class: ".k-titular" }
  enfasis:  { fontFamily: "Fraunces", italic: true, weight: 500, color: "dorado", use: "<em> dentro del titular, 1–3 palabras" }
  ceja:     { fontFamily: "Inter", px: 28, weight: 700, tracking: "0.1em", upper: true, color: "dorado", class: ".k-ceja" }
  texto:    { fontFamily: "Inter", px: 36, weight: 500, lineHeight: 1.35, color: "tinta-2", class: ".k-texto" }
  boton:    { fontFamily: "Inter", px: 38, weight: 700, color: "noche", background: "dorado", class: ".k-boton" }
  subtitulo:{ fontFamily: "Inter", px: 40, weight: 500, lineHeight: 1.3, color: "#FFFFFF", plate: "rgba(27,27,31,0.8)", class: ".k-subtitulo" }
  etiqueta: { fontFamily: "Inter", px: 22, weight: 600, color: "#FFFFFF", plate: "rgba(6,13,31,0.72)", class: ".k-datos-ejemplo" }

radii:
  pill: "999px"
  pantalla: "20px"
  tarjeta: "28px"

components:
  fondo:        ".k-noche (o .k-claro) con .k-halo y .k-puntos dentro, a sangre"
  pantalla-app: ".k-pantalla-noche: la grabación real 16:9, radio 20, anillo de 1 px y sombra grande; sin aparato dibujado"
  datos-ejemplo: ".k-datos-ejemplo: «Datos de ejemplo» en la esquina de toda pantalla que muestre cifras"
  boton:        ".k-boton: solo los llamados aprobados"
  cierre:       "identidad/cierre-comercial.html (5,0 s) con sus variables; nunca un cierre hecho a mano"
---

# Kingdom — Frame del Tipo Comercial

## Adaptación de marca (LEER PRIMERO)

El frontmatter es normativo: los hex, las letras y los pesos se usan tal cual. La prosa explica la intención. La fuente de verdad es
KingdomApp `docs/videos/identidad.md`; este archivo es su versión para un proyecto de HyperFrames. **No se edita por video**: si un video
necesita algo distinto, se resuelve en su composición, no tocando la marca.

## Overview

Un Comercial le muestra a un pastor, a un líder o al director de un ministerio cómo Kingdom resuelve **su** caso y lo lleva a probarlo. El
tono es cercano y seguro, pastoral sin ser solemne: habla de personas cuidadas y de iglesias ordenadas, no de funciones técnicas. La noche
del sitio da el aire de «presentación» y deja que la app, clara y luminosa, sea la protagonista.

## The Frame

- Fondo a sangre `noche` con el halo (azul arriba a la derecha, dorado abajo a la izquierda) y la retícula de puntos que se desvanece hacia la
  izquierda. El halo puede respirar lento (escala 1,08 → 1 en la escena); los puntos no se mueven.
- Márgenes de 96 px a los lados y 72 px arriba y abajo; el texto nunca toca el borde.
- Una idea por escena: titular + la app real, o titular + una frase. Nunca tres bloques de texto.
- Variante **claro** (`.k-claro`, `fondo: "claro"` en el cierre) cuando el video va en un sitio claro o en una presentación; mismas reglas.

## Colors

- `dorado` es escaso: el énfasis del titular, la ceja y el botón. Nunca un fondo grande dorado.
- `azul-marca` vive en el favicon; en texto sobre la noche se usa `tinta`.
- En claro, el dorado de texto es `claro-dorado` (`#7D5800`), porque `#D9A234` no pasa contraste sobre fondo claro.

## Typography

- **Fraunces** solo para la palabra «Kingdom» y los titulares; **Inter** para todo lo demás (cejas, textos, botones, subtítulos).
- Titulares en frase normal (no MAYÚSCULAS), con `text-wrap: balance`, máximo 2 líneas. El énfasis va en itálica dorada sobre 1–3
  palabras, como «Kingdom es para *toda la iglesia*».
- Ceja en MAYÚSCULAS con 0,1em de espaciado, 2–4 palabras.

## Motion

- **La firma:** «la corona se levanta» (baldosa → K que sube → 7 barras de la corona una tras otra con un leve rebote, `back.out(2.2)`, cada
  0,05 s). Solo la hacen las composiciones del kit (cierre, y la apertura si el dueño la aprueba). No se imita en otras escenas.
- Entradas: subir 16–28 px con opacidad, `power3.out` 0,35–0,5 s; botones con escala 0,92 → 1 y `back.out(1.8)`.
- Cortes directos entre escenas, o un barrido corto. Nada de giros, rebotes grandes, destellos ni partículas.
- Acercamientos a la app real para que se lea lo que importa (`/hyperframes-keyframes`), con cuadros de origen en la grabación.

## Composition Rules

1. **Estructura:** problema de la iglesia (sin exagerar) → la app real resolviéndolo → resultado para la iglesia → llamado a la acción →
   `cierre-comercial.html`.
2. **La app es la real:** grabación o captura de la app corriendo con Kingdom Demo. Alrededor se permiten titulares, flechas y marcas; nunca
   una pantalla redibujada ni un teléfono dibujado.
3. Una pantalla de la app ocupa al menos el 55 % del ancho cuando es la protagonista.
4. Subtítulos quemados siempre (`.k-subtitulo`) y VTT aparte.
5. El video **abre** con el problema; abrir con la marca (1 s de la corona) solo si el dueño lo aprueba en el storyboard.

## Formatos

| Formato | Uso | Ajuste |
|---|---|---|
| 1920×1080 | Pieza principal (sitio, YouTube, presentaciones) | Este frame |
| 1080×1080 y 1080×1350 | Redes | Mismos átomos; titular 76–84 px; la app en `.k-telefono` o recortada. El cierre de estos formatos se hace con el primero que se pida (sube la versión del kit) |

## Approved Entities

- Nombre: **Kingdom** (nunca «Kingdom App» en pantalla ni en la voz). Empresa: Legacy Software S.A.S. (solo en créditos legales).
- Frases publicadas que se pueden usar tal cual: «Kingdom es para toda la iglesia», «La app para iglesias», «Prueba gratis 30 días»,
  «Cuida la visión en cada iglesia de tu red» (Kingdom Ministry), «Solo pagas por las personas que realmente participan», «Usuarios
  ilimitados · 30 días gratis».
- Módulos con su nombre en la app: Membresía, Eventos, Academia, Mi iglesia, Portal, Comunicaciones, Equipos, Archivos y Compartir.
- Llamados del cierre: `prueba` o `asesoria`. Contactos: sitio, WhatsApp de ventas o Instagram (`cierre-comercial.html`).

## Numerals & Claims (regla dura)

- Ninguna cifra de resultados, testimonio, logo de iglesia ni precio que el dueño no haya aprobado. Nada de la hoja de ruta.
- Toda cifra que se vea en la app lleva `.k-datos-ejemplo` («Datos de ejemplo»).
- Solo personas e iglesias ficticias (Kingdom Demo). Nunca una iglesia real, un nombre real ni un número de WhatsApp real.

## Pre-Render Self-Audit

- [ ] `npx hyperframes@0.8.62 check` en 0 errores (contraste AA incluido).
- [ ] Hoja de contacto revisada: ninguna pantalla redibujada, todas las cifras con «Datos de ejemplo».
- [ ] El cierre es `cierre-comercial.html` con variables, y el sonido de marca está en su segundo (`kit.json`).
- [ ] Voz a −16 LUFS, música 18–24 dB por debajo, salida a −16 LUFS.
- [ ] El dueño aprobó el storyboard y el preview.

## Known Gaps

- La biblioteca de música está pendiente (`kit.json` → `musica`).
- El sitio aún no tiene dominio propio: el contacto `sitio` dice `kingdom-sitio.web.app` hasta entonces.
