// Guion del tutorial «Recordatorios automáticos de citas» (fuente: LegacyEnterprise frontend/src/ayuda/<idioma>/flujos/recordatorios-de-citas.md, W4.3).
// Cada escena usa un tramo de la grabación real (tools/ayuda/escenas/flujos/recordatorios-de-citas.mjs → pasos.json). `desde` = índice del paso.
export default {
  "articulo": "flujos/recordatorios-de-citas",
  "modulo": "agenda",
  "titulo": {
    "es": "Recordatorios automáticos de citas",
    "en": "Automatic appointment reminders"
  },
  "siguiente": {
    "es": "Metas que avisan a tus clientes",
    "en": "Goals that notify your clients"
  },
  "escenas": [
    {
      "tramo": "atajos",
      "llamada": {
        "es": "WhatsApp",
        "en": "WhatsApp"
      },
      "frases": [
        {
          "es": "Con la Agenda y Comunicaciones, las citas se avisan solas. En los Ajustes de la agenda, la pestaña WhatsApp.",
          "en": "With Scheduling and Communications, appointments announce themselves. In the Calendar settings, the WhatsApp tab."
        },
        {
          "desde": 3,
          "es": "Los atajos crean cada aviso con el cuándo y el a quién listos: recordatorios, confirmación, cambios de hora, cancelaciones.",
          "en": "Shortcuts create each notice with the when and the who ready: reminders, confirmation, time changes, cancellations."
        }
      ]
    },
    {
      "tramo": "automatizacion",
      "llamada": {
        "es": "Automatizaciones",
        "en": "Automations"
      },
      "frases": [
        {
          "es": "Cada aviso es una automatización de Comunicaciones. Al encenderla ves el costo y lo confirmas.",
          "en": "Each notice is a Communications automation. When you turn it on you see the cost and confirm it."
        }
      ]
    },
    {
      "tramo": "mensaje",
      "llamada": {
        "es": "Plantilla",
        "en": "Template"
      },
      "frases": [
        {
          "es": "El mensaje es una plantilla aprobada con los datos de la cita. Si lleva botones, confirmar o cancelar cambia la cita sola.",
          "en": "The message is an approved template with the appointment's data. If it has buttons, confirming or cancelling changes the appointment on its own."
        }
      ]
    }
  ]
};
