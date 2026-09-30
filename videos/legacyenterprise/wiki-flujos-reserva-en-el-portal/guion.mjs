// Guion del tutorial «El cliente reserva en el portal» (fuente: LegacyEnterprise frontend/src/ayuda/<idioma>/flujos/reserva-en-el-portal.md, W4.3).
// Cada escena usa un tramo de la grabación real (tools/ayuda/escenas/flujos/reserva-en-el-portal.mjs → pasos.json). `desde` = índice del paso.
export default {
  "articulo": "flujos/reserva-en-el-portal",
  "modulo": "portal",
  "titulo": {
    "es": "El cliente reserva en el portal",
    "en": "The client books in the portal"
  },
  "siguiente": {
    "es": "Servicios que se repiten",
    "en": "Recurring services"
  },
  "escenas": [
    {
      "tramo": "reglas",
      "llamada": {
        "es": "Servicios",
        "en": "Services"
      },
      "frases": [
        {
          "desde": 3,
          "es": "Tú decides qué se puede pedir desde el portal: en cada servicio, si se puede reservar, con qué anticipación y si necesita tu aprobación.",
          "en": "You decide what can be requested from the portal: on each service, whether it can be booked, how far ahead and whether it needs your approval."
        }
      ]
    },
    {
      "tramo": "solicitud",
      "llamada": {
        "es": "Solicitada",
        "en": "Requested"
      },
      "frases": [
        {
          "es": "La cita que pide el cliente llega a la Agenda. Con aprobación, queda «Solicitada»: acéptala o recházala.",
          "en": "The appointment the client requests reaches Scheduling. With approval, it's \"Requested\": accept or decline it."
        },
        {
          "es": "El cliente recibe el aviso en su app, y puede confirmar, cancelar o cambiar la hora hasta el plazo del servicio.",
          "en": "The client gets the notice in their app, and can confirm, cancel or change the time up to the service's deadline."
        }
      ]
    }
  ]
};
