# Recorrido de Academia — «La clase ya empezó… y lo que sigue» (historia elegida)

2026-10-30 · El recorrido del módulo para la página `/academia` del sitio, YouTube y presentaciones (decisión 218 del dueño:
`KingdomApp/docs/videos/README.md` → Clip del sitio → **recorrido del módulo**). Parte del clip publicado
[«La clase ya empezó»](../clip-sitio-academia/STORY.md) y sigue con lo que se puede lograr con el módulo. **El dueño ya no revisa guiones:**
la historia la decide la dirección creativa y pasa directo a [SPEC.md](SPEC.md). El sistema de la serie
([Membresía → STORY §3](../clip-sitio-membresia/STORY.md)) se respeta: mismas frases cortas, misma ventana, mismas tres transiciones,
mismos sonidos de acción y la marca solo al final.

**Lo que no se reabre:** **16:9 (1920×1080)**, ~100 s (queda en **97,0 s**: 92 de cuerpo + el cierre del Comercial de 5) · sin voz, texto
quemado · «Product Launch» alargada con **una sola costura** en el borde de compás (SPEC §0) · la app real de Kingdom Demo, nunca un
teléfono dibujado · nada inventado, nada de «Próximamente» · **cierre del Comercial** con el llamado `prueba`. El README pide 60–75 s para
el recorrido; los ~100 s los decidió el dueño para esta pieza (se anota en el README cuando se publique).

## 1. La historia

**Nombre:** «La clase ya empezó… y lo que sigue».

**Idea en una frase:** los primeros 28 s son el clip tal cual (el profesor muestra el código, la alumna lo escribe, quien coordina aprueba la
graduación y sale el certificado de Andrea con su código); después la cámara se abre del grupo a la escuela entera y muestra, una por una,
las cinco cosas que hacen posible esa graduación —armar el curso, el examen que se califica solo, la sábana que dice quién va en riesgo, el
tablero de toda la escuela— y termina donde empezó a importar: **un desconocido escribe el código del certificado de Andrea y la página
pública dice «Certificado válido»**.

**El recurso: dos datos que viajan.** El clip ya tenía uno (los cuatro dígitos del código de asistencia: profesor → alumna → contador). El
recorrido suma dos más, del mismo tipo:

1. **La nota de la alumna:** la misma alumna de la parte 1 (cuenta 104) presenta el «Quiz de los evangelios»; la app la califica sola al
   cierre («Tu nota 5 / 5») y, un látigo después, ese **5** aparece en la sábana del profesor, en su fila.
2. **El código del certificado:** «7YU79-NNB7A» se ve en el certificado de Andrea (24–28 s) y vuelve en la parte final: alguien que no
   tiene cuenta lo escribe en `/verificar` y aparece su nombre, su curso y su iglesia.

**La forma:** la del clip (ventana del celular a la derecha, frases a la izquierda, látigo vertical entre celulares) más un segundo
escenario, **el escritorio**, al que se llega con el **látigo horizontal** (izquierda = al escritorio; derecha = de vuelta al celular). El
movimiento del alcance cuenta la historia sin decirlo: **una clase → un curso → una alumna → un grupo → toda la escuela → cualquiera**.

**Por qué es la mejor para un pastor que no conoce Kingdom:** el clip ya lo convenció de que la clase funciona sin papel; el recorrido le
contesta la pregunta que sigue —«¿y el resto de la escuela?»— con cinco escenas que reconoce de su propia escuela de liderazgo: armar el
curso nuevo, calificar exámenes, saber quién se está quedando, ver todo sin pedir informes y que el certificado valga fuera de la iglesia.
Cada escena es un bloque real del sitio (`modulos.ts` → academia → `bloques`), así que el video y la página dicen lo mismo.

## 2. Frases en pantalla (una a la vez; Fraunces 560, 84 px)

