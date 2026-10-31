# Recorrido de Mi iglesia — «Se enteró toda la iglesia… y encontró su lugar» (historia elegida)

2026-10-30 · El recorrido del módulo para la página `/mi-iglesia` del sitio, YouTube y presentaciones (decisión 218 del dueño:
`KingdomApp/docs/videos/README.md` → Clip del sitio → **recorrido del módulo**). Parte del clip publicado
[«Se enteró toda la iglesia»](../clip-sitio-mi-iglesia/STORY.md) y sigue con lo que el portal le da a cada miembro. **El dueño ya no revisa
guiones:** la historia la decide la dirección creativa y pasa directo a [SPEC.md](SPEC.md). El sistema de la serie
([Membresía → STORY §3](../clip-sitio-membresia/STORY.md)) se respeta: frases cortas, la misma ventana, las mismas transiciones con causa,
los sonidos de acción del kit y la marca solo al final. El formato es el de [recorrido-academia](../recorrido-academia/STORY.md): dos
escenarios (celular y escritorio) unidos por el látigo horizontal.

**Lo que no se reabre:** **16:9 (1920×1080)**, **97,0 s** (92 de cuerpo + el cierre del Comercial de 5) · sin voz, texto quemado ·
«Product Launch» alargada con **una sola costura** en el borde de compás: la misma edición de Academia, medida otra vez aquí (SPEC §0) · la
app real de Kingdom Demo, nunca un teléfono dibujado · nada inventado, nada de «Próximamente» · la entrada a la app no se muestra (hoy solo
se entra con Google y la herramienta no la graba; la de WhatsApp no existe) · **cierre del Comercial** con el llamado `prueba`. El README
pide 60–75 s para el recorrido; los ~100 s los decidió el dueño para la serie (se anota en el README cuando se publique, como en los otros).

## 1. La historia

**Nombre:** «Se enteró toda la iglesia… y encontró su lugar».

**Idea en una frase:** los primeros 28 s son el clip tal cual (Gabriela ve el anuncio del congreso en Mi iglesia, le da «Amén», se inscribe
con su esposo y su boleta queda en el celular); después Gabriela cierra la boleta y sigue usando su iglesia en el bolsillo: **encuentra la
comunidad de Jóvenes, se une y pide que un líder la acompañe**; en el computador, **el pastor Andrés lee su mensaje y la toma**; en el
celular de ella aparece **«Andrés te acompañará»**; ella marca **«Lo hice»** en su devocional de la mañana; el pastor abre el tablero del
Portal y ve **a cuántos llegó el anuncio del congreso y quién respondió: Gabriela, con su 🙌**; y el video termina en el celular de
**alguien que acaba de llegar**, con su bienvenida.

**El recurso: datos que viajan.** El clip ya tenía uno (el anuncio que se vuelve boleta). El recorrido suma tres del mismo tipo:

1. **Su mensaje:** Gabriela escribe «Voy al congreso y quiero conocerlos.» en su celular (39–41 s) y, un látigo después, ese mensaje está en
   la bandeja de Contactos del pastor, con su nombre y «hace 1 min» (44 s).
2. **El líder:** el nombre de Andrés aparece primero en la lista de «Líderes» de Jóvenes (34 s), después en el escritorio, tomando el contacto
   (46 s), y vuelve al celular de ella como **«Andrés Felipe Restrepo Gómez te acompañará»** (52 s, el golpe más fuerte de la parte 2).
3. **Su «Amén»:** el toque del segundo 4 del clip reaparece al final de la parte 2 (74,5 s): en el escritorio, la novedad «Inscripciones
   abiertas» dice a cuántas personas llega y, al filtrar por 🙌, **Gabriela Hinestroza Perea** es la primera de la lista. La pregunta del
   gancho («¿Se enteró toda la iglesia?») tiene respuesta en pantalla, con cifras de la app y un nombre.

**La forma:** la del clip (ventana del celular a la derecha, frases a la izquierda) más el escenario del **escritorio**, al que se llega con
el **látigo horizontal** (izquierda = al escritorio; derecha = de vuelta al celular), como en Academia. El alcance se abre sin decirlo:
**una persona → su comunidad → quien la cuida → su hábito → toda la iglesia → quien llega mañana**.

