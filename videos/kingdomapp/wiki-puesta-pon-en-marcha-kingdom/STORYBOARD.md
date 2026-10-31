# STORYBOARD — Pon en marcha una iglesia celular

Tiempos del render en español. La duración de cada escena es la mayor entre su tramo de la grabación y su voz; las frases exactas están en
`guion.mjs` (y `SCRIPT.md`). Cortes directos entre escenas. La grabación es la app real con Kingdom Demo (administrador, cuenta 101), de escritorio.

| # | Tramo | Inicio | Dura | Qué se ve |
|---|---|---|---|---|
| — | Intro del kit | 0,0 | 3,0 | Corona que se levanta, «Kingdom · Ayuda», chip «Puesta en marcha», título |
| 1 | `abrir` | 3,0 | 18,1 | Servir con la tarjeta «Tu arranque»; se toca «Ver mi ruta» y se abre la ruta |
| 2 | `cuestionario` | 21,1 | 25,1 | «Responder»; el cuestionario: Celular, Hasta 300, Ordenar mi membresía, Es independiente, Con un equipo; «Guardar y seguir» |
| 3 | `iglesia` | 46,2 | 10,3 | La etapa «Tu iglesia» con sus pasos (uno ya con «Hecho») |
| 4 | `palabras` | 56,5 | 8,3 | «Revisa las palabras»: «Están bien así» |
| 5 | `marca` | 64,8 | 11,3 | «Hacerlo ahora» abre Marca; «Personalizar», se elige el color y «Guardar» |
| 6 | `hecho` | 76,1 | 9,4 | De vuelta en la ruta: «¡Terminaste «Tu iglesia»!» y «Seguir» |
| 7 | `gente` | 85,5 | 11,6 | La etapa «Tu gente» abierta con sus cuatro pasos |
| 8 | `red` | 97,0 | 20,3 | «Hacerlo ahora» abre Estructura; «Crear Red», nombre, líder elegido de la lista y «Guardar» |
| 9 | `marcado` | 117,4 | 9,2 | La ruta con «Organiza a tu gente en redes» y «Asigna a los líderes» en «Hecho» |
| 10 | `equipo` | 126,5 | 17,0 | La etapa «Tu equipo» con sus cuatro pasos |
| 11 | `sigue` | 143,5 | 22,6 | Las etapas de los módulos y el pie: «Ya conozco Kingdom», «Cambiar mis respuestas», «Ocultar del inicio» |
| — | Cierre del kit | 166,1 | 4,0 | «Sigue con: Responder el cuestionario y recorrer tu ruta de arranque», la corona y la frase de la Ayuda |

Total: 170,1 s en español y 173,1 s en inglés (cuerpo de 2 min 43 s y 2 min 46 s). Revisado con `check` (0 errores, contraste AA) y snapshots de cada escena, la intro y el cierre el 2026-10-31.
Con «Celular» la app no propone palabras distintas a las que la iglesia ya usa: la escena cierra «Revisa las palabras» con «Están bien así» (no aparece la pantalla de «Usar este vocabulario»). La demo ya tiene redes, personas y equipo: el `sql` de la escena la deja sin redes propias y con la ubicación puesta; los pasos de «Tu equipo» con «Hecho» son de la demo.
