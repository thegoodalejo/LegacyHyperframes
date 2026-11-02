# SPEC: Formando líderes con Kingdom (Recursos · Para líderes · Academia)

Este documento da la fuente de cada frase del guion (`guion.mjs`), lo que se ve en cada escena y lo que el video **no** dice.

**Rutas y abreviaturas** (todas las rutas son de KingdomApp):
- **[h:x]**: `frontend-v2/src/ayuda/es/academia/x.md`.
- **[I:n]**: la línea `n` de `frontend-v2/public/i18n/es.json`. Son los textos exactos de la pantalla y se escriben tal cual.
- **[C:n]**: `backend/avisos/catalogo.json`.
- **Componentes** de `frontend-v2/src/app/pages/academia/`, abreviado `PA/`.
- **Capturas** de referencia en `assets/referencias/academia__<artículo>__<nombre>.webp`.
  - Escritorio: 2880×2000 (1440 a 2x). Celular: 1170×2532 (390 a 3x).
  - Sus marcas numeradas y bordes de resaltado no son parte de la app.

**Vocabulario.** La app usa las palabras de fábrica: Curso, Cursos, Grupo, Grupos, Profesor, Profesores. Cada iglesia puede cambiarlas en
Ajustes → «Palabras de tu iglesia».

**Marca.** La pantalla recreada usa el azul de fábrica de v2 (primario `#015bbe`), no el morado de Kingdom Demo, como en
`recurso-afirmando-la-cosecha`. El semáforo usa los tokens propios de `frontend-v2/src/styles/_tokens.scss:57-68`:
- **Cumple:** verde `#006e25`; contenedor `#8cfa94`.
- **En riesgo:** amarillo `#f1c014`; contenedor `#ffe08e`.
- **No cumple:** rojo `#bb1713`; contenedor `#ffdad5`.

## Lo que el video NO dice (y por qué)

- **No hay lectura de Word ni de PDF, ni IA** (decisión 109, `backend/_datos/academia_preguntas.php:13-14`). Hay dos plantillas de **Excel**
  (.xlsx, leídas en el navegador), la del pensum y la de preguntas, más el **texto pegado** para las preguntas. Siempre llevan revisión antes
  de guardar.
- **No hay aula en vivo propia** (decisión 111, para después). El curso híbrido lleva el enlace externo de la iglesia (Zoom, Meet, Teams,
  YouTube).
- **Aplazar corre las clases siguientes los mismos días**, no «a la siguiente sesión». No corre las ventanas de las evaluaciones ni las
  fechas límite de las entregas. El aviso inmediato es para los alumnos y por la clase movida.
- **El código de asistencia necesita señal.** Lo que funciona sin señal es «Pasar lista» del profesor.
- **Graduarse no asciende a nadie.** Quien coordina nombra al profesor en un grupo, y el profesor necesita una cuenta de servidor
  (`backend/academia/_academia.php:100-109`).
- **La ruta de crecimiento no viene conectada a Academia de fábrica.** La iglesia la configura (Membresía → Ajustes → Ruta, «Al empezar un
  curso» / «Al terminar un curso»). Por eso el video dice «puede».
- **Academia no manda WhatsApp** (decisión 120). El botón «Escribir» de «Faltaron» abre el WhatsApp **del propio profesor** con un mensaje
  listo [I:861].
- **El profesor no cambia el banco de preguntas ni los pesos;** eso es de quien coordina. El profesor pone notas, abre evaluaciones, configura
  entregas, sube material de su grupo y aplaza sus clases.
- **Cada iglesia crea sus categorías y programas.** Los de la pantalla son de ejemplo.
- **Sin cifras de resultados.** Los números de pantalla (18 inscritos, 13 marcaron, etc.) son de ejemplo, con la etiqueta «Datos de ejemplo».

## Escena por escena

### gancho (motion design)

