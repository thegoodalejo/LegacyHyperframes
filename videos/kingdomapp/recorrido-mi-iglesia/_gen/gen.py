# Genera index.html y compositions/frase-1..11.html + ceja.html del recorrido de Mi iglesia (16:9), desde index.tpl.html y estas tablas.
#   python _gen/gen.py            (desde recorrido-mi-iglesia/)
# Tramos de video, stills, marcas de toque, sonidos y frases -> HTML. Los cuadros son del video (30 fps); «grab.» = cuadro de la grabación
# del clip (assets/grabaciones/clip/grabacion.mp4) y «rec» = cuadro de las grabaciones nuevas (celular.mp4 y escritorio.mp4).
import os

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
FPS = 30
def s(n): return f"{n / FPS:.6f}".rstrip('0').rstrip('.')
def ms(g): return f"{g / FPS + 0.01:.6f}".rstrip('0').rstrip('.')

K = 'assets/grabaciones/clip/grabacion.mp4'   # la grabación del clip (1170×2532, 1565 cuadros)
C = 'assets/grabaciones/celular.mp4'          # la grabación nueva de celular (1170×2532, 2884 cuadros)
E = 'assets/grabaciones/escritorio.mp4'       # la grabación nueva de escritorio (1920×1080, 1682 cuadros)

# ── Parte 1 (0–840): las tablas del clip (clip-sitio-mi-iglesia/_gen/gen.py), sin cambios salvo el último tramo, que llega al 841 ─────────
# (id, desde, hasta, grab, comentario, dentro_del_iris)
K_TRAMOS = [
    ('k01', 0, 60, 0, 'Mi iglesia arriba (grab. 0–59): la barra «Kingdom Demo», «Buenas tardes, Gabriela», «Mis servicios», «Mis Equipos»', 0),
    ('k02', 60, 105, 96, 'la app baja a la novedad en un cuadro (grab. 96, salto real del `ver`): «Inscripciones abiertas · hace 3 minutos» con la tarjeta del congreso', 0),
    ('k03', 105, 107, 180, 'toque en la flecha de las reacciones (grab. 180)', 0),
    ('k04', 107, 120, 186, 'corte en la espera (182→186, quieta): el selector ya abierto en el 107 (grab. 186)', 0),
    ('k05', 120, 122, 245, 'toque en «Amén» (grab. 245)', 0),
    ('k06', 122, 180, 251, 'corte en la espera (247→251, quieta): «🙌 Amén» puesto y 57 en el 122; el 🙌 salta 125–134 (grab. 254–263)', 0),
    ('k07', 181, 200, 437, 'el evento ya cargado (grab. 437; la K del cargador 371–430 queda fuera) con la entrada propia de la app 181–187', 1),
    ('k08', 200, 300, 447, 'quieto (grab. 447–546; el corte del 200 cae en la pantalla quieta, 445+)', 1),
    ('k09', 300, 301, 547, 'la app baja a «Inscripción» en un cuadro (grab. 547, salto real de 62 px CSS)', 1),
    ('k10', 301, 375, 557, 'quieta (grab. 557–630; 548–556 iguales)', 1),
    ('k11', 375, 377, 631, 'toque en «Inscribirme» (grab. 631–632)', 1),
    ('k12', 377, 389, 638, 'corte en la onda (633→638): «¿A quiénes inscribes? (hasta 4)» y «Yo» entran 377–386 (grab. 638–649)', 1),
    ('k13', 420, 450, 710, 'toque en la casilla del esposo: se marca 420–422 (grab. 710–739)', 1),
    ('k14', 450, 452, 754, 'toque en «Seguir» (grab. 754–755)', 1),
    ('k15', 452, 464, 761, 'corte en la onda (756→761): «1 de 2: Tú» entra 452–461 (grab. 761–772)', 1),
    ('k16', 464, 480, 854, 'la app centró el formulario (grab. 814, salto de 136 px CSS): la cámara lo compensa en el 464, no se ve (grab. 854–869)', 1),
    ('k17', 480, 481, 870, 'toque en «M» (grab. 870)', 1),
    ('k18', 481, 495, 872, 'el radio se llena desde el 481 (grab. 872–885; 871 igual)', 1),
    ('k19', 495, 496, 902, 'toque en «Sí» (grab. 902)', 1),
    ('k20', 496, 510, 904, 'el radio se llena desde el 496 (grab. 904–917; 903 igual)', 1),
    ('k21', 510, 512, 945, 'toque en «Seguir» (grab. 945–946)', 1),
    ('k22', 512, 540, 952, 'corte en la onda (947→952): «2 de 2: Simón Ríos Arango» con los radios vacíos en el 512 (grab. 952–979)', 1),
    ('k23', 540, 541, 999, 'toque en «L» (grab. 999)', 1),
    ('k24', 541, 555, 1002, 'el radio se llena desde el 541 (grab. 1002–1015; 1000–1001 iguales)', 1),
    ('k25', 555, 556, 1032, 'toque en «No» (grab. 1032)', 1),
    ('k26', 556, 600, 1034, 'el radio se llena desde el 556 (grab. 1034–1077; 1033 igual)', 1),
    ('k27', 600, 602, 1090, 'toque en «Inscribir» (grab. 1090–1091)', 1),
    ('k28', 602, 645, 1111, 'corte en la espera y la K del cargador (1092→1111): el sello, el confeti real y «¡Quedaste inscrito!» con las dos filas «Inscrito» (grab. 1111–1153)', 1),
    ('k29', 660, 662, 1259, 'toque en «Ver boleta» (grab. 1259–1260)', 1),
    ('k30', 662, 720, 1281, 'corte en la espera (1261→1281, la carga de «Mis boletas» queda fuera): la boleta con su QR y «Código FM75UZ»; entra 1,03 → 1,00', 1),
    ('k31', 720, 722, 1398, 'toque en el QR (grab. 1398–1399)', 1),
    ('k32', 722, 841, 1405, 'corte en la espera (1400→1405, quieta): la boleta a pantalla completa entra con su animación 722–728 (grab. 1405–1523); '
     'en el 840 (grab. 1523) el toque en «Cerrar»', 1),
]
K_STILLS = [  # (desde, hasta, grab, comentario, dentro_del_iris)
    (389, 420, 705, 'la app bajó 200 px CSS (grab. 701–704, el `scrollIntoView` antes de marcar): still de la grab. 705, compensado por la cámara en el 389; la cámara baja a la lista 390–403', 1),
    (645, 660, 1258, 'la app bajó 84 px CSS (grab. 1257, el `scrollIntoView` antes de «Ver boleta»): still de la grab. 1258, compensado por la cámara en el 645; la cámara baja a «Ver boleta» 646–658', 1),
]

