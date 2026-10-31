# Recorrido del módulo: Membresía — «Valeria llegó el domingo… y así con toda la iglesia»

2026-10-30 · Clip del sitio → **recorrido del módulo** (decisión 218): la misma historia del clip y después lo que Membresía permite lograr.
Para la página `/membresia` del sitio, YouTube y presentaciones. **16:9 (1920×1080), 97 s**, sin voz, «Product Launch» alargada, cierre del
Comercial con «Prueba gratis 30 días». El dueño ya no revisa guiones: la dirección creativa decide y esto pasa directo a [SPEC.md](SPEC.md).

**Lo que no se reabre** (heredado del clip, [STORY](../clip-sitio-membresia/STORY.md) §3 y [SPEC v2](../clip-sitio-membresia/SPEC.md)):
la app real de Kingdom Demo, nunca redibujada ni dentro de un teléfono dibujado · datos ficticios con «Datos de ejemplo» · nada inventado y
nada de «Próximamente» · la noche del sitio con Fraunces y un solo dorado · cada corte en un pulso y cada cambio de mundo en un golpe · las
tres transiciones con causa (iris desde el toque, látigo, dip y corte) · un movimiento de cámara por compás · los sonidos de acción del kit.

## 1. La idea en una línea

**Primero una persona, después toda la iglesia.** El video cuenta a Valeria (la que llegó el domingo, la llamaron y ya tiene una ruta)
y, cuando la ficha de Valeria ya mostró su camino, la cámara se abre: lo que se hizo con ella Kingdom lo hace con cada persona, y quien
dirige la iglesia lo ve. La pregunta que el pastor se lleva no es «¿qué funciones tiene?» sino «¿quién cuida a cada persona de mi iglesia,
y cómo lo sé?». Las cuatro capacidades responden en orden creciente de escala: **los nuevos de esta semana** (Coordinar) → **los que se
están alejando** (el semáforo de actividad) → **la estructura que cuida** (el discipulado) → **la iglesia entera** (los tableros). La última
frase es la del sitio: «Que *ninguna* persona se pierda».

**Recurso:** un momento del día de alguien que se vuelve un sistema (Valeria → todos). **Forma:** cadena de objeto a objeto en el celular
para la historia (la del clip, tal cual) y, para las capacidades, **la ventana que cambia de aparato**: el celular de quien acompaña se
ensancha hasta el escritorio de quien coordina, vuelve al celular del pastor y termina en el escritorio del tablero. El cambio de forma de
la ventana es el que cuenta quién está mirando (el que llama, el que reparte, el que pastorea).

## 2. La estructura

| Tramo | Segundos | Qué es | Aparato | Pista |
|---|---|---|---|---|
| **Acto 1 · La historia del clip** | 0–36 | Valeria: alta sin señal → Mi seguimiento → la llamada → su ficha con la ruta y los objetivos de conexión | celular (Jorge, 103) | 14,05 → 50,05 (entrada, primera subida, respiro, segunda subida con el 42,05) |
| **C1 · Coordinar** | 36–52 | Quien coordina reparte a los nuevos de forma pareja en un toque y ve la carga de cada acompañante | escritorio (Andrés, 101) | 50,05 → 66,05 (el clímax) |
| **C2 · El semáforo de actividad** | 52–64 | El pastor filtra a los que están en rojo y abre la ficha de una persona: «Actividad: Rojo · hace N días» | celular (101) | 26,05 → 38,05 (el respiro y el arranque de la segunda subida, **repetidos**) |
| **C3 · El discipulado** | 64–76 | La pirámide de discipulado, un nivel a la vez, con «directos» y «en total» | celular (101) | 38,05 → 50,05 (con el 42,05, el golpe más fuerte, **otra vez**) |
| **C4 · Los tableros** | 76–92 | Toda la iglesia en el «Resumen»: las cifras, el semáforo, el crecimiento y la descarga en PDF o Excel; cae la frase del sitio | escritorio (101) | 50,05 → 66,05 (el clímax, **otra vez**) |
| **Cierre** | 92–97 | `cierre-comercial` (5 s): la corona, «Kingdom es para *toda la iglesia*», «Prueba gratis 30 días» | — | 82,05 → 86,05 (el final de la pista, con su golpe y su cola) |

