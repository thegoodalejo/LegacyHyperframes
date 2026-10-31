# Genera index.html y compositions/texto-*.html de «Kingdom en un minuto» (16:9) desde index.tpl.html y estas tablas.
#   python _gen/gen.py            (desde clip-sitio-en-un-minuto/)
# Cada módulo es una VENTANA del tramo de su clip (clip-sitio-<modulo>), con los tramos de video, las cámaras, las marcas de toque y los
# sonidos del recorrido 16:9 del mismo módulo (recorrido-<modulo>/_gen), recortados a la ventana y corridos `off` cuadros. Todos los
# corrimientos son múltiplos de 60 (un compás): los pulsos del clip siguen cayendo en pulsos, y los toques clave en los golpes medidos.
# Cuadros a 30 fps; «clip» = cuadro del clip (y de la parte 1 de su recorrido); «grab.» = cuadro de la grabación.
import os

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
FPS = 30
K = 720 / 1170  # px del video del celular → px de la ventana ajustada al ancho (= --f-k)


def num(v):
    return f"{v:.6f}".rstrip('0').rstrip('.')


def s(n):
    return num(n / FPS)


def R(rec):  # cuadro de la grabación → segundos de media (+0,01 s: cae dentro del cuadro buscado)
    return rec / FPS + 0.01


