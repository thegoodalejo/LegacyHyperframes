// Guion del tutorial «Poner en marcha el CRM» (fuente: LegacyEnterprise frontend/src/ayuda/<idioma>/implementacion/crm.md).
// Cada escena usa un tramo de la grabación real (tools/ayuda/escenas/implementacion/crm.mjs → pasos.json). `desde` = índice del paso.
export default {
  articulo: 'implementacion/crm',
  modulo: 'crm',
  titulo: { es: 'Poner en marcha el CRM', en: 'Setting up the CRM' },
  siguiente: { es: 'Poner en marcha Comunicaciones', en: 'Setting up Communications' },
  escenas: [
    {
      tramo: 'embudo',
      llamada: { es: 'Embudo', en: 'Funnel' },
      frases: [
        { es: 'Antes de configurar el CRM, ten a la mano las etapas reales de tu venta y tu lista de productos o servicios con sus códigos.',
          en: 'Before setting up the CRM, have the real stages of your sale and your list of products or services with their codes at hand.' },
        { desde: 2, es: 'En «Embudo», la moneda y las etapas: una por paso real de tu venta, con su probabilidad, y los motivos para ganar o perder.',
          en: 'In "Funnel", the currency and the stages: one per real step of your sale, with its probability, and the reasons to win or lose.' },
      ],
    },
    {
      tramo: 'catalogo',
      llamada: { es: 'Catálogo', en: 'Catalog' },
      frases: [
        { es: 'En «Catálogo», lo que vendes, con los mismos códigos de tu sistema de facturación. Así cada venta importada encuentra lo que vendiste.',
          en: 'In "Catalog", what you sell, with the same codes as your invoicing system. That way each imported sale finds what you sold.' },
      ],
    },
    {
      tramo: 'ventas',
      llamada: { es: 'Importar ventas', en: 'Import sales' },
      frases: [
        { es: 'Después, el historial de ventas: idealmente doce meses o más, que son la referencia de las metas.',
          en: 'Then, the sales history: ideally twelve months or more, the reference for your goals.' },
        { desde: 12, es: 'Revisa antes de importar. Cada mes cargas el archivo nuevo con la misma plantilla de columnas.',
          en: 'Review before importing. Each month you load the new file with the same column template.' },
      ],
    },
    {
      tramo: 'metas',
      llamada: { es: 'Metas', en: 'Goals' },
      frases: [
        { es: 'En «Métricas» decides qué se mide. En Metas, las del mes para la empresa y la sede.',
          en: 'In "Metrics" you decide what\'s measured. In Goals, the month\'s goals for the company and the branch.' },
        { desde: 20, es: '«Generar por…» crea las metas de tus organizaciones con su historial y un porcentaje de crecimiento.',
          en: '"Generate by…" creates your organizations\' goals from their history and a growth percentage.' },
      ],
    },
    {
      tramo: 'tablero',
      llamada: { es: 'Tablero', en: 'Board' },
      frases: [
        { es: 'Listo: tu equipo trabaja las oportunidades en el tablero, con tus etapas.',
          en: 'Done: your team works on opportunities on the board, with your stages.' },
        { es: 'Sigue con Comunicaciones, la Agenda o el Portal, según los módulos de tu sede.',
          en: 'Continue with Communications, Scheduling or the Portal, depending on your branch\'s modules.' },
      ],
    },
  ],
};
