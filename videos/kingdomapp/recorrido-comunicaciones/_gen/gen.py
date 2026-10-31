# Genera index.html y compositions/frase-*.html + ceja.html del recorrido de Comunicaciones (16:9), desde index.tpl.html y estas tablas.
#   python _gen/gen.py            (desde recorrido-comunicaciones/)
# Tramos de video, stills, marcas de toque, sonidos y frases -> HTML. Los cuadros son del video (30 fps); «rec» = cuadro de la grabación.
import os

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
FPS = 30
def s(n): return f"{n / FPS:.6f}".rstrip('0').rstrip('.')
def ms(g): return f"{g / FPS + 0.01:.6f}".rstrip('0').rstrip('.')

K = 'assets/grabaciones/clip/grabacion.mp4'   # la grabación del clip (1170×2532, 1602 cuadros)
C = 'assets/grabaciones/celular.mp4'          # la grabación nueva de celular (1170×2532, 2476 cuadros)
E = 'assets/grabaciones/escritorio.mp4'       # la grabación nueva de escritorio (1920×1080, 1340 cuadros)

# ── Tramos: (id, desde, hasta, rec, comentario) ─────────────────────────────────────────────────────────────────────────────────────────
# Parte 1: los 19 del clip, sin cambios (clip-sitio-comunicaciones/_gen/gen.py → TRAMOS)
TK = [
    ('v01', 0, 78, 40, 'Bandeja quieta, «Cola 4» (grab. 40–117); toque en la fila de Mariana en el 75 (grab. 115)'),
    ('v02', 78, 122, 193, 'match cut sobre el toque: la conversación ya cargada (grab. 193–236); entra 1,03 → 1,00; toque en «Tomar» en el 120 (grab. 235)'),
    ('v03', 122, 140, 246, 'corte en la onda del botón (237→246): «Atendiendo» y «… tomó la conversación» en el 122 (grab. 246)'),
    ('v04', 140, 182, 348, 'quieta (corte invisible 264→348); toque en el compositor en el 180 (grab. 388)'),
    ('v05', 182, 210, 394, 'corte en el foco (390→394): la tecla «/» y las respuestas rápidas en el 182 (grab. 394)'),
    ('v06', 210, 242, 476, 'quieta (corte invisible 422→476); toque en «/horarios» en el 240 (grab. 506)'),
    ('v07', 242, 270, 512, 'corte en la onda (508→512): el compositor lleno con el horario en el 242 (grab. 512)'),
    ('v08', 270, 302, 590, 'quieta (corte invisible 540→590); toque en enviar en el 300 (grab. 620)'),
    ('v09', 302, 340, 630, 'corte en la espera (622→630): la respuesta en el hilo en el 302 (grab. 630), con una palomita'),
    ('v10', 340, 377, 765, 'quieta (corte invisible 668→765); toque en volver en el 375 (grab. 800, fuera del encuadre: no se dibuja)'),
    ('v11', 377, 400, 808, 'corte en la espera (802→808): la lista con «Cola 3 · Mis chats 3» en el 377 (grab. 808)'),
    ('v12', 400, 422, 894, 'quieta (corte invisible 831→894); toque en «Campañas» en el 420 (grab. 914)'),
    ('v13', 422, 450, 928, 'corte en la espera y el esqueleto (916→928): las tarjetas suben escalonadas 422–432 (la animación de la app)'),
    ('v14', 450, 510, 1011, 'quieta (corte invisible 956→1011); la lista baja hasta la invitación en un cuadro en el 480 (grab. 1041, salto real)'),
    ('v15', 510, 602, 1098, 'quieta (corte invisible 1071→1098); toque en la invitación en el 600 (grab. 1188)'),
    ('v16', 602, 630, 1202, 'corte en la espera y el esqueleto (1190→1202): el reporte con sus números en el 602 (grab. 1202)'),
    ('v17', 630, 661, 1299, 'quieta (corte invisible 1230→1299); toque en «respondieron» en el 660 (grab. 1329)'),
    ('v18', 661, 675, 1335, 'corte en la onda (1330→1335): el contorno de «respondieron» en el 661 (grab. 1335)'),
    ('v19', 675, 841, 1396, 'la app baja a los nombres en un cuadro en el 675 (grab. 1396, salto real): «Destinatarios (23)», «Leído» y «Allí estaré»; el látigo horizontal se lo lleva en 830–840'),
]
# Parte 2 · el escritorio, el chatbot (#camE1, 830–1320)
TE1 = [
    ('e01', 830, 902, 37, '830–901 · el lienzo de «Bienvenida con menú» con el panel «Palabras de activación» (hola · menu · buenas) (rec 37–108); toque en «Probar» en el 900 (rec 107)'),
    ('e02', 902, 960, 255, '902–959 · corte sobre el toque (BANNED 41: la búsqueda de la persona de prueba, rec 162–246, queda fuera): el simulador listo, «Probar el flujo · Es una prueba: no se envía nada por WhatsApp ni queda nada guardado. · Probando como Carolina Mejía Arango» (rec 255–312)'),
    ('e03', 960, 990, 344, '960–989 · corte en el foco (el panel se desplazó solo en la rec 332): toque en «Escribe como la persona…» y «hola» se escribe a 1× (rec 344–352), quieto hasta la rec 373'),
    ('e04', 990, 994, 399, '990–993 · toque en enviar (rec 399): «hola» pasa a la derecha (rec 401)'),
    ('e05', 1020, 1080, 404, '1020–1079 · el chatbot contesta (rec 404): «Empezó el flujo «Bienvenida con menú»» · «¡Hola Carolina! Bienvenido a Iglesia Kingdom Demo 1.» · «¿En qué te podemos ayudar?» con Horarios · Oración · Hablar con alguien'),
    ('e06', 1080, 1142, 496, '1080–1141 · quieta (corte invisible 463→496); toque en «Horarios» en el 1140 (rec 556); los botones se apagan (rec 557)'),
    ('e07', 1155, 1320, 560, '1155–1319 · el horario (rec 560): «Nos reunimos los domingos a las 8:00 a. m. y a las 10:30 a. m., y los miércoles a las 7:00 p. m. ¡Te esperamos!» · «El flujo terminó» (rec 560–724); el látigo se lo lleva en 1310–1320'),
]
# Parte 2 · el escritorio, la automatización (#camE2, 1670–2040)
TE2 = [
    ('f01', 1670, 1803, 828, '1670–1802 · Automatizaciones: «Bienvenida a quien llega · Encendida · Cuando llega una persona nueva (1 h después) · Hoy: 4 enviados · 0 omitidos», «Feliz cumpleaños» (rec 828–960); toque en la tarjeta en el 1800 (rec 958)'),
    ('f02', 1803, 1923, 1050, '1803–1922 · corte en la espera (961–968 la página carga): la automatización con «Encendida · Hoy: 4 enviados · 0 omitidos», «Configuración · Envíos · Historial» y la vista previa (rec 1050–1169); toque en «Envíos» en el 1920 (rec 1167, quieto: el clic es la rec 1170)'),
    ('f03', 1923, 2040, 1180, '1923–2039 · corte en la espera (1171–1179, la lista carga): los envíos: Isabela Muñoz Salazar, Tomás Cano Ochoa, Sara Lucía Bermúdez Ríos y Mateo Arango Vélez, «Persona nueva · 30-10-2026 13:54», todos «Leído» (rec 1180–1296)'),
]
# Parte 2 · el celular, la ficha de Mariana (#camM, 1310–1680)
TM = [
    ('m01', 1310, 1388, 414, '1310–1387 · la conversación de Mariana, «Atendiendo», con su pregunta, la nota y la respuesta de Andrés (rec 414–491); toque en el ícono de la persona en el 1380 (rec 484)'),
    ('m02', 1388, 1470, 542, '1388–1469 · el panel «La persona» ya sin la etiqueta del ícono (rec 492–495, fuera): «Este número no está en Membresía…», «Vincular a una persona», «Crear ficha» (rec 542–623); toque en «Crear ficha» en el 1440 (rec 594); el diálogo entra a 1× (rec 601–608)'),
    ('m03', 1470, 1520, 680, '1470–1519 · quieta (corte invisible 623→680): «Crear ficha» con «Mariana» y «Ospina» ya puestos; toque en «¿Cómo llegó?» en el 1500 (rec 710); la lista abre (rec 717–721)'),
    ('m04', 1520, 1541, 771, '1520–1540 · quieta (corte invisible 729→771); toque en «Redes sociales» en el 1530 (rec 781); la lista se cierra (rec 782–791)'),
    ('m05', 1541, 1560, 854, '1541–1559 · quieta (corte invisible 791→854): «Crear ficha» encendido; toque en «Crear ficha» en el 1545 (rec 858); el diálogo empieza a irse (rec 870–872)'),
    ('m06', 1560, 1680, 878, '1560–1679 · corte en el fundido (873–877): el panel con la ficha: «MO · Mariana Ospina · +575550123987 · Ver ficha», «Campañas por WhatsApp · Autorizó los mensajes: escribió primero (30/10/2026)» (rec 878–997)'),
]
# Parte 2 · el celular, la campaña nueva (#camC, 2030–2760)
TC = [
    ('d01', 2030, 2070, 1360, '2030–2069 · una campaña nueva en «2 A quién va»: «Membresía · Un evento», «Toda la iglesia · Un público» (rec 1360–1399)'),
    ('d02', 2070, 2115, 1392, '2070–2114 · quieta (corte invisible 1399→1392); toque en «Un público» en el 2100 (rec 1422): «Agregar filtro» (rec 1429)'),
    ('d03', 2115, 2155, 1498, '2115–2154 · quieta (corte invisible 1436→1498); toque en «Agregar filtro» en el 2130 (rec 1513); la hoja sube a 1× (rec 1521–1525)'),
    ('d04', 2155, 2163, 1578, '2155–2162 · corte en la espera (la hoja se acomoda 6 px en la rec 1574); toque en «Red» en el 2160 (rec 1583)'),
    ('d05', 2163, 2205, 1616, '2163–2204 · corte en la espera: el editor «Red» ya puesto (rec 1616). El cambio de hoja de la rec 1590–1597 queda FUERA: en esos cuadros la hoja se va y deja ver la página con la cifra de toda la iglesia y el texto de ayuda de «Calcular» (decisión 215). Toque en «Red Timoteo» en el 2190 (rec 1643); la casilla se marca (rec 1649)'),
    ('d06', 2205, 2227, 1685, '2205–2226 · quieta (corte invisible 1658→1685); toque en «Aplicar» en el 2220 (rec 1700)'),
    ('d07', 2227, 2262, 1715, '2227–2261 · corte en la espera (la hoja se va en la rec 1707–1709 y queda fuera): el chip «Red: Red Timoteo» (rec 1715); en el 2235 (rec 1723) «Personas de la red Red Timoteo» y la cifra corre hasta «≈ 143 personas · 139 con WhatsApp» (rec 1741)'),
    ('d08', 2262, 2295, 1834, '2262–2294 · quieta (corte invisible 1749→1834); la app sube a «1 El mensaje» en un cuadro en el 2280 (rec 1852, salto real)'),
    ('d09', 2295, 2331, 1910, '2295–2330 · quieta (corte invisible 1866→1910); toque en «Plantilla aprobada» en el 2310 (rec 1925); la lista abre (rec 1926–1936)'),
    ('d10', 2331, 2343, 1986, '2331–2342 · corte en la espera (la lista se acomoda 13 px en la rec 1985); toque en «invitacion_culto · marketing» en el 2340 (rec 1995)'),
    ('d11', 2343, 2410, 2005, '2343–2409 · corte en la onda (1996–2004): la lista se va y la vista previa de WhatsApp se llena: «Hola [Primer nombre], este domingo celebramos [Qué celebramos]. Te esperamos a las 10:30 a. m. con toda tu familia.» · «Allí estaré» · «Cómo llegar» (rec 2005–2071)'),
]
# Stills: (id, desde, hasta, src, pista, comentario) — cuadros quietos de la grabación donde la app espera menos de lo que pide el pulso
ST_E1 = [
    ('se403', 994, 1020, 'assets/stills/still-e403.png', 19, '994–1019 · still de la rec 403: «hola» enviado, el chatbot todavía no contesta (la app contesta en 5 cuadros; el pulso pide 30)'),
    ('se559', 1142, 1155, 'assets/stills/still-e559.png', 19, '1142–1154 · still de la rec 559: «Horarios» tocado, los botones apagados, antes de la respuesta'),
]
ST_C = [
    ('sc2060', 2410, 2760, 'assets/stills/still-c2060.png', 17, '2410–2759 · still de la rec 2060: la vista previa quieta (la grabación sube a «Nueva campaña» en la rec 2073; aquí no hace falta: la vista previa ya está a la vista)'),
]

