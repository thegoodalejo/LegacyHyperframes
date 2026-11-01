# SPEC — Eventos de ciudad, sin perder a nadie

Storyboard escena por escena. Sistema visual: `frame.md` (copia de `_identidad/frame-recurso.md`, kit v1.2). 1920×1080, 30 cps, «Product
Launch» en bucle (pulsos de 0,5 s, compases de 2 s). Todo se anima con `KRecurso.tiempos(window)`: las entradas caen en la palabra que se
oye (−0,08 s) o en el pulso más cercano; los cambios grandes, en el pulso de la frase; las salidas, en los últimos 0,5–0,6 s.

**Reglas comunes de movimiento:** entradas de 24–40 px con desenfoque de 6 px que se va, `power3.out` de 0,35–0,6 s; escalas `back.out(1.8–2.4)`
solo en puntos, íconos y nodos; latidos de 1,03–1,12 en pulsos para que nada quede quieto más de ~6 s; salidas `power2.in` hacia arriba con
desenfoque. Nada de giros, destellos ni partículas. Cifras siempre con «Datos de ejemplo».

**Fuentes** (worktree `KingdomApp-recursos`): EM = `docs/modulos/eventos-masivos.md`; CO = `docs/modulos/comunicaciones.md`; SITIO =
`sitio/src/data/modulos.ts`; AY = `frontend-v2/src/ayuda/es/<ruta>.md`; TE = `docs/modulos/testimonios.md`.