**Por qué es la mejor para un pastor que no conoce Kingdom:** el clip ya lo convenció de que el anuncio llega y la boleta queda en el
bolsillo. El recorrido contesta lo que sigue preguntando un pastor: «¿y después del evento, la gente se conecta?» (comunidades y un líder que
la acompaña), «¿crecen entre domingo y domingo?» (objetivos en curso), «¿cómo sé si se enteraron?» (el tablero y quién respondió) y «¿y el
que llega nuevo?» (la bienvenida). Son cinco bloques reales del sitio (`modulos.ts` → mi-iglesia → `bloques`: Comunidades, Objetivos en
curso, Un tablero para ti, Novedades, Bienvenida con tu QR), así que el video y la página dicen lo mismo, y todos son **del miembro o para
él**: el único escritorio que se ve es el del pastor que la cuida.

## 2. Frases en pantalla (una a la vez; Fraunces 560, 84 px)

| Segundo | Frase | Dónde | Cómo entra | Se va |
|---|---|---|---|---|
| 0,0 | **¿Se enteró / toda la iglesia?** | columna izquierda | una palabra por pulso (0,0 · 0,5 · 1,0 · 1,5), como el clip | 4,0 |
| 4,0 | **Llega a cada celular.** | izquierda | la línea entera, blur 8 → 0 | 6,0 |
| 12,0 | **Y se inscribe / con su familia** | izquierda | palabra a palabra | 20,0 |
| 24,0 | **Su boleta, / también sin señal.** (nueva: la del clip pasa al final) | izquierda | palabra a palabra | 27,9 |
| 28,0 | **Encuentra / su comunidad.** | izquierda | palabra a palabra | 43,9 |
| 44,0 | **Su mensaje llega a los líderes.** | arriba (escritorio) | palabra a palabra | 51,9 |
| 52,0 | **Y un líder / la acompaña.** | izquierda | palabra a palabra | 55,9 |
| 56,0 | **Crece / paso a paso.** | izquierda | palabra a palabra | 67,9 |
| 68,0 | **Y sabes quién respondió.** | arriba (escritorio) | palabra a palabra | 75,9 |
| 76,0 | **A quien llega, / una bienvenida.** | izquierda | palabra a palabra | 83,9 |
| 84,0 | **Tu iglesia, en el *bolsillo* / de cada miembro** (*bolsillo* en itálica dorada; el `titulo` de `modulos.ts`) | izquierda | palabra a palabra | se queda hasta 92,0 |

Más la ceja «MI IGLESIA» (Inter 700, 28 px, dorada), que entra en 6,5 como en el clip, acompaña a cada frase en su escenario y se va en 84,0.
Leídas solas, las once frases son el argumento completo; vistas sin sonido, las imágenes cuentan lo mismo.

De dónde sale cada frase (nada inventado): la 4 dice lo que la app dice en el resultado de la inscripción («Tu boleta ya está en Mis
boletas: también se ve sin señal.»); la 5 responde a la pantalla vacía de Comunidades («…Encuentra la tuya.», `po2.vacio_texto`); la 6 es el
portal por dentro (el pedido de «Conectar con un líder» llega a los líderes de la comunidad: `portal.md` → Comunidades); la 7 es el bloque
«Comunidades» del sitio («pide hablar con un líder que lo acompañe») y lo que la app escribe («{líder} te acompañará»); la 8 es el bloque
«Objetivos en curso» («cada persona avanza paso a paso»); la 9 nombra la columna «Respuesta» del tablero y la lista «Quién reaccionó»; la 10
es el bloque «Bienvenida con tu QR» («ve una bienvenida guiada»). Ninguna depende de un número, una fecha o un nombre de la semilla.

## 3. Recorrido sobre la música (compases de 2 s; la grilla exacta en SPEC §0)