# ── Marcas: (cuadro, x, y del video, capa, rótulo) ──────────────────────────────────────────────────────────────────────────────────────
MARCAS = [
    (75, 584, 1496, 'camK', 'la fila de Mariana'),
    (120, 605, 456, 'camK', '«Tomar»'),
    (180, 585, 2127, 'camK', 'el compositor'),
    (240, 585, 1797, 'camK', '«/horarios»'),
    (300, 1086, 2136, 'camK', 'enviar'),
    (420, 432, 399, 'camK', '«Campañas»'),
    (600, 585, 1857, 'camK', 'la invitación'),
    (660, 311, 1944, 'camK', '«respondieron»'),
    (900, 1319, 429, 'camE1', '«Probar» (rec 107)'),
    (960, 1587, 1049, 'camE1', '«Escribe como la persona…» (rec 344)'),
    (990, 1842, 1048, 'camE1', 'enviar (rec 399)'),
    (1140, 1451, 811, 'camE1', '«Horarios» (rec 556)'),
    (1380, 1086, 456, 'camM', 'el ícono de la persona (rec 484)'),
    (1440, 377, 937, 'camM', '«Crear ficha» del panel (rec 594)'),
    (1500, 585, 1628, 'camM', '«¿Cómo llegó?» (rec 710)'),
    (1530, 585, 1391, 'camM', '«Redes sociales» (rec 781)'),
    (1545, 866, 1883, 'camM', '«Crear ficha» del diálogo (rec 858)'),
    (1800, 479, 411, 'camE2', 'la tarjeta «Bienvenida a quien llega» (rec 958)'),
    (1920, 468, 446, 'camE2', '«Envíos» (rec 1170)'),
    (2100, 827, 1032, 'camC', '«Un público» (rec 1422)'),
    (2130, 336, 1191, 'camC', '«Agregar filtro» (rec 1513)'),
    (2160, 585, 2241, 'camC', '«Red» (rec 1583)'),
    (2190, 268, 2253, 'camC', '«Red Timoteo» (rec 1643)'),
    (2220, 954, 2424, 'camC', '«Aplicar» (rec 1700)'),
    (2310, 585, 1266, 'camC', '«Plantilla aprobada» (rec 1925)'),
    (2340, 585, 2103, 'camC', '«invitacion_culto · marketing» (rec 1995)'),
]

