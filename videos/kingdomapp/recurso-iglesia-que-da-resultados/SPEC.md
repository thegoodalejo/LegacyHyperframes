# SPEC — Tu iglesia, con resultados que se ven

Storyboard escena por escena. Sistema visual: `frame.md` (copia de `_identidad/frame-recurso.md`, v1.2). 1920×1080, 30 cps, noche del
kit debajo de todo el cuerpo. Duración medida por `preparar`: intro 6 s + cuerpo 331 s + cierre 9 s = **346 s (5:46)**.

## Reglas de todo el video

- **Texto:** Fraunces 560 para rótulos (96 px titular, 72 px frase, 112–150 px en golpes), Inter 600 para etiquetas (28–36 px). Nada bajo
  28 px. Cada rótulo es un resumen corto de la frase (los subtítulos completos van en el VTT); sus palabras entran con la voz
  (`T.palabra(...).inicio − 0,08 s`, subir 26 px, desenfoque 6 px → 0, `power3.out` 0,38 s) y salen 0,3 s antes de la frase siguiente
  (subir 24 px, desenfoque, `power2.in` 0,3 s). Las *claves* del rótulo, en dorado.
- **Diagramas:** personas = `.k-recurso-punto`; redes, equipos, pasos = `.k-recurso-nodo` con ícono del kit; vínculos = `.k-recurso-linea`
  que se dibuja (`strokeDashoffset`). Cumplido = anillo y ícono dorados. Escalas con `back.out(1,8–2,2)` solo en cosas pequeñas.
- **Ritmo:** entradas en pulsos (`T.pulso`, `T.reparto`); un cambio cada 1–3 s; nada quieto más de ~4 s (anillos que laten, derivas lentas
  de `sine`). Cada escena sale en sus últimos 0,6 s (subir 30 px + desenfoque).
- **Datos de ejemplo:** la etiqueta del kit está en pantalla siempre que hay una cifra, una barra, una línea o el mapa.
- **Semáforo:** verde `#26a69a` (verde-suave del kit), amarillo = dorado `#e8b95a`, rojo `#e06c5a` (la paleta del kit no trae rojo; solo
  se usa en los semáforos), gris = anillo `tinta-2`.
- **Prohibido y respetado:** nada de la app (ni pantallas ni teléfonos), ninguna cifra de resultados, ningún testimonio, ninguna iglesia ni
  persona real, ningún precio, nada de la hoja de ruta (las redes y solicitudes de Equipos no se nombran; las sesiones por Google Meet
  tampoco, porque están dormidas: pendientes 41).

## Escenas

Fuentes (todas del worktree `F:\Proyectos\KingdomApp-recursos`): **mem** = `docs/modulos/membresia.md`, **ev** = `docs/modulos/eventos.md`,
**ac** = `docs/modulos/academia.md`, **eq** = `docs/modulos/equipos.md`, **ar** = `docs/modulos/arranque.md`, **mod** =
`sitio/src/data/modulos.ts`.

### 0 · Intro del kit (0–6 s)
Título «Tu iglesia, con *resultados* que se ven», ceja «Recursos». Sonido de marca del kit.

### 1 · `sabias` — el gancho (6–23 s)
| Voz | Fuente |
|---|---|
| ¿Sabías que con Kingdom puedes estructurar tu iglesia? | mem → «Estructura» (redes, discipulado, acompañamiento) |
| Tus redes, tus grupos y tus líderes, cada uno en su lugar. | mem → «Estructura» (redes con sus líderes; organigrama del discipulado) |
| Y debajo de cada líder, las personas que cuida. | mem → «Estructura» (discipulado: «N directos · M en total»), «Objetivo» |
| Tu iglesia deja de ser una lista de nombres, y se ve como lo que es: una red de cuidado. | mem → «Objetivo» (por persona, por red y por iglesia) |

Pantalla: titular centrado arriba. 32 personas aparecen sueltas en pulsos y derivan; en «estructurar» van a su sitio y aparece la iglesia
(nodo dorado `church`, anillo que se expande). En «redes», 4 nodos `groups` con sus líneas; en «grupos», laten; en «líderes», 8 nodos
`person`. En «personas», las líneas líder→persona se dibujan y los puntos se encienden. En «red», todo el árbol pasa a dorado y respira en
tres pulsos. Etiquetas de nivel a la izquierda (Redes, Líderes, Personas). Sonido `aparicion` en «estructurar».

