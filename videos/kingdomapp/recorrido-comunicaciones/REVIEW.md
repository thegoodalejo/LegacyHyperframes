# REVIEW · Recorrido de Comunicaciones — «Alguien nuevo escribe… y nadie se queda sin respuesta» (16:9)

2026-10-30 · Construido en HyperFrames 0.8.221 a partir de [SPEC.md](SPEC.md) y [STORY.md](STORY.md). Usa la grabación del clip
(`assets/grabaciones/clip/grabacion.mp4`) y las dos nuevas: `assets/grabaciones/celular.mp4` (1170×2532, 30 fps, 2476 cuadros) y
`assets/grabaciones/escritorio.mp4` (1920×1080, 30 fps, 1340 cuadros), cada una con su `-pasos.json` y su `-hoja.jpg`. El dueño ya no
revisa: se construyó, se verificó y se renderizó sin paradas. **Entrega:** `renders/recorrido-comunicaciones-16x9.mp4`.

## 1. Qué hay

| Archivo | Qué es |
|---|---|
| `index.html` | La raíz, **generada** por `_gen/gen.py` desde `_gen/index.tpl.html`. Tiene el formato (`--f-*`, `--e-*` y `window.KD`), los hosts de las escenas y `#escena`, la tira horizontal con las dos ventanas. Además: los 46 tramos de video, los 3 stills, las 26 marcas de toque, las 5 cámaras, los 4 látigos, los 5 aterrizajes, la ventana que se hace a un lado, el dip, la música y los 48 sonidos (46 de acción, la subida y la marca) |
| `compositions/fondo.html` | La noche del sitio. El halo se asienta en 0 · 180 · 840 · 1320 · 1680 · 2040 · 2520 (a mano) |
| `compositions/frase-1…8.html`, `ceja.html` | Las ocho frases y la ceja «COMUNICACIONES» con sus dos lugares (generadas) |
| `identidad/cierre-comercial.html` | El cierre del Comercial del kit v1.1 (2760–2909), con `{"publico":"iglesia","llamado":"prueba","contacto":"sitio","fondo":"noche","idioma":"es"}` y las campanas en el 92,38 |
| `_gen/gen.py`, `_gen/index.tpl.html`, `_gen/README.md` | El generador: las tablas de tramos, stills, marcas, sonidos y frases, y la plantilla con las cámaras |
| `_gen/musica.sh`, `_gen/mix.py` | Rehace la música desde el mp3 (SPEC §0.1); simula la mezcla con ffmpeg antes de renderizar |
| `assets/grabaciones/clip/` | La grabación del clip y su `pasos.json`, copiadas sin cambios |
| `assets/stills/still-e403.png`, `still-e559.png` | Escritorio: «hola» enviado antes de la respuesta (994–1019); «Horarios» tocado antes del horario (1142–1154) |
| `assets/stills/still-c2060.png` | Celular: la vista previa de la campaña, quieta (2410–2759) |
| `assets/audio/toque-b.wav`, `toque-c.wav` | Las tomas b y c de `toque`, copiadas del clip |
| `assets/musica/product-launch-recorrido.wav` | «Product Launch» editada como en Academia (§5); idéntica, byte a byte, a la de `recorrido-equipos` |

```text
#escena (x 0 = celular · x −1920 = escritorio; látigos 830–840 ←, 1310–1320 →, 1670–1680 ←, 2030–2040 →)
  #ventana-cel.k-ventana.k-ventana-16x9 (x 1104 · y 90 · 720×900)
    #celK > #camK   el clip (0–841)
    #celM > #camM   celular.mp4: la conversación de Mariana y su ficha (1310–1680)
    #celC > #camC   celular.mp4: la campaña nueva para la red Timoteo (2030–2760)
    #datos-cel · #dip
  #ventana-esc.k-ventana.k-ventana-escritorio (x 2160 · y 260 · 1440×760)
    #e1in > #camE1  escritorio.mp4: el flujo del chatbot y «Probar» (830–1320)
    #e2in > #camE2  escritorio.mp4: la automatización «Bienvenida a quien llega» (1670–2040)
    #datos-esc
```

