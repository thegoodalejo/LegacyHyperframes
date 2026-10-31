# Clip del sitio: Comunicaciones — la historia elegida: «Alguien nuevo escribe»

2026-10-30 · Tercer clip de la serie (después de [Membresía, «Valeria llegó el domingo»](../clip-sitio-membresia/STORY.md) y de
[Eventos, «Terminó la reunión»](../clip-sitio-eventos/STORY.md)). **El dueño ya no revisa guiones:** la historia se eligió aquí y se
especifica completa en [SPEC.md](SPEC.md). Son palabras; nada se construye desde este archivo. El proyecto de HyperFrames lo inicializa
otro agente.

**Lo que no se reabre (el sistema de la serie, §3 del STORY de Membresía):**
- 4:5 (1080×1350) y después 9:16 de la misma historia.
- Sin voz, con 3 o 4 frases de 2 a 6 palabras (problema → Kingdom lo resuelve → resultado).
- «Product Launch» del 14,05 al 42,05 s, con el mismo reloj: bajo en 4,0, pico en 6,0, respiro de 12 a 20, segunda subida desde 20,0,
  golpes en 22,0 y 24,0 y la firma en 28,0.
- Mucho movimiento, siempre en los pulsos.
- La app real de Kingdom Demo en celular, dentro de `.k-ventana`; nunca un teléfono dibujado.
- Datos ficticios con «Datos de ejemplo».
- La ceja «COMUNICACIONES» en 6,5.
- La frase final es el `titulo` de `modulos.ts`, recortado para que quepa en dos líneas (como en Membresía), con una palabra en itálica
  dorada.
- `cierre-clip` con el llamado `prueba` en 28,0.

**Lo que este clip cambia del §3:** ese párrafo suponía que el respiro de Comunicaciones viviría en el escritorio. No hace falta. La bandeja
es adaptable: con menos de 840 px se ve la lista **o** el hilo, y el panel va encima. El reporte de una campaña también se apila en una
columna. El clip entero es de **celular**, en la misma `.k-ventana` de los dos anteriores. No se usa `.k-ventana-escritorio`.

## El reloj (igual que en Membresía y Eventos)

120 BPM: un pulso cada 0,5 s (15 cuadros a 30 fps) y un compás cada 2 s. El t = 0 del clip es el 14,05 de la pista. La grilla real, cuadro
por cuadro, está en SPEC §0.

| Compás | Clip | La pista | Qué le toca al video |
|---|---|---|---|
| 1–2 | 0 – 4 | entrada sin bajo | El gancho: la cola de la bandeja con mensajes sin responder. Cuadro 0 nunca negro ni la marca |
| 3 | **4,0** | **entra el bajo** | El primer toque grande: «Tomar». Frase 2 |
| 4 | **6,0** | pico | La pantalla clave: las respuestas rápidas que suben al escribir «/». La ceja «COMUNICACIONES» |
| 4–6 | 6 – 12 | energía sostenida | «/horarios» llena la respuesta y se envía. Un movimiento de cámara por compás |
| 7–10 | 12 – 20 | respiro | Frase 3. A velocidad normal: volver, «Campañas», bajar hasta la invitación del domingo |
| 11–12 | 20 – 24 | segunda subida (20,0); el compás más fuerte del cuerpo (22–24) | 20,0: el reporte con sus números. 22,0: «respondieron» y los nombres |
| 13–14 | 24 – 28 | golpe en 24,0; el más fuerte en 28,0 | Frase 4 quieta; la app viva detrás |
| — | 28,0 – 30,5 | se desvanece bajo las campanas | La firma |

---

## La historia: «Alguien nuevo escribe» ★ elegida

**Idea en una frase:** una mujer que nunca ha ido a la iglesia escribe al WhatsApp de la iglesia:
> «Hola, buenas noches. ¿A qué hora es el culto del domingo? Es mi primera vez y quiero ir con mi esposo.»

Alguien del equipo toma la conversación en Kingdom y le responde con un toque («/horarios»). Después abre la invitación al culto del domingo
que la iglesia mandó por WhatsApp a toda una red y ve, con nombre, quién la leyó y quién contestó «Allí estaré».

**Recurso:**
- **Un momento del día de alguien:** quien atiende el WhatsApp de la iglesia abre la bandeja.
- **Un dato real que viaja:** el domingo. Mariana pregunta por el culto del domingo y la respuesta dice «Nos reunimos los domingos…».
  La invitación al culto del domingo llegó a 139 personas y 115 la leyeron.