### 2 · `pastor` — la idea central (23–46 s)
| Voz | Fuente |
|---|---|
| Pastor, tú no tienes que pasar el día en la app. | Pedido del dueño (BRIEF) |
| Tus líderes son los que la usan: reportan, acompañan, enseñan y sirven. | ev → «Reportar»; mem → «Mi seguimiento»; ac → «Objetivo»; eq → «Objetivo» |
| Kingdom les da una forma clara de hacer su trabajo con excelencia. | Pedido del dueño (BRIEF) |
| Y a ti te muestra lo que importa: los resultados. | mem → «Tableros»; ev → «Tablero y mapa»; ac → «Seguimiento… y tablero»; eq → «Reportes» |
| Veamos lo que puedes medir en cuatro módulos: Membresía, Eventos, Academia y Equipos. | mod (los cuatro módulos) |

Pantalla: dos columnas. A la derecha, el pastor (nodo dorado, rótulo arriba) y cuatro líderes en arco, cada uno en su verbo (`edit_note`,
`handshake`, `school`, `volunteer_activism`). En «excelencia» se encienden en dorado, uno por pulso. En la frase 3, luz que sube por las
líneas en tres pulsos; en «resultados», el ícono del pastor pasa de `person` a `insights` con un anillo. Frase 4: titular arriba y los
cuatro módulos en fila (168 px), cada uno en su nombre, unidos por una línea dorada; laten en pulsos al final.

### 3 · Capítulo 1 «Membresía: que *nadie* se pierda» (46–50 s) — `groups`, noche

### 4 · `cuidado` (50–72 s)
| Voz | Fuente |
|---|---|
| Todo empieza con las personas. | — (transición) |
| Cuando alguien llega por primera vez, se registra desde el celular, aun sin señal. | mem → «Registrar a alguien (también sin señal)»; mod (Membresía, puntos) |
| Y no se queda solo: quien coordina reparte a los nuevos de forma pareja entre quienes acompañan. | mem → «Tablero del coordinador» (Nuevos: «Repartir» de forma pareja) |
| Cada acompañante lo ve en Mi seguimiento: a quién llamar y qué paso sigue. | mem → «Mi seguimiento»; mod (Membresía → «Mi seguimiento») |
| Y tú sabes quién ya recibió su llamada, y quién todavía no. | mem → «Tablero del coordinador» (sin llamar a tiempo); mod («nadie nuevo se queda sin llamada») |

Pantalla: la iglesia como 26 puntos tenues en círculo; el nuevo (dorado) entra desde la derecha; «Sin señal» (`wifi_off`) y luego
«Registrada» (`task_alt` verde). Tres acompañantes; seis nuevos que, en «pareja», van dos a cada uno con su línea dorada. En «llamar»
laten; en «sigue», una flecha junto a cada acompañante. Frase 4: cuatro de seis pasan a verde, los otros dos laten; «4 de 6 con su
llamada» y «Datos de ejemplo».

### 5 · `semaforo` (72–93 s)
| Voz | Fuente |
|---|---|
| Además, cada persona tiene un semáforo de actividad. | mem → «Semáforo de actividad (2026-10-29)» |
| Verde, si participó hace poco. / Amarillo, si se está alejando. / Rojo, si hace tiempo que no la vemos. / Y gris, si no tiene actividad. | ídem → «Los colores» |
| Tu iglesia decide cuántos días vale cada color. | ídem → «Ajustes → Seguimiento» (días configurables; por defecto 10, 30 y 50) |
| Así ves a tiempo a quien se está enfriando, y lo buscas antes de perderlo. | ídem (filtro, Tableros → Resumen) |

Pantalla: titular arriba; cuatro círculos de 190 px, cada uno en su color al pulso de su frase, con personas que caen dentro (sonido
`toque` en el verde). Los días por defecto debajo de cada color, uno por pulso. Frase final: la iglesia en una barra de partes (48/27/15/10 %,
Datos de ejemplo); en «a tiempo» se enmarca el amarillo, su círculo late y lo demás se atenúa.

### 6 · `ruta` (93–113,5 s)
| Voz | Fuente |
|---|---|
| Cada persona también tiene su ruta de crecimiento. | mod (Membresía → «Ruta de crecimiento»); mem → «Ajustes de la ruta» |
| La llamada de bienvenida, la visita, su grupo, un curso, servir. | mod (pasos: llamada, visita, consolidación, curso); eq → «Objetivo de conexión Servir» |
| Kingdom propone el siguiente paso. | mod («Kingdom propone el siguiente paso»); mem → «Mi seguimiento» |
| Y el paso se cumple con hechos: una asistencia, un curso terminado, un turno servido. | mem → «Principios» 2; ev → «Membresía ↔ Eventos»; ac → «Cerrar y graduar»; eq → «Objetivo de conexión Servir» |
| En el camino, cada persona suma sus logros: sus hitos y sus niveles. | mem → «Logros» (hitos y logros de niveles) |