## 2. Los planos

«rec.» es el cuadro de la grabación nueva de ese aparato. **Todos los tramos van a 1×.** Escalas: G ×1,085 · G⁺ ×1,15 · F ×1,18 · M ×1,4
(celular); D ×1,8 · D⁺ ×2,0 (escritorio).

| Plano | Cuadros | Grabación y cámara |
|---|---|---|
| P1–P6 El clip | 0–839 | Los mismos 19 tramos, 8 marcas, match cut y 16 sonidos del clip. Todas las cámaras a 1,085 con los centros de SPEC §2.1, salvo `compositor`, que pasa de cx 196,5 a **194**: la lista de respuestas rápidas empieza en el CSS 16,3 y el «/» de «/bienvenida» quedaba cortado. La frase 3 se queda hasta el 837 y la cámara, en `cierre` desde el 720: seis nombres con «Leído» y «↩ Allí estaré» |
| P8 «Responde a cualquier hora.» | 840–1319 | **Látigo al escritorio** 830–840 (aterriza 1,04 → 1,00). El lienzo de «Bienvenida con menú» en D `lienzo` (CSS 155–866 × 268–643). 870 → D `probar`: «Probar» y el panel «Palabras de activación» con buenas · hola · menu. **900: toque en «Probar»** (rec. 107). **902: corte** (BANNED 41) al simulador listo (rec. 255): «Probar el flujo», «Es una prueba: no se envía nada por WhatsApp ni queda nada guardado.», «Probando como Carolina Mejía Arango», legibles ya en D. 915 → D⁺ `simulador`. **960: toque en «Escribe como la persona…»** (rec. 344) en la costura de la música; el panel se desplazó solo 85 px CSS (rec. 332) y el encuadre baja con él en el mismo cuadro (D⁺ `campo`); «hola» se escribe a 1×. **990: enviar** (rec. 399): «hola» a la derecha; still de la rec. 403 hasta el 1019. **1020: el chatbot contesta** (rec. 404): «Empezó el flujo «Bienvenida con menú»», «¡Hola Carolina! Bienvenido a Iglesia Kingdom Demo 1.», «¿En qué te podemos ayudar?», Horarios · Oración · Hablar con alguien. 1080 → D⁺ `menu`. **1140: «Horarios»** (rec. 556); still de la rec. 559. **1155: el horario** (rec. 560): «Nos reunimos los domingos a las 8:00 a. m. y a las 10:30 a. m., y los miércoles a las 7:00 p. m. ¡Te esperamos!» y «El flujo terminó». 1200 → D⁺ `horario`; se lee 3,7 s |
| P9 «De un chat a su ficha.» | 1320–1679 | **Látigo de vuelta.** La conversación de Mariana (rec. 414–491) en G `hiloM`: «Sin ficha · +575550123987», «Atendiendo», su pregunta, «Andrés Felipe Restrepo Gómez tomó la conversación» y la respuesta con el horario. **1380: el ícono de la persona** (rec. 484). En el 1388 el panel «La persona» (rec. 542; la etiqueta «La persona» del ícono, rec. 492–495, queda fuera). 1395 → G `panelM`. **1440: «Crear ficha»** (rec. 594) y el diálogo entra a 1×. 1455 → G `dialogo`: «Crear ficha · Con el número +575550123987…», «Mariana», «Ospina». **1500: «¿Cómo llegó?»** (rec. 710) · **1530: «Redes sociales»** (rec. 781) · **1545: «Crear ficha»** (rec. 858). **1560: la ficha** (rec. 878; el fundido 873–877 queda fuera) con punch a M `fichaM`: «MO · Mariana Ospina · +575550123987 · Ver ficha». 1620 → G `panelM`: Boletas, «Notas del equipo» |
| P10 «La bienvenida sale sola.» | 1680–2039 | **Látigo al escritorio.** Automatizaciones (rec. 828–960) en D `autos`: «Bienvenida a quien llega · Encendida · Cuando llega una persona nueva (1 h después) · Personas de Membresía · Hoy: 4 enviados · 0 omitidos», «Feliz cumpleaños», y la segunda fila. 1740 → D⁺ `tarjeta`. **1800: toque en la tarjeta** (rec. 958). **1803: corte** a la automatización (rec. 1050; la carga 961–968 queda fuera) con el encuadre en D⁺ `vista`: «Vista previa» y el mensaje entero. **1890** → D `pestanas`: «Encendida · Hoy: 4 enviados · 0 omitidos» y «Configuración · Envíos · Historial». **1920: toque en «Envíos», dibujado** (la válvula de SPEC §5). **1923: corte** a los envíos (rec. 1180; la carga 1171–1179 queda fuera), ya en D `envios`: Isabela Muñoz Salazar, Tomás Cano Ochoa, Sara Lucía Bermúdez Ríos y Mateo Arango Vélez, cada uno con «Persona nueva · 30-10-2026 13:54». **1980** → D `leidos`: la cámara recorre las filas hasta los cuatro «Leído» |
| P11 «Cada aviso, a quien lo necesita.» | 2040–2279 | **Látigo de vuelta.** La campaña nueva en «2 A quién va» (rec. 1360–1436) en G `publico` (CSS 0–359 × 0–449). **2100: «Un público»** (rec. 1422): «Agregar filtro». **2130: «Agregar filtro»** (rec. 1513); la hoja sube a 1×. 2145 → G `hoja` (abajo del todo). **2160: «Red»** (rec. 1583). **2163: corte** al editor «Red» ya puesto (rec. 1616): el cambio de hoja (rec. 1590–1597) deja ver la página con la cifra de toda la iglesia y la ayuda de «Calcular», y queda fuera (§4.3). **2190: «Red Timoteo»** (rec. 1643), la casilla se marca. **2220: «Aplicar»** (rec. 1700). **2227: corte** (la hoja se va en la rec. 1707–1709, fuera) con el encuadre en G⁺ `cifra` en el mismo cuadro: el chip «Red: Red Timoteo». **2235** (rec. 1723): «Personas de la red Red Timoteo» y la cifra corre a 1× hasta «≈ 143 personas · 139 con WhatsApp» (2253, rec. 1741) |
| P12 «… y la vista previa» | 2280–2519 | **2280: la app sube** a «1 El mensaje» en un cuadro (rec. 1852, salto real) y el encuadre cambia con ella, en el mismo cuadro, a G `lista` (§4.7). **2310: «Plantilla aprobada»** (rec. 1925): las plantillas aprobadas con su categoría. **2340: «invitacion_culto · marketing»** (rec. 1995). **2343: corte** (la onda 1996–2004 queda fuera) con el encuadre en G `vistaPrevia` en el mismo cuadro: la vista previa de WhatsApp ya llena, «Hola [Primer nombre], este domingo celebramos [Qué celebramos]. Te esperamos a las 10:30 a. m. con toda tu familia.», **«Allí estaré»** y «Cómo llegar». Desde el 2410, still de la rec. 2060. 2460 → F `final` |
| P13 La frase del sitio | 2520–2759 | «Habla con tu iglesia, / sin perder a *nadie*» de 2520 a 2534. La ceja se va en 2520–2523. La ventana se hace a un lado (0,92, +24) en 2524–2538. `subida` desde el 90,533. Dip 2757–2759 |
| P14 El cierre | 2760–2909 | `cierre-comercial`, con las campanas en el 92,38 |

