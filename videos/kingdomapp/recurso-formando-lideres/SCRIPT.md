# SCRIPT — narración bloqueada

<!-- GENERADO desde guion.mjs por _herramientas/recurso.mjs: se edita guion.mjs. -->

Slug: `formando-lideres` · Llamado: acompanamiento · Contacto: whatsapp

## Español — «Formando *líderes* con Kingdom»

> Para el líder de academia, clases de la visión o escuela bíblica: cómo ordenar los cursos, cargarlos desde Excel, dictar en línea, llevar asistencia, notas y evaluaciones, aplazar una clase y graduar con certificado, para formar líderes que formen a otros.

### 1. gancho

- Una persona llegó a tu iglesia, la llamaron, la acompañaron y se *quedó*.
- Afirmarla fue el comienzo. Ahora tiene que *crecer*.
- Conocer la Palabra, ser edificada y, un día, *formar* a otros.
- Si diriges la *academia*, las clases de la visión o la escuela bíblica, este video es para ti.
- Vas a ver cómo usar Kingdom para que cada alumno crezca y tu iglesia tenga más *líderes*.

_Fuente:_ Pedido del dueño (BRIEF): que el afirmado crezca, sea edificado y forme a otros; continúa «Afirmando la cosecha». SPEC → «gancho».



### 2. cap-1 — capítulo 1 «Formados para *formar*»

_(sin voz, 4 s)_

### 3. formar

- Pablo le encargó a Timoteo que enseñara lo que había aprendido a personas fieles, capaces de enseñar a *otros*.
- En una sola frase hay cuatro *generaciones*: Pablo, Timoteo, los fieles y los otros.
- Ese es el corazón de tu academia: no llenar salones, sino formar personas que *formen* a otras.
- El miembro se vuelve *discípulo*, y el discípulo se vuelve líder.
- Una iglesia crece hasta donde crecen sus *líderes*: cada líder nuevo puede abrir un grupo nuevo.
- Kingdom te ayuda a que ese camino sea *claro*, medible y sin papeles.

_Fuente:_ 2 Timoteo 2:2, en palabras propias (en pantalla solo la cita); los niveles Miembro, Discípulo y Líder del programa «Clases de la visión» (`backend/cron/jobs/_demo_academia.php:64`) y del logro «Nivel de la visión» (`backend/_datos/personas_catalogos.php:301-309`). SPEC → «formar».



### 4. cap-2 — capítulo 2 «Tu academia en *orden*»

_(sin voz, 4 s)_

### 5. orden

- Todo empieza ordenando tu academia en *categorías*: Visión, Biblia, Servicio. Las creas tú, con su ícono y su color.
- Dentro de una categoría puedes armar un *programa*: una serie de cursos por niveles.
- Por ejemplo, Clases de la visión: Miembros, *Discípulos* y Líderes.
- Cada nivel pide haber aprobado el *anterior*, y Kingdom lo revisa al inscribir.
- El curso se define *una vez*, y abres los grupos que necesites: el martes en la noche, el domingo en la tarde.
- Al inscribir, Kingdom te muestra quiénes *pueden* tomarlo.
- Y si alguien falta, puede *recuperar* la clase en otro grupo del mismo curso.

_Fuente:_ Ayuda `academia/ajustes`, `abrir-un-grupo`, `inscribir` y `marcar-mi-asistencia`; es.json («Nueva categoría», «Nuevo programa», «Pueden tomarlo», `ac.ac2_cu_recuperar`); el prerrequisito en `academia_cursos.php:245-265` y `academia_inscripciones.php:32-81`. SPEC → «orden».



### 6. cap-3 — capítulo 3 «Un curso listo en *minutos*»

_(sin voz, 4 s)_

### 7. curso

- Crear un curso es un asistente de cinco *pasos*: datos, materias y clases, actividades y pesos, criterios, y logro.
- Eliges su modalidad: *presencial*, híbrido, en línea, o exprés, de un solo día.
- ¿Ya tienes el pensum en Excel? Descarga la *plantilla*, llénala y súbela.
- Kingdom revisa cada fila, te marca los errores y arma las materias, las clases y las actividades con sus *pesos*.
- Las preguntas de las evaluaciones también se cargan de una vez: desde Excel, o pegando el *texto* que ya tienes en Word o en WhatsApp.
- Un asterisco marca la respuesta correcta; revisas y las guardas *todas* juntas.
- Y el material, presentaciones, lecturas o videos, lo subes de *varios* archivos a la vez, por materia o por clase.