Pantalla: titular arriba a la izquierda; seis pasos en fila unidos por una línea que se dibuja; el marcador `person_pin_circle` sobre el
paso actual; la línea dorada avanza con cada paso cumplido. «Siguiente paso» late sobre «Llamada». Tres hechos (Asistencia, Curso
terminado, Turno servido) caen en su paso y lo cumplen. Frase final: la ruta sube y tres logros (Bautismo, Nivel 1, Nivel 2) llegan a una
fila abajo, uno por pulso.

### 7 · `tableros` (113,5–134 s)
| Voz | Fuente |
|---|---|
| Y todo eso lo ves en los tableros. | mem → «Tableros» |
| Personas activas, nuevas, en ruta y conectadas, con su cambio en el período. | mem → «Tableros» → «Resumen» |
| De toda la iglesia, o de cada red. | mem → «Tableros» (filtro de red) |
| Y si necesitas algo puntual, armas el reporte a tu medida, en PDF o en Excel. | mem → «Buscar y ver personas» («Armar el reporte»), «Semáforo de actividad» (columnas) |
| Llévalo a tu reunión de liderazgo, y decide con datos. | ev (mod → «Reportes»: «para tu reunión de liderazgo») |

Pantalla: cuatro tarjetas con contadores que suben en su palabra (sonido `subida`) y su cambio; la línea del crecimiento. Filtros «Toda la
iglesia» / «Red Jóvenes»: en «red» los contadores bajan y la línea cambia. Después, «Tu reporte» con sus columnas (Nombre, Red, Actividad,
Última actividad) una por pulso, renglones y PDF / Excel. En «datos», la tarjeta late dos veces. Datos de ejemplo todo el tiempo.

### 8 · Capítulo 2 «Eventos: cada reunión *cuenta*» (134–138 s) — `event_available`

### 9 · `reportar` (138–160,5 s)
| Voz | Fuente |
|---|---|
| Ahora, las reuniones. / Cultos, casas de paz, células: cada iglesia define las suyas. | ev → «Principios» (categoría = comportamiento) |
| Al terminar, el líder la reporta desde su celular, en pasos guiados. | ev → «Reportar» (pasos con barra de avance) |
| Marca a los de siempre en un toque, agrega a la persona nueva y cuenta a los visitantes. | ev → «Reportar» (habituales, «+ Persona nueva», visitantes) |
| ¿No hay señal? Se guarda, y se envía solo cuando vuelve la conexión. | ev → «Reportar» (sin señal, E4) |
| Ninguna reunión se queda en una libreta. | — (cierre de la idea) |

Pantalla: cuatro categorías (la cuarta, «Las tuyas», en dorado). Pasos Asistencia → Reporte → Listo; 24 casillas que se marcan en una ola
en «siempre»; la persona nueva (dorada, `person_add`); «+3 visitantes» en pasos. Sin señal: `wifi_off`, todo se recoge en una cápsula «1
por enviar» que, en «envía», pasa a «Enviado» (sonido `confirmacion`). Final centrado con tres íconos en pulsos.

### 10 · `medir` (160,5–186 s)
| Voz | Fuente |
|---|---|
| Para ti, cada evento tiene su semáforo: al día, por reportar o retrasado. | ev → «Alertas, tendencia, metas y niveles» (semáforo) |
| Puede tener su meta, y Kingdom te muestra su tendencia: si crece, o si necesita apoyo. | ev → ídem (meta, tendencia); mod (Eventos → «Metas y semáforo») |
| En el tablero ves la asistencia, las personas por reunión y los nuevos del período. | ev → «Tablero y mapa» → «Resumen» |
| Y en el mapa, dónde viven tus personas, / y en qué zonas todavía no hay una reunión cerca. | ev → «Tablero y mapa» → capas «Dónde viven», «Zonas sin evento»; mod (Eventos → «El mapa de tu ciudad») |
| Quizás ahí va tu próxima casa de paz. | — (idea, sin prometer) |

Pantalla: tres eventos con su estado; la meta punteada y dos tendencias dibujadas (la que crece logra la meta: ★; la que baja: «Necesita
apoyo»); tres cifras del tablero. Mapa de densidad (celdas de ≈1 km en azul de marca, ocho zonas) con las reuniones encima; la zona sin
reunión se enmarca y un pin late; en «casa», aparece la nueva casa de paz dorada. Datos de ejemplo desde la frase 2.