## 3. Sincronía (parte 2; la parte 1 es la del clip, REVIEW del clip §3)

El sonido cae un cuadro después de la imagen: `data-start` = (imagen + 1) / 30 − acento. Cada toque se dibuja (la marca aparece 4 cuadros
antes, se hunde en el cuadro y se va 6 después, o con el corte) y suena en el cuadro siguiente.

| Qué | Imagen | Pulso (fuerza) | Sonido | rec. | Desvío |
|---|---|---|---|---|---|
| Látigo al escritorio; frase 4 | 830–840 · 843–849 | **840 (1,00)** | `desliz` 1,4 | — | 0 |
| Cámara → «Probar» | 870–883 | 870 (0,51) | — | — | 0 |
| Toque «Probar» | 900 | 900 (0,84) | `toque` a | 107 | 0 |
| Corte al simulador con Carolina | 902 | — | — | 255 | SPEC 905 (§4.2) |
| Cámara → D⁺ simulador | 915–928 | 915 (0,82) | — | — | 0 |
| Toque en el campo y «hola» (la costura) | 960 · 960–968 | **960 (0,92)** | `toque` b | 344–352 | 0 |
| Toque enviar | 990 | 990 (0,58) | `toque` c | 399 | 0 |
| El chatbot contesta | 1020 | 1020 (0,77) | `aparicion` | 404 | 0 |
| Cámara → menú | 1080–1093 | 1080 (0,76) | — | — | 0 |
| Toque «Horarios» | 1140 | 1140 (0,75) | `toque` a | 556 | 0 |
| El horario | 1155 | 1155 (0,61) | `confirmacion` 1,4 | 560 | 0 |
| Cámara → horario | 1200–1213 | 1200 (0,67) | — | — | 0 |
| Látigo de vuelta; frase 5 | 1310–1320 · 1322–1332 | **1320 (0,93)** | `desliz` | — | 0 |
| Toque en el ícono de la persona | 1380 | **1380 (0,90)** | `toque` b | 484 | 0 |
| El panel «La persona» | 1388 | — | — | 542 | (a 1×: la app tarda 8 cuadros) |
| Cámara → panel | 1395–1408 | **1395 (0,89)** | — | — | 0 |
| Toque «Crear ficha» | 1440 | **1440 (0,96)** | `toque` c | 594 | 0 |
| Cámara → diálogo | 1455–1468 | 1455 (0,77) | — | — | 0 |
| Toque «¿Cómo llegó?» | 1500 | **1500 (0,88)** | `toque` a | 710 | 0 |
| Toque «Redes sociales» | 1530 | 1530 (0,62) | `toque` b | 781 | 0 |
| Toque «Crear ficha» | 1545 | 1545 (0,60) | `toque` c | 858 | 0 |
| La ficha de Mariana; punch | 1560 · 1560–1568 | **1560 (1,00)** | `confirmacion` 1,4 | 878 | 0 |
| Cámara → panel entero | 1620–1633 | 1620 (0,84) | — | — | 0 |
| Látigo al escritorio; frase 6 | 1670–1680 · 1683–1689 | **1680 (0,98)** | `desliz` | — | 0 |
| Cámara → tarjeta | 1740–1753 | 1740 (0,79) | — | — | 0 |
| Toque en la tarjeta | 1800 | **1800 (1,00)** | `toque` a | 958 | 0 |
| La automatización y su vista previa (cámara en el corte) | 1803 | — | `aparicion` | 1050 | 0 |
| Cámara → banda y pestañas | 1890–1903 | 1890 (0,71) | — | — | válvula de SPEC §5 (§4.4) |
| Toque «Envíos» (dibujado) | 1920 | **1920 (1,00)** | `toque` b | 1167 ≈ 1170 | se dibuja (§4.4) |
| Los envíos (cámara en el corte) | 1923 | — | `aparicion` | 1180 | 0 |
| Cámara → «Leído» | 1980–1993 | 1980 (0,62) | — | — | §4.5 |
| Látigo de vuelta; frase 7 | 2030–2040 · 2042–2052 | **2040 (1,00)** | `desliz` | — | 0 |
| Toque «Un público» | 2100 | 2100 (0,71) | `toque` c | 1422 | 0 |
| Toque «Agregar filtro» | 2130 | 2130 (0,73) | `toque` a | 1513 | 0 |
| Cámara → la hoja | 2145–2158 | 2145 (0,71) | — | — | no estaba en el SPEC (§4.3) |
| Toque «Red» | 2160 | **2160 (1,00)** | `toque` b | 1583 | 0 |
| Corte al editor «Red» | 2163 | — | — | 1616 | §4.3 |
| Toque «Red Timoteo» | 2190 | 2190 (0,58) | `toque` c | 1643 | 0 |
| Toque «Aplicar» | 2220 | 2220 (0,54) | `toque` a | 1700 | 0 |
| La hoja se va (cámara en el corte) | 2227 | — | — | 1715 | §4.3 |
| La cifra corre | 2235–2253 | **2235 (1,00)** | `confirmacion` 1,4 | 1723–1741 | 0 |
| La app sube; el encuadre cambia con ella | 2280 | **2280 (0,77)** | `desliz` | 1852 | SPEC: cámara quieta y movimiento al 2295 (§4.7) |
| Toque «Plantilla aprobada» | 2310 | 2310 (0,41) | `toque` b | 1925 | 0 |
| Toque «invitacion_culto» | 2340 | 2340 (0,46) | `toque` c | 1995 | 0 |
| La vista previa llena (cámara en el corte) | 2343 | — | `aparicion` | 2005 | 0 |
| (la app no sube: ya está a la vista) | 2400 | 2400 (0,76) | — | — | sin `desliz` (§4.6) |
| Cámara → la burbuja (F) | 2460–2473 | 2460 (0,46) | — | — | 0 |
| Frase del sitio; ceja sale | 2519–2534 · 2520–2523 | **2520 (0,80)** | — | — | 0 |
| La ventana a un lado | 2524–2538 | — | — | — | 0 |
| `subida` → cierre | 2716–2773 | golpe en 2761 | `subida` | — | 0 |
| Dip; cierre | 2757–2759 · 2760 | 2760 | marca 92,38 | — | 0 |

