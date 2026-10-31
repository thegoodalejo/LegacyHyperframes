# Clip del sitio: Mi iglesia — la historia elegida: «Se enteró toda la iglesia»

2026-10-30 · Tercer clip de la serie, después de [Membresía, «Valeria llegó el domingo»](../clip-sitio-membresia/STORY.md) y
[Eventos, «Terminó la reunión»](../clip-sitio-eventos/STORY.md). **El dueño ya no revisa guiones:** la historia se eligió aquí y se especifica
completa en [SPEC.md](SPEC.md). Son palabras; nada se construye desde este archivo. El proyecto de HyperFrames lo inicializa otro agente.

**Lo que no se reabre (el sistema de la serie, §3 del STORY de Membresía):** 4:5 (1080×1350) y después 9:16 de la misma historia · sin voz,
3–4 frases cortas (problema → Kingdom lo resuelve → resultado) · «Product Launch» 14,05 → 42,05 s, el mismo reloj de 14 compases (bajo en
4,0, pico en 6,0, respiro 12–20, segunda subida desde 20,0, golpes en 22,0 y 24,0, la firma en 28,0) · mucho movimiento y siempre en los
pulsos · la app real de Kingdom Demo en celular, dentro de `.k-ventana`, nunca un teléfono dibujado · datos ficticios con «Datos de ejemplo»
· la ceja «MI IGLESIA» en 6,5 · la frase final es el `titulo` de `modulos.ts` («Tu iglesia, en el bolsillo de cada miembro») con una palabra
en itálica dorada · `cierre-clip` con el llamado `prueba` en 28,0.

> **Sobre la duración.** La ampliación de Membresía (2026-10-30) llevó ese clip a 18 compases y propuso el mismo reloj para la serie. Para
> Mi iglesia se mantiene lo decidido en el pedido de este clip: **30,5 s** (28 de cuerpo + 2,5 de firma), igual que Eventos. La función que
> define el módulo (la boleta en el bolsillo) cae dentro de los 28 s; si después se decide pasar la serie a 18 compases, el tramo que se
> agregaría está anotado en SPEC §5.

## El reloj (igual que en Membresía y Eventos)

120 BPM: un pulso cada 0,5 s (15 cuadros a 30 fps), un compás cada 2 s. t = 0 del clip ↔ 14,05 de la pista. La grilla real cuadro por
cuadro está en SPEC §0.

| Compás | Clip | La pista | Qué le toca al video |
|---|---|---|---|
| 1–2 | 0 – 4 | entrada sin bajo | El gancho: Mi iglesia ya abierto; la app baja sola a la novedad. Cuadro 0 nunca negro ni la marca |
| 3 | **4,0** | **entra el bajo** | El primer toque grande: «Amén» a la novedad. Frase 2 |
| 4 | **6,0** | pico | «Inscribirme» en la tarjeta de la novedad → el evento; la ceja «MI IGLESIA» |
| 4–6 | 6 – 12 | energía sostenida | Un movimiento de cámara por compás sobre el evento; la app baja a «Inscripción» |
| 7–10 | 12 – 20 | respiro | La inscripción con su familia, a velocidad normal. Frase 3 |
| 11–12 | 20 – 24 | segunda subida (20,0), el compás más fuerte del cuerpo (22–24) | 20,0 «¡Quedaste inscrito!»; 22,0 la boleta con su QR |
| 13–14 | 24 – 28 | golpe en 24,0 y el más fuerte en 28,0 | La boleta a pantalla completa; frase 4 quieta ≥ 3,6 s |
| — | 28,0 – 30,5 | se desvanece bajo las campanas | La firma |

---

## La historia: «Se enteró toda la iglesia» ★ elegida

**Idea en una frase:** la iglesia anunció el congreso; Gabriela, una miembro, lo ve en Mi iglesia en su celular, le da «Amén», toca
«Inscribirme», se inscribe con su esposo, responde la talla de la camiseta de los dos y en un toque tiene su boleta con QR, que se abre a
pantalla completa para mostrarla en la entrada.