| Frase | Fuente |
|---|---|
| «llegó… la llamaron, la acompañaron y se quedó» | Continúa el video anterior, «Afirmando la cosecha» (registrar, llamar, acompañar). |
| «Afirmarla fue el comienzo. Ahora tiene que crecer… formar a otros» | El pedido del dueño (BRIEF). |
| «Si diriges la academia, las clases de la visión o la escuela bíblica» | El pedido del dueño. |

Lo que se ve: una persona (un punto o avatar) que avanza por afirmada → formada → forma a otros. Es la misma gramática de motion design de
`recurso-afirmando-la-cosecha/compositions/gancho.html` y `camino.html`.

### formar (estrategia, motion design)

| Frase | Fuente |
|---|---|
| «Pablo le encargó a Timoteo…» | 2 Timoteo 2:2, parafraseado. En pantalla, la cita «2 Timoteo 2:2», sin el texto de una versión con derechos. |
| «cuatro generaciones: Pablo, Timoteo, los fieles y los otros» | Lectura del mismo versículo. |
| «Miembro → Discípulo → Líder» | El programa de ejemplo «Clases de la visión» (niveles Miembros, Discípulos, Líderes), de `backend/cron/jobs/_demo_academia.php:64`. Es el logro de niveles «Nivel de la visión» (Miembro, Discípulo, Líder) de la plantilla de Membresía (`backend/_datos/personas_catalogos.php:301-309`). |
| «cada líder nuevo puede abrir un grupo nuevo» | Estrategia del dueño (multiplicación). |

Lo que se ve: cuatro nodos que se encadenan y se multiplican (1 → 1 → varios → muchos), y la escalera Miembro → Discípulo → Líder.

### orden (escritorio, 1440×760)

| Frase | Fuente | Referencia |
|---|---|---|
| Categorías, «Las creas tú, con su ícono y su color» | [h:ajustes] «Categorías»; el diálogo pide Nombre, Ícono, Color y «Descripción (opcional)» [I:438] | `ajustes__03-categorias`, `ajustes__04-categoria-nueva`, `crear-un-curso__01-catalogo` |
| Programa: una serie de cursos por niveles | [h:ajustes] «Programas»; «Nuevo programa» [I:446] y «Logro de niveles que otorga» [I:452] | `ajustes__05-programas` |
| «Clases de la visión: Miembros, Discípulos y Líderes» | Demo `_demo_academia.php:64`; `docs/modulos/academia.md:144-146` | catálogo: chips «Clases de la visión · nivel 1» |
| «Cada nivel pide haber aprobado el anterior, y Kingdom lo revisa al inscribir» | `academia_cursos.php:245-265` (cadena automática) y `academia_inscripciones.php:32-81` (se exige al inscribir) | `inscribir__05-requisito` |
| «El curso se define una vez, y abres los grupos que necesites» | [h:abrir-un-grupo]; grupos de la demo «Miembros · martes 7 p. m.» y «Miembros · domingo 2 p. m.» | `abrir-un-grupo__01-catalogo`, `abrir-un-grupo__02-datos` |
| «quiénes pueden tomarlo» | «Pueden tomarlo» [I:810]; [h:inscribir] | `inscribir__02-pueden` |
| «recuperar la clase en otro grupo del mismo curso» | [h:marcar-mi-asistencia]; «¿Vienes a recuperar una clase en otro grupo? Marca el código» [I:878] | — |

Lo que se ve: el catálogo «Cursos» (`PA/cursos.page.ts`) con los chips de categoría, una sección por categoría con su ícono en su color y
tarjetas de curso con sus grupos. La cámara entra al programa y lo muestra por niveles; luego, «Inscribir» → «Pueden tomarlo».

### curso (escritorio)

