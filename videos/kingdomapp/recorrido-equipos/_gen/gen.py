# Genera index.html y compositions/frase-*.html + ceja.html del recorrido de Equipos (16:9), desde index.tpl.html y estas tablas.
#   python _gen/gen.py            (desde recorrido-equipos/)
# Tramos de video, marcas de toque, sonidos y frases -> HTML. Los cuadros son del video (30 fps); «rec» = cuadro de la grabación.
import os, sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
FPS = 30
def s(n): return f"{n / FPS:.6f}".rstrip('0').rstrip('.')
def ms(g): return f"{g / FPS + 0.01:.6f}".rstrip('0').rstrip('.')

K = 'assets/grabaciones/parqueadero/grabacion.mp4'   # la grabación del clip (1170×2532)
C = 'assets/grabaciones/celular.mp4'                 # la grabación nueva de celular (1170×2532, 2416 cuadros)
E = 'assets/grabaciones/escritorio.mp4'              # la grabación nueva de escritorio (1920×1080, 760 cuadros)

# ── Tramos: (id, desde, hasta, rec, comentario) ─────────────────────────────────────────────────────────────────────────────────────────
# Parte 1: los del clip, sin cambios (clip-sitio-equipos/_gen/gen.py)
M1A = [  # cam1: antes del iris del 120
    ('v01', 0, 78, 81, '0–78 · el calendario de Seguridad ya desplazado al primer domingo (grab. 81–158); toque en la fila del domingo en el 75 (grab. 156)'),
    ('v02', 78, 120, 169, '78–120 · match cut sobre el toque: el turno ya cargado (grab. 169–210; el esqueleto 163–168 queda fuera); entra 1,03 → 1,00'),
    ('v03', 120, 121, 362, '120 · toque en «Asignar» (grab. 362); el iris nace aquí'),
]
M1B = [  # cam1b: dentro del iris del 120 y la vuelta del 656
    ('v04', 121, 150, 379, '121–150 · el diálogo «Asignar · Parqueadero» ya puesto, con la lista sugerida (grab. 379–407)'),
    ('v05', 150, 151, 463, '150 · toque en la casilla de Gabriela (grab. 463)'),
    ('v06', 151, 180, 470, '151–180 · corte en la onda: la fila de Gabriela ya llena y «Asignar (1)» (grab. 470–498)'),
    ('v07', 180, 181, 524, '180 · toque en «Asignar (1)» (grab. 524)'),
    ('v08', 181, 183, 539, '181–183 · corte en la espera: el diálogo ya se fue, el puesto todavía «Vacante» (grab. 539–540)'),
    ('v09', 183, 240, 542, '183–240 · Gabriela «Sin avisar» y la barra «Avisar a 1 persona» (grab. 542–598)'),
    ('v10', 240, 242, 689, '240–242 · toque en «Avisar a 1 persona» (grab. 689–690)'),
    ('v11', 242, 300, 717, '242–300 · corte en la espera y la K del cargador: «Avisados» entero (grab. 717–774)'),
    ('v12', 300, 301, 805, '300 · toque en «Entendido» (grab. 805)'),
    ('v13', 301, 303, 815, '301–303 · corte en el fundido del diálogo: todavía «Sin avisar» (grab. 815–816)'),
    ('v14', 303, 367, 819, '303–367 · el turno recargado: Gabriela «Por confirmar» (grab. 819–882); el látigo se lo lleva en 356–366'),
    ('v15', 656, 840, 1660, '656–839 · el látigo de vuelta: el turno del líder, Gabriela «Confirmado», «5 de 5» (grab. 1660–1843); el látigo horizontal se lo lleva en 830–840'),
]
M2A = [
    ('w01', 356, 375, 1113, '356–375 · Mi iglesia de Gabriela con «Tu próximo servicio» (grab. 1113–1131)'),
    ('w02', 375, 376, 1132, '375 · toque en la tarjeta (grab. 1132); el iris nace aquí'),
]
M2B = [
    ('w03', 376, 450, 1144, '376–450 · su servicio, «Llega a las 7:45 a. m.», «Por confirmar» (grab. 1144–1217)'),
    ('w04', 450, 540, 1270, '450–540 · la app baja a «Instrucciones» en un cuadro (grab. 1270, salto real)'),
    ('w05', 540, 600, 1392, '540–600 · la app vuelve arriba en un cuadro (grab. 1392): «Aceptar · No puedo»'),
    ('w06', 600, 602, 1469, '600–602 · toque en «Aceptar» (grab. 1469–1470)'),
    ('w07', 602, 667, 1484, '602–667 · «¡Gracias por servir! Tu líder ya lo sabe.», «Confirmado» (grab. 1484–1548)'),
]
# Parte 2, celular de Jorge (celular.mp4)
C3A = [  # cam3: el chat de Alabanza y el toque en «Servir»
    ('c01', 1310, 1443, 132, '1310–1442 · el chat de Alabanza con la encuesta en el centro y el anuncio anclado arriba (rec 132–264; la entrada 0–43 queda fuera); toque en «Way Maker» en el 1440 (rec 262)'),
    ('c02', 1443, 1500, 269, '1443–1499 · corte en la espera (265→269): «Way Maker» marcada, 7 → 8, «11 personas votaron» (rec 269–325)'),
    ('c03', 1500, 1560, 336, '1500–1559 · la app baja al ensayo en un cuadro (rec 336, salto real): «Ensayo de Alabanza», «Asistiré · No asistiré», «Van 9» (rec 336–395)'),
    ('c04', 1560, 1563, 428, '1560–1562 · toque en «Asistiré» (rec 428–430; corte en la espera quieta 396→428)'),
    ('c05', 1563, 1680, 440, '1563–1679 · corte en la onda (431→440): «Asistiré» lleno y «Van 10 · no van 1» (rec 440–556)'),
    ('c06', 1680, 1681, 601, '1680 · toque en la caja de escribir (rec 601; corte en la espera quieta 557→601)'),
    ('c07', 1681, 1740, 643, '1681–1739 · corte en el foco (602→643): «¡Cuenten conmigo el jueves!» se escribe a 1×, de la primera letra (rec 643) a la última (rec 701)'),
    ('c08', 1740, 1743, 750, '1740–1742 · toque en «Enviar» (rec 750–752; corte en el cursor quieto 702→750)'),
    ('c09', 1743, 1800, 758, '1743–1799 · corte (753→758): su mensaje al final del hilo, con el reloj y luego «20:05» (rec 758–814)'),
    ('c10', 1800, 1803, 876, '1800–1802 · toque en «Servir» de la barra de abajo (rec 876–878); el inicio de Servir carga en 886–946 y queda fuera'),
]
C3B = [  # cam3b: dentro del iris del 1920
    ('c11', 1921, 2040, 1188, '1921–2039 · «Cerrar el turno» ya cargado (rec 1188–1306; el esqueleto 1112 y el desplazamiento quedan fuera): «5 sirvieron · 0 no llegaron», todos «Sirvió»'),
    ('c12', 2040, 2043, 1307, '2040–2042 · toque en «No llegó» de Julián Villa Jaramillo (rec 1307–1309)'),
    ('c13', 2043, 2160, 1362, '2043–2159 · corte en la espera (1310→1362): Julián en rojo, «4 sirvieron · 1 no llegaron» (rec 1362–1478)'),
    ('c14', 2160, 2168, 1479, '2160–2167 · toque en «Cerrar el turno» (rec 1479–1486); el aviso «Quedó guardado en este dispositivo…» de 1487–1494 queda fuera (still del 1486 hasta el 2175)'),
    ('c15', 2175, 2281, 1502, '2175–2280 · corte en la entrada del diálogo (1487→1502): «El turno quedó cerrado · 1 persona cumplió su objetivo de servir en la ruta.» (rec 1502–1607; «Entendido» se toca en el 1656, fuera)'),
]
C4 = [  # cam4: el celular de Gabriela
    ('c16', 2270, 2346, 1844, '2270–2345 · Mi iglesia de Gabriela, «Buenas noches, Gabriela» (rec 1844–1919; el cambio de cuenta 1714–1790 queda fuera); toque en «Objetivos» en el 2340 (rec 1914)'),
    ('c17', 2346, 2760, 1927, '2346–2759 · corte sobre el toque (1920→1927; la página en blanco 1922–1926 queda fuera): «Mis objetivos» sube y el check de «Servir» se cierra en el 2355 (rec 1936); «Cumplido el vie, 30 de oct» (rec 1927–2340)'),
]
E1 = [  # camE1: la cobertura del administrador (escritorio.mp4)
    ('e01', 830, 900, 48, '830–899 · la cobertura del próximo domingo, arriba: el selector, «Solo lo que falta» y «13 de 19 confirmados (68 %)» (rec 48–117)'),
    ('e02', 900, 1080, 118, '900–1079 · la app baja a Seguridad en un cuadro (rec 118, salto real): «5/5 · 100 %», Gabriela «Confirmado» (rec 118–297)'),
    ('e03', 1080, 1140, 298, '1080–1139 · la app vuelve arriba en un cuadro (rec 298, salto real): «Solo lo que falta», «2/7 · 29 %» (rec 298–357)'),
    ('e04', 1140, 1143, 422, '1140–1142 · toque en «Solo lo que falta» (rec 422–424; corte en la espera quieta 358→422)'),
    ('e05', 1143, 1320, 427, '1143–1319 · corte en el interruptor (425→427): ya encendido y la lista solo con lo que falta (rec 427–603)'),
]