# ── Parte 2, celular (celular.mp4): (id, desde, hasta, rec, comentario) ──────────────────────────────────────────────────────────────────
C1A = [  # camC1: Gabriela, de «Mis boletas» a la tarjeta de Jóvenes (hasta el iris del 960)
    ('c01', 841, 870, 153, '841–869 · corte sobre el toque en «Cerrar» (840): «Mis boletas» con «Código FM75UZ» y la barra de abajo (rec 153–181; la boleta en grande de la rec 64–152 la pone el clip)'),
    ('c02', 870, 873, 234, '870–872 · toque en «Comunidades» de la barra (rec 234–236)'),
    ('c03', 873, 900, 249, '873–899 · corte en la espera (237→249; la carga, el esqueleto y la página que todavía se pinta, 243–248, quedan fuera): «Todavía no estás en una comunidad» termina de entrar con la app 873–875 (rec 249–275)'),
    ('c04', 900, 903, 332, '900–902 · toque en «Explorar comunidades» (rec 332–334)'),
    ('c05', 903, 930, 344, '903–929 · corte en la espera (335→344; el esqueleto 339–343 fuera): «Explorar» con Matrimonios «Para ti» primero, las tarjetas entran 903–911 (rec 344–370)'),
    ('c06', 930, 961, 456, '930–960 · la app baja a Jóvenes en un cuadro (el `ver` saltó en la rec 412; quieta 412–486): la tarjeta de Jóvenes con «Unirme» (rec 456–486); toque en la portada en el 960 (rec 486)'),
]
C1B = [  # camC1b: dentro del iris del 960
    ('c07', 961, 1020, 505, '961–1019 · la comunidad ya pintada (rec 505–563; la página en blanco y el esqueleto 495–504 quedan fuera); su entrada termina en el 975 (rec 519)'),
    ('c08', 1020, 1082, 618, '1020–1081 · quieta (rec 618–679); toque en «Unirme» en el 1080 (rec 680–681)'),
    ('c09', 1082, 1137, 691, '1082–1136 · corte en la espera (682→691; el botón gris 687–690 fuera): sin «Unirme», «Miembros: 23» y el confeti de la app (rec 691–745)'),
    ('c10', 1137, 1143, 813, '1137–1142 · quieta (rec 813–818); toque en «Conectar con un líder» en el 1140 (rec 816)'),
    ('c11', 1143, 1158, 830, '1143–1157 · corte en la espera (819→830): el diálogo «Conectar con un líder» ya puesto, con el foco en el mensaje (rec 830–844)'),
    ('c12', 1158, 1258, 872, '1158–1257 · corte en el foco quieto (845→872): «Voy al congreso y quiero conocerlos.» se escribe a 1× desde el 1171 (rec 885) hasta el 1251 (rec 965), con su contador «36 / 500» (rec 872–971)'),
    ('c13', 1258, 1263, 1009, '1258–1262 · corte en el texto quieto (972→1009); toque en «Enviar» en el 1260 (rec 1011–1013)'),
    ('c14', 1263, 1320, 1029, '1263–1319 · corte en la espera (1014→1029; el diálogo que se va, la tarjeta que cambia y el fundido de entrada, 1019–1028, quedan fuera): «Pediste conectar con un líder · Un líder te escribirá pronto.» con el confeti de la tarjeta detrás (rec 1029–1085); el látigo se lo lleva en 1310–1320'),
]
C2 = [  # camC2: Gabriela acompañada y su objetivo
    ('c15', 1550, 1683, 1544, '1550–1682 · Jóvenes con «Andrés Felipe Restrepo Gómez te acompañará · Te escribirá pronto para conocerte.» (rec 1544–1676; la toma fuera de cámara 1177–1477 y la entrada 1478–1500 quedan fuera); toque en «Objetivos» en el 1680 (rec 1674)'),
    ('c16', 1683, 1740, 1691, '1683–1739 · corte en la espera (1677→1691; la página en blanco y el esqueleto 1682–1690 fuera): «Mis objetivos» termina de entrar 1683–1692 con «Un devocional cada mañana · Paso 13 de 14 · 86 %» (rec 1691–1747)'),
    ('c17', 1740, 1743, 1797, '1740–1742 · toque en la tarjeta del devocional (rec 1797–1799)'),
    ('c18', 1743, 1800, 1808, '1743–1799 · corte en la espera (1800→1808; el esqueleto 1805–1807 fuera): el objetivo con «Hoy · Servir · Marcos 10:45…» y «Lo hice» (rec 1808–1864)'),
    ('c19', 1800, 1803, 1913, '1800–1802 · toque en «Lo hice» (rec 1913–1915)'),
    ('c20', 1803, 1920, 1924, '1803–1919 · corte en la espera (1916→1924; el aviso «Lo que marcaste espera señal para enviarse.» de la API local, rec 1921–1923, queda fuera): '
     '«¡Listo! Marcamos «Servir» como hecho.» entra 1804–1808 y en el 1811 (rec 1932) el anillo pasa a «Paso 14 de 14 · 93 %» con «Mañana · Esperanza» (rec 1924–2040)'),
    ('c21', 1920, 2040, 2085, '1920–2039 · la app baja a «Todos los pasos» en un cuadro (rec 2085, salto real del `ver`): Perdón, La palabra, Gozo, Servir «Hoy» y Esperanza «Mañana» (rec 2085–2204)'),
]
C3 = [  # camC3: Lucía, la bienvenida
    ('c22', 2280, 2370, 2278, '2280–2369 · la portada de la bienvenida de Lucía desde su primer cuadro pintado: el logo con su resorte, «Hola, Lucía», el título, el texto y el botón (rec 2278–2367; el cambio de cuenta 2238–2272 y la K del cargador 2273–2276 quedan fuera)'),
    ('c23', 2370, 2403, 2444, '2370–2402 · quieta (rec 2444–2476; la portada flota igual); toque en «Empezar mis primeros pasos» en el 2400 (rec 2474)'),
    ('c24', 2403, 2760, 2483, '2403–2759 · corte en la espera (2477→2483): la portada se va y «Tus primeros pasos» entra con su animación 2404–2427 (rec 2483–2839)'),
]
# ── Parte 2, escritorio (escritorio.mp4) ────────────────────────────────────────────────────────────────────────────────────────────────
E1 = [  # camE1: el pastor en Contactos
    ('e01', 1310, 1383, 91, '1310–1382 · «Contactos» con la fila de Gabriela, la última de los pendientes, «hace 1 min» y su mensaje (rec 91–163; quieta desde la rec 33); toque en «Tomar» en el 1380 (rec 161)'),
    ('e02', 1383, 1560, 324, '1383–1559 · corte en la espera (164→324; la K del cargador 169–323 queda fuera): el detalle «Gabriela Hinestroza Perea · Tomado · hace 1 min · Lo tomó Andrés Felipe Restrepo Gómez», su mensaje, «Llamar», «Escribir por WhatsApp», con el confeti de la fila detrás (rec 324–500)'),
]
E2 = [  # camE2: el tablero y quién reaccionó
    ('e03', 2030, 2100, 1010, '2030–2099 · el tablero del Portal con sus cifras ya puestas (rec 1010–1079; la carga 666–1005 queda fuera)'),
    ('e04', 2100, 2130, 1249, '2100–2129 · la app baja a «Las 21 más recientes» en un cuadro (rec 1248, salto real; el salto intermedio de la rec 1143 queda fuera): «Inscripciones abiertas · Toda la iglesia», «1.324» (rec 1249–1278)'),
    ('e05', 2130, 2163, 1275, '2130–2162 · quieta (rec 1275–1307); toque en «Inscripciones abiertas» en el 2160 (rec 1305)'),
    ('e06', 2163, 2190, 1456, '2163–2189 · corte en la espera (1308→1456; la carga de la novedad y su `ver`, 1309–1455, quedan fuera): «Quién reaccionó · Todas · 57» y 🙌 5 (rec 1456–1482)'),
    ('e07', 2190, 2223, 1535, '2190–2222 · quieta (rec 1535–1567); toque en 🙌 en el 2220 (rec 1565; el botón se marca en la 1567)'),
    ('e08', 2223, 2280, 1574, '2223–2279 · corte en la espera (1568→1574; la K del cargador 1571–1573 queda fuera): la lista de 🙌 con «Gabriela Hinestroza Perea» primera e «Isaac Gómez Sepúlveda» (rec 1574–1630)'),
]

