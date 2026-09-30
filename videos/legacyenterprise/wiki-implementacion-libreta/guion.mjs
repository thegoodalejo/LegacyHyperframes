// Guion del tutorial «Poner en marcha la libreta» (fuente: LegacyEnterprise frontend/src/ayuda/<idioma>/implementacion/libreta.md).
// Cada escena usa un tramo de la grabación real (tools/ayuda/escenas/implementacion/libreta.mjs → pasos.json). `desde` = índice del paso.
export default {
  articulo: 'implementacion/libreta',
  modulo: 'implementacion',
  titulo: { es: 'Poner en marcha la libreta', en: 'Setting up the address book' },
  siguiente: { es: 'Poner en marcha el CRM', en: 'Setting up the CRM' },
  escenas: [
    {
      tramo: 'vocabulario',
      llamada: { es: 'Vocabulario', en: 'Vocabulary' },
      frases: [
        { es: 'La libreta es la misma en el CRM, en Comunicaciones y en la Agenda. Se configura una vez, en los Ajustes de cualquiera.',
          en: 'The address book is the same in the CRM, Communications and Scheduling. You set it up once, in the Settings of any of them.' },
        { desde: 1, es: 'En «Vocabulario», dale a cada cosa el nombre de tu negocio: pacientes, clientes, convenios. Hazlo antes de capacitar al equipo.',
          en: 'In "Vocabulary", give each thing your business\'s name: patients, clients, partners. Do it before training your team.' },
      ],
    },
    {
      tramo: 'campos',
      llamada: { es: 'Campos personalizados', en: 'Custom fields' },
      frases: [
        { es: 'En «Campos personalizados», los datos que de verdad usas de cada perfil. Pocos obligatorios: cada uno es un paso más.',
          en: 'In "Custom fields", the details you really use from each profile. Few required ones: each one is one more step.' },
      ],
    },
    {
      tramo: 'etiquetas',
      llamada: { es: 'Etiquetas', en: 'Tags' },
      frases: [
        { es: 'Las etiquetas, agrupadas por tema, sirven para filtrar, enviar campañas y armar automatizaciones.',
          en: 'Tags, grouped by topic, are for filtering, sending campaigns and building automations.' },
      ],
    },
    {
      tramo: 'roles',
      llamada: { es: 'Roles', en: 'Roles' },
      frases: [
        { es: 'Si le vendes a negocios, los roles dicen cómo se relaciona cada persona con su organización.',
          en: 'If you sell to businesses, roles say how each person relates to their organization.' },
      ],
    },
    {
      tramo: 'importar',
      llamada: { es: 'Importar', en: 'Import' },
      frases: [
        { es: 'Ahora, carga tu libreta. Primero las organizaciones y después las personas: así encuentran su vínculo.',
          en: 'Now load your address book. Organizations first, then people: that\'s how they find their link.' },
        { desde: 12, es: 'Elige el archivo de Excel o CSV. La app reconoce las columnas, y la plantilla se guarda para la próxima vez.',
          en: 'Choose the Excel or CSV file. The app recognizes the columns, and the template is saved for next time.' },
      ],
    },
    {
      tramo: 'revisar',
      llamada: { es: 'Revisar', en: 'Review' },
      frases: [
        { es: '«Revisar» lee todo el archivo sin guardar nada y te dice qué va a pasar y qué filas tienen error.',
          en: '"Review" reads the whole file without saving anything and tells you what will happen and which rows have errors.' },
        { es: 'Corrige lo que haga falta e importa. Cada importación se puede revertir.',
          en: 'Fix what\'s needed and import. Every import can be reverted.' },
      ],
    },
  ],
};
