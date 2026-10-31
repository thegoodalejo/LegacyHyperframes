# Extrae cuadros del render y arma una hoja con su número de cuadro.
import sys, subprocess, os
from PIL import Image, ImageDraw, ImageFont
src = sys.argv[1]; out = sys.argv[2]; frames = [int(x) for x in sys.argv[3].split(',')]; cols = int(sys.argv[4]) if len(sys.argv) > 4 else 10
os.makedirs('rf', exist_ok=True)
sel = '+'.join(f'eq(n\,{f})' for f in frames)
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', src, '-vf', f"select='{sel}',scale=270:338", '-fps_mode', 'passthrough', 'rf/t_%04d.png'], check=True)
font = ImageFont.truetype('arial.ttf', 18); w, h = 270, 338
rows = (len(frames) + cols - 1) // cols
img = Image.new('RGB', (cols * w, rows * (h + 22)), 'white'); d = ImageDraw.Draw(img)
for i, f in enumerate(sorted(frames)):
    x = (i % cols) * w; y = (i // cols) * (h + 22)
    img.paste(Image.open(f'rf/t_{i + 1:04d}.png'), (x, y + 22)); d.text((x + 4, y + 2), str(f), fill='red', font=font)
img.save(out, quality=85)