# ── Los seis módulos ───────────────────────────────────────────────────────────────────────────────────────────────────────────────
# tramos: (id, clip desde, clip hasta, media en segundos en «desde», tasa, cámara, comentario)
# cam:    las cámaras del módulo: {selector: (encuadre inicial, [(clip, 'set'|'mover', encuadre, duración en cuadros)])}
# marcas: (clip, x, y del video, cámara, corte (cuadro del clip en que cambia la pantalla) o None, rótulo)
# sonidos: (clip del sonido = imagen + 1, tipo, volumen, comentario)
MOD = [
    dict(
        n=1, clave='mem', nombre='Membresía', src='assets/grabaciones/membresia.mp4', ini=540, fin=720, off=-420, pre=12,
        lineas=[['Cada', 'persona,'], ['acompañada.']],
        com='Membresía (clip 540–720 → 120–300): «Muy contenta, viene el domingo», «Marcar cumplido» y «Llamada de bienvenida cumplido · '
            'Ahora va en: Mensaje de bienvenida». El toque cae en el pico del 180 y el punch en el 240',
        tramos=[
            ('m21', 495, 567, 86.043333, 1.138889, 'c1', 'clip 495–567 · «Muy contenta, viene el domingo» (grab. 2581–2663), a 1,139×'),
            ('m22', 567, 600, 91.143333, 1, 'c1', 'clip 567–600 · hasta el toque en «Marcar cumplido» del diálogo (grab. 2767)'),
            ('m23', 600, 603, 92.243333, 1, 'c1', 'clip 600–603 · el toque'),
            ('m24', 603, 700, 93.243333, 1, 'c1', 'clip 603–700 · «cumplido · Ahora va en: Mensaje de bienvenida»'),
            ('m25', 700, 785, 97.076667, 1, 'c1', 'clip 700–785 · «Listo» y la tarjeta (el corte del 720 se la lleva antes)'),
        ],
        cam={'#c1': ('E1.observaciones', [(570, 'mover', 'E1.botones', 14), (600, 'mover', 'E1.resultado', 14),
                                          (660, 'mover', 'E1.ahora', 9)])},
        marcas=[(600, 808, 2088, 'c1', 603, '«Marcar cumplido» del diálogo')],
        sonidos=[(601, 'toque', 1, '«Marcar cumplido» del diálogo, con el pico'), (603, 'confirmacion', 1.4, '«cumplido · Ahora va en…»')],
    ),
    dict(
        n=2, clave='eve', nombre='Eventos', src='assets/grabaciones/eventos.mp4', ini=540, fin=720, off=-240, pre=12,
        lineas=[['Cada', 'reunión,'], ['reportada.']],
        com='Eventos (clip 540–720 → 300–480): «Total: 10 personas», «Guardar asistencia», el reporte y «¡Listo!» con «Reportada»',
        tramos=[
            ('e22', 525, 540, R(925), 1, 'c2', 'clip 525–540 · la app ya bajó 62 px CSS (grab. 919, compensado): la misma pantalla que e23; solo se ve en el látigo de entrada'),
            ('e23', 540, 602, R(947), 1, 'c2', 'clip 540–602 · quieta; toque en «Guardar asistencia» en el 600 (grab. 1007)'),
            ('e24', 609, 615, R(1029), 1, 'c2', 'clip 609–615 · la barra crece 15 → 66 % (grab. 1030–1034)'),
            ('e25', 615, 617, R(1154), 1, 'c2', 'clip 615–617 · la app subió 66 px CSS (compensado); toque en «Muy bien»'),
            ('e26', 617, 622, R(1160), 1, 'c2', 'clip 617–622 · el radio se llena'),
            ('e27', 622, 632, R(1195), 1, 'c2', 'clip 622–632 · toque en «Tema de la palabra» en el 630'),
            ('e28', 632, 645, R(1213), 1.5, 'c2', 'clip 632–645 · «El perdón» a 1,5×'),
            ('e29', 645, 662, R(1293), 1, 'c2', 'clip 645–662 · la app bajó 66 px (compensado); toque en «Enviar reporte» en el 660'),
            ('e30', 662, 780, R(1328), 1, 'c2', 'clip 662–780 · «¡Listo!» con «10 personas.» y «Reportada»'),
        ],
        stills=[('st-e1027', 602, 609, 'assets/stills/eventos-1027.png', 'c2', 'clip 602–609 · still de la grab. 1027: el paso ② con la barra al 15 %')],
        cam={'#c2': ('E2.botones', [(600, 'mover', 'E2.formulario', 9), (615, 'set', 'comp(E2.formulario, 66)', 0),
                                    (645, 'set', 'E2.formulario', 0), (646, 'mover', 'E2.enviar', 13), (660, 'mover', 'E2.listo', 14),
                                    (690, 'mover', 'E2.tarjeta', 9)])},
        marcas=[(600, 337, 2184, 'c2', 602, '«Guardar asistencia»'), (615, 251, 1188, 'c2', None, '«Muy bien»'),
                (630, 585, 1608, 'c2', None, '«Tema de la palabra»'), (660, 880, 2184, 'c2', 662, '«Enviar reporte»')],
        sonidos=[(601, 'toque', 1, '«Guardar asistencia»'), (603, 'confirmacion', 1, 'el paso ② «Reporte»'), (616, 'toque', 1, '«Muy bien»'),
                 (631, 'toque', 1, '«Tema de la palabra»'), (661, 'toque', 1, '«Enviar reporte»'), (663, 'confirmacion', 1.4, '«¡Listo!»')],
    ),
    dict(
        n=3, clave='aca', nombre='Academia', src='assets/grabaciones/academia.mp4', ini=0, fin=240, off=480,
        lineas=[['Cada', 'clase,'], ['sin', 'papel.']],
        com='Academia (clip 0–240 → 480–720): el profesor muestra 3 5 9 8; látigo vertical a la alumna; los cuatro números, uno por pulso; '
            '«¡Listo! Quedó tu asistencia» en el 660',
        tramos=[
            ('a01', 0, 120, R(0), 1, 'c3a', 'clip 0–120 · el profesor (grab. 0–119): 3 5 9 8, la barra, el QR y «13 de 18 marcaron»'),
            ('a07', 100, 120, R(444), 1, 'c3b', 'clip 100–120 · la alumna: las cuatro casillas vacías; llega con el látigo del 110–120'),
            ('a08', 120, 135, R(464), 1, 'c3b', 'clip 120–135 · el «3»'),
            ('a09', 135, 150, R(508), 1, 'c3b', 'clip 135–150 · el «5»'),
            ('a10', 150, 165, R(552), 1, 'c3b', 'clip 150–165 · el «9»'),
            ('a11', 165, 180, R(600), 1, 'c3b', 'clip 165–180 · el «8» y «Enviando…»'),
            ('a12', 180, 245, R(626), 1, 'c3b', 'clip 180–245 · «¡Listo! Quedó tu asistencia»'),
        ],
        stills=[('st-a0', -3, 0, 'assets/stills/academia-0.png', 'c3a',
                 'el primer cuadro de la grabación (grab. 0) en 477–480, dentro del iris que arranca en el 479 (el clip empieza en su cuadro 0)')],
        cam={'#c3a': ('E3.codigo', [(60, 'mover', 'E3.contador', 14)]),
             '#c3b': ('E3.casillas', [(180, 'mover', 'E3.listo', 14)])},
        marcas=[],
        sonidos=[(120, 'desliz', 1, 'el látigo vertical a la alumna (110–120)'), (121, 'aparicion', 1, 'el «3»'),
                 (136, 'aparicion', 1, 'el «5»'), (151, 'aparicion', 1, 'el «9»'), (166, 'aparicion', 1, 'el «8»'),
                 (181, 'confirmacion', 1.4, '«¡Listo! Quedó tu asistencia»')],
    ),
    dict(
        n=4, clave='mig', nombre='Mi iglesia', src='assets/grabaciones/mi-iglesia.mp4', ini=540, fin=780, off=180, pre=12,
        lineas=[['Cada', 'miembro,'], ['con', 'su', 'boleta.']],
        com='Mi iglesia (clip 540–780 → 720–960): la inscripción de Simón, «Inscribir», «¡Quedaste inscrito!», «Ver boleta» y la boleta con '
            'su QR a pantalla completa',
        tramos=[
            ('k22', 512, 540, R(952), 1, 'c4', 'clip 512–540 · «2 de 2: Simón Ríos Arango» con los radios vacíos; solo se ve en el látigo de entrada'),
            ('k23', 540, 541, R(999), 1, 'c4', 'clip 540 · toque en «L» (grab. 999)'),
            ('k24', 541, 555, R(1002), 1, 'c4', 'clip 541–555 · el radio se llena'),
            ('k25', 555, 556, R(1032), 1, 'c4', 'clip 555 · toque en «No»'),
            ('k26', 556, 600, R(1034), 1, 'c4', 'clip 556–600 · el radio se llena'),
            ('k27', 600, 602, R(1090), 1, 'c4', 'clip 600–602 · toque en «Inscribir»'),
            ('k28', 602, 645, R(1111), 1, 'c4', 'clip 602–645 · el sello, el confeti y «¡Quedaste inscrito!» con las dos filas «Inscrito»'),
            ('k29', 660, 662, R(1259), 1, 'c4', 'clip 660–662 · toque en «Ver boleta»'),
            ('k30', 662, 720, R(1281), 1, 'c4', 'clip 662–720 · la boleta con su QR y «Código FM75UZ»; entra 1,03 → 1,00'),
            ('k31', 720, 722, R(1398), 1, 'c4', 'clip 720–722 · toque en el QR'),
            ('k32', 722, 841, R(1405), 1, 'c4', 'clip 722–841 · la boleta a pantalla completa'),
        ],
        stills=[('st-k1258', 645, 660, 'assets/stills/mi-iglesia-1258.png', 'c4',
                 'clip 645–660 · still de la grab. 1258 (la app bajó 84 px antes de «Ver boleta», compensado por la cámara)')],
        cam={'#c4': ('E4.form', [(570, 'mover', 'E4.botonesForm', 14), (600, 'mover', 'E4.resultado', 14),
                                 (645, 'set', 'comp(E4.resultado, -84)', 0), (646, 'mover', 'E4.verBoleta', 13),
                                 (662, 'set', 'E4.boleta', 0), (690, 'mover', 'E4.qr', 9), (720, 'mover', 'E4.grande', 14)])},
        marcas=[(555, 191, 1980, 'c4', None, '«No»'), (600, 919, 2136, 'c4', 602, '«Inscribir»'),
                (660, 477, 2112, 'c4', 662, '«Ver boleta»'), (720, 585, 1251, 'c4', 722, 'el QR')],
        sonidos=[(556, 'toque', 1, '«No»'), (601, 'toque', 1, '«Inscribir»'), (603, 'confirmacion', 1.4, '«¡Quedaste inscrito!»'),
                 (661, 'toque', 1, '«Ver boleta»'), (663, 'confirmacion', 1, '«Mis boletas» con el QR'), (721, 'toque', 1, 'el QR'),
                 (723, 'aparicion', 1, 'la boleta a pantalla completa')],
    ),
    dict(
        n=5, clave='com', nombre='Comunicaciones', src='assets/grabaciones/comunicaciones.mp4', ini=540, fin=780, off=420,
        lineas=[['Cada', 'aviso,'], ['con', 'su', 'respuesta.']],
        com='Comunicaciones (clip 540–780 → 960–1200): la invitación, su reporte (137 entregados, 115 leídos, 23 respondieron) y los nombres '
            'con «Leído» y «Allí estaré»',
        tramos=[
            ('v15', 510, 602, R(1098), 1, 'c5', 'clip 510–602 · la tarjeta de la invitación quieta; toque en el 600 (grab. 1188)'),
            ('v16', 602, 630, R(1202), 1, 'c5', 'clip 602–630 · el reporte con sus números'),
            ('v17', 630, 661, R(1299), 1, 'c5', 'clip 630–661 · quieta; toque en «respondieron» en el 660'),
            ('v18', 661, 675, R(1335), 1, 'c5', 'clip 661–675 · el contorno de «respondieron»'),
            ('v19', 675, 841, R(1396), 1, 'c5', 'clip 675–841 · los nombres: «Destinatarios (23)», «Leído» y «Allí estaré»'),
        ],
        cam={'#c5': ('E5.tarjeta', [(602, 'set', 'E5.kpis', 0), (690, 'mover', 'E5.nombres', 14), (720, 'mover', 'E5.cierre', 14)])},
        marcas=[(600, 585, 1857, 'c5', 602, 'la invitación'), (660, 311, 1944, 'c5', None, '«respondieron»')],
        sonidos=[(601, 'toque', 1, 'la invitación'), (603, 'confirmacion', 1, 'el reporte con sus números'),
                 (661, 'toque', 1, '«respondieron», con el golpe'), (676, 'confirmacion', 1.4, 'los nombres con «Leído» y «Allí estaré»')],
    ),
    dict(
        n=6, clave='equ', nombre='Equipos', src='assets/grabaciones/equipos.mp4', ini=540, fin=780, off=660,
        lineas=[['Cada', 'puesto,'], ['cubierto.']],
        com='Equipos (clip 540–780 → 1200–1440): Gabriela acepta el turno, «¡Gracias por servir! Tu líder ya lo sabe.», y el látigo '
            'vertical al líder: Gabriela «Confirmado» y «5 de 5»',
        tramos=[
            ('w05', 540, 600, R(1392), 1, 'c6b', 'clip 540–600 · Gabriela: «Aceptar · No puedo» (grab. 1392)'),
            ('w06', 600, 602, R(1469), 1, 'c6b', 'clip 600–602 · toque en «Aceptar»'),
            ('w07', 602, 667, R(1484), 1, 'c6b', 'clip 602–667 · «¡Gracias por servir! Tu líder ya lo sabe.», «Confirmado»'),
            ('v15', 656, 840, R(1660), 1, 'c6a', 'clip 656–840 · el turno del líder: Gabriela «Confirmado», «5 de 5» (látigo 656–666)'),
        ],
        stills=[('st-w1392', 528, 540, 'assets/stills/equipos-1392.png', 'c6b',
                 'clip 528–540 · still de la grab. 1392 (el primer cuadro de w05, «Aceptar · No puedo»): lo que se ve en el látigo de entrada '
                 '(el tramo anterior del clip es la pantalla desplazada a «Instrucciones»)')],
        cam={'#c6b': ('E6.botones', []),
             '#c6a': ('E6.parqueadero2', [(690, 'mover', 'E6.cierre', 9)])},
        marcas=[(600, 311, 1221, 'c6b', 602, '«Aceptar»')],
        sonidos=[(601, 'toque', 1, '«Aceptar»'), (603, 'confirmacion', 1.4, '«¡Gracias por servir! Tu líder ya lo sabe.»'),
                 (660, 'desliz', 1.4, 'el látigo vertical al líder (656–666)'), (662, 'confirmacion', 1, 'Gabriela «Confirmado» en el turno del líder')],
    ),
]