# ── Sonidos: (cuadro del sonido = imagen + 1, archivo, acento, pista, volumen, nombre, comentario) ─────────────────────────────────────────
T_A = ('identidad/audio/toque.wav', 0.075)
T_B = ('assets/audio/toque-b.wav', 0.073)
T_C = ('assets/audio/toque-c.wav', 0.077)
AP = ('identidad/audio/aparicion.wav', 0.22)
CO = ('identidad/audio/confirmacion.wav', 0.32)
DE = ('identidad/audio/desliz.wav', 0.36)
SONIDOS = [
    # Parte 1 (los 16 del clip, sin la subida del 796 ni el sonido de marca del 851)
    (76, T_A, 0, 21, 1, 'toque', 'toque a en la fila de Mariana (75)'),
    (121, T_C, 0, 21, 1, 'toque', 'toque c en «Tomar», con el bajo (120)'),
    (123, AP, 0, 22, 1, 'aparicion', '«Atendiendo» y la nota «… tomó la conversación» (122)'),
    (181, T_B, 0, 21, 1, 'toque', 'toque b en el compositor, con el pico (180)'),
    (196, AP, 0, 22, 1, 'aparicion', 'la ceja «COMUNICACIONES» (195)'),
    (241, T_A, 0, 21, 1, 'toque', 'toque a en «/horarios» (240)'),
    (243, AP, 0, 22, 1, 'aparicion', 'el compositor se llena con el horario (242)'),
    (301, T_C, 0, 21, 1, 'toque', 'toque c en enviar (300)'),
    (303, CO, 0.1, 24, 1.4, 'confirmacion', 'la respuesta queda en el hilo (302)'),
    (376, T_B, 0, 21, 1, 'toque', 'toque b en volver (375; fuera del encuadre: se oye y no se dibuja)'),
    (421, T_A, 0, 21, 1, 'toque', 'toque a en «Campañas» (420)'),
    (481, DE, 0.2, 23, 1, 'desliz', 'la lista baja hasta la invitación (480)'),
    (601, T_B, 0, 21, 1, 'toque', 'toque b en la invitación, con la segunda subida (600)'),
    (603, CO, 0.1, 24, 1, 'confirmacion', 'el reporte con sus números (602)'),
    (661, T_C, 0, 21, 1, 'toque', 'toque c en «respondieron», con el golpe (660)'),
    (676, CO, 0.1, 24, 1.4, 'confirmacion', 'los nombres con «Leído» y «Allí estaré» (675), la prueba más fuerte de la parte 1'),
    # Parte 2 (SPEC §1.7, con los cuadros reales)
    (841, DE, 0.2, 23, 1.4, 'desliz', 'el látigo horizontal al escritorio (830–840)'),
    (901, T_A, 0, 21, 1, 'toque', 'toque a en «Probar» (900)'),
    (961, T_B, 0, 21, 1, 'toque', 'toque b en «Escribe como la persona…» (960; las teclas de «hola» no suenan)'),
    (991, T_C, 0, 21, 1, 'toque', 'toque c en enviar (990)'),
    (1021, AP, 0, 22, 1, 'aparicion', 'el chatbot contesta: el saludo y el menú (1020)'),
    (1141, T_A, 0, 21, 1, 'toque', 'toque a en «Horarios» (1140)'),
    (1156, CO, 0.1, 24, 1.4, 'confirmacion', 'el horario (1155), la primera prueba de la parte 2'),
    (1321, DE, 0.2, 23, 1, 'desliz', 'el látigo horizontal de vuelta al celular (1310–1320)'),
    (1381, T_B, 0, 21, 1, 'toque', 'toque b en el ícono de la persona (1380)'),
    (1441, T_C, 0, 21, 1, 'toque', 'toque c en «Crear ficha» del panel (1440)'),
    (1501, T_A, 0, 21, 1, 'toque', 'toque a en «¿Cómo llegó?» (1500)'),
    (1531, T_B, 0, 21, 1, 'toque', 'toque b en «Redes sociales» (1530)'),
    (1546, T_C, 0, 21, 1, 'toque', 'toque c en «Crear ficha» del diálogo (1545)'),
    (1561, CO, 0.1, 24, 1.4, 'confirmacion', 'la ficha de Mariana Ospina en el panel (1560)'),
    (1681, DE, 0.2, 23, 1, 'desliz', 'el látigo horizontal al escritorio (1670–1680)'),
    (1801, T_A, 0, 21, 1, 'toque', 'toque a en la tarjeta «Bienvenida a quien llega» (1800)'),
    (1804, AP, 0, 22, 1, 'aparicion', 'la automatización con la vista previa del mensaje (1803)'),
    (1921, T_B, 0, 21, 1, 'toque', 'toque b en «Envíos» (1920)'),
    (1924, AP, 0, 22, 1, 'aparicion', 'los cuatro envíos (1923)'),
    (2041, DE, 0.2, 23, 1, 'desliz', 'el látigo horizontal de vuelta al celular (2030–2040)'),
    (2101, T_C, 0, 21, 1, 'toque', 'toque c en «Un público» (2100)'),
    (2131, T_A, 0, 21, 1, 'toque', 'toque a en «Agregar filtro» (2130)'),
    (2161, T_B, 0, 21, 1, 'toque', 'toque b en «Red» (2160)'),
    (2191, T_C, 0, 21, 1, 'toque', 'toque c en «Red Timoteo» (2190)'),
    (2221, T_A, 0, 21, 1, 'toque', 'toque a en «Aplicar» (2220)'),
    (2236, CO, 0.1, 24, 1.4, 'confirmacion', '«Personas de la red Red Timoteo» y la cifra (2235), la tercera prueba'),
    (2281, DE, 0.2, 23, 1, 'desliz', 'la app sube al mensaje (2280; la cámara quieta)'),
    (2311, T_B, 0, 21, 1, 'toque', 'toque b en «Plantilla aprobada» (2310)'),
    (2341, T_C, 0, 21, 1, 'toque', 'toque c en «invitacion_culto · marketing» (2340)'),
    (2344, AP, 0, 22, 1, 'aparicion', 'la vista previa de WhatsApp se llena (2343)'),
]

