# Genera index.html del clip de Mi iglesia (4:5) desde index.tpl.html y las tablas de abajo (tramos de video, stills, marcas de toque
# y sonidos). Cuadros del clip a 30 fps; «grab.» = cuadro de assets/grabaciones/grabacion.mp4. La cámara, el iris y las marcas viven en el
# <script> de la plantilla. Uso, desde la raíz del proyecto:
#   python _gen/gen.py index.html _gen/index.tpl.html
import sys
OUT, TPL = sys.argv[1], sys.argv[2]

def s(n):  # cuadro -> segundos
    return f'{n / 30:.6f}'.rstrip('0').rstrip('.')

# (desde, hasta, grab, comentario, dentro_del_iris)
TRAMOS = [
    (0, 60, 0, 'Mi iglesia arriba (grab. 0–59): la barra «Kingdom Demo», «Buenas tardes, Gabriela», «Mis servicios», «Mis Equipos»', 0),
    (60, 105, 96, 'la app baja a la novedad en un cuadro (grab. 96, salto real del `ver`): «Inscripciones abiertas · hace 3 minutos» con la tarjeta del congreso', 0),
    (105, 107, 180, 'toque en la flecha de las reacciones (grab. 180)', 0),
    (107, 120, 186, 'corte en la espera (182→186, quieta): el selector ya abierto en el 107 (grab. 186)', 0),
    (120, 122, 245, 'toque en «Amén» (grab. 245)', 0),
    (122, 180, 251, 'corte en la espera (247→251, quieta): «🙌 Amén» puesto y 57 en el 122; el 🙌 salta 125–134 (grab. 254–263)', 0),
    (181, 200, 437, 'el evento ya cargado (grab. 437; la K del cargador 371–430 queda fuera) con la entrada propia de la app 181–187', 1),
    (200, 300, 447, 'quieto (grab. 447–546; el corte del 200 cae en la pantalla quieta, 445+)', 1),
    (300, 301, 547, 'la app baja a «Inscripción» en un cuadro (grab. 547, salto real de 62 px CSS)', 1),
    (301, 375, 557, 'quieta (grab. 557–630; 548–556 iguales)', 1),
    (375, 377, 631, 'toque en «Inscribirme» (grab. 631–632)', 1),
    (377, 389, 638, 'corte en la onda (633→638): «¿A quiénes inscribes? (hasta 4)» y «Yo» entran 377–386 (grab. 638–649)', 1),
    (420, 450, 710, 'toque en la casilla del esposo: se marca 420–422 (grab. 710–739)', 1),
    (450, 452, 754, 'toque en «Seguir» (grab. 754–755)', 1),
    (452, 464, 761, 'corte en la onda (756→761): «1 de 2: Tú» entra 452–461 (grab. 761–772)', 1),
    (464, 480, 854, 'la app centró el formulario (grab. 814, salto de 136 px CSS): la cámara lo compensa en el 464, no se ve (grab. 854–869)', 1),
    (480, 481, 870, 'toque en «M» (grab. 870)', 1),
    (481, 495, 872, 'el radio se llena desde el 481 (grab. 872–885; 871 igual)', 1),
    (495, 496, 902, 'toque en «Sí» (grab. 902)', 1),
    (496, 510, 904, 'el radio se llena desde el 496 (grab. 904–917; 903 igual)', 1),
    (510, 512, 945, 'toque en «Seguir» (grab. 945–946)', 1),
    (512, 540, 952, 'corte en la onda (947→952): «2 de 2: Simón Ríos Arango» con los radios vacíos en el 512 (grab. 952–979)', 1),
    (540, 541, 999, 'toque en «L» (grab. 999)', 1),
    (541, 555, 1002, 'el radio se llena desde el 541 (grab. 1002–1015; 1000–1001 iguales)', 1),
    (555, 556, 1032, 'toque en «No» (grab. 1032)', 1),
    (556, 600, 1034, 'el radio se llena desde el 556 (grab. 1034–1077; 1033 igual)', 1),
    (600, 602, 1090, 'toque en «Inscribir» (grab. 1090–1091)', 1),
    (602, 645, 1111, 'corte en la espera y la K del cargador (1092→1111): el sello, el confeti real y «¡Quedaste inscrito!» con las dos filas «Inscrito» (grab. 1111–1153, confeti 1111–1151 a 1×)', 1),
    (660, 662, 1259, 'toque en «Ver boleta» (grab. 1259–1260)', 1),
    (662, 720, 1281, 'corte en la espera (1261→1281, la carga de «Mis boletas» queda fuera): la boleta con su QR y «Código FM75UZ»; entra 1,03 → 1,00', 1),
    (720, 722, 1398, 'toque en el QR (grab. 1398–1399)', 1),
    (722, 840, 1405, 'corte en la espera (1400→1405, quieta): la boleta a pantalla completa entra con su propia animación 722–728 (grab. 1405–1522)', 1),
]
STILLS = [  # (desde, hasta, grab, comentario, dentro_del_iris)
    (389, 420, 705, 'la app bajó 200 px CSS (grab. 701–704, el `scrollIntoView` antes de marcar): still de la grab. 705 (705–709 quietas), compensado por la cámara en el 389; la cámara baja a la lista 390–403', 1),
    (645, 660, 1258, 'la app bajó 84 px CSS (grab. 1257, el `scrollIntoView` antes de «Ver boleta»): still de la grab. 1258, compensado por la cámara en el 645; la cámara baja a «Ver boleta» 646–658', 1),
]
# toques[] de pasos.json en px del video: (cuadro del clip, x, y, nombre)
TOQUES = [
    (105, 543, 1744, 'la flecha de las reacciones'), (120, 792, 1559, '«Amén»'),
    (375, 585, 2112, '«Inscribirme»'), (420, 357, 1980, 'la casilla del esposo'), (450, 936, 2136, '«Seguir»'),
    (480, 181, 1380, '«M»'), (495, 181, 1860, '«Sí»'), (510, 936, 2136, '«Seguir»'), (540, 174, 1500, '«L»'), (555, 191, 1980, '«No»'),
    (600, 919, 2136, '«Inscribir»'), (660, 477, 2112, '«Ver boleta»'), (720, 585, 1251, 'el QR'),
]
# Sonidos: (cuadro del sonido, archivo, duración, acento, volumen, pista, comentario)
T = {'a': ('identidad/audio/toque.wav', 0.075), 'b': ('assets/audio/toque-b.wav', 0.073), 'c': ('assets/audio/toque-c.wav', 0.077)}
SON = []
def toque(n, tk, vol, com, clave=False):
    f, d = T[tk]
    SON.append((n, f, d, 0, vol, 21, f'toque {tk} en {com}' + (' (clave; 1,0: ver REVIEW §5)' if clave else ''), f'toque-{n - 1}'))
