# Recorrido de Equipos — «Falta uno en Parqueadero… y el domingo, cubierto» (historia elegida)

2026-10-30 · El recorrido del módulo para la página `/equipos` del sitio, YouTube y presentaciones (decisión 218 del dueño:
`KingdomApp/docs/videos/README.md` → Clip del sitio → **recorrido del módulo**). Parte del clip publicado
[«Falta uno en Parqueadero»](../clip-sitio-equipos/STORY.md) y sigue con lo que se logra con los equipos que sirven. **El dueño ya no
revisa guiones:** la historia la decide la dirección creativa y pasa directo a [SPEC.md](SPEC.md). Se respeta el sistema de la serie
([Membresía → STORY §3](../clip-sitio-membresia/STORY.md)) y el de los otros dos recorridos ([Academia](../recorrido-academia/STORY.md),
[Eventos](../recorrido-eventos/STORY.md)): frases cortas, la misma ventana, las mismas transiciones, los mismos sonidos de acción y la marca
solo al final.

**Lo que no se reabre:** **16:9 (1920×1080)**, **97,0 s** (92 de cuerpo + el cierre del Comercial de 5) · sin voz, texto quemado ·
«Product Launch» alargada con **una sola costura** en el borde de compás, **la misma edición de Academia** (SPEC §0) · la app real de
Kingdom Demo en `.k-ventana-16x9` (celular) y `.k-ventana-escritorio`, nunca un aparato dibujado · nada inventado, **nada de «Redes y
solicitudes»** (en `modulos.ts` es «Próximamente») · **`cierre-comercial`** con el llamado `prueba`. El README pide 60–75 s para el
recorrido; los ~100 s los decidió el dueño para esta serie (se anota en el README al publicar).

## 1. La historia

**Nombre:** «Falta uno en Parqueadero… y el domingo, cubierto».

**Idea en una frase:** los primeros 28 s son el clip tal cual (el líder de Seguridad asigna a Gabriela, ella ve a qué hora llegar y
acepta, el turno queda «5 de 5»); después la cámara se abre del turno a **toda la iglesia** (la cobertura del domingo, departamento por
departamento), entra al **chat de un equipo** (el anuncio anclado, la encuesta de la canción, el ensayo del jueves con «Asistiré»), vuelve
al líder **después del culto**, que cierra el turno con Gabriela marcada «Sirvió», y termina donde importa: **en el celular de Gabriela, su
objetivo «Servir» se dibuja cumplido en su ruta de crecimiento**.

**El recurso: una persona que viaja.** El clip ya tenía un dato que viaja (el puesto de Parqueadero: «Vacante» → «Por confirmar» →
«Confirmado»). El recorrido sigue **a Gabriela Hinestroza Perea** por cuatro pantallas más, cada una de otra persona o de otro momento:

1. **La cobertura del administrador** (escritorio): en Seguridad, «5/5 · 100 %» y su nombre en verde, «Confirmado». Al tocar «Solo lo que
   falta», Seguridad desaparece: está completo. Quedan Alabanza y Audiovisual con lo que les falta.
2. **El cierre del turno** (celular del líder): su fila viene marcada «Sirvió».
3. **El aviso del cierre:** «1 persona cumplió su objetivo de servir en la ruta». Esa persona es ella (es la única de ese turno que va en
   una ruta y le faltaba un servicio).
4. **Su celular:** «Mis objetivos» → «Servir», con el check que se dibuja.

**La forma:** la del clip (la ventana del celular a la derecha, las frases a la izquierda, el látigo vertical entre personas) más **el
escritorio** para la cobertura, al que se llega con el **látigo horizontal** (izquierda = al escritorio; derecha = de vuelta), como en
Academia. Dentro del celular del líder, las dos navegaciones son de la app y se ven con sus transiciones de la serie: el **corte sobre el
toque** («Servir» en la barra de abajo, como el toque en la fila del domingo del clip) y el **iris desde el toque** (la fila del turno por
cerrar). El alcance cuenta la historia sin decirlo: **un puesto → un turno → toda la iglesia → un equipo → el turno cerrado → una persona**.

**Por qué es la mejor para un pastor que no conoce Kingdom:** el clip ya lo convenció de que un puesto se cubre sin perseguir a nadie; el
recorrido contesta lo que pregunta un pastor después: «¿y el resto de la iglesia?» (la cobertura del domingo, sin pedir informes), «¿y la
comunicación del equipo?» (su chat, con lo que un grupo de WhatsApp no tiene: la encuesta y el «Asistiré»), y «¿y eso le sirve a la
persona?» (servir le cuenta en su ruta de crecimiento). Cubre los cinco bloques del sitio que existen (`modulos.ts` → equipos →
`bloques`): «Turnos con confirmación» e «Instrucciones claras» (el clip), «Cobertura de la iglesia», «El chat de cada equipo» y «Servir
cuenta». El video y la página dicen lo mismo.