**Forma:** un solo aparato, en una cadena objeto a objeto:
- la fila de Mariana abre su conversación;
- «Tomar» la vuelve del equipo;
- «/» levanta las respuestas rápidas;
- «/horarios» llena la respuesta;
- enviar la pone en el hilo;
- volver deja la cola en 3;
- «Campañas» abre la lista;
- la invitación abre su reporte;
- «respondieron» trae los nombres.

Es un solo mundo: el celular del que atiende. Hay un match cut en el primer toque y un dip hacia la firma. Sin iris ni látigo: aquí no se
abre ninguna hoja ni cambia la persona.

**Por qué es la mejor para un pastor que no conoce Kingdom:**
- **El gancho es el miedo de todo pastor.** La primera vez que alguien escribe a la iglesia, el mensaje cae en un celular que nadie mira
  el sábado en la noche. «Es mi primera vez y quiero ir con mi esposo» es la persona que una iglesia no puede perder, y el clip la nombra
  con su propio mensaje, leído a 44 px.
- **Las dos mitades del `titulo` del sitio salen sin listarlas.**
  - «Sin perder a nadie» es Mariana: la toma alguien del equipo y le contesta desde el número de la iglesia, sin compartir un celular. Es
    el bloque «Bandeja del equipo».
  - «Habla con tu iglesia» es la invitación: un envío a toda una red, con entregados, leídos y respuestas. Es el punto 1 del sitio,
    «Campañas a cada red o grupo, con entregados y leídos».
- **La respuesta rápida es el gesto de Kingdom.** Una barra y un toque, y sale el horario completo. Es tan claro como «Igual que la última
  vez» en Eventos y no se parece a él: allá se llena una lista, aquí se llena una respuesta.
- **El cierre es una prueba con nombres.** Primero llegan los números (139 · 137 entregados · 115 leídos · 23 respondieron) y después las
  personas: «Emmanuel Zuluaga Rojas · Leído · ↩ Allí estaré». Ningún grupo de WhatsApp le dice eso a un pastor.
- **Es distinta de los dos clips anteriores donde debe serlo.** Membresía y Eventos terminan con una persona nueva registrada. Aquí la
  persona nueva no se registra: se le **contesta**. El resultado es de alcance (toda una red), no de una ficha.
- **Es nativa del celular.** La bandeja y el reporte se ven completos a 390 px, así que el clip vive en 4:5 y 9:16 con una sola ventana.

### Frases en pantalla

| Segundo | Frase | Cómo entra | Se va |
|---|---|---|---|
| 0,0 | **Alguien nuevo escribe. ¿Quién contesta?** | Una landing por pulso: «Alguien» 0,0 · «nuevo escribe.» 0,5 · «¿Quién» 1,0 · «contesta?» 1,5 (blur 6 px → 0, sin desplazarse) | 4,0, con el toque |
| 4,0 | **Todo tu equipo, un solo número.** | La línea entera, blur 8 → 0 en 0,2 s, con el toque en «Tomar» | 6,0, con el toque en el compositor |
| 12,0 | **Y sabes quién leyó el aviso** | Palabra a palabra, 0,067 s entre palabras | 20,0, blur-out 0,2 s |
| 24,0 | **Habla con tu iglesia, sin perder a *nadie*** (*nadie* en itálica dorada) | Palabra a palabra; el único dorado del cuerpo junto a la ceja | Se queda hasta 28,0 |

Más la ceja «COMUNICACIONES» (Inter, mayúsculas, dorado), que cae en 6,5 sobre la ventana y se va en 24,0.

**De dónde salen las frases:**
- **Frase 2:** junta dos bloques del sitio, «Tu propio número» y «Bandeja del equipo» («Tu equipo toma las conversaciones, responde y se
  las pasa entre sí, sin compartir un solo celular»).
- **Frase 3:** es el punto 1 del sitio («con entregados y leídos») dicho como lo diría un pastor.
- **Frase 4:** es el `titulo` de `modulos.ts` («Habla con tu iglesia por WhatsApp, sin perder a nadie») sin «por WhatsApp». Esa versión
  ocupaba 54 caracteres, tres líneas a 80 px, y chocaba con la ventana. WhatsApp ya está en cada cuadro y en la página del módulo.
  Membresía recortó su `titulo` de la misma forma.

**Lo que ninguna frase nombra:** un número, un nombre, una hora ni el nombre de una campaña. Todo eso cambia con la semilla de Kingdom Demo.

### Recorrido sobre la música

