import sys, numpy as np
from PIL import Image
D='../fr/f%04d.png'
prev=None
out=[]
for i in range(1593):
    a=np.asarray(Image.open(D%i).convert('L'),dtype=np.int16)
    if prev is not None:
        d=np.abs(a-prev)
        m=(d>12)
        if m.any():
            ys,xs=np.where(m)
            out.append(f"{i}: n={m.sum()} y={ys.min()}-{ys.max()} x={xs.min()}-{xs.max()}")
    prev=a
open('diff.txt','w').write("\n".join(out))
