// Guion del tutorial «Entrar por primera vez» (fuente: LegacyEnterprise frontend/src/ayuda/<idioma>/empieza/entrar-por-primera-vez.md).
// Cada escena usa un tramo de la grabación real (tools/ayuda/escenas/empieza/entrar-por-primera-vez.mjs → pasos.json). Cada frase es un
// subtítulo y un audio; `desde` = índice del paso de pasos.json en que la frase empieza (no antes), para que la voz vaya con lo que se ve.
// `voz` (opcional) = el texto que se lee cuando la pronunciación lo pide; si falta, se lee el texto sin comillas.
// No inventar funciones ni números: todo sale del artículo, y la app se recorrió con la escena de captura.
export default {
  articulo: 'empieza/entrar-por-primera-vez',
  modulo: 'base',
  titulo: { es: 'Entrar por primera vez', en: 'Signing in for the first time' },
  siguiente: { es: 'Roles y qué puede hacer cada uno', en: 'Roles and what each one can do' },
  escenas: [
    {
      tramo: 'entrar',
      llamada: { es: 'Continuar con Google', en: 'Continue with Google' },
      frases: [
        { es: 'En este video vas a entrar a la app por primera vez y a darle acceso a una persona nueva de tu equipo.',
          en: "In this video you'll sign in to the app for the first time and give a new team member access." },
        { es: 'Para entrar necesitas una cuenta de Google y el código de tu sede, que te da tu administrador.',
          en: 'To sign in you need a Google account and your branch code, which your administrator gives you.' },
        { desde: 2, es: 'Toca «Continuar con Google» y elige tu cuenta.', en: 'Tap "Continue with Google" and pick your account.' },
      ],
    },
    {
      tramo: 'codigo',
      llamada: { es: 'Código de la sede', en: 'Branch code' },
      frases: [
        { es: 'La primera vez, la app te pide el código de tu sede.', en: 'The first time, the app asks for your branch code.' },
        { desde: 4, es: 'Escríbelo y toca «Unirme a la sede».', en: 'Type it and tap "Join branch".' },
        { es: 'Si abriste el enlace o el QR, el código ya viene escrito.', en: 'If you opened the link or the QR, the code is already filled in.' },
      ],
    },
    {
      tramo: 'pendiente',
      llamada: { es: 'Tu acceso está pendiente', en: 'Your access is pending' },
      frases: [
        { es: 'Ya estás en la sede, pero tu acceso queda pendiente hasta que un administrador te asigne un rol y tus módulos.',
          en: "You're in the branch now, but your access stays pending until an administrator assigns you a role and your modules." },
      ],
    },
    {
      tramo: 'invitar',
      llamada: { es: 'Invitar', en: 'Invite' },
      frases: [
        { es: 'Ahora, del lado del administrador.', en: "Now, on the administrator's side." },
        { desde: 9, es: 'En «Usuarios», el botón «Invitar» muestra el código de la sede, su QR y «Copiar enlace».',
          en: 'In "Users", the "Invite" button shows the branch code, its QR and "Copy link".' },
        { es: 'Compártelo por donde prefieras.', en: 'Share it however you like.' },
      ],
    },
    {
      tramo: 'aprobar',
      llamada: { es: 'Editar acceso', en: 'Edit access' },
      frases: [
        { es: 'Quien se une aparece como «Pendiente de aprobación».', en: 'New members show up as "Pending approval".' },
        { desde: 13, es: 'Toca «Editar acceso», elige su rol y marca los módulos que va a usar.',
          en: 'Tap "Edit access", choose their role and check the modules they will use.' },
        { desde: 17, es: 'Deja encendido «Acceso activo» y guarda.', en: 'Leave "Access enabled" on and save.' },
      ],
    },
    {
      tramo: 'listo',
      llamada: { es: 'Bienvenida', en: 'Welcome' },
      frases: [
        { es: 'Cuando la persona vuelve a abrir la app, la bienvenida le muestra su rol y sus módulos.',
          en: 'When they open the app again, the welcome shows their role and their modules.' },
        { desde: 22, es: 'Toca «Empezar» y en Inicio ya ve sus módulos, cada uno con sus primeros pasos.',
          en: 'They tap "Get started" and their modules appear on Home, each with its first steps.' },
        { es: 'Si ves un mensaje que no esperabas, revisa «Problemas comunes» en este artículo de la Ayuda.',
          en: 'If you see a message you did not expect, check "Common problems" in this Help article.' },
      ],
    },
  ],
};
