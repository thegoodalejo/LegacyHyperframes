import subprocess, numpy as np, sys
src=sys.argv[1]
W,H=195,422
p=subprocess.run(['ffmpeg','-v','error','-i',src,'-vf',f'scale={W}:{H},format=gray','-f','rawvideo','-'],capture_output=True)
a=np.frombuffer(p.stdout,np.uint8).reshape(-1,H,W).astype(np.int16)
print(a.shape)
d=np.abs(np.diff(a,axis=0))
for i in range(len(d)):
    m=d[i].mean()
    if m>0.02:
        rows=np.where(d[i].max(axis=1)>20)[0]
        r=(rows.min()*2,rows.max()*2) if len(rows) else None  # CSS y approx (422 rows -> 844 css)
        print(i+1, round(float(m),3), r)
