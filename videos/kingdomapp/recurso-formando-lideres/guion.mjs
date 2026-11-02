// Recurso para líderes 2 (sección «Para líderes», departamento Academia): «Formando líderes con Kingdom» (decisión 241; formato en
// ../README.md → «Tipo Recurso», variante «Para líderes» del kit v1.3: la app recreada en HTML, fiel a v2).
// node ../_herramientas/recurso.mjs preparar --idioma es
// Fuentes de cada afirmación: SPEC.md (KingdomApp frontend-v2/src/ayuda/es/academia/**, public/i18n/es.json y el código de Academia). La
// estrategia es del dueño (formar líderes que formen a otros) sobre 2 Timoteo 2:2, dicha en palabras propias (decisión del 2026-11-02).
export default {
  slug: 'formando-lideres',
  titulo: { es: 'Formando *líderes* con Kingdom' },
  ceja: { es: 'Recursos · Para líderes' }, // SPEC → intro: la ceja de la sección «Para líderes»
  descripcion: {
    es: 'Para el líder de academia, clases de la visión o escuela bíblica: cómo ordenar los cursos, cargarlos desde Excel, dictar en línea, llevar asistencia, notas y evaluaciones, aplazar una clase y graduar con certificado, para formar líderes que formen a otros.',
  },
  llamado: 'acompanamiento',
  contacto: 'whatsapp',
  para: ['lideres'],
  seccion: 'lideres',
  departamento: 'academia',
  mensaje: {
    es: 'Para tu equipo de academia: mira cómo formar líderes con Kingdom, paso a paso. {enlace}',
  },
  escenas: [
    // ── Apertura ────────────────────────────────────────────────────────────────────────────────────────────────────────────────
    {
      id: 'gancho',
      frases: [
        { es: 'Una persona llegó a tu iglesia, la llamaron, la acompañaron y se *quedó*.', clave: 'quedo', pausa: 0.6 },
        { es: 'Afirmarla fue el comienzo. Ahora tiene que *crecer*.', clave: 'crecer', pausa: 0.6 },
        { es: 'Conocer la Palabra, ser edificada y, un día, *formar* a otros.', clave: 'formar', pausa: 0.8 },
        { es: 'Si diriges la *academia*, las clases de la visión o la escuela bíblica, este video es para ti.', clave: 'academia', pausa: 0.5 },
        { es: 'Vas a ver cómo usar Kingdom para que cada alumno crezca y tu iglesia tenga más *líderes*.', clave: 'lideres', pausa: 0.5 },
      ],
      entrada: 0.5,
      cola: 0.8,
      sonidos: [{ sonido: 'aparicion', frase: 0, palabra: 12, desfase: -0.2, alPulso: true }],
    },
    // ── Capítulo 1: formados para formar (estrategia, 2 Timoteo 2:2) ────────────────────────────────────────────────────────────
    {
      id: 'cap-1',
      capitulo: { numero: '1', titulo: { es: 'Formados para *formar*' }, bajada: { es: 'El plan es que se multiplique' }, icono: 'diversity_3', fondo: 'noche' },
      duracion: 4,
    },
    {
      id: 'formar',
      frases: [
        { es: 'Pablo le encargó a Timoteo que enseñara lo que había aprendido a personas fieles, capaces de enseñar a *otros*.', clave: 'otros', pausa: 0.6 },
        { es: 'En una sola frase hay cuatro *generaciones*: Pablo, Timoteo, los fieles y los otros.', clave: 'generaciones', pausa: 0.7 },
        { es: 'Ese es el corazón de tu academia: no llenar salones, sino formar personas que *formen* a otras.', clave: 'formen', pausa: 0.6 },
        { es: 'El miembro se vuelve *discípulo*, y el discípulo se vuelve líder.', clave: 'discipulo', pausa: 0.6 },
        { es: 'Una iglesia crece hasta donde crecen sus *líderes*: cada líder nuevo puede abrir un grupo nuevo.', clave: 'lideres', pausa: 0.6 },
        { es: 'Kingdom te ayuda a que ese camino sea *claro*, medible y sin papeles.', clave: 'claro', pausa: 0.5 },
      ],
      entrada: 0.5,
      cola: 0.8,
      estirable: true,
    },
    // ── Capítulo 2: categorías, programas y grupos ──────────────────────────────────────────────────────────────────────────────
    {
      id: 'cap-2',
      capitulo: { numero: '2', titulo: { es: 'Tu academia en *orden*' }, bajada: { es: 'Categorías, programas y grupos' }, icono: 'account_tree', fondo: 'noche' },
      duracion: 4,
    },
    {
      id: 'orden',
      frases: [
        { es: 'Todo empieza ordenando tu academia en *categorías*: Visión, Biblia, Servicio. Las creas tú, con su ícono y su color.', clave: 'categorias', pausa: 0.5 },
        { es: 'Dentro de una categoría puedes armar un *programa*: una serie de cursos por niveles.', clave: 'programa', pausa: 0.5 },
        { es: 'Por ejemplo, Clases de la visión: Miembros, *Discípulos* y Líderes.', clave: 'discipulos', pausa: 0.5 },
        { es: 'Cada nivel pide haber aprobado el *anterior*, y Kingdom lo revisa al inscribir.', clave: 'anterior', pausa: 0.5 },
        { es: 'El curso se define *una vez*, y abres los grupos que necesites: el martes en la noche, el domingo en la tarde.', clave: 'vez', pausa: 0.5 },
        { es: 'Al inscribir, Kingdom te muestra quiénes *pueden* tomarlo.', clave: 'pueden', pausa: 0.5 },
        { es: 'Y si alguien falta, puede *recuperar* la clase en otro grupo del mismo curso.', clave: 'recuperar', pausa: 0.5 },
      ],
      entrada: 0.5,
      cola: 0.8,
      estirable: true,
    },
    // ── Capítulo 3: crear el curso y cargarlo desde Excel ───────────────────────────────────────────────────────────────────────
    {
      id: 'cap-3',
      capitulo: { numero: '3', titulo: { es: 'Un curso listo en *minutos*' }, bajada: { es: 'Del Excel a tu academia' }, icono: 'upload_file', fondo: 'noche' },
      duracion: 4,
    },
    {
      id: 'curso',
      frases: [
        { es: 'Crear un curso es un asistente de cinco *pasos*: datos, materias y clases, actividades y pesos, criterios, y logro.', clave: 'pasos', pausa: 0.5 },
        { es: 'Eliges su modalidad: *presencial*, híbrido, en línea, o exprés, de un solo día.', clave: 'presencial', pausa: 0.5 },
        { es: '¿Ya tienes el pensum en Excel? Descarga la *plantilla*, llénala y súbela.', clave: 'plantilla', pausa: 0.5 },
        { es: 'Kingdom revisa cada fila, te marca los errores y arma las materias, las clases y las actividades con sus *pesos*.', clave: 'pesos', pausa: 0.5 },
        { es: 'Las preguntas de las evaluaciones también se cargan de una vez: desde Excel, o pegando el *texto* que ya tienes en Word o en WhatsApp.', clave: 'texto', pausa: 0.5 },
        { es: 'Un asterisco marca la respuesta correcta; revisas y las guardas *todas* juntas.', clave: 'todas', pausa: 0.5 },
        { es: 'Y el material, presentaciones, lecturas o videos, lo subes de *varios* archivos a la vez, por materia o por clase.', clave: 'varios', pausa: 0.5 },
      ],
      entrada: 0.5,
      cola: 0.8,
      estirable: true,
      sonidos: [{ sonido: 'subida', frase: 3, palabra: 9, desfase: -0.15, alPulso: true }],
    },
    // ── Capítulo 4: en línea e híbrido ──────────────────────────────────────────────────────────────────────────────────────────
    {
      id: 'cap-4',
      capitulo: { numero: '4', titulo: { es: 'Clases en *línea*' }, bajada: { es: 'A su ritmo o en vivo' }, icono: 'play_circle', fondo: 'noche' },
      duracion: 4,
    },
    {
      id: 'enlinea',
      frases: [
        { es: 'Un curso *en línea* se toma a su ritmo, sin calendario.', clave: 'linea', pausa: 0.5 },
        { es: 'Arrastras tus videos y cada uno queda como una *lección*, con su nombre y su duración.', clave: 'leccion', pausa: 0.5 },
        { es: 'O pegas el enlace de *YouTube* o de Vimeo, y no gastas espacio.', clave: 'youtube', pausa: 0.5 },
        { es: 'Puedes pedir un *quiz* para completar la lección, que avancen en orden y que de verdad vean el video.', clave: 'quiz', pausa: 0.5 },
        { es: 'El alumno ve su *avance*, y al volver, el video sigue donde iba.', clave: 'avance', pausa: 0.5 },
        { es: 'Si lleva siete días sin avanzar, le llega un aviso: te *esperamos*.', clave: 'esperamos', pausa: 0.6 },
        { es: 'Y si prefieres clases en vivo, el curso *híbrido* lleva el enlace de tu Zoom o tu Meet, con el botón «Unirse en vivo» quince minutos antes.', clave: 'hibrido', pausa: 0.5 },
      ],
      entrada: 0.5,
      cola: 0.8,
      estirable: true,
    },
    // ── Capítulo 5: el profesor ─────────────────────────────────────────────────────────────────────────────────────────────────
    {
      id: 'cap-5',
      capitulo: { numero: '5', titulo: { es: 'El profesor, sin *papeles*' }, bajada: { es: 'Asistencia, notas y evaluaciones' }, icono: 'fact_check', fondo: 'noche' },
      duracion: 4,
    },
    {
      id: 'asistencia',
      frases: [
        { es: 'Para el profesor, todo empieza en «*Hoy*»: la clase del día, lo pendiente y lo que vence esta semana.', clave: 'hoy', pausa: 0.5 },
        { es: 'Toca «Tomar asistencia» y muestra el *código*: cuatro números que cambian cada minuto.', clave: 'codigo', pausa: 0.5 },
        { es: 'A cada alumno le llega un aviso; escribe el código en su celular, y *listo*.', clave: 'listo', pausa: 0.5 },
        { es: 'El profesor ve en vivo cuántos marcaron, y a quien no tiene celular lo marca con un *toque*.', clave: 'toque', pausa: 0.5 },
        { es: '¿No hay señal en el salón? «Pasar *lista*» funciona sin señal, y se envía sola cuando vuelve.', clave: 'lista', pausa: 0.5 },
      ],
      entrada: 0.5,
      cola: 0.8,
      estirable: true,
      sonidos: [{ sonido: 'confirmacion', frase: 'listo', palabra: 14, desfase: -0.15, alPulso: true }],
    },
    {
      id: 'calificar',
      frases: [
        { es: 'Las *notas* se ponen en fila: escribes, Enter, y pasas al siguiente.', clave: 'notas', pausa: 0.5 },
        { es: 'Las evaluaciones se abren con un toque, por el tiempo que elijas, y se *califican* solas al cerrar. Las preguntas abiertas las calificas tú.', clave: 'califican', pausa: 0.5 },
        { es: 'Cada alumno recibe su nota y ve cuál era la respuesta *correcta*.', clave: 'correcta', pausa: 0.5 },
        { es: 'Los trabajos llegan con una foto o un archivo, y los calificas uno tras otro, con un *comentario*.', clave: 'comentario', pausa: 0.5 },
        { es: 'Todo cae en la sábana de notas, con el *semáforo* de cada alumno: cumple, en riesgo o no cumple.', clave: 'semaforo', pausa: 0.5 },
        { es: 'Y en «Faltaron» ves quién lleva varias clases sin venir, y le *escribes* por WhatsApp con un toque.', clave: 'escribes', pausa: 0.5 },
      ],
      entrada: 0.5,
      cola: 0.8,
      estirable: true,
    },
    // ── Capítulo 6: aplazar una clase ───────────────────────────────────────────────────────────────────────────────────────────
    {
      id: 'cap-6',
      capitulo: { numero: '6', titulo: { es: 'Si la clase se *corre*' }, bajada: { es: 'Aplazar sin rehacer el calendario' }, icono: 'calendar_month', fondo: 'noche' },
      duracion: 4,
    },
    {
      id: 'aplazar',
      frases: [
        { es: 'Un festivo, un viaje, un culto *especial*: a veces una clase no se puede dictar ese día.', clave: 'especial', pausa: 0.5 },
        { es: 'En «Fechas», abres el menú de la clase y tocas «Aplazar o *mover*».', clave: 'mover', pausa: 0.5 },
        { es: 'Eliges la nueva fecha, y la opción de correr también las clases *siguientes* ya viene marcada.', clave: 'siguientes', pausa: 0.5 },
        { es: 'Antes de confirmar, ves cómo *quedan*: las cinco clases siguientes se corren siete días.', clave: 'quedan', pausa: 0.5 },
        { es: 'Tocas «Aplazar y avisar»: el calendario se corre *solo*, la fecha de cierre también, y los recordatorios se reprograman.', clave: 'solo', pausa: 0.5 },
        { es: 'Y a cada alumno le llega el aviso: tu clase cambió de *fecha*.', clave: 'fecha', pausa: 0.5 },
      ],
      entrada: 0.5,
      cola: 0.8,
      estirable: true,
      sonidos: [{ sonido: 'desliz', frase: 'solo', palabra: 5, desfase: -0.1, alPulso: true }],
    },
    // ── Capítulo 7: el alumno ───────────────────────────────────────────────────────────────────────────────────────────────────
    {
      id: 'cap-7',
      capitulo: { numero: '7', titulo: { es: 'Cada alumno ve su *avance*' }, bajada: { es: 'Su progreso en su celular' }, icono: 'trending_up', fondo: 'noche' },
      duracion: 4,
    },
    {
      id: 'alumno',
      frases: [
        { es: 'Del otro lado, el alumno tiene todo en su *celular*, en «Mis cursos».', clave: 'celular', pausa: 0.5 },
        { es: 'Ve a cuántas clases ha venido, cuál es la *próxima* y qué tiene pendiente.', clave: 'proxima', pausa: 0.5 },
        { es: 'Cuando el profesor abre la asistencia, le llega el aviso; escribe los cuatro números y queda *marcada*.', clave: 'marcada', pausa: 0.5 },
        { es: 'Entrega un trabajo tomando una *foto*, o subiendo un PDF.', clave: 'foto', pausa: 0.5 },
        { es: 'Presenta su evaluación con el *tiempo* a la vista, y si se va la señal, sus respuestas se guardan en el celular.', clave: 'tiempo', pausa: 0.5 },
        { es: 'Y en «Mis notas» sabe cómo va, y qué le falta para *aprobar*.', clave: 'aprobar', pausa: 0.5 },
      ],
      entrada: 0.5,
      cola: 0.8,
      estirable: true,
      sonidos: [{ sonido: 'confirmacion', frase: 'marcada', palabra: 16, desfase: -0.15, alPulso: true }],
    },
    // ── Capítulo 8: graduar y multiplicar ───────────────────────────────────────────────────────────────────────────────────────
    {
      id: 'cap-8',
      capitulo: { numero: '8', titulo: { es: 'Graduados que *forman*' }, bajada: { es: 'Certificados y nuevos líderes' }, icono: 'workspace_premium', fondo: 'noche' },
      duracion: 4,
    },
    {
      id: 'graduar',
      frases: [
        { es: 'Al terminar, el profesor abre «*Graduar*»: Kingdom arma la lista con los criterios del curso.', clave: 'graduar', pausa: 0.5 },
        { es: 'Quien coordina la *aprueba*, y a cada graduado le llega: ya está tu certificado.', clave: 'aprueba', pausa: 0.5 },
        { es: 'Lleva el logo de tu iglesia, la firma de tu pastor si la subes, y un código *QR* que cualquiera puede verificar.', clave: 'qr', pausa: 0.5 },
        { es: 'Si el curso otorga un *logro*, la persona lo recibe, y tu ruta de crecimiento puede cumplir ese paso sola.', clave: 'logro', pausa: 0.5 },
      ],
      entrada: 0.5,
      cola: 0.8,
      estirable: true,
      sonidos: [{ sonido: 'aparicion', frase: 'aprueba', palabra: 10, desfase: -0.2, alPulso: true }],
    },
    {
      id: 'multiplicar',
      frases: [
        { es: 'En el *Tablero* ves toda tu academia: quién está en riesgo, quién falta seguido, quién se graduó.', clave: 'tablero', pausa: 0.6 },
        { es: 'Pero el fruto no es un certificado: es una persona que ahora puede *enseñar*.', clave: 'ensenar', pausa: 0.6 },
        { es: 'Quien se graduó de Líderes puede ser el *profesor* del próximo grupo.', clave: 'profesor', pausa: 0.5 },
        { es: 'Si ya sirve en tu iglesia, lo nombras en el grupo, y ve *solo* ese grupo: sus alumnos, su asistencia y sus notas.', clave: 'solo', pausa: 0.6 },
        { es: 'Así se cumple lo que Pablo le encargó a Timoteo: fieles que enseñan a *otros*.', clave: 'otros', pausa: 0.6 },
        { es: 'Y una iglesia que forma líderes es una iglesia que se *multiplica*.', clave: 'multiplica', pausa: 0.6 },
      ],
      entrada: 0.5,
      cola: 0.8,
    },
    {
      id: 'resumen',
      frases: [
        { es: 'Formar líderes con Kingdom es *simple*.', clave: 'simple', pausa: 0.6 },
        { es: 'Ordena tu academia en categorías, programas y grupos. Carga tus cursos desde Excel.', clave: 'r1', pausa: 0.4 },
        { es: 'Deja que la asistencia, las notas y los avisos trabajen por ti.', clave: 'r2', pausa: 0.4 },
        { es: 'Acompaña a cada alumno hasta graduarse, y ponlo a enseñar a otros.', clave: 'r3', pausa: 0.7 },
        { es: 'Porque cada persona que formas hoy es un *líder* que formará mañana.', clave: 'lider', pausa: 0.6 },
      ],
      entrada: 0.5,
      cola: 0.8,
      estirable: true,
    },
    {
      id: 'llamado',
      frases: [
        { es: 'En Kingdom te *acompañamos* a poner en marcha tu academia.', clave: 'acompanamos', pausa: 0.5 },
        { es: 'Escríbenos por WhatsApp.', clave: 'whatsapp', pausa: 0.5 },
      ],
      entrada: 0.5,
      cola: 1.0,
    },
  ],
};
