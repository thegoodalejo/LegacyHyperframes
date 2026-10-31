# Recorrido del módulo: Eventos — «Terminó la reunión, y el lunes el pastor lo ve»

2026-10-30 · El recorrido de Eventos para la página `/eventos` del sitio, YouTube y presentaciones: **16:9 (1920×1080), 97 s** (92 de cuerpo
+ el cierre del Comercial de 5 s). Empieza con la misma historia del [clip publicado](../clip-sitio-eventos/STORY.md) («Terminó la
reunión») y después muestra lo que el módulo logra para la iglesia. **El dueño ya no revisa guiones:** la historia se decide aquí y se
especifica completa en [SPEC.md](SPEC.md). Son palabras; nada se construye desde este archivo.

**Lo que no se reabre** (el sistema de la serie, [Membresía §3](../clip-sitio-membresia/STORY.md)): sin voz, frases cortas quemadas
(Fraunces, una palabra en itálica dorada solo en la última), «Product Launch» con el movimiento en sus pulsos, la app real de Kingdom Demo
dentro de la ventana del kit (nunca un teléfono dibujado), datos ficticios con «Datos de ejemplo», la ceja «EVENTOS», un movimiento de
cámara por compás, las tres transiciones de la serie (iris desde el toque, látigo entre dos mundos, dip + corte a la firma) y los sonidos
de acción del kit. Lo que cambia por ser recorrido: 16:9, el doble de largo, dos mundos (el celular de Jorge y el computador del pastor) y
el **cierre del Comercial** (`cierre-comercial`, 5 s, llamado «Prueba gratis 30 días») en vez de la firma del clip.

> Nota de reglas: `KingdomApp/docs/videos/README.md` dice que el recorrido dura de 60 a 75 s. Este dura 97 s por decisión del pedido del
> 2026-10-30 («~100 s», 3 a 5 capacidades). Hay que llevar ese número al README en la misma entrega (SPEC §8).

## La idea en una frase

Terminó la casa de paz de Jorge y la reporta en el celular (la historia del clip, tal cual); la siguiente reunión la reporta **sin señal** y
se envía sola cuando vuelve la conexión; y el lunes **el pastor** abre el tablero en el computador: ve de un vistazo cómo van todas las
reuniones, **dónde falta una** en el mapa de la ciudad, **cuál crece y cuál necesita apoyo**, y entra a la casa de Jorge: «Última reunión:
10 personas», con su tendencia, su meta y, en la lista de quiénes vinieron, **Ximena Hoyos Vélez**, la persona nueva del principio.

**Recurso:** un dato real que viaja de un mundo al otro. La reunión que Jorge reporta en el segundo 22 (10 personas, entre ellas Ximena)
reaparece en el segundo 74, en la ficha que abre el pastor. Es la prueba de «cada reunión cuenta»: lo que el líder hace en la casa le llega
contado a quien cuida la iglesia, sin pedirlo por WhatsApp el jueves.

**Forma:** dos mundos unidos por un solo látigo horizontal (del celular de Jorge al computador del pastor, en el 36,0, cuando entra el
respiro de la música); dentro de cada mundo, cadena objeto a objeto: cada toque abre lo siguiente («Volver a la lista» → la lista sin
señal → la casa → «Igual que la última vez» → «Guardar asistencia»; «Mapa» → «Dónde viven» → «Zonas sin evento» → «Eventos» → buscar a
Jorge → su casa → su ficha).

## Por qué esta y no otra

Un pastor que no conoce Kingdom ya vio en el clip que un líder reporta en 24 segundos. Lo que le falta saber es **qué gana él**: el
recorrido le contesta tres miedos en orden — «¿y si en la casa no hay señal?», «¿y yo cómo veo todo eso?», «¿y para qué me sirve?» — con
pantallas reales, y cierra el círculo con la misma reunión del principio. Las capacidades no se listan: cada una es un paso de la misma
semana de la misma iglesia.

