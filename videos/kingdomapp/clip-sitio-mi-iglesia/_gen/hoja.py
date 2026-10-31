import sys, subprocess, os
from PIL import Image, ImageDraw, ImageFont
src="F:/Proyectos/LegacyHyperframes/videos/kingdomapp/clip-sitio-mi-iglesia/assets/grabaciones/grabacion.mp4"
frames=[int(x) for x in sys.argv[2].split(',')]
out=sys.argv[1]
cols=int(sys.argv[3]) if len(sys.argv)>3 else 8
os.makedirs('fr',exist_ok=True)
need=[f for f in frames if not os.path.exists(f'fr/{f}.png')]
if need:
    sel='+'.join(f'eq(n\,{f})' for f in need)
    subprocess.run(['ffmpeg','-v','error','-y','-i',src,'-vf',f"select='{sel}',scale=390:844",'-fps_mode','passthrough','fr/tmp_%04d.png'],check=True)
    for i,f in enumerate(sorted(need)):
        os.replace(f'fr/tmp_{i+1:04d}.png',f'fr/{f}.png')
w,h=390,844
rows=(len(frames)+cols-1)//cols
img=Image.new('RGB',(cols*w,rows*(h+30)),'white')
d=ImageDraw.Draw(img)
try: font=ImageFont.truetype('arial.ttf',24)
except: font=None
for i,f in enumerate(frames):
    x=(i%cols)*w; y=(i//cols)*(h+30)
    img.paste(Image.open(f'fr/{f}.png'),(x,y+30))
    d.text((x+5,y+2),str(f),fill='red',font=font)
img.save(out,quality=85)
