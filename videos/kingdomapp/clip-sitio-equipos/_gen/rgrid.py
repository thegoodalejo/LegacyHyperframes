import sys
from PIL import Image, ImageDraw, ImageFont
S=sys.argv[1]; out=sys.argv[2]; frames=[int(x) for x in sys.argv[3].split(',')]; cols=int(sys.argv[4])
w,h=360,450
rows=(len(frames)+cols-1)//cols
G=Image.new('RGB',(cols*(w+4),rows*(h+20)),'white'); d=ImageDraw.Draw(G)
f=ImageFont.truetype("C:/Windows/Fonts/arial.ttf",16)
for i,n in enumerate(frames):
    x=(i%cols)*(w+4); y=(i//cols)*(h+20)
    G.paste(Image.open(f"{S}/r/{n:04d}.jpg"),(x,y+20)); d.text((x+4,y+2),str(n),fill='red',font=f)
G.save(out,quality=85)