Ningún par de sonidos se encima salvo los del SPEC (1800 + 1803, 1920 + 1923, 2340 + 2343). Sin tics de tecla.

## 4. Desvíos del SPEC y su porqué

1. **Lo que trajo la grabación** (todo real, nada se retocó):
   - El chatbot saluda «¡Hola Carolina! Bienvenido a **Iglesia Kingdom Demo 1**.» (el SPEC esperaba «Kingdom Demo»); el horario es el mismo,
     palabra por palabra, que el de «/horarios» de la parte 1, más «¡Te esperamos!».
   - Las dos vistas previas usan los marcadores de la app, no los ejemplos de la plantilla: la bienvenida dice «Hola [Primer nombre], gracias
     por visitarnos en [Iglesia]. Alguien del equipo te escribirá para acompañarte. Si necesitas algo, responde a este mensaje.» y la campaña
     «Hola [Primer nombre], este domingo celebramos [Qué celebramos]. Te esperamos a las 10:30 a. m. con toda tu familia.», con «Allí estaré»
     y «Cómo llegar». El SPEC esperaba «Hola Ana… la Santa Cena». Ninguna frase depende de eso.
   - Los cuatro envíos de la bienvenida están en «Leído» (ninguno en «Entregado»). La red Timoteo da **≈ 143 personas · 139 con WhatsApp**:
     el mismo 139 de la invitación de la parte 1.
   - No hubo fichas parecidas al crear la de Mariana: «Crear ficha» guardó directo.
   - La ficha aparece en el panel en la rec. 878 (el panel no cambia de la 878 a la 1182). La cabecera del hilo («Sin ficha») queda tapada
     por el panel en todo el plano, así que la comprobación «la cabecera sin «Sin ficha»» del SPEC §4.4 no se puede ver: lo que se ve es el
     panel con «MO · Mariana Ospina» y «Ver ficha».
