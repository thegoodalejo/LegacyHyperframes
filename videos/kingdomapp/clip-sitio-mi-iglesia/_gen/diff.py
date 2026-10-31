import numpy as np
W,H=390,844
a=np.memmap('frames.gray',dtype=np.uint8,mode='r').reshape(-1,H,W)
n=a.shape[0]
out=[]
for i in range(1,n):
    d=np.abs(a[i].astype(np.int16)-a[i-1].astype(np.int16))
    m=d.mean()
    if m>0.02:
        ys=np.where(d.max(axis=1)>20)[0]
        rng=(ys.min(),ys.max()) if len(ys) else None
        out.append((i,round(float(m),3),rng))
for o in out: print(*o)
