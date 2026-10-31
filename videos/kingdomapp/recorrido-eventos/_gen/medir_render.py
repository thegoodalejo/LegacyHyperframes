# Mide el render: cuadros alrededor de los cortes «invisibles» (diferencia media entre el cuadro anterior y el del corte) y la sonoridad.
# Uso (desde la raíz): python _gen/medir_render.py renders/recorrido-eventos-16x9.mp4
import sys, subprocess, re, os, tempfile
import numpy as np
from PIL import Image
v = sys.argv[1]
tmp = tempfile.mkdtemp()
pares = [(1199, 1200), (1470, 1471), (1650, 1651), (1860, 1861), (899, 900), (29 * 30 + 29, 30 * 30)]
fr = sorted({f for p in pares for f in p})
sel = '+'.join(f'eq(n\,{f})' for f in fr)
subprocess.run(['ffmpeg', '-v', 'error', '-i', v, '-vf', f'select={sel}', '-fps_mode', 'passthrough', os.path.join(tmp, 'r%03d.png')], check=True)
fs = sorted(os.listdir(tmp)); m = dict(zip(fr, fs))
for a, b in pares:
    A = np.asarray(Image.open(os.path.join(tmp, m[a])).convert('L'), dtype=np.float32)
    B = np.asarray(Image.open(os.path.join(tmp, m[b])).convert('L'), dtype=np.float32)
    print(f'corte {a}→{b}: diferencia media {np.abs(A - B).mean():.2f} / 255')
r = subprocess.run(['ffmpeg', '-nostats', '-i', v, '-af', 'ebur128=peak=true:metadata=1', '-f', 'null', '-'], capture_output=True, text=True,
                   encoding='utf-8', errors='replace')
s = r.stderr; i = s.find('Summary:')
print(s[i:i + 600])
# Sonoridad momentánea alrededor de la costura (29,6–30,4 s)
for line in s.splitlines():
    mt = re.search(r't:\s*([\d.]+)\s+TARGET.*?M:\s*(-?[\d.]+)\s+S:\s*(-?[\d.]+)', line)
    if mt and 29.6 <= float(mt.group(1)) <= 30.4:
        print('t', mt.group(1), 'M', mt.group(2), 'S', mt.group(3))