2. **El corte al simulador va en el 902, no en el 905.** La app cambia el panel en la rec. 109, dos cuadros después del clic; el 903–904
   habría mostrado el simulador vacío («Probar como una persona de la iglesia…»). En el 902 ya se lee «Probando como Carolina Mejía Arango»,
   y el encuadre `probar` (D) deja leer el título, el aviso de prueba y la persona desde ese cuadro.
3. **La decisión 215 manda en la campaña** (BANNED 38). El texto de ayuda de «A quién va» («Calcular» dice cuántos la reciben de verdad…)
   está pegado debajo de la cifra: a 11 px CSS en la rec. 1400 y a 13 px en la 1745. Por eso:
   - el aterrizaje (`publico`, G, CSS 0–449) muestra «A quién va» **sin** la cifra de toda la iglesia: la cifra y la ayuda empiezan en el
     455,7 y el 479,7. El SPEC pedía la sección entera con la cifra;
   - las hojas «Agregar filtro» y «Red» están abajo de la pantalla (Red en el 753, Red Timoteo en el 750, «Aplicar» en el 807): fuera de
     `publico`. Se agregó un movimiento de cámara en el **2145** (G `hoja`, abajo del todo), que el SPEC no tenía;
   - **el cambio de hoja de la rec. 1590–1597 se corta** (2160 → 2163): en esos cuadros la hoja «Agregar filtro» se va y deja ver, por
     debajo, «≈ 1.325 personas · 1.170 con WhatsApp» y la ayuda. Se encontró en el primer render (cuadros 2168–2172) y se quitó;
   - cuando la hoja «Red» se va (rec. 1707–1709) la cámara estaba abajo, donde la ayuda queda a la vista. Ese cierre se corta (2227) y el
     encuadre sube a `cifra` en el mismo cuadro; en el 2235 la tarjeta cambia y la cifra corre sin que la cámara se mueva;
   - `cifra` (G⁺) termina en el CSS 546: la cifra acaba en el 534,7 y la ayuda empieza en el 547,7. La píldora «Datos de ejemplo» va abajo a
     la izquierda de la ventana, como en todo el video, así que **cae sobre «≈ 143 personas ·»**. El encuadre se corrió (x CSS 36–375) para
     que el borde de la píldora quede en el 191 y «139 con WhatsApp» (desde el 197,7) se lea entero. No hay otra salida: la píldora ocupa los
     38 px CSS de abajo del encuadre y entre la cifra y la ayuda solo hay 13.
