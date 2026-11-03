# Videos de Kingdom

Videos de **Kingdom** (la app para iglesias) hechos con HyperFrames. Las directivas (los tipos: Wiki, Comercial, Corto, Estrategia y Recurso; la app real; datos
ficticios; aprobaciones) y la identidad viven en el repo de la app: `KingdomApp/docs/videos/README.md` y `KingdomApp/docs/videos/identidad.md`.
Este directorio tiene el **kit de identidad** que todos los videos montan y las muestras que lo prueban.

## Qué hay aquí

| Carpeta | Qué es |
|---|---|
| `_identidad/` | Kit de identidad **v1.4**: intro y cierre del Tipo Wiki, cierres de marca del Comercial (16:9), del Corto (9:16) y del clip (4:5), las piezas del Tipo Recurso (`intro-recurso`, `capitulo-recurso`, `fondo-recurso`, `cierre-recurso`, `recurso.js`, `frame-recurso.md`), `kit.json`, `kit.css` (con `.k-ventana`, `.k-feed-*`, `.k-recurso-*` y, desde la v1.3, `.k-app-*`, `.k-dedo` y `.k-foco` para la app recreada de «Para líderes»), `frame-wiki.md`, `frame-comercial.md`, `frame-corto.md`, favicon, Inter y Fraunces, 117 íconos de Material Symbols, `sonido-marca.mjs`, `sonidos-accion.mjs`, `musica/` (las pistas, fuera de git, y el mapa de pulsos de «Product Launch») y licencias. **No se edita por video** |
| `_herramientas/montar-kit.mjs` | Copia el kit en `<proyecto>/identidad/`, comprueba el favicon contra la app, genera el sonido de marca a −20 LUFS y los sonidos de acción con su nivel de mezcla |
| `muestra-kit/` | Muestra 16:9: intro Wiki → cuerpo con una captura real de la ayuda → cierre Wiki → cierre del Comercial |
| `muestra-corto/` | Muestra 9:16: una escena de Corto con los componentes de `kit.css` → cierre del Corto |
| `_herramientas/recurso.mjs` | Arma un video del Tipo Recurso desde su `guion.mjs`: voz, música en bucle, línea de tiempo en la rejilla de la música, host, VTT, render y entrega (ver «Tipo Recurso (v1.2)») |
| `muestra-recurso/` | Muestra del Tipo Recurso (v1.2, 32 s): intro → capítulo → escena con voz y tipografía cinética en frases y pulsos → cierre, de punta a punta con `recurso.mjs` |
| `muestra-clip/` | Muestra 4:5 (v1.1): la app real en `.k-ventana` con la cámara dentro, una frase con `.k-feed-*`, sonidos de acción sobre «Product Launch» → `cierre-clip` |
| `<tipo>-<tema>/` | Un proyecto por video: `wiki-eventos-crear-y-editar`, `clip-sitio-membresia`, `comercial-iglesia-ordenada`, `corto-asistencia-sin-papel` |

Los videos anteriores (`../kingdomapp-promo`, `../kingdomapp-afirmar-nuevo`) son de antes del kit: recrean la app y usan otra marca. No se
toman como referencia visual.

En git va solo el código del video. Capturas, voces, música, renders, hojas de contacto y el `identidad/` montado quedan fuera (`.gitignore`).

## Requisitos de esta máquina

- Node 22, FFmpeg y el CLI fijado por `npx`: `hyperframes@0.8.62` en las muestras v1 y la Wiki (el mismo de los videos de
  LegacyEnterprise); `hyperframes@0.8.221` en los clips del sitio, `muestra-clip` y todo el Tipo Recurso (`recurso.mjs` la fija
  y comprueba que tenga `tts`).
- Voz: `../../.venv-tts/` y el modelo Kokoro (ver `../legacyenterprise/README.md`).
- KingdomApp al lado (`F:\Proyectos\KingdomApp`, o la variable `KINGDOMAPP_REPO`): `montar-kit.mjs` compara el favicon del kit con
  `frontend-v2/public/favicon.svg` y se detiene si la app cambió de marca.

## Usar el kit en un proyecto

1. Crear la carpeta `<tipo>-<tema>/` con `BRIEF.md` (con la línea `tipo:`), `hyperframes.json` y un `package.json` con el script
   `"kit": "node ../_herramientas/montar-kit.mjs"` (copiar los de `muestra-kit/`).