# ── Frases: (id, líneas, lugar, host desde, host hasta, entrada, salida, comentario) ─────────────────────────────────────────────────────
# líneas: lista de líneas; cada palabra es texto o ('em', texto). entrada: 'pulsos' (frase 1), 'linea' (frase 2) o 'palabras' (cada 2 cuadros
# desde el inicio del host: el host arranca un cuadro antes del pulso y la primera palabra se ve en el pulso). salida: cuadro absoluto o None.
FRASES = [
    ('frase-1', [['Alguien', 'nuevo escribe.'], ['¿Quién', 'contesta?']], 'cel', 0, 122, 'pulsos', 117,
     'P1 · «Alguien nuevo escribe. / ¿Quién contesta?»: una landing por pulso («Alguien» 0 · «nuevo escribe.» 15 · «¿Quién» 30 · «contesta?» 45), como el clip; sale 117–121'),
    ('frase-2', [['Todo', 'tu', 'equipo,'], ['un', 'solo', 'número.']], 'cel', 119, 182, 'linea', 177,
     'P2 · «Todo tu equipo, / un solo número.»: la línea entera 120–126 (blur 8 → 0) con el toque en «Tomar»; sale 177–181'),
    ('frase-3', [['Y', 'sabes', 'quién'], ['leyó', 'el', 'aviso']], 'cel', 359, 842, 'palabras', 837,
     'P4–P6 · «Y sabes quién / leyó el aviso»: palabra a palabra 360–370; acompaña el reporte y los nombres y sale 837–841 con el látigo horizontal'),
    ('frase-4', [['Responde', 'a', 'cualquier', 'hora.']], 'esc', 842, 1321, 'palabras', 1317,
     'P8 · «Responde a cualquier hora.» (una línea, arriba del escritorio): 843 · 845 · 847 · 849; sale 1317–1321 con el látigo de vuelta'),
    ('frase-5', [['De', 'un', 'chat'], ['a', 'su', 'ficha.']], 'cel', 1321, 1681, 'palabras', 1677,
     'P9 · «De un chat / a su ficha.»: 1322 · 1324 · … · 1332; sale 1677–1681 con el látigo al escritorio'),
    ('frase-6', [['La', 'bienvenida', 'sale', 'sola.']], 'esc', 1682, 2041, 'palabras', 2037,
     'P10 · «La bienvenida sale sola.» (una línea, arriba del escritorio): 1683 · 1685 · 1687 · 1689; sale 2037–2041 con el látigo de vuelta'),
    ('frase-7', [['Cada', 'aviso,'], ['a', 'quien', 'lo', 'necesita.']], 'cel', 2041, 2520, 'palabras', 2515,
     'P11–P12 · «Cada aviso, / a quien lo necesita.»: 2042 · 2044 · … · 2052; sale 2515–2519'),
    ('frase-8', [['Habla', 'con', 'tu', 'iglesia,'], ['sin', 'perder', 'a', ('em', 'nadie')]], 'cel', 2519, 2760, 'palabras', None,
     'P13 · «Habla con tu iglesia, / sin perder a nadie» (el título de Comunicaciones en modulos.ts, sin «por WhatsApp», como en el clip): 2520 · 2522 · … · 2534; «nadie» en itálica dorada; quieta hasta el corte al cierre (2760)'),
]
CEJA_DESDE, CEJA_HASTA = 194, 2524