## Las capacidades (cuatro, las de más impacto que existen hoy)

| # | Capacidad | Dónde | Por qué esta | Fuente |
|---|---|---|---|---|
| 1 | **Reportar sin señal** y que se envíe solo | celular (Jorge, cuenta 103) | Es la promesa del sitio que el clip dejó fuera («Reporte guiado de cada reunión, también sin señal»); en muchas casas no hay datos | `docs/modulos/eventos.md` → Offline; ayuda `reportar-una-reunion` → sin señal (escena verificada) |
| 2 | **El tablero**: cifras del período, al día y retrasados, tendencia y metas | computador (el pastor, cuenta 101) | «De un vistazo sabes qué reunión crece y cuál necesita apoyo» (bloque «Metas y semáforo» de `modulos.ts`) | ayuda `tablero-y-mapa` |
| 3 | **El mapa de la ciudad**: dónde viven y las zonas sin reunión | computador | El bloque «El mapa de tu ciudad»; la imagen más fuerte del módulo, en el golpe más fuerte de la música | ayuda `tablero-y-mapa` → El mapa |
| 4 | **La lista de eventos y la ficha**: semáforo y tendencia por evento, y la casa con su última reunión, su meta y quiénes vinieron | computador | Cierra el círculo con la reunión de Jorge y la persona nueva del clip («Conectado con Membresía») | ayuda `ver-eventos` (ficha → Asistencia), `tablero-y-mapa` → Eventos |

**Descartadas** (una línea cada una): **asistencia por QR** (es el ingreso con boletas de la Boletería: existe, pero escanear con la cámara
no se puede grabar con Playwright y la boleta es otro relato); **reportes en PDF y Excel** (el diálogo existe, pero el archivo descargado
no se ve en la grabación y mostrar el PDF sería un gráfico propio); **categorías a tu manera** (es configuración del administrador: honesta
pero quieta, mala para la salida de la pista); **solicitudes de eventos** (otro recorrido entero); **Eventos masivos** (complemento aparte,
solo en Kingdom Demo 1: no se muestra).

## Las frases en pantalla (nueve)

Las tres primeras son las del clip, en el mismo segundo. Ninguna depende de un número, un nombre de casa ni una fecha de la semilla.

| Segundo | Frase | Mundo | Se va |
|---|---|---|---|
| 0,0 | **Terminó la reunión. ¿Quién vino?** (una palabra por pulso) | celular | 4,0 |
| 4,0 | **Los de siempre, en un toque.** | celular | 6,0 |
| 12,0 | **Y queda registrada en la iglesia** | celular | 20,0 |
| 24,0 | **¿Sin señal? La asistencia se guarda** | celular | 32,0 |
| 32,0 | **Y se envía sola al volver la señal** | celular | 35,9 |
| 38,0 | **El pastor lo ve todo** | computador | 44,0 |
| 52,0 | **Y dónde falta una reunión** | computador | 60,0 |
| 60,0 | **Cuál crece y cuál necesita apoyo** | computador | 69,1 |
| 86,0 | **Cada *reunión* cuenta, y cuenta bien** (*reunión* en itálica dorada; el `titulo` de `modulos.ts`) | computador | hasta la firma (92,0) |

Origen de cada una: la 4 dice lo que la app dice en pantalla («Sin señal: la asistencia se guarda en este dispositivo…», `ev3.sin_red_reporte`)
y no promete más (el formulario necesita señal); la 5 es textual de la misma nota («…y se envía sola al volver la conexión»); la 6 es la
persona del cierre del Comercial («Kingdom es para toda la iglesia»), dicha sin cifras; la 7 es el bloque «El mapa de tu ciudad» («en qué
zonas todavía no hay una reunión cerca»); la 8 es el bloque «Metas y semáforo» («qué reunión crece y cuál necesita apoyo»). Cuatro
empiezan con «Y»: es la cadena de lo que la iglesia ya tiene, como en Membresía; la 6 no, porque abre otro mundo.

