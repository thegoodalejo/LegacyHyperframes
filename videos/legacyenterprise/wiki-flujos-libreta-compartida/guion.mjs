// Guion del tutorial «Una sola libreta para todos los módulos» (fuente: LegacyEnterprise frontend/src/ayuda/<idioma>/flujos/libreta-compartida.md, W4.3).
// Cada escena usa un tramo de la grabación real (tools/ayuda/escenas/flujos/libreta-compartida.mjs → pasos.json). `desde` = índice del paso.
export default {
  "articulo": "flujos/libreta-compartida",
  "modulo": "base",
  "titulo": {
    "es": "Una sola libreta para todos los módulos",
    "en": "One address book for every module"
  },
  "siguiente": {
    "es": "De WhatsApp a una cita",
    "en": "From WhatsApp to an appointment"
  },
  "escenas": [
    {
      "tramo": "crm",
      "llamada": {
        "es": "Perfil",
        "en": "Profile"
      },
      "frases": [
        {
          "es": "Tu sede tiene una sola libreta. Este perfil es el mismo en el CRM, en Comunicaciones y en la Agenda.",
          "en": "Your branch has a single address book. This profile is the same in the CRM, Communications and Scheduling."
        },
        {
          "desde": 2,
          "es": "Cada módulo le suma sus tarjetas: oportunidades y ventas, conversaciones de WhatsApp, citas y el portal.",
          "en": "Each module adds its cards: opportunities and sales, WhatsApp conversations, appointments and the portal."
        }
      ]
    },
    {
      "tramo": "bandeja",
      "llamada": {
        "es": "Bandeja",
        "en": "Inbox"
      },
      "frases": [
        {
          "es": "En la bandeja, el panel muestra los mismos datos, etiquetas y notas. Una nota escrita aquí aparece en el perfil.",
          "en": "In the inbox, the panel shows the same details, tags and notes. A note written here shows on the profile."
        }
      ]
    },
    {
      "tramo": "agenda",
      "llamada": {
        "es": "Agenda",
        "en": "Scheduling"
      },
      "frases": [
        {
          "es": "Y desde la Agenda, el mismo perfil con sus citas. Lo que alguien cambia en un módulo, los demás lo ven al instante.",
          "en": "And from Scheduling, the same profile with its appointments. What someone changes in one module, the others see right away."
        }
      ]
    }
  ]
};