### 11 · Capítulo 3 «Academia: líderes *formados*» (186–190 s) — `school`

### 12 · `clases` (190–212 s)
| Voz | Fuente |
|---|---|
| Tu visión necesita líderes formados. | mod (Academia: «Forma a los líderes que tu visión necesita») |
| Con Academia, armas cada curso una vez, y lo repites con cada grupo. | ac → «Principios» (se define una vez y se repite) |
| En clase, el profesor muestra un código de cuatro números, / y cada alumno marca su asistencia desde el celular. Sin listas de papel. | ac → «Tomar asistencia»; mod (Academia, puntos) |
| La sábana de notas te dice quién cumple, y quién va en riesgo, / a tiempo para acompañarlo. | mod (Academia → «Notas con semáforo»); ac → «Seguimiento del profesor…» |

Pantalla: la escuela (nodo dorado) con su arco de líderes que se doran en «formados»; «El curso» y tres grupos en cascada. El código «4 8 2
7» dígito por dígito (sonido `toque`); 12 alumnos que marcan en pulsos, «9 de 12 marcaron su asistencia» (Datos de ejemplo). La sábana
(6 × 7) columna por columna; en «riesgo» se enmarca la fila 3; en «acompañarlo» llega la mano (`handshake`).

### 13 · `graduar` (212–234 s)
| Voz | Fuente |
|---|---|
| Al cerrar el grupo, el profesor propone a quienes cumplieron, y quien coordina aprueba la graduación. | ac → «Cerrar y graduar (el coordinador aprueba, decisión 112)» |
| Cada graduado recibe su certificado, con la firma del pastor y un código que cualquiera puede verificar. | ac → ídem («El certificado»); mod (Academia → «Graduación y certificado») |
| Y su ruta de crecimiento avanza sola. | ac → ídem (al aprobar se cumplen los pasos de la ruta); mod («Conectado con la ruta») |
| En el tablero ves los grupos en curso, los alumnos en riesgo y los graduados de cada período. | ac → «Seguimiento del profesor, reportes y tablero» |

Pantalla: ocho alumnos, seis pasan a verde; flecha a «Coordina», que aprueba (visto dorado). El certificado (ceja «Certificado», «Escuela
de líderes»), el sello, la firma que se dibuja (sonido `confirmacion` en «certificado») y «Código verificable» con el QR. La ruta pequeña:
«Curso» se cumple. El tablero: Grupos en curso, En riesgo, Graduados y graduados por mes (Datos de ejemplo).

### 14 · Capítulo 4 «Equipos: cada puesto *cubierto*» (234–238 s) — `volunteer_activism`

### 15 · `turnos` (238–264,5 s)
| Voz | Fuente |
|---|---|
| Detrás de cada reunión hay personas que sirven. | eq → «Objetivo» |
| Alabanza, seguridad, medios, audiovisual: cada equipo con sus líderes y sus integrantes. | eq → «Objetivo» (ejemplos de equipos), «Crear un equipo y nombrar sus líderes» |
| El líder arma el turno, y Kingdom le sugiere a quién poner: quien sabe hacerlo, y ha servido menos. | mod (Equipos → «Turnos con confirmación»); eq → «Programar un turno» |
| Cada persona acepta su turno desde el celular, con sus instrucciones: a qué hora llegar y cómo vestirse. | eq → «La persona recibe la asignación y responde», «Instrucciones» |
| Y antes de la reunión, ves qué puestos están cubiertos, y cuáles faltan. | eq → «Reportes» → «Cobertura de la iglesia»; mod (Equipos) |

Pantalla: la iglesia con su anillo de servidores; cuatro equipos (con su líder dorado y sus integrantes). El turno de Alabanza: funciones
(Voz, Teclado, Sonido) y puestos; el vacío late en rojo; «Sugerida» (`lightbulb`) entra al puesto. Los puestos aceptan uno por pulso y llegan
las instrucciones (llegada, vestimenta). Cobertura por equipo: 6 de 6, 7 de 8, 4 de 4, 3 de 5; los vacantes laten (Datos de ejemplo).