_Fuente:_ Ayuda `academia/crear-un-curso` y `material-y-banco`; `pensum-dialog.component.ts` y es.json:369-427 (el pensum de Excel); «Cargar desde Excel o texto», «Pegar texto» y «Guardar {n} preguntas» (`academia_preguntas.php:463-542`, todo o nada); el material por materia o clase. SPEC → «curso».



### 8. cap-4 — capítulo 4 «Clases en *línea*»

_(sin voz, 4 s)_

### 9. enlinea

- Un curso *en línea* se toma a su ritmo, sin calendario.
- Arrastras tus videos y cada uno queda como una *lección*, con su nombre y su duración.
- O pegas el enlace de *YouTube* o de Vimeo, y no gastas espacio.
- Puedes pedir un *quiz* para completar la lección, que avancen en orden y que de verdad vean el video.
- El alumno ve su *avance*, y al volver, el video sigue donde iba.
- Si lleva siete días sin avanzar, le llega un aviso: te *esperamos*.
- Y si prefieres clases en vivo, el curso *híbrido* lleva el enlace de tu Zoom o tu Meet, con el botón «Unirse en vivo» quince minutos antes.

_Fuente:_ Ayuda `academia/lecciones-en-linea` y `mis-cursos`; `academia_en_linea.php`; el aviso `academia.sin_avanzar` («Te esperamos en {curso}», `backend/avisos/catalogo.json`); «Unirse en vivo» 15 minutos antes (es.json `ac.ac2_mi_unirse_vivo`, `ac.ac2_mc_vivo_luego`). SPEC → «enlinea».



### 10. cap-5 — capítulo 5 «El profesor, sin *papeles*»

_(sin voz, 4 s)_

### 11. asistencia

- Para el profesor, todo empieza en «*Hoy*»: la clase del día, lo pendiente y lo que vence esta semana.
- Toca «Tomar asistencia» y muestra el *código*: cuatro números que cambian cada minuto.
- A cada alumno le llega un aviso; escribe el código en su celular, y *listo*.
- El profesor ve en vivo cuántos marcaron, y a quien no tiene celular lo marca con un *toque*.
- ¿No hay señal en el salón? «Pasar *lista*» funciona sin señal, y se envía sola cuando vuelve.

_Fuente:_ `asistencia/hoy.component.ts` y `toma.page.ts`; el código por minuto (`academia_asistencia.php:5-19`); el aviso `academia.asistencia`; «{n} de {total} marcaron», «Presente» y «Pasar lista» (es.json 721-767). SPEC → «asistencia».



### 12. calificar

- Las *notas* se ponen en fila: escribes, Enter, y pasas al siguiente.
- Las evaluaciones se abren con un toque, por el tiempo que elijas, y se *califican* solas al cerrar. Las preguntas abiertas las calificas tú.
- Cada alumno recibe su nota y ve cuál era la respuesta *correcta*.
- Los trabajos llegan con una foto o un archivo, y los calificas uno tras otro, con un *comentario*.
- Todo cae en la sábana de notas, con el *semáforo* de cada alumno: cumple, en riesgo o no cumple.
- Y en «Faltaron» ves quién lleva varias clases sin venir, y le *escribes* por WhatsApp con un toque.

_Fuente:_ `notas/notas-grupo.component.ts`, `evaluaciones-grupo.component.ts`, `calificar-abiertas.component.ts` y `entregas/calificar-entregas.page.ts`; el aviso «Ya está tu nota»; «Faltaron», «{n} clases seguidas sin venir» y «Escribir» (es.json 848-861; Academia no manda WhatsApp, abre el del profesor). SPEC → «calificar».



### 13. cap-6 — capítulo 6 «Si la clase se *corre*»

_(sin voz, 4 s)_

### 14. aplazar

- Un festivo, un viaje, un culto *especial*: a veces una clase no se puede dictar ese día.
- En «Fechas», abres el menú de la clase y tocas «Aplazar o *mover*».
- Eliges la nueva fecha, y la opción de correr también las clases *siguientes* ya viene marcada.
- Antes de confirmar, ves cómo *quedan*: las cinco clases siguientes se corren siete días.
- Tocas «Aplazar y avisar»: el calendario se corre *solo*, la fecha de cierre también, y los recordatorios se reprograman.
- Y a cada alumno le llega el aviso: tu clase cambió de *fecha*.

