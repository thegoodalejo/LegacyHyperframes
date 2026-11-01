/* Kit de identidad de Kingdom v1.2 · Tipo Recurso (decisión 239 de KingdomApp): los tiempos de una escena, para animar con la voz y la música
   sin números a mano. Lo carga el host (index.html que genera _herramientas/recurso.mjs) en su <head>, después de GSAP:
     <script src="identidad/recurso.js"></script>
   Dentro de la escena (compositions/<id>.html), al EMPEZAR su <script> y fuera de cualquier callback (la variable es de la escena que corre):
     const T = KRecurso.tiempos(window);   // «window» dentro de la escena es la suya (sus variables), no la del host
     T.duracion                         duración de la escena (s); todo en segundos relativos al inicio de la escena
     T.frases[i]  / T.frase('clave')    { id, clave, texto, inicio, fin, palabras: [{ texto, inicio, fin }] } (las palabras son estimadas, ±0,15 s)
     T.palabra(i, j)                    la palabra j de la frase i (o por clave: T.palabra('clave', j))
     T.pulso(t) / T.compas(t)           el primer pulso (0,5 s) o compás (2 s) de la música en t o después
     T.pulsoAntes(t)                    el último pulso en t o antes
     T.golpes                           golpes fuertes de la música dentro de la escena
     T.salida(d = 0.5)                  cuándo empezar la salida para terminar justo al final (duracion − d)
     T.reparto(n, desde, hasta)         n instantes repartidos en pulsos entre desde y hasta (para listas que entran una a una)
   Sin la variable (la composición abierta sola) usa el `default` declarado en la composición. No se edita por video. */
(function () {
  const PULSO = 0.5;
  const COMPAS = 2;
  const r3 = (n) => Math.round(n * 1000) / 1000;

  function envolver(t) {
    const frases = (t.frases || []).map((f, i) => ({ ...f, n: i, palabras: f.palabras || [] }));
    const desfase = Number(t.compas0 || 0); // segundo de la escena donde cae el primer compás (0, 0,5, 1 o 1,5)
    const T = {
      duracion: Number(t.duracion || 0),
      inicioAbs: Number(t.inicioAbs || 0),
      idioma: t.idioma || 'es',
      frases,
      golpes: t.golpes || [],
      compas0: desfase,
      frase(k) {
        const f = typeof k === 'number' ? frases[k] : frases.find((x) => x.clave === k || x.id === k);
        if (!f) throw new Error(`KRecurso: la escena no tiene la frase «${k}»`);
        return f;
      },
      palabra(k, j) {
        const f = T.frase(k);
        const p = f.palabras[Math.max(0, Math.min(j, f.palabras.length - 1))];
        return p || { texto: f.texto, inicio: f.inicio, fin: f.fin };
      },
      pulso(x) {
        return r3(Math.ceil(x / PULSO - 1e-6) * PULSO);
      },
      pulsoAntes(x) {
        return r3(Math.floor(x / PULSO + 1e-6) * PULSO);
      },
      compas(x) {
        return r3(desfase + Math.ceil((x - desfase) / COMPAS - 1e-6) * COMPAS);
      },
      salida(d) {
        return r3(T.duracion - (d === undefined ? 0.5 : d));
      },
      reparto(n, desde, hasta) {
        const a = T.pulso(desde);
        const b = Math.max(a, T.pulsoAntes(hasta));
        const pasos = Math.max(1, Math.round((b - a) / PULSO));
        const out = [];
        for (let i = 0; i < n; i++) out.push(r3(a + Math.round((pasos * i) / Math.max(1, n - 1 || 1)) * PULSO));
        return n === 1 ? [a] : out;
      },
    };
    return T;
  }

  window.KRecurso = {
    version: 'v1.2',
    // w: el «window» de la escena (dentro de una subcomposición HyperFrames lo cambia por uno con las variables de esa instancia; el
    // window del host devolvería las del video entero). También acepta el objeto de variables o el JSON de «tiempos».
    tiempos(w) {
      let v = {};
      if (typeof w === 'string') v = { tiempos: w };
      else if (w && w.__hyperframes && w.__hyperframes.getVariables) v = w.__hyperframes.getVariables() || {};
      else if (w && typeof w === 'object') v = w;
      let t = null;
      try {
        t = typeof v.tiempos === 'string' ? JSON.parse(v.tiempos) : v.tiempos;
      } catch (e) {
        t = null;
      }
      return envolver(t || { duracion: 6, frases: [] });
    },
  };
})();
