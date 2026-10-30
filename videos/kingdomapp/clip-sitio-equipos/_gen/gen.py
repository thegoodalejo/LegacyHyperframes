# Genera index.html del clip de Equipos (4:5). Tabla de tramos, marcas y sonidos -> HTML.
import sys
OUT = sys.argv[1]
FPS = 30
def s(n): return f"{n / FPS:.6f}".rstrip('0').rstrip('.')
def ms(g): return f"{g / FPS + 0.01:.6f}".rstrip('0').rstrip('.')

# (id, desde, hasta, grab, comentario)
M1A = [  # cam1: antes del iris del 120
    ('v01', 0, 78, 81, '0–78 · el calendario de Seguridad ya desplazado al primer domingo (grab. 81–158; el desplazamiento real es la grab. 41); toque en la fila del domingo en el 75 (grab. 156)'),
    ('v02', 78, 120, 169, '78–120 · match cut sobre el toque: el turno ya cargado (grab. 169–210; el esqueleto 163–168 queda fuera); entra 1,03 → 1,00'),
    ('v03', 120, 121, 362, '120 · toque en «Asignar» (grab. 362); el iris nace aquí'),
]
M1B = [  # cam1b: dentro del iris del 120 y la vuelta del 656
    ('v04', 121, 150, 379, '121–150 · el diálogo «Asignar · Parqueadero» ya puesto, con la lista sugerida (grab. 379–407; el fundido y el esqueleto 363–378 quedan fuera)'),
    ('v05', 150, 151, 463, '150 · toque en la casilla de Gabriela (grab. 463; corte en el diálogo quieto 408→463)'),
    ('v06', 151, 180, 470, '151–180 · corte en la onda (464→470): la fila de Gabriela ya llena y «Asignar (1)» (grab. 470–498)'),
    ('v07', 180, 181, 524, '180 · toque en «Asignar (1)» (grab. 524; corte en el diálogo quieto 499→524)'),
    ('v08', 181, 183, 539, '181–183 · corte en la espera (525→539): el diálogo ya se fue, el puesto todavía «Vacante» (grab. 539–540)'),
    ('v09', 183, 240, 542, '183–240 · Gabriela «Sin avisar» y la barra «1 asignación sin avisar · Avisar a 1 persona» (grab. 542–598)'),
    ('v10', 240, 242, 689, '240–242 · toque en «Avisar a 1 persona» (grab. 689–690)'),
    ('v11', 242, 300, 717, '242–300 · corte en la espera y la K del cargador (691→717): «Avisados» entero (grab. 717–774)'),
    ('v12', 300, 301, 805, '300 · toque en «Entendido» (grab. 805)'),
    ('v13', 301, 303, 815, '301–303 · corte en el fundido del diálogo (806→815): el diálogo ya se fue, todavía «Sin avisar» (grab. 815–816)'),
    ('v14', 303, 367, 819, '303–367 · el turno recargado: Gabriela «Por confirmar» y sin la barra (grab. 819–882); el látigo se lo lleva en 356–366'),
    ('v15', 656, 840, 1660, '656–840 · el látigo de vuelta: el turno del líder recién abierto (grab. 1660–1843; el cambio de cuenta 1609–1647 queda fuera): Gabriela «Confirmado», «5 de 5»'),
]
M2A = [
    ('w01', 356, 375, 1113, '356–375 · Mi iglesia de Gabriela con «Tu próximo servicio» (grab. 1113–1131; el cambio de cuenta 910–993 queda fuera)'),
    ('w02', 375, 376, 1132, '375 · toque en la tarjeta (grab. 1132); el iris nace aquí'),
]
M2B = [
    ('w03', 376, 450, 1144, '376–450 · corte en la espera (1133→1144, el esqueleto fuera): su servicio, «Llega a las 7:45 a. m.», «Por confirmar» (grab. 1144–1217)'),
    ('w04', 450, 540, 1270, '450–540 · la app baja a «Instrucciones» en un cuadro (grab. 1270, salto real): lugar, vestimenta, colores y cronograma (grab. 1270–1359)'),
    ('w05', 540, 600, 1392, '540–600 · la app vuelve arriba en un cuadro (grab. 1392, salto real): «Aceptar · No puedo» (grab. 1392–1451)'),
    ('w06', 600, 602, 1469, '600–602 · toque en «Aceptar» (grab. 1469–1470)'),
    ('w07', 602, 667, 1484, '602–667 · corte en la espera (1471→1484; quedan fuera los botones apagados y el aviso de guardado sin señal de 1477): «¡Gracias por servir! Tu líder ya lo sabe.», «Confirmado», «Ya no puedo» (grab. 1484–1548)'),
]

# Marcas: (cuadro, x, y del video, capa, rótulo)
MARCAS = [
    (75, 585, 1266, 'cam1', 'la fila del domingo'),
    (120, 972, 1095, 'cam1', '«Asignar»'),
    (150, 544, 981, 'cam1b', 'la casilla de Gabriela'),
    (180, 871, 2191, 'cam1b', '«Asignar (1)»'),
    (240, 373, 2178, 'cam1b', '«Avisar a 1 persona»'),
    (300, 877, 1458, 'cam1b', '«Entendido»'),
    (375, 585, 768, 'cam2', 'la tarjeta «Tu próximo servicio»'),
    (600, 311, 1221, 'cam2b', '«Aceptar»'),
]