La cuenta es la 101: el administrador de Kingdom Demo, la única cuenta de la demo con Comunicaciones. La app va en celular.

| Compás | Clip | Pantalla real y acción | Movimiento |
|---|---|---|---|
| 1 | 0–2 | **Cuadro 0:** Servir → Comunicaciones → **Bandeja**, vista **«Cola 4»**. Las conversaciones esperando, cada una con su globo de no leídos: «Juan Rivera González · Hola, buenas. ¿Me pueden enviar…», «Carolina Mejía Arango · Quiero saber cómo puedo servir…», **«Mariana Ospina · Hola, buenas noches. ¿A qué hor… · Sin ficha»** y «Camilo Ríos · Sin ficha» | La frase 1 cae en los cuatro pulsos. 1,5–2,0: la cámara se acerca a la fila de Mariana |
| 2 | 2–4 | **2,5: toque en la fila de Mariana** → su conversación entra (match cut sobre el toque, 1,03 → 1,00). Se ve: «Mariana Ospina» · «Sin ficha · +575550123987 · Línea principal» · **«En la cola»** · **«Tomar»** · «Hoy», y su burbuja: **«Hola, buenas noches. ¿A qué hora es el culto del domingo? Es mi primera vez y quiero ir con mi esposo.»** | 3,0–3,5: la cámara encuadra la cabecera y la burbuja; el mensaje se lee a 44 px. En 3,5 el dedo se posa en «Tomar» y espera el bajo |
| 3 | **4,0**–6 | **4,0: toque en «Tomar»** → la píldora pasa a **«Atendiendo»**, «Tomar» se va y aparece la nota **«Andrés Felipe Restrepo Gómez tomó la conversación»**. 5,0: la cámara baja al compositor | Cae la frase 2. El primer cambio grande: la conversación ya es de alguien |
| 4 | **6,0**–8 | **6,0: toque en el compositor y «/»** → suben las respuestas rápidas del equipo: «/bienvenida», **«/horarios · Horarios de los cultos»**, «/oracion», «/gracias», cada una con su texto | Pico: la lista llena la mitad baja del encuadre. La ceja cae en 6,5. «Datos de ejemplo» está desde el cuadro 0 |
| 5 | 8–10 | **8,0: toque en «/horarios»** → la lista se va y el compositor crece con **«Nos reunimos los domingos a las 8:00 a. m. y a las 10:30 a. m., y los miércoles a las 7:00 p. m.»** | La respuesta entera aparece de un toque |
| 6 | 10–12 | **10,0: toque en enviar** → la respuesta queda en el hilo, a la derecha, con «Andrés Felipe Restrepo Gómez», la hora y su palomita (enviado). 10,5: la cámara encuadra la pregunta, la nota y la respuesta | 11,0–12,0: se lee. Es el fin del primer acto |
| 7 | 12–14 | **Respiro.** 12,0: cae la frase 3. **12,5: toque en volver** (se oye; la flecha queda fuera del encuadre) → la lista: **«Cola 3» · «Mis chats 3»**. Mariana ya no espera. 13,0: la cámara abre a la parte de arriba | De aquí a 20 la app va a velocidad normal |
| 8 | 14–16 | **14,0: toque en «Campañas»** (la pestaña con el ícono) → las campañas: «Bienvenida a los nuevos de octubre · Borrador», «Noche de oración del viernes · Fuera de horario», «Recordatorio: Congreso de Jóvenes · Programada»… 15,0: la cámara se acerca a las tarjetas | Las campañas de la iglesia pasan en sus estados |
| 9 | 16–18 | 16,0: la lista baja hasta **«Invitación: culto de jóvenes del domingo · Completada»**, con su barra llena y «137 enviados · 100 % entregados · 84 % leídos · 23 respondieron · 39 clics · 2 fallidos» | La cámara, quieta mientras la app baja |
| 10 | 18–20 | 18,0: la cámara encuadra esa tarjeta. 19,8: el dedo llega a su nombre | |
| 11 | **20,0**–22 | **20,0, segunda subida: toque en la invitación** → su reporte: «Completada», la barra, y los números grandes: **139 Total · 137 enviados · 137 entregados · 115 leídos · 23 respondieron · 39 clics · 2 fallidos** | La frase 3 sale. La cámara abre a los números. La primera prueba |
| 12 | **22,0**–24 | **22,0, el compás más fuerte: toque en «respondieron»** → la tarjeta queda marcada y la lista se filtra. La app baja a **«Destinatarios (23)»**: «Emmanuel Zuluaga Rojas · Leído · ↩ Allí estaré · abrió el enlace», «Liliana Lopera Rojas · Leído · ↩ Allí estaré»… 23,0: acercamiento a los nombres | La prueba más fuerte: las personas, con nombre, que leyeron y respondieron |
| 13 | **24,0**–26 | **24,0, golpe:** cae la frase 4. La ceja se va. La ventana baja a 0,92 y se corre al borde; la cámara abre lo justo para seis nombres con su «Leído» y su «Allí estaré» | La frase final, sostenida |
| 14 | 26–28 | Todo quieto salvo la app (la lista real); la subida desde 26,5; dip en 27,9 | |
| — | **28,0**–30,5 | **La firma sobre el golpe más fuerte:** `cierre-clip` (fondo azul, la corona se levanta, campanas en 28,38, llamado `prueba`) | La corona es el único gesto de marca |