2. `npm run kit` → monta `identidad/` e imprime en qué segundo va el sonido de marca de cada pieza.
3. En el `<head>` del `index.html`, una sola vez (nunca dentro del `<template>` de una escena: ahí no carga):

   ```html
   <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
   <link rel="stylesheet" href="identidad/fuentes/fuentes.css" />
   <link rel="stylesheet" href="identidad/kit.css" />
   ```

4. Montar las piezas del kit como subcomposiciones y poner el sonido de marca en el host, en **inicio de la pieza + su `sonido`** de
   `kit.json` (una subcomposición no puede mover su audio según una variable):

   ```html
   <!-- Tipo Wiki -->
   <div id="intro-wiki" data-composition-id="intro-wiki" data-composition-src="identidad/intro-wiki.html"
     data-variable-values='{"titulo":"Crear, editar o inactivar un evento","seccion":"eventos","idioma":"es"}'
     data-start="0" data-duration="3" data-track-index="1" data-width="1920" data-height="1080"></div>
   <audio id="marca-intro" src="identidad/audio/sonido-marca.wav" data-start="0.38" data-duration="2.1" data-track-index="11"></audio>
   …
   <div id="cierre-wiki" data-composition-id="cierre-wiki" data-composition-src="identidad/cierre-wiki.html"
     data-variable-values='{"siguiente":"Aprobar solicitudes de eventos y reportes","seccion":"eventos","idioma":"es"}'
     data-start="T" data-duration="4" data-track-index="1" data-width="1920" data-height="1080"></div>
   <!-- sonido en T + 1.88; sin «siguiente»: data-duration="2.5" y sonido en T + 0.38 -->

   <!-- Tipo Comercial (al final) -->
   <div id="cierre-comercial" data-composition-id="cierre-comercial" data-composition-src="identidad/cierre-comercial.html"
     data-variable-values='{"publico":"iglesia","llamado":"prueba","contacto":"sitio","fondo":"noche","idioma":"es"}'
     data-start="T" data-duration="5" data-track-index="1" data-width="1920" data-height="1080"></div>
   <!-- sonido en T + 0.38 -->

   <!-- Tipo Corto (al final, en un proyecto 1080×1920) -->
   <div id="cierre-corto" data-composition-id="cierre-corto" data-composition-src="identidad/cierre-corto.html"
     data-variable-values='{"llamado":"prueba","fondo":"azul","idioma":"es"}'
     data-start="T" data-duration="2.5" data-track-index="1" data-width="1080" data-height="1920"></div>
   <!-- sonido en T + 0.38 -->

   <!-- Clip del sitio y feed en 4:5 (al final, en un proyecto 1080×1350): las mismas variables del Corto -->
   <div id="cierre-clip" data-composition-id="cierre-clip" data-composition-src="identidad/cierre-clip.html"
     data-variable-values='{"llamado":"prueba","fondo":"azul","idioma":"es"}'
     data-start="T" data-duration="2.5" data-track-index="1" data-width="1080" data-height="1350"></div>
   <!-- sonido en T + 0.38 -->
   ```

5. Comercial y Corto: copiar `identidad/frame-comercial.md` o `identidad/frame-corto.md` como `frame.md` del proyecto **antes** de entrar al
   flujo de HyperFrames (`/product-launch-video` o `/general-video`), para que el flujo use la marca y no invente otra. Cada escena es una
   subcomposición en `compositions/` que usa las clases `.k-*` (ver `muestra-corto/compositions/gancho.html`).
6. Revisión: `npm run check` (0 errores) → `npx --yes hyperframes@0.8.62 snapshot --at …` en la mitad de cada escena y revisar la hoja de
   contacto → render. Comercial y Corto: el visto bueno del dueño sobre el storyboard y el preview.

Cada pieza del kit se monta **una vez** por proyecto (los ids internos no se repiten). Para otra variante, otro proyecto.

## La app en 4:5, 9:16 y 16:9: `.k-ventana` (v1.1)

La grabación real de la app va **recortada y ampliada** dentro de una ventana con radio, anillo sutil y sombra sobre la noche. No es un
teléfono ni un marco de aparato (las directivas lo prohíben). La cámara es un envoltorio que GSAP escala y mueve; la ventana y la grabación
no se transforman:

