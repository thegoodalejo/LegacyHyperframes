import sys
from PIL import Image, ImageDraw
# uso: sheet.py out.jpg cols f1 f2 ... (o a:b:paso)
out=sys.argv[1]; cols=int(sys.argv[2]); fr=[]
for a in sys.argv[3:]:
    if ':' in a:
        p=[int(x) for x in a.split(':')]; fr+=list(range(p[0],p[1]+1,p[2] if len(p)>2 else 1))
    else: fr.append(int(a))
crop=None
W,H=390,844
rows=(len(fr)+cols-1)//cols
sheet=Image.new('RGB',(cols*W,rows*(H+24)),'white')
d=ImageDraw.Draw(sheet)
for k,f in enumerate(fr):
    im=Image.open('../fr/f%04d.png'%f).convert('RGB')
    x=(k%cols)*W; y=(k//cols)*(H+24)
    sheet.paste(im,(x,y+24)); d.text((x+4,y+4),str(f),fill='red')
sheet.save(out,quality=85)