## Recorrido sobre la música

La música es «Product Launch» alargada a 96 s con **una repetición sin costura**: se toca del 14,05 al 44,05 de la pista y se vuelve al
20,05 (los compases 42–46 y 18–22 son el mismo material: correlación de la onda 0,81 sin desfase), así que el golpe más fuerte de la pista
(42,05) suena **dos veces**, en el 28,0 y en el 52,0, y la pista termina sola, con su acorde final, en el 92,0, donde arranca el cierre.
Detalle y grilla en SPEC §0.

| Clip | La pista | Mundo | Lo que pasa |
|---|---|---|---|
| 0–24,0 | 14,05–38,05: entrada, el bajo (4,0), pico (6,0), respiro, segunda subida (20,0, 22,0) | celular | **La historia del clip, idéntica** (sus 720 primeros cuadros): Servir → «Reportar» → «Igual que la última vez» → «Persona nueva» (Ximena) → visitantes → «Guardar asistencia» → «Enviar reporte» → «¡Listo! … 10 personas.» |
| 24,0–26,0 | 38,05 (golpe 0,96) | celular | Cae «¿Sin señal? La asistencia se guarda». La cámara baja a los botones del «¡Listo!» |
| 26,0 | 40,05 (0,88) | celular | **Toque en «Volver a la lista»**: la lista de Reportar, ahora con el chip **«Sin señal»** arriba |
| 27,0 | 40,55 | celular | Toque en la casa: su reunión siguiente (la vencida) se abre desde el dispositivo, con la nota «Sin señal: la asistencia se guarda…» |
| **28,0** | **42,05 (1,00)** | celular | **Toque en «Igual que la última vez», sin señal**: la lista se marca sola, el eco del 4,0 en el golpe más fuerte |
| 29,0 | 42,55 | celular | La app baja hasta «Guardar asistencia» |
| **30,0** | 44,05 → **20,05** (la costura) | celular | **Toque en «Guardar asistencia»** (el ícono del reloj): **«Espera señal»**, **«1 sin enviar»** y «Guardado en este dispositivo: se enviará solo cuando vuelva la señal.» |
| **32,0** | 22,05 (0,92) | celular | Vuelve la señal: los chips «Sin señal» y «1 sin enviar» **se van solos**. Cae «Y se envía sola al volver la señal» |
| **36,0** | 26,05: entra el respiro | → computador | **El látigo horizontal** al computador del pastor: el tablero de eventos, las cifras contando desde cero |
| 38,0–44,0 | respiro | computador | «El pastor lo ve todo». La cámara recorre las cifras: eventos activos, asistencia del período, al día con los retrasados en rojo, tendencia ↗ ↘, metas logradas |
| **44,0** | 34,05 (0,93): segunda subida, otra vez | computador | **Toque en «Mapa»**: la ciudad con los eventos en círculos |
| 46,0 | 36,05 (0,90) | computador | Toque en **«Dónde viven»**: las zonas donde vive la gente de la iglesia |
| **52,0** | **42,05 (1,00)**, segunda vez | computador | **Toque en «Zonas sin evento»**: aparecen las zonas con gente y sin una reunión cerca. Cae «Y dónde falta una reunión» |
| 54,0–58,0 | 44–48 | computador | La cámara va a una zona y se acerca |
| **60,0** | 50,05 (0,93): **clímax** | computador | **Toque en «Eventos»**: la lista con el semáforo y la tendencia de cada uno, lo más urgente arriba. Cae «Cuál crece y cuál necesita apoyo» |
| 64,0 | clímax | computador | Toque en la columna **«Tendencia»**: la lista se reordena |
| 66,0 | clímax | computador | Toque en el buscador y se escribe **«Jorge Gallego»**: quedan sus reuniones |
| **70,0** | 60,05 | computador | **Toque en «Casa de Paz Laureles 1»** → iris → su ficha |
| 72,0–76,0 | 62–66 | computador | La tarjeta «Asistencia»: **«Última reunión: 28 de oct de 2026 · 10 personas»**, el promedio, la tendencia, la meta con su barra |
| 76,0–84,0 | **salida** | computador | **«Quiénes vinieron el 28 de oct»**: la cámara llega a **«Ximena Hoyos Vélez»** (80,0) y vuelve a la tarjeta entera |
| **86,0** | 76,05 | computador | Cae «Cada *reunión* cuenta, y cuenta bien»; la ceja se va. 88,0: la ventana se hace un poco más chica |
| **92,0** | **82,05: el acorde final** | — | **El cierre del Comercial** (5 s, noche, «Prueba gratis 30 días», `kingdom-sitio.web.app`); campanas en el 92,38 |