def otro(n, nombre, vol, com):
    f = {'aparicion': ('identidad/audio/aparicion.wav', 0.22, 0, 22), 'desliz': ('identidad/audio/desliz.wav', 0.36, 0.2, 23),
         'confirmacion': ('identidad/audio/confirmacion.wav', 0.32, 0.1, 24)}[nombre]
    SON.append((n, f[0], f[1], f[2], vol, f[3], com, f'{nombre}-{n - 1}'))
otro(61, 'desliz', 1, 'la app baja a la novedad (60); acento 0,2')
toque(106, 'a', 1, 'la flecha de las reacciones')
otro(108, 'aparicion', 1, 'el selector abierto (107)')
toque(121, 'c', 1, '«Amén», con el bajo', True)
otro(123, 'aparicion', 1.4, '«🙌 Amén» puesto y el total en 57 (122)')
toque(181, 'b', 1, '«Inscribirme», con el pico (el iris)', True)
otro(196, 'aparicion', 1, 'la ceja «MI IGLESIA» (195)')
otro(301, 'desliz', 1, 'la app baja a «Inscripción» (300); acento 0,2')
toque(376, 'a', 1, '«Inscribirme»')
toque(421, 'b', 1, 'la casilla del esposo')
toque(451, 'c', 1, '«Seguir»')
toque(481, 'a', 1, '«M»')
toque(496, 'b', 1, '«Sí»')
toque(511, 'c', 1, '«Seguir»')
toque(541, 'a', 1, '«L»')
toque(556, 'b', 1, '«No»')
toque(601, 'c', 1, '«Inscribir», con la segunda subida', True)
otro(603, 'confirmacion', 1.4, 'el sello y «¡Quedaste inscrito!» (602); acento 0,1')
toque(661, 'a', 1, '«Ver boleta», con el golpe', True)
otro(663, 'confirmacion', 1, '«Mis boletas» con el QR (662); acento 0,1')
toque(721, 'b', 1, 'el QR')
otro(723, 'aparicion', 1, 'la boleta a pantalla completa (722)')

