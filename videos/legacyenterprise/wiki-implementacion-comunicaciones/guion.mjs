// Guion del tutorial «Poner en marcha Comunicaciones» (fuente: LegacyEnterprise frontend/src/ayuda/<idioma>/implementacion/comunicaciones.md).
// Cada escena usa un tramo de la grabación real (tools/ayuda/escenas/implementacion/comunicaciones.mjs → pasos.json). `desde` = índice del paso.
export default {
  articulo: 'implementacion/comunicaciones',
  modulo: 'comunicaciones',
  titulo: { es: 'Poner en marcha Comunicaciones', en: 'Setting up Communications' },
  siguiente: { es: 'Poner en marcha la Agenda', en: 'Setting up Scheduling' },
  escenas: [
    {
      tramo: 'ajustes',
      llamada: { es: 'Ajustes', en: 'Settings' },
      frases: [
        { es: 'Antes de empezar, tu asesor de la app conecta tu número de WhatsApp y carga tus créditos.',
          en: 'Before you start, your app advisor connects your WhatsApp number and loads your credits.' },
        { desde: 1, es: 'En los Ajustes: la bolsa de créditos, las palabras con que el cliente pide un asesor y qué hacer si el chatbot no entiende.',
          en: 'In Settings: the credit wallet, the words a client uses to ask for an agent and what to do if the chatbot doesn\'t understand.' },
        { desde: 2, es: 'Y los mensajes al pasar a un asesor y al cerrar la conversación.',
          en: 'And the messages when handing over to an agent and when closing the conversation.' },
      ],
    },
    {
      tramo: 'respuestas',
      llamada: { es: 'Respuestas de equipo', en: 'Team quick replies' },
      frases: [
        { es: 'Las respuestas de equipo son los textos que todos usan con la barra en la bandeja: horarios, precios, dirección.',
          en: 'Team replies are the texts everyone uses with the slash in the inbox: hours, prices, address.' },
      ],
    },
    {
      tramo: 'flujo',
      llamada: { es: 'Chatbot', en: 'Chatbot' },
      frases: [
        { es: 'Tu primer flujo del chatbot nace con un menú de ejemplo. Cambia los textos por los tuyos y elige sus palabras de activación.',
          en: 'Your first chatbot flow starts with a sample menu. Replace the texts with yours and pick its trigger words.' },
        { desde: 12, es: 'Con «Probar» lo recorres como un cliente, sin enviar nada. Cuando funcione, enciéndelo.',
          en: 'With "Test" you go through it like a client, without sending anything. When it works, turn it on.' },
      ],
    },
    {
      tramo: 'plantillas',
      llamada: { es: 'Plantillas', en: 'Templates' },
      frases: [
        { es: 'Las plantillas de WhatsApp sirven para escribir primero, como un recordatorio. Meta las revisa y decide su categoría.',
          en: 'WhatsApp templates are for writing first, like a reminder. Meta reviews them and sets their category.' },
      ],
    },
    {
      tramo: 'creditos',
      llamada: { es: 'Créditos', en: 'Credits' },
      frases: [
        { es: 'En Créditos ves el saldo y lo que gasta cada envío. Responder dentro de las 24 horas no gasta créditos.',
          en: 'In Credits you see the balance and what each send uses. Replying within 24 hours doesn\'t use credits.' },
      ],
    },
    {
      tramo: 'bandeja',
      llamada: { es: 'Bandeja', en: 'Inbox' },
      frases: [
        { es: 'La prueba final: escribe hola a tu número desde un celular. El chatbot responde; escribe asesor y la conversación llega a la cola.',
          en: 'The final test: text hi to your number from a phone. The chatbot answers; text agent and the conversation reaches the queue.' },
        { es: 'Tómala y responde desde aquí.', en: 'Take it and reply from here.' },
      ],
    },
  ],
};
