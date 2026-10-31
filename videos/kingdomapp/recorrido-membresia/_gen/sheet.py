import sys
from PIL import Image, ImageDraw
# uso: sheet.py rec out.jpg cols box(x0,y0,x1,y1 o -) scale f1 f2 ... (a:b:paso)
r=sys.argv[1]; out=sys.argv[2]; cols=int(sys.argv[3]); box=sys.argv[4]; sc=float(sys.argv[5]); fr=[]
for a in sys.argv[6:]:
    if ':' in a:
        p=[int(x) for x in a.split(':')]; fr+=list(range(p[0],p[1]+1,p[2] if len(p)>2 else 1))
    else: fr.append(int(a))
ims=[]
for f in fr:
    im=Image.open(f'fr/{r}/f{f:04d}.png').convert('RGB')
    if box!='-': im=im.crop(tuple(int(v) for v in box.split(',')))
    im=im.resize((int(im.width*sc),int(im.height*sc)),Image.LANCZOS); ims.append(im)
W,H=ims[0].size; rows=(len(ims)+cols-1)//cols
sh=Image.new('RGB',(cols*W,rows*(H+20)),'white'); d=ImageDraw.Draw(sh)
for k,(f,im) in enumerate(zip(fr,ims)):
    x=(k%cols)*W; y=(k//cols)*(H+20); sh.paste(im,(x,y+20)); d.text((x+4,y+4),str(f),fill='red')
sh.save(out,quality=88); print('ok')