**Recurso:** un dato real que viaja: el anuncio. Empieza como una novedad del feed («Inscripciones abiertas»), se vuelve un evento, después
una inscripción de dos personas y termina como una boleta con QR en la mano de la persona. **Forma:** cadena objeto a objeto en un solo
aparato (el celular de la miembro): la tarjeta del evento dentro de la novedad abre el evento; «Inscribirme» abre «¿A quiénes inscribes?»;
«Seguir» abre el formulario de cada uno; «Inscribir» trae el sello y el confeti; «Ver boleta» trae la boleta; tocar el QR la pone en grande.
Un mundo, un iris (de la novedad al evento), un corte sobre el toque (del resultado a la boleta) y el dip a la firma; sin látigo.

**Por qué es la mejor para un pastor que no conoce Kingdom:** todo pastor conoce el anuncio del domingo que nadie oyó: se dice desde el
púlpito, se repite en el grupo de WhatsApp, y el día del congreso todavía hay quien pregunta cuándo era y una fila en la mesa de inscripción.
El clip responde la pregunta del gancho («¿Se enteró toda la iglesia?») con la misma pantalla: el anuncio está en el celular de la persona,
ella responde, se inscribe con su familia y la boleta queda en su bolsillo, también sin señal. Las tres promesas del sitio salen solas:
novedades con reacciones y la tarjeta de un evento (punto 1), el evento con boleta (punto 1) y «tu iglesia, con tu logo» (la barra de la app
y el saludo con su nombre). Es la historia que un desconocido repite: «lo anunciaron y ella ya tenía la boleta en el celular». Y es distinta
de los dos clips anteriores donde debe serlo: Membresía es de quien recibe a la persona nueva; Eventos, del líder que reporta; Mi iglesia es
**del miembro**, el único clip donde la app es de la persona y no del equipo.

### Frases en pantalla

| Segundo | Frase | Cómo entra | Se va |
|---|---|---|---|
| 0,0 | **¿Se enteró toda la iglesia?** | una landing por pulso: «¿Se» 0,0 · «enteró» 0,5 · «toda la» 1,0 · «iglesia?» 1,5 (blur 6 px → 0, sin desplazarse) | 4,0, con el toque |
| 4,0 | **Llega a cada celular.** | la línea entera, blur 8 → 0 en 0,2 s, con el toque en «Amén» | 6,0, con el toque en «Inscribirme» |
| 12,0 | **Y se inscribe con su familia** | palabra a palabra, 0,067 s entre palabras; el toque en «Inscribirme» cae en 12,5 | 20,0, blur-out 0,2 s |
| 24,0 | **Tu iglesia, en el *bolsillo* de cada miembro** (*bolsillo* en itálica dorada) | palabra a palabra; el único dorado del cuerpo junto a la ceja | se queda hasta 28,0 |

Más la ceja «MI IGLESIA» (Inter, mayúsculas, dorado) que cae en 6,5 sobre la ventana y se va en 24,0.

La frase 1 es la pregunta del pastor, no la del miembro: el clip la contesta con imágenes. La frase 2 es lo que hace Kingdom (la novedad va
a toda la iglesia y su aviso llega al celular: [portal](../../../../KingdomApp/docs/modulos/portal.md) → «Novedades», «avisar»). La frase 3
es textual de la ayuda («puedes inscribir también a tu familia registrada en la iglesia»,
`frontend-v2/src/ayuda/es/mi-iglesia/inscribirme-a-un-evento.md`). La frase 4 es el `titulo` de `modulos.ts`. Ninguna frase depende de un
número, de un nombre ni de una fecha de la semilla.

### Recorrido sobre la música