# ── Marcas: (cuadro, x, y del video, capa, rótulo) — toques[] de cada pasos.json ─────────────────────────────────────────────────────────
K_MARCAS = [  # las del clip (y la del 840, sobre «Cerrar»: la boleta en grande del clip y la de celular.mp4 son la misma pantalla)
    (105, 543, 1744, 'la flecha de las reacciones'), (120, 792, 1559, '«Amén»'),
    (375, 585, 2112, '«Inscribirme»'), (420, 357, 1980, 'la casilla del esposo'), (450, 936, 2136, '«Seguir»'),
    (480, 181, 1380, '«M»'), (495, 181, 1860, '«Sí»'), (510, 936, 2136, '«Seguir»'), (540, 174, 1500, '«L»'), (555, 191, 1980, '«No»'),
    (600, 919, 2136, '«Inscribir»'), (660, 477, 2112, '«Ver boleta»'), (720, 585, 1251, 'el QR'),
    (840, 585, 2003, '«Cerrar» (celular.mp4 rec 146: x 585, y 2003; el mismo botón de la grab. 1522)'),
]
MARCAS = [
    (870, 441, 2418, 'camC1', '«Comunidades» en la barra (rec 234)'),
    (900, 585, 1497, 'camC1', '«Explorar comunidades» (rec 332)'),
    (960, 585, 990, 'camC1', 'la portada de Jóvenes (rec 486)'),
    (1080, 221, 1483, 'camC1b', '«Unirme» (rec 680)'),
    (1140, 585, 1546, 'camC1b', '«Conectar con un líder» (rec 816)'),
    (1260, 916, 1687, 'camC1b', '«Enviar» (rec 1011)'),
    (1380, 1569, 944, 'camE1', '«Tomar» de Gabriela (escritorio, rec 161)'),
    (1680, 1017, 2418, 'camC2', '«Objetivos» en la barra (rec 1674)'),
    (1740, 585, 753, 'camC2', 'la tarjeta «Un devocional cada mañana» (rec 1797)'),
    (1800, 269, 1377, 'camC2', '«Lo hice» (rec 1913)'),
    (2160, 350, 540, 'camE2', '«Inscripciones abiertas» (escritorio, rec 1305)'),
    (2220, 803, 876, 'camE2', '🙌 (escritorio, rec 1565)'),
    (2400, 585, 1740, 'camC3', '«Empezar mis primeros pasos» (rec 2474)'),
]

