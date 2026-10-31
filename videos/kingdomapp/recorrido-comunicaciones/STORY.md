# Recorrido de Comunicaciones — «Alguien nuevo escribe… y nadie se queda sin respuesta» (historia elegida)

2026-10-30 · El recorrido del módulo para la página `/comunicaciones` del sitio, YouTube y presentaciones (decisión 218 del dueño:
`KingdomApp/docs/videos/README.md` → Clip del sitio → **recorrido del módulo**). Parte del clip publicado
[«Alguien nuevo escribe»](../clip-sitio-comunicaciones/STORY.md) y sigue con lo que una iglesia logra con su WhatsApp. **El dueño ya no
revisa guiones:** la historia la decide la dirección creativa y pasa directo a [SPEC.md](SPEC.md). El sistema de la serie
([Membresía → STORY §3](../clip-sitio-membresia/STORY.md)) se respeta: mismas frases cortas, mismas ventanas, mismas transiciones, mismos
sonidos de acción y la marca solo al final. El formato lo fijó [el recorrido de Academia](../recorrido-academia/STORY.md), que es el modelo.

**Lo que no se reabre:** **16:9 (1920×1080)**, **97,0 s** (92 de cuerpo + el cierre del Comercial de 5) · sin voz, texto quemado ·
«Product Launch» alargada con **una sola costura** en el borde de compás, **la misma edición de Academia, al cuadro** (SPEC §0) · la app real
de Kingdom Demo en `.k-ventana-16x9` y `.k-ventana-escritorio`, nunca un teléfono dibujado · nada inventado, nada de «Próximamente» ·
**decisión 215: ni un crédito, saldo, precio, cupo ni costo de Meta en cuadro** · **cierre del Comercial** con el llamado `prueba`.

## 1. La historia

**Nombre:** «Alguien nuevo escribe… y nadie se queda sin respuesta».

**Idea en una frase:** los primeros 28 s son el clip tal cual (Mariana escribe de noche, el equipo la toma y le responde con «/horarios», y el
reporte de la invitación dice quién la leyó y quién va a estar); después la cámara se abre de una conversación a la iglesia entera y muestra
lo que hace posible que nadie se pierda: **el chatbot que contesta lo mismo a cualquier hora, la ficha de Mariana que nace del chat, la
bienvenida que sale sola a cada persona nueva y el aviso que se arma para una red entera** con la información de Membresía.

**El recurso: tres datos que viajan** (el clip ya traía uno, el domingo):

1. **El horario.** «Nos reunimos los domingos a las 8:00 a. m. y a las 10:30 a. m., y los miércoles a las 7:00 p. m.» es la respuesta que
   Andrés le manda a Mariana con «/horarios» (8–10 s). En la parte 2 **el chatbot da el mismo horario**, palabra por palabra, cuando alguien
   escribe «hola» y toca «Horarios». Es la semilla de la demo: el flujo y la respuesta rápida dicen lo mismo.
2. **Mariana.** En el clip es «Sin ficha». En la parte 2 su misma conversación vuelve (con la respuesta de Andrés ya enviada) y de ahí sale
   **su ficha en Membresía**. El plano siguiente es la automatización «Bienvenida a quien llega», que se dispara **cuando llega una persona
   nueva**: el video no dice que Mariana la recibió (en local no corre el worker, SPEC §5); muestra a las cuatro personas que llegaron antes
   y el mensaje que recibieron, y deja que el espectador ate el cabo.
3. **La red Timoteo y el «Allí estaré».** La invitación del clip salió a 139 personas de la red Timoteo y sus nombres traen «↩ Allí estaré».
   Al final se arma un aviso nuevo: el público es **«Red: Red Timoteo»** (la cifra en vivo cae de toda la iglesia a ≈ 139 con WhatsApp) y
   la vista previa de WhatsApp trae el botón **«Allí estaré»**. El video termina donde empezó todo: hablándole a la iglesia.

