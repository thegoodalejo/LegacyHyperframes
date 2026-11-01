# SPEC — La experiencia del nuevo

Storyboard escena por escena. Sistema visual: `frame.md` (= `_identidad/frame-recurso.md`, kit v1.2), sin la app. Todas las escenas usan
dos columnas (texto cinético a la izquierda en x 192–1052, diagrama a la derecha en x 1080–1728), salvo `resumen`, que va a lo ancho.
Los tiempos salen de `KRecurso.tiempos()`: entradas en pulsos, cambios de etapa en el pulso de la palabra que los nombra, salida en los
últimos 0,6 s.

**Números del sistema (para todas las escenas):**
- Texto: `.k-recurso-frase` 72 px; rótulos cortos (≤ 42 caracteres) en lugar del párrafo cuando la frase es larga; el VTT trae la frase
  completa. Cada palabra entra a −0,08 s de oírse (y +28 px, desenfoque 6 px, `power3.out` 0,4 s) y el bloque sale a −0,32 s de la frase
  siguiente (`power2.in` 0,3 s).
- Ceja de la escena (`.k-recurso-ceja`, 28 px) en x 192, y 132: dónde estamos («Mi iglesia · Comunidades»).
- Chips: 64 px de alto, Inter 600 30 px, ícono de 34 px; el dorado es lo que la persona toca o recibe.
- Nodos `.k-recurso-nodo` de 84–220 px con su ícono al 46 %; puntos de 18–34 px. **El punto dorado (30–34 px) es la persona nueva** en todo
  el video; **el azul** es quien la acompaña.
- Entradas `back.out(2)` solo en puntos, íconos y chips; «late» = escala 1,1–1,6 → 1 en 0,45 s; halo = anillo dorado de 120 px que se
  abre a ×1,9 en 0,9 s.
- Semáforo: verde `#26A69A` (paleta), amarillo = dorado `#E8B95A` (paleta), rojo `#E57373` (no está en la paleta: solo como color de
  punto o barra, nunca de texto), gris = punto tenue o anillo.
- Prohibidos por nombre: pantallas o teléfonos dibujados, logos de terceros (Google y WhatsApp se nombran, no se dibujan), partículas,
  giros (salvo el leve vaivén de la campana), cifras sin «Datos de ejemplo».

## Fuentes (rutas en el worktree `F:\Proyectos\KingdomApp-recursos`)

| Clave | Archivo |
|---|---|
| [P] | `docs/modulos/portal.md` (Objetivo, Glosario, «Cómo se usa → Mi iglesia») |
| [M] | `docs/modulos/membresia.md` (Mi seguimiento, Tablero del coordinador, Logros, Semáforo de actividad) |
| [S] | `sitio/src/data/modulos.ts` («Mi iglesia» y «Membresía») |
| [A:x] | `frontend-v2/src/ayuda/es/mi-iglesia/x.md` |
| [Mm:x] | `frontend-v2/src/ayuda/es/membresia/x.md` |
| [Ac] | `frontend-v2/src/ayuda/es/academia/marcar-mi-asistencia.md` |
| [N] | `frontend-v2/src/ayuda/es/empieza/notificaciones-en-mi-celular.md` |
| [E] | `docs/modulos/equipos.md` («Quiero servir» desde Mi iglesia) |

## Escenas

### intro (kit, 6 s)
Título «La experiencia del *nuevo*», ceja «Recursos».

### gancho — apertura (sin ceja)
- Voz: domingo, primera vez; pasa al altar y vuelve a su casa; ¿y el lunes?; que no se quede sola; lo que vive alguien nuevo con
  Kingdom; cómo la iglesia la acompaña desde el primer minuto. Es la situación del pastor, sin función nombrada ([P] Objetivo: «desde ese
  minuto quede conectado»).
- Diagrama: la puerta, el altar y su casa (nodos en y 290) unidos por una ruta que se dibuja mientras ella (punto dorado) la recorre; debajo la
  semana (D L M M J V S) con el domingo en dorado. En «lunes» el lunes se enciende ×1,5. En «sola» todo se va y 18 puntos que habían llegado
  se alejan. En «nuevo» vuelven y forman un anillo de r 210 con seis lazos. En «acompaña» llega el punto azul unido por un lazo dorado.