# ── Sonidos: (cuadro del sonido = imagen + 1, archivo, acento, pista, volumen, nombre, comentario) ─────────────────────────────────────────
T_A = ('identidad/audio/toque.wav', 0.075)
T_B = ('assets/audio/toque-b.wav', 0.073)
T_C = ('assets/audio/toque-c.wav', 0.077)
AP = ('identidad/audio/aparicion.wav', 0.22)
CO = ('identidad/audio/confirmacion.wav', 0.32)
DE = ('identidad/audio/desliz.wav', 0.36)
SONIDOS = [
    # Parte 1: los 22 del clip (clip-sitio-mi-iglesia/_gen/gen.py → SON), sin la subida, las campanas ni el fundido de su firma
    (61, DE, 0.2, 23, 1, 'desliz', 'la app baja a la novedad (60)'),
    (106, T_A, 0, 21, 1, 'toque', 'toque a en la flecha de las reacciones (105)'),
    (108, AP, 0, 22, 1, 'aparicion', 'el selector abierto (107)'),
    (121, T_C, 0, 21, 1, 'toque', 'toque c en «Amén», con el bajo (120)'),
    (123, AP, 0, 22, 1.4, 'aparicion', '«🙌 Amén» puesto y el total en 57 (122)'),
    (181, T_B, 0, 21, 1, 'toque', 'toque b en «Inscribirme», con el iris (180)'),
    (196, AP, 0, 22, 1, 'aparicion', 'la ceja «MI IGLESIA» (195)'),
    (301, DE, 0.2, 23, 1, 'desliz', 'la app baja a «Inscripción» (300)'),
    (376, T_A, 0, 21, 1, 'toque', 'toque a en «Inscribirme» (375)'),
    (421, T_B, 0, 21, 1, 'toque', 'toque b en la casilla del esposo (420)'),
    (451, T_C, 0, 21, 1, 'toque', 'toque c en «Seguir» (450)'),
    (481, T_A, 0, 21, 1, 'toque', 'toque a en «M» (480)'),
    (496, T_B, 0, 21, 1, 'toque', 'toque b en «Sí» (495)'),
    (511, T_C, 0, 21, 1, 'toque', 'toque c en «Seguir» (510)'),
    (541, T_A, 0, 21, 1, 'toque', 'toque a en «L» (540)'),
    (556, T_B, 0, 21, 1, 'toque', 'toque b en «No» (555)'),
    (601, T_C, 0, 21, 1, 'toque', 'toque c en «Inscribir», con la segunda subida (600)'),
    (603, CO, 0.1, 24, 1.4, 'confirmacion', 'el sello y «¡Quedaste inscrito!» (602)'),
    (661, T_A, 0, 21, 1, 'toque', 'toque a en «Ver boleta», con el golpe (660)'),
    (663, CO, 0.1, 24, 1, 'confirmacion', '«Mis boletas» con el QR (662)'),
    (721, T_B, 0, 21, 1, 'toque', 'toque b en el QR (720)'),
    (723, AP, 0, 22, 1, 'aparicion', 'la boleta a pantalla completa (722)'),
    # Parte 2 (SPEC §1.7, con los cuadros que dio la grabación: cada resultado entra en el corte de su espera, 1–3 cuadros después del toque)
    (841, T_A, 0, 21, 1, 'toque', 'toque a en «Cerrar», el golpe más fuerte (840)'),
    (871, T_B, 0, 21, 1, 'toque', 'toque b en «Comunidades» (870)'),
    (901, T_C, 0, 21, 1, 'toque', 'toque c en «Explorar comunidades» (900)'),
    (931, DE, 0.2, 23, 1, 'desliz', 'la app baja hasta Jóvenes (930)'),
    (961, T_A, 0, 21, 1, 'toque', 'toque a en la tarjeta de Jóvenes, con el iris y la costura de la música (960)'),
    (1081, T_B, 0, 21, 1, 'toque', 'toque b en «Unirme» (1080)'),
    (1083, AP, 0, 22, 1, 'aparicion', 'el confeti de la app y «Miembros: 23» (1082)'),
    (1141, T_C, 0, 21, 1, 'toque', 'toque c en «Conectar con un líder» (1140)'),
    (1144, AP, 0, 22, 1, 'aparicion', 'el diálogo (1143)'),
    (1261, T_A, 0, 21, 1, 'toque', 'toque a en «Enviar» (1260)'),
    (1264, CO, 0.1, 24, 1, 'confirmacion', '«Pediste conectar con un líder» (1263)'),
    (1321, DE, 0.2, 23, 1.4, 'desliz', 'el látigo horizontal al escritorio (1310–1320)'),
    (1381, T_B, 0, 21, 1, 'toque', 'toque b en «Tomar» (1380)'),
    (1384, AP, 0, 22, 1, 'aparicion', 'el detalle y el confeti de la fila (1383)'),
    (1561, DE, 0.2, 23, 1, 'desliz', 'el látigo horizontal de vuelta al celular (1550–1560)'),
    (1576, CO, 0.1, 24, 1.4, 'confirmacion', 'el punch sobre «Andrés Felipe Restrepo Gómez te acompañará» (1575)'),
    (1681, T_C, 0, 21, 1, 'toque', 'toque c en «Objetivos» (1680)'),
    (1741, T_A, 0, 21, 1, 'toque', 'toque a en la tarjeta del devocional (1740)'),
    (1801, T_B, 0, 21, 1, 'toque', 'toque b en «Lo hice», el primer golpe del clímax (1800)'),
    (1804, AP, 0, 22, 1, 'aparicion', '«¡Listo! Marcamos «Servir» como hecho.» (1803)'),
    (1921, DE, 0.2, 23, 1, 'desliz', 'la app baja a «Todos los pasos» (1920)'),
    (2041, DE, 0.2, 23, 1, 'desliz', 'el látigo horizontal al escritorio (2030–2040)'),
    (2101, DE, 0.2, 23, 1, 'desliz', 'la app baja a «Las 21 más recientes» (2100)'),
    (2161, T_C, 0, 21, 1, 'toque', 'toque c en «Inscripciones abiertas» (2160)'),
    (2164, AP, 0, 22, 1, 'aparicion', '«Quién reaccionó» (2163)'),
    (2221, T_A, 0, 21, 1, 'toque', 'toque a en 🙌 (2220)'),
    (2224, CO, 0.1, 24, 1.4, 'confirmacion', '«Gabriela Hinestroza Perea 🙌», la primera de la lista (2223)'),
    (2281, DE, 0.2, 23, 1, 'desliz', 'el látigo horizontal de vuelta: la bienvenida de Lucía (2270–2280)'),
    (2401, T_B, 0, 21, 1, 'toque', 'toque b en «Empezar mis primeros pasos» (2400)'),
    (2404, AP, 0, 22, 1, 'aparicion', 'el camino de sus primeros pasos (2403)'),
]