## 2. Frases en pantalla (una a la vez; Fraunces 560, 84 px)

| Segundo | Frase | Dónde | Cómo entra | Se va |
|---|---|---|---|---|
| 0,0 | **¿Quién cubre / el domingo?** | columna izquierda | una palabra por pulso (0,0 · 0,5 · 1,0 · 1,5) | 3,9 |
| 4,0 | **Kingdom sugiere / a quién poner** | izquierda | la línea entera, blur 8 → 0 | 5,9 |
| 12,0 | **Y sabe a qué / hora llegar** | izquierda | palabra a palabra | 19,9 |
| 24,0 | **Y el domingo, / completo.** (nueva: la «revelación» que dejó escrita el clip; sobre «5 de 5») | izquierda | palabra a palabra | 27,9, con el látigo |
| 28,0 | **Lo que falta, antes del domingo.** | arriba (escritorio) | palabra a palabra | 43,9 |
| 44,0 | **Cada equipo, / con su chat.** | izquierda | palabra a palabra | 59,9 |
| 60,0 | **Servir cuenta.** | izquierda | palabra a palabra | 75,9 |
| 76,0 | **Y da un paso / en su ruta.** | izquierda | palabra a palabra | 83,9 |
| 84,0 | **Que cada puesto / de servicio / esté *cubierto*** (*cubierto* en itálica dorada; el `titulo` de `modulos.ts`) | izquierda | palabra a palabra | se queda hasta 92,0 |

Más la ceja «EQUIPOS» (Inter 700, 28 px, dorada), que entra en 6,5 como en el clip, acompaña a cada frase en su escenario y se va en 84,0.
Leídas solas, las nueve frases son el argumento completo; vistas sin sonido, las imágenes cuentan lo mismo.

De dónde sale cada frase (nada inventado): «antes de cada reunión… por departamento qué puestos están… vacantes» es el bloque «Cobertura de
la iglesia»; «Cada departamento con sus líderes, sus turnos y su chat» es el `resumen` del sitio; «Servir cuenta» es el título de un
bloque, y «se cumple el paso Servir de la ruta de crecimiento», su texto. La frase 1 pregunta con el verbo de la última («cubre» →
«*cubierto*»), como en el clip; la frase 4 contesta a la 1 con la imagen («5 de 5») y la 5 la abre a toda la iglesia.

## 3. Recorrido sobre la música (compases de 2 s; la grilla exacta en SPEC §0)