```html
<div class="k-ventana k-ventana-4x5" id="escena-ventana" style="left: 100px; top: 400px">
  <div class="k-ventana-camara" id="escena-camara" data-layout-allow-overflow>
    <img class="k-ventana-grabacion" src="assets/captura/….webp" alt="" />   <!-- o <video muted playsinline> -->
  </div>
</div>
```

| Clase | Tamaño | Dónde va | Para qué |
|---|---|---|---|
| `.k-ventana-4x5` | 880 × 840, radio 28 | left 100, top 400 (debajo de la ceja y la frase) | Clip del sitio y feed, 1080×1350 |
| `.k-ventana-9x16` | 960 × 850, radio 28 | left 60, top 480 (zona segura del Corto) | Corto y Reels, 1080×1920 |
| `.k-ventana-16x9` | 720 × 900, radio 28 | left 1104, top 90 (columna derecha) | La grabación del celular en un video 16:9 |
| `.k-ventana-escritorio` | 1440 × 760, radio 20 | left 240, top 260 (el titular arriba) | Un recorte de una grabación de escritorio en 16:9 |

- **El plano:** la grabación llena el ancho de la ventana. Con la del celular (390 px a 3×, 1170 px de ancho, o al menos 1080), el plano
  de 4:5 la muestra a 2,26× del celular real: el texto de 14 px de la app queda en 32 px.
- **La cámara:** acercamientos de **1,6 a 2** sobre el plano (1,5 si el encuadre no cabe), uno por compás (0,4–0,6 s, `power3.inOut`) y
  quieta después. Con origen 0 0, para poner el punto `(cx, cy)` de la grabación ajustada en el centro con el acercamiento `z`:
  `x = ancho/2 − z·cx`, `y = alto/2 − z·cy`; o la esquina de arriba a la izquierda en `(ex, ey)`: `x = −z·ex`, `y = −z·ey`. A 2, cada píxel
  de una grabación de 1170 px ocupa 1,5 px: todavía nítida; más allá se nota.
- `data-layout-allow-overflow` en la cámara: la grabación es más grande que la ventana a propósito (si no, `check` avisa).
- Toda cifra visible lleva `.k-datos-ejemplo`; en 4:5 y 9:16, con `.k-feed-datos` (28 px, el mínimo que se lee en un celular).

## Textos en 4:5: `.k-feed-*` (v1.1)

Dentro del 80 % seguro para títulos: `.k-feed-zona` (108 px a los lados, 135 px arriba y abajo). En un celular el cuadro se ve a unos
390 px de ancho (×0,36).

| Clase | Letra | En el celular |
|---|---|---|
| `.k-feed-ceja` | Inter 700, 34 px, mayúsculas, dorado | 12 px |
| `.k-feed-frase` | Fraunces 560, 80 px, interlínea 1,04, máx. 2 líneas (~40 caracteres); `<em>` en itálica dorada, 1–3 palabras | 29 px |
| `.k-feed-texto` | Inter 500, 42 px, máx. 2 líneas | 15 px |

Con la ceja y la frase de dos líneas, el texto ocupa de 135 a ~360 px y la ventana empieza en 400. Usan los colores de `.k-noche` o
`.k-claro`. Ver `muestra-clip/compositions/cuerpo.html`.

## Sonidos de acción (v1.1)

Propios, generados por código (`_identidad/sonidos-accion.mjs`, el motor del sonido de marca: notas de Mi mayor y ruido con semilla fija).
`montar-kit.mjs` los deja en `identidad/audio/<nombre>.wav` con su nivel de mezcla; la huella de cada uno está en `kit.json` →
`sonidosAccion`.

| Sonido | Dura | Acento | Pico montado | Bajo la música | Cuándo |
|---|---|---|---|---|---|
| `toque` | 75 ms | 0 | −7 dBFS | −10 dB | Un toque real en la app |
| `aparicion` | 220 ms | 0 | −13 dBFS | −8 dB | Una tarjeta, una píldora, un contador o la ventana que aparecen |
| `desliz` | 360 ms | 0,2 s | −13 dBFS | −8 dB | Un corte rápido, el látigo entre dos mundos, un movimiento grande de cámara |
| `subida` | 1,9 s | 1,5 s (el golpe) | −11 dBFS | −4 dB | Una vez por video, hacia el cambio más grande |
| `confirmacion` | 320 ms | 0,1 s | −14 dBFS | −7 dB | Algo que queda hecho («Guardado», «cumplido») |