| Frase | Fuente | Referencia |
|---|---|---|
| Los cinco pasos: «Datos, modalidad y visibilidad», «Materias y clases», «Actividades y pesos», «Criterios de aprobación», «Logro y prerrequisito» | [h:crear-un-curso]; `PA/curso.page.ts` | `crear-un-curso__03-datos` … `07-logro` |
| Modalidades: «Presencial», «Híbrido», «En línea», «Exprés» (de un solo día) | [I:98-101]; `academia_grupos.php:61` (exprés de un día) | `crear-un-curso__03-datos` |
| «Descarga la plantilla, llénala y súbela» | «¿Ya tienes el pensum en Excel?…» e «Importar desde Excel» [I:276]; «Descargar plantilla» [I:373] | `crear-un-curso__04-estructura` (el botón). **El diálogo del pensum no tiene captura:** se recrea desde `PA/pensum-dialog.component.ts` (con `services/academia/pensum-excel.ts`) y [I:369-427]. |
| «revisa cada fila, te marca los errores y arma las materias, las clases y las actividades con sus pesos» | La revisión con las filas con error y «Usar este pensum» [I:421]; columnas Materia, Clase, Fecha, Actividad, Nombre de la actividad y Peso (%) (`services/academia/pensum.ts:1-14`) | `crear-un-curso__04-estructura`, `crear-un-curso__05-pesos` |
| Preguntas desde Excel o pegando el texto de Word o WhatsApp | «Cargar desde Excel o texto» [I:1420], «Pegar texto» [I:1329]; [h:material-y-banco] | `material-y-banco__05-banco`, `material-y-banco__06-importar` |
| «Un asterisco marca la respuesta correcta; revisas y las guardas todas juntas» | [I:1338]; «Guardar {n} preguntas» [I:1351]; todo o nada (`academia_preguntas.php:463-542`) | `material-y-banco__07-banco-listo` |
| Material: varios archivos a la vez, por materia o por clase | «Subir archivos», «Agregar un enlace», «Traer de Archivos»; «Dónde va»: General, materia o clase [I:924-1000] | `material-y-banco__02-agregar`, `material-y-banco__04-material` |

### enlinea (escritorio para el constructor; celular para el alumno)

| Frase | Fuente | Referencia |
|---|---|---|
| «se toma a su ritmo, sin calendario» | [h:lecciones-en-linea]; `academia_en_linea.php:1-26` | — |
| «Arrastras tus videos y cada uno queda como una lección, con su nombre y su duración» | «Subir videos» [I:1702]; [I:1716-1717] | `lecciones-en-linea__01-constructor` |
| «el enlace de YouTube o de Vimeo, y no gastas espacio» | «Usar el enlace»; el video subido sí gasta espacio [h:lecciones-en-linea] | `lecciones-en-linea__02-leccion` |
| «un quiz para completar la lección, que avancen en orden y que de verdad vean el video» | «Requisito para completarla»: Ninguno, Un quiz, Entregar un archivo; «En orden» [I:1710], «Exigir ver el video» [I:1712], que pide el 90 % | `lecciones-en-linea__03-opciones` |
| «ve su avance, y al volver, el video sigue donde iba» | El anillo «{n} de {total} lecciones» y «Continuar»; «seguirá donde ibas» [I:1636]; `ac_progreso` guarda la posición | `mis-cursos__08-leccion`, `mis-cursos__09-completada` |
| «siete días sin avanzar, le llega un aviso: te esperamos» | `academia.sin_avanzar`, «Te esperamos en {curso}» [C:750-760], a los 7 días y como mucho uno por semana (`ac_diario.php`) | — |
| Híbrido: el enlace de Zoom o Meet y «Unirse en vivo» quince minutos antes | «Enlace de la clase en vivo»; «Unirse en vivo» [I:875]; [I:906] | `abrir-un-grupo__02-datos` |

### asistencia (celular del profesor, 390×812)

