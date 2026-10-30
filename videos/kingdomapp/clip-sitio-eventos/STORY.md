# Clip del sitio: Eventos — la historia elegida: «Terminó la reunión»

2026-10-30 · Segundo clip de la serie (después de [Membresía, «Valeria llegó el domingo»](../clip-sitio-membresia/STORY.md)). **El dueño ya
no revisa guiones:** la historia se eligió aquí y se especifica completa en [SPEC.md](SPEC.md). Son palabras; nada se construye desde este
archivo. El proyecto de HyperFrames lo inicializa otro agente.

**Lo que no se reabre (el sistema de la serie, §3 del STORY de Membresía):** 4:5 (1080×1350) y después 9:16 de la misma historia · sin voz,
3–4 frases de 2 a 6 palabras (problema → Kingdom lo resuelve → resultado) · «Product Launch» 14,05 → 42,05 s, el mismo reloj (bajo en 4,0,
pico en 6,0, respiro 12–20, segunda subida desde 20,0, golpes en 22,0 y 24,0, la firma en 28,0) · mucho movimiento y siempre en los pulsos ·
la app real de Kingdom Demo en celular, dentro de `.k-ventana`, nunca un teléfono dibujado · datos ficticios con «Datos de ejemplo» · la ceja
«EVENTOS» en 6,0 · la frase final es el `titulo` de `modulos.ts` («Cada reunión cuenta, y cuenta bien») con una palabra en itálica dorada ·
`cierre-clip` con el llamado `prueba` en 28,0.

## El reloj (igual que en Membresía)

120 BPM: un pulso cada 0,5 s (15 cuadros a 30 fps), un compás cada 2 s. t = 0 del clip ↔ 14,05 de la pista. La grilla real cuadro por
cuadro está en SPEC §0.

| Compás | Clip | La pista | Qué le toca al video |
|---|---|---|---|
| 1–2 | 0 – 4 | entrada sin bajo | El gancho: la app ya trabajando. Cuadro 0 nunca negro ni la marca |
| 3 | **4,0** | **entra el bajo** | El primer toque grande en la app: Kingdom entra. Frase 2 |
| 4 | **6,0** | pico | La pantalla clave del módulo; la ceja «EVENTOS» |
| 4–6 | 6 – 12 | energía sostenida | Un movimiento de cámara por compás; la app actúa |
| 7–10 | 12 – 20 | respiro | La tarea a velocidad normal. Frase 3 |
| 11–12 | 20 – 24 | segunda subida (20,0), el compás más fuerte del cuerpo (22–24) | 20,0 y 22,0: las dos pruebas |
| 13–14 | 24 – 28 | golpe en 24,0 y el más fuerte en 28,0 | Frase 4 quieta ≥ 3,6 s; la app viva detrás |
| — | 28,0 – 30,5 | se desvanece bajo las campanas | La firma |

---

## La historia: «Terminó la reunión» ★ elegida

**Idea en una frase:** terminó la casa de paz de Jorge; con la app en la mano marca a los de siempre en un toque, agrega a la persona que
vino por primera vez (y queda registrada en la iglesia), suma a los visitantes, responde dos preguntas y la reunión queda reportada con su
número: siete personas.

**Recurso:** un momento del día de alguien (el líder al terminar la reunión) + un dato real que viaja (la reunión de la casa de paz: de
«Pendiente» con «2 vencidas» a «Reportada: 7 personas»). **Forma:** un solo aparato, cadena objeto a objeto: el botón «Reportar» de la
tarjeta abre el reporte; «Igual que la última vez» llena la lista; «Persona nueva» abre la hoja; «Agregar» pone la fila; «Guardar
asistencia» avanza los pasos; «Enviar reporte» trae el «¡Listo!». Un mundo (el celular del líder), el iris para la hoja y el dip hacia la
firma; sin látigo: este clip no cambia de persona.

**Por qué es la mejor para un pastor que no conoce Kingdom:** todo pastor tiene a Jorge: el líder de célula al que hay que perseguir el jueves
para saber cuántos fueron el miércoles. El clip muestra el reporte entero, de la tarjeta al «¡Listo!», en 24 segundos reales de la app, y
las tres promesas del sitio salen sin listarlas: el reporte guiado con sus pasos (①②✓ y la barra), la asistencia por nombre (casillas,
«Igual que la última vez», «Persona nueva», visitantes) y que cada reunión queda contada («Casa de Paz Laureles 1, miércoles, 28 de octubre:
7 personas.»). Es la historia que un desconocido repite: «terminó la reunión y en lo que llegaba a la casa ya estaba reportada». Es nativa
del celular, así que vive cómoda en 4:5 y 9:16 con una sola ventana. Y es distinta de Membresía donde debe serlo: allá el gancho era una
persona nueva escribiéndose; acá el gancho es la lista de reuniones por reportar y el gesto de Kingdom es una lista que se marca sola.