- **Nivel:** con la música a −18 LUFS (la pista de la biblioteca con su `volumen`), los sonidos van con `data-volume="1"`. «Bajo la música»
  es la sonoridad momentánea (400 ms) del sonido solo menos la de la música en ese instante, medida con «Product Launch». Si la música va
  más baja o más alta, se mueven lo mismo.
- **Cuándo:** el acento cae un cuadro después de su imagen: `data-start = momento visible + 0,033 − acento`. Para la subida hacia la firma:
  `data-start = T − 1,467`.
- **Pocos y exactos:** cada uno con una causa en pantalla; `desliz` nunca en todos los cortes; `subida` una sola vez.

```html
<audio id="snd-toque" src="identidad/audio/toque.wav" data-start="1.533" data-duration="0.075" data-track-index="13" data-volume="1"></audio>
```

## Música

La biblioteca está en `_identidad/musica/` (los mp3 fuera de git) y en `kit.json` → `musica.biblioteca`: archivo, licencia, `volumen` para
−18 LUFS sin voz, pulsos y mapa. Cada proyecto copia la suya a `assets/musica/` (`npm run musica` en `muestra-clip`).

- **«Product Launch»** (`product-launch`, 120 BPM, `volumen` 0,7): todos los clips del sitio. Compases de 2 s desde el 2,05: entrada sin bajo
  hasta el 18; el bajo entra en el 18,05 (pico en el 20); respiro del 26 al 34; segunda subida desde el 34 con golpes en el 36, el 38 y el
  42,05 (el más fuerte); clímax del 50 al 66; salida del 66 al 82; final en el 84. Los pulsos, en `musica/product-launch-the-mountain.pulsos.json`.
  Los clips de módulo usan 14,05 → 42,05 y la firma arranca en el golpe del 42,05 (`data-media-start`, `data-fade-out="1"`).
- **«Education Piano»** (`education-piano`, `volumen` 0,83): en la biblioteca, sin uso por ahora.

## Probar el kit

```bash
cd muestra-kit && npm run captura && npm run kit && npm run check && npm run render   # renders/muestra-kit-16x9.mp4 (16 s)
cd ../muestra-corto && npm run kit && npm run check && npm run render  # renders/muestra-corto-9x16.mp4 (5 s)
cd ../muestra-clip && npm run captura && npm run musica && npm run kit && npm run check && npm run render  # renders/muestra-clip-4x5.mp4 (6,5 s)
cd ../muestra-recurso && npm run preparar:es && npm run check && npm run render:es && npm run entregar:es  # entrega/es/ (32 s, v1.2)
```

## Tutoriales de la wiki

`_herramientas/tutorial-wiki.mjs` arma un tutorial narrado desde la grabación real de la app (`KingdomApp/tools/ayuda`,
`node capturar.mjs <seccion/articulo> --idioma es --modo video`) y su `guion.mjs`: monta el kit con `montar-kit.mjs`, toma de `kit.json` →
`piezas` las duraciones y los segundos del sonido de marca, genera la voz (Kokoro), las escenas, el `index.html`, el VTT y `SCRIPT.md`, y
`entregar` deja el MP4 a −16 LUFS, el póster y el VTT en `KingdomApp/tools/ayuda/salida/tutorial/<idioma>/<articulo>/`. Piloto:
`wiki-eventos-crear-y-editar/` (`npm run preparar:es`, `npm run check`, `npm run render:es`, `npm run entregar:es`; lo mismo con `en`).
Proceso y lista de revisión: `KingdomApp/docs/ayuda/videos.md`.

## Tipo Recurso (v1.2; variante «Para líderes» en la v1.3)

Videos largos (5–7 min, 16:9) que el dueño comparte por WhatsApp a pastores y líderes que ya usan Kingdom (decisión 239; directivas en
`KingdomApp/docs/videos/README.md` → «Tipo 5. Recurso»). Los de pastores son **motion design puro con la marca, sin la app** (excepción a
la regla 1, decidida por el dueño); los de la sección «Para líderes» (decisión 241) **recrean la app v2 en HTML, fiel**, en sus escenas
técnicas (ver «Variante “Para líderes”» abajo). Voz Kokoro fija y «Product Launch» en bucle. El sistema visual está en `_identidad/frame-recurso.md` (cópialo como
`frame.md` del proyecto antes de diseñar). La herramienta es `_herramientas/recurso.mjs`, fijada a **`hyperframes@0.8.221`**.