# Las pistas del timeline (solo para el editor) por cámara
PISTA = {'c1': 10, 'c2': 11, 'c3a': 12, 'c3b': 13, 'c4': 14, 'c5': 15, 'c6a': 16, 'c6b': 17, 'c7': 18}
PISTA_STILL = 19

# La síntesis: el tablero del pastor (tableros.mp4 de recorrido-membresia, 1920×1080, «Resumen» quieto en la grab. 160–369)
SINTESIS_TRAMO = ('t01', 1440, 1620, R(160), 1, 'c7', '1440–1620 · Tableros › Resumen, «Toda la iglesia»: 1.324, 448 nuevas, 145 en ruta… '
                  'y el semáforo de actividad (grab. 160–339)')

# Los cuadros de los cambios de mundo (todos en un golpe medido; SPEC §0.3)
T_ENTRA, T_LAT1, T_IRIS, T_LATV, T_ZOOM, T_LAT2, T_MORPH, T_CIERRE = 120, 300, 480, 720, 960, 1200, 1440, 1620
FIN = 1770

# Sonidos de la estructura (cuadro del sonido = imagen + 1)
SONIDOS_FIJOS = [
    (121, 'desliz', 1.4, 'la ventana sube con el bajo (110–120)'),
    (301, 'desliz', 1, 'el látigo horizontal a Eventos (290–300)'),
    (481, 'desliz', 1, 'el iris a Academia, sobre la costura de la música (479–484)'),
    (721, 'desliz', 1.4, 'el látigo vertical a Mi iglesia, en el golpe más fuerte (710–720)'),
    (961, 'desliz', 1, 'el empuje a Comunicaciones, el clímax (952–968)'),
    (1201, 'desliz', 1, 'el látigo horizontal de vuelta, a Equipos (1190–1200)'),
    (1441, 'desliz', 1.4, 'el morph del celular al escritorio (1434–1446)'),
]

