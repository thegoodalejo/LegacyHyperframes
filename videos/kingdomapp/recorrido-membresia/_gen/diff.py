import sys, numpy as np, os
from PIL import Image
r=sys.argv[1]; d=f'fr/{r}'; n=len(os.listdir(d))
prev=None; out=[]
for i in range(n):
    a=np.asarray(Image.open(f'{d}/f{i:04d}.png').convert('L'),dtype=np.int16)
    if prev is not None:
        m=np.abs(a-prev)>12
        if m.any():
            ys,xs=np.where(m)
            out.append(f"{i}: n={m.sum()} y={ys.min()}-{ys.max()} x={xs.min()}-{xs.max()}")
    prev=a
open(f'diff-{r}.txt','w').write("\n".join(out)); print(r, len(out))