| Frase | Fuente | Referencia |
|---|---|---|
| «Hoy»: la clase del día, lo pendiente y lo que vence esta semana | `PA/asistencia/hoy.component.ts`; [I:772-781] | `tomar-asistencia__01-hoy` |
| «Tomar asistencia» → «Mostrar el código»: cuatro números que cambian cada minuto | [I:763-765]; [I:699]; HMAC por minuto (`academia_asistencia.php:5-19`) | `tomar-asistencia__02-formas`, `tomar-asistencia__03-codigo` |
| «A cada alumno le llega un aviso; escribe el código» | `academia.asistencia`, «Tu profesor está tomando asistencia» [C:574-588] | `marcar-mi-asistencia__01-tarjeta`, `__02-codigo`, `__03-listo` |
| «ve en vivo cuántos marcaron, y a quien no tiene celular lo marca con un toque» | «{n} de {total} marcaron» [I:721]; «Faltan (N)» con «Presente» [I:731-732] | `tomar-asistencia__03-codigo`, `tomar-asistencia__04-presente` |
| «Pasar lista» funciona sin señal y se envía sola | [I:767]; [I:737] | `tomar-asistencia__06-lista` |

### calificar (celular del profesor)

| Frase | Fuente | Referencia |
|---|---|---|
| «Las notas se ponen en fila: escribes, Enter, y pasas al siguiente» | [I:1193] | `notas-entregas-y-evaluaciones__01-notas`, `__02-columna` |
| «se abren con un toque, por el tiempo que elijas, y se califican solas al cerrar; las abiertas las calificas tú» | «Abrir ahora» [I:1514] → «¿Por cuánto tiempo?» (15, 30, 45, 60, 90, 120); `ac_horario.php` califica al cierre; «Calificar (N)» para las abiertas | `__05-evaluaciones`, `__07-ventana` |
| «recibe su nota y ve cuál era la respuesta correcta» | «Ya está tu nota» [C:728-737]; el resultado con «Tu respuesta» y «La correcta» | `mis-cursos__06-evaluacion`, `__06-resultados` |
| «Los trabajos llegan con una foto o un archivo, y los calificas uno tras otro, con un comentario» | «Calificar en fila ({n})» [I:1081]; «Comentario para el alumno» | `__03-entregas`, `__04-configurar` |
| La sábana de notas con el semáforo | `PA/notas/notas-grupo.component.ts`; Cumple, En riesgo, No cumple | `__01-notas` |
| «Faltaron»: quién lleva varias clases sin venir, y «Escribir» por WhatsApp | «Faltaron ({n})» [I:848], «{n} clases seguidas sin venir», «Escribir» [I:851] y el mensaje [I:861] | `tomar-asistencia__07-faltaron` |

### aplazar (escritorio)

| Frase | Fuente | Referencia |
|---|---|---|
| «En “Fechas”, abres el menú de la clase y tocas “Aplazar o mover”» | [h:abrir-un-grupo]; «Aplazar o mover» [I:562] | `abrir-un-grupo__04-fechas` |
| «la opción de correr también las clases siguientes ya viene marcada» | [I:589]; marcada por defecto (`PA/aplazar-dialog.component.ts:98`); la nueva fecha propone una semana después (línea 94) | `abrir-un-grupo__05-aplazar` |
| «las cinco clases siguientes se corren siete días» | «Las {n} clases siguientes se corren {dias} días.» [I:590]. **La captura muestra exactamente 5 y 7** | `abrir-un-grupo__05-aplazar` |
| «Aplazar y avisar»: el calendario se corre solo, la fecha de cierre también, y los recordatorios se reprograman | [I:596]; `acClaseAplazar` (`academia_grupos.php:651-691`), `acGrupoFechasResumen` (362-367, la fecha de fin) y `acAvisosClasesGrupo` (`academia_avisos.php:126-189`) | — |
| «tu clase cambió de fecha» | `academia.clase_cambio`, «Tu clase cambió de fecha» [C:589-606]; «Se avisa a {n} inscritos.» [I:592] | — |

Lo que se ve:
- La lista de «Fechas» con las tarjetas de clase (día grande, «JUE», nombre de la clase, «7:00 p. m. – 8:30 p. m. · Crecer en la fe»).
- El diálogo con «Nueva fecha», «Hora», la casilla marcada y la vista previa con la lista «antes → después».
- Al confirmar, las tarjetas de la lista se corren en cascada a sus fechas nuevas.
- El aviso en el celular del alumno.