**La edición de la música** en una línea: la pista suena 14,05 → 66,05, salta de vuelta al **26,05** (respiro, segunda subida y clímax
otra vez, 40 s) y en el 66,05 de esa segunda vuelta salta al **82,05**, el final real de la pista. Dos empalmes, los dos en la cabeza de un
compás que empieza un ciclo de 4 compases y los dos escondidos debajo de un cambio de mundo. Los números, en [SPEC §0](SPEC.md#0-la-música-la-edición-y-la-grilla).

Por qué este orden y no otro:

- **C1 sobre el primer clímax**: es la respuesta directa a la historia («¿y quién le asignó a Jorge esa llamada?»). Repartir es la acción
  más grande del módulo para quien decide, y el 54,05 y el 58,05 de la pista (las cabezas de frase más fuertes del clímax) caen en el toque
  de «Repartir» y en «Se repartieron N personas».
- **C2 sobre el respiro**: la música baja justo cuando el tema baja (los que se enfrían). Es el único tramo de tensión del recorrido, y el
  empalme del 52 (del clímax al respiro) suena como un cambio de arreglo, no como un corte.
- **C3 sobre la segunda subida**: el 42,05, el golpe más fuerte de la pista, ya reveló la ruta de Valeria en el acto 1; en su segunda vuelta
  abre la pirámide de discipulado. Los dos golpes más fuertes del video son las dos estructuras que cuidan a la persona (su ruta, su
  discipulado).
- **C4 sobre el segundo clímax**: la iglesia entera es lo más grande que se ve, y la frase del sitio cae en el 62,05 de la pista, la última
  cabeza fuerte antes del final.

## 3. Las capacidades elegidas y su porqué

El sitio ofrece seis bloques en `/membresia` (`sitio/src/data/modulos.ts`): ruta de crecimiento, Mi seguimiento, ficha completa,
organigrama del discipulado, tableros y reportes, y arrancar es fácil. **El acto 1 ya cubre los tres primeros** (la ruta, Mi seguimiento con
su semáforo de la ruta y la ficha con «Avance»). Las cuatro capacidades salen de los otros tres y del punto «quien coordina reparte parejo y
ve quién no ha llamado» del bloque de Mi seguimiento. Cada una existe hoy en v2, se graba con Kingdom Demo y tiene escena de ayuda o pantalla
verificada:

| # | Capacidad | Lo que el pastor valora | Pantalla real | Prueba en la grabación |
|---|---|---|---|---|
| C1 | **Coordinar: repartir parejo** | Que nadie nuevo se quede sin llamada aunque lleguen veinte el mismo domingo, sin hacer la lista a mano | Membresía → «Coordinar» → «Nuevos» → «Repartir» → «Quienes acompañan» (escritorio; escena de ayuda `coordinar-el-seguimiento`, la demo deja nuevos sin repartir a propósito) | «N personas nuevas esperan acompañante.» → «Se repartieron N personas.» → «Todos los nuevos tienen quién los acompañe.» → «Acompaña a 3 de 4» con su barra de carga |
| C2 | **El semáforo de actividad** | Ver a tiempo a quien se está alejando, antes de que deje de venir («la gente no se pierde de golpe, se enfría») | Membresía → «Personas» → «Agregar filtro» → «Semáforo de actividad» → «Rojo» → la ficha (celular; escena de ayuda `buscar-y-filtrar`; la demo siembra la sección «semaforo» con personas en los cuatro colores) | el chip del filtro, el contador «N de 1 000», los puntos rojos, «Actividad: Rojo · hace N días» y los botones «Llamar» y «WhatsApp» |
| C3 | **El discipulado** | Saber quién discipula a quién y cuánta gente cuelga de cada líder, desde el celular | Membresía → «Estructura» → «Discipulado» (celular: el componente se pensó para el celular, decisiones 10 y 13; escena de ayuda `estructura` en escritorio) | «Quienes encabezan la pirámide», «N directos · M en total», bajar dos niveles y las migas «Inicio › … › …» |
| C4 | **Los tableros** | Ver a toda la iglesia en una pantalla y llevarla a la reunión de liderazgo en PDF o Excel | Membresía → «Tableros» → «Resumen» (escritorio; escena de ayuda `tableros`) | las cifras con su cambio, la barra del «Semáforo de actividad» con sus cuatro colores, el crecimiento y el menú «PDF · Excel» |

**Las que quedan fuera, y por qué:**

- **Importar desde Excel.** Es lo que más alivia a quien arranca, pero su pantalla es una tabla de columnas y un lote: no tiene un resultado
  que se vea (la escena de la ayuda se detiene antes de «Importar» a propósito) y le habla al administrador que configura, no al pastor
  que cuida. Va en el bloque «Arrancar es fácil» del sitio, al lado del video, y en el llamado «Prueba gratis 30 días».
- **«Armar el reporte».** Existe y se graba, pero es un diálogo de columnas sin un final visible (la descarga no se ve). El menú «PDF ·
  Excel» de los tableros dice lo mismo en un segundo.
- **La vista «Ruta» de los tableros (el embudo).** Es la más rica en datos y la más técnica; para un pastor que no conoce Kingdom, la ruta
  ya quedó dicha con Valeria.
- **Depurar duplicados, logros, etiquetas, notas pastorales.** Reales, pero de detalle; el recorrido no lista funciones.

## 4. Las frases (nueve; ninguna es una lista)

Las cuatro del acto 1 son las del clip; las cinco nuevas nombran lo que la iglesia logra, cada una dicha por la pantalla que la prueba. La
única palabra dorada del cuerpo es *ninguna*, en la última.

| Seg. | Frase | Sobre qué | De dónde sale |
|---|---|---|---|
| 0,0 | **Valeria llegó el domingo.** | «Nueva persona» escribiéndose | el clip |
| 4,0 | **Registrada. Aun sin señal.** | «Guardada en este dispositivo» | el clip; el sitio: «Funciona sin señal» |
| 12,0 | **Y ya tiene quién la llame** | la tarjeta de Mi seguimiento | el clip |
| 28,0 | **Y una ruta para crecer** | la tarjeta «Avance» de su ficha | el clip |
| 36,5 | **Nadie nuevo se queda sin llamada** | Coordinar → «Repartir» | el sitio, literal: «Mi seguimiento con semáforo: nadie nuevo se queda sin llamada» |
| 52,5 | **Ves a tiempo quién se aleja** | el filtro «Rojo» y la ficha | la ayuda: «Sirve para ver a tiempo a quien se está alejando» |
| 65,0 | **Quién discipula a quién** | la pirámide | el sitio: «el árbol de discipulado… con directos y total» |
| 76,5 | **Tu iglesia, de un vistazo** | el «Resumen» de los tableros | el sitio: «Tableros y reportes» |
| 88,0 | **Que *ninguna* persona se pierda** | el crecimiento de la iglesia | el sitio: el `titulo` de Membresía |

Descartadas: «Así con cada persona que llega» como puente después del acto 1 (la quinta frase ya generaliza: «nadie nuevo»), «Y toda la
iglesia, en un tablero» (el cierre del kit dice «Kingdom es para *toda la iglesia*» cinco segundos después: se oiría repetida), «Tu Excel,
adentro en minutos» (no hay medida de los minutos y la capacidad quedó fuera), «Reparte en un toque» (es un verbo de función; la frase del
sitio dice el resultado).

Además de las frases, una **ceja** dorada con el nombre real de la pantalla en cada capítulo: «MEMBRESÍA» (acto 1), «COORDINAR»,
«SEMÁFORO DE ACTIVIDAD», «DISCIPULADO» y «TABLEROS». No son frases: son el rótulo que el pastor encuentra después en la app y en los
bloques del sitio.

## 5. El movimiento, en una línea por nivel

- **Cada pulso (0,5 s):** aterriza una palabra, un toque real, un chip, una lista que cambia o un movimiento de cámara. Ningún compás sin un
  toque o un movimiento.
- **Cada compás (2 s):** un movimiento de cámara dentro de la ventana (14 cuadros, `power2.inOut`), quieta después.
- **Cada capítulo (un golpe):** la ventana cambia de forma (celular ↔ escritorio) con un látigo horizontal, o de pantalla con un látigo
  vertical cuando es el mismo celular. La ceja y la frase llegan con el mundo.
- **Los golpes más fuertes:** 4,0 «Registrar» · 28,0 la ruta de Valeria · 40,0 «Repartir» · 44,0 «Se repartieron» · **68,0 la pirámide se
  abre** · 88,0 la frase del sitio · 92,0 la corona.
- **Lo que no se mueve:** las frases aterrizadas, el halo (se asienta una vez por mundo), los puntos del fondo y los píxeles de la app.

## 6. El sonido

La pista alargada a −18 LUFS; los sonidos de acción del kit en cada toque real (tres tomas rotadas), en cada ceja (`aparicion`, tres tomas),
en los cambios de mundo (`desliz`, tres tomas) y en lo que queda hecho (`confirmacion`: «Guardada», «cumplido», «Se repartieron»); una sola
`subida`, hacia el cierre; las campanas del kit a +0,38 s del cierre, sobre la cola del final real de la pista.

## 7. Riesgos que deciden la grabación (detalle en [SPEC §5](SPEC.md#5-riesgos-y-lo-que-se-decide-al-grabar))

- La grilla del clímax: el mapa de pulsos marca los contratiempos entre el 52,5 y el 80 de la pista; la medición dice que la grilla de los
  tiempos (x,05) se mantiene. El recorrido corta en la grilla de los tiempos y nunca en un contratiempo.
- El escritorio en 1440×760 solo se lee como **recorte** (la grabación de escritorio es de 1,5×): nunca la pantalla entera.
- Las cifras de Kingdom Demo (cuántos nuevos sin acompañante, cuántas personas en rojo, el tamaño de la pirámide) salen de la grabación;
  ninguna frase depende de un número.