4. **«Envíos» se dibuja** (la válvula de SPEC §5, y el encargo: cada acción con su toque dibujado). El mensaje se lee del 1803 al 1889
   (2,9 s, no 3,9), en el 1890 la cámara va a D `pestanas` (la banda «Encendida · Hoy: 4 enviados · 0 omitidos» y las pestañas) y el toque
   del 1920 cae sobre «Envíos». En el 1923 la lista entra con el encuadre ya en las cuatro filas.
5. **Los nombres y «Leído» no caben juntos.** Las filas de envíos van del CSS 135 al 1250 y «Leído» está en el 1180–1240: en D (711 px
   CSS) no entran con los nombres. En el 1980 la cámara recorre las filas hasta los cuatro «Leído» (D `leidos`) y se queda ahí 1,2 s antes
   del látigo. El SPEC pedía D⁺ sobre «nombre y estado».
6. **La vista previa de la campaña ya está a la vista en el corte del 2343** (la app la llena arriba y el encuadre sube a ella en el mismo
   cuadro). Por eso el 2400 no tiene `desliz` ni movimiento (SPEC §2.2: «si ya está a la vista, quieto»); el salto de la grabación a «Nueva
   campaña» (rec. 2073) no se usa: del 2410 al 2759 va un still de la rec. 2060. El final es F (×1,18) con «Vista previa» fuera: en F no
   caben a la vez la etiqueta (x 18) y el texto de la burbuja (x 36–350).
7. **El salto del 2280 cambia el encuadre en el mismo cuadro** (a G `lista`), en vez de quedar quieto y moverse en el 2295: con el encuadre
   de la cifra (x 36–375), el salto dejaba «Elige una plantilla…» cortado a la izquierda medio segundo. Es un corte con causa: la pantalla
   entera cambia en la rec. 1852.
8. **El 1020 no mueve la cámara**: `campo` (D⁺, CSS 371–709) ya muestra el saludo y el menú enteros; el movimiento va en el 1080 (`menu`),
   como dice el SPEC.
9. **Tres stills** sostienen la app donde espera menos que el pulso: «hola» enviado (rec. 403, 994–1019: la app contesta en 5 cuadros y el
   pulso pide 30), «Horarios» tocado (rec. 559, 1142–1154) y la vista previa quieta (rec. 2060, 2410–2759).
