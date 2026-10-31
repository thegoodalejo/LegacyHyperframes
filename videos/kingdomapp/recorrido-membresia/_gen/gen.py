# Genera el recorrido de Membresía (16:9) desde index.tpl.html: index.html, compositions/fondo.html, frase-1..9.html y ceja-1..5.html.
# Fuente de verdad de los tramos de video, las marcas de toque, los sonidos y los textos. Uso (desde la raíz del proyecto):
#   python _gen/gen.py
# Medidas de las grabaciones: REVIEW.md §3 (cuadros de cada cambio, desplazamientos y cajas).
import os

RAIZ = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
K = 720 / 1170  # px del video del celular → px de la ventana ajustada al ancho (= --f-k)


def num(v):
    return f"{v:.6f}".rstrip('0').rstrip('.')


def s(n):  # cuadro → segundos
    return num(n / 30)


def ms(rec):  # cuadro de la grabación → data-media-start (+0,01 s: cae dentro del cuadro)
    return num(rec / 30 + 0.01)


# ─── Tramos de video ────────────────────────────────────────────────────────────────────────────────────────────────────────
# Acto 1 (cuadros 0–1079): los 29 tramos del clip (clip-sitio-membresia/index.html) SIN CAMBIOS, en segundos tal cual.
# (id, archivo, data-start, data-duration, data-media-start, tasa, pista, contenedor, comentario)
G1, G2 = 'assets/grabaciones/grabacion.mp4', 'assets/grabaciones/grabacion-2.mp4'
CLIP = [
    ('v01', G1, '0', '1', '5.466667', '0.466667', 10, 'm1', '0–30 · la «V» ya puesta y «aleria» letra a letra (grab. 164–176), a 0,467× (clip)'),
    ('v02', G1, '1', '1', '5.933333', '1.11', 10, 'm1', '30–60 · quieto hasta el toque en «Apellidos» (grab. 211), a 1,11×'),
    ('v03', G1, '2', '0.833333', '7.043333', '1.36', 10, 'm1', '60–85 · «Cardona Ríos» (grab. 211–245), a 1,36×'),
    ('v04', G1, '2.833333', '0.166667', '9.143333', '1', 10, 'm1', '85–90 · corte en la pausa hasta «Cómo llegó» (grab. 279)'),
    ('v05', G1, '3', '0.5', '9.31', '1.8', 10, 'm1', '90–105 · el selector se abre y queda abierto (grab. 288–306), a 1,8×'),
    ('v06', G1, '3.5', '0.1', '10.21', '3', 10, 'm1', '105–108 · el chip «Servicio General» (grab. 306–315), a 3×'),
    ('v07', G1, '3.6', '0.1', '10.51', '1', 10, 'm1', '108–111 · el selector se desvanece'),
    ('v08', G1, '3.7', '0.3', '15.276667', '1', 10, 'm1', '111–120 · corte en la pausa; la app salta a «Registrar» en el 114'),
    ('v09', G1, '4', '0.066667', '17.543333', '1', 10, 'iris1', '120 · toque en «Registrar» (grab. 526)'),
    ('v10', G1, '4.066667', '0.933333', '17.776667', '1', 10, 'iris1', '122–150 · «Guardada en este dispositivo» (corte en la espera 528→533)'),
    ('v11', G1, '5', '0.4', '20.543333', '1', 10, 'iris1', '150–162 · toque en «Entendido» (grab. 616)'),
    ('v12', G1, '5.4', '0.533333', '22.476667', '1', 10, 'iris1', '162–178 · la app vuelve arriba: «1 sin enviar»'),
    ('v13', G1, '5.933333', '0.266667', '26.376667', '1', 10, 'iris1', '178–186 · vuelve la señal; el látigo se lo lleva'),
    ('v14', G1, '6', '6.5', '73.576667', '1', 11, 'm2in', '180–375 · la tarjeta de Valeria quieta (grab. 2207–2402)'),
    ('v15', G1, '12.5', '0.033333', '80.076667', '1', 11, 'iris2', '375 · toque en «Marcar cumplido» (grab. 2402)'),
    ('v16', G1, '12.533333', '0.8', '80.376667', '1', 11, 'iris2', '376–400 · «Reporte del paso» entra 377–381'),
    ('v17', G1, '13.333333', '1.666667', '82.11', '1', 11, 'iris2', '400–450 · hasta el toque en «Contestó» (grab. 2513)'),
    ('v18', G1, '15', '0.066667', '83.776667', '1', 11, 'iris2', '450–452 · el toque en «Contestó»'),
    ('v19', G1, '15.066667', '0.766667', '83.976667', '1', 11, 'iris2', '452–475 · el radio se llena (456)'),
    ('v20', G1, '15.833333', '0.666667', '85.376667', '1', 11, 'iris2', '475–495 · hasta el toque en «Observaciones» (grab. 2581)'),
    ('v21', G1, '16.5', '2.4', '86.043333', '1.138889', 11, 'iris2', '495–567 · «Muy contenta, viene el domingo» (grab. 2581–2663), a 1,139×'),
    ('v22', G1, '18.9', '1.1', '91.143333', '1', 11, 'iris2', '567–600 · hasta el toque en «Marcar cumplido» del diálogo (grab. 2767)'),
    ('v23', G1, '20', '0.1', '92.243333', '1', 11, 'iris2', '600–603 · el toque'),
    ('v24', G1, '20.1', '3.233333', '93.243333', '1', 11, 'iris2', '603–700 · «cumplido · Ahora va en: …»'),
    ('v25', G1, '23.333333', '2.833333', '97.076667', '1', 11, 'iris2', '700–785 · «Listo» en el 720; la tarjeta al día desde el 738'),
    ('v29', G2, '28', '8', '104.51', '1', 12, 'm3post', '840–1080 · la ficha desplazada 484 px CSS, quieta (grab2. 3135–3375): el historial del 1020'),
    ('v26', G2, '26', '2', '94.676667', '1', 12, 'm3pre', '780–840 · la ficha limpia (grab2. 2840–2899)'),
    ('v27', G2, '28', '0.066667', '97.943333', '1', 12, 'm3pre', '840–842 · el dedo en «Avance» (grab2. 2938–2939)'),
    ('v28', G2, '28.066667', '3.933333', '98.276667', '1', 12, 'm3ab', '842–960 · la tarjeta abierta sin desplazar (grab2. 2948–3066)'),
]