ind = '                '
def video(i, d, h, g, com, pad):
    return (f'{pad}<!-- {d}–{h} · {com} -->\n'
            f'{pad}<video data-hf-id="hf-mv{i:02d}" id="v{i:02d}" class="clip" src="assets/grabaciones/grabacion.mp4" muted playsinline data-track-index="10"\n'
            f'{pad}  data-start="{s(d)}" data-duration="{s(h - d)}" data-media-start="{(g / 30 + 0.01):.6f}" data-playback-rate="1"></video>\n')
def still(d, h, g, com, pad):
    return (f'{pad}<!-- {d}–{h} · {com} -->\n'
            f'{pad}<img data-hf-id="hf-ms{g}" id="still{g}" class="clip" src="assets/stills/still-{g}.png" alt="" data-track-index="11"\n'
            f'{pad}  data-start="{s(d)}" data-duration="{s(h - d)}" />\n')
items = [('v', t) for t in TRAMOS] + [('s', t) for t in STILLS]
items.sort(key=lambda x: x[1][0])
fuera, dentro = '', ''
vi = 0
for k, t in items:
    pad = ind if not t[4] else ind + '  '
    if k == 'v':
        vi += 1
        txt = video(vi, t[0], t[1], t[2], t[3], pad)
    else:
        txt = still(t[0], t[1], t[2], t[3], pad)
    if t[4]: dentro += txt
    else: fuera += txt
marcas = ''
for n, x, y, nom in TOQUES:
    marcas += (f'{ind}<!-- {n} · {nom} -->\n'
               f'{ind}<div data-hf-id="hf-mtq{n}" class="toque" id="tq-{n}" style="left: calc({x}px * var(--f-k)); top: calc({y}px * var(--f-k))"></div>\n'
               f'{ind}<div data-hf-id="hf-mon{n}" class="onda" id="on-{n}" style="left: calc({x}px * var(--f-k)); top: calc({y}px * var(--f-k))"></div>\n')
sonidos = ''
for n, f, d, ac, vol, tr, com, sid in SON:
    start = n / 30 - ac
    sonidos += (f'      <!-- {n} · {com} -->\n'
                f'      <audio data-hf-id="hf-msnd-{sid}" id="snd-{sid}" src="{f}" data-start="{start:.6f}" data-duration="{d}" data-track-index="{tr}" data-volume="{vol}"></audio>\n')

tpl = open(TPL, encoding='utf-8').read()
for k, v in (('@@FUERA@@\n', fuera), ('@@DENTRO@@\n', dentro), ('@@MARCAS@@\n', marcas), ('@@SONIDOS@@\n', sonidos)):
    assert k in tpl, k
    tpl = tpl.replace(k, v)
open(OUT, 'w', encoding='utf-8', newline='\n').write(tpl)
print('ok', vi, 'videos', len(SON), 'sonidos')