### 16 · `servir` (264,5–284 s)
| Voz | Fuente |
|---|---|
| Al terminar, el líder cierra el turno y marca quién sirvió. | eq → «Cerrar el turno» |
| Así queda un historial real de cada servidor, y la carga se reparte parejo. | mod (Equipos → «Servir cuenta»); eq → «Objetivo» |
| Y servir cuenta: cumple el paso Servir de su ruta de crecimiento. | eq → «Objetivo de conexión Servir»; mod («Servir cuenta») |
| Los reportes te muestran la cobertura de cada reunión, y la carga de cada persona. | eq → «Reportes» (cobertura por reunión, carga por persona) |

Pantalla: cinco filas con «Sirvió» / «No llegó», una por pulso. El historial de 12 semanas que se llena; las barras de carga que se
emparejan en «parejo». La ruta pequeña: en «cuenta», «Servir» se cumple («Paso cumplido»). Reportes: cobertura por reunión (columnas con
%) y carga por persona en 90 días (Datos de ejemplo).

### 17 · Capítulo 5 «Lo que *gana* tu iglesia» (284–288 s) — `insights`, **claro** (el único del video)

### 18 · `gana` (288–311,5 s)
| Voz | Fuente |
|---|---|
| Entonces, pastor, ¿qué gana tu iglesia? | — |
| Decisiones con datos, no con suposiciones. | Resumen de los tableros (mem, ev, ac, eq) |
| Nadie se pierde: cada persona tiene quién la cuide, y ves a tiempo a quien se aleja. | mem → «Objetivo», «Semáforo de actividad»; mod (Membresía: «Que ninguna persona se pierda») |
| Líderes que rinden cuentas, sin papeles, y sin perseguir a nadie por su reporte. | ev → «Reportar» (recordatorios y avisos de reporte vencido); ac → «Tomar asistencia» |
| Y todo conectado: la asistencia, los cursos y el servicio mueven la misma ruta de cada persona. | ev → «Membresía ↔ Eventos»; ac → «Ruta de crecimiento y logros»; eq → «Objetivo de conexión Servir» |

Pantalla: la pregunta en grande; cada frase llega grande (1,75×) al tercio de abajo, centrada, y al empezar la siguiente vuelve a su lugar
en la lista de la izquierda, con su ícono (`query_stats`, `diversity_1`, `task_alt`) y su bajada. Al final, la ruta de cada persona (nodo
dorado `route`) con Asistencia, Cursos y Servicio, cada uno en su palabra; la luz viaja por las líneas en tres pulsos.

### 19 · `acompana` (311,5–337 s)
| Voz | Fuente |
|---|---|
| Y no lo haces solo. | frame-recurso.md → llamado «acompanamiento»; pedido del dueño |
| Al empezar, Kingdom te da una ruta de arranque, paso a paso, para acomodarlo a tu iglesia. | ar → «Objetivo», «La ruta de arranque» (etapas Tu iglesia, Tu gente, Tu equipo y por módulo; cuestionario) |
| En la Ayuda está la Escuela Kingdom, con lecciones y videos cortos para cada líder. | ar → «La Escuela Kingdom» (rutas por rol, lecciones con video) |
| Y nuestro equipo ve cómo avanza tu iglesia, y te acompaña a mejorar tus procesos. | ar → «Objetivo» («El equipo de Kingdom ve el avance de cada iglesia y sabe cuándo hace falta acompañarla»), «Plataforma»; pedido del dueño |
| Porque la meta no es usar una app. Es cuidar mejor a cada persona, y poder verlo. | — (remate) |

Pantalla: la iglesia y, en «solo», el equipo de Kingdom (`support_agent`) a su lado. La ruta de arranque en vertical (Empieza, Tu iglesia,
Tu gente, Tu equipo, Tus módulos) con el avance dorado. La Escuela Kingdom (`menu_book`) y tres rutas de aprendizaje (administrador, líder de
red, servidor). El equipo de Kingdom unido a la iglesia: el anillo de avance se llena y aparecen Ve el avance, Ajusta, Mejora. Remate
centrado; 24 personas llegan de todas partes a formar el anillo alrededor del punto dorado, que se dora en «verlo».

### 20 · Cierre del kit (337–346 s)
«Sigue con: Eventos de ciudad, sin perder a nadie», llamado «Te acompañamos a mejorar los procesos de tu iglesia» y WhatsApp +57 300 471 2642.
El último golpe de la música cae en la firma.

## Música

«Product Launch» en bucle (plan por defecto de `kit.json`): entrada 0,05–50,05, bucle 18,05–66,05 cinco veces y media, salida 66,05–86,05
con el último golpe en la firma del cierre. Las tarjetas de capítulo caen en compases y la música sube debajo; la voz va 18,3 dB por encima.