**La forma:** la del clip (la ventana del celular a la derecha, las frases a la izquierda) más el escritorio, al que se llega con el
**látigo horizontal** (izquierda = al escritorio; derecha = de vuelta al celular). Cuatro látigos, alternados, en cuatro golpes: 28 · 44 ·
56 · 68. No hay látigo vertical: es siempre la misma persona (Andrés, el administrador) y sus dos aparatos. El alcance crece sin decirlo:
**una conversación → cualquiera que escriba → una persona que entra a la iglesia → cada persona nueva → una red entera**.

**Por qué es la mejor para un pastor que no conoce Kingdom:** el clip ya lo convenció de que su equipo contesta sin compartir un celular; el
recorrido responde las preguntas que siguen —«¿y si escriben a medianoche?», «¿y esa persona queda en algún lado?», «¿le damos la
bienvenida?», «¿cómo le hablo a una sola red?»— con cuatro escenas que son los cuatro puntos del sitio (`modulos.ts` → comunicaciones →
`puntos` y `bloques`: el chatbot, la bandeja, los mensajes automáticos y las campañas con el público de Membresía). Lo que el video dice y
lo que dice la página son lo mismo.

## 2. Frases en pantalla (una a la vez; Fraunces 560, 84 px)

| Segundo | Frase | Dónde | Cómo entra | Se va |
|---|---|---|---|---|
| 0,0 | **Alguien nuevo escribe. / ¿Quién contesta?** | columna izquierda | una landing por pulso (0,0 · 0,5 · 1,0 · 1,5), como el clip | 4,0, con el toque en «Tomar» |
| 4,0 | **Todo tu equipo, / un solo número.** | izquierda | la línea entera, blur 8 → 0 | 6,0, con el toque en el compositor |
| 12,0 | **Y sabes quién / leyó el aviso** | izquierda | palabra a palabra | **27,9** (en el clip se iba en 20,0: aquí acompaña el reporte y los nombres) |
| 28,0 | **Responde a cualquier hora.** | arriba (escritorio), una línea | palabra a palabra | 43,9 |
| 44,0 | **De un chat / a su ficha.** | izquierda | palabra a palabra | 55,9 |
| 56,0 | **La bienvenida sale sola.** | arriba (escritorio), una línea | palabra a palabra | 67,9 |
| 68,0 | **Cada aviso, / a quien lo necesita.** | izquierda | palabra a palabra | 83,9 |
| 84,0 | **Habla con tu iglesia, / sin perder a *nadie*** (*nadie* en itálica dorada; el `titulo` de `modulos.ts` sin «por WhatsApp», como en el clip) | izquierda | palabra a palabra | se queda hasta 92,0 |

Más la ceja «COMUNICACIONES» (Inter 700, 28 px, dorada), que entra en 6,5 como en el clip, acompaña a cada frase en su escenario y se va en
84,0. Leídas solas, las ocho frases son el argumento; vistas sin sonido, las imágenes cuentan lo mismo.

De dónde sale cada frase (nada inventado): «a cualquier hora» es de la `bajada` del sitio («un chatbot que atiende a cualquier hora»);
«a su ficha» describe «Crear ficha» de la bandeja (bloque «Bandeja del equipo» y la ayuda); «sale sola» describe el bloque «Mensajes
automáticos» («Kingdom envía el mensaje que preparaste»); «a quien lo necesita» es de la `bajada` («campañas a quien las necesita»). La
frase final es la del clip.

## 3. Recorrido sobre la música (compases de 2 s; la grilla exacta en SPEC §0)

