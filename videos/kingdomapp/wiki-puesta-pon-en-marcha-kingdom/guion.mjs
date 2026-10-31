// Guion del tutorial «Pon en marcha una iglesia celular» (fuente: KingdomApp frontend-v2/src/ayuda/<idioma>/puesta/pon-en-marcha-kingdom.md y
// puesta/ruta-de-arranque.md). Cada escena usa un tramo de la grabación real (KingdomApp tools/ayuda/escenas/puesta/pon-en-marcha-kingdom.mjs →
// pasos.json). Cada frase es un subtítulo y un audio; `desde` = índice del paso de pasos.json en que la frase empieza (no antes), para que la voz
// vaya con lo que se ve. `voz` (opcional) = el texto que se lee cuando la pronunciación lo pide; si falta, se lee el texto sin comillas.
// No inventar funciones ni números: todo sale de los artículos, y la app se recorrió con la escena de captura (Kingdom Demo).
//
// Índices de pasos.json: 5 «Ver mi ruta» · 8 «Responder» · 9-13 las cinco respuestas · 15 «Guardar y seguir» · 16 «Tu iglesia» ·
// 18 «Revisa las palabras» · 20 «Están bien así» · 21 «Hacerlo ahora» (marca) · 22 «Personalizar» · 23 el color · 24 «Guardar» ·
// 25 de vuelta en la ruta (celebración) · 29 «Seguir» · 30 «Tu gente» · 32 «Hacerlo ahora» (redes) · 33 «Crear Red» · 34 «Nombre» ·
// 35 «Quiénes la dirigen» · 36 elegir a la persona · 37 «Guardar» · 38 de vuelta en la ruta · 40 «Tu equipo» · 43 lo que sigue.
export default {
  articulo: 'puesta/pon-en-marcha-kingdom',
  seccion: 'puesta',
  titulo: { es: 'Pon en marcha una iglesia celular', en: 'Get a cell church started' },
  siguiente: { es: 'Responder el cuestionario y recorrer tu ruta de arranque', en: 'Answer the questionnaire and go through your start route' },
  escenas: [
    {
      tramo: 'abrir',
      llamada: { es: 'Tu arranque', en: 'Your start' },
      frases: [
        { es: 'En este video vas a poner en marcha una iglesia celular con «Tu arranque», la ruta de Kingdom que te dice qué hacer y en qué orden.',
          en: 'In this video you will get a cell church started with “Your start”, the Kingdom route that tells you what to do and in what order.' },
        { desde: 5, es: 'Lo hace el administrador de la iglesia. En «Servir», toca «Ver mi ruta» en la tarjeta «Tu arranque».',
          en: 'The church administrator does it. In “Serve”, tap “See my route” on the “Your start” card.' },
        { desde: 7, es: 'Arriba, un aviso te pide responder el cuestionario. Debajo están las etapas de tu ruta.',
          en: 'At the top, a notice asks you to answer the questionnaire. Below are the stages of your route.' },
      ],
    },
    {
      tramo: 'cuestionario',
      llamada: { es: 'Cuéntanos cómo es tu iglesia', en: 'Tell us about your church' },
      frases: [
        { desde: 8, es: 'Toca «Responder»: son cinco preguntas.',
          en: 'Tap “Answer”: there are five questions.' },
        { desde: 9, es: 'Tu modelo de iglesia: elige «Celular».',
          en: 'Your kind of church: choose “Cell church”.' },
        { desde: 10, es: 'Cuántas personas son: «Hasta 300».',
          en: 'How many people: “Up to 300”.' },
        { desde: 11, es: 'Lo primero que quieres lograr: «Ordenar mi membresía».',
          en: 'What you want to achieve first: “Organize my membership”.' },
        { desde: 12, es: 'Si tu iglesia tiene cobertura: «Es independiente».',
          en: 'Whether your church has a covering: “It is independent”.' },
        { desde: 13, es: 'Y si trabajas con un equipo: «Con un equipo».',
          en: 'And whether you work with a team: “With a team”.' },
        { desde: 15, es: 'Toca «Guardar y seguir». Con tus respuestas, la app ordena tu ruta, y puedes cambiarlas cuando quieras.',
          en: 'Tap “Save and continue”. With your answers, the app orders your route, and you can change them whenever you want.' },
      ],
    },
    {
      tramo: 'iglesia',
      llamada: { es: 'Tu iglesia', en: 'Your church' },
      frases: [
        { desde: 16, es: 'La primera etapa es «Tu iglesia»: que Kingdom lleve tu nombre, tu marca y tus palabras.',
          en: 'The first stage is “Your church”: Kingdom carries your name, your brand and your words.' },
        { desde: 17, es: 'Cada paso dice qué es y por qué importa. Los que ya cumples muestran «Hecho».',
          en: 'Each step says what it is and why it matters. The ones you already meet show “Done”.' },
      ],
    },
    {
      tramo: 'palabras',
      llamada: { es: 'Revisa las palabras', en: 'Review the words' },
      frases: [
        { desde: 18, es: 'Con una iglesia celular, la app no te propone palabras distintas a las que ya usas.',
          en: 'With a cell church, the app does not suggest words different from the ones you already use.' },
        { desde: 20, es: 'Toca «Están bien así» y el paso queda hecho.',
          en: 'Tap “They are fine” and the step is done.' },
      ],
    },
    {
      tramo: 'marca',
      llamada: { es: 'Pon tu logo y tus colores', en: 'Add your logo and colors' },
      frases: [
        { desde: 21, es: 'Hagamos un paso de verdad: toca «Hacerlo ahora».',
          en: 'Let us do a real step: tap “Do it now”.' },
        { desde: 22, es: 'Toca «Personalizar».',
          en: 'Tap “Customize”.' },
        { desde: 23, es: 'Elige tu color.',
          en: 'Choose your color.' },
        { desde: 24, es: 'Toca «Guardar».',
          en: 'Tap “Save”.' },
      ],
    },
    {
      tramo: 'hecho',
      llamada: { es: 'Hecho', en: 'Done' },
      frases: [
        { desde: 25, es: 'Al volver a la ruta, la app ya sabe que lo hiciste.',
          en: 'When you return to the route, the app already knows you did it.' },
        { desde: 26, es: 'Completaste «Tu iglesia»: Kingdom lo celebra y te dice cuál sigue.',
          en: 'You completed “Your church”: Kingdom celebrates and tells you which stage comes next.' },
      ],
    },
    {
      tramo: 'gente',
      llamada: { es: 'Tu gente', en: 'Your people' },
      frases: [
        { desde: 30, es: 'La segunda etapa es «Tu gente»: cargar a tus personas, organizarlas en redes y darles líderes.',
          en: 'The second stage is “Your people”: add your people, organize them into networks and give them leaders.' },
        { desde: 31, es: 'Los pasos se marcan solos. Solo «Conoce la ruta de crecimiento» lo marcas tú, con «Ya lo vi».',
          en: 'Steps check themselves off. Only “Learn the growth path” is yours to tap, with “I saw it”.' },
      ],
    },
    {
      tramo: 'red',
      llamada: { es: 'Organiza a tu gente en redes', en: 'Organize your people into networks' },
      frases: [
        { desde: 32, es: 'Hagamos este: toca «Hacerlo ahora».',
          en: 'Let us do this one: tap “Do it now”.' },
        { desde: 33, es: 'Toca «Crear Red».',
          en: 'Tap “Create Network”.' },
        { desde: 34, es: 'Ponle un «Nombre».',
          en: 'Give it a “Name”.' },
        { desde: 35, es: 'En «Quiénes la dirigen», busca a la persona que la lidera.',
          en: 'In “Who leads it”, search for the person who leads it.' },
        { desde: 36, es: 'Elígela de la lista.',
          en: 'Pick them from the list.' },
        { desde: 37, es: 'Toca «Guardar».',
          en: 'Tap “Save”.' },
      ],
    },
    {
      tramo: 'marcado',
      llamada: { es: 'Hecho', en: 'Done' },
      frases: [
        { desde: 38, es: 'Al volver a la ruta, «Organiza a tu gente en redes» y «Asigna a los líderes» ya aparecen con «Hecho».',
          en: 'Back on the route, “Organize your people into networks” and “Assign the leaders” already show “Done”.' },
        { es: 'Se marcaron solos: la red existe y tiene un líder.',
          en: 'They checked themselves off: the network exists and it has a leader.' },
      ],
    },
    {
      tramo: 'equipo',
      llamada: { es: 'Tu equipo', en: 'Your team' },
      frases: [
        { desde: 40, es: 'La tercera etapa es «Tu equipo»: invitar a quienes te ayudan y darles el acceso que necesitan.',
          en: 'The third stage is “Your team”: invite those who help you and give them the access they need.' },
        { desde: 41, es: 'Pide invitar a alguien, darle permisos, elegir quién atiende las dudas e instalar la app.',
          en: 'It asks you to invite someone, give them permissions, choose who answers questions and install the app.' },
        { desde: 42, es: 'Kingdom te recomienda terminar antes la etapa anterior, pero puedes hacer estos pasos cuando quieras.',
          en: 'Kingdom recommends finishing the previous stage first, but you can do these steps whenever you want.' },
      ],
    },
    {
      tramo: 'sigue',
      llamada: { es: 'Ya conozco Kingdom', en: 'I already know Kingdom' },
      frases: [
        { desde: 43, es: 'Después vienen las etapas de los módulos que tiene tu iglesia, como Eventos y Academia.',
          en: 'After those come the stages for the modules your church has, such as Events and Academy.' },
        { es: 'Si ya conoces Kingdom, toca «Ya conozco Kingdom» y haz las etapas en el orden que quieras: nada se bloquea.',
          en: 'If you already know Kingdom, tap “I already know Kingdom” and do the stages in any order: nothing is blocked.' },
        { es: 'La tarjeta «Tu arranque» se va sola cuando no queda nada por hacer. Para volver a tu ruta, entra a «Ayuda» y toca «Tu ruta de arranque».',
          en: 'The “Your start” card leaves on its own when nothing is left to do. To get back to your route, go to “Help” and tap “Your getting-started route”.' },
        { es: 'Cada paso tiene su «Cómo se hace», que abre su artículo en la ayuda.',
          en: 'Each step has its “How to do it”, which opens its article in the help.' },
      ],
    },
  ],
};