# Textos: (id, líneas, lugar, host desde, host hasta, salida (cuadro absoluto) o None, ceja, comentario)
# lugar: 'apertura' (centrada, 132 px), 'cel' (columna izquierda) o 'esc' (arriba del escritorio). Las palabras entran cada 2 cuadros
# desde el host + 1 (el host arranca un cuadro antes del pulso); la apertura, una por pulso (0 · 15 · 30 · 45).
TEXTOS = [
    ('texto-0', [['Cada', 'punto'], ['es', ('em', 'una'), ('em', 'persona.')]], 'apertura', 0, 120, 105, None,
     'P1 · la frase del sitio que revela el hero al bajar («Cada punto es una persona.»), sobre los puntos del kit: «Cada» (0, ya en la '
     'miniatura) · «punto» (15) · «es una» (30) · «persona.» (45); «una persona.» en itálica dorada; sale 105–109, antes de que suba la ventana. «Kingdom es para toda la '
     'iglesia» no se repite aquí: es la frase del cierre del Comercial'),
]
for m in MOD:
    a = {1: 120, 2: 300, 3: 480, 4: 720, 5: 960, 6: 1200}[m['n']]
    b = a + (180 if m['n'] <= 2 else 240)
    TEXTOS.append((f"texto-{m['n']}", m['lineas'], 'cel', a, b, b - 12, m['nombre'],
                   f"P{m['n'] + 1} · {m['nombre']}: la ceja y «{' '.join(w if isinstance(w, str) else w[1] for l in m['lineas'] for w in l)}» "
                   f"desde el {a + 1}; salen {b - 12}–{b - 8}, antes de que arranque el cambio del {b}"))
