// Guion del tutorial «Poner en marcha la sede» (fuente: LegacyEnterprise frontend/src/ayuda/<idioma>/implementacion/sede.md).
// Cada escena usa un tramo de la grabación real (tools/ayuda/escenas/implementacion/sede.mjs → pasos.json). `desde` = índice del paso de
// pasos.json en que la frase empieza. No inventar funciones ni números: todo sale de la guía.
export default {
  articulo: 'implementacion/sede',
  modulo: 'implementacion',
  titulo: { es: 'Poner en marcha la sede', en: 'Setting up the branch' },
  siguiente: { es: 'Poner en marcha la libreta', en: 'Setting up the address book' },
  escenas: [
    {
      tramo: 'inicio',
      llamada: { es: 'Puesta en marcha', en: 'Setup' },
      frases: [
        { es: 'En este video pones en marcha una sede nueva: la plantilla de tu negocio, tu equipo y sus accesos.',
          en: 'In this video you set up a new branch: your business template, your team and their access.' },
        { es: 'Como Administrador de sede, en Inicio tienes la puesta en marcha, con lo que sigue.',
          en: 'As the Branch administrator, Home shows Setup, with what comes next.' },
        { desde: 2, es: '«Continuar» abre la lista completa, por grupos. Cada paso se marca solo cuando está hecho.',
          en: '"Continue" opens the full list, in groups. Each step checks itself off when it\'s done.' },
      ],
    },
    {
      tramo: 'plantilla',
      llamada: { es: 'Plantillas', en: 'Templates' },
      frases: [
        { es: 'Primero, la plantilla de tu tipo de negocio, en la pestaña «Plantillas» de los Ajustes.',
          en: 'First, the template for your type of business, in the Settings "Templates" tab.' },
        { desde: 8, es: 'Agrega de una vez el vocabulario, los campos, las etiquetas, el embudo y los servicios. No borra nada de lo que ya tengas.',
          en: 'It adds the vocabulary, fields, tags, funnel and services in one go. It doesn\'t delete anything you already have.' },
      ],
    },
    {
      tramo: 'invitar',
      llamada: { es: 'Invitar', en: 'Invite' },
      frases: [
        { es: 'Después, tu equipo. En «Usuarios», un aviso dice quién espera acceso.',
          en: 'Next, your team. In "Users", a notice says who is waiting for access.' },
        { desde: 12, es: '«Invitar» muestra el código de la sede, su QR y «Copiar enlace». Compártelo con tu equipo.',
          en: '"Invite" shows the branch code, its QR and "Copy link". Share it with your team.' },
      ],
    },
    {
      tramo: 'aprobar',
      llamada: { es: 'Editar acceso', en: 'Edit access' },
      frases: [
        { es: 'Cuando alguien se une, te llega una notificación. Toca «Editar acceso».',
          en: 'When someone joins, you get a notification. Tap "Edit access".' },
        { desde: 16, es: 'Elige su rol: Nivel 1 para el trabajo diario, Nivel 2 para supervisar. Marca solo los módulos que va a usar y guarda.',
          en: 'Choose their role: Level 1 for daily work, Level 2 to supervise. Check only the modules they\'ll use and save.' },
      ],
    },
    {
      tramo: 'listo',
      llamada: { es: 'Puesta en marcha', en: 'Setup' },
      frases: [
        { es: 'De vuelta en la puesta en marcha, «Invita a tu equipo» ya está hecho.',
          en: 'Back in Setup, "Invite your team" is already done.' },
        { desde: 23, es: 'Sigue con la guía de cada módulo: el botón «Ver la guía» de cada grupo.',
          en: 'Continue with each module\'s guide: the "See the guide" button in each group.' },
      ],
    },
  ],
};
