// Guion del tutorial «El chatbot que agenda» (fuente: LegacyEnterprise frontend/src/ayuda/<idioma>/flujos/chatbot-que-agenda.md, W4.3).
// Cada escena usa un tramo de la grabación real (tools/ayuda/escenas/flujos/chatbot-que-agenda.mjs → pasos.json). `desde` = índice del paso.
export default {
  "articulo": "flujos/chatbot-que-agenda",
  "modulo": "comunicaciones",
  "titulo": {
    "es": "El chatbot que agenda",
    "en": "The chatbot that books"
  },
  "escenas": [
    {
      "tramo": "crear",
      "llamada": {
        "es": "Chatbot de citas",
        "en": "Appointments chatbot"
      },
      "frases": [
        {
          "es": "El chatbot puede agendar por WhatsApp a cualquier hora. En los Ajustes de la agenda, pestaña WhatsApp, «Crear el flujo de ejemplo».",
          "en": "The chatbot can book on WhatsApp at any hour. In the Calendar settings, WhatsApp tab, \"Create the sample flow\"."
        }
      ]
    },
    {
      "tramo": "editor",
      "llamada": {
        "es": "Agendar por WhatsApp",
        "en": "Book on WhatsApp"
      },
      "frases": [
        {
          "es": "Se crea el flujo «Agendar por WhatsApp», apagado. Sus listas muestran los servicios y las horas libres, con las reglas del portal.",
          "en": "The \"Book on WhatsApp\" flow is created, turned off. Its lists show the services and free times, with the portal's rules."
        }
      ]
    },
    {
      "tramo": "probar",
      "llamada": {
        "es": "Probar",
        "en": "Test"
      },
      "frases": [
        {
          "es": "Pruébalo como un cliente: agendar, ver sus citas o hablar con alguien.",
          "en": "Try it like a client: book, see their appointments or talk to someone."
        },
        {
          "desde": 15,
          "es": "Cuando funcione, enciéndelo. Las citas llegan a la Agenda como «Por WhatsApp».",
          "en": "When it works, turn it on. Appointments reach Scheduling as \"Via WhatsApp\"."
        }
      ]
    }
  ]
};