10. **Lo que se cortó de la app:** la búsqueda de Carolina (rec. 162–246, BANNED 41); el desplazamiento solo del panel del simulador (rec.
    332, cae en el corte del 960); la etiqueta «La persona» del ícono dentro del panel (rec. 492–495; antes del toque, en 1385–1387, se ve
    la etiqueta real del ícono); el fundido del diálogo de ficha (873–877); las cargas de la automatización (961–968) y de los envíos
    (1171–1179); el cambio de hoja de los filtros (1590–1597) y el cierre de la hoja «Red» (1707–1714); la onda de la plantilla
    (1996–2004).
11. **Píldoras sobre texto que no se lee:** en el diálogo «Crear ficha» la píldora tapa casi todo «Cancelar» (se lee «…elar» a su lado);
    en el editor «Red» queda junto a «Cancelar». El diálogo ocupa 450 px CSS de alto, lo mismo que G: no hay encuadre de lectura que deje
    los botones encima de la píldora sin cortar el título.
12. **«Datos de ejemplo» a 31 px** (alto 56), no a los 22 del kit para 16:9, como el clip y los otros recorridos: con la ventana a 0,92
    sigue en ≥ 28 px.
13. **Parte 1:** `compositor` pasa de cx 196,5 a 194 (el «/» de «/bienvenida» quedaba cortado). Lo demás es el clip, tal cual.

## 5. La música, la costura y la mezcla

- **La edición** es la de Academia (SPEC §0.1), rehecha con `_gen/musica.sh` desde `assets/musica/product-launch-the-mountain.mp3`:
  **95,997 s** (`ffprobe`), idéntica byte a byte a la de `recorrido-equipos` (md5 655d22c6…). La costura (31,96–31,99 del video) cae en el
  simulador, en el cuadro 960, donde se toca el campo y se escribe «hola»: la imagen no corta y la frase está quieta.
- **La costura, medida:** el mayor salto entre muestras dentro del cruce (31,955–31,995) es 0,039, igual que en los 25 ms anteriores (0,039); el mayor de la zona es 0,045 y cae en el 32,000, el ataque del golpe del compás, no en el cruce: no hay clic. La energía en 400 ms pasa de −13,9 dB (antes) a −12,6 dB (después): es el golpe del 32,0. `hyperframes audio … --only beats` da la grilla de 0,5 s pareja: 30,495 · 31,015 · 31,515 · 31,995 · 32,505 · 32,995 · 33,455, sin pulso doble ni perdido entre el 31,0 y el 33,0. **No se oyó.**
- **El render:** **−17,0 LUFS integrados, pico real −2,5 dBTP** (ffmpeg `ebur128` y `hyperframes audio` coinciden), sin recortes, LRA 2,8 LU, corto plazo máximo −15,4. La simulación previa con `_gen/mix.py` dio lo mismo (−17,0 / −2,5). Queda en el «en torno a −17» del encargo y dentro del ±1 del SPEC (−16); no se normalizó. Niveles: toques a 1,0; confirmaciones de las pruebas (302, 675, 1155, 1560, 2235) y el primer látigo a 1,4; lo demás a 1,0; música a 0,75 en el carril.
- **Los golpes:** `hyperframes audio` sobre el render detecta los **27 `toque`, cada uno un cuadro después de su imagen**: parte 1: 76 · 121 · 181 · 241 · 301 · 376 · 421 · 601 · 661; parte 2: **901 · 961 · 991 · 1141 · 1381 · 1441 · 1501 · 1531 · 1546 · 1801 · 1921 · 2101 · 2131 · 2161 · 2191 · 2221 · 2311 · 2341**. Las `aparicion`, `confirmacion` y `desliz` quedan por debajo del umbral del detector (entre 4 y 10 dB bajo la música, como manda el kit); su sitio está en la tabla de §3 y en `gen.py`.
- Música a 0,75 todo el video, sin fundido: el último acorde se apaga solo debajo del cierre. Las campanas en el 92,38.

## 6. Lo que se revisó