def videos(lista, src, pista, sangria):
    out = []
    for vid, a, b, g, c in lista:
        out.append(f'{sangria}<!-- {c} -->')
        out.append(f'{sangria}<video id="{vid}" class="clip" src="{src}" muted playsinline data-track-index="{pista}"\n'
                   f'{sangria}  data-start="{s(a)}" data-duration="{s(b - a)}" data-media-start="{ms(g)}" data-playback-rate="1"></video>')
    return '\n'.join(out)

def stills(lista, sangria):
    out = []
    for sid, a, b, src, pista, c in lista:
        out.append(f'{sangria}<!-- {c} -->')
        out.append(f'{sangria}<img id="{sid}" class="clip" src="{src}" alt="" data-track-index="{pista}" data-start="{s(a)}" data-duration="{s(b - a)}" />')
    return '\n'.join(out)

def marcas(capa, sangria):
    k = 'var(--e-k)' if capa.startswith('camE') else 'var(--f-k)'
    out = [f'{sangria}<div class="marcas">']
    for n, x, y, c, r in MARCAS:
        if c != capa: continue
        out.append(f'{sangria}  <!-- {n} · {r} (toques[] de pasos.json, px del video × el factor de la ventana) -->')
        st = f'left: calc({x}px * {k}); top: calc({y}px * {k})'
        out.append(f'{sangria}  <div class="toque" id="tq-{n}" style="{st}"></div>')
        out.append(f'{sangria}  <div class="onda" id="on-{n}" style="{st}"></div>')
    out.append(f'{sangria}</div>')
    return '\n'.join(out)