| Compás | Video | La pista | Pantalla real y acción | Movimiento |
|---|---|---|---|---|
| 1–14 | **0–28** | 14,05–42,05 | **El clip, cuadro por cuadro** (su grabación, sus cortes, su iris y sus cámaras), llevado a 16:9: la ventana del celular a la derecha, las frases a la izquierda. Sin la ventana a un lado, sin la subida ni la firma; la frase del sitio pasa al final y en el 24,0 entra «Su boleta, también sin señal.»; en el 26,0 la cámara baja para que se vea «Cerrar» | El iris del 6,0 y el corte del 22,0, como en el clip |
| 15 | **28,0**–30 | 42,05 (1,00, el más fuerte) | **Toque en «Cerrar»** de la boleta en grande → «Mis boletas» con la barra de abajo; 29,0 toque en **«Comunidades»** → «Todavía no estás en una comunidad» | Cae «Encuentra su comunidad.» Corte sobre el toque |
| 16 | 30–32 | 44,05 | 30,0 «Explorar comunidades» → la lista con «Para ti»; 31,0 la app baja hasta **«Jóvenes»** | La app se mueve; la cámara, quieta |
| 17 | **32,0**–34 | 22,05 (costura) | **Toque en la tarjeta de Jóvenes → iris → la comunidad**: su portada, «Miembros: N», «Un lugar para crecer juntos en la fe…», «Unirme» | El único iris de la parte 2, encima de la costura |
| 18 | 34–36 | 24,05 (respiro) | La cámara baja a **«Conectar con un líder»** y a **«Líderes»: Andrés Felipe Restrepo Gómez** y David | Un movimiento |
| 19 | **36,0**–38 | 26,05 | **«Unirme»**: el confeti de la app; ya es parte | Lo hace la app |
| 20–21 | **38,0**–42 | 28,05–32,05 | **«Conectar con un líder»** → el diálogo; se escribe **«Voy al congreso y quiero conocerlos.»** | El respiro: la cámara quieta |
| 22 | **42,0**–44 | 32,05 | **«Enviar»** → «Pediste conectar con un líder · Un líder te escribirá pronto.» | Confirmación |
| 23 | **44,0**–46 | 34,05 (0,93, segunda subida) | **Látigo horizontal al escritorio: el pastor (101) en Contactos.** Abajo de la bandeja, la fila nueva: **Gabriela Hinestroza Perea · Jóvenes · hace 1 min · «Voy al congreso y quiero conocerlos.»** | Cae «Su mensaje llega a los líderes.»; la cámara va de su nombre a «Tomar» |
| 24–26 | **46,0**–52 | 36,05–42,05 | **«Tomar»** → el confeti en la fila y el detalle: «Tomado · Lo tomó Andrés…», su mensaje, «Llamar», «Escribir por WhatsApp», «Ver su ficha (Membresía)» | Toque, resultado, la cámara al detalle |
| 27–28 | **52,0**–56 | 42,05 (1,00) | **Látigo horizontal de vuelta al celular de Gabriela:** en Jóvenes, **«Andrés Felipe Restrepo Gómez te acompañará · Te escribirá pronto para conocerte.»** | Cae «Y un líder la acompaña.»; un punch a la tarjeta y la cámara baja a la barra |
| 29–30 | **56,0**–60 | 46,05 (0,98) | Toque en **«Objetivos»** → «Mis objetivos»: **«Un devocional cada mañana · Paso 13 de 14 · 86 %»** (real); toque en la tarjeta → su paso de **hoy** | Cae «Crece paso a paso.» |
| 31–32 | **60,0**–64 | 50,05 (clímax) | **«Lo hice»** → «¡Listo! Marcamos «…» como hecho.» y el anillo crece a **93 %** | El golpe del clímax es el toque de ella |
| 33–34 | **64,0**–68 | 54,05 | La app baja a **«Todos los pasos»**: una fila de ✓, una por mañana | Quieto |
| 35–36 | **68,0**–72 | 58,05 (clímax, segunda frase) | **Látigo horizontal al escritorio: el tablero del Portal** (las cifras con «Datos de ejemplo»); 70,0 la app baja a **«Publicaciones»**: «Inscripciones abiertas · Toda la iglesia · Alcance · Reacciones · Respuesta» | Cae «Y sabes quién respondió.» |
| 37–38 | **72,0**–76 | 62,05 | Toque en **«Inscripciones abiertas»** → «Quién reaccionó» con sus conteos; 74,0 toque en **🙌** → **«Gabriela Hinestroza Perea 🙌»** arriba de la lista (74,5) | El «Amén» del segundo 4 vuelve |
| 39–42 | **76,0**–84 | 66,05–74,05 (salida) | **Látigo horizontal de vuelta al celular, pero de otra persona:** la bienvenida de quien acaba de llegar (cuenta 104): el logo de la iglesia que entra con su resorte, **«Hola, Lucía»**, el título palabra por palabra, las luces que flotan; 80,0 **«Empezar mis primeros pasos»** → el camino de sus primeros pasos | Cae «A quien llega, una bienvenida.»; la música baja sola |
| 43–46 | **84,0**–92 | 74,05–82,05 | Quieto: el camino de la bienvenida | Cae la frase del sitio; la ventana se hace a un lado; la subida; el dip |
| — | **92,0**–97,0 | 82,05 → fin (el último acorde, que se apaga solo) | **`cierre-comercial`** (noche, «Kingdom es para *toda la iglesia*», «Prueba gratis 30 días», `kingdom-sitio.web.app`), campanas en 92,38 | El único gesto de marca |