### cap-1 (kit, 4 s): «La *bienvenida*» · «Del QR a sus primeros pasos» · `qr_code_2`

### qr — «La bienvenida · El QR»
| Voz | Fuente |
|---|---|
| El QR de bienvenida; se imprime o se proyecta en el altar | [P] «Entrar por el QR de bienvenida» 1 |
| Lo escanea con su celular y ve el logo de su iglesia | [A:la-bienvenida] «Entrar por el QR» 1 |
| Entra con Google | [P] 3; [A:la-bienvenida] 2 |
| Nombre, teléfono y género; «Unirme» | [A:la-bienvenida] 4–5 |
| Ya es miembro, sin esperar aprobación («en un minuto», pedido del dueño) | [P] 4 (decisión 156); [S] «queda conectado como miembro al instante» |
| Si ya tenía ficha con ese correo, se reconoce | [P] «si ya tenía ficha con ese correo, se reconoce» |

Diagrama: un QR abstracto de 13 × 13 celdas (esquinas en dorado) entra en onda desde el centro; chips «Impreso» y «En el altar»; un barrido
dorado lo cruza dos veces y se recoge en el nodo de su iglesia. Después, en columna: «Continuar con Google», «Nombre», «Teléfono», «Género» y
«Unirme» (dorado, se presiona). Todo se recoge en ella; el anillo del minuto se cierra en 1,2 s con «1 min» y quedan «Miembro» y «Sin esperar
aprobación». Cierra con «El mismo correo» → tarjeta «Su ficha en la iglesia · Reconocida».

### pasos — «La bienvenida · Primeros pasos»
| Voz | Fuente |
|---|---|
| Los primeros pasos que la iglesia preparó | [A:la-bienvenida] primer párrafo; [P] «La bienvenida» |
| No es un formulario largo: pantallas cortas | [P] Principios («Nunca es un formulario largo… pantallas cortas con “Siguiente”») |
| Serie para orar, un libro, una playlist | [P] tipos de paso (Recurso, Serie educativa «Cómo orar») |
| Comunidad, contar de sí, activar notificaciones | [P] tipos (Comunidad, Cuéntanos de ti, Activa las notificaciones) |
| La pregunta «¿Quieres que te acompañemos con un plan de lectura?»; con un sí empieza el plan con recordatorios | [P] «Pregunta final» y ejemplo «libro»; [A:mis-objetivos] |
| Al terminar, la app lo celebra | [A:la-bienvenida] («Al terminar el último paso, la app lo celebra») |

Diagrama: un camino en serpentina (dos filas de tres nodos: Cómo orar, Un libro, Una playlist, Comunidad, Cuéntanos de ti, Avisos) que se
dibuja en 2,2 s; ella lo recorre por la curva y cada nodo se vuelve dorado en la palabra que lo nombra. «Siguiente» late tres veces en
pulsos. La pregunta entra en una tarjeta con «Sí, quiero» y «Ahora no» (los textos de la app); «Sí, quiero» se presiona y la tarjeta se
vuelve el nodo del plan con «Con recordatorios». Al final el camino se vuelve dorado, los seis
nodos laten en fila y aparece `celebration`.

### cap-2 (kit, 4 s): «Su iglesia, *en el bolsillo*» · «Lo que encuentra en Mi iglesia» · `church` ([S] «Tu iglesia, en el bolsillo de cada miembro»)

### inicio — «Mi iglesia · Inicio»
| Voz | Fuente |
|---|---|
| Mi iglesia en su celular, con el logo y los colores de tu iglesia | [S] bajada de «Mi iglesia» |
| Lo destacado y las novedades, como una red social | [A:inicio-de-mi-iglesia] 3 y 6 |
| Fotos, videos, la tarjeta de un evento o un curso; reacciona «Amén», «Me edifica» | [P] Glosario (Publicación, Reacción) |
| Los próximos eventos en el calendario del mes | [A:inicio-de-mi-iglesia] 4 |
| Comunicados: ahora, programados o repetidos | [S] bloque «Comunicados» |
| Lo último que vio, sin señal | [A:inicio-de-mi-iglesia] «Sin señal» |