# ── Frases: (id, líneas, lugar, host desde, host hasta, entrada, salida, comentario) ─────────────────────────────────────────────────────
# líneas: lista de líneas; cada palabra es texto o ('em', texto). entrada: 'pulsos' (frase 1), 'linea' (frase 2) o 'palabras' (cada 2 cuadros
# desde el inicio del host: el host arranca un cuadro antes del pulso y la primera palabra se ve en el pulso). salida: cuadro absoluto o None.
FRASES = [
    ('frase-1', [['¿Se', 'enteró'], ['toda la', 'iglesia?']], 'cel', 0, 122, 'pulsos', 117,
     'P1 · «¿Se enteró / toda la iglesia?»: una landing por pulso (0 · 15 · 30 · 45); sale 117–121'),
    ('frase-2', [['Llega', 'a', 'cada', 'celular.']], 'cel', 119, 182, 'linea', 177,
     'P2 · «Llega a cada celular.»: la línea entera 120–126 (blur 8 → 0); sale 177–181, antes del iris del 180'),
    ('frase-3', [['Y', 'se', 'inscribe'], ['con', 'su', 'familia']], 'cel', 359, 602, 'palabras', 597,
     'P4 · «Y se inscribe / con su familia»: palabra a palabra 360–370; sale 597–601'),
    ('frase-4', [['Su', 'boleta,'], ['también', 'sin', 'señal.']], 'cel', 719, 842, 'palabras', 837,
     'P8 · «Su boleta, / también sin señal.»: 720 · 722 · 724 · 726 · 728 sobre la boleta en grande; sale 837–841, con el toque en «Cerrar»'),
    ('frase-5', [['Encuentra'], ['su', 'comunidad.']], 'cel', 841, 1321, 'palabras', 1317,
     'P9 · «Encuentra / su comunidad.»: 842 · 844 · 846; sale 1317–1321 con el látigo al escritorio'),
    ('frase-6', [['Su', 'mensaje', 'llega', 'a', 'los', 'líderes.']], 'esc', 1322, 1561, 'palabras', 1557,
     'P10 · «Su mensaje llega a los líderes.» (una línea, arriba del escritorio): 1323 · 1325 · … · 1333; sale 1557–1561 con el látigo de vuelta'),
    ('frase-7', [['Y', 'un', 'líder'], ['la', 'acompaña.']], 'cel', 1561, 1682, 'palabras', 1677,
     'P11 · «Y un líder / la acompaña.»: 1562 · 1564 · 1566 · 1568 · 1570; sale 1677–1681'),
    ('frase-8', [['Crece'], ['paso', 'a', 'paso.']], 'cel', 1681, 2042, 'palabras', 2037,
     'P12 · «Crece / paso a paso.»: 1682 · 1684 · 1686 · 1688; sale 2037–2041 con el látigo al escritorio'),
    ('frase-9', [['Y', 'sabes', 'quién', 'respondió.']], 'esc', 2042, 2282, 'palabras', 2277,
     'P13 · «Y sabes quién respondió.» (una línea, arriba del escritorio): 2043 · 2045 · 2047 · 2049; sale 2277–2281 con el látigo de vuelta'),
    ('frase-10', [['A', 'quien', 'llega,'], ['una', 'bienvenida.']], 'cel', 2281, 2520, 'palabras', 2515,
     'P14 · «A quien llega, / una bienvenida.»: 2282 · 2284 · 2286 · 2288 · 2290; sale 2515–2519'),
    ('frase-11', [['Tu', 'iglesia,', 'en', 'el', ('em', 'bolsillo')], ['de', 'cada', 'miembro']], 'cel', 2518, 2760, 'palabras', None,
     'P14 · la frase del sitio, «Tu iglesia, en el bolsillo / de cada miembro»: 2519 · 2521 · … · 2533; «bolsillo» en itálica dorada; quieta hasta el corte al cierre (2760)'),
]
CEJA_H = 194  # el host de la ceja arranca aquí y termina en el 2524