### Lo que este recorrido hace distinto dentro del sistema (y por qué)

- **El paso del clip a la parte 2 no es un látigo.** Es la misma persona en el mismo celular, así que la cadena sigue objeto a objeto: tocar
  «Cerrar» en la boleta y tocar «Comunidades» en la barra de abajo. El látigo horizontal se guarda para el cambio de persona o de aparato.
- **Cuatro látigos horizontales y un solo iris.** Ida y vuelta al escritorio dos veces (44,0 → 52,0 y 68,0 → 76,0); la segunda vuelta no
  regresa a Gabriela sino a alguien nuevo: el último plano es el primer día de otra persona. El iris del 32,0 (de la tarjeta de Jóvenes a la
  comunidad) cae encima de la costura de la música: la imagen se abre desde el toque y el oído no busca nada.
- **El golpe más fuerte de la parte 2 (52,0) es una frase de la app, no un efecto:** «Andrés Felipe Restrepo Gómez te acompañará». Es la
  respuesta humana a todo lo anterior y el centro emocional del video.
- **El clímax de la música (60–76) es la persona y después la iglesia:** el «Lo hice» de Gabriela en el primer golpe del clímax y, en la
  segunda frase, el tablero que cuenta a toda la iglesia y vuelve a nombrarla a ella.
- **El cierre es el del Comercial (5 s, 16:9)**, no la firma corta del clip, y llega sobre el final natural de la pista: no hay fundido.

## 4. Alternativas descartadas (una línea cada una)

- **Empezar la parte 2 en la bienvenida** (lo que proponía el STORY del clip): la bienvenida es de otra persona y cortaba la historia de
  Gabriela justo después del gancho; queda como el último plano, donde abre la escala a «quien llega mañana».
- **Matrimonios en vez de Jóvenes** (Gabriela está casada): es «con aprobación», pide «Solicitar» y que un líder apruebe otro día, y sus
  líderes de la demo no son el pastor de las capturas; Jóvenes es abierta, la de la historia de la semilla (`_demo_portal_6_recorrido.php`)
  y la del congreso del clip.
- **Mujeres** (la que la app le sugiere «Para ti»): sus dos líderes son fichas sin cuenta en Kingdom Demo; solo el administrador podría tomar
  el contacto y la tarjeta diría que la acompaña alguien que no aparece en «Líderes».
- **Comunicados** (crear uno y ver «Cómo le fue»): es un formulario de escritorio largo para 8 s y su resultado (cifras de entrega) ya lo
  cuenta, mejor y con un nombre, la novedad con «Quién reaccionó».
- **Mi ficha** (corregir sus datos): real y útil, pero quieta; no tiene un resultado que se vea en un pulso.
- **Completar el objetivo entero** (el último paso, con el confeti de «¡Completaste el objetivo!»): obligaba a reescribir su avance en la
  demo por SQL; el paso de hoy con el anillo que crece cuenta lo mismo sin tocar el motor.
- **El QR de bienvenida en el escritorio** antes del último plano: un segundo QR después de la boleta confunde; la frase 10 lo nombra sin
  mostrarlo.