| Compás | Clip | Pantalla real (celular, cuenta 105 = la miembro, «Gabriela» en la demo) y acción | Movimiento |
|---|---|---|---|
| 1 | 0–2 | **Cuadro 0:** Mi iglesia arriba: la barra «Kingdom Demo» con su logo, **«Buenos días, Gabriela» (real)**, «Iglesia Kingdom Demo 1», «Mis servicios», «Mis Equipos» y la destacada «¡Bienvenidos a nuestra iglesia en la app!» asomando | La frase 1 cae en los cuatro pulsos; la cámara quieta (G arriba) |
| 2 | 2–4 | **2,0:** la app baja sola, rápido, por el calendario y los próximos eventos hasta las novedades y se detiene en la primera: **«Iglesia Kingdom Demo 1 · hace 3 minutos» · «Inscripciones abiertas» · «Separa la fecha y asegura tu cupo: los cupos son limitados.»** con la tarjeta del **«Congreso de Jóvenes»** y su botón **«Inscribirme»**. 3,0: la cámara a la tarjeta y a las reacciones. **3,5: toque en la flecha de las reacciones**: se abren «Me gusta · Me edifica · Me sorprende · Amén», escalonadas con su resorte | El desplazamiento de la app es el movimiento de 2,0; la cámara, el de 3,0 |
| 3 | **4,0**–6 | **4,0: toque en «Amén» 🙌**: el selector se cierra, el botón queda «🙌 Amén» en su color y el total sube en uno. 5,0: la cámara se centra en la tarjeta del evento; 5,5 aparece la marca sobre «Inscribirme» | Cae la frase 2. Primer cambio grande: la persona le responde a su iglesia |
| 4 | **6,0**–8 | **6,0: toque en «Inscribirme»** → iris desde el dedo → **el evento en Mi iglesia**: «← Mi iglesia», la portada, «Encuentro», **«Congreso de Jóvenes»** y sus fechas | Pico: el evento llena la ventana. Cae la ceja «MI IGLESIA» en 6,5. «Datos de ejemplo» desde el cuadro 0 |
| 5 | 8–10 | 8,0: la cámara a los datos: **«Del martes, 24 de noviembre al miércoles, 25 de noviembre · 8:00 a. m.» (real)**, «Día 1 · Día 2» y «Dos días para encontrarnos, adorar y crecer juntos. Trae tu Biblia y tu boleta.» | Un movimiento de cámara por compás |
| 6 | 10–12 | 10,0: la app baja a **«Inscripción»**: «Llega 30 minutos antes con tu boleta en el celular (también funciona sin señal).» y el botón **«Inscribirme»**; 11,0 la cámara a esa tarjeta | Ídem |
| 7 | 12–14 | **Respiro.** 12,0 cae la frase 3; **12,5: toque en «Inscribirme»** → entra **«¿A quiénes inscribes? (hasta 4)»** con «Yo» marcado y su esposo **(real)** sin marcar; 13,0 la cámara a la lista | De aquí a 20 la app va a velocidad normal |
| 8 | 14–16 | **14,0: toque en el esposo** (queda marcado); **15,0: «Seguir»** → **«1 de 2: Tú»**: «Talla de camiseta» S · M · L · XL y «¿Es tu primera vez en el congreso?» Sí · No; 15,5 la cámara abre al formulario entero | Movimiento pequeño: una casilla, un botón |
| 9 | 16–18 | **16,0 «M» · 16,5 «Sí» · 17,0 «Seguir»** → **«2 de 2: {su esposo}»** | Los radios que se llenan son el movimiento del respiro |
| 10 | 18–20 | **18,0 «L» · 18,5 «No»**; 19,0 la cámara a los botones «Atrás · **Inscribir**»; 19,5 la marca | |
| 11 | **20,0**–22 | **20,0, segunda subida: toque en «Inscribir»** → el **sello** con la boleta entra con su resorte, **confeti** de la app, **«¡Quedaste inscrito!»** · «Tu boleta ya está en Mis boletas: también se ve sin señal.» · las dos personas «Inscrito» · **«Ver boleta»** · «Listo» | Frase 3 sale. La celebración es de la app, no del montaje |
| 12 | **22,0**–24 | **22,0, el compás más fuerte: toque en «Ver boleta»** → **«Mis boletas»**: «Congreso de Jóvenes», sus días, el lugar (ya se ve: quedó inscrita), «Tu boleta», **el QR** y **«Código ······»**. 23,0: acercamiento al QR | La prueba más fuerte del clip: el anuncio ya es una boleta |
| 13 | **24,0**–26 | **24,0, golpe: toque en el QR** → **la boleta a pantalla completa, sobre blanco**: el QR grande, su nombre y el código; la ventana baja a 0,92 y se corre al borde | Cae la frase 4; la ceja se va |
| 14 | 26–28 | Todo quieto salvo la app (la boleta real); la subida desde 26,5; 27,9 dip | La frase final sostenida |
| — | **28,0**–30,5 | **La firma sobre el golpe más fuerte:** `cierre-clip` (fondo azul, la corona se levanta, campanas en 28,38, llamado `prueba`) | La corona es el único gesto de marca |

