// Guion del tutorial «Servicios que se repiten» (fuente: LegacyEnterprise frontend/src/ayuda/<idioma>/flujos/servicios-que-se-repiten.md, W4.3).
// Cada escena usa un tramo de la grabación real (tools/ayuda/escenas/flujos/servicios-que-se-repiten.mjs → pasos.json). `desde` = índice del paso.
export default {
  "articulo": "flujos/servicios-que-se-repiten",
  "modulo": "agenda",
  "titulo": {
    "es": "Servicios que se repiten",
    "en": "Recurring services"
  },
  "siguiente": {
    "es": "El chatbot que agenda",
    "en": "The chatbot that books"
  },
  "escenas": [
    {
      "tramo": "servicio",
      "llamada": {
        "es": "Servicio periódico",
        "en": "Recurring service"
      },
      "frases": [
        {
          "desde": 3,
          "es": "Marca el servicio como periódico: cada cuánto se repite y con cuánta anticipación se avisa.",
          "en": "Mark the service as recurring: how often it repeats and how far ahead it's announced."
        }
      ]
    },
    {
      "tramo": "lista",
      "llamada": {
        "es": "Por reagendar",
        "en": "To rebook"
      },
      "frases": [
        {
          "es": "La app calcula cuándo le toca a cada cliente. En «Por reagendar», tu equipo ve a quién ya le tocó y a quién le toca pronto.",
          "en": "The app works out when it's due for each client. In \"To rebook\", your team sees whose is overdue and whose is coming up."
        }
      ]
    },
    {
      "tramo": "agendar",
      "llamada": {
        "es": "Agendar",
        "en": "Book"
      },
      "frases": [
        {
          "es": "«Agendar» abre la cita con el cliente, el servicio y el día. Con el portal y WhatsApp, el cliente también se entera solo.",
          "en": "\"Book\" opens the appointment with the client, the service and the day. With the portal and WhatsApp, the client also finds out on their own."
        }
      ]
    }
  ]
};
