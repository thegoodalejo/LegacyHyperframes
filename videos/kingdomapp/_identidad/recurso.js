/* Kit de identidad de Kingdom v1.3 · Tipo Recurso (decisión 239 de KingdomApp): los tiempos de una escena, para animar con la voz y la música
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
   Sin la variable (la composición abierta sola) usa el `default` declarado en la composición. No se edita por video.
   v1.3 (decisión 241, variante «Para líderes»): KRecurso.app, las ayudas para manipular la app recreada con las piezas .k-app-* de kit.css
   (cámara, escribir, tocar, foco, hojas y desplazamiento); están documentadas abajo, junto a su código. */
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

  // ─── v1.3 · KRecurso.app: manipular la app recreada (.k-app-* de kit.css), variante «Para líderes» (decisión 241) ───────────────────
  // Todo va sobre la ÚNICA línea de tiempo en pausa de la escena (tl) y en segundos de la escena: nada de temporizadores ni callbacks, solo
  // tweens y sets que GSAP vuelve a pintar igual al buscar cualquier cuadro. Las medidas son px LÓGICOS de la app (las de .k-app-escala).
  // Se llaman cuando el DOM ya está armado y las fuentes cargadas (dentro del construir() que corre en document.fonts.ready).
  //   const A = KRecurso.app;
  //   A.caja(el, ancla)                          { x, y, w, h, cx, cy } de el dentro de ancla (offsets: sin transformaciones)
  //   A.medida(el) / A.conLayout(el, fn)         medir con el diseño real aunque la escena esté oculta al armar la línea de tiempo
  //   A.camara(tl, cam, { z, cx, cy | en, ancla, dy, borde, t, d })   acercamiento z (1–1,8) con el punto (cx, cy) al centro (o con el
  //                                              borde izquierdo fijo: borde: 'izquierda'); power2.inOut
  //   A.desliz(tl, desliz, y, t, d)              «scroll» de la página: la y de .k-app-desliz
  //   A.escribir(tl, campo, texto, t, { cps })   enfoca el campo, sube la etiqueta si estaba vacío, escribe letra por letra con su cursor
  //                                              y lo desenfoca; devuelve el segundo en que termina
  //   A.vaciar(tl, campo)                        el campo se ve vacío (etiqueta abajo) hasta que A.escribir() lo llena
  //   A.tocar(tl, ancla, en, t, { dx, dy })      el dedo cae en «en», lo presiona 120 ms y se va; crea su .k-dedo dentro de ancla
  //   A.foco(tl, ancla, en, t, hasta, { pad })   oscurece el resto y pone el anillo dorado sobre «en» de t a hasta; crea su .k-foco
  //   A.hoja(tl, el, t, { tipo, velo, hasta })   una hoja que sube (tipo 'hoja') o un diálogo que aparece (tipo 'dialogo'), con su velo
  //   A.aparecer(tl, el, t) / A.quitar(tl, el, t)   entrada y salida cortas de una pieza de la app (snackbar, menú, una fila nueva)
  const app = (function () {
    const r3 = (n) => Math.round(n * 1000) / 1000;
    const css = (el, v, def) => (getComputedStyle(el).getPropertyValue(v) || '').trim() || def;
    let nDedo = 0;
    let nFoco = 0;

    /** Mide con el diseño real: cuando se arma la línea de tiempo la escena suele estar oculta (display: none hasta su ventana de tiempo),
     *  y así todo mide 0. Muestra un instante los ancestros ocultos de el (display: block !important), corre fn y los deja como estaban. */
    function conLayout(el, fn) {
      const ocultos = [];
      for (let n = el; n && n.nodeType === 1; n = n.parentElement) {
        if (getComputedStyle(n).display === 'none') {
          ocultos.push([n, n.style.getPropertyValue('display'), n.style.getPropertyPriority('display')]);
          n.style.setProperty('display', 'block', 'important');
        }
      }
      try {
        return fn();
      } finally {
        for (const [n, v, p] of ocultos.reverse()) {
          if (v) n.style.setProperty('display', v, p);
          else n.style.removeProperty('display');
        }
      }
    }
    /** Ancho y alto de el (px lógicos) con el diseño real. */
    const medida = (el) => conLayout(el, () => ({ w: el.offsetWidth, h: el.offsetHeight }));

    /** Caja de el dentro de ancla, en px lógicos, sumando offsetLeft/offsetTop (no ve transformaciones: es la posición de diseño). */
    function caja(el, ancla) {
      return conLayout(el, () => cajaYa(el, ancla));
    }
    function cajaYa(el, ancla) {
      let x = 0, y = 0, n = el;
      while (n && n !== ancla) {
        x += n.offsetLeft;
        y += n.offsetTop;
        const p = n.offsetParent;
        if (!p) break;
        if (ancla && !ancla.contains(p) && p !== ancla) {
          // ancla no es un ancestro posicionado: se resta su propia posición respecto al mismo padre
          const a = cajaYa(ancla, p);
          x -= a.x;
          y -= a.y;
          break;
        }
        n = p;
      }
      const w = el.offsetWidth, h = el.offsetHeight;
      return { x, y, w, h, cx: x + w / 2, cy: y + h / 2 };
    }

    /** Cámara sobre .k-app-camara: con origen 0 0, x = W/2 − z·cx e y = H/2 − z·cy, sin dejar ver fuera de la pantalla (limitar). */
    function camara(tl, cam, o) {
      const m = medida(cam);
      const W = m.w, H = m.h;
      const z = o.z ?? 1;
      let cx = o.cx, cy = o.cy;
      if (o.en) {
        const c = caja(o.en, o.ancla || cam);
        cx = c.cx;
        cy = c.cy;
      }
      cx = (cx ?? W / 2) + (o.dx || 0);
      cy = (cy ?? H / 2) + (o.dy || 0);
      let x = W / 2 - z * cx, y = H / 2 - z * cy;
      // borde: 'izquierda' deja fijo el borde izquierdo (en el celular las etiquetas y los textos empiezan ahí: se acerca sin cortarlos)
      if (o.borde === 'izquierda') x = 0;
      else if (o.borde === 'derecha') x = W - z * W;
      if (o.limitar !== false) {
        x = Math.min(0, Math.max(W - z * W, x));
        y = Math.min(0, Math.max(H - z * H, y));
      }
      tl.to(cam, { x: r3(x), y: r3(y), scale: z, duration: o.d ?? 1, ease: o.ease || 'power2.inOut' }, o.t);
      return { x, y, z };
    }

    function desliz(tl, el, y, t, d) {
      tl.to(el, { y, duration: d ?? 0.9, ease: 'power2.inOut' }, t);
    }

    /** Prepara el valor del campo como letras (una caja por letra, con su cursor a la derecha): así escribir es solo opacidad, buscable. */
    function letras(campo) {
      const v = campo.querySelector('.k-app-campo-valor');
      if (!v) throw new Error('KRecurso.app: el campo no tiene .k-app-campo-valor');
      return v;
    }

    function etiquetaAbajo(campo) {
      const et = campo.querySelector('.k-app-campo-etiqueta');
      const ico = campo.firstElementChild && campo.firstElementChild.classList.contains('k-app-icono') ? campo.firstElementChild : null;
      const xr = ico ? medida(ico).w + 12 : 0; // en reposo va después del ícono de adelante (buscar, quién lo invitó); la flecha del select va atrás
      const yr = 28; // el centro de la primera línea (campo de 56 px o área con 16 px de relleno arriba)
      return { et, desde: { x: xr, y: yr, scale: 4 / 3 } };
    }

    /** El campo vacío (la etiqueta en reposo, dentro) hasta que se escriba. */
    function vaciar(tl, campo) {
      const { et, desde } = etiquetaAbajo(campo);
      if (et) tl.set(et, desde, 0);
      campo.__kVacio = true;
    }

    /** Escribe texto en el campo desde t: foco (borde de 2 px y etiqueta en el primario; la etiqueta sube si estaba vacío), letras a cps
     *  por segundo con su cursor, dos parpadeos y se desenfoca (salvo desenfocar: false). Devuelve el segundo en que termina. */
    function escribir(tl, campo, texto, t, o) {
      o = o || {};
      const cps = o.cps || 14;
      const v = letras(campo);
      const primario = css(campo, '--k-app-primario', '#015bbe');
      const contorno = css(campo, '--k-app-contorno', '#74777f');
      const texto2 = css(campo, '--k-app-texto-2', '#44474f');
      const { et, desde } = etiquetaAbajo(campo);
      v.textContent = '';
      const viejas = [];
      for (const ch of String(o.antes || '')) {
        const s = document.createElement('span');
        s.textContent = ch;
        v.appendChild(s);
        viejas.push(s);
      }
      const cur0 = document.createElement('span');
      cur0.className = 'k-app-cursor';
      v.appendChild(cur0);
      const ls = [];
      for (const ch of String(texto)) {
        const s = document.createElement('span');
        s.textContent = ch;
        s.style.opacity = '0';
        s.style.position = 'relative';
        const c = document.createElement('span');
        c.className = 'k-app-cursor';
        c.style.position = 'absolute';
        c.style.right = '-2px';
        c.style.top = '2px';
        c.style.margin = '0';
        s.appendChild(c);
        v.appendChild(s);
        ls.push({ s, c });
      }
      const f0 = t - 0.3;
      tl.to(campo, { boxShadow: `inset 0 0 0 2px ${primario}`, duration: 0.15, ease: 'power1.out' }, f0);
      if (et) {
        tl.to(et, { color: primario, duration: 0.15 }, f0);
        if (campo.__kVacio || o.vacio) tl.fromTo(et, desde, { x: 0, y: 0, scale: 1, duration: 0.2, ease: 'power2.out', immediateRender: false }, f0);
      }
      const paso = 1 / cps;
      if (viejas.length) {
        // Borrar lo que había: el cursor al final y las letras se van de atrás para adelante (al doble de velocidad), antes de t.
        const b0 = r3(t - 0.15 - viejas.length * paso * 0.5);
        v.insertBefore(cur0, null);
        tl.set(cur0, { opacity: 1 }, f0 + 0.05);
        viejas.slice().reverse().forEach((s, i) => tl.set(s, { opacity: 0, display: 'none' }, r3(b0 + i * paso * 0.5)));
      } else tl.set(cur0, { opacity: 1 }, f0 + 0.05);
      let anterior = cur0;
      ls.forEach(({ s, c }, i) => {
        const ti = r3(t + i * paso);
        tl.set(s, { opacity: 1 }, ti);
        tl.set(anterior, { opacity: 0 }, ti);
        tl.set(c, { opacity: 1 }, ti);
        anterior = c;
      });
      const fin = r3(t + ls.length * paso);
      // Dos parpadeos del cursor (finitos) y el desenfoque.
      [0.25, 0.5, 0.75].forEach((k, j) => tl.set(anterior, { opacity: j % 2 ? 1 : 0 }, fin + k));
      const blur = fin + (o.espera ?? 0.9);
      if (o.desenfocar !== false) {
        tl.set(anterior, { opacity: 0 }, blur);
        tl.to(campo, { boxShadow: `inset 0 0 0 1px ${contorno}`, duration: 0.15 }, blur);
        if (et) tl.to(et, { color: texto2, duration: 0.15 }, blur);
      }
      return fin;
    }

    /** El dedo: aparece 4 cuadros antes en el centro de «en» (más dx, dy), se hunde en t con su onda, el elemento queda presionado
     *  120 ms (escala 0,97 y un poco más oscuro) y el dedo se va. Crea su .k-dedo dentro de ancla (mejor la misma capa que «en»). */
    function tocar(tl, ancla, en, t, o) {
      o = o || {};
      const c = caja(en, ancla);
      const d = document.createElement('div');
      d.className = 'k-dedo';
      d.id = o.id || `k-dedo-${++nDedo}`;
      const onda = document.createElement('span');
      onda.className = 'k-dedo-onda';
      d.appendChild(onda);
      ancla.appendChild(d);
      const x = r3(c.cx + (o.dx || 0)), y = r3(c.cy + (o.dy || 0));
      const F = 1 / 30;
      tl.set(d, { x, y }, 0);
      tl.fromTo(d, { opacity: 0, scale: 1.3 }, { opacity: 1, scale: 1, duration: 0.22, ease: 'power2.out', immediateRender: false }, t - 0.22 - 4 * F);
      tl.to(d, { scale: 0.82, duration: 0.08, ease: 'power2.in' }, t);
      tl.fromTo(onda, { opacity: 0.9, scale: 0.6 }, { opacity: 0, scale: 1.45, duration: 0.45, ease: 'power2.out', immediateRender: false }, t);
      tl.to(d, { scale: 1, duration: 0.12, ease: 'power2.out' }, t + 0.12);
      tl.to(d, { opacity: 0, duration: 0.25, ease: 'power1.in' }, t + (o.queda ?? 0.35));
      if (o.presionar !== false) {
        tl.to(en, { scale: 0.97, filter: 'brightness(0.9)', duration: 0.06, ease: 'power1.out' }, t);
        tl.to(en, { scale: 1, filter: 'brightness(1)', duration: 0.14, ease: 'power1.out' }, t + 0.12);
      }
      return d;
    }

    /** El foco: un anillo dorado redondeado sobre «en» (con pad px de aire) y el resto de la pantalla al 55 %, de t a hasta. */
    function foco(tl, ancla, en, t, hasta, o) {
      o = o || {};
      const c = caja(en, ancla);
      const pad = o.pad ?? 6;
      const f = document.createElement('div');
      f.className = 'k-foco';
      f.id = o.id || `k-foco-${++nFoco}`;
      Object.assign(f.style, { left: `${c.x - pad}px`, top: `${c.y - pad}px`, width: `${c.w + 2 * pad}px`, height: `${c.h + 2 * pad}px` });
      if (o.radio !== undefined) f.style.setProperty('--k-foco-radio', `${o.radio}px`);
      ancla.appendChild(f);
      tl.fromTo(f, { opacity: 0, scale: 1.08 }, { opacity: 1, scale: 1, duration: 0.35, ease: 'power2.out', immediateRender: false }, t);
      if (hasta !== undefined && hasta !== null) tl.to(f, { opacity: 0, duration: 0.3, ease: 'power1.in' }, hasta);
      return f;
    }

    /** Hoja desde abajo (Material 3: sube con una desaceleración marcada) o diálogo (aparece y crece de 0,92 a 1), con el velo. */
    function hoja(tl, el, t, o) {
      o = o || {};
      const dialogo = (o.tipo || 'hoja') === 'dialogo';
      if (o.velo) tl.fromTo(o.velo, { opacity: 0 }, { opacity: 1, duration: 0.25, ease: 'power1.out', immediateRender: false }, t);
      if (dialogo) tl.fromTo(el, { opacity: 0, scale: 0.92 }, { opacity: 1, scale: 1, duration: 0.32, ease: 'power2.out' }, t);
      else tl.fromTo(el, { yPercent: 104 }, { yPercent: 0, duration: 0.5, ease: 'expo.out' }, t);
      if (o.hasta !== undefined && o.hasta !== null) {
        if (dialogo) tl.to(el, { opacity: 0, scale: 0.96, duration: 0.22, ease: 'power1.in' }, o.hasta);
        else tl.to(el, { yPercent: 104, duration: 0.3, ease: 'power2.in' }, o.hasta);
        if (o.velo) tl.to(o.velo, { opacity: 0, duration: 0.25 }, o.hasta);
      }
    }

    function aparecer(tl, el, t, o) {
      tl.fromTo(el, { opacity: 0, y: (o && o.dy) ?? 12 }, { opacity: 1, y: 0, duration: (o && o.d) || 0.3, ease: 'power2.out', immediateRender: !(o && o.otra) }, t);
    }
    function quitar(tl, el, t, o) {
      tl.to(el, { opacity: 0, y: (o && o.dy) ?? 0, duration: (o && o.d) || 0.25, ease: 'power1.in' }, t);
    }

    return { conLayout, medida, caja, camara, desliz, escribir, vaciar, tocar, foco, hoja, aparecer, quitar };
  })();

  window.KRecurso = {
    version: 'v1.3',
    app,
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
