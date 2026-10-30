import numpy as np
from PIL import Image
def L(i): return np.asarray(Image.open('../fr/f%04d.png'%i).convert('L'),dtype=np.float32)
def best(a,b,y0=60,y1=760):
    A=L(a);B=L(b);res=[]
    for d in range(-450,451):
        # content at y in A appears at y+d in B
        ys=max(y0,y0-d); ye=min(y1,y1-d)
        if ye-ys<80: continue
        e=np.mean(np.abs(A[ys:ye]-B[ys+d:ye+d]))
        res.append((e,d))
    res.sort(); return res[:3]
for a,b in [(290,291),(918,919),(1038,1153),(1232,1293),(1089,1090),(1256,1257)]:
    print(a,b,best(a,b))