Los nombres, las horas, el número de Mariana y las cifras de la campaña son los de la semilla. El SPEC los marca «(real)» y los toma de la
grabación.

### El lenguaje del movimiento, en una línea por nivel

- **Cada pulso entre 0 y 11 s:** o aterriza una palabra, o hay un toque real, o la app muestra algo nuevo (la conversación, la píldora,
  la lista de respuestas, la respuesta que llena el compositor, la burbuja). La única pausa a propósito es 11,0–12,0: la respuesta enviada
  se lee.
- **Cada compás (2 s):** un movimiento de cámara dentro de la ventana (14 cuadros, `power2.inOut`, con blur de render) y luego quieta.
  Nunca la cámara y el desplazamiento de la app a la vez.
- **Los cambios grandes caen en los golpes:**
  - 4,0: «Tomar» (Kingdom entra con el bajo).
  - 6,0: «/» y las respuestas rápidas.
  - 20,0 y 22,0: el reporte y «respondieron», las dos pruebas.
  - 24,0: la frase final.
  - 28,0: la corona.
- **12–20:** sin cortes de montaje; la app cambia de pantalla por sus propios toques (volver, «Campañas», la invitación), a velocidad
  normal.
- **Transiciones con causa:** el match cut sobre el toque (la conversación que entra en 2,5), los cambios de pantalla de la propia app
  y el dip con corte hacia la firma. Sin iris (no se abre ninguna hoja) y sin látigo (es un solo celular).

### Grabaciones que necesita (Kingdom Demo, `capturar.mjs --modo video`)

Una sola escena de **celular**, `tools/ayuda/escenas/clips/comunicaciones-alguien-nuevo.mjs` (`movil: true`, `toque: false`). Usa la cuenta
101 y la API de las capturas con Meta simulado (`COM_GRAPH_FAKE=1`, `COM_DESPERTAR_WORKER=0`, `COM_GRAPH_FAKE_PLANTILLAS`). Sus tramos:
`cola` · `abrir` · `tomar` · `barra` · `horarios` · `enviar` · `volver` · `campanas` · `bajar` · `reporte` · `respondieron`. Está completa
y lista para copiar en SPEC §3.

**Lo que la demo garantiza**, verificado el 2026-10-30 en `tools/ayuda/semillas/comunicaciones.php`, en el informe de la semilla de hoy
(`F:/dev/kingdom-local/ayuda_capturas_logs/comunicaciones_es.json`) y con consultas a `ayuda_capturas_db`:

- **La línea:** «Línea principal», conectada y simulada: `com_lineas`, calidad GREEN, `TIER_1K`, con su medio de pago.
- **La cola:** 4 conversaciones. La de **Mariana Ospina** (`wa_id 575550123987`, sin ficha, conversación 296) tiene un solo mensaje
  entrante, sin respuesta del chatbot (no coincide con ninguna palabra de activación). Entró por el webhook unas 4 horas antes de la
  consulta, así que la ventana de 24 horas está abierta el día de la semilla.
- **La respuesta rápida** «/horarios» del equipo («Horarios de los cultos»).
- **La campaña completada** «Invitación: culto de jóvenes del domingo», a la red Timoteo:
  - 139 destinatarios: 115 leídos, 22 entregados sin leer y 2 fallidos (así sale «137 entregados»);
  - 23 respondieron «Allí estaré»;
  - 39 clics.

La API local no tiene worker (`COM_DESPERTAR_WORKER=0`) y Meta simulado nunca manda los estados «entregado» ni «leído». Por eso la
respuesta a Mariana queda con **una palomita (enviado)** y así se muestra. Las cifras de entregados y leídos vienen de la campaña que la
semilla ya envió.

