import sys
from PIL import Image, ImageDraw, ImageFont
frames=[int(x) for x in sys.argv[2].split(',')]
font=ImageFont.truetype('arial.ttf',14)
img=Image.new('RGB',(len(frames)*420,880),'white'); d=ImageDraw.Draw(img)
for i,f in enumerate(frames):
    x=i*420+30
    im=Image.open(f'fr/{f}.png'); img.paste(im,(x,30))
    d.text((x,5),str(f),fill='red',font=font)
    for y in range(0,845,25):
        col=(255,0,0) if y%100==0 else (255,170,170)
        d.line([(x-6 if y%50==0 else x-3,30+y),(x+390,30+y)] if y%100==0 else [(x-6,30+y),(x,30+y)],fill=col,width=1)
        if y%50==0: d.text((x-30,30+y-7),str(y),fill='red',font=font)
img.save(sys.argv[1])
