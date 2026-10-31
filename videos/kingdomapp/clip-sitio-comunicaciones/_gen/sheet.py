import os
import subprocess, sys
from PIL import Image, ImageDraw, ImageFont
src=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets/grabaciones/grabacion.mp4")
frames=[int(x) for x in sys.argv[2].split(',')]
out=sys.argv[1]
w=390;h=844
ims=[]
for f in frames:
    p=subprocess.run(['ffmpeg','-v','error','-i',src,'-vf',f'select=eq(n\,{f}),scale={w}:{h}','-vframes','1','-f','image2pipe','-vcodec','png','-'],capture_output=True)
    import io
    im=Image.open(io.BytesIO(p.stdout)).convert('RGB')
    d=ImageDraw.Draw(im); d.rectangle([0,0,70,24],fill=(200,0,0)); d.text((4,4),str(f),fill=(255,255,255),font=ImageFont.truetype('arial.ttf',18))
    ims.append(im)
cols=min(len(ims),8); rows=(len(ims)+cols-1)//cols
S=Image.new('RGB',(cols*w,rows*h),'white')
for i,im in enumerate(ims): S.paste(im,((i%cols)*w,(i//cols)*h))
S.save(out,quality=88)