| Compás | Video | La pista | Pantalla real y acción | Movimiento |
|---|---|---|---|---|
| 1–14 | **0–28** | 14,05–42,05 | **El clip, cuadro por cuadro** (su grabación, sus cortes y sus toques), llevado a 16:9: la ventana del celular a la derecha, las frases a la izquierda. Sin la ventana a un lado en 24,0, sin el dip ni la firma | Las cámaras del clip con el piso de lectura de 16:9 (SPEC §2.1) |
| 15 | **28,0**–30 | 42,05 (1,00, el más fuerte) | **Látigo horizontal al escritorio** (101): el editor del flujo «Bienvenida con menú», con su lienzo (el paso «¿En qué te podemos ayudar?» y sus tres salidas) y las palabras «hola · menu · buenas» | Cae «Responde a cualquier hora.» |
| 16 | 30–32 | 44,05 | **30,0: toque «Probar»** → el simulador: «Probar el flujo · Es una prueba: no se envía nada por WhatsApp ni queda nada guardado · Probando como Carolina Mejía Arango» | La cámara al simulador |
| 17 | **32,0**–34 | 22,05 (costura) | Se escribe **«hola»** y se envía (33,0) | Toque, teclas, toque |
| 18–21 | 34–42 | 24,05–32,05 (respiro) | 34,0: el chatbot contesta: «Empezó el flujo «Bienvenida con menú»» · «¡Hola Carolina! Bienvenido a Kingdom Demo.» · «¿En qué te podemos ayudar?» con **Horarios · Oración · Hablar con alguien** · 38,0: toque «Horarios» → **«Nos reunimos los domingos a las 8:00 a. m. y a las 10:30 a. m., y los miércoles a las 7:00 p. m. ¡Te esperamos!»** · «El flujo terminó» | El respiro: una cámara por compás, la respuesta se lee |
| 22 | 42–44 | 32,05 | Quieto: el horario | — |
| 23 | **44,0**–46 | 34,05 (0,93, segunda subida) | **Látigo horizontal de vuelta al celular:** la conversación de Mariana, ya «Atendiendo», con su pregunta y la respuesta de Andrés | Cae «De un chat a su ficha.» |
| 24–26 | 46–52 | 36,05–42,05 | 46,0 el ícono de la persona → el panel «Sin ficha» · 48,0 **«Crear ficha»** → el formulario con «Mariana» y «Ospina» ya puestos y «Con el número +575550123987» · 50,0–51,5 «¿Cómo llegó?» → la forma → «Crear ficha» | Un toque por golpe |
| 27 | **52,0**–54 | 42,05 (1,00) | **El panel con la ficha de Mariana Ospina** y «Ver ficha» | El punch de la parte 2 |
| 28 | 54–56 | 44,05 | El panel entero | La cámara abre |
| 29–30 | **56,0**–60 | 46,05–50,05 (0,98) | **Látigo horizontal al escritorio:** Automatizaciones: «Bienvenida a quien llega · Encendida · Cuando llega una persona nueva (1 h después) · Hoy: 4 enviados»; al lado, «Feliz cumpleaños» | Cae «La bienvenida sale sola.» |
| 31–32 | **60,0**–64 | 50,05–54,05 (clímax) | **60,0: toque en la tarjeta** → la automatización, con su vista previa: **«Hola Ana, gracias por visitarnos en Kingdom Demo. Alguien del equipo te escribirá para acompañarte…»** | El mensaje se lee |
| 33–34 | **64,0**–68 | 54,05–58,05 (clímax) | **64,0: «Envíos»** → quién la recibió: Mateo Arango Vélez, Sara Lucía Bermúdez Ríos, Tomás Cano Ochoa, Isabela Muñoz Salazar, con «Leído» o «Entregado» | Los nombres |
| 35–38 | **68,0**–76 | 58,05–66,05 (clímax, segunda frase) | **Látigo horizontal de vuelta al celular:** una campaña nueva en «A quién va». 70,0 «Un público» · 71,0 «Agregar filtro» · 72,0 «Red» · 73,0 «Red Timoteo» · 74,0 «Aplicar» → **74,5: «Red: Red Timoteo» y la cifra que baja a ≈ 139 con WhatsApp** | Cae «Cada aviso, a quien lo necesita.» |
| 39–42 | **76,0**–84 | 66,05–74,05 (salida) | 76,0 la app sube al mensaje · 77,0 «Plantilla aprobada» · 78,0 **«invitacion_culto»** → la vista previa de WhatsApp se llena: «Hola Ana, este domingo celebramos la Santa Cena. Te esperamos a las 10:30 a. m. con toda tu familia.» · **Allí estaré · Cómo llegar** | La música baja sola; la cámara a la burbuja |
| 43–46 | **84,0**–92 | 74,05–82,05 | Quieto: la burbuja con «Allí estaré» | Cae la frase del sitio; la ventana se hace a un lado; la subida; el dip |
| — | **92,0**–97,0 | 82,05 → fin | **`cierre-comercial`** (noche, «Kingdom es para *toda la iglesia*», «Prueba gratis 30 días», `kingdom-sitio.web.app`), campanas en 92,38 | El único gesto de marca |