# ── Marcas: (cuadro, x, y del video, capa, rótulo) ──────────────────────────────────────────────────────────────────────────────────────
MARCAS = [
    (75, 585, 1266, 'cam1', 'la fila del domingo'),
    (120, 972, 1095, 'cam1', '«Asignar»'),
    (150, 544, 981, 'cam1b', 'la casilla de Gabriela'),
    (180, 871, 2191, 'cam1b', '«Asignar (1)»'),
    (240, 373, 2178, 'cam1b', '«Avisar a 1 persona»'),
    (300, 877, 1458, 'cam1b', '«Entendido»'),
    (375, 585, 768, 'cam2', 'la tarjeta «Tu próximo servicio»'),
    (600, 311, 1221, 'cam2b', '«Aceptar»'),
    (1140, 989, 398, 'camE1', '«Solo lo que falta» (escritorio, rec 422)'),
    (1440, 478, 1287, 'cam3', '«Way Maker» (rec 262)'),
    (1560, 304, 1839, 'cam3', '«Asistiré» (rec 428)'),
    (1680, 585, 2202, 'cam3', 'la caja de escribir (rec 601)'),
    (1740, 1086, 2214, 'cam3', '«Enviar» (rec 750)'),
    (1800, 1046, 2448, 'cam3', '«Servir» en la barra de abajo (rec 876)'),
    (1920, 585, 1242, 'cam3', 'la fila «Seguridad · Servicio General» (rec 1103: y 1266; se sube a 1242, dentro de la fila, para quedar sobre el nombre y no sobre el borde que oculta la fecha)'),
    (2040, 937, 1773, 'cam3b', '«No llegó» de Julián (rec 1307)'),
    (2160, 585, 2172, 'cam3b', '«Cerrar el turno» (rec 1479)'),
    (2340, 1017, 2418, 'cam4', '«Objetivos» en la barra de abajo (rec 1914)'),
]

