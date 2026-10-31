# Genera index.html del clip de Comunicaciones (4:5) a partir de tablas: tramos, marcas y sonidos.
import io, os, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(AQUI, "..", "index.html")
TPL = sys.argv[2] if len(sys.argv) > 2 else os.path.join(AQUI, "index.tpl.html")
f = lambda n: f"{n/30:.6f}".rstrip('0').rstrip('.') if n % 30 else str(n // 30)

# (clip desde, clip hasta, grab desde, comentario)  — todo a 1×
TRAMOS = [
    (0, 78, 40, "Bandeja quieta, «Cola 4» (grab. 40–117); toque en la fila de Mariana en el 75 (grab. 115)"),
    (78, 122, 193, "match cut sobre el toque: la conversación ya cargada (grab. 193–236; «Cargando…» 121–125 queda fuera); entra 1,03 → 1,00; toque en «Tomar» en el 120 (grab. 235)"),
    (122, 140, 246, "corte en la onda del botón (237→246): «Atendiendo» y «… tomó la conversación» en el 122 (grab. 246)"),
    (140, 182, 348, "quieta (corte invisible en la pausa 264→348); toque en el compositor en el 180 (grab. 388)"),
    (182, 210, 394, "corte en el foco (390→394): la tecla «/» y las respuestas rápidas en el 182 (grab. 394)"),
    (210, 242, 476, "quieta (corte invisible 422→476); toque en «/horarios» en el 240 (grab. 506)"),
    (242, 270, 512, "corte en la onda (508→512): el compositor lleno con el horario en el 242 (grab. 512)"),
    (270, 302, 590, "quieta (corte invisible 540→590); toque en enviar en el 300 (grab. 620)"),
    (302, 340, 630, "corte en la espera (622→630): la respuesta en el hilo en el 302 (grab. 630), con una palomita"),
    (340, 377, 765, "quieta (corte invisible 668→765); toque en volver en el 375 (grab. 800, fuera del encuadre: no se dibuja)"),
    (377, 400, 808, "corte en la espera (802→808): la lista con «Cola 3 · Mis chats 3» en el 377 (grab. 808)"),
    (400, 422, 894, "quieta (corte invisible 831→894); toque en «Campañas» en el 420 (grab. 914)"),
    (422, 450, 928, "corte en la espera y el esqueleto (916→928): las tarjetas suben escalonadas 422–432 (la animación de la app)"),
    (450, 510, 1011, "quieta (corte invisible 956→1011); la lista baja hasta la invitación en un cuadro en el 480 (grab. 1041, salto real)"),
    (510, 602, 1098, "quieta (corte invisible 1071→1098); toque en la invitación en el 600 (grab. 1188)"),
    (602, 630, 1202, "corte en la espera y el esqueleto (1190→1202): el reporte con sus números en el 602 (grab. 1202)"),
    (630, 661, 1299, "quieta (corte invisible 1230→1299); toque en «respondieron» en el 660 (grab. 1329)"),
    (661, 675, 1335, "corte en la onda (1330→1335): el contorno de «respondieron» en el 661 (grab. 1335)"),
    (675, 840, 1396, "la app baja a los nombres en un cuadro en el 675 (grab. 1396, salto real): «Destinatarios (23)», «Leído» y «Allí estaré»"),
]

# toques[] de pasos.json (px del video) — 375 (volver) no se dibuja
MARCAS = [
    (75, 584, 1496, "la fila de Mariana"),
    (120, 605, 456, "«Tomar»"),
    (180, 585, 2127, "el compositor"),
    (240, 585, 1797, "«/horarios»"),
    (300, 1086, 2136, "enviar"),
    (420, 432, 399, "«Campañas»"),
    (600, 585, 1857, "la invitación"),
    (660, 311, 1944, "«respondieron»"),
]

# (cuadro del sonido, archivo, acento, duración, volumen, pista, id, comentario)
T = {"a": ("identidad/audio/toque.wav", 0.075), "b": ("assets/audio/toque-b.wav", 0.073), "c": ("assets/audio/toque-c.wav", 0.077)}
SONIDOS = []
def toque(n, k, com, clave=False):
    src, d = T[k]
    SONIDOS.append((n, src, 0, d, 1, 21, f"snd-toque-{n-1}", f"{n} · toque {k} en {com}" + (" (clave; 1,0: ver REVIEW §5)" if clave else "")))
def otro(n, kind, com, vol=1):
    src = f"identidad/audio/{kind}.wav"
    ac, d, pista = {"aparicion": (0, 0.22, 22), "desliz": (0.2, 0.36, 23), "confirmacion": (0.1, 0.32, 24)}[kind]
    SONIDOS.append((n, src, ac, d, vol, pista, f"snd-{kind}-{n-1}", f"{n} · {com}" + (f"; acento {str(ac).replace('.', ',')}" if ac else "")))

toque(76, "a", "la fila de Mariana")
toque(121, "c", "«Tomar», con el bajo", True)
otro(123, "aparicion", "«Atendiendo» y la nota «… tomó la conversación» (122)")
toque(181, "b", "el compositor, con el pico (la lista sube con el mismo toque: sin sonido propio)", True)
otro(196, "aparicion", "la ceja «COMUNICACIONES» (195)")
toque(241, "a", "«/horarios»")
otro(243, "aparicion", "el compositor se llena con el horario (242)")
toque(301, "c", "enviar", True)
otro(303, "confirmacion", "la respuesta queda en el hilo (302)", 1.4)
toque(376, "b", "volver (fuera del encuadre: se oye y no se dibuja)")
toque(421, "a", "«Campañas»")
otro(481, "desliz", "la lista baja hasta la invitación (480)")
toque(601, "b", "la invitación, con la segunda subida", True)
otro(603, "confirmacion", "el reporte con sus números (602)", 1.0)
toque(661, "c", "«respondieron», con el golpe; el contorno en el 661", True)
otro(676, "confirmacion", "los nombres con «Leído» y «Allí estaré» (675), la prueba más fuerte", 1.4)

def ds(n, ac):
    v = n / 30 - ac
    return f"{v:.6f}".rstrip('0').rstrip('.')

o = io.StringIO()
w = o.write
tramos = []
for i, (a, b, g, com) in enumerate(TRAMOS, 1):
    ms = f"{g/30 + 0.01:.6f}".rstrip('0').rstrip('.')
    tramos.append(f"""              <!-- {a}–{b} · {com} -->
              <video data-hf-id="hf-cv{i:02d}" id="v{i:02d}" class="clip" src="assets/grabaciones/grabacion.mp4" muted playsinline data-track-index="10"
                data-start="{ds(a,0)}" data-duration="{ds(b-a,0)}" data-media-start="{ms}" data-playback-rate="1"></video>""")
marcas = []
for n, x, y, com in MARCAS:
    marcas.append(f"""                <!-- {n} · {com} -->
                <div data-hf-id="hf-ctq{n}" class="toque" id="tq-{n}" style="left: calc({x}px * var(--f-k)); top: calc({y}px * var(--f-k))"></div>
                <div data-hf-id="hf-con{n}" class="onda" id="on-{n}" style="left: calc({x}px * var(--f-k)); top: calc({y}px * var(--f-k))"></div>""")
sonidos = []
for n, src, ac, d, vol, pista, sid, com in SONIDOS:
    sonidos.append(f"""      <!-- {com} -->
      <audio data-hf-id="hf-c{sid}" id="{sid}" src="{src}" data-start="{ds(n, ac)}" data-duration="{d}" data-track-index="{pista}" data-volume="{vol}"></audio>""")

tpl = open(TPL, encoding="utf-8").read()
html = tpl.replace("@@TRAMOS@@", "\n".join(tramos)).replace("@@MARCAS@@", "\n".join(marcas)).replace("@@SONIDOS@@", "\n".join(sonidos))
open(OUT, "w", encoding="utf-8", newline="\n").write(html)
print("ok", len(TRAMOS), len(MARCAS), len(SONIDOS))