| Escena | Dura | Molde | Qué se ve (en orden, con su disparador) |
|---|---|---|---|
| intro (kit) | 6 s | — | `intro-recurso` con la ceja «Recursos» y el título |
| gancho | 18 s | Ciudad de puntos → estadio → gigante | Suelo que se dibuja y 26 columnas de puntos que suben en pulsos (la ciudad) · cinco iglesias que se unen al centro · 220 puntos que llegan de los bordes al estadio (55 % tenues: «muchas no son de tu iglesia») · el estadio se cierra y late · todo se apaga, el punto dorado se aleja y «¿Cómo no perder a *nadie*?» en gigante en el pulso (con `desliz`) |
| promesa | 22 s | Tarjetas → dos nodos → ruta | Cuatro preguntas en tarjetas, una por cada «quién» · se recogen en el nodo «Eventos *masivos* / Complemento de Eventos» (con `aparicion`) · «Comunicaciones / El WhatsApp de tu iglesia» y la línea dorada que los une · suben y aparece la ruta 1–4 (Antes, El día, Después, La conversación) con el punto dorado que la recorre en cada palabra |
| cap-1 | 4 s | Kit | «Antes del *evento*», ícono `confirmation_number` |
| inscripcion | 27,5 s | Dos columnas: texto cinético + diagrama | El formulario late · las tres puertas (Enlace, QR, WhatsApp) en sus palabras y sus caminos se dibujan · 18 puntos (color = origen) viajan al formulario · anillos «Tu Membresía» (sólido) y «Participantes del evento» (punteado) y 36 puntos que se reparten · el punto dorado va a participantes y sube a Membresía en «teléfono», con `how_to_reg` |
| boletas | 24 s | Objeto central que se transforma | Boleta abstracta (franja de color, rayas y un QR de 9×9 con semilla) que arma su QR en tres pulsos (con `aparicion`) · GENERAL / VIP / STAFF en fila, cada uno en su palabra, saltan en «color» · dos boletas «General 1/2» con sus reglas («Si es pastor →», «Si es líder →») · la boleta dorada viaja por un arco al globo del chat; reloj de 24 h con la franja 07:00–21:00 · «En el mismo chat» y el globo late |
| servir | 16,5 s | Ícono grande + cascada | Nodo `volunteer_activism` y «Quiero *servir*» · «Un enlace y un QR propios, sin cuenta» · caen tres solicitudes (Medios, Logística, Alabanza) · el visto verde en cada una (con `confirmacion`), su línea cambia a «Staff · …» (Logística con «— Zonas generales») · Día 1, 2, 3 se encienden en dorado |
| cap-2 | 4 s | Kit | «El día del *evento*», ícono `stadium` |
| equipo | 14 s | Fila → tres funciones → marco | Nueve personas en fila · Ingreso, Conteo y Testimonios en sus palabras, tres personas bajan a cada una · marco punteado «El evento» y cuatro íconos afuera apagados · «Sin ver otras partes de Membresía» |
| ingreso | 20 s | Fila que cruza una puerta | La línea del escáner y el QR arriba · 22 personas cruzan en pulsos: onda verde y «¡Bienvenido!», una ámbar «Ya entró hoy» · contador «entraron hoy» (Datos de ejemplo) · sin señal: `wifi_off`, la puerta gris, los ingresos se apilan y sube «por enviar» · vuelve: la nube los recibe y el contador los suma · alguien sin boleta (punto con borde) se detiene, `person_add`, se vuelve verde y entra |
| manillas | 22 s | Par vinculado → tres contadores | La banda con su código (barras con semilla) y la boleta unidas por la línea dorada · tres tarjetas de conteo (Pasó al altar, Aceptó a Cristo, Aforo general) y las manillas que llegan a las dos primeras con su contador · el aforo suma con +1, +5, +10 y +20 · «Etiqueta de Membresía» se pega a «Aceptó a Cristo» y late |
| testimonios | 16 s | Línea de tres etapas + firma | La luz del escáner recorre la manilla · «La persona» y «El evento» ya puestos · Antes, Durante y Después (tenues desde el inicio de la frase, se encienden en su palabra) unidos por la línea · la firma se dibuja sobre su renglón hasta el visto (con `confirmacion`) |
| cap-3 | 4 s | Kit | «Después, que *nadie* se pierda», ícono `route` |
| ruta | 30 s | Dos carriles | Carriles «Mensajes del evento / A todos los inscritos» y «Seguimiento / Solo a los participantes nuevos» se dibujan · marcas Al registrarse, Días antes, El evento; los envíos viajan · 15 participantes nuevos, tres llamadores y el reparto parejo · tarjeta «Reporte de la llamada»: interés 4 de 5, transporte, alojamiento · todo se apaga; el punto dorado pasa a la iglesia (con `confirmacion`), entra a la red, su ruta de crecimiento crece y el llamador se acerca |
| reportes | 22 s | Gigante → tablero → tabla → embudo | «Todo se puede *medir*» · barras por día, por camino, por tipo de boleta y «entraron» con contador · tabla cruzada (de dónde vienen × rol) que se enciende por columnas y «Reporte guardado» · embudo Enviadas → Llegaron → Leídas → Tocaron un botón con contadores. «Datos de ejemplo» todo el tiempo |
| cap-4 | 4 s | Kit (claro, el único) | «La conversación *no se corta*», ícono `forum` |
| linea | 26 s | Dos columnas: texto + constelación | La iglesia y su número (anillo punteado) con diez personas que le escriben · «Con Kingdom» · el chatbot ocupa el centro y responde a seis (globos dorados) · «A cualquier hora» · quien pide a alguien pasa a la bandeja · tres personas del equipo toman las conversaciones |
| campanas | 32,5 s | Pista con cuatro estaciones (cámara) | Plantilla abstracta con sus datos `{nombre}` `{evento}` `{fecha}`, botones y «Aprobada por WhatsApp» · tres públicos (Una red, Con una etiqueta, Inscritos de un evento) hacia el envío; «Ahora / Programada» · reloj de 24 h: la franja dorada, la medianoche apagada y la aguja que espera hasta las 07:00 · tres automatizaciones (Llega alguien nuevo, Un día antes de cada reunión, El día de su cumpleaños) · Invita, Confirma, Da *seguimiento* |
| resultado | 16,5 s | Recorrido → multitud | Ocho íconos del recorrido con su línea · en el golpe (con `subida`), «Un evento de *ciudad*» en gigante sobre 220 puntos y seis dorados al centro: «Con pocas personas» · barrido azul de izquierda a derecha («medido») · 18 nuevos en verde, cada uno unido a alguien del equipo |
| acompanamiento | 12 s | Dos nodos y apretón | «No lo haces *solo*» · Tu iglesia — apretón de manos — Kingdom; el evento, el chat y la ruta viajan de Kingdom a la iglesia · «*Escríbenos* y lo preparamos contigo» |
| cierre (kit) | 9 s | — | `cierre-recurso` con «Sigue con: La experiencia del nuevo», llamado de acompañamiento y el WhatsApp |

## La voz y su fuente

