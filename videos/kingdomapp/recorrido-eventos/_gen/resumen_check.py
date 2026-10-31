# Resume el último informe de `hyperframes check` (.hyperframes/artifacts/checks/*.json): errores y avisos por sección.
import json, glob, os
f = max(glob.glob('.hyperframes/artifacts/checks/*.json'), key=os.path.getmtime)
d = json.load(open(f, encoding='utf-8'))
print(f, 'ok' if d.get('ok') else 'NO ok')
for k, v in d.items():
    if isinstance(v, dict) and 'findings' in v:
        print('==', k, 'errores', v.get('errorCount'), 'avisos', v.get('warningCount'))
        for x in v['findings']:
            print('  ', x.get('severity'), x.get('code'), (x.get('message') or '')[:220])