### El lenguaje del movimiento, en una línea por nivel

- **Cada pulso (0,5 s) entre 0 y 6:** o aterriza una palabra, o un toque real, o la app muestra algo nuevo (el desplazamiento, el selector
  de reacciones, el «Amén»). Entre 6 y 12 la cámara recorre el evento una vez por compás y la app baja una vez.
- **Cada compás (2 s):** un movimiento de cámara dentro de la ventana (14 cuadros, `power2.inOut`, blur de render), luego quieta. Nunca la
  cámara y el desplazamiento de la app a la vez.
- **4,0:** «Amén»: la persona le responde a su iglesia con el bajo. **6,0:** el iris al evento (el único iris). **20,0 y 22,0:** «Inscribir» y
  «Ver boleta»: las dos pruebas, una por golpe. **24,0:** la boleta en grande y la frase final. **28,0:** la corona.
- **12–20:** cero cortes; solo la app a velocidad normal (una casilla, dos formularios de dos radios, tres botones).
- Transiciones con causa (dos clases y el cierre): iris desde el toque (al evento, 6,0), corte sobre el toque (de «Ver boleta» a la boleta,
  22,0), dip + corte (a la firma). Sin látigo: un solo mundo.

### Grabaciones que necesita (Kingdom Demo, `capturar.mjs --modo video`)

Una sola escena de **celular**, `tools/ayuda/escenas/clips/mi-iglesia-boleta.mjs` (`movil: true`, `toque: false`), con la cuenta **105**
(la miembro de las capturas; en la demo, «Gabriela», una adulta casada sin cargo: `_demo_capturas.php`, líneas 22 y 113–114) y tramos:
`inicio` · `bajar` · `reaccion` · `evento` · `inscripcion` · `familia` · `formulario` · `inscrito` · `boleta` · `grande`. Está completa, lista
para copiar, en SPEC §3.

Lo que la semilla garantiza (verificado): la novedad «Inscripciones abiertas» con la tarjeta de un evento
(`_demo_portal_3_publicaciones.php`, línea 84); el «Congreso de Jóvenes» a 30 días, de dos días, con el formulario «Talla de camiseta»
(S/M/L/XL, obligatoria) y «¿Es tu primera vez en el congreso?» (Sí/No), hasta 4 por cuenta, la familia permitida, el mensaje «Llega 30
minutos antes con tu boleta en el celular (también funciona sin señal).», categoría Encuentro visible en Mi iglesia y con boletería
(`_demo_eventos_inscripcion.php`, líneas 39–77); el diseño de su boleta y la miembro inscrita (`tools/ayuda/semillas/comunicaciones.php`,
líneas 158–168); «Amén» 🙌 en el catálogo de reacciones (`backend/_datos/portal.php`, línea 34); la miembro con familia que puede inscribir
(la captura `mi-iglesia/inscribirme-a-un-evento/01-evento` muestra «Inscribir a alguien más»). Comunidades (Jóvenes, con un líder que la
acompaña) y un objetivo en curso al día también existen para ella (`_demo_portal_6_recorrido.php`), pero no entran en este clip (§ alternativas).