# Capítulos nuevos (desde el 1080), en cuadros: (id, archivo, cuadro inicio, cuadro fin, cuadro de la grabación, tasa, pista, contenedor, comentario)
R1, R2, R3, R4 = ('assets/grabaciones/' + n + '.mp4' for n in ('coordinar', 'semaforo', 'discipulado', 'tableros'))
NUEVOS = [
    # C1 · Coordinar (R1, escritorio). Cambios medidos: lista 162–165, toque «Repartir» 317–318, diálogo 321–327, toque confirmar 418,
    # cierre 422–425, la K del cargador 430–508, resultado 509 con «Actualizando…» hasta el 521, limpio desde el 522; «Quienes acompañan» 709.
    ('r1a', R1, 1080, 1142, 99, 1, 13, 'r1base', '1080–1142 · «Resumen» quieto (grab. 99–158); toque en «Nuevos» en el 1140 (grab. 159)'),
    ('r1b', R1, 1142, 1207, 165, 1, 13, 'r1base', '1142–1207 · corte en la espera (160→165): la lista completa con «Repartir» (grab. 165–229); queda debajo del iris del 1200'),
    ('r1c', R1, 1200, 1203, 318, 1, 14, 'r1iris', '1200–1203 · toque en «Repartir» (grab. 318)'),
    ('r1d', R1, 1203, 1290, 330, 1, 14, 'r1iris', '1203–1290 · corte en el fundido (321→330): el diálogo «Repartir» completo y quieto (grab. 330–416)'),
    ('r1e', R1, 1290, 1297, 418, 1, 14, 'r1iris', '1290–1297 · toque en «Repartir» del diálogo (grab. 418) y el diálogo que se cierra (422–424)'),
    ('r1f', R1, 1297, 1320, 293, 1, 14, 'r1iris', '1297–1320 · la lista todavía con sus nuevos (grab. 293–315, igual que antes del diálogo): la espera y la K del cargador se cortan'),
    ('r1g', R1, 1320, 1380, 522, 1, 14, 'r1iris', '1320–1380 · el resultado de golpe: «Se repartieron 257 personas.» y «Todos los nuevos tienen quién los acompañe.» (grab. 522–581, sin «Actualizando…»)'),
    ('r1h', R1, 1380, 1383, 707, 2 / 3, 14, 'r1iris', '1380–1383 · toque en «Quienes acompañan» (grab. 707–708), a 0,667×'),
    ('r1i', R1, 1383, 1560, 759, 0.63, 14, 'r1iris', '1383–1560 · «Quienes acompañan» quieto (grab. 759–871, a 0,63×): se salta el parpadeo de una barra del 709 al 758'),
    # C2 · Semáforo (R2, celular). Cambios: toque «Agregar filtro» 415, la hoja sube 422–427, toque «Semáforo» 504, editor 509, «Rojo» 622–628,
    # «Aplicar» 683–687, la hoja se va 689–691, lista filtrada 692, toque en la persona 919, «Cargando…» 928, ficha 933, limpia 936.
    ('r2a', R2, 1560, 1641, 354, 1, 15, 'r2base', '1560–1641 · la lista quieta; toque en «Agregar filtro» en el 1620 (grab. 414); la hoja sube 1628–1633 (grab. 422–427, a 1×)'),
    ('r2b', R2, 1641, 1665, 478, 1, 15, 'r2base', '1641–1665 · corte en la pausa (434→478): la hoja quieta'),
    ('r2c', R2, 1665, 1668, 502, 1, 15, 'r2base', '1665–1668 · toque en «Semáforo de actividad» (grab. 502–504)'),
    ('r2d', R2, 1668, 1710, 509, 1, 15, 'r2base', '1668–1710 · corte (504→509): el editor con los cuatro colores y sus días'),
    ('r2e', R2, 1710, 1740, 621, 1, 15, 'r2base', '1710–1740 · toque en «Rojo · 31 a 50 días» (grab. 621): la casilla se marca 1711–1717'),
    ('r2f', R2, 1740, 1744, 683, 1, 15, 'r2base', '1740–1744 · toque en «Aplicar» (grab. 683–686)'),
    ('r2g', R2, 1744, 1806, 692, 1, 15, 'r2base', '1744–1806 · corte (686→692): la lista filtrada, «Semáforo de actividad: Rojo» y «62 de 1.324»; queda debajo del iris del 1800'),
    ('r2h', R2, 1800, 1803, 918, 1, 16, 'r2iris', '1800–1803 · toque en Sara Yepes Muñoz (grab. 918–920)'),
    ('r2i', R2, 1803, 1925, 936, 1, 16, 'r2iris', '1803–1925 · corte en «Cargando…» y «Actualizando…» (920→936): la ficha con «Actividad: Rojo · hace 31 días»'),
    # C3 · Discipulado (R3, celular). Cambios: cabezas desde el 63/65, toque en la cabeza → pirámide 235, desplazamiento de 7 px CSS en el 387
    # (no se usa), toque «bajar» → nivel nuevo 441.
    ('r3a', R3, 1914, 2046, 100, 1, 17, 'r3base', '1914–2046 · «Quienes encabezan la pirámide (1)» quieto (grab. 100–231); queda debajo del iris del 2040'),
    ('r3b', R3, 2040, 2043, 232, 1, 18, 'r3iris1', '2040–2043 · toque en la cabeza (grab. 232–234)'),
    ('r3c', R3, 2043, 2166, 238, 1, 18, 'r3iris1', '2043–2166 · la pirámide abierta: «24 directos · 725 en total» y «Sus discípulos directos (12)» (grab. 238–360, antes del desplazamiento del 387)'),
    ('r3d', R3, 2160, 2163, 355, 1, 19, 'r3iris2', '2160–2163 · toque en «PA Hernán Álvarez Arias y PA Luz Elena García Herrera» (la misma imagen, grab. 355–357)'),
    ('r3e', R3, 2163, 2287, 443, 1, 19, 'r3iris2', '2163–2287 · un nivel más abajo: las migas y «12 directos · 162 en total» (grab. 443–566)'),
    # C4 · Tableros (R4, escritorio). Cambios: toque en la descarga 380, menú 384–386, Escape 451, el menú se cierra 453–456, desplazamiento
    # instantáneo de 453 px CSS en el 506 (capa B, 453 px más abajo: la cámara recorre una sola página).
    ('r4a', R4, 2280, 2490, 160, 1, 20, 'r4a', '2280–2490 · «Resumen» quieto: las cifras y el semáforo de actividad (grab. 160–369)'),
    ('r4b', R4, 2490, 2493, 380, 1, 20, 'r4a', '2490–2493 · toque en la descarga (grab. 380–382)'),
    ('r4c', R4, 2493, 2520, 386, 1, 20, 'r4a', '2493–2520 · corte (382→386): el menú «PDF · Excel» abierto'),
    ('r4d', R4, 2520, 2535, 453, 1, 20, 'r4a', '2520–2535 · Escape: el menú se cierra (grab. 453–456); la página sin desplazar debajo de la capa B'),
    ('r4e', R4, 2520, 2760, 509, 0.72, 21, 'r4b', '2520–2760 · la página desplazada 453 px CSS: el crecimiento (grab. 509–681, a 0,72×)'),
]