## 5. Lo que la demo tiene (verificado el 2026-10-30, en código y en la base local de capturas)

- **Cuentas de captura** (`backend/cron/jobs/_demo_capturas.php`): 101 el administrador (en la demo, **Andrés Felipe Restrepo Gómez**, el
  pastor), 104 una servidora (**Lucía Ruiz Montoya**) y 105 la miembro (**Gabriela Hinestroza Perea**, nacida en 1991, casada con Simón
  Ríos Arango).
- **La historia de la semilla** (`_demo_portal_6_recorrido.php`): Gabriela entró por el QR General, terminó la bienvenida, está en Jóvenes
  con un contacto que tomó su primer líder, tiene un objetivo en curso al día y está inscrita en el Congreso de Jóvenes. La base local de
  capturas lo confirma: contacto «tomado» por la ficha de 101, «Un devocional cada mañana» activo en el paso 12 de 14.
- **Comunidades** (`_demo_portal_1_comunidades.php`): Jóvenes, Matrimonios, Mujeres, Hombres y Deportes; en la base local, los líderes de
  Jóvenes son las fichas de 101 y 106. Jóvenes es abierta, con la descripción «Un lugar para crecer juntos en la fe, hacer amigos y servir.
  Nos vemos los sábados.»; la bandeja de Contactos trae pendientes de 3, 30 y 55 horas en Jóvenes y uno en Mujeres.
- **La pantalla de la comunidad** (`frontend-v2/src/app/pages/mi/comunidad.page.ts`): «Unirme» con el confeti de la app (`celebrar`), «Conectar
  con un líder» con su diálogo (`comunidad-mensaje.component.ts`) y la tarjeta `#po2-contacto` que dice «Un líder te escribirá pronto.» o
  «{líder} te acompañará». La bandeja (`portal/contactos.page.ts`) ordena los pendientes del más viejo al más nuevo y «Tomar» celebra la fila y
  abre el detalle.
- **Objetivos** (`_demo_portal_2_objetivos.php` y `pages/mi/objetivo.page.ts`): «Un devocional cada mañana», 14 pasos (Salmo 23, Mateo
  11:28-30…); en el detalle, «Lo hice» marca el paso sin esperar la fecha, muestra «¡Listo! Marcamos «{paso}» como hecho.» y el anillo crece.
- **Novedades y tablero** (`portal/tablero/publicaciones.component.ts`, `portal/novedad-editar.page.ts`, `backend/_datos/portal_publicaciones.php`):
  la tabla de las publicaciones recientes con «Alcance», «Reacciones» y «Respuesta», con el título enlazado a la novedad; en la novedad,
  «Quién reaccionó» con un botón por reacción y la lista de personas de la más reciente a la más vieja.
- **La bienvenida** (`pages/mi/bienvenida/portada.component.ts`): el logo con su resorte, «Hola, {nombre}», el título palabra por palabra,
  dos luces que flotan y «Empezar mis primeros pasos»; la escena de la ayuda `escenas/mi-iglesia/la-bienvenida.mjs` ya la recorre borrando el
  avance de la persona.

## 6. Riesgos (el detalle en SPEC §5)

- **Gabriela en Jóvenes con 35 años:** es la comunidad que eligió la semilla y la del congreso; en la app no se ve su edad. Si el dueño lo
  objeta al ver el render, la escena cambia a Mujeres con un líder con cuenta (SPEC §5).
- **Dos grabaciones del mismo instante:** la toma del contacto se graba en el escritorio (la que se ve) y otra vez en el celular, fuera de
  cuadro (para que su tarjeta diga «te acompañará»). Las dos las hace el mismo pastor sobre la misma demo: la imagen es coherente.
- **La boleta de la parte 2 es una fila de la demo ajustada** para que su código sea el del clip (FM75UZ); el corte del 28,0 va de la boleta
  en grande de la grabación del clip a la lista de la grabación nueva, y el nombre y el código coinciden.
- **El paso de «hoy» del devocional** depende de la hora de la grabación: la escena fija su día en hoy para que diga «Hoy».
- **La costura de la música** es la de Academia, medida dos veces (allá y aquí), pero nadie la ha oído: se oye en la vista previa antes del
  render.