En la captura, el grupo de ejemplo es «Discípulos», jueves 7 p. m., con las clases «La vida devocional», «La palabra cada día», «La oración que
transforma», «El ayuno», «Dar con alegría» y «Servir en un ministerio». En la recreación, el diálogo dice «Se avisa a 18 inscritos.», no «Todavía no
hay inscritos…».

### alumno (celular de la alumna)

| Frase | Fuente | Referencia |
|---|---|---|
| «Mis cursos» | [h:mis-cursos]; `PA/mis-cursos.page.ts`; En curso, Explorar, Terminados | `mis-cursos__01-mis-cursos`, `mi-iglesia__mis-cursos__01-cursos` |
| «a cuántas clases ha venido, cuál es la próxima y qué tiene pendiente» | [I:872-873]; «Pendientes» | `mis-cursos__02-clases`, `mis-cursos__03-pendientes` |
| El aviso y los cuatro números | [I:697-708]; «¡Listo! Quedó tu asistencia» | `marcar-mi-asistencia__01-tarjeta`, `__02-codigo`, `__03-listo` |
| «tomando una foto, o subiendo un PDF» | «Tomar foto» [I:1172], «Elegir archivo» | `mis-cursos__04-entrega` |
| «con el tiempo a la vista, y si se va la señal, sus respuestas se guardan en el celular» | La cuenta regresiva con la hora del servidor; [I:1226] | `mis-cursos__06-evaluacion` |
| «Mis notas»: cómo va y qué le falta para aprobar | [I:902]; el semáforo con su motivo (por ejemplo «Asistencia: 50 %; se pide 75 %») | `mis-cursos__05-notas` |

### graduar (escritorio)

| Frase | Fuente | Referencia |
|---|---|---|
| «Cerrar y graduar»: la lista con los criterios del curso | [I:1854]; `academia_graduaciones.php:474-486` | `notas-entregas-y-evaluaciones__08-graduar` |
| Quien coordina la aprueba, y «¡Ya está tu certificado!» | «Por aprobar», «Aprobar ({n})»; `academia.certificado` [C:739-749] | `graduar-y-certificados__01-por-aprobar` … `03-confirmar` |
| El logo, la firma «si la subes» y el QR verificable | `services/academia/certificado-pdf.ts`; Ajustes → Certificado («Subir la firma» es opcional); `/verificar/<código>` es pública | `graduar-y-certificados__05-certificado`, `ajustes__06-certificado` |
| «Si el curso otorga un logro, la persona lo recibe, y tu ruta de crecimiento puede cumplir ese paso sola» | Paso 5 «Logro y prerrequisito»; `academiaRutaGraduado` (`academia_graduaciones.php:549-555`); el paso «Al terminar un curso» se configura en Membresía | `crear-un-curso__07-logro` |

### multiplicar (escritorio y motion design)

| Frase | Fuente | Referencia |
|---|---|---|
| El Tablero: quién está en riesgo, quién falta seguido, quién se graduó | «Alumnos en riesgo», «Con 2 o más faltas seguidas», «Graduados» [I:2138-2209] | `tablero__01-resumen` |
| «Quien se graduó de Líderes puede ser el profesor del próximo grupo» | Estrategia; al abrir un grupo se nombran sus profesores [h:abrir-un-grupo] | `abrir-un-grupo__03-profesor` |
| «Si ya sirve en tu iglesia, lo nombras en el grupo, y ve solo ese grupo» | `_academia.php:100-109` (`dictar` «suyo», con cuenta de servidor) | — |
| «fieles que enseñan a otros» / «se multiplica» | 2 Timoteo 2:2 (vuelve el gráfico de las generaciones) | — |

### resumen y llamado

Son las mismas formas de `recurso-afirmando-la-cosecha` (`resumen.html` y `llamado.html`): «Te acompañamos» y WhatsApp, con el llamado
`acompanamiento`.