def videos(lista, src, pista, sangria):
    out = []
    for vid, a, b, g, c in lista:
        out.append(f'{sangria}<!-- {c} -->')
        out.append(f'{sangria}<video id="{vid}" class="clip" src="{src}" muted playsinline data-track-index="{pista}"\n'
                   f'{sangria}  data-start="{s(a)}" data-duration="{s(b - a)}" data-media-start="{ms(g)}" data-playback-rate="1"></video>')
    return '\n'.join(out)

def k_tramos(dentro, sangria):
    items = [('v', t) for t in K_TRAMOS] + [('s', t) for t in K_STILLS]
    items.sort(key=lambda x: x[1][1] if x[0] == 'v' else x[1][0])
    out = []
    for k, t in items:
        if k == 'v':
            vid, a, b, g, c, d = t
            if d != dentro: continue
            out.append(f'{sangria}<!-- {a}–{b - 1} · {c} -->')
            out.append(f'{sangria}<video id="{vid}" class="clip" src="{K}" muted playsinline data-track-index="10"\n'
                       f'{sangria}  data-start="{s(a)}" data-duration="{s(b - a)}" data-media-start="{ms(g)}" data-playback-rate="1"></video>')
        else:
            a, b, g, c, d = t
            if d != dentro: continue
            out.append(f'{sangria}<!-- {a}–{b - 1} · {c} -->')
            out.append(f'{sangria}<img id="still{g}" class="clip" src="assets/stills/still-{g}.png" alt="" data-track-index="11"\n'
                       f'{sangria}  data-start="{s(a)}" data-duration="{s(b - a)}" />')
    return '\n'.join(out)

