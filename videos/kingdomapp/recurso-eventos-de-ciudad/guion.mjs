// Guion del Recurso 2 de la serie «Recursos»: Eventos de ciudad, sin perder a nadie (Eventos masivos y Comunicaciones).
// Formato en ../README.md → «Tipo Recurso (v1.2)». node ../_herramientas/recurso.mjs preparar --idioma es
// De dónde sale cada afirmación de la voz: SPEC.md (fuentes en KingdomApp docs/modulos/eventos-masivos.md, comunicaciones.md, eventos.md,
// testimonios.md, sitio/src/data/modulos.ts y la ayuda frontend-v2/src/ayuda/es/{eventos,comunicaciones}/). Nada inventado.
export default {
  slug: 'eventos-de-ciudad',
  titulo: { es: 'Eventos de *ciudad*, sin perder a nadie' },
  descripcion: {
    es: 'Cómo llevar un evento de ciudad con Eventos masivos y Comunicaciones: inscripción, boletas, ingreso, conteos, seguimiento y WhatsApp.',
  },
  siguiente: { es: 'La experiencia del nuevo' },
  llamado: 'acompanamiento',
  contacto: 'whatsapp',
  para: ['pastores', 'lideres'],
  mensaje: { es: 'Pastor, mira cómo llevar un evento de ciudad con Kingdom, sin perder a nadie: {enlace}' },
  escenas: [
    // ─── Apertura ───────────────────────────────────────────────────────────────────────────────────────────────────────────
    {
      id: 'gancho',
      frases: [
        { es: 'Pastor, piensa en una *cruzada* en tu ciudad.', pausa: 0.5 },
        { es: 'O en un congreso que traen *varias iglesias*.', pausa: 0.6 },
        { es: 'Miles de personas se inscriben durante meses, y muchas no son de tu iglesia.', pausa: 0.6 },
        { es: 'Llega el día, se llena el lugar, y después viene la pregunta de siempre.', pausa: 0.5 },
        { es: '¿Cómo no perder a *nadie*?', clave: 'nadie', pausa: 0.8, alPulso: true },
      ],
      entrada: 0.5,
      cola: 1,
      sonidos: [{ sonido: 'desliz', frase: 'nadie', palabra: 0, desfase: -0.2, alPulso: true }],
    },
    {
      id: 'promesa',
      frases: [
        { es: '¿Quién se inscribió, quién llegó, quién pasó al altar, y quién lo va a llamar después?', pausa: 0.7 },
        { es: 'Para eso existe *Eventos masivos*, un complemento del módulo Eventos de Kingdom.', clave: 'masivos', pausa: 0.5 },
        { es: 'Y lo acompaña *Comunicaciones*: el WhatsApp de tu iglesia, conectado a todo.', clave: 'comunicaciones', pausa: 0.6 },
        { es: 'Lo vamos a ver en cuatro momentos: antes, el día del evento, después, y la conversación que no se corta.', clave: 'momentos' },
      ],
      cola: 1,
      sonidos: [{ sonido: 'aparicion', frase: 'masivos', palabra: 3, desfase: -0.2, alPulso: true }],
    },

    // ─── 1. Antes del evento ───────────────────────────────────────────────────────────────────────────────────────────────
    {
      id: 'cap-1',
      capitulo: { numero: '1', titulo: { es: 'Antes del *evento*' }, bajada: { es: 'Que cualquiera se inscriba y tenga su boleta' }, icono: 'confirmation_number' },
      duracion: 4,
    },
    {
      id: 'inscripcion',
      frases: [
        { es: 'Todo empieza con la inscripción, y no hace falta tener una cuenta.', pausa: 0.6 },
        { es: 'La persona abre un *enlace*, escanea un *QR* impreso, o escribe la palabra del evento al *WhatsApp* de la iglesia.', clave: 'caminos', pausa: 0.6 },
        { es: 'Por cualquier camino responde las mismas preguntas, y queda anotado por dónde llegó.', pausa: 0.7 },
        { es: 'Quien no es de tu iglesia queda como *participante*: tiene su ficha, pero no llena tu Membresía.', clave: 'participante', pausa: 0.5 },
        { es: 'Y si ya es miembro, Kingdom lo reconoce por su teléfono y no lo duplica.' },
      ],
      cola: 0.9,
      estirable: true,
    },
    {
      id: 'boletas',
      frases: [
        { es: 'Cada inscrito recibe su *boleta*, con un código QR.', clave: 'boleta', pausa: 0.6 },
        { es: 'Hay tipos de boleta: General, VIP o la del staff, cada una con su color.', clave: 'tipos', pausa: 0.6 },
        { es: 'Una regla asigna el tipo según lo que la persona respondió: por ejemplo, los pastores en una boleta y los líderes en otra.', clave: 'regla', pausa: 0.7 },
        { es: 'Y la boleta le llega a su *WhatsApp*, dentro del horario de envío de la iglesia.', clave: 'whatsapp', pausa: 0.5 },
        { es: 'Si se inscribió por el chat, la recibe ahí mismo.' },
      ],
      cola: 0.9,
      sonidos: [{ sonido: 'aparicion', frase: 'boleta', palabra: 4, desfase: -0.25, alPulso: true }],
    },
    {
      id: 'servir',
      frases: [
        { es: 'Y para los que quieren ayudar, está *Quiero servir*.', pausa: 0.5 },
        { es: 'Un enlace propio, donde cada voluntario dice en qué quiere servir y de qué iglesia viene.', clave: 'enlace', pausa: 0.6 },
        { es: 'Tu equipo lo aprueba, elige su tipo de staff, y su boleta sale sola, válida todos los días del evento.', clave: 'aprueba' },
      ],
      cola: 1,
      sonidos: [{ sonido: 'confirmacion', frase: 'aprueba', palabra: 3, desfase: -0.1, alPulso: true }],
    },

    // ─── 2. El día del evento ─────────────────────────────────────────────────────────────────────────────────────────────
    {
      id: 'cap-2',
      capitulo: { numero: '2', titulo: { es: 'El día del *evento*' }, bajada: { es: 'Cada persona que entra, contada' }, icono: 'stadium' },
      duracion: 4,
    },
    {
      id: 'equipo',
      frases: [
        { es: 'El día del evento, cada persona de tu equipo sabe qué le toca.', pausa: 0.6 },
        { es: 'En el *equipo del evento*, cada una tiene su función: *ingreso*, *conteo* o *testimonios*.', clave: 'funciones', pausa: 0.6 },
        { es: 'Y actúa solo en ese evento, sin ver otras partes de Membresía.' },
      ],
      cola: 0.9,
    },
    {
      id: 'ingreso',
      frases: [
        { es: 'En la entrada se escanea el QR de cada boleta.', pausa: 0.5 },
        { es: 'Verde: bienvenido. Ámbar: ya entró hoy. Y cada ingreso queda como su asistencia de ese día.', clave: 'colores', pausa: 0.7 },
        { es: 'Si se cae la señal, se sigue escaneando: el celular guarda los ingresos y los envía solos cuando vuelve.', clave: 'senal', pausa: 0.6 },
        { es: 'Y quien llega sin boleta se inscribe ahí mismo, en la puerta.', clave: 'puerta' },
      ],
      cola: 0.9,
      estirable: true,
    },
    {
      id: 'manillas',
      frases: [
        { es: 'Si el evento usa *manillas*, cada persona recibe una en la muñeca, vinculada a su boleta.', clave: 'manilla', pausa: 0.6 },
        { es: 'Con ella, el equipo de conteo registra quién pasó al altar o quién aceptó a Cristo, sin hojas de papel.', clave: 'conteo', pausa: 0.6 },
        { es: 'Para el aforo se cuenta sin manilla: más uno, más cinco, más diez.', clave: 'aforo', pausa: 0.6 },
        { es: 'Y una etiqueta de Membresía puede marcar a quien se contó con su manilla, para darle seguimiento.', clave: 'etiqueta' },
      ],
      cola: 0.9,
    },
    {
      id: 'testimonios',
      frases: [
        { es: 'Cuando alguien quiere contar lo que Dios hizo, el equipo de testimonios escanea su manilla.', pausa: 0.6 },
        { es: 'Se abre su testimonio con la persona y el evento ya puestos: *antes*, *durante* y *después*.', clave: 'etapas', pausa: 0.6 },
        { es: 'Y si le falta, la persona *firma* ahí mismo, en el celular.', clave: 'firma' },
      ],
      cola: 1,
      sonidos: [{ sonido: 'confirmacion', frase: 'firma', palabra: 6, desfase: 1.0, alPulso: true }],
    },

    // ─── 3. Después ───────────────────────────────────────────────────────────────────────────────────────────────────────
    {
      id: 'cap-3',
      capitulo: { numero: '3', titulo: { es: 'Después, que *nadie* se pierda' }, bajada: { es: 'Cada persona nueva, con quien la siga' }, icono: 'route' },
      duracion: 4,
    },
    {
      id: 'ruta',
      frases: [
        { es: 'Aquí está el corazón de todo: la *ruta del evento*.', pausa: 0.6 },
        { es: 'A todos los inscritos les llegan los mensajes del evento: al registrarse, y unos días antes, con su boleta otra vez.', clave: 'mensajes', pausa: 0.6 },
        { es: 'Y cada participante nuevo se reparte entre los *llamadores*, que lo ven en su Mi seguimiento.', clave: 'llamadores', pausa: 0.6 },
        { es: 'Llaman, preguntan su interés y si necesita transporte o alojamiento, y dejan su reporte.', clave: 'reporte', pausa: 0.6 },
        { es: 'Quien se queda *pasa a la iglesia*: entra a una red, empieza su ruta de crecimiento, y queda listo para que alguien lo acompañe.', clave: 'pasa' },
      ],
      cola: 1,
      estirable: true,
      sonidos: [{ sonido: 'confirmacion', frase: 'pasa', palabra: 3, desfase: -0.1, alPulso: true }],
    },
    {
      id: 'reportes',
      frases: [
        { es: 'Y todo se puede *medir*.', pausa: 0.5 },
        { es: 'Los reportes del evento muestran cuántos se inscribieron cada día, por qué camino, con qué tipo de boleta, y cuántos entraron.', clave: 'fijos', pausa: 0.6 },
        { es: 'Puedes cruzar dos preguntas, como de dónde vienen y su rol, y guardar el reporte para volver a abrirlo.', clave: 'cruzar', pausa: 0.6 },
        { es: 'Y en *Envíos* ves cada boleta que salió: si llegó, si la leyeron y qué botón tocaron.', clave: 'envios' },
      ],
      cola: 1,
    },

    // ─── 4. Comunicaciones ────────────────────────────────────────────────────────────────────────────────────────────────
    {
      id: 'cap-4',
      capitulo: { numero: '4', titulo: { es: 'La conversación *no se corta*' }, bajada: { es: 'Comunicaciones, el WhatsApp de tu iglesia' }, icono: 'forum', fondo: 'claro' },
      duracion: 4,
    },
    {
      id: 'linea',
      frases: [
        { es: 'Todo esto vive en *Comunicaciones*: tu iglesia escribe desde su propio número de WhatsApp, con su nombre.', clave: 'numero', pausa: 0.5 },
        { es: 'Y te acompañamos a conectarlo.', pausa: 0.7 },
        { es: 'El *chatbot* responde las preguntas de siempre, a cualquier hora, e inscribe a quien escribe la palabra del evento.', clave: 'chatbot', pausa: 0.6 },
        { es: 'Cuando la persona pide hablar con alguien, la conversación pasa a la *bandeja*.', clave: 'bandeja', pausa: 0.5 },
        { es: 'Ahí tu equipo toma cada conversación y responde, sin compartir un solo celular.', clave: 'toma' },
      ],
      cola: 1,
      estirable: true,
    },
    {
      id: 'campanas',
      frases: [
        { es: 'Para invitar a escala están las *plantillas*: mensajes aprobados por WhatsApp, con sus datos y sus botones.', clave: 'plantillas', pausa: 0.6 },
        { es: 'Con ellas armas una *campaña*: eliges el público, por red, por etiquetas o los inscritos de un evento, y la envías ahora o la programas.', clave: 'campana', pausa: 0.6 },
        { es: 'Sale dentro del *horario de envío* de la iglesia: nada llega a medianoche.', clave: 'horario', pausa: 0.6 },
        { es: 'Y las *automatizaciones* envían solas: cuando llega alguien nuevo, un día antes de cada reunión o el día de su cumpleaños.', clave: 'auto', pausa: 0.6 },
        { es: 'Así tu iglesia invita, confirma y da seguimiento, sin depender de la memoria de nadie.', clave: 'asi' },
      ],
      cola: 1,
    },

    // ─── Resumen y acompañamiento ─────────────────────────────────────────────────────────────────────────────────────────
    {
      id: 'resultado',
      frases: [
        { es: 'Al final, pastor, esto es lo que tienes.', pausa: 0.6 },
        { es: 'Un evento de *ciudad* que se organiza con *pocas personas*.', clave: 'ciudad', pausa: 0.7, alPulso: true },
        { es: 'Cada asistente inscrito, con su boleta y medido en la entrada.', clave: 'medido', pausa: 0.5 },
        { es: 'Y cada persona nueva, con nombre, con su ruta y con alguien que la siga.', clave: 'seguido' },
      ],
      cola: 1.2,
      estirable: true,
      sonidos: [{ sonido: 'subida', frase: 'ciudad', palabra: 3, alPulso: true }],
    },
    {
      id: 'acompanamiento',
      frases: [
        { es: 'Y no lo haces solo: en Kingdom te acompañamos a mejorar los procesos de tu iglesia, también en tu próximo evento.', clave: 'acompanamos', pausa: 0.6 },
        { es: 'Escríbenos, y lo preparamos contigo.', clave: 'escribenos' },
      ],
      cola: 1.2,
    },
  ],
};