TEXTOS.append(('texto-7', [['Toda', 'tu', 'iglesia,', 'en', ('em', 'una'), ('em', 'sola'), ('em', 'app.')]], 'esc', 1440, 1620, None,
               'Del pastor al miembro más nuevo',
               'P8 · la síntesis arriba del escritorio: la ceja (la bajada del hero) y «Toda tu iglesia, en una sola app.» palabra a palabra '
               'desde el 1447 (cuando el morph ya asentó); se sostiene hasta el corte al cierre (1620)'))


# ── Generación ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
def recorte(m):
    """Los tramos de la ventana [ini, fin) del clip, corridos `off`."""
    out = []
    for tid, a, b, media, rate, cam, c in m['tramos']:
        a2, b2 = max(a, m['ini'] - m.get('pre', 0)), min(b, m['fin'])
        if b2 <= a2:
            continue
        me = media + (a2 - a) / FPS * rate
        out.append((f"{m['clave']}-{tid}", a2 + m['off'], b2 + m['off'], me, rate, cam, f"{a2 + m['off']}–{b2 + m['off']} · {c}"))
    return out


def video_html(t, src, sangria):
    vid, a, b, me, rate, cam, c = t
    return (f'{sangria}<!-- {c} -->\n'
            f'{sangria}<video id="{vid}" class="clip" src="{src}" muted playsinline data-track-index="{PISTA[cam]}"\n'
            f'{sangria}  data-start="{s(a)}" data-duration="{s(b - a)}" data-media-start="{num(me)}" data-playback-rate="{num(rate)}"></video>')