# ─── Marcas de toque ─────────────────────────────────────────────────────────────────────────────────────────────────────────
# (cuadro, contenedor, x, y, tipo, comentario). Celular: px del video × K (de toques[] de pasos*.json). Escritorio: px CSS × 2 (nivel D).
MARCAS = [
    (60, 'm1', 585 * K, 783 * K, 'cel', '«Apellidos»'), (90, 'm1', 585 * K, 1250 * K, 'cel', '«Cómo llegó»'),
    (105, 'm1', 585 * K, 1574 * K, 'cel', '«Servicio General»'), (120, 'm1', 931 * K, 2184 * K, 'cel', '«Registrar»'),
    (150, 'm1', 877 * K, 1506 * K, 'cel', '«Entendido»'),
    (375, 'm2in', 671 * K, 2136 * K, 'cel', '«Marcar cumplido»'), (450, 'm2in', 277 * K, 837 * K, 'cel', '«Contestó»'),
    (495, 'm2in', 585 * K, 1677 * K, 'cel', '«Observaciones»'), (600, 'm2in', 808 * K, 2088 * K, 'cel', '«Marcar cumplido» del diálogo'),
    (780, 'm3', 510 * K, 1476 * K + 900 - 2532 * K, 'cel', 'el nombre de Valeria (pantalla del mundo 2)'), (840, 'm3', 585 * K, 2001 * K, 'cel', '«Avance»'),
    (1140, 'r1', 341 * 2, 189 * 2, 'esc', '«Nuevos» (pasos: 511·283 px del video)'),
    (1200, 'r1', 1149 * 2, 237 * 2, 'esc', '«Repartir» (1723·356)'),
    (1290, 'r1', 805 * 2, 434 * 2, 'esc', '«Repartir» del diálogo (1208·651)'),
    (1380, 'r1', 492 * 2, 189 * 2, 'esc', '«Quienes acompañan» (738·283)'),
    (1620, 'r2', 285 * K, 759 * K, 'cel', '«Agregar filtro»'), (1665, 'r2', 585 * K, 1025 * K, 'cel', '«Semáforo de actividad»'),
    (1710, 'r2', 348 * K, 2133 * K, 'cel', '«Rojo · 31 a 50 días»'), (1740, 'r2', 954 * K, 2424 * K, 'cel', '«Aplicar»'),
    (1800, 'r2', 585 * K, 1251 * K, 'cel', 'Sara Yepes Muñoz'),
    (2040, 'r3', 519 * K, 1416 * K, 'cel', 'la cabeza de la pirámide'),
    (2160, 'r3', 519 * K, (2049 + 21) * K, 'cel', 'el primer discípulo que discipula (toques[] + 7 px CSS: la imagen es la de antes del desplazamiento)'),
    (2490, 'r4', 1188 * 2, 245 * 2, 'esc', 'la descarga (1782·368)'),
]