### Frases en pantalla

| Segundo | Frase | Cómo entra | Se va |
|---|---|---|---|
| 0,0 | **Terminó la reunión. ¿Quién vino?** | una landing por pulso: «Terminó» 0,0 · «la reunión.» 0,5 · «¿Quién» 1,0 · «vino?» 1,5 (blur 6 px → 0, sin desplazarse) | 4,0, con el toque |
| 4,0 | **Los de siempre, en un toque.** | la línea entera, blur 8 → 0 en 0,2 s, con el toque en «Igual que la última vez» | 6,0, con el toque en «Persona nueva» |
| 12,0 | **Y queda registrada en la iglesia** | palabra a palabra, 0,067 s entre palabras; el toque en «Agregar» cae en 12,5 | 20,0, blur-out 0,2 s |
| 24,0 | **Cada *reunión* cuenta, y cuenta bien** (*reunión* en itálica dorada) | palabra a palabra; el único dorado del cuerpo junto a la ceja | se queda hasta 28,0 |

Más la ceja «EVENTOS» (Inter, mayúsculas, dorado) que cae en 6,5 sobre la ventana y se va en 24,0.

La frase 3 es textual de la ayuda («Cada persona nueva queda registrada en Membresía, con este evento como la forma en que llegó») y del
sitio («Conectado con Membresía»). La frase 4 es el `titulo` de `modulos.ts`. Ninguna frase depende de un número, de un nombre de evento ni
de un día de la semana: todo eso cambia con la semilla de Kingdom Demo.

### Recorrido sobre la música

