import sys, numpy as np
from PIL import Image
r=sys.argv[1]; a=int(sys.argv[2]); b=int(sys.argv[3]); y0=int(sys.argv[4]); y1=int(sys.argv[5]); x0=int(sys.argv[6]); x1=int(sys.argv[7]); rng=int(sys.argv[8])
L=lambda i: np.asarray(Image.open(f'fr/{r}/f{i:04d}.png').convert('L'),dtype=np.float32)[:,x0:x1]
A=L(a);B=L(b);res=[]
for d in range(-rng,rng+1):
    ys=max(y0,y0-d); ye=min(y1,y1-d)
    if ye-ys<40: continue
    res.append((float(np.mean(np.abs(A[ys:ye]-B[ys+d:ye+d]))),d))
res.sort(); print(res[:4])