| Segundo | Frase | Dónde | Cómo entra | Se va |
|---|---|---|---|---|
| 0,0 | **La clase / ya empezó.** | columna izquierda | una palabra por pulso (0,0 · 0,5 · 1,0 · 1,5) | 3,9, con el látigo |
| 4,0 | **Sin listas / de papel.** | izquierda | la línea entera, blur 8 → 0 | 11,9, con el látigo |
| 12,0 | **Quien cumple, / se gradúa.** | izquierda | palabra a palabra | **27,9** (en el clip se iba en 20,0: aquí acompaña la aprobación y el certificado) |
| 28,0 | **Un curso, en cinco pasos.** | arriba (escritorio) | palabra a palabra | 43,9 |
| 44,0 | **Exámenes que / se califican solos.** | izquierda | palabra a palabra | 55,9 |
| 56,0 | **Sabes quién / va en riesgo.** | izquierda | palabra a palabra | 67,9 |
| 68,0 | **Toda tu escuela, de un vistazo.** | arriba (escritorio) | palabra a palabra | 75,9 |
| 76,0 | **Y cualquiera / lo verifica.** | izquierda | palabra a palabra | 83,9 |
| 84,0 | **Forma a los *líderes* / que tu visión necesita** (*líderes* en itálica dorada; el `titulo` de `modulos.ts`) | izquierda | palabra a palabra | se queda hasta 92,0 |

Más la ceja «ACADEMIA» (Inter 700, 28 px, dorada), que entra en 6,5 como en el clip, acompaña a cada frase en su escenario y se va en 84,0.
Leídas solas, las nueve frases son el argumento completo; vistas sin sonido, las imágenes cuentan lo mismo.

De dónde sale cada frase (nada inventado): «exámenes que se califican solos», «quién está en riesgo» y «un QR que cualquiera verifica» son
del texto de los bloques del sitio; «un asistente de 5 pasos arma el curso», también; «de un vistazo» describe el tablero de Academia (AC8)
sin prometer nada que no muestre la pantalla.

## 3. Recorrido sobre la música (compases de 2 s; la grilla exacta en SPEC §0)

| Compás | Video | La pista | Pantalla real y acción | Movimiento |
|---|---|---|---|---|
| 1–14 | **0–28** | 14,05–42,05 | **El clip, cuadro por cuadro** (su grabación, sus cortes y sus cámaras), llevado a 16:9: la ventana del celular a la derecha, las frases a la izquierda. Sin la ventana a un lado en 24,0 ni la firma | Los tres látigos verticales y los dos iris del clip |
| 15 | **28,0**–30 | 42,05 (1,00, el más fuerte) | **Látigo horizontal al escritorio** (quien coordina, 101): «Cursos» → toque «Nuevo curso» (29,0) → «En blanco» (30,0) | Cae «Un curso, en cinco pasos.» |
| 16 | 30–32 | 44,05 | «Paso 1 de 5 · Datos, modalidad y visibilidad»: se escribe «Matrimonios fuertes» | La cámara sobre la barra de avance y el nombre |
| 17 | **32,0**–34 | 22,05 (costura) | «Paso 2 de 5 · Materias y clases»: «Comunicación» (Escuchar con amor, Hablar con verdad) y «Finanzas en casa» | Cada paso en un pulso fuerte; la barra se llena de a un segmento |
| 18–21 | 34–42 | 24,05–32,05 (respiro) | «Paso 3 de 5» (36,0) · «Paso 4 de 5» (38,0) · «Paso 5 de 5» (40,0) | El respiro: la cámara no se mueve; solo cambian los pasos |
| 22 | 42–44 | 32,05 | Toque «Publicar» (42,0) → **«¡Publicado!»** (42,5) | Confirmación |
| 23 | **44,0**–46 | 34,05 (0,93, segunda subida) | **Látigo horizontal de vuelta al celular: la alumna (104)** presenta el «Quiz de los evangelios»: «Pregunta 1 de 3», el reloj de la ventana corriendo | Cae «Exámenes que se califican solos.» |
| 24–26 | 46–52 | 36,05–42,05 | Una respuesta por golpe: «Cuatro» (46,0) · «Verdadero» (48,0) · «Pablo» (50,0); «Revisar» → «Respondiste 3 de 3 · No hay que entregar…» con el reloj ya en **«0:01»** (51,0); «La evaluación cerró. Calculando tu nota…» (51,5) | Toque, pulso, toque |
| 27 | **52,0**–54 | 42,05 (1,00) | **«Tu nota · 5 / 5 · Alcanzó la nota mínima»**: la app la calificó sola | El punch más grande de la parte 2 |
| 28 | 54–56 | 44,05 | Las tres preguntas con «Correcta» | La cámara baja a la lista |
| 29 | **56,0**–58 | 46,05 (0,98) | **Látigo vertical hacia abajo, de vuelta al profesor (103):** la sábana de notas, en la fila de la alumna: su **5** ya está en la columna del quiz | Cae «Sabes quién va en riesgo.» |
| 30 | 58–60 | 48,05 | Los filtros del semáforo: «Cumple · En riesgo · No cumple» con sus cuentas | La cámara sube a los filtros |
| 31–34 | **60,0**–68 | 50,05–58,05 (clímax) | **Toque «En riesgo» (60,0)**: la tabla queda con los que están en riesgo; la tabla se corre hasta «Final» (62,0) y se ve el ícono de cada uno con su nota (64,0) | La sábana a velocidad real |
| 35–38 | **68,0**–76 | 58,05–66,05 (clímax, segunda frase) | **Látigo horizontal al escritorio:** el tablero de Academia (101): las cifras del día → «Alumnos en riesgo» (70,0) → toque en la primera persona (72,0) → su **ficha académica** entra por la derecha (72,5) | Cae «Toda tu escuela, de un vistazo.» |
| 39–42 | **76,0**–84 | 66,05–74,05 (salida) | **Látigo horizontal de vuelta al celular: `/verificar`**, la página pública. Se escribe «7YU79-NNB7A» (77,0), toque «Verificar» (78,0) → **«Certificado válido» · Andrea Perea López · Fundamentos bíblicos** (80,0) | Cae «Y cualquiera lo verifica.»; la música baja sola |
| 43–46 | **84,0**–92 | 74,05–82,05 | Quieto: el certificado verificado | Cae la frase del sitio; la ventana se hace a un lado; la subida; el dip |
| — | **92,0**–97,0 | 82,05 → fin (el último acorde de la pista, que se apaga solo) | **`cierre-comercial`** (noche, «Kingdom es para *toda la iglesia*», «Prueba gratis 30 días», `kingdom-sitio.web.app`), campanas en 92,38 | El único gesto de marca |

