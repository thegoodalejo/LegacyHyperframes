// Guion del tutorial «De WhatsApp a una cita» (fuente: LegacyEnterprise frontend/src/ayuda/<idioma>/flujos/de-whatsapp-a-una-cita.md, W4.3).
// Cada escena usa un tramo de la grabación real (tools/ayuda/escenas/flujos/de-whatsapp-a-una-cita.mjs → pasos.json). `desde` = índice del paso.
export default {
  "articulo": "flujos/de-whatsapp-a-una-cita",
  "modulo": "comunicaciones",
  "titulo": {
    "es": "De WhatsApp a una cita",
    "en": "From WhatsApp to an appointment"
  },
  "siguiente": {
    "es": "De oportunidad a venta",
    "en": "From opportunity to sale"
  },
  "escenas": [
    {
      "tramo": "bandeja",
      "llamada": {
        "es": "Bandeja",
        "en": "Inbox"
      },
      "frases": [
        {
          "es": "Un cliente pide una cita por WhatsApp. Toma la conversación: el panel muestra sus datos, sus notas y sus citas.",
          "en": "A client asks for an appointment on WhatsApp. Take the conversation: the panel shows their details, notes and appointments."
        }
      ]
    },
    {
      "tramo": "perfil",
      "llamada": {
        "es": "Ver perfil",
        "en": "Open profile"
      },
      "frases": [
        {
          "es": "«Ver perfil» abre su perfil. En la tarjeta «Citas», el botón «Agendar».",
          "en": "\"Open profile\" opens their profile. On the \"Appointments\" card, the \"Schedule\" button."
        }
      ]
    },
    {
      "tramo": "agendar",
      "llamada": {
        "es": "Buscar horario libre",
        "en": "Find a free time"
      },
      "frases": [
        {
          "es": "La cita nueva ya trae al cliente. Elige el servicio y «Buscar horario libre» te da horas reales para ofrecerle.",
          "en": "The new appointment already has the client. Pick the service, and \"Find a free time\" gives you real times to offer."
        },
        {
          "desde": 10,
          "es": "Confírmale por el chat: dentro de las 24 horas no gasta créditos. Y si prefieres que lo haga solo, está el chatbot de citas.",
          "en": "Confirm it in the chat: within 24 hours it doesn't use credits. And if you'd rather it happen on its own, there's the appointments chatbot."
        }
      ]
    }
  ]
};
