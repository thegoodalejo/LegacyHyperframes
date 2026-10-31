import numpy as np,sys
W,H=390,844
a=np.memmap('frames.gray',dtype=np.uint8,mode='r').reshape(-1,H,W)
def sh(i,j):
    A=a[i].astype(np.float32); B=a[j].astype(np.float32)
    best=None
    for d in range(-700,701):
        # content at A[y] appears at B[y-d]  (d>0: content moved up by d)
        y0=max(60,60+d); y1=min(765,765+d)
        if y1-y0<60: continue
        e=np.abs(A[y0:y1]-B[y0-d:y1-d]).mean()
        if best is None or e<best[0]: best=(e,d,y1-y0)
    return best
for p in sys.argv[1:]:
    i,j=map(int,p.split(':'))
    print(p, sh(i,j))