def stills_html(m, cam, sangria):
    out = []
    for sid, a, b, src, c_, com in m.get('stills', []):
        if c_ != cam:
            continue
        a2, b2 = a + m['off'], b + m['off']
        out.append(f'{sangria}<!-- {a2}–{b2} · {com} -->')
        out.append(f'{sangria}<img id="{sid}" class="clip" src="{src}" alt="" data-track-index="{PISTA_STILL}" data-start="{s(a2)}" '
                   f'data-duration="{s(b2 - a2)}" />')
    return '\n'.join(out)


def marcas_html(m, cam, sangria):
    out = [f'{sangria}<div class="marcas">']
    for n, x, y, c_, corte, r in m['marcas']:
        if c_ != cam:
            continue
        f = n + m['off']
        st = f'left: {x * K:.1f}px; top: {y * K:.1f}px'
        out.append(f'{sangria}  <!-- {f} (clip {n}) · {r} (toques[] de pasos.json, px del video × 720/1170) -->')
        out.append(f'{sangria}  <div class="toque" id="tq-{f}" style="{st}"></div>')
        out.append(f'{sangria}  <div class="onda" id="on-{f}" style="{st}"></div>')
    out.append(f'{sangria}</div>')
    return '\n'.join(out)


def camara_html(m, cam, sangria):
    partes = [video_html(t, m['src'], sangria) for t in recorte(m) if t[5] == cam]
    st = stills_html(m, cam, sangria)
    if st:
        partes.append(st)
    partes.append(marcas_html(m, cam, sangria))
    return '\n'.join(partes)


def camaras_js():
    out = []
    for m in MOD:
        out.append(f"        // {m['nombre']} (clip {m['ini']}–{m['fin']} → {m['ini'] + m['off']}–{m['fin'] + m['off']})")
        for sel, (ini, ops) in m['cam'].items():
            out.append(f"        gsap.set('{sel}', {ini}); tl.set('{sel}', {ini}, 0);")
            for n, tipo, e, d in ops:
                f = n + m['off']
                if tipo == 'set':
                    out.append(f"        tl.set('{sel}', {e}, F({f}));")
                else:
                    out.append(f"        mover('{sel}', {e}, {f}, {d});")
    return '\n'.join(out)


TOMAS = {
    'toque': [('identidad/audio/toque.wav', 0.075, 0), ('assets/audio/toque-b.wav', 0.072833, 0), ('assets/audio/toque-c.wav', 0.077333, 0)],
    'aparicion': [('identidad/audio/aparicion.wav', 0.22, 0), ('assets/audio/aparicion-b.wav', 0.213604, 0),
                  ('assets/audio/aparicion-c.wav', 0.226813, 0)],
    'desliz': [('identidad/audio/desliz.wav', 0.36, 0.2), ('assets/audio/desliz-b.wav', 0.349521, 0.2 / 1.03),
               ('assets/audio/desliz-c.wav', 0.371146, 0.2 / 0.97)],
    'confirmacion': [('identidad/audio/confirmacion.wav', 0.32, 0.1)],
}
CARRIL = {'toque': 21, 'aparicion': 22, 'desliz': 23, 'confirmacion': 24}