| Compás | Clip | Pantalla real (celular, cuenta 103 = Jorge Gallego Gil) y acción | Movimiento |
|---|---|---|---|
| 1 | 0–2 | **Cuadro 0:** Servir, la tarjeta **«Reuniones por reportar»** con su número en rojo y la fila **«Casa de Paz Laureles 1 · Mié, 28 de oct · 2 vencidas · Reportar»** | La frase 1 cae en los cuatro pulsos. 1,5–2,0: la cámara se acerca a la fila |
| 2 | 2–4 | **2,5: toque en «Reportar»** → el reporte de la reunión entra (match cut sobre el toque, 1,03 → 1,00): «Casa de Paz Laureles 1 · Casa de paz · miércoles, 28 de octubre · **Pendiente**», los atajos de fecha con el punto rojo, los pasos **① Asistencia · ② Reporte · ✓ Listo** con su barra, **«0 marcadas» · «Igual que la última vez»**, el buscador y las primeras casillas («Vino 4 de 4») | 3,0–3,5 la cámara abre al general; 3,5 el dedo se posa en «Igual que la última vez» y espera el bajo |
| 3 | **4,0**–6 | **4,0: toque en «Igual que la última vez»** → las filas se marcan a la vez (ámbar), **«4 marcadas»**. 5,0–5,5: la app baja hasta **«Persona nueva» · «Visitantes» · «Total: 4 personas»** | Cae la frase 2. Primer cambio grande: la lista se llena sola |
| 4 | **6,0**–8 | **6,0: toque en «Persona nueva»** → iris desde el dedo → la hoja real **«Persona nueva»** sube desde abajo (Nombres, Apellidos, Indicativo y Teléfono, Mujer / Hombre, «Es un niño o una niña (sin teléfono)», Cancelar / Agregar) | Pico: la hoja llena la ventana. Cae la ceja «EVENTOS» en 6,5. «Datos de ejemplo» desde el cuadro 0 |
| 5 | 8–10 | 8,0: la cámara a la mitad alta de la hoja; se escribe **«Ximena»** (8,0–8,5) y, en 9,0, **«Hoyos Vélez»** (9,0–9,8) | Un movimiento de cámara por compás; la escritura es el movimiento de la app |
| 6 | 10–12 | 10,0: la cámara a la mitad baja; se escribe el teléfono **`5550198765`** (10,0–11,0); 11,5 toque en **«Mujer»**; la cámara abre a la hoja entera con «Agregar» | Ídem |
| 7 | 12–14 | **Respiro.** 12,0 cae la frase 3; **12,5: toque en «Agregar»** → la hoja se cierra y en la lista aparece la fila **«Ximena Hoyos Vélez · Nueva»** ya marcada; «Total: 5 personas» | De aquí a 20 la app va a velocidad normal |
| 8 | 14–16 | 15,0: toque en el **«+»** de Visitantes → 1 · «Total: 6 personas» | Movimiento pequeño: un contador |
| 9 | 16–18 | 16,0: **«+»** → 2 · **«Total: 7 personas»**; 17,0 acercamiento a la línea del total | El número que crece es el movimiento del respiro |
| 10 | 18–20 | 18,0 la cámara a los botones **«No hubo reunión» · «Guardar asistencia»**; 19,5 el dedo llega | |
| 11 | **20,0**–22 | **20,0, segunda subida: toque en «Guardar asistencia»** → el paso ① queda hecho, la **barra salta de 15 % a 66 %** y entra el paso ② **«Reporte de la casa de paz»**: «¿Cómo estuvo la reunión?» · Muy bien / Bien / Difícil · «Tema de la palabra» · «Peticiones de oración». 20,5 toque en **«Muy bien»**; 21,0–21,7 se escribe **«El perdón»**; el dedo baja a «Enviar reporte» | Frase 3 sale. La barra que crece es la prueba de «reporte guiado» |
| 12 | **22,0**–24 | **22,0, el compás más fuerte: toque en «Enviar reporte»** → **«¡Listo!»** (ícono `task_alt`) · **«Casa de Paz Laureles 1, miércoles, 28 de octubre: 7 personas.»** · «Volver a la lista» · «Reportar la siguiente»; arriba el estado ya dice **«Reportada»** y los tres pasos están hechos, la barra al 100 %. 23,0: acercamiento a la tarjeta del «¡Listo!» | La prueba más fuerte del clip: el número, leído a 44 px |
| 13 | **24,0**–26 | **24,0, golpe:** cae la frase 4; la ceja se va; la ventana baja a 0,92 y se corre al borde; la cámara abre apenas para que quepan «Reportada», los pasos hechos y el «¡Listo!» | La frase final sostenida 4 s |
| 14 | 26–28 | Todo quieto salvo la app (el «¡Listo!» real); la subida desde 26,5; 27,9 dip | |
| — | **28,0**–30,5 | **La firma sobre el golpe más fuerte:** `cierre-clip` (fondo azul, la corona se levanta, campanas en 28,38, llamado `prueba`) | La corona es el único gesto de marca |

### El lenguaje del movimiento, en una línea por nivel

- **Cada pulso (0,5 s) entre 0 y 12:** o aterriza una palabra, o un toque real, o la app muestra algo nuevo (una fila que se marca, un
  contador, la hoja que sube, una tecla). Nunca un pulso vacío.
- **Cada compás (2 s):** un movimiento de cámara dentro de la ventana (14 cuadros, `power2.inOut`, blur de render), luego quieta. Nunca la
  cámara y el desplazamiento de la app a la vez.
- **4,0:** el toque en «Igual que la última vez»: Kingdom entra con el bajo. **6,0:** el iris a la hoja «Persona nueva» (el único iris).
  **20,0 y 22,0:** «Guardar asistencia» y «Enviar reporte»: las dos pruebas, una por golpe. **24,0:** la frase final. **28,0:** la corona.
- **12–20:** cero cortes; solo la app a velocidad normal (la hoja que se cierra, dos toques en «+», el dedo que baja).
- Transiciones con causa (dos clases y el cierre): match cut sobre el toque (el reporte que entra en 2,5), iris desde el toque (la hoja), dip
  + corte (a la firma). Sin látigo: un solo mundo.

### Grabaciones que necesita (Kingdom Demo, `capturar.mjs --modo video`)

Una sola escena de **celular**, `tools/ayuda/escenas/clips/eventos-casa-de-paz.mjs` (`movil: true`, `toque: false`), con la cuenta 103
(el servidor Jorge Gallego Gil, responsable de la primera casa de paz de la semilla) y tramos: `inicio` (Servir) · `reportar` · `igual` ·
`abajo` · `nueva` · `agregar` · `visitantes` · `guardar` · `listo`. Está completa, lista para copiar, en SPEC §3. Lo que la semilla
garantiza (`_demo_eventos.php`): la cuenta de servidor es responsable de la primera casa de paz (línea 215), esa casa tiene sus últimas
reuniones sin reportar (línea 178: «2 vencidas» en la tarjeta), la categoría Casa de Paz cuenta visitantes y pide el formulario «Reporte de
la casa de paz» con «¿Cómo estuvo la reunión?» obligatoria y «Tema de la palabra» opcional (líneas 61–72). Lo único que la semilla no
garantiza es cuántas personas marca «Igual que la última vez»: la escena lo comprueba con una `ref` y, si son menos de tres, se niega y entra
el plan B (SPEC §3).