| Compás | Video | La pista | Pantalla real y acción | Movimiento |
|---|---|---|---|---|
| 1–12 | **0–24** | 14,05–38,05 | **El clip, cuadro por cuadro** (su grabación, sus cortes, sus iris y sus látigos), llevado a 16:9 | Lo del clip |
| 13–14 | **24,0**–28 | 38,05–42,05 | El turno del líder quieto con «5 de 5» (lo mismo que el clip, sin la ventana a un lado ni la firma) | Cae «Y el domingo, completo.» |
| 15 | **28,0**–30 | 42,05 (1,00) | **Látigo horizontal al escritorio** (el administrador, 101): Servir → Equipos → **Cobertura**, el próximo domingo: «13 de 19 confirmados (68 %)» | Cae «Lo que falta, antes del domingo.» |
| 16 | 30–32 | 44,05 | La app baja a **Seguridad: «5/5 · 100 %»**, Parqueadero con Rut y **Gabriela Hinestroza Perea · Confirmado** | La cámara quieta mientras la app se mueve |
| 17 | **32,0**–34 | 22,05 (costura) | Quieto | La cámara se acerca a Gabriela en verde |
| 18 | 34–36 | 24,05 | La app vuelve arriba | La cámara abre al interruptor |
| 19–22 | **36,0**–44 | 26,05–34,05 (respiro) | **Toque «Solo lo que falta» (36,0)**: Seguridad, Evangelismo y Medios se van; quedan **Alabanza** (vacantes en rojo, por confirmar en ámbar) y **Audiovisual** | Respiro: la cámara sobre lo que falta |
| 23 | **44,0**–46 | 34,05 (0,93) | **Látigo horizontal de vuelta al celular:** el líder (103), que también canta en Alabanza, en **el chat de Alabanza**: el anuncio anclado «Ensayamos todos los jueves a las 7 p. m.…» | Cae «Cada equipo, con su chat.» |
| 24–25 | 46–50 | 36,05–40,05 | La encuesta **«¿Con qué canción abrimos el domingo? 🎶»** → **toque «Way Maker» (48,0)**: su voto y la barra crecen | La cámara a la encuesta |
| 26 | 50–52 | 40,05 | La app baja a la tarjeta del **«Ensayo de Alabanza»** (jueves, 7:00–9:00 p. m., cada semana, Salón principal) | |
| 27 | **52,0**–54 | 42,05 (1,00) | **Toque «Asistiré»**: el botón se llena y «N van» sube uno | El punch más grande de la parte 2 |
| 28–30 | 54–60 | 44,05–50,05 | Escribe **«¡Cuenten conmigo el jueves!»** (56,0) y lo envía (58,0) | La cámara al pie del chat |
| 31–32 | **60,0**–64 | 50,05 (clímax) | **Toque «Servir»** en la barra de abajo → su inicio de Servir con la tarjeta **«Cerrar el turno · 1 turno de tus equipos espera que marques quién sirvió»** | Cae «Servir cuenta.» |
| 33 | **64,0**–66 | 54,05 | **Toque en «Seguridad · Servicio General»** → iris → **«Cerrar el turno»**: «5 sirvieron», los confirmados ya marcados «Sirvió», **Gabriela entre ellos** | |
| 34 | 66–68 | 56,05 | La cámara sobre la fila de Gabriela | |
| 35 | **68,0**–70 | 58,05 | **Toque «No llegó»** en el que faltó | |
| 36 | 70–72 | 60,05 | La cámara a la barra «Cerrar el turno» | |
| 37–38 | **72,0**–76 | 62,05–66,05 | **Toque «Cerrar el turno»** → **«El turno quedó cerrado · 1 persona cumplió su objetivo de servir en la ruta.»** | Punch al aviso |
| 39 | **76,0**–78 | 66,05 (salida) | **Látigo vertical al celular de Gabriela:** «Buenas tardes, Gabriela» | Cae «Y da un paso en su ruta.» |
| 40–42 | **78,0**–84 | 68,05–74,05 | **Toque «Objetivos»** → «Mis objetivos» → «Para conectarte»: **«Servir» con el check que se dibuja** (78,9) y «Cumplido el …» | La cámara a «Servir» |
| 43–46 | **84,0**–92 | 74,05–82,05 | Quieto: su objetivo cumplido | Cae la frase del sitio; la ventana se hace a un lado; la subida; el dip |
| — | **92,0**–97,0 | 82,05 → fin | **`cierre-comercial`** (noche, «Kingdom es para *toda la iglesia*», «Prueba gratis 30 días», `kingdom-sitio.web.app`), campanas en 92,38 | El único gesto de marca |

### Lo que este recorrido hace distinto dentro del sistema (y por qué)

- **Un solo viaje al escritorio.** Solo la cobertura es de escritorio en la vida real (el administrador la mira antes del domingo, la
  imprime o la exporta); el chat, el cierre y el objetivo son del celular. Por eso hay dos látigos horizontales (28,0 y 44,0) y no cuatro.
- **El líder cambia de equipo sin cambiar de celular.** Jorge es líder de Seguridad e integrante de Alabanza (así lo siembra la demo):
  el chat es el suyo como cantante y el cierre, el suyo como líder. Entre los dos no hay látigo (no cambia la persona): hay un toque en
  «Servir» de su barra de abajo, que es como la app lo hace.
- **La costura de la música cae en un compás quieto de la cobertura** (32,0): la cámara se acerca a Gabriela y nada corta. Igual que en
  Academia, la pista repite su respiro y su segunda subida: el golpe más fuerte suena en el 28,0 (el látigo al escritorio) y otra vez en el
  52,0 («Asistiré»).
- **El clímax es el cierre del turno** (60–76): cuatro golpes fuertes, cuatro toques (Servir, la fila, «No llegó», «Cerrar el turno») y
  el aviso del objetivo en el 72,5. La salida, tranquila, es de Gabriela.
- **El cierre es el del Comercial (5 s, 16:9)**, no la firma corta del clip, y llega sobre el final natural de la pista.

## 4. Alternativas descartadas (una línea cada una)

- **El chat de Seguridad con Gabriela** (ella, nueva en el equipo, vota la encuesta anónima de diciembre): mantiene a la misma persona,
  pero Seguridad no tiene reunión del equipo ni anuncio anclado en la demo; el «Asistiré» del ensayo de Alabanza es lo que un grupo de
  WhatsApp no hace.
