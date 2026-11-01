// Guion de la muestra del Tipo Recurso (formato en ../README.md → «Tipo Recurso (v1.2)»). node ../_herramientas/recurso.mjs preparar --idioma es
export default {
  slug: 'muestra-recurso',
  titulo: { es: 'Así se ve *un recurso* de Kingdom' },
  descripcion: { es: 'Muestra del formato Recursos de Kingdom: intro, capítulo, una idea con voz al ritmo de la música y el cierre.' },
  siguiente: { es: 'El siguiente recurso de la serie' },
  llamado: 'compartir',
  contacto: 'whatsapp',
  // Para el publicador de Plataforma → Recursos (opcionales): a quién va y el texto de WhatsApp, con {enlace} donde va el enlace.
  para: ['pastores', 'lideres'],
  mensaje: { es: 'Así se ve un Recurso de Kingdom: {enlace}' },
  // Muestra corta: la salida de la pista arranca en el 78,05 para que se oigan la entrada del bajo y su pico (18,05 y 20 → segundos 18 y 20 del video).
  musica: { salida: 78.05 },
  escenas: [
    { id: 'cap-1', capitulo: { numero: '1', titulo: { es: 'Una *persona*, una historia' }, icono: 'person' }, duracion: 4 },
    {
      id: 'personas',
      frases: [
        { es: 'Cada persona que llega a tu iglesia tiene un *nombre* y una *historia*.' },
        { es: 'Aquí la vemos como un punto de luz que se une a los demás.', pausa: 0.8 },
        { es: 'Así se ven los recursos de Kingdom: ideas claras, al *ritmo* de la música.' },
      ],
      minimo: 12,
      // El punto dorado aparece en T.pulso(palabra «persona» − 0,25) (compositions/personas.html): el sonido, en el mismo instante.
      sonidos: [{ sonido: 'aparicion', frase: 0, palabra: 1, desfase: -0.25, alPulso: true }],
    },
  ],
};
