# Genera index.html del clip de Eventos (4:5) a partir de index.tpl.html. Fuente de verdad de los tramos, los toques y los sonidos.
def s(n):
    return f"{n/30:.6f}".rstrip('0').rstrip('.') if n % 30 else str(n // 30)

def ms(rec):
    return f"{rec/30+0.01:.6f}".rstrip('0').rstrip('.')

# (id, clip_ini, clip_fin, rec_ini, rate, comentario, contenedor m = mundo / i = iris)
T = [
 ('v01',0,78,23,1,'0–78 · Servir quieto (grab. 23–100): «Reuniones por reportar» y la fila de la casa; toque en «Reportar» en el 75 (grab. 98)','m'),
 ('v02',78,120,170,1,'78–120 · match cut sobre el toque: el reporte ya cargado (grab. 170–211; la espera «Cargando…» 108–114 queda fuera); entra 1,03 → 1,00','m'),
 ('v03',120,121,212,1,'120 · toque en «Igual que la última vez» (grab. 212)','m'),
 ('v04',121,150,219,1,'121–150 · corte en la onda del botón (213→219): en el 122 las filas ya están marcadas, «7 marcadas» (grab. 220)','m'),
 ('v05',150,180,335,1,'150–180 · la app baja hasta el final de la lista en un cuadro (grab. 291, salto real): «Persona nueva», «Visitantes», «Total: 7 personas»','m'),
 ('v06',180,181,365,1,'180 · toque en «Persona nueva» (grab. 365), dentro del iris','i'),
 ('v07',181,200,380,1,'181–200 · corte en el fundido de la hoja (366→380): la hoja «Persona nueva» ya puesta; el iris la abre desde el botón','i'),
 ('v08',200,262,406,1,'200–262 · quieta (grab. 406–445); toque en «Nombres» en el 240 (grab. 446); «Ximena» 248–260','i'),
 ('v09',262,270,495,1,'262–270 · corte en la pausa (468→495) hasta el toque en «Apellidos» (grab. 503)','i'),
 ('v10',270,298,503,33/28,'270–298 · «Hoyos Vélez» (grab. 503–536), a 1,18× para que termine antes del toque del 300','i'),
 ('v11',298,300,569,1,'298–300 · corte en la pausa (536→569)','i'),
 ('v12',300,315,571,7/15,'300–315 · toque en «Teléfono» (grab. 571) y el campo que se enfoca, a 0,467× (la cámara baja; nadie escribe)','i'),
 ('v13',315,343,578,0.8,'315–343 · «5550198765» (grab. 578–600), a 0,8×, con la cámara quieta','i'),
 ('v14',343,355,635,1,'343–355 · corte en la pausa (600→635); toque en «Mujer» en el 345 (grab. 637), el botón se llena 346–352','i'),
 ('v15',355,377,666,1,'355–377 · quieta (grab. 666–687); toque en «Agregar» en el 375 (grab. 686)','i'),
 ('v16',377,390,694,1,'377–390 · corte en la onda (688→694): la hoja se va 377–378 y en el 379 la fila «Ximena Hoyos Vélez · Nueva» marcada; «Total: 8 personas»','i'),
 ('v17',390,452,754,1,'390–452 · quieta (grab. 754–815); toque en «+» en el 450 (grab. 814)','i'),
 ('v18',452,462,821,1,'452–462 · corte en la espera (816→821): «1» y «Total: 9 personas» en el 452','i'),
 ('v19',462,482,844,1,'462–482 · quieta; toque en «+» en el 480 (grab. 862)','i'),
 ('v20',482,500,870,1,'482–500 · corte en la espera (864→870): «2» y «Total: 10 personas» en el 482','i'),
 ('v21',500,525,894,1,'500–525 · quieta (grab. 894–918)','i'),
 ('v22',525,540,925,1,'525–540 · la app ya bajó 62 px CSS (grab. 919, salto real); la cámara lo compensa en el mismo cuadro: no se ve','i'),
 ('v23',540,602,947,1,'540–602 · quieta; toque en «Guardar asistencia» en el 600 (grab. 1007)','i'),
 ('v24',609,615,1029,1,'609–615 · la barra crece 15 → 66 % (grab. 1030–1034) con la cámara ya quieta en el formulario','i'),
 ('v25',615,617,1154,1,'615–617 · la app subió 66 px CSS (grab. 1090, salto real), compensado por la cámara; toque en «Muy bien» en el 615 (grab. 1154)','i'),
 ('v26',617,622,1160,1,'617–622 · corte en la onda (1156→1160): el radio se llena 618–621','i'),
 ('v27',622,632,1195,1,'622–632 · quieta; toque en «Tema de la palabra» en el 630 (grab. 1203)','i'),
 ('v28',632,645,1213,1.5,'632–645 · «El perdón» (grab. 1213–1232), a 1,5×, con la cámara quieta','i'),
 ('v29',645,662,1293,1,'645–662 · la app bajó 66 px CSS (grab. 1257, salto real), compensado; toque en «Enviar reporte» en el 660 (grab. 1308)','i'),
 ('v30',662,840,1328,1,'662–840 · corte en la espera y la K del cargador (1310→1328): «¡Listo!» con «10 personas.» y «Reportada»; la barra 66 → 100 % en 663–672','i'),
]
TOQUES = [(75,921,801),(120,794,1269),(180,301,1410),(240,585,1443),(270,585,1647),(300,753,1851),(345,330,2094),(375,917,2424),
          (450,546,1929),(480,546,1929),(600,337,2184),(615,251,1188),(630,585,1608),(660,880,2184)]
NOMBRES = {75:'Reportar',120:'Igual que la última vez',180:'Persona nueva',240:'Nombres',270:'Apellidos',300:'Teléfono',345:'Mujer',375:'Agregar',
           450:'+',480:'+',600:'Guardar asistencia',615:'Muy bien',630:'Tema de la palabra',660:'Enviar reporte'}

def vid(t, ind):
    i, a, b, r, rate, c, _ = t
    rr = f"{rate:.6f}".rstrip('0').rstrip('.')
    return (f"{ind}<!-- {c} -->\n"
            f"{ind}<video data-hf-id=\"hf-e{i}\" id=\"{i}\" class=\"clip\" src=\"assets/grabaciones/grabacion.mp4\" muted playsinline data-track-index=\"10\"\n"
            f"{ind}  data-start=\"{s(a)}\" data-duration=\"{s(b-a)}\" data-media-start=\"{ms(r)}\" data-playback-rate=\"{rr}\"></video>\n")

m = ''.join(vid(t, ' ' * 16) for t in T if t[6] == 'm')
iv = ''
for t in T:
    if t[6] != 'i':
        continue
    if t[0] == 'v24':
        iv += ("                  <!-- 602–609 · corte en la espera y la K del cargador (1009→1026): el paso ② «Reporte de la casa de paz (2)» con la barra\n"
               "                       todavía al 15 %; un still del cuadro 1027 (la app no cambia entre 1026 y 1029) sostiene la barra mientras la cámara sube -->\n"
               "                  <img data-hf-id=\"hf-estill2\" id=\"still2\" class=\"clip\" src=\"assets/stills/still-1027.png\" alt=\"\" data-track-index=\"11\"\n"
               "                    data-start=\"20.066667\" data-duration=\"0.233333\" />\n")
    iv += vid(t, ' ' * 18)
marcas = ''
for n, x, y in TOQUES:
    marcas += f"                <!-- {n} · «{NOMBRES[n]}» -->\n"
    marcas += f"                <div data-hf-id=\"hf-etq{n}\" class=\"toque\" id=\"tq-{n}\" style=\"left: calc({x}px * var(--f-k)); top: calc({y}px * var(--f-k))\"></div>\n"
    marcas += f"                <div data-hf-id=\"hf-eon{n}\" class=\"onda\" id=\"on-{n}\" style=\"left: calc({x}px * var(--f-k)); top: calc({y}px * var(--f-k))\"></div>\n"

# Sonidos: (id, archivo, cuadro del sonido = imagen + 1, acento, duración, volumen, pista, comentario)
SND = [
 ('snd-toque-75','identidad/audio/toque.wav',76,0,0.075,1,21,'76 · toque a en «Reportar»'),
 ('snd-toque-120','assets/audio/toque-c.wav',121,0,0.077,1,21,'121 · toque c en «Igual que la última vez» (clave; 1,0 y no 1,4: ver REVIEW §5), con el bajo'),
 ('snd-confirmacion-122','identidad/audio/confirmacion.wav',123,0.1,0.32,1.4,24,'123 · las filas se marcan, «7 marcadas» (122); acento 0,1'),
 ('snd-desliz-150','identidad/audio/desliz.wav',151,0.2,0.36,1,23,'151 · la app baja al final de la lista (salto en el 150); acento 0,2'),
 ('snd-toque-180','assets/audio/toque-b.wav',181,0,0.073,1,21,'181 · toque b en «Persona nueva» (clave; 1,0), con el pico'),
 ('snd-aparicion-195','identidad/audio/aparicion.wav',196,0,0.22,1,22,'196 · la ceja «EVENTOS» (195)'),
 ('snd-toque-240','identidad/audio/toque.wav',241,0,0.075,1,21,'241 · toque a en «Nombres»'),
 ('snd-toque-270','assets/audio/toque-b.wav',271,0,0.073,1,21,'271 · toque b en «Apellidos»'),
 ('snd-toque-300','assets/audio/toque-c.wav',301,0,0.077,1,21,'301 · toque c en «Teléfono»'),
 ('snd-toque-345','identidad/audio/toque.wav',346,0,0.075,1,21,'346 · toque a en «Mujer»'),
 ('snd-toque-375','assets/audio/toque-b.wav',376,0,0.073,1,21,'376 · toque b en «Agregar»'),
 ('snd-aparicion-379','identidad/audio/aparicion.wav',380,0,0.22,1,22,'380 · la fila «Ximena Hoyos Vélez · Nueva» (379)'),
 ('snd-toque-450','assets/audio/toque-c.wav',451,0,0.077,1,21,'451 · toque c en «+»'),
 ('snd-aparicion-452','identidad/audio/aparicion.wav',453,0,0.22,1,22,'453 · «Total: 9 personas» (452)'),
 ('snd-toque-480','identidad/audio/toque.wav',481,0,0.075,1,21,'481 · toque a en «+»'),
 ('snd-aparicion-482','identidad/audio/aparicion.wav',483,0,0.22,1,22,'483 · «Total: 10 personas» (482)'),
 ('snd-toque-600','assets/audio/toque-b.wav',601,0,0.073,1,21,'601 · toque b en «Guardar asistencia» (clave; 1,0), con la segunda subida'),
 ('snd-confirmacion-602','identidad/audio/confirmacion.wav',603,0.1,0.32,1,24,'603 · el paso ② «Reporte» (602); la barra crece 610–614; acento 0,1'),
 ('snd-toque-615','assets/audio/toque-c.wav',616,0,0.077,1,21,'616 · toque c en «Muy bien»'),
 ('snd-toque-630','identidad/audio/toque.wav',631,0,0.075,1,21,'631 · toque a en «Tema de la palabra»'),
 ('snd-toque-660','assets/audio/toque-b.wav',661,0,0.073,1,21,'661 · toque b en «Enviar reporte» (clave; 1,0), con el golpe'),
 ('snd-confirmacion-662','identidad/audio/confirmacion.wav',663,0.1,0.32,1.4,24,'663 · «¡Listo!» (662); acento 0,1'),
]
snd = ''
for i, f, n, ac, d, v, tr, c in SND:
    st = f"{n/30-ac:.6f}".rstrip('0').rstrip('.')
    snd += (f"      <!-- {c} -->\n      <audio data-hf-id=\"hf-e{i}\" id=\"{i}\" src=\"{f}\" data-start=\"{st}\" data-duration=\"{d}\""
            f" data-track-index=\"{tr}\" data-volume=\"{v}\"></audio>\n")

tpl = open('index.tpl.html', encoding='utf-8').read()
out = (tpl.replace('@@M1@@', m.rstrip('\n')).replace('@@IRIS@@', iv.rstrip('\n'))
          .replace('@@MARCAS@@', marcas.rstrip('\n')).replace('@@SONIDOS@@', snd.rstrip('\n'))
          .replace('@@TOQUES@@', ', '.join(str(n) for n, _, _ in TOQUES)))
open(r'F:/Proyectos/LegacyHyperframes/videos/kingdomapp/clip-sitio-eventos/index.html', 'w', encoding='utf-8').write(out)
print('ok')