### El proyecto

`recurso-<tema>/` (copiar `package.json` y `hyperframes.json` de `muestra-recurso/`) con:

- `BRIEF.md` (línea `tipo: recurso`), `guion.mjs` y `compositions/<id>.html` (una por escena con voz o sin ella; las tarjetas de capítulo
  son del kit).
- Se generan (fuera de git): `identidad/`, `assets/voice/`, `assets/musica/`, `assets/mezcla/<idioma>/`, `index.html`, `tiempos-<idioma>.json`,
  `renders/`, `snapshots/` y `entrega/`. `SCRIPT.md` (la narración) también se genera y sí va a git.

### `guion.mjs`

```js
export default {
  slug: 'pastor-resultados',                         // minúsculas y guiones; va a la ficha
  titulo: { es: 'Lo que tu iglesia *ya puede ver*' }, // intro (máx. ~48 caracteres, 2 líneas); *así* va en itálica dorada
  descripcion: { es: '…' },                          // página pública y vista previa de WhatsApp (~160 caracteres)
  ceja: { es: 'Recursos' },                           // opcional (por defecto «Recursos»/«Resources»); o el nombre de la serie
  siguiente: { es: 'Eventos de ciudad, de punta a punta' }, // opcional: «Sigue con» en el cierre (sin él, el cierre dura 6 s)
  llamado: 'acompanamiento',                          // acompanamiento | compartir | ministerio (v1.4: «Tu aliado para la expansión del Reino») | ninguno
  contacto: 'whatsapp',                               // whatsapp | sitio | ninguno
  para: ['pastores', 'lideres'],                      // opcional, a la ficha: pastores | lideres | administradores | servidores
  seccion: 'lideres',                                 // opcional (v1.3), a la ficha: pastores | lideres (la sección de Recursos)
  departamento: 'afirmacion',                         // opcional (v1.3), a la ficha, en «Para líderes»: afirmacion (lista cerrada)
  mensaje: { es: 'Pastor, mira este recurso: {enlace}' }, // opcional, a la ficha: el texto de WhatsApp, con {enlace}
  poster: { en: 5.2 },                                // opcional: segundo del póster (por defecto, el final de la intro)
  musica: {                                           // opcional: todo tiene valor por defecto (kit.json → mapa.recurso)
    entrada: [0.05, 50.05],                           // tramo de la pista que abre (en cabezas de compás: 0,05 + 2k)
    bucle: [[18.05, 66.05]],                          // tramos que se repiten en orden hasta cubrir el video
    salida: 66.05,                                    // desde aquí la pista va de corrido hasta su final natural (86,05)
    corte: 2,                                         // el bucle se corta en múltiplos de esto (s; 8 = medias frases, más holgura)
    cruce: 0.03,                                      // cruce de potencia constante antes de cada cabeza de compás (s)
    bajoLaVoz: 20,                                    // dB de la música por debajo de la voz (18–24)
  },
  escenas: [
    { id: 'cap-1', capitulo: { numero: '1', titulo: { es: 'Ver a *cada persona*' }, bajada: { es: '…' }, icono: 'groups', fondo: 'noche' }, duracion: 4 },
    {
      id: 'medir',                                    // compositions/medir.html (o composicion: 'compositions/otra')
      frases: [
        { es: 'Cada domingo llegan *personas nuevas*.', clave: 'llegan', pausa: 0.5 },
        { es: 'Kingdom te muestra quién volvió.', voz: { es: 'Kíngdom te muestra quién volvió.' }, alPulso: true },
      ],
      entrada: 0.5, cola: 0.8, minimo: 12,            // s: antes de la 1.ª frase, después de la última, duración mínima
      variables: { rotulo: { es: '…' } },             // otras variables de la composición (por idioma o fijas)
      sonidos: [{ sonido: 'aparicion', frase: 0, palabra: 3, desfase: -0.25, alPulso: true }], // opcional (sonidos de acción del kit)
      estirable: true,                                // puede recibir la holgura de la música (en compases)
      alinear: 'pulso',                               // pulso (por defecto con voz) | compas (por defecto sin voz)
    },
    { id: 'respiro', duracion: 3.5 },                  // escena sin voz: compositions/respiro.html con duración fija
  ],
};
```