Lo que la semilla **no** deja como lo necesita la historia, y la escena arregla con su `sql` antes de grabar (SPEC §3): la tarjeta de la
novedad apunta al primer evento con portada, no al congreso (se repunta al congreso y la novedad pasa a ser la más reciente, «hace 3
minutos»); la miembro y su esposo ya pueden estar inscritos (se borran sus inscripciones del congreso); el congreso quedó con el cupo lleno y
con aprobación (se abre sin cupo y sin aprobación, para que el resultado sea «¡Quedaste inscrito!» y no «lista de espera»); y la miembro
puede haber reaccionado ya a esa novedad (se borra su reacción).

### De 4:5 a 9:16

Misma línea de tiempo, misma grabación, mismas cajas de `pasos.json`; cambia el encuadre como en Membresía y Eventos: titular 80 → 104 px,
ventana 880×1050 que sangra → 960×850 completa entre 480 y 1330, cámara G 2,256 → 2,462 ppc, firma `cierre-clip` → `cierre-corto`. La frase
4 va en tres líneas en 9:16 y sube al lugar de la ceja (SPEC §1.4).

---

## Alternativas que se descartaron (una línea cada una)

- **«Recibió a Jesús el domingo»** (el QR de bienvenida → la entrada → la bienvenida guiada con «Cómo orar» → «Sí, quiero» → la celebración):
  la más emotiva y el primer bloque del sitio, pero repite la persona nueva de Membresía en la misma página de inicio y la entrada con Google
  no se puede grabar con la herramienta; va al recorrido de 60–75 s, que empieza ya dentro de la bienvenida.
- **«Un capítulo por día»** (Mis objetivos: el paso de hoy, «Lo hice», el anillo que avanza, «¿Seguimos?»): tierna y real, pero es un solo
  toque, su gancho natural (el recordatorio en el celular) es una notificación del sistema que no está en la grabación y no se dibuja, y
  «objetivo en curso» no lo entiende un pastor que no conoce Kingdom en 4 s.
- **«Quiero conocer a los jóvenes»** (Comunidades: Explorar → Unirme → «Conectar con un líder» → «Un líder te escribirá pronto»): habla de
  conexión, pero el desenlace (el líder que la toma) ocurre en otro celular y otro día, y repite el «alguien la acompaña» de Membresía.
- **«Todo en el bolsillo»** (un montaje: el feed, una comunidad, un objetivo y la boleta, 6 s cada uno): lista funciones, que es la forma
  prohibida de la serie; es el trabajo de «Kingdom en un minuto».
- **«Amén»** (las reacciones como protagonistas: conteos que suben en varias novedades): demasiado delgada para 28 s; queda como el gesto del
  4,0 dentro de la elegida.

## Riesgos y dudas (el detalle en SPEC §5)

- **Su esposo:** la historia necesita que la miembro tenga cónyuge activo en la iglesia. La `ref` `conyuge` lo exige o la escena se niega;
  el plan B inscribe solo a la miembro y la frase 3 pasa a «Y se inscribe sin hacer fila».
- **El `sql` de la escena** toca cuatro cosas de la demo local (la tarjeta de la novedad, dos inscripciones, el cupo y una reacción): se
  prueba primero con `--modo capturas` y las `refs` fallan si alguna no quedó.
- **El cargador de la app** (la K a los 150 ms) al abrir el evento, al inscribir y al abrir «Mis boletas»: con la API local no debería
  asomar; si asoma, se corta en la espera.
- **El confeti** depende del modo ligero y de `prefers-reduced-motion` de la app; si no sale en la grabación, no se agrega en el montaje.
- **El saludo** («Buenos días/Buenas tardes») depende de la hora de la grabación; el nombre, las fechas y el código cambian con la semilla.
  Ninguna frase depende de ellos.
