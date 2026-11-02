// Recurso para líderes 1 (sección «Para líderes», departamento Afirmación): «Afirmando la cosecha con Kingdom» (decisión 241;
// formato en ../README.md → «Tipo Recurso», variante «Para líderes» del kit v1.3: la app recreada en HTML, fiel a v2).
// node ../_herramientas/recurso.mjs preparar --idioma es
// Fuentes de cada afirmación: SPEC.md (KingdomApp frontend-v2/src/ayuda/es/** y docs/modulos/*.md). La estrategia sale de un libro sobre
// acogida que el dueño entregó; por decisión suya NO se nombra, y sus ideas van en palabras propias (sin su anécdota ni citas).
export default {
  slug: 'afirmando-la-cosecha',
  titulo: { es: 'Afirmando la *cosecha* con Kingdom' },
  ceja: { es: 'Recursos · Para líderes' }, // SPEC → intro: la ceja de la sección «Para líderes»
  descripcion: {
    es: 'Para el líder de afirmación o consolidación: cómo recibir, repartir, llamar y acompañar a cada persona nueva con Kingdom, y medir que se quede, crezca y se multiplique.',
  },
  llamado: 'acompanamiento',
  contacto: 'whatsapp',
  para: ['lideres'],
  seccion: 'lideres',
  departamento: 'afirmacion',
  mensaje: {
    es: 'Para tu equipo de afirmación: mira cómo afirmar la cosecha con Kingdom, paso a paso. {enlace}',
  },
  escenas: [
    // ── Apertura ────────────────────────────────────────────────────────────────────────────────────────────────────────────────
    {
      id: 'gancho',
      frases: [
        { es: 'El domingo llegaron doce personas *nuevas* a tu iglesia.', clave: 'doce', pausa: 0.6 },
        { es: 'Pasaron al altar, dejaron sus datos y volvieron a casa.', clave: 'altar', pausa: 0.6 },
        { es: 'La pregunta es: ¿cuántas *vuelven*?', clave: 'vuelven', pausa: 0.9 },
        { es: 'La cosecha casi nunca se pierde en el altar. Se pierde el *lunes*, cuando nadie llama.', clave: 'lunes', pausa: 0.8 },
        { es: 'Si diriges *afirmación*, o consolidación, este video es para ti.', clave: 'afirmacion', pausa: 0.5 },
        { es: 'Vas a ver cómo usar Kingdom para que cada persona nueva se *quede*, crezca y se multiplique.', clave: 'quede', pausa: 0.5 },
      ],
      entrada: 0.5,
      cola: 0.8,
      sonidos: [{ sonido: 'aparicion', frase: 0, palabra: 4, desfase: -0.2, alPulso: true }],
    },
    // ── Capítulo 1: el camino del nuevo (estrategia) ────────────────────────────────────────────────────────────────────────────
    {
      id: 'cap-1',
      capitulo: { numero: '1', titulo: { es: 'El camino del *nuevo*' }, bajada: { es: 'La acogida no termina el domingo' }, icono: 'route', fondo: 'noche' },
      duracion: 4,
    },
    {
      id: 'camino',
      frases: [
        { es: 'Antes de llegar, una persona ya te está *conociendo*: por una invitación, por las redes, por un evento.', clave: 'conociendo', pausa: 0.5 },
        { es: 'Después decide si este lugar es para ella.', clave: 'decide', pausa: 0.5 },
        { es: 'Luego *vive* el domingo: cómo la reciben, cómo la miran, si se siente en casa.', clave: 'vive', pausa: 0.5 },
        { es: 'Y al final dice *sí*: esta es mi iglesia.', clave: 'si', pausa: 0.7 },
        { es: 'Entre vivir el domingo y decir sí hay un tramo que es *tuyo*.', clave: 'tuyo', pausa: 0.7 },
        { es: 'La acogida no es un momento: es un *camino*. Y no termina cuando se acaba el servicio.', clave: 'camino', pausa: 0.6 },
        { es: 'Además, quien decide si tu iglesia es acogedora no son los de adentro: es la persona que *llega*.', clave: 'llega', pausa: 0.5 },
      ],
      entrada: 0.5,
      cola: 0.8,
      estirable: true,
    },
    // ── Capítulo 2: registrar a cada persona ────────────────────────────────────────────────────────────────────────────────────
    {
      id: 'cap-2',
      capitulo: { numero: '2', titulo: { es: 'Que nadie se quede *sin nombre*' }, bajada: { es: 'Registrar a cada persona que llega' }, icono: 'person_add', fondo: 'noche' },
      duracion: 4,
    },
    {
      id: 'registro',
      frases: [
        { es: 'No puedes acompañar a alguien si no sabes que llegó. Por eso todo empieza con un *registro*.', clave: 'registro', pausa: 0.5 },
        { es: 'Proyecta el *QR de bienvenida*: la persona lo escanea y se registra sola, desde su celular.', clave: 'qr', pausa: 0.5 },
        { es: 'O tu equipo de recepción la registra en «*Nueva persona*», incluso sin señal.', clave: 'nueva', pausa: 0.5 },
        { es: 'Nombres, teléfono y «*Cómo llegó*»: por una casa de paz, por una invitación, por un evento.', clave: 'como', pausa: 0.5 },
        { es: 'Si sabes quién la *invitó*, anótalo también.', clave: 'invito', pausa: 0.5 },
        { es: 'Y si ya estaba registrada, Kingdom te avisa: registras su *llegada*, sin crear otra ficha.', clave: 'llegada', pausa: 0.5 },
        { es: 'Desde ese momento empieza su ruta, con el primer paso: la *llamada de bienvenida*.', clave: 'llamada', pausa: 0.5 },
      ],
      entrada: 0.5,
      cola: 0.8,
      estirable: true,
      sonidos: [{ sonido: 'confirmacion', frase: 5, palabra: 10, desfase: -0.15, alPulso: true }],
    },
    // ── Capítulo 3: repartir ────────────────────────────────────────────────────────────────────────────────────────────────────
    {
      id: 'cap-3',
      capitulo: { numero: '3', titulo: { es: 'Repartir la *cosecha*' }, bajada: { es: 'Que nadie se quede sin quien lo acompañe' }, icono: 'diversity_3', fondo: 'noche' },
      duracion: 4,
    },
    {
      id: 'repartir',
      frases: [
        { es: 'Tú no tienes que llamar a todos. Tu trabajo es que *nadie* se quede sin alguien que lo acompañe.', clave: 'nadie', pausa: 0.6 },
        { es: 'En Membresía, abre «*Coordinar*». En «Nuevos» están quienes todavía no tienen acompañante, con cómo y cuándo llegaron.', clave: 'coordinar', pausa: 0.5 },
        { es: 'Toca «*Repartir*», y Kingdom los reparte parejo entre tu equipo, según el cupo de cada uno.', clave: 'repartir', pausa: 0.6 },
        { es: 'O toca «Asignar» para elegir tú quién acompaña a cada uno.', clave: 'asignar', pausa: 0.5 },
        { es: 'Cada acompañante recibe un aviso en su celular: «Alguien nuevo para *acompañar*».', clave: 'aviso', pausa: 0.6 },
        { es: 'En «Quienes acompañan» ves la carga de cada uno y sus pendientes en *rojo*.', clave: 'carga', pausa: 0.5 },
        { es: 'Y en «Resumen», las cifras del día: quién está en rojo y a quién no han llamado *a tiempo*.', clave: 'resumen', pausa: 0.5 },
      ],
      entrada: 0.5,
      cola: 0.8,
      sonidos: [{ sonido: 'aparicion', frase: 4, palabra: 4, desfase: -0.2, alPulso: true }],
    },
    // ── Capítulo 4: la llamada ──────────────────────────────────────────────────────────────────────────────────────────────────
    {
      id: 'cap-4',
      capitulo: { numero: '4', titulo: { es: 'La llamada que *abraza*' }, bajada: { es: 'El primer contacto, a tiempo y en persona' }, icono: 'call', fondo: 'noche' },
      duracion: 4,
    },
    {
      id: 'llamada',
      frases: [
        { es: 'Un mensaje automático informa. Una *llamada* a tiempo, de una persona real, abraza.', clave: 'llamada', pausa: 0.7 },
        { es: 'Cada acompañante abre «*Mi seguimiento*» y ve a quienes acompaña, con el paso que les toca.', clave: 'seguimiento', pausa: 0.5 },
        { es: 'El semáforo le dice si va *a tiempo*, si está por vencer o si ya se venció.', clave: 'tiempo', pausa: 0.5 },
        { es: 'Llama desde la tarjeta. Al colgar, toca «*Marcar cumplido*» y llena el reporte: cómo fue, la petición de oración y las observaciones.', clave: 'marcar', pausa: 0.5 },
        { es: 'Si no contestó, toca «Solo registrar el *intento*»: queda constancia y lo vuelves a intentar.', clave: 'intento', pausa: 0.5 },
        { es: 'Kingdom te dice cuál es el *siguiente* paso, y tú lo aceptas o eliges otro.', clave: 'siguiente', pausa: 0.6 },
        { es: 'Y tu iglesia puede armar su propio *formulario* para esa llamada, con las preguntas que ustedes usan.', clave: 'formulario', pausa: 0.5 },
      ],
      entrada: 0.5,
      cola: 0.8,
      estirable: true,
      sonidos: [{ sonido: 'confirmacion', frase: 5, palabra: 6, desfase: -0.15, alPulso: true }],
    },
    {
      id: 'consejos',
      frases: [
        { es: 'Para que la llamada abrace: preséntate y da *gracias* por su visita.', clave: 'gracias', pausa: 0.5 },
        { es: 'Pregúntale cómo se sintió, *escucha* más de lo que hablas y, si te lo permite, ora por ella.', clave: 'escucha', pausa: 0.5 },
        { es: 'Sé breve, no hagas preguntas personales e invítala a algo *concreto*: la próxima reunión, una casa de paz.', clave: 'concreto', pausa: 0.6 },
        { es: 'Si tu iglesia tiene Comunicaciones, el mensaje de *bienvenida* por WhatsApp sale solo, una hora después de que llega.', clave: 'bienvenida', pausa: 0.5 },
        { es: 'Y si hubo una visita, una consejería o una oración aparte, regístrala como *actividad extra* en su ficha.', clave: 'extra', pausa: 0.5 },
      ],
      entrada: 0.5,
      cola: 0.8,
    },
    // ── Capítulo 5: de visitante a familia ──────────────────────────────────────────────────────────────────────────────────────
    {
      id: 'cap-5',
      capitulo: { numero: '5', titulo: { es: 'De visitante a *familia*' }, bajada: { es: 'Un camino claro, paso a paso' }, icono: 'diversity_1', fondo: 'noche' },
      duracion: 4,
    },
    {
      id: 'ruta',
      frases: [
        { es: 'Afirmar no es una llamada: es acompañar a la persona hasta que se *conecta*.', clave: 'conecta', pausa: 0.6 },
        { es: 'Por eso cada persona tiene su *ruta de crecimiento*: llega a la iglesia, se conecta con una casa de paz, empieza las clases de la visión, empieza a servir.', clave: 'ruta', pausa: 0.5 },
        { es: 'Muchos pasos se cumplen *solos*: cuando asiste a su casa de paz, cuando empieza un curso, cuando se une a un equipo.', clave: 'solos', pausa: 0.5 },
        { es: 'Con «Casa de paz, ¿cuál?» ves las más *cercanas* y le asignas una.', clave: 'cercanas', pausa: 0.5 },
        { es: 'Un paso cumplido puede darle un *logro*. Y cuando cumple sus objetivos, Kingdom lo celebra: «¡Se conectó con la iglesia!».', clave: 'logro', pausa: 0.6 },
      ],
      entrada: 0.5,
      cola: 0.8,
      estirable: true,
      sonidos: [{ sonido: 'subida', frase: 4, palabra: 15, desfase: -0.2, alPulso: true }],
    },
    {
      id: 'semaforo',
      frases: [
        { es: 'Y si alguien se enfría, lo ves *a tiempo*.', clave: 'tiempo', pausa: 0.5 },
        { es: 'El *semáforo de actividad* pasa de verde a amarillo cuando lleva días sin venir, sin ir a clase, sin abrir la app.', clave: 'semaforo', pausa: 0.6 },
        { es: 'Amarillo no es una cifra: es una persona que necesita otra *llamada*.', clave: 'llamada', pausa: 0.5 },
      ],
      entrada: 0.5,
      cola: 0.8,
    },
    // ── Capítulo 6: medir ───────────────────────────────────────────────────────────────────────────────────────────────────────
    {
      id: 'cap-6',
      capitulo: { numero: '6', titulo: { es: 'Lo que se mide, *se cuida*' }, bajada: { es: 'Saber qué funciona, con datos' }, icono: 'monitoring', fondo: 'noche' },
      duracion: 4,
    },
    {
      id: 'tableros',
      frases: [
        { es: 'Un buen proceso de acogida no se adivina: se *mide*.', clave: 'mide', pausa: 0.5 },
        { es: 'En «*Tableros*», la vista «Ruta» te muestra el embudo: cuántos iniciaron cada paso, cuántos lo cumplieron y en cuántos días.', clave: 'tableros', pausa: 0.5 },
        { es: 'Ahí ves dónde se te está quedando la gente. Y en «*Estancados*», quiénes llevan su paso vencido.', clave: 'estancados', pausa: 0.5 },
        { es: 'La vista «Personas» te dice por dónde llegan los nuevos: así sabes qué *funciona*.', clave: 'funciona', pausa: 0.5 },
        { es: 'Con los filtros armas tu lista: llegaron este mes y todavía están «*Sin red*».', clave: 'filtros', pausa: 0.5 },
        { es: 'Descargas el tablero en PDF o Excel y lo llevas a la *reunión* de tu equipo.', clave: 'reunion', pausa: 0.6 },
        { es: 'Y pregúntale a los nuevos cómo se sintieron: su opinión vale más que la *nuestra*.', clave: 'opinion', pausa: 0.5 },
      ],
      entrada: 0.5,
      cola: 0.8,
      estirable: true,
    },
    // ── Capítulo 7: multiplicar ─────────────────────────────────────────────────────────────────────────────────────────────────
    {
      id: 'cap-7',
      capitulo: { numero: '7', titulo: { es: 'Afirmados que *afirman*' }, bajada: { es: 'Crecimiento y multiplicación' }, icono: 'all_inclusive', fondo: 'noche' },
      duracion: 4,
    },
    {
      id: 'multiplicar',
      frases: [
        { es: 'El fruto de afirmar no es una lista llena: es una iglesia que crece y se *multiplica*.', clave: 'multiplica', pausa: 0.6 },
        { es: 'Quien hoy fue afirmado, mañana puede *acompañar* a otro.', clave: 'acompanar', pausa: 0.5 },
        { es: 'Cuando se une a tu equipo, lo sumas a la bolsa de acompañantes, con su *cupo*.', clave: 'cupo', pausa: 0.5 },
        { es: 'Cada acompañante puede ver *solo* a quienes acompaña: la información de cada persona queda cuidada.', clave: 'solo', pausa: 0.5 },
        { es: 'Y si en tu iglesia se llaman *consolidadores*, Kingdom usa esa palabra.', clave: 'consolidadores', pausa: 0.6 },
        { es: 'Así, la cosecha de un domingo se convierte en la *familia* de mañana.', clave: 'familia', pausa: 0.6 },
      ],
      entrada: 0.5,
      cola: 0.8,
    },
    {
      id: 'resumen',
      frases: [
        { es: 'Afirmar la cosecha con Kingdom es *simple*.', clave: 'simple', pausa: 0.6 },
        { es: 'Registra a cada persona que llega. Reparte, para que nadie se quede solo.', clave: 'r1', pausa: 0.4 },
        { es: 'Llama a tiempo y marca su paso. Acompáñala hasta que se conecte.', clave: 'r2', pausa: 0.4 },
        { es: 'Mide, ajusta y vuelve a empezar.', clave: 'r3', pausa: 0.7 },
        { es: 'Porque cada persona que llega es alguien que Dios te *confió*.', clave: 'confio', pausa: 0.6 },
      ],
      entrada: 0.5,
      cola: 0.8,
      estirable: true,
    },
    {
      id: 'llamado',
      frases: [
        { es: 'En Kingdom te *acompañamos* a poner en marcha tu proceso de afirmación.', clave: 'acompanamos', pausa: 0.5 },
        { es: 'Escríbenos por WhatsApp.', clave: 'whatsapp', pausa: 0.5 },
      ],
      entrada: 0.5,
      cola: 1.0,
    },
  ],
};