# ── Sonidos: (cuadro del sonido = imagen + 1, archivo, acento, pista, volumen, nombre, comentario) ─────────────────────────────────────────
T_A = ('identidad/audio/toque.wav', 0.075)
T_B = ('assets/audio/toque-b.wav', 0.073)
T_C = ('assets/audio/toque-c.wav', 0.077)
AP = ('identidad/audio/aparicion.wav', 0.22)
CO = ('identidad/audio/confirmacion.wav', 0.32)
DE = ('identidad/audio/desliz.wav', 0.36)
SONIDOS = [
    # Parte 1 (los 18 del clip)
    (76, T_A, 0, 21, 1, 'toque', 'toque a en la fila del domingo (75)'),
    (121, T_C, 0, 21, 1, 'toque', 'toque c en «Asignar» (120)'),
    (151, T_A, 0, 21, 1, 'toque', 'toque a en la casilla de Gabriela (150)'),
    (181, T_B, 0, 21, 1, 'toque', 'toque b en «Asignar (1)» (180)'),
    (184, AP, 0, 22, 1, 'aparicion', 'Gabriela «Sin avisar» y la barra (183)'),
    (196, AP, 0, 22, 1, 'aparicion', 'la ceja «EQUIPOS» (195)'),
    (241, T_C, 0, 21, 1, 'toque', 'toque c en «Avisar a 1 persona» (240)'),
    (243, CO, 0.1, 24, 1, 'confirmacion', '«Avisados» (242)'),
    (301, T_A, 0, 21, 1, 'toque', 'toque a en «Entendido» (300)'),
    (304, AP, 0, 22, 1, 'aparicion', 'el puesto pasa a «Por confirmar» (303)'),
    (360, DE, 0.2, 23, 1.4, 'desliz', 'el látigo vertical de ida 356–366'),
    (376, T_B, 0, 21, 1, 'toque', 'toque b en la tarjeta «Tu próximo servicio» (375)'),
    (451, DE, 0.2, 23, 1, 'desliz', 'la app baja a «Instrucciones» (450)'),
    (541, DE, 0.2, 23, 1, 'desliz', 'la app vuelve arriba (540)'),
    (601, T_C, 0, 21, 1, 'toque', 'toque c en «Aceptar» (600)'),
    (603, CO, 0.1, 24, 1.4, 'confirmacion', '«¡Gracias por servir!» y «Confirmado» (602)'),
    (660, DE, 0.2, 23, 1.4, 'desliz', 'el látigo vertical de vuelta 656–666'),
    (662, CO, 0.1, 24, 1, 'confirmacion', 'Gabriela «Confirmado» en el turno del líder (661)'),
    # Parte 2 (SPEC §1.7, con los cuadros reales)
    (841, DE, 0.2, 23, 1.4, 'desliz', 'el látigo horizontal al escritorio (830–840)'),
    (901, DE, 0.2, 23, 1, 'desliz', 'la app baja a Seguridad (900)'),
    (1081, DE, 0.2, 23, 1, 'desliz', 'la app vuelve arriba (1080)'),
    (1141, T_A, 0, 21, 1, 'toque', 'toque a en «Solo lo que falta» (1140)'),
    (1144, AP, 0, 22, 1, 'aparicion', 'quedan solo los que les falta (1143)'),
    (1321, DE, 0.2, 23, 1.4, 'desliz', 'el látigo horizontal de vuelta (1310–1320)'),
    (1441, T_B, 0, 21, 1, 'toque', 'toque b en «Way Maker» (1440)'),
    (1501, DE, 0.2, 23, 1, 'desliz', 'la app baja al ensayo (1500)'),
    (1561, T_C, 0, 21, 1, 'toque', 'toque c en «Asistiré» (1560)'),
    (1564, AP, 0, 22, 1, 'aparicion', '«Asistiré» lleno y «Van 10» (1563)'),
    (1681, T_A, 0, 21, 1, 'toque', 'toque a en la caja de escribir (1680)'),
    (1741, T_B, 0, 21, 1, 'toque', 'toque b en «Enviar» (1740)'),
    (1744, AP, 0, 22, 1, 'aparicion', 'su mensaje en el hilo (1743)'),
    (1801, T_C, 0, 21, 1, 'toque', 'toque c en «Servir» (1800)'),
    (1921, T_A, 0, 21, 1, 'toque', 'toque a en la fila del turno (1920)'),
    (2041, T_B, 0, 21, 1, 'toque', 'toque b en «No llegó» (2040)'),
    (2161, T_C, 0, 21, 1, 'toque', 'toque c en «Cerrar el turno» (2160)'),
    (2176, CO, 0.1, 24, 1.4, 'confirmacion', '«1 persona cumplió su objetivo de servir en la ruta.» (2175)'),
    (2281, DE, 0.2, 23, 1.4, 'desliz', 'el látigo vertical a Gabriela (2270–2280)'),
    (2341, T_A, 0, 21, 1, 'toque', 'toque a en «Objetivos» (2340)'),
    (2356, CO, 0.1, 24, 1.4, 'confirmacion', 'el check de «Servir» se cierra (2355; rec 1936)'),
]