- `npx hyperframes check --json`: **0 errores**. Un aviso que se deja a propósito: `composition_file_too_large` (636 líneas): la raíz lleva
  los 46 tramos para que se vean y se recorten en la línea de tiempo, como el clip y los otros recorridos; la genera `gen.py`. El
  `dead_stretch` de la frase del sitio (86,96–91,82) se resolvió con `data-hold` en su host: la quietud es a propósito.
- `npx hyperframes snapshot --review`: `.hyperframes/artifacts/snapshots/9b04c792-2323-4be6-a97e-9d336b0956c4/` (`review-beats-1…6.jpg`,
  59 `review-seam-*.jpg`, `review-phone-1…6.jpg`), más tres rondas de cuadros clave (`snapshot --at`). Notas que salieron y se corrigieron:
  - **P0:** las hojas «Agregar filtro» y «Red» quedaban fuera del encuadre de la campaña (los toques en «Red», «Red Timoteo» y «Aplicar»
    caían fuera de cuadro) → movimiento al 2145 (§4.3).
  - **P0:** al cerrarse la hoja «Red» con la cámara abajo se veía la ayuda de «Calcular» → corte con encuadre en el 2227 (§4.3).
  - **P0 (en el primer render):** el cambio de hoja de los filtros dejaba ver la cifra de toda la iglesia y la ayuda en los cuadros
    2168–2172 → se cortó (2160 → 2163) y se volvió a renderizar.
  - **P1:** el campo «Escribe como la persona…» quedaba cortado abajo; «queda nada guardado» cortado arriba en `horario`; la barra de arriba
    de la app asomaba en `panelM` y `fichaM`; «Vista previa» cortada en el final; «Elige una plantilla…» cortado tras el salto del 2280;
    «/bienvenida» cortado en `compositor`. Todos corregidos con los encuadres medidos sobre la grabación (filas y columnas de texto en px
    CSS, §2).
  - **P1:** la píldora sobre la cifra (§4.3), resuelta corriendo el encuadre.
- La hoja del celular (360 px) lee las frases; el texto de la app a esa escala es textura, como en todo 16:9 de la serie.
- **El render final, cuadro a cuadro** (hojas de cuadros alrededor de cada látigo, toque y corte): cada marca de toque cae en su pulso, sobre su botón; los cortes del 902, 960, 1803, 1923, 2163, 2227 y 2343 caen limpios; **la ayuda de «Calcular», la cifra de toda la iglesia, créditos, saldos, precios, «Encender» y «Uso» no aparecen en ningún cuadro** (revisados uno a uno 2137–2262, que es donde están cerca); el simulador lee «Es una prueba: no se envía nada por WhatsApp ni queda nada guardado» desde el 902; los látigos no dejan ningún cuadro con las dos ventanas vacías; dip 2757–2759 y el cierre desde el 2760. `ffprobe`: H.264 1920×1080, 30 fps, **2910 cuadros, 97,000 s**; AAC 48 kHz estéreo; 18,6 MB. Tardó 10 min 10 s en renderizar (con TEMP en `F:	mp-hf-com`: el disco C tenía 0,9 GB libres y el primer intento se negó a arrancar).
- La vista previa del editor no se abrió: nadie la iba a mirar y el render se verificó cuadro a cuadro.
- Nadie oyó el sonido ni vio el movimiento a velocidad real.

## 7. El plano más débil y qué cambiaría con más tiempo

- **«Leído» (1980–2029):** el final de cuatro filas casi vacías con su «Leído» a la derecha. La pantalla de envíos usa todo el ancho del
  escritorio y el estado queda lejos del nombre. Con más tiempo: grabar el escritorio con la ventana más angosta (o la vista de envíos en
  el celular), para que nombre y «Leído» entren en un mismo D.
- **La cifra de la red Timoteo:** la píldora tapa «≈ 143 personas» y la ayuda de «Calcular» obliga a encuadrar justo encima. Con más
  tiempo: que la escena desplace la página hasta dejar la cifra justo arriba de la barra de abajo (la ayuda quedaría debajo de la barra) y
  encuadrar ahí, con la píldora sobre la barra.
- **El diálogo «Crear ficha»** con la píldora sobre «Cancelar».
- La 9:16 queda para después (SPEC: no se especifica aquí).
