import sys
from PIL import Image, ImageDraw, ImageFont
S=sys.argv[1]; out=sys.argv[2]; frames=[int(x) for x in sys.argv[3].split(',')]
cols=int(sys.argv[4]) if len(sys.argv)>4 else 6
crop=None
if len(sys.argv)>5: crop=[int(v) for v in sys.argv[5].split(',')]  # y0,y1 css
ims=[]
for n in frames:
    im=Image.open(f"{S}/f/{n:04d}.jpg")
    if crop: im=im.crop((0,crop[0],390,crop[1]))
    ims.append((n,im))
w,h=ims[0][1].size
rows=(len(ims)+cols-1)//cols
G=Image.new('RGB',(cols*(w+6),rows*(h+22)),'white')
d=ImageDraw.Draw(G)
f=ImageFont.truetype("C:/Windows/Fonts/arial.ttf",16)
for i,(n,im) in enumerate(ims):
    x=(i%cols)*(w+6); y=(i//cols)*(h+22)
    G.paste(im,(x,y+22)); d.text((x+4,y+2),str(n),fill='red',font=f)
G.save(out,quality=85)
