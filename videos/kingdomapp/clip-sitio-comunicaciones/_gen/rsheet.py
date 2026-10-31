import os
import subprocess, sys, io
from PIL import Image, ImageDraw, ImageFont
src=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "renders/clip-sitio-comunicaciones-4x5.mp4")
frames=[int(x) for x in sys.argv[2].split(',')]
w,h=270,338
sel='+'.join(f'eq(n\,{f})' for f in frames)
p=subprocess.run(['ffmpeg','-v','error','-i',src,'-vf',f'select={sel},scale={w}:{h}','-fps_mode','passthrough','-f','image2pipe','-vcodec','png','-'],capture_output=True)
data=p.stdout; ims=[]
sig=b'\x89PNG\r\n\x1a\n'; parts=data.split(sig)[1:]
for part,f in zip(parts,frames):
    im=Image.open(io.BytesIO(sig+part)).convert('RGB'); d=ImageDraw.Draw(im); d.rectangle([0,0,48,20],fill=(200,0,0)); d.text((3,2),str(f),fill='white',font=ImageFont.truetype('arial.ttf',16)); ims.append(im)
cols=min(8,len(ims)); rows=(len(ims)+cols-1)//cols
S=Image.new('RGB',(cols*w,rows*h),'white')
for i,im in enumerate(ims): S.paste(im,((i%cols)*w,(i//cols)*h))
S.save(sys.argv[1],quality=88)