# ── Frases: (id, líneas, lugar, host desde, host hasta, entrada, salida, comentario) ─────────────────────────────────────────────────────
# líneas: lista de líneas; cada palabra es texto o ('em', texto). entrada: 'pulsos' (frase 1), 'linea' (frase 2) o 'palabras' (cada 2 cuadros
# desde el inicio del host: el host arranca un cuadro antes del pulso y la primera palabra se ve en el pulso). salida: cuadro absoluto o None.
FRASES = [
    ('frase-1', [['¿Quién', 'cubre'], ['el', 'domingo?']], 'cel', 0, 122, 'pulsos', 117,
     'P1 · «¿Quién cubre / el domingo?»: una palabra por pulso (0 · 15 · 30 · 45); sale 117–121'),
    ('frase-2', [['Kingdom', 'sugiere'], ['a', 'quién', 'poner']], 'cel', 119, 182, 'linea', 177,
     'P2 · «Kingdom sugiere / a quién poner»: la línea entera 120–126 (blur 8 → 0); sale 177–181'),
    ('frase-3', [['Y', 'sabe', 'a', 'qué'], ['hora', 'llegar']], 'cel', 359, 602, 'palabras', 597,
     'P4 · «Y sabe a qué / hora llegar»: palabra a palabra 360–370 con el látigo; sale 597–601'),
    ('frase-4', [['Y', 'el', 'domingo,'], ['completo.']], 'cel', 719, 842, 'palabras', 837,
     'P8 · «Y el domingo, / completo.»: 720 · 722 · 724 · 726 sobre «5 de 5»; sale 837–841 con el látigo horizontal'),
    ('frase-5', [['Lo', 'que', 'falta,', 'antes', 'del', 'domingo.']], 'esc', 842, 1321, 'palabras', 1317,
     'P9 · «Lo que falta, antes del domingo.» (una línea, arriba del escritorio): 843 · 845 · … · 853; sale 1317–1321 con el látigo de vuelta'),
    ('frase-6', [['Cada', 'equipo,'], ['con', 'su', 'chat.']], 'cel', 1321, 1802, 'palabras', 1797,
     'P10 · «Cada equipo, / con su chat.»: 1322 · 1324 · 1326 · 1328 · 1330; sale 1797–1801'),
    ('frase-7', [['Servir', 'cuenta.']], 'cel', 1801, 2282, 'palabras', 2277,
     'P11 · «Servir cuenta.» (una línea): 1802 · 1804; sale 2277–2281 con el látigo vertical'),
    ('frase-8', [['Y', 'da', 'un', 'paso'], ['en', 'su', 'ruta.']], 'cel', 2281, 2520, 'palabras', 2515,
     'P12 · «Y da un paso / en su ruta.»: 2282 · 2284 · … · 2294; sale 2515–2519'),
    ('frase-9', [['Que', 'cada', 'puesto'], ['de', 'servicio'], ['esté', ('em', 'cubierto')]], 'cel', 2519, 2760, 'palabras', None,
     'P13 · «Que cada puesto / de servicio / esté cubierto» (el título de Equipos en modulos.ts): 2520 · 2522 · … · 2532; «cubierto» en itálica dorada; quieta hasta el corte al cierre (2760)'),
]

