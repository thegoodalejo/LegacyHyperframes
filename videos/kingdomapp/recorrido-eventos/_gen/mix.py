# Simula la mezcla de index.html con ffmpeg (las mismas fuentes, tiempos, niveles y carriles de volumen) para elegir niveles antes de
# renderizar. Uso (desde la raíz): python _gen/mix.py [factor_musica]
import re, json, subprocess, sys
html = open('index.html', encoding='utf-8').read()
fm = float(sys.argv[1]) if len(sys.argv) > 1 else 1.0
tags = re.findall(r'<audio [^>]*>', html, re.S)
ins, fil, labs = [], [], []
for k, t in enumerate(tags):
    g = lambda a: (re.search(r'\s' + a + r'="([^"]*)"', t) or [None, None])[1]
    src, st, dur = g('src'), float(g('data-start')), float(g('data-duration'))
    ms = float(g('data-media-start') or 0)
    ins += ['-i', src]
    m = re.search(r"data-automation='([^']*)'", t)
    if m:
        pts = json.loads(m.group(1))['lanes'][0]['points']
        expr = '0'
        for a, b in reversed(list(zip(pts, pts[1:]))):
            va, vb = a['v'] * fm, b['v'] * fm
            seg = f"{va}+({vb}-{va})*(t-{a['t']})/{max(b['t']-a['t'],1e-6)}"
            expr = f"if(lt(t,{b['t']}),{seg},{expr})"
        expr = f"if(lt(t,{pts[0]['t']}),{pts[0]['v']*fm},{expr})" if pts[0]['t'] > 0 else expr
        last = pts[-1]['v'] * fm
        expr = f"if(gte(t,{pts[-1]['t']}),{last},{expr})"
        vol = f"volume='{expr}':eval=frame"
    else:
        vol = f"volume={float(g('data-volume') or 1)}"
    d = int(round(st * 1000))
    fil.append(f"[{k}:a]atrim=start={ms}:duration={dur},asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo,{vol},adelay={d}|{d}[a{k}]")
    labs.append(f'[a{k}]')
fil.append(''.join(labs) + f'amix=inputs={len(tags)}:normalize=0:duration=longest,atrim=duration=97,ebur128=peak=true[o]')
r = subprocess.run(['ffmpeg', '-nostats', '-v', 'info', *ins, '-filter_complex', ';'.join(fil), '-map', '[o]', '-f', 'null', '-'],
                   capture_output=True, text=True, encoding='utf-8', errors='replace')
s = r.stderr; i = s.find('Summary:')
if i < 0:
    print(s[-3000:]); sys.exit(1)
print(re.findall(r'I:\s+(-?[\d.]+) LUFS', s[i:])[0], 'LUFS · pico real', re.findall(r'Peak:\s+(-?[\d.]+) dBFS', s[i:])[0], 'dBTP')