def todos_los_sonidos():
    lista = [(f, t, v, c) for f, t, v, c in SONIDOS_FIJOS]
    for m in MOD:
        for n, t, v, c in m['sonidos']:
            lista.append((n + m['off'], t, v, f"{m['nombre']}: {c} (clip {n})"))
    lista.sort()
    return lista


def sonidos_html():
    out, giro = [], {k: 0 for k in TOMAS}
    for f, tipo, vol, c in todos_los_sonidos():
        tomas = TOMAS[tipo]
        src, dur, acento = tomas[giro[tipo] % len(tomas)]
        letra = 'abc'[giro[tipo] % len(tomas)]
        giro[tipo] += 1
        start = f / FPS - acento
        out.append(f'      <!-- {f} · {tipo} {letra if len(tomas) > 1 else ""} · {c} -->')
        out.append(f'      <audio id="snd-{tipo}-{f}" src="{src}" data-start="{num(start)}" data-duration="{dur}" '
                   f'data-track-index="{CARRIL[tipo]}" data-volume="{num(vol)}"></audio>')
    return '\n'.join(out)


def toques_js():
    filas = []
    for m in MOD:
        for n, x, y, c_, corte, r in m['marcas']:
            filas.append(f"[{n + m['off']}, {corte + m['off'] if corte else 'null'}]")
    return '[' + ', '.join(filas) + ']'


def hosts_html():
    out = []
    pista = 1
    for tid, lineas, lugar, a, b, salida, ceja, c in TEXTOS:
        desde = max(0, a - 1) if lugar != 'apertura' else 0
        hold = '\n        data-hold' if salida is None else ''
        out.append(f'      <!-- {c} -->')
        out.append(f'      <div id="{tid}" data-composition-id="{tid}" data-composition-src="compositions/{tid}.html" data-track-kind="graphics"{hold}\n'
                   f'        data-start="{s(desde)}" data-duration="{s(b - desde)}" data-track-index="{pista}" data-width="1920" data-height="1080"></div>')
        pista = 2 if pista == 1 else 1
    return '\n'.join(out)


TEXTO_TPL = '''<!doctype html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <!-- {comentario}. Ceja: Inter 700, 28 px, mayúsculas, dorada (.k-feed-ceja con el tamaño de 16:9). Frase: Fraunces 560, {px} px,
         interlínea 1,04, −0,02 em; entrada-palabra: blur 6 → 0 + opacidad, 4 cuadros, power4.out, sin desplazarse; salida-texto: blur 0 → 8 +
         opacidad, 4 cuadros, power3.in. Generada por _gen/gen.py. -->
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
        .t-ceja {{
          position: absolute;
          left: {cx};
          top: {cy};
          font-size: 28px;
          line-height: 1.2;
          white-space: nowrap;
        }}
        .t-frase {{
          position: absolute;
          left: {fx};
          top: {fy};
          width: {fw};
          font-size: {px}px;
          color: var(--k-noche-tinta);
          text-align: {alin};
          text-wrap: initial;
        }}
        .t-frase em {{
          color: var(--k-noche-dorado);
        }}
        .linea {{
          display: block;
          white-space: nowrap;
        }}
        .palabra {{
          display: inline-block;
        }}
      </style>
      <div id="root" data-composition-id="{tid}" data-width="1920" data-height="1080" data-duration="{dur}">
{ceja}        <div class="k-feed-frase t-frase" id="{pref}">
{lineas}
        </div>
      </div>
      <script>
        (function () {{
          const F = (n) => n / 30;
          const tl = gsap.timeline({{ paused: true }});
{tweens}
          tl.set({{}}, {{}}, F({fin}));
          window.__timelines['{tid}'] = tl;
        }})();
      </script>
    </template>
  </body>
</html>
'''


