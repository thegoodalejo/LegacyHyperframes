import sys, glob, os, re
from PIL import Image, ImageDraw
# uso: snap.py <dir de snapshots> <salida-prefijo> [cols] [ancho] [por hoja]
d = sys.argv[1]; pre = sys.argv[2]
cols = int(sys.argv[3]) if len(sys.argv) > 3 else 3
w = int(sys.argv[4]) if len(sys.argv) > 4 else 640
per = int(sys.argv[5]) if len(sys.argv) > 5 else cols * 3
fs = sorted(glob.glob(os.path.join(d, 'frame-*.png')), key=lambda p: int(re.search(r'frame-(\d+)', p).group(1)))
h = int(w * 1080 / 1920)
for k in range(0, len(fs), per):
    grupo = fs[k:k + per]
    rows = (len(grupo) + cols - 1) // cols
    sheet = Image.new('RGB', (cols * w, rows * (h + 22)), 'white')
    dr = ImageDraw.Draw(sheet)
    for j, p in enumerate(grupo):
        t = float(re.search(r'at-([\d.]+)s', p).group(1))
        im = Image.open(p).convert('RGB').resize((w, h), Image.LANCZOS)
        x = (j % cols) * w; y = (j // cols) * (h + 22)
        sheet.paste(im, (x, y + 22)); dr.text((x + 4, y + 4), f"cuadro {round(t*30)}  t={t:.3f}", fill='red')
    sheet.save(f"{pre}-{k // per + 1}.jpg", quality=85)
print('ok', len(fs))
