# Genera index.html y compositions/frase-4..9.html del recorrido de Eventos (16:9) a partir de index.tpl.html.
# Fuente de verdad de los tramos de video, las marcas de toque, los sonidos y las frases nuevas. Uso (desde la raíz del proyecto):
#   python _gen/gen.py
# Los cuadros son del video (30 fps); «grab.» es el cuadro de la grabación. Ver REVIEW.md §2 y §3.
import os

RAIZ = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))


def s(n):
    """cuadro → segundos (texto corto)"""
    return f"{n/30:.6f}".rstrip('0').rstrip('.') if n % 30 else str(n // 30)


def ms(rec):
    """cuadro de la grabación → data-media-start (+0,01 s: cae dentro del cuadro buscado)"""
    return f"{rec/30+0.01:.6f}".rstrip('0').rstrip('.')


GRAB = {'clip': 'assets/grabaciones/grabacion.mp4', 'ss': 'assets/grabaciones/sin-senal.mp4', 'tb': 'assets/grabaciones/tablero.mp4'}

# ── El celular de Jorge (0–1089). (id, ini, fin, grab., velocidad, archivo, contenedor m = mundo / i = iris, comentario)
# v01–v29: el montaje del clip, tal cual (clip-sitio-eventos/REVIEW.md §2). v30 se acorta al 780.
T1 = [
 ('v01',0,78,23,1,'clip','m','0–78 · Servir quieto (grab. 23–100): «Reuniones por reportar» y la fila de la casa; toque en «Reportar» en el 75 (grab. 98)'),
 ('v02',78,120,170,1,'clip','m','78–120 · match cut sobre el toque: el reporte ya cargado (grab. 170–211; la espera «Cargando…» 108–114 queda fuera); entra 1,03 → 1,00'),
 ('v03',120,121,212,1,'clip','m','120 · toque en «Igual que la última vez» (grab. 212)'),
 ('v04',121,150,219,1,'clip','m','121–150 · corte en la onda del botón (213→219): en el 122 las filas ya están marcadas, «7 marcadas» (grab. 220)'),
 ('v05',150,180,335,1,'clip','m','150–180 · la app baja hasta el final de la lista en un cuadro (grab. 291, salto real): «Persona nueva», «Visitantes», «Total: 7 personas»'),
 ('v06',180,181,365,1,'clip','i','180 · toque en «Persona nueva» (grab. 365), dentro del iris'),
 ('v07',181,200,380,1,'clip','i','181–200 · corte en el fundido de la hoja (366→380): la hoja «Persona nueva» ya puesta; el iris la abre desde el botón'),
 ('v08',200,262,406,1,'clip','i','200–262 · quieta (grab. 406–445); toque en «Nombres» en el 240 (grab. 446); «Ximena» 248–260'),
 ('v09',262,270,495,1,'clip','i','262–270 · corte en la pausa (468→495) hasta el toque en «Apellidos» (grab. 503)'),
 ('v10',270,298,503,33/28,'clip','i','270–298 · «Hoyos Vélez» (grab. 503–536), a 1,18× para que termine antes del toque del 300'),
 ('v11',298,300,569,1,'clip','i','298–300 · corte en la pausa (536→569)'),
 ('v12',300,315,571,7/15,'clip','i','300–315 · toque en «Teléfono» (grab. 571) y el campo que se enfoca, a 0,467× (la cámara baja; nadie escribe)'),
 ('v13',315,343,578,0.8,'clip','i','315–343 · «5550198765» (grab. 578–600), a 0,8×, con la cámara quieta'),
 ('v14',343,355,635,1,'clip','i','343–355 · corte en la pausa (600→635); toque en «Mujer» en el 345 (grab. 637), el botón se llena 346–352'),
 ('v15',355,377,666,1,'clip','i','355–377 · quieta (grab. 666–687); toque en «Agregar» en el 375 (grab. 686)'),
 ('v16',377,390,694,1,'clip','i','377–390 · corte en la onda (688→694): la hoja se va 377–378 y en el 379 la fila «Ximena Hoyos Vélez · Nueva» marcada; «Total: 8 personas»'),
 ('v17',390,452,754,1,'clip','i','390–452 · quieta (grab. 754–815); toque en «+» en el 450 (grab. 814)'),
 ('v18',452,462,821,1,'clip','i','452–462 · corte en la espera (816→821): «1» y «Total: 9 personas» en el 452'),
 ('v19',462,482,844,1,'clip','i','462–482 · quieta; toque en «+» en el 480 (grab. 862)'),
 ('v20',482,500,870,1,'clip','i','482–500 · corte en la espera (864→870): «2» y «Total: 10 personas» en el 482'),
 ('v21',500,525,894,1,'clip','i','500–525 · quieta (grab. 894–918)'),
 ('v22',525,540,925,1,'clip','i','525–540 · la app ya bajó 62 px CSS (grab. 919, salto real); la cámara lo compensa en el mismo cuadro: no se ve'),
 ('v23',540,602,947,1,'clip','i','540–602 · quieta; toque en «Guardar asistencia» en el 600 (grab. 1007)'),
 ('v24',609,615,1029,1,'clip','i','609–615 · la barra crece 15 → 66 % (grab. 1030–1034) con la cámara ya quieta en el formulario'),
 ('v25',615,617,1154,1,'clip','i','615–617 · la app subió 66 px CSS (grab. 1090, salto real), compensado por la cámara; toque en «Muy bien» en el 615 (grab. 1154)'),
 ('v26',617,622,1160,1,'clip','i','617–622 · corte en la onda (1156→1160): el radio se llena 618–621'),
 ('v27',622,632,1195,1,'clip','i','622–632 · quieta; toque en «Tema de la palabra» en el 630 (grab. 1203)'),
 ('v28',632,645,1213,1.5,'clip','i','632–645 · «El perdón» (grab. 1213–1232), a 1,5×, con la cámara quieta'),
 ('v29',645,662,1293,1,'clip','i','645–662 · la app bajó 66 px CSS (grab. 1257, salto real), compensado; toque en «Enviar reporte» en el 660 (grab. 1308)'),
 ('v30',662,780,1328,1,'clip','i','662–780 · corte en la espera y la K del cargador (1310→1328): «¡Listo!» con «10 personas.» y «Reportada»; quieto hasta el 779 (grab. 1445)'),
 # P6 · sin señal (sin-senal.mp4, 1170×2532). Su grab. 1050 es idéntica a la 1445 del clip (diferencia media 0,17 de 255): el corte no se ve.
 ('s00',780,781,1051,1,'ss','i','780 · toque en «Volver a la lista» (sin señal, grab. 1051; la pantalla es la misma del clip)'),
 ('s01',781,811,1167,1,'ss','i','781–811 · match cut: la lista de Reportar con el chip «Sin señal» ya puesto (grab. 1167–1196; la lista sin el chip, 1060–1126, queda fuera); toque en la casa en el 810 (grab. 1196)'),
 ('s02',811,813,1197,1,'ss','i','811–813 · la fila tocada (grab. 1197–1198)'),
 ('s03',813,841,1274,1,'ss','i','813–841 · corte en la espera (1199→1274): el reporte de la vencida del 21 de oct, «Vencida» y la nota «Sin señal: …»; toque en «Igual que la última vez» en el 840 (grab. 1301)'),
 ('s04',841,842,1308,1,'ss','i','841 · corte en la onda del botón (1302→1308)'),
 ('s05',842,870,1309,1,'ss','i','842–870 · las filas en ámbar, «8 marcadas» (grab. 1309: las 7 de siempre y Ximena)'),
 ('s06',870,902,1424,1,'ss','i','870–902 · la app ya bajó hasta «Guardar asistencia» (salto real de la grab. 1379, aquí en el 870); toque en «Guardar asistencia» en el 900 (grab. 1454)'),
 ('s07',902,903,1460,1,'ss','i','902 · corte en la onda del botón (1456→1460)'),
 ('s08',903,960,1461,1,'ss','i','903–960 · paso ②: «Sin señal», «1 sin enviar», «Espera señal» y «Guardado en este dispositivo: se enviará solo cuando vuelva la señal.» (grab. 1461–1517, quieta)'),
 ('s09',960,1090,1607,1,'ss','i','960–1090 · vuelve la señal (grab. 1598): corte al primer cuadro sin chips ya asentado (grab. 1607; los de transición 1599–1606 quedan fuera): «Falta el reporte» y el formulario'),
]

# ── El computador del pastor (1080–2760), tablero.mp4 (1920×1080 = 1280×720 CSS a 1,5×).
#    m2 = la cámara del tablero (hasta el iris del 2100); m3 = la ficha, dentro del iris.
T2 = [
 ('d01',1080,1200,817,1,'tb','m2','1080–1200 · el «Tablero de eventos» de la cuenta 101: las cifras cuentan desde 0 (grab. 817–835 → 1080–1098) y quedan quietas'),
 ('d02',1200,1321,988,1,'tb','m2','1200–1321 · la app subió 32 px CSS (grab. 962, salto real), compensado por la cámara en el 1200; toque en «Mapa» en el 1320 (grab. 1108)'),
 ('d03',1321,1381,1299,1,'tb','m2','1321–1381 · match cut: el mapa con teselas y las capas arriba (grab. 1299–1358; la carga 1109–1253 y el desplazamiento quedan fuera); toque en «Dónde viven» en el 1380 (grab. 1358)'),
 ('d04',1381,1471,1371,1,'tb','m2','1381–1471 · corte en la espera de la capa (1359→1371): las zonas donde vive la gente, en violeta (grab. 1371–1460, quieta)'),
 ('d05',1471,1561,1418,1,'tb','m2','1471–1561 · la misma pantalla quieta (grab. 1418–1507); toque en «Zonas sin evento» en el 1560 (grab. 1507)'),
 ('d06',1561,1651,1521,1,'tb','m2','1561–1651 · corte en la espera (1508→1521): la zona sin evento, «2 km · 10 personas» (grab. 1521–1610)'),
 ('d07',1651,1740,1573,1,'tb','m2','1651–1740 · la misma pantalla quieta (grab. 1573–1661; el salto a la leyenda de la 1663 queda fuera)'),
 ('d08',1740,1801,1796,1,'tb','m2','1740–1801 · la app sube a las pestañas (salto real de la grab. 1796); toque en «Eventos» en el 1800'),
 ('d09',1801,1861,1887,1,'tb','m2','1801–1861 · match cut: la lista con el semáforo, lo más urgente arriba (grab. 1887–1946)'),
 ('d10',1861,1922,1978,1,'tb','m2','1861–1922 · quieta (grab. 1978–2038); toque en «Tendencia» en el 1920 (grab. 2037)'),
 ('d11',1922,1950,2039,1,'tb','m2','1922–1950 · la lista ordenada por tendencia (grab. 2039–2066)'),
 ('d12',1950,1975,2111,1,'tb','m2','1950–1975 · la app sube al buscador (salto real de la grab. 2111)'),
 ('d13',1975,2025,2194,1,'tb','m2','1975–2025 · toque en el buscador en el 1980 (grab. 2199); «Jorge Gallego» se escribe 1982–2012 (grab. 2201–2231, 1×)'),
 ('d14',2025,2040,2248,1,'tb','m2','2025–2040 · corte en la espera del filtro (2232→2248): quedan las 4 reuniones de Jorge'),
 ('d15',2040,2106,2355,1,'tb','m2','2040–2106 · la app baja a sus filas (salto real de la grab. 2334); toque en «Casa de Paz Laureles 1» en el 2100; sigue debajo del iris'),
 ('e01',2101,2160,2430,1,'tb','m3','2101–2160 · dentro del iris: la ficha de la casa con su portada (grab. 2430–2488; la carga 2421–2429 queda fuera)'),
 ('e02',2160,2760,2531,1,'tb','m3','2160–2760 · la app baja a la tarjeta «Asistencia» (salto real de la grab. 2531) y queda quieta hasta el cierre (grab. 2531–3130)'),
]

# Toques: (cuadro, x, y en px del video), de toques[] de cada pasos.json
TOQUES1 = [(75,921,801),(120,794,1269),(180,301,1410),(240,585,1443),(270,585,1647),(300,753,1851),(345,330,2094),(375,917,2424),
           (450,546,1929),(480,546,1929),(600,337,2184),(615,251,1188),(630,585,1608),(660,880,2184),
           (780,585,1737),(810,585,882),(840,794,1545),(900,337,2184)]
NOMBRES1 = {75:'Reportar',120:'Igual que la última vez',180:'Persona nueva',240:'Nombres',270:'Apellidos',300:'Teléfono',345:'Mujer',375:'Agregar',
            450:'+',480:'+',600:'Guardar asistencia',615:'Muy bien',630:'Tema de la palabra',660:'Enviar reporte',
            780:'Volver a la lista',810:'Casa de Paz Laureles 1',840:'Igual que la última vez (sin señal)',900:'Guardar asistencia (sin señal)'}
TOQUES2 = [(1320,445,621),(1380,452,160),(1560,686,160),(1800,623,540),(1920,1083,663),(1980,1044,312),(2100,335,659)]
NOMBRES2 = {1320:'Mapa',1380:'Dónde viven',1560:'Zonas sin evento',1800:'Eventos',1920:'Tendencia',1980:'Buscar evento o responsable',
            2100:'Casa de Paz Laureles 1'}


def vid(t, ind):
    i, a, b, r, rate, g, _, c = t
    rr = f"{rate:.6f}".rstrip('0').rstrip('.')
    pista = 12 if g == 'tb' else 10
    return (f"{ind}<!-- {c} -->\n"
            f"{ind}<video data-hf-id=\"hf-e{i}\" id=\"{i}\" class=\"clip\" src=\"{GRAB[g]}\" muted playsinline data-track-index=\"{pista}\"\n"
            f"{ind}  data-start=\"{s(a)}\" data-duration=\"{s(b-a)}\" data-media-start=\"{ms(r)}\" data-playback-rate=\"{rr}\"></video>\n")


def bloque(T, cont, ind):
    out = ''
    for t in T:
        if t[6] != cont:
            continue
        if t[0] == 'v24':
            out += (f"{ind}<!-- 602–609 · corte en la espera y la K del cargador (1009→1026): el paso ② con la barra todavía al 15 %; un still del\n"
                    f"{ind}     cuadro 1027 (la app no cambia entre 1026 y 1029) sostiene la barra mientras la cámara sube -->\n"
                    f"{ind}<img data-hf-id=\"hf-estill2\" id=\"still2\" class=\"clip\" src=\"assets/stills/still-1027.png\" alt=\"\" data-track-index=\"11\"\n"
                    f"{ind}  data-start=\"20.066667\" data-duration=\"0.233333\" />\n")
        out += vid(t, ind)
    return out.rstrip('\n')


def marcas(T, nombres, cls, pre, ind):
    out = ''
    for n, x, y in T:
        out += f"{ind}<!-- {n} · «{nombres[n]}» -->\n"
        out += (f"{ind}<div data-hf-id=\"hf-{pre}tq{n}\" class=\"toque {cls}\" id=\"tq-{n}\""
                f" style=\"left: calc({x}px * var(--{pre}-k)); top: calc({y}px * var(--{pre}-k))\"></div>\n")
        out += (f"{ind}<div data-hf-id=\"hf-{pre}on{n}\" class=\"onda {cls}\" id=\"on-{n}\""
                f" style=\"left: calc({x}px * var(--{pre}-k)); top: calc({y}px * var(--{pre}-k))\"></div>\n")
    return out.rstrip('\n')


# Sonidos: (id, archivo, cuadro del sonido = imagen + 1, acento, volumen, pista, comentario)
A, B, C = 'identidad/audio/toque.wav', 'assets/audio/toque-b.wav', 'assets/audio/toque-c.wav'
AP, CO, DE = 'identidad/audio/aparicion.wav', 'identidad/audio/confirmacion.wav', 'identidad/audio/desliz.wav'
DUR = {A: 0.075, B: 0.073, C: 0.077, AP: 0.22, CO: 0.32, DE: 0.36}
SND = [
 # Los 22 del clip, con sus niveles finales (clip-sitio-eventos/REVIEW.md §5)
 ('snd-toque-75',A,76,0,1,21,'76 · toque a en «Reportar»'),
 ('snd-toque-120',C,121,0,1,21,'121 · toque c en «Igual que la última vez» (clave), con el bajo'),
 ('snd-confirmacion-122',CO,123,0.1,1.4,24,'123 · las filas se marcan, «7 marcadas» (122); acento 0,1'),
 ('snd-desliz-150',DE,151,0.2,1,23,'151 · la app baja al final de la lista (salto en el 150); acento 0,2'),
 ('snd-toque-180',B,181,0,1,21,'181 · toque b en «Persona nueva» (clave), con el pico'),
 ('snd-aparicion-195',AP,196,0,1,22,'196 · la ceja «EVENTOS» (195)'),
 ('snd-toque-240',A,241,0,1,21,'241 · toque a en «Nombres»'),
 ('snd-toque-270',B,271,0,1,21,'271 · toque b en «Apellidos»'),
 ('snd-toque-300',C,301,0,1,21,'301 · toque c en «Teléfono»'),
 ('snd-toque-345',A,346,0,1,21,'346 · toque a en «Mujer»'),
 ('snd-toque-375',B,376,0,1,21,'376 · toque b en «Agregar»'),
 ('snd-aparicion-379',AP,380,0,1,22,'380 · la fila «Ximena Hoyos Vélez · Nueva» (379)'),
 ('snd-toque-450',C,451,0,1,21,'451 · toque c en «+»'),
 ('snd-aparicion-452',AP,453,0,1,22,'453 · «Total: 9 personas» (452)'),
 ('snd-toque-480',A,481,0,1,21,'481 · toque a en «+»'),
 ('snd-aparicion-482',AP,483,0,1,22,'483 · «Total: 10 personas» (482)'),
 ('snd-toque-600',B,601,0,1,21,'601 · toque b en «Guardar asistencia» (clave), con la segunda subida'),
 ('snd-confirmacion-602',CO,603,0.1,1,24,'603 · el paso ② «Reporte» (602); acento 0,1'),
 ('snd-toque-615',C,616,0,1,21,'616 · toque c en «Muy bien»'),
 ('snd-toque-630',A,631,0,1,21,'631 · toque a en «Tema de la palabra»'),
 ('snd-toque-660',B,661,0,1,21,'661 · toque b en «Enviar reporte» (clave), con el golpe'),
 ('snd-confirmacion-662',CO,663,0.1,1.4,24,'663 · «¡Listo!» (662); acento 0,1'),
 # Los del recorrido (SPEC §1.7); toque sigue la rotación desde la b del 661
 ('snd-toque-780',A,781,0,1,21,'781 · toque a en «Volver a la lista»'),
 ('snd-toque-810',B,811,0,1,21,'811 · toque b en la fila de la casa'),
 ('snd-toque-840',C,841,0,1,21,'841 · toque c en «Igual que la última vez», sin señal (golpe 1,00)'),
 ('snd-aparicion-842',AP,843,0,1,22,'843 · las filas se marcan, «8 marcadas» (842)'),
 ('snd-desliz-870',DE,871,0.2,1,23,'871 · la app baja a «Guardar asistencia» (870); acento 0,2'),
 ('snd-toque-900',A,901,0,1,21,'901 · toque a en «Guardar asistencia» (la costura de la música)'),
 ('snd-aparicion-903',AP,904,0,1,22,'904 · el chip «1 sin enviar» y «Espera señal» (903)'),
 ('snd-confirmacion-960',CO,961,0.1,1.4,24,'961 · los chips se van: se envió sola (960); acento 0,1'),
 ('snd-desliz-1080',DE,1081,0.2,1,23,'1081 · el látigo al computador (1080–1088); acento 0,2'),
 ('snd-toque-1320',B,1321,0,1,21,'1321 · toque b en «Mapa»'),
 ('snd-toque-1380',C,1381,0,1,21,'1381 · toque c en «Dónde viven»'),
 ('snd-toque-1560',A,1561,0,1,21,'1561 · toque a en «Zonas sin evento» (golpe 1,00)'),
 ('snd-aparicion-1561',AP,1562,0,1,22,'1562 · aparece la zona sin evento (1561)'),
 ('snd-desliz-1740',DE,1741,0.2,1,23,'1741 · la app sube a las pestañas (1740); acento 0,2'),
 ('snd-toque-1800',B,1801,0,1,21,'1801 · toque b en «Eventos» (clímax)'),
 ('snd-toque-1920',C,1921,0,1,21,'1921 · toque c en «Tendencia»'),
 ('snd-toque-1980',A,1981,0,1,21,'1981 · toque a en el buscador'),
 ('snd-toque-2100',B,2101,0,1,21,'2101 · toque b en «Casa de Paz Laureles 1»'),
]


def sonidos(ind):
    out = ''
    for i, f, n, ac, v, tr, c in SND:
        st = f"{n/30-ac:.6f}".rstrip('0').rstrip('.')
        out += (f"{ind}<!-- {c} -->\n{ind}<audio data-hf-id=\"hf-e{i}\" id=\"{i}\" src=\"{f}\" data-start=\"{st}\" data-duration=\"{DUR[f]}\""
                f" data-track-index=\"{tr}\" data-volume=\"{v:g}\"></audio>\n")
    return out.rstrip('\n')


# ── Frases nuevas (SPEC §1.2 y §2.1): (n, mundo, host ini, host fin, líneas [[(palabra, cuadro)]], salida o None, comentario).
#    El host arranca un cuadro antes del primer pulso y cada palabra un cuadro antes del suyo: su primer cuadro visible es el pulso.
FRASES = [
 (4, 'cel', 719, 961, [[('¿Sin', 720), ('señal?', 722)], [('La', 724), ('asistencia', 726), ('se', 728), ('guarda', 730)]], 956,
  'P6 · Frase 4: «¿Sin señal? / La asistencia se guarda» (lo que dice la app, ev3.sin_red_reporte). Palabra a palabra cada 2 cuadros desde el golpe del 720; sale 956–960'),
 (5, 'cel', 959, 1078, [[('Y', 960), ('se', 962), ('envía', 964), ('sola', 966)], [('al', 968), ('volver', 970), ('la', 972), ('señal', 974)]], 1072,
  'P6 · Frase 5: «Y se envía sola / al volver la señal» (textual de la nota de la app). Desde el 960, cuando los chips se van; sale 1072–1076, antes del látigo'),
 (6, 'esc', 1139, 1321, [[('El', 1140), ('pastor', 1142), ('lo', 1144), ('ve', 1146), ('todo', 1148)]], 1316,
  'P7 · Frase 6: «El pastor lo ve todo», una línea sobre la ventana del computador; sale 1316–1320, con el toque en «Mapa»'),
 (7, 'esc', 1559, 1801, [[('Y', 1560), ('dónde', 1562), ('falta', 1564), ('una', 1566), ('reunión', 1568)]], 1796,
  'P8 · Frase 7: «Y dónde falta una reunión», en el golpe más fuerte (2.ª vez), con «Zonas sin evento»; sale 1796–1800'),
 (8, 'esc', 1799, 2075, [[('Cuál', 1800), ('crece', 1802), ('y', 1804), ('cuál', 1806), ('necesita', 1808), ('apoyo', 1810)]], 2070,
  'P9 · Frase 8: «Cuál crece y cuál necesita apoyo», en el clímax con la lista de eventos (entra mientras sale la 7: blur swap); sale 2070–2074'),
 (9, 'esc', 2579, 2760, [[('Cada', 2580), ('<em>reunión</em>', 2582), ('cuenta,', 2584), ('y', 2586), ('cuenta', 2588), ('bien', 2590)]], None,
  'P11 · Frase 9: «Cada reunión cuenta, y cuenta bien» (el título de Eventos en modulos.ts); «reunión» en itálica dorada. Quieta hasta el corte al cierre (2760)'),
]

PLANT_FRASE = '''<!doctype html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <!-- {com}. Posición y tamaño: --{m}-* del host (SPEC §1.4). Generado por _gen/gen.py. -->
  </head>
  <body>
    <template>
      <style>
        #root {{
          position: absolute;
          inset: 0;
          width: 1920px;
          height: 1080px;
          overflow: hidden;
        }}
        .f-frase {{
          position: absolute;
          left: var(--{m}-frase-x);
          top: var(--{m}-frase-y);
          width: var(--{m}-frase-ancho);
          font-size: var(--{m}-frase-px);
          color: var(--k-noche-tinta);
          --k-enfasis: var(--k-noche-dorado);
          text-wrap: initial;
        }}
        .linea {{
          display: block;
          white-space: nowrap;
        }}
        .palabra {{
          display: inline-block;
        }}
      </style>
      <div data-hf-id="hf-f{n}00" id="root" data-composition-id="frase-{n}" data-width="1920" data-height="1080" data-duration="{dur}">
        <div data-hf-id="hf-f{n}01" class="k-titular f-frase" id="f{n}">
{lineas}
        </div>
      </div>
      <script>
        (function () {{
          const F = (n) => n / 30;
          const tl = gsap.timeline({{ paused: true }});
          // Cada palabra arranca un cuadro antes de su pulso (entrada-palabra: blur 6 → 0, 4 cuadros, power4.out, sin desplazarse).
          [{pal}].forEach(([sel, n]) => {{
            tl.fromTo(sel, {{ opacity: 0, filter: 'blur(6px)' }}, {{ opacity: 1, filter: 'blur(0px)', duration: F(4), ease: 'power4.out' }}, F(n));
          }});
{salida}          tl.set({{}}, {{}}, F({fin}));
          window.__timelines['frase-{n}'] = tl;
        }})();
      </script>
    </template>
  </body>
</html>
'''


def frase(n, m, h0, h1, lineas, sal, com):
    k = 0
    ls, pal = [], []
    for li, lin in enumerate(lineas):
        ws = []
        for txt, cu in lin:
            k += 1
            if txt.startswith('<em>'):
                ws.append(f'<em data-hf-id="hf-f{n}e{k}"><span data-hf-id="hf-f{n}w{k}" class="palabra" id="f{n}-w{k}">{txt[4:-5]}</span></em>')
            else:
                ws.append(f'<span data-hf-id="hf-f{n}w{k}" class="palabra" id="f{n}-w{k}">{txt}</span>')
            pal.append(f"['#f{n}-w{k}', {cu - h0 - 1}]")
        ls.append(f'          <span data-hf-id="hf-f{n}l{li}" class="linea">' + ' '.join(ws) + '</span>')
    salida = ''
    if sal:
        salida = (f"          tl.to('#f{n}', {{ opacity: 0, filter: 'blur(8px)', duration: F(4), ease: 'power3.in' }}, F({sal - h0})); "
                  f"// {sal}–{sal + 4}\n")
    return PLANT_FRASE.format(com=com, m=m, n=n, dur=s(h1 - h0), lineas='\n'.join(ls), pal=', '.join(pal), salida=salida, fin=h1 - h0)


def main():
    tpl = open(os.path.join(RAIZ, '_gen', 'index.tpl.html'), encoding='utf-8').read()
    out = (tpl.replace('@@M1@@', bloque(T1, 'm', ' ' * 16)).replace('@@IRIS@@', bloque(T1, 'i', ' ' * 18))
              .replace('@@M2@@', bloque(T2, 'm2', ' ' * 16)).replace('@@M3@@', bloque(T2, 'm3', ' ' * 18))
              .replace('@@MARCAS1@@', marcas(TOQUES1, NOMBRES1, 'cel', 'c', ' ' * 16))
              .replace('@@MARCAS2@@', marcas(TOQUES2, NOMBRES2, 'esc', 'd', ' ' * 16))
              .replace('@@SONIDOS@@', sonidos(' ' * 6))
              .replace('@@TOQUES1@@', ', '.join(str(n) for n, _, _ in TOQUES1))
              .replace('@@TOQUES2@@', ', '.join(str(n) for n, _, _ in TOQUES2)))
    assert '@@' not in out
    open(os.path.join(RAIZ, 'index.html'), 'w', encoding='utf-8', newline='\n').write(out)
    for f in FRASES:
        open(os.path.join(RAIZ, 'compositions', f'frase-{f[0]}.html'), 'w', encoding='utf-8', newline='\n').write(frase(*f))
    print('ok')


if __name__ == '__main__':
    main()
