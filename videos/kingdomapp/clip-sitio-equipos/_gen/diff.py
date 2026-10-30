import sys, numpy as np
from PIL import Image
S=sys.argv[1]
prev=None; res=[]
for n in range(1957):
    a=np.asarray(Image.open(f"{S}/f/{n:04d}.jpg").convert('L'),dtype=np.int16)
    if prev is not None:
        res.append((n,float(np.abs(a-prev).mean())))
    prev=a
np.save(f"{S}/diff.npy",np.array(res))
# print runs of change
th=0.4
run=None
for n,v in res:
    if v>th:
        if run is None: run=[n,n,v]
        else: run[1]=n; run[2]=max(run[2],v)
    else:
        if run: print(f"{run[0]}-{run[1]} max {run[2]:.1f}"); run=None
if run: print(run)