Diagrama: el nodo «Mi iglesia» (180 px) con tres colores de marca y «Tu logo y tus colores»; sube y se abre un feed de tarjetas abstractas
(ícono + palabra: Destacado, Novedades, Un video, Un evento · Inscribirme, Un curso · Unirme…) que **sube sin parar** 560 px; las reacciones
«Amén» y «Me edifica» saltan en su palabra. Calendario de 30 días que entra en diagonal; ocho días con evento laten en pulsos. Nodo
`campaign` con tres rayos: «Ahora», «Programado», «Repetido». Cierra con «Lo último que vio» y «Sin señal».

### comunidades — «Mi iglesia · Comunidades»
| Voz | Fuente |
|---|---|
| Jóvenes, matrimonios, mujeres, deportes | [P] Glosario «Comunidad»; [S] |
| Las sugeridas salen primero | [A:comunidades] «Explorar» 2 («Para ti») |
| Se une con un toque o la solicita si aprueba | [A:comunidades] 3–4 |
| Adentro, lo que comparten sus líderes y sus cursos | [A:comunidades] «Dentro de una comunidad» |
| «Conectar con un líder»; un líder lo toma; «… te acompañará» | [P] «Conectar con un líder»; [A:comunidades] («Ana» es el ejemplo de la ayuda en [A:conectarme-a-un-grupo]) |

Diagrama: constelación de cuatro comunidades alrededor de ella con rayos; «Para ti» sobre Jóvenes, que se vuelve dorada; «Unirme» se
presiona y ella entra; «Solicitar» en otra. La comunidad crece al centro ×1,5 con dos líderes, «Publicaciones» y «Cursos». «Conectar con un
líder» (dorado). «Un mensaje corto» sube al líder; el líder se vuelve azul y aparece «Ana *te acompañará*». Final: ella y la líder (azul) se
juntan con un lazo dorado y dos halos.

### objetivos — «Mi iglesia · Objetivos»
| Voz | Fuente |
|---|---|
| Planes que la animan a seguir; un libro de 4 en 4 páginas, un devocional cada mañana, una canción por semana | [S] bloque «Objetivos en curso»; [P] Objetivo |
| Anillo de avance y recordatorio | [A:mis-objetivos] |
| «Lo hice» y «Aplazar» corre todo el plan sin perder pasos | [A:mis-objetivos] «Marcar tu paso» |
| Pasos para conectarse, como una casa de paz | [A:conectarme-a-un-grupo] |
| «Conectarme»: su dirección, los grupos más cercanos, sin la dirección de nadie | [A:conectarme-a-un-grupo] paso 2–3; [P] |
| «Quiero asistir»; quienes lideran le escriben | [A:conectarme-a-un-grupo] 4–5 |

Diagrama: tres anillos (r 84) con su ícono y su ritmo; se llenan a 40, 70 y 25 % en «anillo»; «Recordatorio en su celular». Un solo anillo
grande (r 140) con ocho pasos en fila: «Lo hice» enciende el cuarto; «Aplazar» **corre los cuatro que faltan un lugar a la derecha**. Después,
el nodo de la casa de paz, «Conectarme», un pin, tres franjas de distancia que se dibujan y tres grupos con «A menos de 2 km», «De 2 a 5 km»,
«De 5 a 10 km» (las franjas de la app); «Sin la dirección de nadie». «Quiero asistir» y dos líderes azules cuyo mensaje viaja al pin.

### boleta — «Mi iglesia · Eventos»
| Voz | Fuente |
|---|---|
| Se inscribe desde su celular a un congreso o retiro | [A:inscribirme-a-un-evento] |
| Y a su familia (esposo, hijos) | [A:inscribirme-a-un-evento] 3; [S] |
| Boleta: QR personal y código de 6 caracteres | [P] «Un evento, la inscripción y Mis boletas» 4 |
| Sin señal; en la entrada la escanean | [A:inscribirme-a-un-evento] «Mis boletas» |

Diagrama: nodo del evento, «Inscribirme» se presiona; cuatro puntos de su familia se suman. La boleta (forma de ticket con muescas, 400 × 560)
sube; el QR entra fila a fila y el código «K7M4QX» (de ejemplo) cae letra a letra. «Sin señal, igual se ve»; un barrido la escanea y queda
«Ya entraste hoy» (texto de la app).

