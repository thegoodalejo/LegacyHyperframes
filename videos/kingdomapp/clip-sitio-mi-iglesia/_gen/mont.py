import sys,glob,re,os
from PIL import Image,ImageDraw,ImageFont
d=sys.argv[1]; out=sys.argv[2]; cols=int(sys.argv[3]) if len(sys.argv)>3 else 6; w=int(sys.argv[4]) if len(sys.argv)>4 else 360
fs=sorted(glob.glob(d+'/frame-*-at-*.png'),key=lambda f:int(re.search(r'frame-(\d+)',f).group(1)))
h=int(w*1350/1080); font=ImageFont.truetype('arial.ttf',22)
rows=(len(fs)+cols-1)//cols
img=Image.new('RGB',(cols*w,rows*(h+28)),'white'); dr=ImageDraw.Draw(img)
for i,f in enumerate(fs):
    t=float(re.search(r'at-([\d.]+)s',f).group(1)); fr=int(t*30)
    x=(i%cols)*w; y=(i//cols)*(h+28)
    img.paste(Image.open(f).convert('RGB').resize((w,h)),(x,y+28)); dr.text((x+4,y+2),f'{fr}',fill='red',font=font)
img.save(out,quality=85); print(len(fs))
