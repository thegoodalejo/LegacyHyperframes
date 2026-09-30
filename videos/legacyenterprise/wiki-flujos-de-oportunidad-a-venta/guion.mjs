// Guion del tutorial «De oportunidad a venta» (fuente: LegacyEnterprise frontend/src/ayuda/<idioma>/flujos/de-oportunidad-a-venta.md, W4.3).
// Cada escena usa un tramo de la grabación real (tools/ayuda/escenas/flujos/de-oportunidad-a-venta.mjs → pasos.json). `desde` = índice del paso.
export default {
  "articulo": "flujos/de-oportunidad-a-venta",
  "modulo": "crm",
  "titulo": {
    "es": "De oportunidad a venta",
    "en": "From opportunity to sale"
  },
  "siguiente": {
    "es": "Recordatorios automáticos de citas",
    "en": "Automatic appointment reminders"
  },
  "escenas": [
    {
      "tramo": "ficha",
      "llamada": {
        "es": "Ficha",
        "en": "Record"
      },
      "frases": [
        {
          "es": "Una posible venta en tu embudo. Su ficha tiene la tarjeta «Citas», con «Agendar».",
          "en": "A possible sale in your funnel. Its record has the \"Appointments\" card, with \"Schedule\"."
        }
      ]
    },
    {
      "tramo": "agendar",
      "llamada": {
        "es": "Agendar",
        "en": "Schedule"
      },
      "frases": [
        {
          "es": "La cita nace ligada, con el cliente y el servicio que sugiere la etapa. Si el embudo lo tiene encendido, la etapa avanza sola.",
          "en": "The appointment is created linked, with the client and the service the stage suggests. If the funnel has it on, the stage moves on its own."
        }
      ]
    },
    {
      "tramo": "atender",
      "llamada": {
        "es": "¿Qué sigue?",
        "en": "What's next?"
      },
      "frases": [
        {
          "desde": 8,
          "es": "Al atender la cita, «¿Qué sigue?» te propone registrar la venta, agendar la siguiente o abrir otra posible venta.",
          "en": "When you attend the appointment, \"What's next?\" suggests registering the sale, booking the next one or opening another possible sale."
        }
      ]
    },
    {
      "tramo": "venta",
      "llamada": {
        "es": "Venta",
        "en": "Sale"
      },
      "frases": [
        {
          "es": "Y cuando la ganas, la venta queda ligada a su ficha. «Ver venta» la abre.",
          "en": "And when you win it, the sale is linked to its record. \"View sale\" opens it."
        }
      ]
    }
  ]
};