### Lo que este recorrido hace distinto dentro del sistema (y por qué)

- **Sin látigo vertical.** Academia lo usa porque cambia de persona (profesor, alumna); aquí todo lo hace Andrés, así que el único cambio
  es de aparato: celular ↔ escritorio, cuatro veces, alternado. Cada mundo de un escenario reemplaza al anterior mientras su ventana está
  fuera de cuadro (SPEC §1.4).
- **Dos toques «se oyen y no se dibujan» dentro de un corte** (1800 y 1920 en la automatización): la cámara está en la vista previa o en la
  tarjeta y lo que cambia es la pantalla entera; la cámara se fija en el cuadro del corte, como el reporte del clip (REVIEW del clip §4.3).
- **El simulador es honesto en cuadro.** «Probar el flujo» y «Es una prueba: no se envía nada por WhatsApp ni queda nada guardado» se leen
  en el primer encuadre del simulador; la frase dice que el chatbot responde, y la pantalla dice que esto es su prueba.
- **La persona con la que se prueba se elige en un corte** («Probando como Carolina Mejía Arango»): es un ajuste de la prueba, no la
  historia, y sin él el chatbot saludaría «¡Hola Persona!». Carolina es la de la cola del clip (0–2 s), la que llegó a la cola por este
  mismo flujo en la semilla.
- **La costura de la música cae dentro del simulador** (32,0): ahí se escribe «hola»; la imagen no corta y la frase está quieta.
- **El cierre es el del Comercial (5 s, 16:9)**, sobre el final natural de la pista: no hay fundido.

## 4. Capacidades consideradas y descartadas (una línea cada una)

- **Lanzar la campaña («Calcular» → «Enviar»):** «Calcular» muestra el cupo, los créditos y el costo aproximado en Meta (decisión 215), y en
  local una campaña lanzada se queda en «Enviando · 0» (no hay worker ni estados de Meta). El recorrido arma el público y el mensaje, y el
  reporte de una enviada ya está en la parte 1.
- **Encender una automatización:** «Encender» abre el estimado con su costo en cupo y créditos (215). Se muestra una encendida y sus envíos.
- **Mariana en los envíos de la bienvenida:** el envío lo crea el worker una hora después del suceso; en local no corre y meterlo por SQL
  sería fabricar lo que el sistema no hizo en la grabación. El video lo deja implícito.
- **Transferir la conversación a otra persona del equipo:** en Kingdom Demo solo la cuenta 101 tiene Comunicaciones; la lista de a quién
  pasarla sale vacía.
- **La petición de oración que el chatbot avisa al equipo (la campana):** es la imagen más pastoral, pero depende del aviso del motor de
  notificaciones en la base de capturas, que no se verificó; queda para cuando haya un recorrido de Notificaciones.
- **El constructor de plantillas con la revisión de categoría:** es la herramienta de quien coordina y su mensaje («Meta la cobraría más»)
  roza el costo; la vista previa de WhatsApp ya aparece en la campaña.
- **El chatbot en el celular (la vista «Pasos»):** se ve como un chat, pero se pierde el lienzo, que es lo que le dice al pastor que el
  chatbot lo arma su iglesia.
- **Las boletas por WhatsApp (Eventos masivos):** es un complemento que hoy solo está activo en Kingdom Demo y la página de Comunicaciones no
  lo promete.