### Lo que este recorrido hace distinto dentro del sistema (y por qué)

- **Dos escenarios.** El clip vive entero en el celular; el recorrido alterna celular y escritorio, porque dos de las cinco tareas son de
  escritorio en la vida real (quien coordina arma cursos y mira el tablero en el computador). El cambio de escenario es siempre el látigo
  horizontal y la dirección cuenta (izquierda = al escritorio, derecha = de vuelta), como el vertical cuenta «al otro / de vuelta».
- **La costura de la música cae dentro de un paso del asistente** (32,0): ahí la imagen corta en un golpe y la frase está quieta, así que
  ni la vista ni el oído buscan nada. La pista repite su respiro y su segunda subida: el recorrido tiene dos «segundas subidas» y las dos
  terminan en el golpe más fuerte (28,0 y 52,0), una para el certificado de Andrea y otra para la nota de la alumna.
- **El examen se califica solo de verdad.** La alumna no toca «Entregar» (no existe: «No hay que entregar»); el reloj de su ventana llega a
  cero y la app calcula la nota. El corte del 51,0 salta el tiempo de espera y lo dice el propio reloj, que pasa de «0:4x» a «0:01».
- **El cierre es el del Comercial (5 s, 16:9)**, no la firma corta del clip, y llega sobre el final natural de la pista: no hay fundido.

## 4. Alternativas descartadas (una línea cada una)

- **«Un semestre en 90 segundos» (una sola alumna de principio a fin):** de la inscripción al certificado propio; la alumna de la demo
  tiene 50 % de asistencia y no se gradúa, y pedía inventar medio semestre por SQL.
- **«El curso en línea con video» como capacidad:** la «Inducción a los departamentos» de Kingdom Demo no tiene videos (lecciones de texto
  y enlaces de lectura); mostrarla vendería mal el punto «Cursos en línea con video» y agregar un video de YouTube a la demo es meter
  contenido de terceros en la grabación.
- **«La entrega con foto»:** la entrega de «Fundamentos bíblicos» acepta enlace o PDF, no imagen; habría que cambiar su configuración y
  fabricar una foto de un trabajo. Queda para cuando la demo tenga una entrega con imagen.