### De 4:5 a 9:16

Misma línea de tiempo, misma grabación, mismas cajas de `pasos.json`; cambia el encuadre exactamente como en Membresía: titular 80 → 104 px
(máx. 3 líneas: la frase 4 se parte «Cada *reunión* / cuenta, / y cuenta bien»), ventana 880×1050 que sangra → 960×850 completa entre 480 y
1330, cámara G 2,256 → 2,462 ppc, firma `cierre-clip` → `cierre-corto`.

---

## Alternativas que se descartaron (una línea cada una)

- **«Miércoles sin señal»** (reportar en la casa sin internet: «Sin señal», «Espera señal», «1 sin enviar», y la cola que se envía sola al
  volver): es la promesa del sitio que falta aquí, pero repite el gancho y el 4,0 de Membresía en la misma página de inicio; va al
  recorrido de 60–75 s, donde cabe entera.
- **«El lunes del pastor»** (dos mundos: Jorge reporta y, en 24,0, el látigo al celular del pastor con la ficha de la casa: «Última reunión ·
  7 personas», promedio, tendencia, la barra de la meta): el resultado para la iglesia es tentador, pero mete otra cuenta y otra pantalla en
  los últimos 4 s, el estado de la casa seguiría «Retrasado» (quedan dos vencidas) y la frase final pide quietud; el tablero y la ficha van al
  recorrido.
- **«Pendiente, Reportada»** (el estado del reporte como protagonista: abrir en la lista de Eventos con «Retrasado» en rojo y cerrar en
  «Reportada» en verde, match cut sobre la píldora): abre con el producto mostrando un problema y el semáforo del día depende de la semilla;
  la píldora «Reportada» sí se ve, pero como parte del «¡Listo!».
- **«No hubo reunión»** (el gesto más corto de Eventos: un toque, el motivo, listo): honesto y raro en un software, pero cuenta una reunión que
  no pasó: no sirve para «cuenta bien».
- **«El mapa de la ciudad»** (escritorio con `.k-ventana-escritorio`: «Dónde viven» y «Zonas sin evento»): es la pantalla del que coordina, no
  del pastor que no conoce Kingdom, y en 4:5 y 9:16 pide tres o cuatro recortes de escritorio.
- **«Ximena vino por primera vez»** (abrir con la hoja «Persona nueva» y su nombre escribiéndose): la persona nueva es el corazón del clip,
  pero abrir escribiendo un nombre en un formulario es exactamente el cuadro 0 de Valeria; aquí la hoja llega en el pico (6,0) y la frase 3
  dice lo que pasa con ella.

## Riesgos y dudas (el detalle en SPEC §5)

- **«Igual que la última vez»** marca a las personas de la última reunión con asistencia de la casa (`igualQueLaUltima` →
  `ultima_personas`); la semilla deja las últimas tres reuniones de esa casa sin reportar, así que «la última vez» es la cuarta hacia atrás y
  sus personas salen de la copia de v1: no se sabe cuántas son hasta restaurar el volcado. La escena exige ≥ 3 o se niega; el plan B marca
  tres casillas a mano en 4,0 · 4,5 · 5,0 y la frase 2 pasa a «Marca quién vino.».
- **La hoja «Persona nueva» busca duplicados** mientras se escribe el nombre; «Ximena» no está en el banco de nombres de la demo
  (`DEMO_NOMBRES_F`), así que no debería salir «¿Ya está registrada?». Si sale, cambia el nombre, no el guion.
- **El cargador de la app** (`loading.wrap`, la K animada a los 150 ms) podría asomarse en «Guardar asistencia» y «Enviar reporte» si la API
  local tarda; se ve en la grabación y, si asoma, se corta en la pausa.
- **Los textos exactos** («Vino 4 de 4», los nombres de las personas, «Casa de Paz Laureles 1», «Mié, 28 de oct») cambian con la semilla del
  día; ninguna frase depende de ellos.