def marca(n, x, y, r, k, sangria):
    st = f'left: calc({x}px * {k}); top: calc({y}px * {k})'
    return (f'{sangria}<!-- {n} · {r} -->\n'
            f'{sangria}<div class="toque" id="tq-{n}" style="{st}"></div>\n'
            f'{sangria}<div class="onda" id="on-{n}" style="{st}"></div>')

def k_marcas(sangria):
    return '\n'.join(marca(n, x, y, r, 'var(--f-k)', sangria) for n, x, y, r in K_MARCAS)

def marcas(capa, sangria):
    k = 'var(--e-k)' if capa.startswith('camE') else 'var(--f-k)'
    out = [f'{sangria}<div class="marcas">']
    for n, x, y, c, r in MARCAS:
        if c != capa: continue
        out.append(marca(n, x, y, r + ' — toques[] de pasos.json, px del video × el factor de la ventana', k, sangria + '  '))
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
        out.append(f'      <div id="{fid}" data-composition-id="{fid}" data-composition-src="compositions/{fid}.html" data-track-kind="graphics"\n'
                   f'        data-start="{s(a)}" data-duration="{s(b - a)}" data-track-index="{pista}" data-width="1920" data-height="1080"></div>')
        pista = 2 if pista == 1 else 1
        if fid == 'frase-1':
            out.append('      <!-- La ceja «MI IGLESIA» (host 194–2524): entra en el 195 en la columna izquierda y cambia de lugar con cada látigo (sale con blur en su '
                       'escenario y entra en el otro): arriba del escritorio 1322–2041 y 2042–2281 · a la izquierda 1562–2041 y 2282–2519; se va en 2520–2523 -->')
            out.append('      <div id="ceja" data-composition-id="ceja" data-composition-src="compositions/ceja.html" data-track-kind="graphics"\n'
                       f'        data-start="{s(CEJA_H)}" data-duration="{s(2524 - CEJA_H)}" data-track-index="3" data-width="1920" data-height="1080"></div>')
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
        tw.append('          // «¿Se» ya está en el cuadro 0 (la miniatura). Cada landing arranca un cuadro antes de su pulso (15 · 30 · 45).')
        tw.append("          [['#f1-w2', 15], ['#f1-w3', 30], ['#f1-w4', 45]].forEach(([sel, n]) => {")
        tw.append("            tl.fromTo(sel, { opacity: 0, filter: 'blur(6px)' }, { opacity: 1, filter: 'blur(0px)', duration: F(4), ease: 'power4.out' }, F(n - 1));")
        tw.append('          });')
    elif entrada == 'linea':
        tw.append(f"          tl.fromTo('#{pref}', {{ opacity: 0, filter: 'blur(8px)' }}, {{ opacity: 1, filter: 'blur(0px)', duration: F(6), ease: 'power4.out' }}, 0);")
    else:
        tw.append(f'          for (let i = 1; i <= {n}; i++) {{')
        tw.append(f'            // El host arranca un cuadro antes del pulso ({a}): la primera palabra se ve en el {a + 1}, las demás cada 2 cuadros.')
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
    <!-- La ceja «MI IGLESIA» (host 194–2524), con sus dos lugares (SPEC §1.4): en la columna izquierda del celular (x 120 · y 412) y arriba del
         escritorio (x 240 · y 92). Nunca se desliza con los látigos: sale con blur y entra en el otro lugar (entrada-linea: blur 8 → 0, 6 cuadros,
         power4.out; salida-texto, 3 cuadros, power3.in). Inter 700, 28 px, mayúsculas, dorada (.k-feed-ceja con el tamaño de 16:9).
         Generada por _gen/gen.py. -->
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
        <div class="k-feed-ceja f-ceja" id="ceja-cel">Mi iglesia</div>
        <div class="k-feed-ceja f-ceja" id="ceja-esc">Mi iglesia</div>
      </div>
      <script>
        (function () {
          const F = (n) => n / 30;
          const H = 194; // el cuadro del video en que arranca el host
          const tl = gsap.timeline({ paused: true });
          const entra = (sel, n, primera) =>
            tl.fromTo(sel, { opacity: 0, filter: 'blur(8px)' }, { opacity: 1, filter: 'blur(0px)', duration: F(6), ease: 'power4.out', immediateRender: !!primera }, F(n - H));
          const sale = (sel, n) => tl.to(sel, { opacity: 0, filter: 'blur(8px)', duration: F(3), ease: 'power3.in' }, F(n - H));
          entra('#ceja-cel', 194, true); // en el 195 (el pulso) ya se lee
          sale('#ceja-cel', 1317); // 1317–1320, con el látigo al escritorio
          entra('#ceja-esc', 1322); // 1322–1328, arriba del escritorio
          sale('#ceja-esc', 1557); // 1557–1560, con el látigo de vuelta
          entra('#ceja-cel', 1562); // 1562–1568, otra vez a la izquierda
          sale('#ceja-cel', 2037); // 2037–2040, con el segundo látigo al escritorio
          entra('#ceja-esc', 2042); // 2042–2048
          sale('#ceja-esc', 2277); // 2277–2280, con el último látigo
          entra('#ceja-cel', 2282); // 2282–2288
          sale('#ceja-cel', 2520); // 2520–2523, con la frase del sitio
          tl.set({}, {}, F(2524 - H));
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
    ktoques = '[' + ', '.join(str(m[0]) for m in K_MARCAS) + ']'
    p16, p18, p20 = ' ' * 16, ' ' * 18, ' ' * 20
    html = (tpl.replace('@@FRASES@@', hosts())
            .replace('@@KFUERA@@', k_tramos(0, p18)).replace('@@KDENTRO@@', k_tramos(1, p20)).replace('@@KMARCAS@@', k_marcas(p20))
            .replace('@@C1A@@', videos(C1A, C, 12, p16)).replace('@@C1A_MARCAS@@', marcas('camC1', p16))
            .replace('@@C1B@@', videos(C1B, C, 14, p18)).replace('@@C1B_MARCAS@@', marcas('camC1b', p18))
            .replace('@@C2@@', videos(C2, C, 15, p16)).replace('@@C2_MARCAS@@', marcas('camC2', p16))
            .replace('@@C3@@', videos(C3, C, 16, p16)).replace('@@C3_MARCAS@@', marcas('camC3', p16))
            .replace('@@E1@@', videos(E1, E, 18, p16)).replace('@@E1_MARCAS@@', marcas('camE1', p16))
            .replace('@@E2@@', videos(E2, E, 19, p16)).replace('@@E2_MARCAS@@', marcas('camE2', p16))
            .replace('@@SONIDOS@@', sonidos())
            .replace('@@TOQUES@@', toques).replace('@@KTOQUES@@', ktoques))
    assert '@@' not in html, 'quedó un marcador sin reemplazar'
    open(os.path.join(RAIZ, 'index.html'), 'w', encoding='utf8', newline='\n').write(html)
    comp = os.path.join(RAIZ, 'compositions')
    os.makedirs(comp, exist_ok=True)
    for f in FRASES:
        open(os.path.join(comp, f[0] + '.html'), 'w', encoding='utf8', newline='\n').write(frase(*f))
    open(os.path.join(comp, 'ceja.html'), 'w', encoding='utf8', newline='\n').write(CEJA.replace('@@DUR@@', s(2524 - CEJA_H)))
    print('ok: index.html, frase-1..11 y ceja ·', len(K_TRAMOS) + len(C1A) + len(C1B) + len(C2) + len(C3) + len(E1) + len(E2), 'tramos ·',
          len(K_MARCAS) + 1 + len(MARCAS), 'marcas ·', len(SONIDOS), 'sonidos de acción')

main()
