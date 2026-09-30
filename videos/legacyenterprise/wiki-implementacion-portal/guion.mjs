// Guion del tutorial «Poner en marcha el Portal de clientes» (fuente: LegacyEnterprise frontend/src/ayuda/<idioma>/implementacion/portal.md).
// Cada escena usa un tramo de la grabación real (tools/ayuda/escenas/implementacion/portal.mjs → pasos.json). `desde` = índice del paso.
export default {
  articulo: 'implementacion/portal',
  modulo: 'portal',
  titulo: { es: 'Poner en marcha el Portal', en: 'Setting up the Client portal' },
  siguiente: { es: 'Qué ve el cliente en el portal', en: 'What the client sees in the portal' },
  escenas: [
    {
      tramo: 'ajustes',
      llamada: { es: 'Ajustes del portal', en: 'Portal settings' },
      frases: [
        { es: 'El enlace del portal de tu empresa lo configura tu asesor de la app. Lo demás lo decides aquí.',
          en: 'Your app advisor sets up your company\'s portal link. You decide the rest here.' },
        { desde: 1, es: 'Enciende el portal y elige qué secciones ve el cliente y qué ve cada rol de lo de su organización.',
          en: 'Turn the portal on and choose which sections the client sees and what each role sees of their organization.' },
        { desde: 2, es: 'Con el CRM, qué metas y embudos ve, y cómo se llama cada etapa para el cliente.',
          en: 'With the CRM, which goals and funnels they see, and what each stage is called for the client.' },
      ],
    },
    {
      tramo: 'terminos',
      llamada: { es: 'Términos', en: 'Terms' },
      frases: [
        { es: 'Tus términos y tu bienvenida. Si cambias los términos, cada cliente los vuelve a aceptar.',
          en: 'Your terms and your welcome. If you change the terms, each client accepts them again.' },
      ],
    },
    {
      tramo: 'servicios',
      llamada: { es: 'Servicios', en: 'Services' },
      frases: [
        { es: 'Con la Agenda, en cada servicio decides si el cliente lo puede pedir, con cuánta anticipación y si necesita tu aprobación.',
          en: 'With Scheduling, on each service you decide whether the client can request it, how far ahead and whether it needs your approval.' },
      ],
    },
    {
      tramo: 'acceso',
      llamada: { es: 'Portal de clientes', en: 'Client portal' },
      frases: [
        { es: 'Solo entra quien está en tu libreta, con el mismo correo de su cuenta de Google.',
          en: 'Only people in your address book can sign in, with the same email as their Google account.' },
        { desde: 13, es: 'En su perfil, la tarjeta del portal tiene su código y su QR. La primera vez lo usa; después entra solo con su correo.',
          en: 'On their profile, the portal card has their code and QR. They use it the first time; after that they sign in with their email.' },
      ],
    },
    {
      tramo: 'accesos',
      llamada: { es: 'Accesos', en: 'Access' },
      frases: [
        { es: 'En Accesos ves quién ya entró; en Solicitudes, lo que piden los clientes.',
          en: 'In Access you see who has signed in; in Requests, what clients ask for.' },
      ],
    },
  ],
};