def sonidos():
    out = []
    for n, (src, dur), acento, pista, vol, nombre, c in SONIDOS:
        start = n / FPS - acento
        out.append(f'      <!-- {n} · {c} -->')
        out.append(f'      <audio id="snd-{nombre}-{n}" src="{src}" data-start="{s(start * FPS)}" data-duration="{dur}" data-track-index="{pista}" data-volume="{vol}"></audio>')
    return '\n'.join(out)

def hosts():
    out = []
    pista = 1
    for fid, lineas, lugar, a, b, entrada, salida, c in FRASES:
        out.append(f'      <!-- {c} -->')
        hold = '\n        data-beat="nadie" data-hold' if salida is None else ''  # la frase del sitio se sostiene a propósito (2520–2759)
        out.append(f'      <div id="{fid}" data-composition-id="{fid}" data-composition-src="compositions/{fid}.html" data-track-kind="graphics"{hold}\n'
                   f'        data-start="{s(a)}" data-duration="{s(b - a)}" data-track-index="{pista}" data-width="1920" data-height="1080"></div>')
        pista = 2 if pista == 1 else 1
        if fid == 'frase-1':
            out.append(f'      <!-- La ceja «COMUNICACIONES» (host {CEJA_DESDE}–{CEJA_HASTA}): entra en el 195 en la columna izquierda; cambia de lugar con cada '
                       'látigo (sale con blur y entra en el otro: arriba del escritorio 842 y 1682, a la izquierda 1322 y 2042) y se va en 2520–2523 '
                       'con la frase del sitio -->')
            out.append('      <div id="ceja" data-composition-id="ceja" data-composition-src="compositions/ceja.html" data-track-kind="graphics"\n'
                       f'        data-start="{s(CEJA_DESDE)}" data-duration="{s(CEJA_HASTA - CEJA_DESDE)}" data-track-index="3" data-width="1920" data-height="1080"></div>')
    return '\n'.join(out)