- Frase: `es` (y `en`, `pt`) es el texto de la pantalla y del VTT; `voz` es otro texto solo para la pronunciación; `*clave*` marca palabras
  (`clave: true` en sus tiempos) sin que la voz ni el VTT lleven asteriscos; `clave` (en la frase) es un nombre para buscarla con
  `T.frase('nombre')`; `pausa` (0,3) es el silencio después; `desde` (s) es el inicio mínimo en la escena; `alPulso` la empuja al pulso
  siguiente.
- La duración de una escena con voz es `entrada + frases + pausas + cola` (o `minimo`), redondeada al pulso. Las escenas con voz empiezan
  en un pulso y las que no tienen voz, en un compás.
- `sonidos`: los de acción del kit (`toque`, `aparicion`, `desliz`, `subida`, `confirmacion`), en el host, con `en` (s en la escena) o
  `frase`/`palabra`; `desfase` se suma antes de `alPulso`, igual que `T.pulso(t + desfase)` en la composición. Pocos y con causa en pantalla.

### Comandos

```bash
cd recurso-<tema>
node ../_herramientas/recurso.mjs preparar --idioma es   # kit, voz, música, tiempos, VTT, SCRIPT.md, index.html; imprime las mitades
npx --yes hyperframes@0.8.221 check                     # 0 errores
npx --yes hyperframes@0.8.221 snapshot --at <mitades> --no-end -o snapshots   # revisar la hoja de contacto (pocas imágenes)
node ../_herramientas/recurso.mjs render --idioma es     # renders/recurso-es.mp4, temporales en renders/tmp (F:), mide el tiempo
node ../_herramientas/recurso.mjs entregar --idioma es   # entrega/es/ y la verificación de sonoridad
```

`preparar` comprueba que `hyperframes@0.8.221 tts` exista (Kokoro, con `HYPERFRAMES_PYTHON` del `.venv-tts`), valida `para`, `seccion`, `departamento` y `mensaje`,
monta el kit, genera la voz fija del kit (`ef_dora` a 1,1 en español; una frase por archivo, normalizada a −16 LUFS en dos pasadas y en
caché por texto) e imprime cada escena, el plan de la música, la mezcla medida y los segundos para el snapshot.

### Cómo lee sus tiempos una composición

El host le pasa a cada escena, en `data-variable-values`, la variable `tiempos` (JSON) con su duración, sus frases y palabras y los golpes de
la música, en segundos **relativos a la escena**. La composición la declara y la lee con `identidad/recurso.js` (que carga el host):

```html
<html data-composition-variables='[{"id":"tiempos","type":"string","label":"Tiempos (los escribe recurso.mjs)","default":"{\"duracion\":8,\"frases\":[]}"}]'>
…
<script>
  (function () {
    const T = KRecurso.tiempos(window);   // al EMPEZAR el script: «window» dentro de la escena es el suyo (sus variables)
    const f = T.frase(0);                 // { texto, inicio, fin, palabras: [{ texto, inicio, fin, clave? }] } (o T.frase('nombre'))
    const tl = gsap.timeline({ paused: true });
    f.palabras.forEach((p, j) => tl.fromTo(`#mi-p-${j}`, { y: 26, opacity: 0 }, { y: 0, opacity: 1, duration: 0.35 }, p.inicio - 0.08));
    tl.fromTo('#mi-grafica', { scaleY: 0 }, { scaleY: 1, duration: 0.6 }, T.compas(f.fin));  // el cambio grande en un compás
    tl.to('#mi-todo', { opacity: 0, duration: 0.4 }, T.salida());                              // sale en los últimos 0,5 s
    tl.set({}, {}, T.duracion);
    window.__timelines['mi-escena'] = tl;
  })();