### cursos — «Mi iglesia · Cursos»
| Voz | Fuente |
|---|---|
| En «Cursos», los que toma y los que puede tomar | [A:mis-cursos] (En curso, Explorar, Terminados) |
| Se une con un toque; cuántas clases lleva y la próxima | [A:mis-cursos] «Lo que ves» y «Unirme a un curso» |
| Marca su asistencia con un código | [Ac] (código de 4 números; «¡Listo! Quedó tu asistencia») |
| Su certificado en «Terminados» | [A:mis-cursos] |

Diagrama: las tres pestañas como chips; «Unirme»; ocho clases en fila, cinco doradas y la próxima que late tres veces; cuatro rollos de
números que giran hasta 4-8-2-7 y «¡Listo! Quedó tu asistencia»; el certificado (`workspace_premium`, 220 px) vuela a «Terminados».

### servir — «Mi iglesia · Quiero servir»
| Voz | Fuente |
|---|---|
| «Quiero servir»: los equipos que reciben gente, cada uno con su descripción | [A:quiero-servir-en-un-equipo] 2 |
| «Quiero servir aquí», elige lo que le gustaría hacer, mensaje a los líderes | [A:quiero-servir-en-un-equipo] 2–4; [E] |
| «¡Ya eres parte de…!» | [A:quiero-servir-en-un-equipo] «Qué pasa después» |

Diagrama: seis equipos (los nombres son de ejemplo); tres «reciben gente» y se vuelven dorados, los demás se apagan. Bienvenida sube; «Quiero
servir aquí» se presiona; dos funciones de ejemplo se marcan; «Mensaje para los líderes». Ella sube al equipo, que se llena de dorado:
«¡Ya eres parte!» e «Integrante». Final: la ruta dorada desde «Un domingo, el altar» hasta su equipo.

### historia — «Mi iglesia · Su historia»
| Voz | Fuente |
|---|---|
| «Contar mi testimonio»: antes, durante, después; fotos o video; la iglesia lo revisa | [A:contar-mi-testimonio] |
| «Mis documentos»: firma con el dedo, como la autorización de sus datos | [A:mis-documentos] |
| «Mi ficha»: corrige su celular, su dirección, su fecha de nacimiento | [A:mi-ficha] |
| Así te pueden acompañar mejor | [A:mi-ficha] primer párrafo |

Diagrama: «Contar mi testimonio»; tres etapas en línea (Antes, Durante, Después) que se dibuja por tramos; chips de evidencias; «Por
revisar». Documento abstracto con renglones y una firma dorada que se dibuja en 1,3 s; «Firma guardada». Mi ficha con tres campos que se
encienden en su palabra; «¡Guardado!». La ficha se encoge y se une a «Quien la acompaña» (azul).

### avisos — «Mi iglesia · Avisos»
| Voz | Fuente |
|---|---|
| Los avisos: recordatorio del plan, boleta, clase, el líder | [P] Principios («Las notificaciones son el canal con el miembro»); [A:mis-objetivos], [A:inscribirme-a-un-evento], [Ac], [A:comunidades] |
| Todo queda en la campana | [N] («Los avisos también quedan en la campana») |
| Elige qué recibir; horario silencioso | [N] «Elegir qué recibir» |

Diagrama: la campana (150 px) con un vaivén leve en «avisos»; cuatro avisos entran desde la derecha y se apilan, la campana late con cada uno;
suben y entran en ella, que queda con su punto. Tres preferencias (dos se encienden, «Resúmenes» se apaga) y un reloj de 24 h con el arco de
22:00 a 6:00 en dorado.

### cap-3 (kit, 4 s, **fondo claro**: el giro del relato): «Del otro lado, *tu iglesia*» · «Nadie llega y se va sin que alguien lo note» · `visibility`