_Fuente:_ `aplazar-dialog.component.ts` y es.json 588-598 («Correr también las clases siguientes los mismos días», «Las {n} clases siguientes se corren {dias} días.», «Aplazar y avisar»); `acClaseAplazar` (`academia_grupos.php:651-691`); el aviso `academia.clase_cambio` («Tu clase cambió de fecha»). SPEC → «aplazar».



### 15. cap-7 — capítulo 7 «Cada alumno ve su *avance*»

_(sin voz, 4 s)_

### 16. alumno

- Del otro lado, el alumno tiene todo en su *celular*, en «Mis cursos».
- Ve a cuántas clases ha venido, cuál es la *próxima* y qué tiene pendiente.
- Cuando el profesor abre la asistencia, le llega el aviso; escribe los cuatro números y queda *marcada*.
- Entrega un trabajo tomando una *foto*, o subiendo un PDF.
- Presenta su evaluación con el *tiempo* a la vista, y si se va la señal, sus respuestas se guardan en el celular.
- Y en «Mis notas» sabe cómo va, y qué le falta para *aprobar*.

_Fuente:_ `mis-cursos.page.ts`, `mis-curso.page.ts`, `entregas/entrega.page.ts` y `notas/mis-notas.component.ts`; es.json 872-873 («Viniste a…», «Próxima…») y 1226 (sin señal); «¡Listo! Quedó tu asistencia». SPEC → «alumno».



### 17. cap-8 — capítulo 8 «Graduados que *forman*»

_(sin voz, 4 s)_

### 18. graduar

- Al terminar, el profesor abre «*Graduar*»: Kingdom arma la lista con los criterios del curso.
- Quien coordina la *aprueba*, y a cada graduado le llega: ya está tu certificado.
- Lleva el logo de tu iglesia, la firma de tu pastor si la subes, y un código *QR* que cualquiera puede verificar.
- Si el curso otorga un *logro*, la persona lo recibe, y tu ruta de crecimiento puede cumplir ese paso sola.

_Fuente:_ La pestaña «Graduar» del grupo, con su sección «Cerrar y graduar» y «Enviar para aprobar» (`graduar/graduar-grupo.component.ts`, `proponer.component.ts`; es.json 1854 y 1871), y `por-aprobar.component.ts`; el aviso `academia.certificado`; `services/academia/certificado-pdf.ts` (logo, firma y QR verificable); `academiaRutaGraduado` (`academia_graduaciones.php:549-555`). SPEC → «graduar».



### 19. multiplicar

- En el *Tablero* ves toda tu academia: quién está en riesgo, quién falta seguido, quién se graduó.
- Pero el fruto no es un certificado: es una persona que ahora puede *enseñar*.
- Quien se graduó de Líderes puede ser el *profesor* del próximo grupo.
- Si ya sirve en tu iglesia, lo nombras en el grupo, y ve *solo* ese grupo: sus alumnos, su asistencia y sus notas.
- Así se cumple lo que Pablo le encargó a Timoteo: fieles que enseñan a *otros*.
- Y una iglesia que forma líderes es una iglesia que se *multiplica*.

_Fuente:_ El Tablero de Academia (es.json 2138-2209); el profesor del grupo con alcance «suyo» (`backend/academia/_academia.php:100-109`); 2 Timoteo 2:2. SPEC → «multiplicar».



### 20. resumen

- Formar líderes con Kingdom es *simple*.
- Ordena tu academia en categorías, programas y grupos. Carga tus cursos desde Excel.
- Deja que la asistencia, las notas y los avisos trabajen por ti.
- Acompaña a cada alumno hasta graduarse, y ponlo a enseñar a otros.
- Porque cada persona que formas hoy es un *líder* que formará mañana.

_Fuente:_ Resumen de las escenas anteriores, con la forma de `recurso-afirmando-la-cosecha/compositions/resumen.html`. SPEC → «resumen y llamado».



### 21. llamado

- En Kingdom te *acompañamos* a poner en marcha tu academia.
- Escríbenos por WhatsApp.

_Fuente:_ Llamado `acompanamiento` y contacto `whatsapp` del kit. SPEC → «resumen y llamado».