FRASE_TPL = '''<!doctype html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <!-- {comentario}. Fraunces 560, 84 px, interlínea 1,04, −0,02 em (.k-feed-frase del kit con el tamaño de 16:9); entrada-palabra: blur 6 → 0 +
         opacidad, 4 cuadros, power4.out, sin desplazarse; salida-texto: blur 0 → 8 + opacidad, 4 cuadros, power3.in. Generada por _gen/gen.py. -->
  </head>
  <body>
    <template>
      <style>
        #root {{
          position: absolute;
          inset: 0;
          width: 1920px;
          height: 1080px;
          overflow: hidden;
        }}
        .f-frase {{
          position: absolute;
          left: {left};
          top: {top};
          width: {ancho};
          font-size: var(--f-frase-px, 84px);
          color: var(--k-noche-tinta);
          text-wrap: initial;
        }}
        .linea {{
          display: block;
          white-space: nowrap;
        }}
        .palabra {{
          display: inline-block;
        }}
      </style>
      <div id="root" data-composition-id="{fid}" data-width="1920" data-height="1080" data-duration="{dur}">
        <div class="k-feed-frase f-frase" id="{pref}">
{lineas}
        </div>
      </div>
      <script>
        (function () {{
          const F = (n) => n / 30;
          const tl = gsap.timeline({{ paused: true }});
{tweens}
          tl.set({{}}, {{}}, F({fin}));
          window.__timelines['{fid}'] = tl;
        }})();
      </script>
    </template>
  </body>
</html>
'''

def frase(fid, lineas, lugar, a, b, entrada, salida, c):
    pref = 'f' + fid.split('-')[1]
    i = 0
    hl = []
    for ln in lineas:
        partes = []
        for w in ln:
            i += 1
            if isinstance(w, tuple):
                partes.append(f'<em><span class="palabra" id="{pref}-w{i}">{w[1]}</span></em>')
            else:
                partes.append(f'<span class="palabra" id="{pref}-w{i}">{w}</span>')
        hl.append('          <span class="linea">' + ' '.join(partes) + '</span>')
    n = i
    tw = []
    if entrada == 'pulsos':
        tw.append('          // «Alguien» ya está en el cuadro 0 (la miniatura). Cada landing arranca un cuadro antes de su pulso (15 · 30 · 45).')
        tw.append("          [['#f1-w2', 15], ['#f1-w3', 30], ['#f1-w4', 45]].forEach(([sel, n]) => {")
        tw.append("            tl.fromTo(sel, { opacity: 0, filter: 'blur(6px)' }, { opacity: 1, filter: 'blur(0px)', duration: F(4), ease: 'power4.out' }, F(n - 1));")
        tw.append('          });')
    elif entrada == 'linea':
        tw.append(f"          tl.fromTo('#{pref}', {{ opacity: 0, filter: 'blur(8px)' }}, {{ opacity: 1, filter: 'blur(0px)', duration: F(6), ease: 'power4.out' }}, 0);")
    else:
        tw.append(f'          for (let i = 1; i <= {n}; i++) {{')
        tw.append(f'            // El host arranca un cuadro antes del pulso ({a + 1}): la primera palabra se ve en el {a + 1}, las demás cada 2 cuadros.')
        tw.append(f"            tl.fromTo(`#{pref}-w${{i}}`, {{ opacity: 0, filter: 'blur(6px)' }}, {{ opacity: 1, filter: 'blur(0px)', duration: F(4), ease: 'power4.out' }}, F(2 * (i - 1)));")
        tw.append('          }')
    if salida is not None:
        tw.append(f"          tl.to('#{pref}', {{ opacity: 0, filter: 'blur(8px)', duration: F(4), ease: 'power3.in' }}, F({salida - a})); // {salida}–{salida + 4}")
    if lugar == 'cel':
        left, top, ancho = 'var(--f-margen-x, 120px)', 'var(--f-frase-y, 460px)', 'var(--f-frase-ancho, 936px)'
    else:
        left, top, ancho = 'var(--f-esc-x, 240px)', 'var(--f-esc-frase-y, 132px)', 'var(--f-esc-frase-ancho, 1440px)'
    return FRASE_TPL.format(comentario=c, left=left, top=top, ancho=ancho, fid=fid, dur=s(b - a), pref=pref,
                            lineas='\n'.join(hl), tweens='\n'.join(tw), fin=b - a)