| Escena | Frase (resumen) | Fuente |
|---|---|---|
| gancho | Cruzada, congreso de varias iglesias, miles inscritos durante meses, muchos no son de la iglesia | EM → «Objetivo» (congreso pastoral, cruzada, se prepara durante meses, traen varias iglesias) y «Principios» 1 |
| promesa | Quién se inscribió, llegó, pasó al altar, quién lo llama; Eventos masivos es un complemento de Eventos; Comunicaciones es el WhatsApp de la iglesia | EM → «Objetivo», «Qué es y cómo se activa»; AY `eventos/eventos-masivos` («complemento del módulo Eventos»); SITIO → comunicaciones («WhatsApp de tu iglesia») |
| inscripcion | Sin cuenta; enlace, QR o la palabra del evento al WhatsApp; las mismas preguntas y queda el origen; participante con ficha que no llena Membresía; el miembro se reconoce por su teléfono y no se duplica | EM → «Objetivo», «Principios» 1, 2 y 5, glosario «Origen», «La página pública», «Inscripción por WhatsApp», «Qué pasa por dentro con la persona»; AY `eventos/masivos-formulario-publico` |
| boletas | Boleta con QR; tipos General, VIP, staff con su color; reglas por respuesta (pastores en una, líderes en otra); llega al WhatsApp dentro del horario de envío; por el chat, ahí mismo | EM → «Tipos de boleta (W10)» (reglas «Apóstol, Pastor o Profeta → General 1; Líder → General 2»), «La página pública» paso 5, «Inscripción por WhatsApp» paso 4; AY `eventos/tipos-de-boleta` |
| servir | Quiero servir con su enlace; función e iglesia de donde viene; el equipo aprueba, elige el tipo de staff y la boleta sale, vale todos los días | EM → «"Quiero servir" y el staff», «Tipos de boleta» (staff vale todos los días); AY `eventos/quiero-servir` |
| equipo | Equipo del evento con funciones ingreso, conteo, testimonios; actúa solo en ese evento, sin ver otras partes de Membresía | AY `eventos/equipo-del-evento` |
| ingreso | Escanear el QR; verde bienvenido, ámbar ya entró hoy; cada ingreso es su asistencia; sin señal guarda y envía al volver; sin boleta se inscribe en la puerta | AY `eventos/ingreso-con-boletas`, `eventos/manillas` («Llegó sin boleta: inscribir en la puerta») |
| manillas | Manilla vinculada a la boleta; el equipo de conteo registra altar y aceptó a Cristo sin papel; aforo sin manilla +1, +5, +10; etiqueta de Membresía para seguimiento | AY `eventos/manillas`, `eventos/conteos-del-evento`; EM → «Manillas y conteos (decisión 227)» |
| testimonios | El equipo de testimonios escanea la manilla; persona y evento ya puestos; antes, durante y después; la persona firma en el celular | AY `eventos/testimonios-en-el-evento`; TE → glosario «Testimonio» (tres etapas) |
| ruta | Mensajes del evento a todos (al registrarse, días antes, con la boleta); llamadores con Mi seguimiento; interés, transporte, alojamiento y reporte; pasar a la iglesia: red, ruta de crecimiento, quien lo acompañe | EM → «La ruta del evento» (carriles 1 y 2), «Participantes, duplicados y la ficha» → «Pasar a la iglesia»; AY `eventos/masivos-ruta-del-evento`, `eventos/masivos-llamadas` |
| reportes | Inscritos por día, por camino (origen), por tipo y cuántos entraron; cruzar dos preguntas y guardar; Envíos: llegó, leída, botón tocado | EM → «Reportes del evento», «Envíos de boletas»; AY `eventos/masivos-reportes`, `eventos/envios-de-boletas` |
| linea | Número propio de WhatsApp con su nombre; te acompañamos a conectarlo; chatbot a cualquier hora que inscribe con la palabra; bandeja; el equipo toma y responde sin compartir un celular | SITIO → comunicaciones («Tu propio número… Te acompañamos a conectarlo», «Chatbot», «Bandeja del equipo», «un chatbot que atiende a cualquier hora»); EM → «Inscripción por WhatsApp» |
| campanas | Plantillas aprobadas con datos y botones; campaña a un público por red, etiquetas o inscritos de un evento, ahora o programada; horario de envío; automatizaciones (llega alguien nuevo, un día antes de cada reunión, cumpleaños) | AY `comunicaciones/plantillas`, `comunicaciones/campanas` (horario 07:00–21:00), `comunicaciones/automatizaciones`; SITIO → «Campañas con plantillas» |
| resultado | Un evento de ciudad con pocas personas; cada asistente con boleta y medido en la entrada; cada nuevo con su ruta y quien lo siga | Resumen de lo anterior (sin cifras ni promesas de resultado) |
| acompanamiento | Kingdom acompaña a mejorar los procesos de la iglesia | `frame.md` → llamado `acompanamiento` |

## Pronunciación

Revisada con el fonemizador del kit (espeak `es`): «Kingdom» → `kˈiŋɡðom` (acento en la primera, bien), «QR» → `kuˈɛre`, «staff» → `stˈaff`,
«WhatsApp» → `wˈats ˈapp`. No hace falta `voz` alterno.