def videos(lista, src, pista, sangria='                  '):
    out = []
    for vid, a, b, g, c in lista:
        out.append(f'{sangria}<!-- {c} -->')
        out.append(f'{sangria}<video id="{vid}" class="clip" src="{src}" muted playsinline data-track-index="{pista}"\n'
                   f'{sangria}  data-start="{s(a)}" data-duration="{s(b - a)}" data-media-start="{ms(g)}" data-playback-rate="1"></video>')
    return '\n'.join(out)

def marcas(capa, sangria='                  '):
    k = 'var(--e-k)' if capa == 'camE1' else 'var(--f-k)'
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
        out.append(f'      <div id="{fid}" data-composition-id="{fid}" data-composition-src="compositions/{fid}.html" data-track-kind="graphics"\n'
                   f'        data-start="{s(a)}" data-duration="{s(b - a)}" data-track-index="{pista}" data-width="1920" data-height="1080"></div>')
        pista = 2 if pista == 1 else 1
        if fid == 'frase-1':
            out.append('      <!-- La ceja «EQUIPOS» (host 194–2524): entra en el 195 en la columna izquierda; pasa arriba del escritorio (sale 837–840, entra '
                       '842–848), vuelve a la izquierda (sale 1317–1320, entra 1322–1328) y se va en 2520–2523 con la frase del sitio -->')
            out.append('      <div id="ceja" data-composition-id="ceja" data-composition-src="compositions/ceja.html" data-track-kind="graphics"\n'
                       f'        data-start="{s(194)}" data-duration="{s(2524 - 194)}" data-track-index="3" data-width="1920" data-height="1080"></div>')
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
        tw.append('          // «¿Quién» ya está en el cuadro 0 (la miniatura). Cada palabra arranca un cuadro antes de su pulso (15 · 30 · 45).')
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
    <!-- La ceja «EQUIPOS» (host 194–2524), con sus dos lugares (SPEC §1.4): en la columna izquierda del celular (x 120 · y 412) y arriba del
         escritorio (x 240 · y 92). Nunca se desliza con el látigo horizontal: sale con blur y entra en el otro lugar (entrada-linea: blur 8 → 0,
         6 cuadros, power4.out; salida-texto, 3 cuadros, power3.in). Inter 700, 28 px, mayúsculas, dorada (.k-feed-ceja con el tamaño de 16:9).
         En el látigo vertical (2270–2280) se queda quieta. Generada por _gen/gen.py. -->
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
        <div class="k-feed-ceja f-ceja" id="ceja-cel">Equipos</div>
        <div class="k-feed-ceja f-ceja" id="ceja-esc">Equipos</div>
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
          sale('#ceja-cel', 837); // 837–840, con el látigo al escritorio
          entra('#ceja-esc', 842); // 842–848, arriba del escritorio
          sale('#ceja-esc', 1317); // 1317–1320, con el látigo de vuelta
          entra('#ceja-cel', 1322); // 1322–1328, otra vez a la izquierda
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
    html = (tpl.replace('@@FRASES@@', hosts())
            .replace('@@M1A@@', videos(M1A, K, 10)).replace('@@M1A_MARCAS@@', marcas('cam1'))
            .replace('@@M1B@@', videos(M1B, K, 10, ' ' * 20)).replace('@@M1B_MARCAS@@', marcas('cam1b', ' ' * 20))
            .replace('@@M2A@@', videos(M2A, K, 12)).replace('@@M2A_MARCAS@@', marcas('cam2'))
            .replace('@@M2B@@', videos(M2B, K, 12, ' ' * 20)).replace('@@M2B_MARCAS@@', marcas('cam2b', ' ' * 20))
            .replace('@@C3A@@', videos(C3A, C, 14)).replace('@@C3A_MARCAS@@', marcas('cam3'))
            .replace('@@C3B@@', videos(C3B, C, 15, ' ' * 20)).replace('@@C3B_MARCAS@@', marcas('cam3b', ' ' * 20))
            .replace('@@C4@@', videos(C4, C, 17)).replace('@@C4_MARCAS@@', marcas('cam4'))
            .replace('@@E1@@', videos(E1, E, 18, ' ' * 14)).replace('@@E1_MARCAS@@', marcas('camE1', ' ' * 14))
            .replace('@@SONIDOS@@', sonidos())
            .replace('@@TOQUES@@', toques))
    assert '@@' not in html, 'quedó un marcador sin reemplazar'
    open(os.path.join(RAIZ, 'index.html'), 'w', encoding='utf8', newline='\n').write(html)
    comp = os.path.join(RAIZ, 'compositions')
    os.makedirs(comp, exist_ok=True)
    for f in FRASES:
        open(os.path.join(comp, f[0] + '.html'), 'w', encoding='utf8', newline='\n').write(frase(*f))
    open(os.path.join(comp, 'ceja.html'), 'w', encoding='utf8', newline='\n').write(CEJA.replace('@@DUR@@', s(2524 - 194)))
    print('ok: index.html, frase-1..9 y ceja')

main()
