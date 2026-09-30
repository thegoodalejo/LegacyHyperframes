// Guion del tutorial «Poner en marcha la Agenda» (fuente: LegacyEnterprise frontend/src/ayuda/<idioma>/implementacion/agenda.md).
// Cada escena usa un tramo de la grabación real (tools/ayuda/escenas/implementacion/agenda.mjs → pasos.json). `desde` = índice del paso.
export default {
  articulo: 'implementacion/agenda',
  modulo: 'agenda',
  titulo: { es: 'Poner en marcha la Agenda', en: 'Setting up Scheduling' },
  siguiente: { es: 'Poner en marcha el Portal', en: 'Setting up the Client portal' },
  escenas: [
    {
      tramo: 'recursos',
      llamada: { es: 'Recursos', en: 'Resources' },
      frases: [
        { es: 'Primero, quién o qué atiende: tus profesionales, cada uno con su usuario, las salas y los equipos.',
          en: 'First, who or what serves: your professionals, each with their user, the rooms and the equipment.' },
        { desde: 2, es: 'Cada recurso necesita su horario semanal. Sin horario no hay espacios libres para agendar.',
          en: 'Each resource needs its weekly hours. Without hours there are no free slots to book.' },
      ],
    },
    {
      tramo: 'servicios',
      llamada: { es: 'Servicios', en: 'Services' },
      frases: [
        { es: 'En cada servicio: la duración, el tiempo antes y después, la modalidad y quién lo presta.',
          en: 'On each service: the duration, the time before and after, the mode and who provides it.' },
        { desde: 8, es: 'Más abajo, si se repite y si el cliente lo puede pedir desde el portal.',
          en: 'Further down, whether it repeats and whether the client can request it from the portal.' },
      ],
    },
    {
      tramo: 'festivos',
      llamada: { es: 'Bloqueos y festivos', en: 'Blocks and holidays' },
      frases: [
        { es: 'Marca los festivos y los días que la sede no abre: no se ofrecen para agendar.',
          en: 'Mark holidays and the days the branch is closed: they aren\'t offered for booking.' },
      ],
    },
    {
      tramo: 'ajustes',
      llamada: { es: 'Ajustes', en: 'Settings' },
      frases: [
        { es: 'En Ajustes, el intervalo de la agenda, el aviso a quien atiende y la dirección de la sede que usan los mensajes.',
          en: 'In Settings, the booking interval, the notice to whoever serves and the branch address used by the messages.' },
      ],
    },
    {
      tramo: 'whatsapp',
      llamada: { es: 'WhatsApp', en: 'WhatsApp' },
      frases: [
        { es: 'Con Comunicaciones, aquí enciendes los recordatorios y las confirmaciones por WhatsApp.',
          en: 'With Communications, this is where you turn on WhatsApp reminders and confirmations.' },
      ],
    },
    {
      tramo: 'probar',
      llamada: { es: 'Buscar horario libre', en: 'Find a free time' },
      frases: [
        { es: 'Pruébala: en una cita nueva, elige un servicio y «Buscar horario libre» muestra las horas de quienes lo prestan.',
          en: 'Try it: in a new appointment, pick a service and "Find a free time" shows the times of those who provide it.' },
        { desde: 23, es: 'Si ofrece horas reales, tu agenda está lista.', en: 'If it offers real times, your schedule is ready.' },
      ],
    },
  ],
};