# ─── Sonidos ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────
TQ = {'a': ('identidad/audio/toque.wav', 0.075), 'b': ('assets/audio/toque-b.wav', 0.072833), 'c': ('assets/audio/toque-c.wav', 0.077333)}
AP = {'a': ('identidad/audio/aparicion.wav', 0.22, 0), 'b': ('assets/audio/aparicion-b.wav', 0.213604, 0), 'c': ('assets/audio/aparicion-c.wav', 0.226813, 0)}
DS = {'a': ('identidad/audio/desliz.wav', 0.36, 0.2), 'b': ('assets/audio/desliz-b.wav', 0.349521, 0.2 / 1.03), 'c': ('assets/audio/desliz-c.wav', 0.371146, 0.2 / 0.97)}
CF = ('identidad/audio/confirmacion.wav', 0.32, 0.1)
# (cuadro del pico, tipo, toma, volumen, comentario)
SND = [
    (61, 'toque', 'a', 1, '«Apellidos»'), (91, 'toque', 'b', 1, '«Cómo llegó»'), (109, 'aparicion', 'a', 1, 'el chip «Servicio General» (108)'),
    (115, 'desliz', 'a', 1, 'la cámara baja y la app salta a «Registrar» (109–120)'),
    (121, 'toque', 'c', 1.4, '«Registrar» (+3 dB)'), (123, 'confirmacion', '', 1.4, '«Guardada en este dispositivo» (+3 dB)'),
    (151, 'toque', 'a', 1, '«Entendido»'), (166, 'aparicion', 'a', 1, '«1 sin enviar» (165)'), (180, 'desliz', 'a', 1.4, 'el látigo (+3 dB)'),
    (196, 'aparicion', 'a', 1, 'la ceja «MEMBRESÍA» (195)'), (376, 'toque', 'b', 1, '«Marcar cumplido»'), (451, 'toque', 'c', 1, '«Contestó»'),
    (496, 'toque', 'a', 1, '«Observaciones»'), (601, 'toque', 'b', 1.4, '«Marcar cumplido» del diálogo (+3 dB)'),
    (603, 'confirmacion', '', 1.4, '«cumplido» (+3 dB)'), (721, 'toque', 'c', 1, '«Listo»'), (781, 'toque', 'a', 1, 'el nombre de Valeria'),
    (841, 'toque', 'b', 1.4, '«Avance» (+3 dB)'), (843, 'aparicion', 'a', 1.4, 'la tarjeta «Avance» abierta (+3 dB)'),
    (1080, 'desliz', 'a', 1.4, 'el morph al escritorio (+3 dB)'),
    (1087, 'aparicion', 'a', 1, 'la ceja «COORDINAR» (1086)'), (1141, 'toque', 'c', 1, '«Nuevos»'), (1201, 'toque', 'a', 1.4, '«Repartir» (+3 dB)'),
    (1204, 'aparicion', 'b', 1, 'el diálogo «Repartir» (1203)'), (1291, 'toque', 'b', 1, '«Repartir» del diálogo'),
    (1321, 'confirmacion', '', 1.4, '«Se repartieron 257 personas.» (+3 dB)'), (1381, 'toque', 'c', 1, '«Quienes acompañan»'),
    (1560, 'desliz', 'b', 1, 'el morph al celular'),
    (1567, 'aparicion', 'b', 1, 'la ceja «SEMÁFORO DE ACTIVIDAD» (1566)'), (1621, 'toque', 'a', 1, '«Agregar filtro»'),
    (1666, 'toque', 'b', 1, '«Semáforo de actividad»'), (1711, 'toque', 'c', 1, '«Rojo»'), (1741, 'toque', 'a', 1, '«Aplicar»'),
    (1744, 'aparicion', 'c', 1, 'el chip y la lista en rojo'), (1801, 'toque', 'b', 1.4, 'Sara Yepes Muñoz (+3 dB)'),
    (1920, 'desliz', 'c', 1, 'el látigo vertical'),
    (1927, 'aparicion', 'c', 1, 'la ceja «DISCIPULADO» (1926)'), (2041, 'toque', 'c', 1.4, 'la cabeza de la pirámide (+3 dB)'),
    (2044, 'aparicion', 'a', 1.4, 'la pirámide abierta (+3 dB)'), (2161, 'toque', 'a', 1, 'un nivel más'),
    (2280, 'desliz', 'a', 1.4, 'el morph al escritorio (+3 dB)'),
    (2287, 'aparicion', 'a', 1, 'la ceja «TABLEROS» (2286)'), (2491, 'toque', 'b', 1, 'la descarga'), (2494, 'aparicion', 'b', 1, 'el menú «PDF · Excel» (2493)'),
]