# Sonidos: (cuadro del acento, archivo, dur, acento, pista, volumen, comentario)
T_A = ('identidad/audio/toque.wav', 0.075)
T_B = ('assets/audio/toque-b.wav', 0.073)
T_C = ('assets/audio/toque-c.wav', 0.077)
AP = ('identidad/audio/aparicion.wav', 0.22)
CO = ('identidad/audio/confirmacion.wav', 0.32)
DE = ('identidad/audio/desliz.wav', 0.36)
SONIDOS = [
    (76, T_A, 0, 21, 1, 'toque', 'toque a en la fila del domingo (75)'),
    (121, T_C, 0, 21, 1, 'toque', 'toque c en «Asignar» (clave; 1,0 como en Eventos), con el bajo'),
    (151, T_A, 0, 21, 1, 'toque', 'toque a en la casilla de Gabriela (150)'),
    (181, T_B, 0, 21, 1, 'toque', 'toque b en «Asignar (1)» (clave; 1,0), con el pico'),
    (184, AP, 0, 22, 1, 'aparicion', 'Gabriela «Sin avisar» y la barra «Avisar a 1 persona» (183)'),
    (196, AP, 0, 22, 1, 'aparicion', 'la ceja «EQUIPOS» (195)'),
    (241, T_C, 0, 21, 1, 'toque', 'toque c en «Avisar a 1 persona» (240)'),
    (243, CO, 0.1, 24, 1, 'confirmacion', '«Avisados» (242); acento 0,1'),
    (301, T_A, 0, 21, 1, 'toque', 'toque a en «Entendido» (300)'),
    (304, AP, 0, 22, 1, 'aparicion', 'el puesto pasa a «Por confirmar» (303)'),
    (360, DE, 0.2, 23, 1.4, 'desliz', 'el látigo de ida 356–366 (acento 0,2 en el 360)'),
    (376, T_B, 0, 21, 1, 'toque', 'toque b en la tarjeta «Tu próximo servicio» (375)'),
    (451, DE, 0.2, 23, 1, 'desliz', 'la app baja a «Instrucciones» (450); acento 0,2'),
    (541, DE, 0.2, 23, 1, 'desliz', 'la app vuelve arriba (540); acento 0,2'),
    (601, T_C, 0, 21, 1, 'toque', 'toque c en «Aceptar» (clave; 1,0), con la segunda subida'),
    (603, CO, 0.1, 24, 1.4, 'confirmacion', '«¡Gracias por servir! Tu líder ya lo sabe.» y «Confirmado» (602); acento 0,1'),
    (660, DE, 0.2, 23, 1.4, 'desliz', 'el látigo de vuelta 656–666 (acento 0,2 en el 660)'),
    (662, CO, 0.1, 24, 1, 'confirmacion', 'Gabriela «Confirmado» en el turno del líder: su fila entra entera en la ventana en el 661, con el látigo de vuelta; acento 0,1'),
]

def videos(lista, pista):
    out = []
    for vid, a, b, g, c in lista:
        out.append(f'              <!-- {c} -->')
        out.append(f'              <video id="{vid}" class="clip" src="assets/grabaciones/grabacion.mp4" muted playsinline data-track-index="{pista}"\n'
                   f'                data-start="{s(a)}" data-duration="{s(b - a)}" data-media-start="{ms(g)}" data-playback-rate="1"></video>')
    return '\n'.join(out)

def marcas(capa):
    out = ['              <div class="marcas">']
    for n, x, y, c, r in MARCAS:
        if c != capa: continue
        out.append(f'                <!-- {n} · {r} (toques[] de pasos.json, px del video × --f-k) -->')
        st = f'left: calc({x}px * var(--f-k)); top: calc({y}px * var(--f-k))'
        out.append(f'                <div class="toque" id="tq-{n}" style="{st}"></div>')
        out.append(f'                <div class="onda" id="on-{n}" style="{st}"></div>')
    out.append('              </div>')
    return '\n'.join(out)

def sonidos():
    out = []
    for n, (src, dur), acento, pista, vol, nombre, c in SONIDOS:
        start = n / FPS - acento
        out.append(f'      <!-- {n} · {c} -->')
        out.append(f'      <audio id="snd-{nombre}-{n}" src="{src}" data-start="{s(start * FPS)}" data-duration="{dur}" data-track-index="{pista}" data-volume="{vol}"></audio>')
    return '\n'.join(out)

tpl = open(sys.argv[2], encoding='utf8').read()
html = (tpl.replace('@@M1A@@', videos(M1A, 10)).replace('@@M1A_MARCAS@@', marcas('cam1'))
        .replace('@@M1B@@', videos(M1B, 10)).replace('@@M1B_MARCAS@@', marcas('cam1b'))
        .replace('@@M2A@@', videos(M2A, 12)).replace('@@M2A_MARCAS@@', marcas('cam2'))
        .replace('@@M2B@@', videos(M2B, 12)).replace('@@M2B_MARCAS@@', marcas('cam2b'))
        .replace('@@SONIDOS@@', sonidos()))
open(OUT, 'w', encoding='utf8', newline='\n').write(html)
print('ok')