- **Terminar en el reporte con los nombres (como el clip):** ya es la parte 1; el final en la burbuja con «Allí estaré» cierra el círculo
  hacia adelante.

## 5. Lo que la demo tiene (verificado el 2026-10-30, en código)

- **Cuenta:** 101, Andrés Felipe Restrepo Gómez, la única de Kingdom Demo con Comunicaciones (`_demo_capturas.php`; `$YO` de la semilla).
- **El flujo «Bienvenida con menú»** (`tools/ayuda/semillas/comunicaciones.php` §5): se activa con «hola» (exacta), saluda «¡Hola
  {{persona.primer_nombre}}! Bienvenido a {{iglesia.nombre}}.», pregunta «¿En qué te podemos ayudar?» con **Horarios · Oración · Hablar con
  alguien**, y «Horarios» termina con el mismo horario de la respuesta rápida «/horarios» más «¡Te esperamos!». Sin varios idiomas: no
  pregunta el idioma. «Probar» (`chatbot-simulador.component.ts`, `comBotProbar`) no envía ni guarda nada; sin persona saluda a «Persona de
  prueba», por eso se prueba como Carolina.
- **Carolina Mejía Arango** es la persona de la semilla que escribió «Hola», tocó «Hablar con alguien» y quedó en la cola con «Quiero saber
  cómo puedo servir en el grupo de alabanza» (la segunda fila de la cola del clip).
- **Mariana Ospina** (`575550123987`, sin ficha, en la cola): la escena la toma y le responde con «/horarios» fuera de cámara, igual que el
  clip, para que la conversación llegue como la dejó la parte 1. «Crear ficha» (`bandeja-crear-ficha.component.ts`) trae «Mariana» y
  «Ospina» del perfil y el número; pide «¿Cómo llegó?»; revisa duplicados (mismo teléfono o mismo nombre).
- **La automatización «Bienvenida a quien llega»** (semilla §9): suceso `membresia.persona_creada` («Llega una persona nueva»), espera 60 min,
  plantilla `bienvenida_nuevos` («Hola {{1}}, gracias por visitarnos en {{2}}. Alguien del equipo te escribirá para acompañarte. Si
  necesitas algo, responde a este mensaje.»), encendida. La semilla registra a Mateo Arango Vélez, Sara Lucía Bermúdez Ríos, Tomás Cano
  Ochoa e Isabela Muñoz Salazar y corre el worker: sus cuatro envíos quedan con la mitad «Leído».
- **La campaña nueva:** el editor (`campana.page.ts`) usa el editor de públicos de Membresía (`segmento-editor.component.ts`) con la cifra en
  vivo «≈ N personas · M con WhatsApp»; la red **Red Timoteo** existe (la de la invitación del clip, 139 destinatarios con WhatsApp el día de
  la semilla). La plantilla `invitacion_culto` (aprobada) trae los botones «Allí estaré» y «Cómo llegar»; la vista previa usa los ejemplos
  de la plantilla («Ana», «la Santa Cena»). Nada se calcula ni se envía.

## 6. Riesgos (el detalle en SPEC §5)

- **La ventana de 24 horas de Mariana** (la escena de celular le responde): la misma `ref` del clip (escribió hace menos de 20 horas).
- **Duplicados al crear la ficha:** una `ref` exige que no haya otra Mariana Ospina ni el mismo número; si aun así aparecen fichas
  parecidas, la escena toca «Crear de todos modos» y el toque del 51,5 se marca sobre ese botón.
- **La cifra de la red Timoteo** puede no ser exactamente 139; ninguna frase la nombra.
- **La vista previa de la campaña está arriba del formulario en el celular:** al elegir la plantilla puede crecer fuera de la vista; la
  escena sube hasta ella y el montaje usa ese desplazamiento (76,0 / 80,0).
- **El escritorio se lee solo de cerca** (D = 1,8): cada encuadre se elige con la grabación.
- **La costura de la música** es la de Academia, medida y no oída: se oye en la vista previa antes del render.