def video(t, ind):
    i, src, a, b, rec, rate, tr, _, com = t
    if isinstance(a, str):
        st, du, me, ra = a, b, rec, rate
    else:
        st, du, me, ra = s(a), s(b - a), ms(rec), num(rate)
    return (f"{ind}<!-- {com} -->\n{ind}<video data-hf-id=\"hf-{i}\" id=\"{i}\" class=\"clip\" src=\"{src}\" muted playsinline data-track-index=\"{tr}\"\n"
            f"{ind}  data-start=\"{st}\" data-duration=\"{du}\" data-media-start=\"{me}\" data-playback-rate=\"{ra}\"></video>\n")


def videos(cont, ind):
    return ''.join(video(t, ind) for t in CLIP + NUEVOS if t[7] == cont).rstrip('\n')


def marcas(cont, ind):
    out = ''
    for n, c, x, y, tipo, com in MARCAS:
        if c != cont:
            continue
        cl = '' if tipo == 'cel' else ' esc'
        out += (f"{ind}<!-- {n} · {com} -->\n"
                f"{ind}<div data-hf-id=\"hf-tq{n}\" class=\"toque{cl}\" id=\"tq-{n}\" style=\"left: {x:.1f}px; top: {y:.1f}px\"></div>\n"
                f"{ind}<div data-hf-id=\"hf-on{n}\" class=\"onda{cl}\" id=\"on-{n}\" style=\"left: {x:.1f}px; top: {y:.1f}px\"></div>\n")
    return out.rstrip('\n')


def sonidos():
    out = ''
    for n, tipo, toma, vol, com in SND:
        if tipo == 'toque':
            (f, d), ac = TQ[toma], 0
        elif tipo == 'aparicion':
            f, d, ac = AP[toma]
        elif tipo == 'desliz':
            f, d, ac = DS[toma]
        else:
            f, d, ac = CF
        st = num(n / 30 - ac)
        sid = f"snd-{tipo}-{n}"
        out += (f"      <!-- {n} · {tipo} {toma} · {com} -->\n"
                f"      <audio data-hf-id=\"hf-{sid}\" id=\"{sid}\" src=\"{f}\" data-start=\"{st}\" data-duration=\"{num(d)}\" "
                f"data-track-index=\"{ {'toque': 31, 'aparicion': 32, 'desliz': 33, 'confirmacion': 34}[tipo] }\" data-volume=\"{num(vol)}\"></audio>\n")
    return out.rstrip('\n')