def texto_html(tid, lineas, lugar, a, b, salida, ceja, c):
    pref = 'tx' + tid.split('-')[1]  # «tx»: nunca choca con los ids del host (#t3, #t6 son las tiras)
    desde = max(0, a - 1) if lugar != 'apertura' else 0
    i, hl = 0, []
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
    if lugar == 'apertura':
        tw.append('          // «Cada» ya está en el cuadro 0 (la miniatura); luego un grupo por pulso, cada uno un cuadro antes de su pulso.')
        tw.append(f"          [[[2], 15], [[3, 4], 30], [[5], 45]].forEach(([ws, n]) => ws.forEach((w) =>")
        tw.append(f"            tl.fromTo(`#{pref}-w${{w}}`, {{ opacity: 0, filter: 'blur(6px)' }}, {{ opacity: 1, filter: 'blur(0px)', duration: F(4), ease: 'power4.out' }}, F(n - 1))));")
    else:
        if ceja:
            tw.append(f"          tl.fromTo('#{pref}-ceja', {{ opacity: 0, filter: 'blur(8px)' }}, {{ opacity: 1, filter: 'blur(0px)', duration: F(6), ease: 'power4.out' }}, F({0 if lugar == 'cel' else 6})); // entrada-línea")
        primera = 1 if lugar == 'cel' else 7  # sobre el escritorio, después de que el morph asienta (1446)
        tw.append(f'          for (let i = 1; i <= {n}; i++) {{')
        tw.append(f"            tl.fromTo(`#{pref}-w${{i}}`, {{ opacity: 0, filter: 'blur(6px)' }}, {{ opacity: 1, filter: 'blur(0px)', duration: F(4), ease: 'power4.out' }}, F({primera} + 2 * (i - 1)));")
        tw.append('          }')
    if salida is not None:
        sel = f"['#{pref}', '#{pref}-ceja']" if ceja else f"'#{pref}'"
        tw.append(f"          tl.to({sel}, {{ opacity: 0, filter: 'blur(8px)', duration: F(4), ease: 'power3.in' }}, F({salida - desde})); // {salida}–{salida + 4}")
    if lugar == 'apertura':
        fx, fy, fw, px, alin = '0px', '372px', '1920px', 132, 'center'
        cx = cy = '0px'
    elif lugar == 'cel':
        fx, fy, fw, px, alin = '120px', '460px', '936px', 84, 'left'
        cx, cy = '120px', '412px'
    else:
        fx, fy, fw, px, alin = '240px', '132px', '1440px', 84, 'left'
        cx, cy = '240px', '92px'
    ceja_html = f'        <div class="k-feed-ceja t-ceja" id="{pref}-ceja">{ceja}</div>\n' if ceja else ''
    return TEXTO_TPL.format(comentario=c, px=px, cx=cx, cy=cy, fx=fx, fy=fy, fw=fw, alin=alin, tid=tid, dur=s(b - desde), ceja=ceja_html,
                            pref=pref, lineas='\n'.join(hl), tweens='\n'.join(tw), fin=b - desde)


def main():
    tpl = open(os.path.join(AQUI, 'index.tpl.html'), encoding='utf8').read()
    sg = ' ' * 16
    rep = {
        '@@TEXTOS@@': hosts_html(),
        '@@SONIDOS@@': sonidos_html(),
        '@@CAMARAS@@': camaras_js(),
        '@@TOQUES@@': toques_js(),
    }
    for m in MOD:
        for cam in sorted({t[5] for t in m['tramos']}):
            rep[f'@@{cam.upper()}@@'] = camara_html(m, cam, sg)
    t = SINTESIS_TRAMO
    rep['@@C7@@'] = video_html(t, 'assets/grabaciones/tableros.mp4', sg)
    html = tpl
    for k, v in rep.items():
        html = html.replace(k, v)
    assert '@@' not in html, 'quedó un marcador sin reemplazar: ' + html[html.index('@@'):html.index('@@') + 20]
    open(os.path.join(RAIZ, 'index.html'), 'w', encoding='utf8', newline='\n').write(html)
    comp = os.path.join(RAIZ, 'compositions')
    os.makedirs(comp, exist_ok=True)
    for tx in TEXTOS:
        open(os.path.join(comp, tx[0] + '.html'), 'w', encoding='utf8', newline='\n').write(texto_html(*tx))
    print('ok: index.html y', len(TEXTOS), 'textos ·', sum(len(recorte(m)) for m in MOD) + 1, 'tramos ·',
          sum(len(m['marcas']) for m in MOD), 'marcas ·', len(todos_los_sonidos()), 'sonidos')


if __name__ == '__main__':
    main()