</script>
```

- `T.pulso(t)`, `T.pulsoAntes(t)`, `T.compas(t)`: el pulso (0,5 s) o compás (2 s) en `t` o después (antes); `T.golpes`: golpes de la música
  en la escena; `T.reparto(n, desde, hasta)`: n instantes en pulsos; `T.salida(d)`: `duracion − d`. Las palabras son **estimadas** (los
  silencios de la voz separan los grupos de la puntuación y cada palabra dura según sus sílabas; ±0,15 s).
- `KRecurso.tiempos()` sin `window` lee las variables del host (las del video entero), no las de la escena.
- Una composición puede montarse en varias escenas (las variables son por instancia), como la tarjeta de capítulo.
- Palabras en cajas: el espacio entre palabras es el margen de `.k-recurso-palabra`, no un espacio de texto (se perdía al partir la línea).
- `tiempos-<idioma>.json` tiene todo también en tiempo absoluto: escenas, frases (`inicioAbs`, `finAbs`), subtítulos y la música.
- Ejemplo completo: `muestra-recurso/compositions/personas.html` (texto cinético por palabra, puntos que aparecen en pulsos, líneas en la
  palabra «une», un anillo en el pulso de la tercera frase, contador con «Datos de ejemplo»).

### Alinear al pulso y el plan de música

- La pista arranca en su 0,05, así que en el video **los pulsos caen en múltiplos de 0,5 s y los compases en segundos pares**. La intro dura
  6 s (el título entra en el primer compás, el 2,0) y el cuerpo empieza en el 6,0, sobre `fondo-recurso` (la noche del cuerpo).
- La música se encadena: `entrada` → `bucle` (cortado en `corte`) → `salida`, cada tramo empezando en un segundo par del video, con un
  cruce de 30 ms que termina 10 ms antes de la cabeza de compás. La salida va de corrido hasta el final natural de la pista (86,05) y el
  **último golpe (82,05) cae en la firma del cierre** (3,0 s después de que empieza el cierre con «Sigue con», o en su inicio sin él). Para
  que eso cuadre, el cuerpo se alarga hasta 2 s (la holgura va a las escenas `estirable`, en compases, o a la última).
- `tiempos-<idioma>.json` → `musica`: `segmentos` (video ↔ pista), `secciones` (entrada, subidas, respiro, clímax, salida, en tiempo del
  video), `golpes` (los del mapa) y `fuertes` (los pulsos más intensos). Los cambios grandes van en esos golpes; los cortes, en pulsos.
- **Mezcla determinista:** la cama (`assets/mezcla/<idioma>/musica.wav`) lleva el volumen de la biblioteca (−18 LUFS sin voz) y una
  envolvente en dB calculada de las frases: baja 0,45 s antes de la voz, queda `bajoLaVoz − 2` dB abajo (18 con 20, así la música queda unos
  20 dB por debajo de la voz) mientras haya frases con huecos de menos de 3 s, y sube en 1,2 s en las escenas sin voz. La voz va en
  `voz.wav` (cada frase a −16 LUFS) y el sonido de marca en el host, en los segundos de `kit.json`. `preparar` mide e imprime la relación
  (sobre los tramos con voz, que incluyen sus silencios internos: por eso da 1–2 dB menos que `bajoLaVoz`).

### Variante «Para líderes» (kit v1.3, decisión 241)

Recursos para **líderes de departamento** (el primero, `recurso-afirmando-la-cosecha/`, para afirmación o consolidación): mezclan la
estrategia (las escenas de motion design de siempre) con lo técnico, y ahí **la app de Kingdom v2 se recrea en HTML, fiel** a las capturas
de la ayuda, y se manipula con animación. No es una grabación de pantalla. Reglas completas en `_identidad/frame-recurso.md` → «Para
líderes (v1.3, decisión 241)».

- **Piezas** (`kit.css`): `.k-app` (los tokens de la marca por defecto de `frontend-v2/src/styles/_tokens.scss`, tema claro, e Inter),
  `.k-telefono.k-app-telefono` (celular de 390 × 812 px lógicos a 1,05) o `.k-ventana.k-ventana-escritorio` (1440 × 760 a 1, como las capturas de escritorio) con
  `.k-app-escala` y `.k-app-camara`; `.k-app-barra`, `.k-app-inferior`, `.k-app-riel`, `.k-app-pestanas`, `.k-app-chip` (con
  `.k-app-chip-n`), `.k-app-campo` (etiqueta flotante, `.k-app-select`, `.k-app-area`), `.k-app-radio`, `.k-app-boton` (relleno,
  `.contorno`, `.texto`, `.tonal`), `.k-app-tarjeta`, `.k-app-fila` con `.k-app-avatar`, `.k-app-dialogo`, `.k-app-hoja`, `.k-app-velo`,
  `.k-app-cifra`, `.k-app-barras` (embudo), `.k-app-notificacion`, `.k-app-snackbar`; `.k-dedo` y `.k-foco`. Íconos con `.k-app-icono`
  (repite su máscara en el `<style>` de la composición, como `.k-recurso-icono`).
- **Ayudas** (`recurso.js` → `KRecurso.app`, sobre la línea de tiempo de la escena, deterministas y buscables): `camara()` (acercamiento y
  paneo, `power2.inOut`), `desliz()` (el desplazamiento de la página), `escribir()` (letra por letra con su cursor; con `antes` borra lo que
  había), `vaciar()`, `tocar()`, `foco()`, `hoja()` (hoja o diálogo con su velo), `aparecer()` y `quitar()`.
- **El guion** lleva `para: ['lideres']`, `seccion: 'lideres'` y `departamento` (hoy `afirmacion`); `recurso.mjs` los valida y los
  escribe en `ficha.json` para el publicador de la app (`KingdomApp/tools/recursos/publicar.mjs`).
- **Fidelidad antes del render:** las capturas de referencia en `assets/referencias/` (fuera de git; las URL están en KingdomApp
  `frontend-v2/src/ayuda/medios.json`) y una hoja `snapshots/fidelidad-*.png` con cada snapshot de la app junto a su captura.

### La entrega

`entregar` toma `renders/recurso-<idioma>.mp4` y deja en `entrega/<idioma>/` (fuera de git) la forma exacta que espera el publicador de
la app (Plataforma → Recursos):

| Archivo | Qué es |
|---|---|
| `video-1080.mp4` | 1920×1080, H.264 High (`-tune animation`, CRF 20 con techo de 1,4 Mb/s, GOP de 2 s), AAC 128 kb/s, `+faststart`: ≤ ~69 MB en 6 min |
| `video-720.mp4` | 1280×720 (CRF 22, techo 650 kb/s), AAC 96 kb/s: ≤ ~34 MB en 6 min, para datos móviles |
| `poster.jpg` | 1200×630, menos de 300 KB (si no, WhatsApp puede no mostrar la vista previa); el final de la intro o `poster.en` |
| `poster.webp` | El mismo cuadro en WebP |
| `video.vtt` | Subtítulos (no quemados): un cue por frase o media frase, máx. 2 líneas de ~42 caracteres |
| `ficha.json` | `{ slug, idioma, titulo, descripcion, duracion, ancho, alto, archivos: { "video-1080.mp4": { bytes, sha256 }, "video-720.mp4": {…}, "poster.jpg": {…}, "poster.webp": {…}, "video.vtt": {…} } }` y, si el guion los trae, `para` (lista de `pastores`, `lideres`, `administradores`, `servidores`), `seccion` (`pastores` o `lideres`), `departamento` (`afirmacion`) y `mensaje` (el texto de WhatsApp, con `{enlace}`). `duracion` en segundos (número); `ancho` y `alto` son los del video de 1080, en 16:9 (el publicador los compara con el archivo) |

El audio sale del render a −16 LUFS integrados (dos pasadas lineales, con margen de pico para el AAC; desde la v1.3 el video se codifica una
vez y, si el AAC ya codificado pasa de −1,6 dBTP, el margen baja de a 1 dB —−2,5, −3,5, −4,5— con un limitador suave, y el usado queda en
`renders/entrega-<idioma>.json`) y `entregar` **verifica** en los dos
videos −16 ±0,5 LUFS y pico ≤ −1,5 dBTP, que el de 1080 mida 1920×1080 y que el póster pese menos de 300 KB; si algo falla, se detiene.
Las medidas técnicas (sonoridad, pico, versiones) quedan en `renders/entrega-<idioma>.json`, aparte de la ficha. Publicar lo hace el
líder; el dueño lo revisa ya publicado.

### Medidas en esta máquina (2026-11-01, `muestra-recurso`, 32 s)

- `preparar`: ~40 s con tres frases nuevas (Kokoro, ~10 s por frase); con la voz en caché, unos segundos.
- `render`: **1,9–2,3 s por segundo de video** (32 s en 1,0–1,2 min): un recurso de 6 min tarda unos 12–14 min. `check` ~1 min y un
  `snapshot` de 4 cuadros ~1 min.
- Entrega de la muestra: `video-1080.mp4` 2,8 MB, `video-720.mp4` 1,3 MB, `poster.jpg` 38 KB (−16,15 LUFS, −2,3 dBTP).
