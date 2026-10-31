# Mide la sincronía de «Kingdom en un minuto» desde las tablas de gen.py y los pasos.json de cada grabación:
import io as _io, sys as _sys; _sys.stdout = _io.TextIOWrapper(_sys.stdout.buffer, encoding="utf-8")
#   · cada marca de toque contra el cuadro real del toque en la grabación (pasos.json → toques[].cuadro), por el tramo que se ve;
#   · cada marca contra su sonido (el sonido cae un cuadro después de la imagen);
#   · que cada toque, cada cambio de mundo y cada sonido caiga en un pulso (múltiplo de 15 cuadros).
#   python _gen/sincronia.py      (desde clip-sitio-en-un-minuto/)
import json, math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen

malos = 0
print('Marca (video) · módulo · rótulo · cuadro de la grabación visto → toque real (pasos.json) · diferencia')
for m in gen.MOD:
    pasos = json.load(open(m['src'].replace('.mp4', '-pasos.json'), encoding='utf8'))['pasos']
    toques = [t for p in pasos for t in p.get('toques', [])]
    tramos = gen.recorte(m)
    sons = {n + m['off'] for n, tipo, v, c in m['sonidos'] if tipo == 'toque'}
    for n, x, y, cam, corte, rot in m['marcas']:
        f = n + m['off']
        tr = [t for t in tramos if t[1] <= f < t[2] and t[5] == cam]
        if not tr:
            print(f'  {f} · {m["nombre"]} · {rot}: SIN TRAMO'); malos += 1; continue
        vid, a, b, me, rate, _, _ = tr[0]
        g = math.floor(round((me - 0.01) * 30, 3) + (f - a) * rate + 1e-6)
        cerca = min(toques, key=lambda t: (t['x'] - x) ** 2 + (t['y'] - y) ** 2 + 400 * (t['cuadro'] - g) ** 2)
        d = g - cerca['cuadro']
        s_ok = (f + 1) in sons
        pulso = f % 15 == 0
        malos += (abs(d) > 1) + (not s_ok) + (not pulso)
        print(f'  {f:5d} · {m["nombre"]:14s} · {rot:32s} · grab. {g} → {cerca["cuadro"]} ({cerca["x"]},{cerca["y"]}) · {d:+d} cuadros'
              f' · sonido en {f + 1}: {"sí" if s_ok else "NO"} · pulso: {"sí" if pulso else "NO"}')
print('Cambios de mundo:', ', '.join(f'{t}{"" if t % 15 == 0 else " NO"}' for t in
      [gen.T_ENTRA, gen.T_LAT1, gen.T_IRIS, gen.T_LATV, gen.T_ZOOM, gen.T_LAT2, gen.T_MORPH, gen.T_CIERRE]))
fuera = [(f, t) for f, t, v, c in gen.todos_los_sonidos() if (f - 1) % 15 not in (0, 14, 1, 2, 3)]
print('Sonidos cuya imagen no cae en un pulso (o a 1–3 cuadros de su toque):', fuera or 'ninguno')
print('OK' if malos == 0 else f'{malos} problemas')