# ─── Textos: frases y cejas (subcomposiciones) ───────────────────────────────────────────────────────────────────────────────
# Celular: ceja x 120 · y 428, frase x 120 · y 476 (88 px, 2 líneas). Escritorio: ceja x 240 · y 76, frase x 240 · y 118 (84 px, 1 línea).
# (n, mundo, host (cuadro), líneas [[(palabra, em)]], entradas por palabra (cuadro local; None = la línea entera en el 0), salida (cuadro local o None), fin (cuadro))
FRASES = [
    (1, 'cel', 0, [['Valeria', 'llegó'], ['el', 'domingo.']], [None, 15, 30, 45], 117, 122, 'P1 · una palabra por pulso; «Valeria» ya está en el 0 (la miniatura); sale 117–121'),
    (2, 'cel', 119, [['Registrada.'], ['Aun sin señal.']], 'linea', 58, 182, 'P2 · la línea entera 120–126 con el toque en «Registrar»; sale 177–181 antes del látigo'),
    (3, 'cel', 359, [['Y', 'ya', 'tiene', 'quién'], ['la', 'llame']], 'pal', 238, 602, 'P4 · palabra a palabra cada 2 cuadros desde el 360; sale 597–601'),
    (4, 'cel', 839, [['Y', 'una', 'ruta'], ['para', 'crecer']], 'pal', 232, 1076, 'P7–P8 · desde el golpe más fuerte (840); se queda sobre la ficha y el historial; sale 1071–1075 antes del morph'),
    (5, 'esc', 1094, [['Nadie', 'nuevo', 'se', 'queda', 'sin', 'llamada']], 'pal', 457, 1556, 'P9 · Coordinar: Nadie 1095 … llamada 1105; sale 1551–1555'),
    (6, 'cel', 1574, [['Ves', 'a', 'tiempo'], ['quién', 'se', 'aleja']], 'pal', 337, 1916, 'P10 · el semáforo: Ves 1575 … aleja 1585; sale 1911–1915'),
    (7, 'cel', 1949, [['Quién', 'discipula'], ['a', 'quién']], 'pal', 322, 2276, 'P11 · el discipulado: Quién 1950 … quién 1956; sale 2271–2275'),
    (8, 'esc', 2294, [['Tu', 'iglesia,', 'de', 'un', 'vistazo']], 'pal', 342, 2641, 'P12 · los tableros: Tu 2295 … vistazo 2303; sale 2636–2640 (blur swap con la frase 9)'),
    (9, 'esc', 2639, [['Que', '*ninguna', 'persona', 'se', 'pierda']], 'pal', None, 2760, 'P12 · Que 2640 · ninguna 2642 · persona 2644 · se 2646 · pierda 2648; quieta hasta el corte al cierre (2760). La única palabra dorada del cuerpo'),
]
CEJAS = [
    (1, 'cel', 194, 'Membresía', 877, 1076, 'entra 195–201 sobre la tarjeta de Valeria; sale 1071–1075'),
    (2, 'esc', 1085, 'Coordinar', 466, 1556, 'entra 1086–1092; sale 1551–1555'),
    (3, 'cel', 1565, 'Semáforo de actividad', 346, 1916, 'entra 1566–1572; sale 1911–1915'),
    (4, 'cel', 1925, 'Discipulado', 346, 2276, 'entra 1926–1932 (el vocabulario de Kingdom Demo); sale 2271–2275'),
    (5, 'esc', 2285, 'Tableros', 351, 2641, 'entra 2286–2292; sale 2636–2640'),
]
POS = {'cel': dict(cx=120, cy=428, fx=120, fy=476, px=88, w=888), 'esc': dict(cx=240, cy=76, fx=240, fy=118, px=84, w=1440)}

ESC_HEAD = '''<!doctype html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <!-- {com} -->
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
{css}
      </style>
'''


