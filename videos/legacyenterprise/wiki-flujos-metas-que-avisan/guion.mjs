// Guion del tutorial «Metas que avisan a tus clientes» (fuente: LegacyEnterprise frontend/src/ayuda/<idioma>/flujos/metas-que-avisan.md, W4.3).
// Cada escena usa un tramo de la grabación real (tools/ayuda/escenas/flujos/metas-que-avisan.mjs → pasos.json). `desde` = índice del paso.
export default {
  "articulo": "flujos/metas-que-avisan",
  "modulo": "crm",
  "titulo": {
    "es": "Metas que avisan a tus clientes",
    "en": "Goals that notify your clients"
  },
  "siguiente": {
    "es": "El cliente reserva en el portal",
    "en": "The client books in the portal"
  },
  "escenas": [
    {
      "tramo": "metas",
      "llamada": {
        "es": "Metas",
        "en": "Goals"
      },
      "frases": [
        {
          "es": "Las metas de tus clientes, en Metas, con su avance y el ritmo esperado.",
          "en": "Your clients' goals, in Goals, with their progress and expected pace."
        }
      ]
    },
    {
      "tramo": "fuente",
      "llamada": {
        "es": "Metas de organizaciones",
        "en": "Organization goals"
      },
      "frases": [
        {
          "es": "En una automatización nueva, la fuente «Metas de organizaciones».",
          "en": "In a new automation, the \"Organization goals\" source."
        },
        {
          "desde": 6,
          "es": "Elige la métrica, a quién le escribes y los filtros: por ejemplo, las atrasadas.",
          "en": "Choose the metric, who you write to and the filters: for example, the ones behind."
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
          "es": "El mensaje lleva el avance de cada meta en el idioma de la plantilla, y sale cuando tú digas.",
          "en": "The message carries each goal's progress in the template's language, and goes out whenever you say."
        }
      ]
    }
  ]
};