### ruta — «Membresía · Ruta de crecimiento»
| Voz | Fuente |
|---|---|
| Su ficha se crea con la forma de llegar del QR («Recibió a Jesús en el altar») y entra a la ruta de crecimiento con su acompañamiento | [P] «Entrar por el QR» («Al entrar…») |
| Reparto parejo entre quienes pueden acompañar | [M] «Tablero del coordinador» («Repartir» de forma pareja); [S] |
| «Mi seguimiento»: su paso y cuándo vence | [M] «Mi seguimiento»; [Mm:mi-seguimiento] |
| La llama, marca cumplido, Kingdom propone el siguiente paso | [Mm:mi-seguimiento] 2–7 |
| Llamada, llegar a la iglesia, casa de paz, curso; un paso puede dar un logro (bautizo) | [M] Glosario (Paso, Logro); [M] «Ajustes de la ruta» («logro que otorga»); [S] |

Diagrama: ella llega y la iglesia recibe el aviso (lazo y halo). Tarjeta de su ficha con «Recibió a Jesús en el altar». Seis nuevos bajan,
dos a cada uno de tres acompañantes (azules), con su cupo que se llena parejo; «Repartir de forma pareja». Tres filas de Mi seguimiento con
el semáforo del paso (A tiempo, Por vencer, Vencido). «La llama», «Marcar cumplido», «Ahora va en: Llega a la iglesia». La ruta vertical
de cuatro pasos que ella baja, y el logro «su bautizo» con su halo.

### semaforo — «Membresía · Semáforo de actividad»
| Voz | Fuente |
|---|---|
| Verde, amarillo, rojo o «Sin actividad» por los días desde lo último | [M] «Semáforo de actividad»; [Mm:semaforo-de-actividad] |
| Cuenta la reunión, la clase, el paso cumplido, usar la app | [M] tabla de fuentes; [Mm:semaforo-de-actividad] «Qué cuenta» |
| La persona no lo ve; es para quien cuida | [Mm:semaforo-de-actividad] («La persona no lo ve en Mi iglesia: es una herramienta para quien cuida») |

Diagrama: cuatro luces apiladas que bajan al eje de los días (0 a 10, 11 a 30, 31 a 50, más de 50: los de fábrica). Ella se corre a la
derecha con los días y se vuelve amarilla; cada actividad (Una reunión, Una clase, Un paso, Usar la app) la regresa a verde con un halo.
Cuando vuelve al amarillo: dos halos, «Lo ves a tiempo», «Alguien la llama», llega el punto azul y ella vuelve a verde. «La persona no lo ve»
y «Para quien cuida».

### cap-4 (kit, 4 s): «Lo que *ves* como pastor» · «Cada persona, y cómo avanza» · `insights`

### tablero — «Portal y Membresía · Tableros» (con «Datos de ejemplo» todo el tiempo que hay cifras)
| Voz | Fuente |
|---|---|
| Tablero del Portal: cuántas terminan la bienvenida, cómo avanzan los objetivos, a cuántas llegan los comunicados | [S] bloque «Un tablero para ti» |
| En Membresía, el semáforo de toda la iglesia, red por red | [M] «Semáforo de actividad» (Tableros → Resumen, con el filtro de red) |

Diagrama: cuatro íconos se arman en rejilla; barras «Empezaron su bienvenida · 48» y «La terminaron» con el 36 que sube; tres anillos de
objetivos con su porcentaje (62, 40, 85 %); 312 personas que recibieron el comunicado con ondas; tres redes de ejemplo con su barra apilada en
los cuatro colores. Todo de ejemplo.

### resumen — a lo ancho
Voz: la ruta entera y «alguien de tu iglesia está con ella» (resume las escenas anteriores). Diagrama: siete paradas de x 300 a 1620 (El QR,
Bienvenida, Comunidad, Sus planes, Eventos, Cursos, Servir); ella las recorre en la palabra que las nombra y cada una se vuelve dorada; el
punto azul la acompaña de vuelta por toda la ruta; se unen al final; 22 personas aparecen en su propio punto de la ruta («cada una»).

### llamado — «Te acompañamos»
Voz: el llamado del cierre `acompanamiento` (frame: «Te acompañamos a mejorar los procesos de tu iglesia») y WhatsApp (contacto del sitio,
`sitio.ts`). Diagrama: el nodo del acompañamiento se une a tu iglesia; «Tu bienvenida», «Tu QR», «WhatsApp».

### cierre (kit, 6 s, sin «Sigue con»)