- **«El banco de preguntas pegando texto» (escritorio):** es la herramienta del profesor y se ve como escribir en un formulario; el examen
  que se califica solo prueba lo mismo con un resultado que un pastor entiende sin explicación.
- **El tablero como cierre (en vez de la verificación):** termina en cifras; la verificación termina en una persona, Andrea, y en la frase
  del sitio sobre los líderes.
- **Empezar la música más atrás (2,05) para tener 12 s más sin costura:** obliga a poner algo antes del gancho del clip, que es el cuadro 0.

## 5. Lo que la demo tiene (verificado el 2026-10-30, en código)

- **Cuentas de captura** (`backend/cron/jobs/_demo_capturas.php`): 101 el administrador (coordina Academia), 103 el profesor de todos los
  grupos, 104 la alumna inscrita en «Fundamentos bíblicos».
- **«Fundamentos bíblicos»** (`_demo_academia.php` → `demoAcFundamentos`): con notas (escala 5, mínima 3), criterios asistencia 75 % y
  promedio 3; actividades «Participación», «Línea de tiempo del Antiguo Testamento» (entrega por enlace), **«Quiz de los evangelios»**
  (3 preguntas del banco: «¿Cuántos evangelios hay en el Nuevo Testamento?», «El evangelio de Lucas lo escribió un médico.», «¿Quién
  escribió la mayoría de las cartas del Nuevo Testamento?») y «Examen final» (6). El grupo en curso tiene las notas y los intentos de lo
  que ya pasó (`demoAcNotas`), así que la sábana trae semáforos de los tres colores.
- **El examen con su propia ventana** (`backend/_datos/academia_evaluaciones.php`): una persona puede tener su ventana en
  `ac_intentos.abre_at/cierra_at` (`acEvalVentanaDe`); al abrir la evaluación después del cierre, el servidor la califica en ese momento
  (`acEvalParaAlumno`) y la nota va a la sábana (`acEvalNotaGuardar` → `academiaNotaFinalRecalcular`). La pantalla
  (`evaluacion.page.ts`) se bloquea en 0:00 y pide el resultado sola.
- **El asistente de 5 pasos** (`curso.page.ts`, `PASOS_CURSO`): «Paso N de 5» con su barra de cinco segmentos; la escena de la ayuda
  `escenas/academia/crear-un-curso.mjs` ya lo recorre con «Matrimonios fuertes».
- **El tablero** (`tablero.page.ts`): cifras del día, «Alumnos en riesgo» (`#tab-riesgo-lista`) y la ficha académica al tocar a alguien;
  sale del resumen diario de la demo (la escena `escenas/academia/tablero.mjs` lo captura sin estado previo).
- **La verificación pública** (`/verificar`, `pages/verificar/verificar.page.ts`, `backend/academia/verificar.php`): sin sesión ni menú;
  muestra el nombre, el curso, la iglesia y la fecha guardados en el certificado (`ac_certificados.nombre_persona`, `nombre_curso`,
  `nombre_iglesia`, `fecha`). Kingdom Demo trae certificados de los grupos ya cerrados («Discípulos» y «Miembros · domingo»); la escena
  convierte el primero en el de Andrea (SPEC §3.2), para que el código sea el mismo que se ve en la parte 1.

## 6. Riesgos (el detalle en SPEC §5)

- **El cierre del examen depende del reloj:** la ventana propia de la alumna cierra 75 s después de la última referencia de la escena; si
  la máquina tarda más en arrancar, se graba otra vez con más margen.
- **El certificado de la parte 2 es una fila de la demo reescrita** para que coincida con el de la grabación del clip (código, nombre,
  curso y fecha); la fecha impresa se compara contra el cuadro del clip antes de montar.
- **El escritorio en la ventana de 1440 px** solo se lee a partir de 1,8× (el texto de 14 px a 28 px): se ven 711 × 375 px CSS de la
  pantalla a la vez, así que cada encuadre se elige con la grabación.
- **La costura de la música** se midió (envolvente igual a la esperada a ±0,4 dB, sin chasquido), pero nadie la ha oído: se oye en la
  vista previa antes del render.
