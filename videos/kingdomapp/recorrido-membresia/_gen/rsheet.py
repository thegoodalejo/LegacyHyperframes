import sys, subprocess, os
from PIL import Image, ImageDraw
# uso: rsheet.py video.mp4 salida.jpg cols ancho f1 f2 ... (cuadros del render)
v, out, cols, w = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
fr = [int(x) for x in sys.argv[5:]]
tmp = os.path.join(os.path.dirname(os.path.abspath(out)), 'rtmp'); os.makedirs(tmp, exist_ok=True)
for f in os.listdir(tmp): os.remove(os.path.join(tmp, f))
sel = '+'.join(f'eq(n\,{f})' for f in fr)
subprocess.run(['ffmpeg', '-v', 'error', '-i', v, '-vf', f'select={sel}', '-fps_mode', 'passthrough', os.path.join(tmp, 'r%03d.png')], check=True)
files = sorted(os.listdir(tmp)); h = int(w * 1080 / 1920); rows = (len(fr) + cols - 1) // cols
sheet = Image.new('RGB', (cols * w, rows * (h + 22)), 'white'); d = ImageDraw.Draw(sheet)
for k, (f, p) in enumerate(zip(sorted(fr), files)):
    im = Image.open(os.path.join(tmp, p)).convert('RGB').resize((w, h), Image.LANCZOS)
    x = (k % cols) * w; y = (k // cols) * (h + 22)
    sheet.paste(im, (x, y + 22)); d.text((x + 4, y + 4), f'render cuadro {f}', fill='red')
sheet.save(out, quality=85); print('ok', len(files))
