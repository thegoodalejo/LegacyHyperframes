# Simula la mezcla de index.html con ffmpeg para elegir niveles antes de renderizar.
# uso: mix.py <musica> <factor_toques_clave>
import re, subprocess, sys
root = r'F:/Proyectos/LegacyHyperframes/videos/kingdomapp/clip-sitio-eventos/'
html = open(root + 'index.html', encoding='utf-8').read()
mus = float(sys.argv[1]); clave = float(sys.argv[2])
tags = re.findall(r'<audio [^>]*>', html)
ins, fil, labs = [], [], []
k = 0
for t in tags:
    g = lambda a: (re.search(r'\s' + a + r'="([^"]*)"', t) or [None, None])[1]
    src, st, dur, vol, ms = g('src'), float(g('data-start')), float(g('data-duration')), g('data-volume'), g('data-media-start')
    ins += ['-i', root + src]
    if g('id') == 'musica':
        # 0–28: mus; 28–28.4: lineal a 0.224·mus/0.7; 28.4–29: a 0
        m2 = 0.224 / 0.7 * mus
        expr = f"if(lt(t,28),{mus},if(lt(t,28.4),{mus}+({m2}-{mus})*(t-28)/0.4,if(lt(t,29),{m2}*(29-t)/0.6,0)))"
        fil.append(f"[{k}:a]atrim=start={ms}:duration={dur},asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo,volume='{expr}':eval=frame[a{k}]")
    else:
        v = float(vol)
        if abs(v - 1.4) < 1e-6 and 'toque' in g('id'):
            v = clave
        d = int(round(st * 1000))
        fil.append(f"[{k}:a]atrim=duration={dur},aresample=48000,aformat=channel_layouts=stereo,volume={v},adelay={d}|{d}[a{k}]")
    labs.append(f'[a{k}]'); k += 1
fil.append(''.join(labs) + f'amix=inputs={k}:normalize=0:duration=longest,atrim=duration=30.5,ebur128=peak=true[o]')
cmd = ['ffmpeg', '-nostats', '-v', 'info', *ins, '-filter_complex', ';'.join(fil), '-map', '[o]', '-f', 'null', '-']
r = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='replace')
s = r.stderr
i = s.find('Summary:')
print(re.findall(r'I:\s+(-?[\d.]+) LUFS', s[i:])[0], 'LUFS · true peak', re.findall(r'Peak:\s+(-?[\d.]+) dBFS', s[i:])[0], 'dBTP')