CEJA = '''<!doctype html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <!-- La ceja «COMUNICACIONES» (host @@DESDE@@–@@HASTA@@), con sus dos lugares (SPEC §1.4): en la columna izquierda del celular (x 120 · y 412) y
         arriba del escritorio (x 240 · y 92). Nunca se desliza con el látigo horizontal: sale con blur y entra en el otro lugar (entrada-linea:
         blur 8 → 0, 6 cuadros, power4.out; salida-texto, 3 cuadros, power3.in). Inter 700, 28 px, mayúsculas, dorada (.k-feed-ceja con el tamaño
         de 16:9). Generada por _gen/gen.py. -->
  </head>
  <body>
    <template>
      <style>
        #root {
          position: absolute;
          inset: 0;
          width: 1920px;
          height: 1080px;
          overflow: hidden;
        }
        .f-ceja {
          position: absolute;
          font-size: var(--f-ceja-px, 28px);
          line-height: 1.2;
          white-space: nowrap;
        }
        #ceja-cel {
          left: var(--f-margen-x, 120px);
          top: var(--f-ceja-y, 412px);
        }
        #ceja-esc {
          left: var(--f-esc-x, 240px);
          top: var(--f-esc-ceja-y, 92px);
          opacity: 0;
        }
      </style>
      <div id="root" data-composition-id="ceja" data-width="1920" data-height="1080" data-duration="@@DUR@@">
        <div class="k-feed-ceja f-ceja" id="ceja-cel">Comunicaciones</div>
        <div class="k-feed-ceja f-ceja" id="ceja-esc">Comunicaciones</div>
      </div>
      <script>
        (function () {
          const F = (n) => n / 30;
          const H = @@DESDE@@; // el cuadro del video en que arranca el host
          const tl = gsap.timeline({ paused: true });
          const entra = (sel, n, primera) =>
            tl.fromTo(sel, { opacity: 0, filter: 'blur(8px)' }, { opacity: 1, filter: 'blur(0px)', duration: F(6), ease: 'power4.out', immediateRender: !!primera }, F(n - H));
          const sale = (sel, n) => tl.to(sel, { opacity: 0, filter: 'blur(8px)', duration: F(3), ease: 'power3.in' }, F(n - H));
          entra('#ceja-cel', 194, true); // en el 195 (el pulso) ya se lee
          sale('#ceja-cel', 837); // 837–840, con el látigo al escritorio
          entra('#ceja-esc', 842); // 842–848, arriba del escritorio
          sale('#ceja-esc', 1317); // 1317–1320, con el látigo de vuelta
          entra('#ceja-cel', 1322); // 1322–1328, otra vez a la izquierda
          sale('#ceja-cel', 1677); // 1677–1680, con el látigo al escritorio
          entra('#ceja-esc', 1682); // 1682–1688
          sale('#ceja-esc', 2037); // 2037–2040, con el látigo de vuelta
          entra('#ceja-cel', 2042); // 2042–2048
          sale('#ceja-cel', 2520); // 2520–2523, con la frase del sitio
          tl.set({}, {}, F(@@HASTA@@ - H));
          window.__timelines['ceja'] = tl;
        })();
      </script>
    </template>
  </body>
</html>
'''

def main():
    tpl = open(os.path.join(AQUI, 'index.tpl.html'), encoding='utf8').read()
    toques = '[' + ', '.join(str(m[0]) for m in MARCAS) + ']'
    sg = ' ' * 18
    html = (tpl.replace('@@FRASES@@', hosts())
            .replace('@@TK@@', videos(TK, K, 10, sg)).replace('@@TK_MARCAS@@', marcas('camK', sg))
            .replace('@@TM@@', videos(TM, C, 12, sg)).replace('@@TM_MARCAS@@', marcas('camM', sg))
            .replace('@@TC@@', videos(TC, C, 14, sg)).replace('@@ST_C@@', stills(ST_C, sg)).replace('@@TC_MARCAS@@', marcas('camC', sg))
            .replace('@@TE1@@', videos(TE1, E, 16, sg)).replace('@@ST_E1@@', stills(ST_E1, sg)).replace('@@TE1_MARCAS@@', marcas('camE1', sg))
            .replace('@@TE2@@', videos(TE2, E, 18, sg)).replace('@@TE2_MARCAS@@', marcas('camE2', sg))
            .replace('@@SONIDOS@@', sonidos())
            .replace('@@TOQUES@@', toques))
    assert '@@' not in html, 'quedó un marcador sin reemplazar'
    open(os.path.join(RAIZ, 'index.html'), 'w', encoding='utf8', newline='\n').write(html)
    comp = os.path.join(RAIZ, 'compositions')
    os.makedirs(comp, exist_ok=True)
    for f in FRASES:
        open(os.path.join(comp, f[0] + '.html'), 'w', encoding='utf8', newline='\n').write(frase(*f))
    ceja = CEJA.replace('@@DUR@@', s(CEJA_HASTA - CEJA_DESDE)).replace('@@DESDE@@', str(CEJA_DESDE)).replace('@@HASTA@@', str(CEJA_HASTA))
    open(os.path.join(comp, 'ceja.html'), 'w', encoding='utf8', newline='\n').write(ceja)
    print('ok: index.html, frase-1..8 y ceja ·', len(TK) + len(TE1) + len(TE2) + len(TM) + len(TC), 'tramos ·', len(MARCAS), 'marcas ·',
          len(SONIDOS), 'sonidos')

main()