def frase(n, mundo, host, lineas, entradas, salida, fin, com):
    p = POS[mundo]
    cid = f'frase-{n}'
    dur = num((fin - host) / 30)
    css = f'''        .f-frase {{
          position: absolute;
          left: {p['fx']}px;
          top: {p['fy']}px;
          width: {p['w']}px;
          font-size: {p['px']}px;
          color: var(--k-noche-tinta);
          text-wrap: initial;
        }}
        .f-frase em {{
          color: var(--k-noche-dorado);
        }}
        .linea {{
          display: block;
          white-space: nowrap;
        }}
        .palabra {{
          display: inline-block;
        }}'''
    k = 0
    html_l = []
    for li, ws in enumerate(lineas):
        if entradas == 'linea':
            html_l.append(f'<span data-hf-id="hf-f{n}l{li}" class="linea">{" ".join(ws)}</span>')
            continue
        partes = []
        for w in ws:
            k += 1
            if w.startswith('*'):
                partes.append(f'<em data-hf-id="hf-f{n}em"><span data-hf-id="hf-f{n}w{k}" class="palabra" id="f{n}-w{k}">{w[1:]}</span></em>')
            else:
                partes.append(f'<span data-hf-id="hf-f{n}w{k}" class="palabra" id="f{n}-w{k}">{w}</span>')
        html_l.append(f'<span data-hf-id="hf-f{n}l{li}" class="linea">{" ".join(partes)}</span>')
    cuerpo = '\n          '.join(html_l)
    js = []
    if entradas == 'linea':
        js.append(f"tl.fromTo('#f{n}', {{ opacity: 0, filter: 'blur(8px)' }}, {{ opacity: 1, filter: 'blur(0px)', duration: F(6), ease: 'power4.out' }}, 0); // entrada-linea")
    elif entradas == 'pal':
        js.append(f"for (let i = 1; i <= {k}; i++) {{\n            // entrada-palabra: el host arranca un cuadro antes del pulso; el primer cuadro visible es el pulso\n"
                  f"            tl.fromTo(`#f{n}-w${{i}}`, {{ opacity: 0, filter: 'blur(6px)' }}, {{ opacity: 1, filter: 'blur(0px)', duration: F(4), ease: 'power4.out' }}, F(2 * (i - 1)));\n          }}")
    else:
        for i, e in enumerate(entradas, 1):
            if e is not None:
                js.append(f"tl.fromTo('#f{n}-w{i}', {{ opacity: 0, filter: 'blur(6px)' }}, {{ opacity: 1, filter: 'blur(0px)', duration: F(4), ease: 'power4.out' }}, F({e - 1}));")
    if salida is not None:
        js.append(f"tl.to('#f{n}', {{ opacity: 0, filter: 'blur(8px)', duration: F(4), ease: 'power3.in' }}, F({salida})); // salida-texto: {host + salida}–{host + salida + 4}")
    js.append(f"tl.set({{}}, {{}}, F({fin - host}));")
    jstxt = '\n          '.join(js)
    out = ESC_HEAD.format(com=f'Frase {n} ({mundo}, host {host}–{fin}): {com}', css=css)
    out += f'''      <div data-hf-id="hf-f{n}r" id="root" data-composition-id="{cid}" data-width="1920" data-height="1080" data-duration="{dur}">
        <div data-hf-id="hf-f{n}t" class="k-titular f-frase" id="f{n}">
          {cuerpo}
        </div>
      </div>
      <script>
        (function () {{
          const F = (n) => n / 30;
          const tl = gsap.timeline({{ paused: true }});
          {jstxt}
          window.__timelines['{cid}'] = tl;
        }})();
      </script>
    </template>
  </body>
</html>
'''
    return cid, out, host, fin


def ceja(n, mundo, host, texto, salida, fin, com):
    p = POS[mundo]
    cid = f'ceja-{n}'
    css = f'''        .f-ceja {{
          position: absolute;
          left: {p['cx']}px;
          top: {p['cy']}px;
          color: var(--k-noche-dorado);
          line-height: 1;
          white-space: nowrap;
        }}'''
    out = ESC_HEAD.format(com=f'Ceja {n} ({mundo}, host {host}–{fin}): «{texto.upper()}» {com}. Inter 700, 28 px, mayúsculas, dorado', css=css)
    out += f'''      <div data-hf-id="hf-c{n}r" id="root" data-composition-id="{cid}" data-width="1920" data-height="1080" data-duration="{num((fin - host) / 30)}">
        <div data-hf-id="hf-c{n}t" class="k-ceja f-ceja" id="c{n}">{texto}</div>
      </div>
      <script>
        (function () {{
          const F = (n) => n / 30;
          const tl = gsap.timeline({{ paused: true }});
          tl.fromTo('#c{n}', {{ opacity: 0, filter: 'blur(8px)' }}, {{ opacity: 1, filter: 'blur(0px)', duration: F(6), ease: 'power4.out' }}, 0); // entrada-linea
          tl.to('#c{n}', {{ opacity: 0, filter: 'blur(8px)', duration: F(4), ease: 'power3.in' }}, F({salida})); // salida-texto: {host + salida}–{host + salida + 4}
          tl.set({{}}, {{}}, F({fin - host}));
          window.__timelines['{cid}'] = tl;
        }})();
      </script>
    </template>
  </body>
</html>
'''
    return cid, out, host, fin