### De 4:5 a 9:16

Misma línea de tiempo, misma grabación y mismas cajas de `pasos.json`. El encuadre cambia exactamente como en Membresía y Eventos:
- el titular pasa de 80 a 104 px, con 3 líneas como máximo:
  - la frase 1 se parte «Alguien nuevo / escribe. / ¿Quién contesta?»;
  - la frase 4, «Habla con / tu iglesia, / sin perder a *nadie*»;
- la ventana pasa de 880×1050 (sangra por abajo) a 960×850, completa entre 480 y 1330;
- la cámara G pasa de 2,256 a 2,462 ppc;
- la firma pasa de `cierre-clip` a `cierre-corto`.

---

## Alternativas que se descartaron (una línea cada una)

- **«El chatbot de medianoche»** (Carolina escribe «Hola», el chatbot la saluda con su menú «Horarios · Oración · Hablar con alguien», ella
  pide a una persona y la conversación pasa a la cola): es el «guau» del módulo, pero en la demo esa conversación ya está escrita. La
  grabación no puede hacer llegar un mensaje (no hay paso de webhook en `capturar.mjs`), así que nada se mueve, el pico queda sin gesto y
  la respuesta hay que teclearla. Va al recorrido de 60–75 s, donde «Probar» lo muestra vivo.
- **«Cien invitaciones, una tarde»** (armar la campaña: plantilla con su vista de WhatsApp, público «Red Timoteo», «Calcular», «Enviar»):
  «Calcular» muestra el cupo, los créditos y el costo aproximado en Meta, que la decisión 215 saca del clip. Además, en local una campaña
  lanzada no avanza (no hay worker ni estados de Meta): terminaría en «Enviando · 0».
- **«Por la salud de mi mamá»** (una petición de oración que el chatbot recibe de noche, responde y avisa al equipo): es la imagen más
  pastoral, pero también es historia ya escrita. El aviso al equipo vive en otra pantalla (la campana), así que va al recorrido.
- **«Feliz cumpleaños, solo»** (automatizaciones: «Bienvenida a quien llega» y «Feliz cumpleaños» con sus envíos): es el tercer punto del
  sitio, pero en el celular es un formulario y una lista sin gesto, y «Encender» abre el estimado en cupo y créditos.
- **«Escribió sin ficha»** (Mariana → panel → «Crear ficha» → queda en Membresía): honesta y conectada, pero sería el tercer clip seguido
  que termina en una persona nueva registrada (Valeria, Ximena).
- **«Juan perdió su QR»** (el panel → «Enviar boleta» → la imagen de la boleta en el chat): muy visual, pero es de Eventos masivos (un
  complemento que hoy solo está activo en Kingdom Demo) y la página de Comunicaciones del sitio no lo promete.
- **«Tres columnas»** (la bandeja de escritorio con lista, hilo y panel en `.k-ventana-escritorio`): muestra todo a la vez, pero en 4:5 y
  9:16 pide recortes de escritorio, y la bandeja de celular ya cuenta la historia completa.

## Riesgos y dudas (el detalle en SPEC §5)

- **La ventana de 24 horas de Mariana.** Su mensaje es de la hora de la semilla. `capturar.mjs` vuelve a sembrar si el volcado no es de hoy,
  y la `ref` de la escena exige que haya escrito hace menos de 20 horas. Si se graba con un volcado viejo, el compositor muestra «Enviar
  plantilla» y la escena se niega antes de grabar.
- **«Tomar» pasa por el cargador** (`loading.wrap`: la K animada a los 150 ms). Con la API local no debería asomar; si asoma, se corta en
  la espera.
- **El orden de las respuestas rápidas** (en qué fila queda «/horarios») sale de la grabación. El encuadre del pico toma la lista entera.
- **La tarjeta de la invitación queda al final** de la lista de campañas (es la más vieja de las cinco manuales). Por eso la app baja
  hasta ella; dónde queda después de bajar lo dice `pasos.json`.
- **El toque de «volver» (12,5) se oye pero no se dibuja.** La flecha queda fuera del encuadre que lee la respuesta, como el «Listo» de
  Membresía. Lo que se ve es la lista que entra con «Cola 3».
- **Los textos exactos** cambian con la semilla del día y ninguna frase depende de ellos:
  - los nombres de la cola y de los destinatarios, las horas y las fechas;
  - «Andrés Felipe Restrepo Gómez»;
  - las cifras de la campaña.