- **Las plantillas de puestos** (escritorio): explican de dónde salen los cinco puestos del domingo, pero es un formulario quieto; el
  clip ya mostró el turno nacido de la plantilla.
- **El recordatorio del día anterior** («Mañana sirves como…»): es un aviso del sistema que no se graba con certeza (horario silencioso,
  FCM); queda dicho en la página.
- **«Por semana»** (la rejilla de reuniones × equipos): con un solo culto a la semana en la demo es una fila de cinco celdas.
- **El cierre del turno en el escritorio** (como la escena de la ayuda): el líder cierra al terminar el culto, en el celular, y sin señal
  si hace falta; en el escritorio se perdía el corte sobre «Servir».
- **La ficha de Membresía de Gabriela** (escritorio, «Cumplió «Servir» con 2 servicios»): es la mirada del pastor, pero obliga a un
  tercer látigo horizontal y quita el final en la persona.
- **Archivos por aprobar en el chat de Medios:** real, pero es la herramienta del líder y pide otra cuenta.

## 5. Lo que la demo tiene (verificado el 2026-10-30 en código y en la base local de capturas, con transacciones de prueba y `ROLLBACK`)

- **Cuentas** (`_demo_capturas.php`, `escenas-equipos.mjs`): 101 el administrador (tiene `servicio.reportes`); **103 Jorge Gallego Gil**,
  líder de Seguridad e integrante de Alabanza (Voz); **105 Gabriela Hinestroza Perea**, miembro, con la **ruta de crecimiento en curso**
  y **un servicio ya marcado «sirvió»** en los últimos 60 días (el de Evangelismo «sin estar programado» que siembra
  `_demo_servicio_historial.php`, paso 4).
- **El objetivo «Servir»** de la ruta está ligado a Equipos con **«2 servicios en 60 días», en cualquier equipo** (paso 5 de la misma
  semilla). Con el cierre del turno, Gabriela llega a 2 y `rutaPorServicio` (`personas_ruta_equipos.php`) lo cumple en el acto: el cierre
  devuelve `objetivos: 1` y la pantalla muestra «1 persona cumplió su objetivo de servir en la ruta» (`cerrar.page.ts`, `eq4.objetivos_
  cumplidos_one`). Nadie más del turno va en una ruta (consultado: los otros cuatro, sin ruta).
- **El turno por cerrar:** la semilla deja «por cerrar» el último domingo de Seguridad (en la base: el 25 de oct, cinco confirmados:
  Parqueadero ×2, Entrada ×2, Rondas). La escena pone a Gabriela en el segundo puesto de Parqueadero.
- **La cobertura** (`cobertura.page.ts`, `eqRepCoberturaReunion`): el próximo domingo tiene Alabanza 2/7 (3 por confirmar, 2 vacantes),
  Audiovisual 3/4, Evangelismo 2/2, Medios 1/1 y Seguridad 4/5; con Gabriela confirmada, Seguridad 5/5 y el total **13 de 19 (68 %)**. Con
  «Solo lo que falta», los equipos completos no salen.
- **El chat de Alabanza** (`_demo_servicio_chat.php` y `_chat_reuniones.php`): el primer mensaje del líder, **anclado** («¡Hola, equipo!
  Ensayamos todos los jueves a las 7 p. m. en el salón principal…»), la encuesta con nombres **«¿Con qué canción abrimos el domingo? 🎶»**
  (Grande y fuerte · Way Maker · Cuán grande es Él) y el **«Ensayo de Alabanza»** de cada jueves con sus «Asistiré». Jorge ya votó y ya
  respondió en la semilla: la escena borra su voto y su respuesta para que lo haga en cámara.
- **«Mis objetivos»** (`/mi/objetivos`, `objetivos-conexion.component.ts`): los objetivos cumplidos salen siempre, con un check que se
  dibuja (círculo 320 ms, trazo 320 ms) y «Cumplido el {fecha}».

## 6. Riesgos (el detalle en SPEC §5)

- **El turno que se cierra es el del domingo pasado**, no el del clip: la base no tiene un 1 de noviembre ya servido. Su fecha se ve en
  la fila de la tarjeta y encima del título de «Cerrar el turno»; los encuadres la dejan fuera y ninguna frase depende de ella.
- **No se graba un domingo** (el turno de hoy sería a la vez el de la cobertura y el que se cierra): la escena se niega.
- **El ensayo sembrado vence:** si se graba después del primer jueves de la semilla, la tarjeta no trae «Asistiré» de nadie; la escena se
  niega y se vuelve a sembrar el volcado.
- **La costura de la música** es la de Academia (medida, no oída): se oye en la vista previa antes del render.