HALOS = [0, 180, 780, 960, 1080, 1560, 1920, 2280, 2640]
FONDO = '''<!doctype html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <!-- El fondo del cuerpo (0–2760): la noche del sitio con el halo y la retícula de puntos del kit (identidad/kit.css, enlazado por el host).
         El halo se asienta una vez por mundo (1,08 → 1,00 en 90 cuadros, sine.out) en los cuadros @@HALOS@@; los puntos no se mueven. -->
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
      </style>
      <div data-hf-id="hf-fdr" id="root" data-composition-id="fondo" data-width="1920" data-height="1080" data-duration="92">
        <div data-hf-id="hf-fdn" class="k-noche">
          <div data-hf-id="hf-fdh" class="k-halo" id="fondo-halo" data-layout-allow-overflow></div>
          <div data-hf-id="hf-fdp" class="k-puntos"></div>
        </div>
      </div>
      <script>
        (function () {
          const tl = gsap.timeline({ paused: true });
          [@@HALOS@@].forEach((n) => {
            tl.fromTo('#fondo-halo', { scale: 1.08 }, { scale: 1, duration: 3, ease: 'sine.out', immediateRender: n === 0 }, n / 30);
          });
          tl.set({}, {}, 92);
          window.__timelines['fondo'] = tl;
        })();
      </script>
    </template>
  </body>
</html>
'''

if __name__ == '__main__':
    comp = os.path.join(RAIZ, 'compositions')
    os.makedirs(comp, exist_ok=True)
    halos = ', '.join(str(h) for h in HALOS)
    open(os.path.join(comp, 'fondo.html'), 'w', encoding='utf-8', newline='\n').write(FONDO.replace('@@HALOS@@', halos))
    hosts = []
    pista = {'frase': [1, 2], 'ceja': [3, 4]}
    for i, f in enumerate(FRASES):
        cid, html, a, b = frase(*f)
        open(os.path.join(comp, cid + '.html'), 'w', encoding='utf-8', newline='\n').write(html)
        hosts.append((cid, a, b, pista['frase'][i % 2], f[7], f[0] == 9))
    for i, c in enumerate(CEJAS):
        cid, html, a, b = ceja(*c)
        open(os.path.join(comp, cid + '.html'), 'w', encoding='utf-8', newline='\n').write(html)
        hosts.append((cid, a, b, pista['ceja'][i % 2], f'«{c[3].upper()}» {c[6]}', False))
    hosts.sort(key=lambda h: h[1])
    htxt = ''
    for cid, a, b, tr, com, hold in hosts:
        extra = ' data-hold' if hold else ''
        htxt += (f"      <!-- {com} -->\n      <div data-hf-id=\"hf-h-{cid}\" id=\"{cid}\" data-composition-id=\"{cid}\" data-composition-src=\"compositions/{cid}.html\""
                 f" data-track-kind=\"graphics\"{extra}\n        data-start=\"{s(a)}\" data-duration=\"{s(b - a)}\" data-track-index=\"{tr}\" data-width=\"1920\" data-height=\"1080\"></div>\n")
    tpl = open(os.path.join(RAIZ, '_gen', 'index.tpl.html'), encoding='utf-8').read()
    reps = {'@@HOSTS@@': htxt.rstrip('\n'), '@@SONIDOS@@': sonidos(),
            '@@TOQUES@@': ', '.join(str(m[0]) for m in MARCAS)}
    for cont in ['m1', 'iris1', 'm2in', 'iris2', 'm3post', 'm3pre', 'm3ab', 'r1base', 'r1iris', 'r2base', 'r2iris', 'r3base', 'r3iris1', 'r3iris2', 'r4a', 'r4b']:
        reps[f'@@V:{cont}@@'] = videos(cont, '')
    for cont in ['m1', 'm2in', 'm3', 'r1', 'r2', 'r3', 'r4']:
        reps[f'@@M:{cont}@@'] = marcas(cont, '')
    out = tpl
    # Sangría: cada marcador va solo en su línea; se reemplaza respetando la sangría de esa línea.
    lineas = []
    for ln in out.split('\n'):
        st = ln.strip()
        if st in reps:
            ind = ln[:len(ln) - len(ln.lstrip())]
            lineas.append('\n'.join(ind + x if x else x for x in reps[st].split('\n')))
        else:
            for k2, v in reps.items():
                if k2 in ln:
                    ln = ln.replace(k2, v)
            lineas.append(ln)
    open(os.path.join(RAIZ, 'index.html'), 'w', encoding='utf-8', newline='\n').write('\n'.join(lineas))
    print('ok', len(CLIP) + len(NUEVOS), 'tramos ·', len(MARCAS), 'marcas ·', len(SND), 'sonidos ·', len(hosts), 'textos')
