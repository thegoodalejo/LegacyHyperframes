// Guion del recurso 1 de la serie «Recursos» (formato en ../README.md → «Tipo Recurso (v1.2)»).
//   node ../_herramientas/recurso.mjs preparar --idioma es
// Fuentes de cada afirmación: SPEC.md (columna «Fuente»). Nada de cifras de resultados, testimonios, iglesias reales ni precios.
export default {
  slug: 'iglesia-que-da-resultados',
  titulo: { es: 'Tu iglesia, con *resultados* que se ven' },
  descripcion: {
    es: 'Para el pastor principal: lo que tu iglesia puede medir con Membresía, Eventos, Academia y Equipos, y cómo te acompaña el equipo de Kingdom.',
  },
  ceja: { es: 'Recursos' },
  siguiente: { es: 'Eventos de ciudad, sin perder a nadie' },
  llamado: 'acompanamiento',
  contacto: 'whatsapp',
  para: ['pastores', 'lideres'],
  mensaje: { es: 'Pastor, le comparto este video de 6 minutos: lo que su iglesia puede medir con Kingdom. {enlace}' },
  escenas: [
    // ── Apertura ──────────────────────────────────────────────────────────────────────────────────────────────────────────
    {
      id: 'sabias',
      frases: [
        { es: '¿Sabías que con Kingdom puedes *estructurar* tu iglesia?', clave: 'gancho', pausa: 0.7 },
        { es: 'Tus redes, tus grupos y tus líderes, cada uno en su lugar.', clave: 'redes', pausa: 0.5 },
        { es: 'Y debajo de cada líder, las personas que cuida.', clave: 'personas', pausa: 0.6 },
        { es: 'Tu iglesia deja de ser una lista de nombres, y se ve como lo que es: una *red* de cuidado.', clave: 'red' },
      ],
      entrada: 0.5, cola: 1.0,
      sonidos: [{ sonido: 'aparicion', frase: 0, palabra: 5, desfase: -0.1, alPulso: true }],
    },
    {
      id: 'pastor',
      frases: [
        { es: 'Pastor, tú no tienes que pasar el día en la app.', clave: 'pastor', pausa: 0.6 },
        { es: 'Tus líderes son los que la usan: reportan, acompañan, enseñan y sirven.', clave: 'lideres', pausa: 0.5 },
        { es: 'Kingdom les da una forma clara de hacer su trabajo con *excelencia*.', clave: 'excelencia', pausa: 0.6 },
        { es: 'Y a ti te muestra lo que importa: los *resultados*.', clave: 'resultados', pausa: 0.7 },
        { es: 'Veamos lo que puedes medir en cuatro módulos: Membresía, Eventos, Academia y Equipos.', clave: 'modulos' },
      ],
      entrada: 0.5, cola: 1.0,
    },
    // ── 1. Membresía ─────────────────────────────────────────────────────────────────────────────────────────────────────
    { id: 'cap-1', capitulo: { numero: '1', titulo: { es: 'Membresía: que *nadie* se pierda' }, bajada: { es: 'Cada persona, con alguien que la cuida' }, icono: 'groups' }, duracion: 4 },
    {
      id: 'cuidado',
      frases: [
        { es: 'Todo empieza con las personas.', clave: 'empieza', pausa: 0.5 },
        { es: 'Cuando alguien llega por primera vez, se registra desde el celular, aun sin señal.', clave: 'llega', pausa: 0.5 },
        { es: 'Y no se queda solo: quien coordina reparte a los nuevos de forma *pareja* entre quienes acompañan.', clave: 'reparte', pausa: 0.6 },
        { es: 'Cada acompañante lo ve en Mi seguimiento: a quién llamar y qué paso sigue.', clave: 'seguimiento', pausa: 0.5 },
        { es: 'Y tú sabes quién ya recibió su llamada, y quién *todavía no*.', clave: 'llamada' },
      ],
      entrada: 0.5, cola: 0.9,
    },
    {
      id: 'semaforo',
      frases: [
        { es: 'Además, cada persona tiene un *semáforo de actividad*.', clave: 'semaforo', pausa: 0.6 },
        { es: 'Verde, si participó hace poco.', clave: 'verde', pausa: 0.3 },
        { es: 'Amarillo, si se está alejando.', clave: 'amarillo', pausa: 0.3 },
        { es: 'Rojo, si hace tiempo que no la vemos.', clave: 'rojo', pausa: 0.3 },
        { es: 'Y gris, si no tiene actividad.', clave: 'gris', pausa: 0.6 },
        { es: 'Tu iglesia decide cuántos días vale cada color.', clave: 'dias', pausa: 0.5 },
        { es: 'Así ves *a tiempo* a quien se está enfriando, y lo buscas antes de perderlo.', clave: 'tiempo' },
      ],
      entrada: 0.5, cola: 0.9,
      sonidos: [{ sonido: 'toque', frase: 1, palabra: 0, desfase: -0.1, alPulso: true }],
    },
    {
      id: 'ruta',
      frases: [
        { es: 'Cada persona también tiene su *ruta de crecimiento*.', clave: 'ruta', pausa: 0.6 },
        { es: 'La llamada de bienvenida, la visita, su grupo, un curso, servir.', clave: 'pasos', pausa: 0.5 },
        { es: 'Kingdom propone el siguiente paso.', clave: 'propone', pausa: 0.4 },
        { es: 'Y el paso se cumple con hechos: una asistencia, un curso terminado, un turno servido.', clave: 'hechos', pausa: 0.6 },
        { es: 'En el camino, cada persona suma sus *logros*: sus hitos y sus niveles.', clave: 'logros' },
      ],
      entrada: 0.5, cola: 0.9,
    },
    {
      id: 'tableros',
      frases: [
        { es: 'Y todo eso lo ves en los *tableros*.', clave: 'tableros', pausa: 0.5 },
        { es: 'Personas activas, nuevas, en ruta y conectadas, con su cambio en el período.', clave: 'cifras', pausa: 0.5 },
        { es: 'De toda la iglesia, o de cada red.', clave: 'red', pausa: 0.5 },
        { es: 'Y si necesitas algo puntual, armas el reporte a tu medida, en PDF o en Excel.', clave: 'reporte', pausa: 0.5 },
        { es: 'Llévalo a tu reunión de liderazgo, y decide con *datos*.', clave: 'datos' },
      ],
      entrada: 0.5, cola: 1.0,
      sonidos: [{ sonido: 'subida', frase: 1, palabra: 0, desfase: -0.1, alPulso: true }],
      estirable: true,
    },
    // ── 2. Eventos ───────────────────────────────────────────────────────────────────────────────────────────────────────
    { id: 'cap-2', capitulo: { numero: '2', titulo: { es: 'Eventos: cada reunión *cuenta*' }, bajada: { es: 'Cultos, casas de paz y células, reportados por tus líderes' }, icono: 'event_available' }, duracion: 4 },
    {
      id: 'reportar',
      frases: [
        { es: 'Ahora, las reuniones.', clave: 'ahora', pausa: 0.4 },
        { es: 'Cultos, casas de paz, células: cada iglesia define las suyas.', clave: 'define', pausa: 0.5 },
        { es: 'Al terminar, el líder la reporta desde su celular, en pasos guiados.', clave: 'reporta', pausa: 0.5 },
        { es: 'Marca a los de siempre en un toque, agrega a la persona nueva y cuenta a los visitantes.', clave: 'marca', pausa: 0.5 },
        { es: '¿No hay señal? Se guarda, y se envía *solo* cuando vuelve la conexión.', clave: 'senal', pausa: 0.5 },
        { es: 'Ninguna reunión se queda en una libreta.', clave: 'libreta' },
      ],
      entrada: 0.5, cola: 0.9,
      sonidos: [{ sonido: 'confirmacion', frase: 4, palabra: 7, desfase: -0.15, alPulso: true }],
    },
    {
      id: 'medir',
      frases: [
        { es: 'Para ti, cada evento tiene su semáforo: al día, por reportar o retrasado.', clave: 'semaforo', pausa: 0.5 },
        { es: 'Puede tener su *meta*, y Kingdom te muestra su tendencia: si crece, o si necesita apoyo.', clave: 'meta', pausa: 0.6 },
        { es: 'En el tablero ves la asistencia, las personas por reunión y los nuevos del período.', clave: 'tablero', pausa: 0.6 },
        { es: 'Y en el *mapa*, dónde viven tus personas,', clave: 'mapa', pausa: 0.3 },
        { es: 'y en qué zonas todavía no hay una reunión cerca.', clave: 'zonas', pausa: 0.5 },
        { es: 'Quizás ahí va tu próxima casa de paz.', clave: 'proxima' },
      ],
      entrada: 0.5, cola: 1.0,
      estirable: true,
    },
    // ── 3. Academia ──────────────────────────────────────────────────────────────────────────────────────────────────────
    { id: 'cap-3', capitulo: { numero: '3', titulo: { es: 'Academia: líderes *formados*' }, bajada: { es: 'Tu escuela de liderazgo, con notas y certificados' }, icono: 'school' }, duracion: 4 },
    {
      id: 'clases',
      frases: [
        { es: 'Tu visión necesita líderes formados.', clave: 'vision', pausa: 0.5 },
        { es: 'Con Academia, armas cada curso una vez, y lo repites con cada grupo.', clave: 'curso', pausa: 0.6 },
        { es: 'En clase, el profesor muestra un *código* de cuatro números,', clave: 'codigo', pausa: 0.3 },
        { es: 'y cada alumno marca su asistencia desde el celular. Sin listas de papel.', clave: 'marca', pausa: 0.6 },
        { es: 'La sábana de notas te dice quién cumple, y quién va en *riesgo*,', clave: 'riesgo', pausa: 0.3 },
        { es: 'a tiempo para acompañarlo.', clave: 'acompanar' },
      ],
      entrada: 0.5, cola: 0.9,
      sonidos: [{ sonido: 'toque', frase: 2, palabra: 6, desfase: -0.3, alPulso: true }],
    },
    {
      id: 'graduar',
      frases: [
        { es: 'Al cerrar el grupo, el profesor propone a quienes cumplieron, y quien coordina aprueba la graduación.', clave: 'cerrar', pausa: 0.6 },
        { es: 'Cada graduado recibe su *certificado*, con la firma del pastor y un código que cualquiera puede verificar.', clave: 'certificado', pausa: 0.6 },
        { es: 'Y su ruta de crecimiento avanza sola.', clave: 'ruta', pausa: 0.6 },
        { es: 'En el tablero ves los grupos en curso, los alumnos en riesgo y los graduados de cada período.', clave: 'tablero' },
      ],
      entrada: 0.5, cola: 1.0,
      sonidos: [{ sonido: 'confirmacion', frase: 1, palabra: 4, desfase: -0.3, alPulso: true }],
    },
    // ── 4. Equipos ───────────────────────────────────────────────────────────────────────────────────────────────────────
    { id: 'cap-4', capitulo: { numero: '4', titulo: { es: 'Equipos: cada puesto *cubierto*' }, bajada: { es: 'Los que sirven, organizados y reconocidos' }, icono: 'volunteer_activism' }, duracion: 4 },
    {
      id: 'turnos',
      frases: [
        { es: 'Detrás de cada reunión hay personas que sirven.', clave: 'detras', pausa: 0.5 },
        { es: 'Alabanza, seguridad, medios, audiovisual: cada equipo con sus líderes y sus integrantes.', clave: 'equipos', pausa: 0.6 },
        { es: 'El líder arma el turno, y Kingdom le sugiere a quién poner: quien sabe hacerlo, y ha servido menos.', clave: 'sugiere', pausa: 0.6 },
        { es: 'Cada persona acepta su turno desde el celular, con sus instrucciones: a qué hora llegar y cómo vestirse.', clave: 'acepta', pausa: 0.6 },
        { es: 'Y antes de la reunión, ves qué puestos están *cubiertos*, y cuáles faltan.', clave: 'cobertura' },
      ],
      entrada: 0.5, cola: 0.9,
    },
    {
      id: 'servir',
      frases: [
        { es: 'Al terminar, el líder cierra el turno y marca quién sirvió.', clave: 'cierra', pausa: 0.5 },
        { es: 'Así queda un historial real de cada servidor, y la carga se reparte parejo.', clave: 'historial', pausa: 0.6 },
        { es: 'Y servir *cuenta*: cumple el paso «Servir» de su ruta de crecimiento.', clave: 'cuenta', pausa: 0.6 },
        { es: 'Los reportes te muestran la cobertura de cada reunión, y la carga de cada persona.', clave: 'reportes' },
      ],
      entrada: 0.5, cola: 1.0,
      estirable: true,
    },
    // ── 5. Lo que gana tu iglesia ────────────────────────────────────────────────────────────────────────────────────────
    { id: 'cap-5', capitulo: { numero: '5', titulo: { es: 'Lo que *gana* tu iglesia' }, bajada: { es: 'Resultados que se miden, y alguien que te acompaña' }, icono: 'insights', fondo: 'claro' }, duracion: 4 },
    {
      id: 'gana',
      frases: [
        { es: 'Entonces, pastor, ¿qué gana tu iglesia?', clave: 'pregunta', pausa: 0.7 },
        { es: '*Decisiones con datos*, no con suposiciones.', clave: 'decisiones', pausa: 0.7 },
        { es: '*Nadie se pierde*: cada persona tiene quién la cuide, y ves a tiempo a quien se aleja.', clave: 'nadie', pausa: 0.7 },
        { es: '*Líderes que rinden cuentas*, sin papeles, y sin perseguir a nadie por su reporte.', clave: 'lideres', pausa: 0.7 },
        { es: 'Y todo conectado: la asistencia, los cursos y el servicio mueven la misma ruta de cada persona.', clave: 'conectado' },
      ],
      entrada: 0.5, cola: 1.0,
    },
    {
      id: 'acompana',
      frases: [
        { es: 'Y no lo haces solo.', clave: 'solo', pausa: 0.6 },
        { es: 'Al empezar, Kingdom te da una *ruta de arranque*, paso a paso, para acomodarlo a tu iglesia.', clave: 'arranque', pausa: 0.6 },
        { es: 'En la Ayuda está la Escuela Kingdom, con lecciones y videos cortos para cada líder.', clave: 'escuela', pausa: 0.6 },
        { es: 'Y nuestro equipo ve cómo avanza tu iglesia, y te acompaña a mejorar tus procesos.', clave: 'equipo', pausa: 0.8 },
        { es: 'Porque la meta no es usar una app. Es cuidar mejor a cada persona, y *poder verlo*.', clave: 'meta' },
      ],
      entrada: 0.5, cola: 1.4,
    },
  ],
};
