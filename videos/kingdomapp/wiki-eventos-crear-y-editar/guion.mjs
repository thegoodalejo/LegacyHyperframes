// Guion del tutorial «Crear, editar o inactivar un evento» (fuente: KingdomApp frontend-v2/src/ayuda/<idioma>/eventos/crear-y-editar.md).
// Cada escena usa un tramo de la grabación real (KingdomApp tools/ayuda/escenas/eventos/crear-y-editar.mjs → pasos.json). Cada frase es un
// subtítulo y un audio; `desde` = índice del paso de pasos.json en que la frase empieza (no antes), para que la voz vaya con lo que se ve.
// `voz` (opcional) = el texto que se lee cuando la pronunciación lo pide; si falta, se lee el texto sin comillas.
// No inventar funciones ni números: todo sale del artículo, y la app se recorrió con la escena de captura (Kingdom Demo).
export default {
  articulo: 'eventos/crear-y-editar',
  seccion: 'eventos',
  titulo: { es: 'Crear, editar o inactivar un evento', en: 'Create, edit or deactivate an event' },
  siguiente: { es: 'Ver mis eventos y su ficha', en: 'See my events and their details' },
  escenas: [
    {
      tramo: 'categoria',
      llamada: { es: '¿Qué evento vas a crear?', en: 'What kind of event are you creating?' },
      frases: [
        { es: 'En este video vas a crear una casa de paz en Eventos: su categoría, horario, ubicación y responsables.',
          en: 'In this video you will create a house of peace in Events: its category, schedule, location and leaders.' },
        { es: 'Lo hace quien coordina Eventos o el administrador, con al menos una categoría activa.',
          en: 'Whoever coordinates Events or the administrator can do it, with at least one active category.' },
        { es: 'Cada categoría dice qué pide, por ejemplo «Pide la dirección» o «Pide la hora».',
          en: 'Each category says what it requires, for example “Address required” or “Time required”.' },
        { desde: 2, es: 'Toca la categoría que quieres. Aquí, «Casa de paz».',
          en: 'Tap the category you want. Here, “House of peace”.' },
      ],
    },
    {
      tramo: 'nombre',
      llamada: { es: 'Nombre', en: 'Name' },
      frases: [
        { desde: 3, es: 'Escribe el «Nombre». Así lo verá toda la iglesia.',
          en: 'Type the “Name”. This is how the whole church will see it.' },
      ],
    },
    {
      tramo: 'cuando',
      llamada: { es: 'Cuándo', en: 'When' },
      frases: [
        { desde: 4, es: 'En «Cuándo», toca los días en que se reúne.',
          en: 'In “When”, tap the days it meets.' },
        { desde: 5, es: 'Pon la «Hora». Debajo ves cómo quedó, por ejemplo «Los martes».',
          en: 'Set the “Time”. Below you see how it reads, for example “Tuesdays”.' },
      ],
    },
    {
      tramo: 'donde',
      llamada: { es: 'Dónde', en: 'Where' },
      frases: [
        { desde: 7, es: 'En «Dónde», toca «Poner en el mapa».',
          en: 'In “Where”, tap “Place on the map”.' },
        { desde: 8, es: 'Busca la dirección o mueve el mapa hasta dejar el pin en el lugar.',
          en: 'Search for the address or move the map until the pin is on the place.' },
        { desde: 10, es: 'Toca «Usar esta ubicación».',
          en: 'Tap “Use this location”.' },
        { es: 'En «Complemento» va el apartamento, la casa o una referencia.',
          en: '“Details” is for the apartment, the house or a landmark.' },
      ],
    },
    {
      tramo: 'responsables',
      llamada: { es: 'Responsables', en: 'Leaders' },
      frases: [
        { desde: 11, es: 'En «Responsables», toca «Agregar un responsable» y busca a quien lo lidera.',
          en: 'In “Leaders”, tap “Add a leader” and search for who leads it.' },
        { desde: 12, es: 'Elígelo de la lista. Se necesita mínimo uno, y puedes agregar hasta doce.',
          en: 'Pick them from the list. You need at least one, and you can add up to twelve.' },
        { desde: 14, es: 'Para reportar, cada responsable necesita cuenta de servidor. Si alguno no la tiene, la app te lo avisa.',
          en: 'To report, each leader needs a server account. If one does not have it, the app warns you.' },
        { desde: 15, es: 'La «Red» queda la de sus responsables; con «Elegir otra red» la cambias.',
          en: 'The “Network” is the one of its leaders; with “Choose another network” you change it.' },
        { es: 'Si quieres, escribe la «Descripción» y sube la «Portada».',
          en: 'If you want, write the “Description” and upload the “Cover”.' },
      ],
    },
    {
      tramo: 'guardar',
      llamada: { es: 'Guardar', en: 'Save' },
      frases: [
        { desde: 17, es: 'Toca «Guardar», y el evento queda creado.',
          en: 'Tap “Save”, and the event is created.' },
      ],
    },
    {
      tramo: 'inactivar',
      llamada: { es: 'Inactivar', en: 'Deactivate' },
      frases: [
        { desde: 18, es: 'Para inactivarlo, abre su ficha, toca «Más acciones» y luego «Inactivar».',
          en: 'To deactivate it, open its details, tap “More actions” and then “Deactivate”.' },
        { desde: 20, es: 'Revisa «Dónde se usa». Inactivarlo no borra nada de eso.',
          en: 'Check “Where it is used”. Deactivating it does not delete any of that.' },
        { es: 'Escribe el «Motivo» o toca uno de los frecuentes, y toca «Inactivar».',
          en: 'Write the “Reason” or tap one of the common ones, and tap “Deactivate”.' },
        { es: 'El evento sale de la lista de activos y su historia queda. Para volver a usarlo, toca «Reactivar» en su ficha.',
          en: 'The event leaves the active list and its history stays. To use it again, tap “Reactivate” in its details.' },
        { es: 'Para cambiar algo, abre su ficha y toca «Editar». Todo lo demás está en el artículo de la ayuda.',
          en: 'To change something, open its details and tap “Edit”. Everything else is in the help article.' },
      ],
    },
  ],
};