### El lenguaje del movimiento

- **Cada pulso entre 0 y 36:** una palabra, un toque real o algo nuevo en la app (como el clip). Del 36 al 92, **algo nuevo cada 2 s** (un
  toque, una capa del mapa, una cifra que cuenta, un movimiento de cámara); nunca más de 3,4 s sin cambio.
- **Cada compás:** un movimiento de cámara dentro de la ventana, luego quieta; nunca a la vez que la app se desplaza o escribe.
- **Golpes:** 28,0 «Igual que la última vez» sin señal · 30,0 la costura y «Guardar asistencia» · 32,0 se envía sola · 36,0 el látigo ·
  44,0 «Mapa» · **52,0 las zonas sin reunión** (el segundo golpe más fuerte) · 60,0 la lista en el clímax · 70,0 la ficha · 86,0 la frase
  final · 92,0 la corona.
- **Transiciones con causa (cinco clases):** match cut sobre el toque (el reporte, la lista sin señal, el mapa, la lista de eventos), iris
  desde el toque (la hoja «Persona nueva» del clip y la ficha del 70,0), **un solo látigo** (el cambio de persona y de mundo, 36,0), el
  cambio de tamaño de la ventana (88,0) y el dip + corte al cierre.

## Grabaciones (Kingdom Demo, `capturar.mjs --modo video`, sin el círculo del toque)

| Grabación | Para qué | Estado |
|---|---|---|
| `clips/eventos-casa-de-paz` (celular, cuenta 103) | 0–26,0: la historia, con el montaje ya verificado del clip | **Se reusa** (`clip-sitio-eventos/assets/grabaciones/`) |
| `clips/recorrido-eventos-sin-senal` (celular, 103) | 26,0–36,0: rehace el mismo reporte (sin usarlo), apaga la red, «Volver a la lista», la casa, «Igual», «Guardar», vuelve la señal | **Nueva**, SPEC §4.2 |
| `clips/recorrido-eventos-tablero` (computador, 103 y luego 101) | 36,0–92,0: rehace el mismo reporte como Jorge (sin usarlo, para que la ficha diga «10 personas» y nombre a Ximena) y entra como el pastor: tablero, mapa, lista, ficha | **Nueva**, SPEC §4.3 |

Las tres sobre **la misma carga de Kingdom Demo** (la reunión pendiente del miércoles 28 de octubre): las escenas nuevas lo comprueban y se
niegan si la semilla es de otro día.

## Riesgos (el detalle en SPEC §7)

- **Que la semilla cambie de día:** la ficha diría otra fecha que la del «¡Listo!». La `ref` `mismaSemilla` lo impide; si falla, se regraban
  las tres escenas el mismo día y se recalculan los cuadros del clip.
- **Que «Zonas sin evento» salga vacía** con los valores por defecto (10 personas, 2 km): plan B en la escena, 5 personas.
- **El mapa necesita sus teselas de internet** (OpenFreeMap) al grabar; se corta la espera.
- **La costura de la música** se mide (sin pico ni hueco en el 30,0), no se oye.
- **El cargador de la app** y las esperas del servidor se cortan, como en el clip.
