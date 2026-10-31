# Genera index.html y compositions/frase-4..9.html del recorrido de Academia (16:9) a partir de _gen/index.tpl.html.
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


GRAB = {'K': 'assets/grabaciones/grabacion.mp4', 'C': 'assets/grabaciones/celular.mp4', 'E': 'assets/grabaciones/escritorio.mp4'}
PISTA = {'cam1': 10, 'cam2': 11, 'cam3': 12, 'iris3a': 13, 'iris3b': 14, 'cam4': 15, 'cam5': 16, 'cam6': 15, 'e1': 17, 'i1': 18, 'e2': 17}

# ── Tramos: (id, ini, fin, grab., velocidad, grabación, contenedor, comentario)
# K = la grabación del clip (clip-sitio-academia, sus 22 tramos tal cual); C = celular.mp4; E = escritorio.mp4.
T = [
 # ── Parte 1: el clip, cuadro por cuadro (clip-sitio-academia/index.html) ──
 ('v01',0,120,0,1,'K','cam1','0–120 · T1: la toma del profesor (grab. 0–119): los cuatro números 3 5 9 8, la barra, el QR, «13 de 18 marcaron» y el temporizador'),
 ('v02',200,270,861,1,'K','cam1','200–270 · T3, fuera de cuadro hasta el látigo del 230–240: «14 de 18 marcaron» y «Faltan (4)» (grab. 861–930)'),
 ('v03',270,273,931,1,'K','cam1','270–273 · toque en «Presente» de Andrea (grab. 931–933)'),
 ('v04',273,300,952,1,'K','cam1','273–300 · corte en la espera (934→952): «15 de 18» (grab. 952–978)'),
 ('v05',300,303,1026,1,'K','cam1','300–303 · toque en «Presente» de Camilo (grab. 1026–1028)'),
 ('v06',303,365,1036,1,'K','cam1','303–365 · corte en la espera (1029→1036): «16 de 18 marcaron»; el látigo del 350–360 se lo lleva'),
 ('v07',100,120,444,1,'K','cam2','100–120 · T2: las cuatro casillas vacías (grab. 444–463); llega con el látigo del 110–120'),
 ('v08',120,135,464,1,'K','cam2','120–135 · el «3» en su casilla'),
 ('v09',135,150,508,1,'K','cam2','135–150 · corte en la pausa: el «5»'),
 ('v10',150,165,552,1,'K','cam2','150–165 · corte en la pausa: el «9»'),
 ('v11',165,180,600,1,'K','cam2','165–180 · corte en la pausa: el «8» y «Enviando…»'),
 ('v12',180,245,626,1,'K','cam2','180–245 · corte en la espera (615→626): «¡Listo! Quedó tu asistencia»'),
 ('v13',340,381,1703,1,'K','cam3','340–381 · T5: Cursos con «Por aprobar 9»; queda debajo del iris del 375'),
 ('v14',375,390,1836,1,'K','iris3a','375–390 · corte en la carga (1822→1836): el grupo «Fundamentos bíblicos», «Lista por aprobar»'),
 ('v15',390,420,1905,1,'K','iris3a','390–420 · la app salta a la lista: «Se gradúan 9 · 9 no se gradúan»'),
 ('v16',420,480,1969,1,'K','iris3a','420–480 · la app salta otra vez: Carolina «No cumple»… y la barra'),
 ('v17',480,484,2036,1,'K','iris3a','480–484 · toque en «Aprobar (9)»'),
 ('v18',484,600,2044,1,'K','iris3a','484–600 · «¿Aprobar la graduación?»'),
 ('v19',600,603,2185,1,'K','iris3a','600–603 · toque en «Aprobar (9)» del diálogo'),
 ('v20',603,615,2206,1,'K','iris3a','603–615 · «Graduado» y «¡Listo! 9 graduados, con su certificado.»'),
 ('v21',615,666,2305,1,'K','iris3a','615–666 · los certificados: Andrea Perea López · 7YU79-NNB7A; queda debajo del iris del 660'),
 ('v22',660,840,2516,1,'K','iris3b','660–840 · «Tu certificado» de Andrea Perea López y el código 7YU79-NNB7A, quieto; el látigo del 830–840 se lo lleva'),

 # ── P9 · El asistente (escritorio, cuenta 101) ──
 ('e01',820,870,33,1,'E','e1','820–870 · «Cursos» con «Nuevo curso», quieto (grab. 33–82); llega con el látigo del 830–840'),
 ('e02',870,885,83,1,'E','e1','870–885 · toque en «Nuevo curso» (grab. 83): las opciones para empezar aparecen en el 877 (grab. 90)'),
 ('e03',885,906,155,1,'E','e1','885–906 · corte en la espera (98→155): las opciones quietas; queda debajo del iris del 900'),
 ('e04',900,915,182,1,'E','i1','900–915 · dentro del iris desde «En blanco» (toque grab. 176): «Paso 1 de 5», el nombre vacío (grab. 182–196)'),
 ('e05',915,960,240,1,'E','i1','915–960 · toque en «Nombre del curso» (grab. 240) y «Matrimonios fuertes» a 1× (teclas 240–282)'),
 ('e06',960,975,741,1,'E','i1','960–975 · corte: «Paso 2 de 5 · Materias y clases» (el «Siguiente» del grab. 740, fuera de cuadro), todavía sin materias'),
 ('e07',975,997,926,2,'E','i1','975–997 · corte en la espera: «Comunicación» ya creada y «Escuchar con amor» a 2× (grab. 926–970)'),
 ('e08',997,1020,1058,2,'E','i1','997–1020 · corte en la espera: «Hablar con verdad» a 2× (grab. 1058–1104)'),
 ('e09',1020,1080,1440,1,'E','i1','1020–1080 · corte: el paso 2 completo, la app ya bajó: «Finanzas en casa» y «El presupuesto familiar» (grab. 1440–1499)'),
 ('e10',1080,1140,1530,1,'E','i1','1080–1140 · corte: «Paso 3 de 5 · Actividades y pesos» (grab. 1530–1589; el «Siguiente» del 1527, fuera de cuadro)'),
 ('e11',1140,1200,2180,1,'E','i1','1140–1200 · corte: «Paso 4 de 5 · Criterios de aprobación» con «Asistencia mínima» marcada al 80 % (grab. 2180–2239)'),
 ('e12',1200,1230,2283,1,'E','i1','1200–1230 · corte: «Paso 5 de 5 · Logro y prerrequisito» (grab. 2283–2312)'),
 ('e13',1230,1260,2390,1/3,'E','i1','1230–1260 · la app ya bajó 100 px CSS al pie (grab. 2390, salto compensado): «Guardar borrador · Publicar», quieto (grab. 2390–2399 a 1/3: cuadros idénticos)'),
 ('e14',1260,1264,2400,1,'E','i1','1260–1264 · toque en «Publicar» (grab. 2400–2403)'),
 ('e15',1264,1330,2406,1,'E','i1','1264–1330 · corte en la carga (2404–2405, «Cargando…»): «¡Publicado!» entra 1264–1268 y se queda (grab. 2406–2471); el látigo del 1310–1320 se lo lleva'),

 # ── P10 · El examen (celular, cuenta 104) ──
 ('c01',1300,1380,77,1,'C','cam4','1300–1380 · «Quiz de los evangelios» · «Pregunta 1 de 3» con el reloj en 1:08 (grab. 77–156; el aviso de los 5 minutos ya se cerró en el 52)'),
 ('c02',1380,1382,157,1,'C','cam4','1380–1382 · toque en «B · Cuatro» (grab. 157–158)'),
 ('c03',1382,1395,164,1,'C','cam4','1382–1395 · corte en la espera (159→164): «Cuatro» marcada'),
 ('c04',1395,1396,237,1,'C','cam4','1395 · toque en «Siguiente» (grab. 237, fuera de cuadro)'),
 ('c05',1396,1410,244,1,'C','cam4','1396–1410 · corte en la espera (238→244): «Pregunta 2 de 3»'),
 ('c06',1410,1440,286,1,'C','cam4','1410–1440 · corte en la espera (258→286): la pregunta 2 quieta, el reloj en 1:01'),
 ('c07',1440,1442,316,1,'C','cam4','1440–1442 · toque en «A · Verdadero» (grab. 316–317)'),
 ('c08',1442,1455,324,1,'C','cam4','1442–1455 · corte en la espera (318→324): «Verdadero» marcada'),
 ('c09',1455,1456,396,1,'C','cam4','1455 · toque en «Siguiente» (grab. 396, fuera de cuadro)'),
 ('c10',1456,1470,404,1,'C','cam4','1456–1470 · corte en la espera (397→404): «Pregunta 3 de 3»'),
 ('c11',1470,1500,446,1,'C','cam4','1470–1500 · corte en la espera (418→446): la pregunta 3 quieta'),
 ('c12',1500,1502,476,1,'C','cam4','1500–1502 · toque en «C · Pablo» (grab. 476–477)'),
 ('c13',1502,1515,483,1,'C','cam4','1502–1515 · corte en la espera (478→483): «Pablo» marcada'),
 ('c14',1515,1516,555,1,'C','cam4','1515 · toque en «Revisar» (grab. 555, fuera de cuadro)'),
 ('c15',1516,1530,562,1,'C','cam4','1516–1530 · corte en la espera (556→562): «Respondiste 3 de 3 · No hay que entregar…», el reloj en 0:53'),
 ('c16',1530,1545,2105,1,'C','cam4','1530–1545 · corte con el salto de tiempo a la vista (576→2105): la misma vista con el reloj en «0:01» (los 70 s de espera, fuera)'),
 ('c17',1545,1560,2160,1,'C','cam4','1545–1560 · el cierre (grab. 2160): «La evaluación cerró. Calculando tu nota…»'),
 ('c18',1560,1620,2223,1,'C','cam4','1560–1620 · corte en la espera (2175→2223): «Tu nota · 5 / 5 · Alcanzó la nota mínima (3)»'),
 ('c19',1620,1690,2840,1,'C','cam4','1620–1690 · la app ya bajó a la lista (salto real del grab. 2835): las tres «Correcta»; el látigo del 1670–1680 se lo lleva'),

 # ── P11 · La sábana (celular, cuenta 103) ──
 ('s01',1640,1740,3166,1,'C','cam5','1640–1740 · la sábana desplazada a la tabla: «Lucía Ruiz Montoya · 4 · 5» en «Quiz de los evangelios» (grab. 3166–3265); llega con el látigo del 1670–1680'),
 ('s02',1740,1800,3083,1,'C','cam5','1740–1800 · corte: la pestaña Notas arriba, con los filtros «Todos · 18 · Cumple · 13 · En riesgo · 1 · No cumple · 4» (grab. 3083–3142, antes de bajar; la misma pantalla del 3271)'),
 ('s03',1800,1803,3271,1,'C','cam5','1800–1803 · toque en «En riesgo · 1» (grab. 3271–3273: la app ya subió al filtro; el toque fue en el 3268)'),
 ('s04',1803,1860,3274,1,'C','cam5','1803–1860 · «En riesgo · 1» marcado (grab. 3274–3330)'),
 ('s05',1860,2050,3354,1,'C','cam5','1860–2050 · la tabla bajó y se corrió hasta «Final» (salto real del grab. 3354): «Ester Gil Mesa · 3 · 1,67 · ⚠ 2,8»; el látigo del 2030–2040 se lo lleva'),

 # ── P12 · El tablero (escritorio, cuenta 101) ──
 ('t01',2020,2100,2620,1,'E','e2','2020–2100 · «Tablero de Academia»: 6 grupos, 86 cursando, 80 %, 4 / 5, 43 %, 0, 89 graduados (grab. 2620–2699); llega con el látigo del 2030–2040'),
 ('t02',2100,2160,2754,1,'E','e2','2100–2160 · la app bajó a «Alumnos en riesgo» (salto real del grab. 2754): Jhon Fredy, Juan David, Esteban, Lucía, Ester…'),
 ('t03',2160,2290,2871,1,'E','e2','2160–2290 · toque en «Jhon Fredy Lezcano Montoya» (grab. 2871): la ficha entra por la derecha 2163–2165 (67 %, «No cumple», 3,96 / 5); el látigo del 2270–2280 se lo lleva'),

 # ── P13 · La verificación pública (celular, sin cuenta) ──
 ('f01',2260,2760,3608,1,'C','cam6','2260–2760 · /verificar, una sola toma a 1× (grab. 3608–4107): toque en el campo en el 2310 (grab. 3658), «7YU79-NNB7A» 2316–2340, toque en «Verificar» en el 2385 (grab. 3733), «Buscando…» 2392 y «Certificado válido» en el 2397 (grab. 3745), quieto hasta el corte'),
]

# Marcas de toque: (cuadro, x, y en px del video, contenedor de marcas, nombre)
TOQUES = [
 (270,906,1368,'cam1','«Presente» de Andrea'), (300,906,1578,'cam1','«Presente» de Camilo'),
 (375,585,900,'cam3','la lista de «Por aprobar» (sin desplazar)'), (480,848,2175,'cam3','«Aprobar (9)»'),
 (600,862,1566,'cam3','«Aprobar (9)» del diálogo'), (660,401,484,'cam3','«Ver» del certificado'),
 (870,1699,151,'e1','«Nuevo curso»'), (900,1044,471,'e1','«En blanco»'), (915,1044,542,'e1','«Nombre del curso»'),
 (1260,1529,954,'e1','«Publicar» (la app ya bajó)'),
 (1380,585,1220,'cam4','«B · Cuatro»'), (1440,585,1022,'cam4','«A · Verdadero»'), (1500,585,1418,'cam4','«C · Pablo»'),
 (1800,239,2019,'cam5','«En riesgo · 1»'),
 (2160,1044,180,'e2','«Jhon Fredy Lezcano Montoya»'),
 (2310,359,504,'cam6','«Código del certificado»'), (2385,908,504,'cam6','«Verificar»'),
]


def vid(t, ind):
    i, a, b, r, rate, g, cont, c = t
    rr = f"{rate:.6f}".rstrip('0').rstrip('.')
    return (f"{ind}<!-- {c} -->\n"
            f"{ind}<video data-hf-id=\"hf-a{i}\" id=\"{i}\" class=\"clip\" src=\"{GRAB[g]}\" muted playsinline data-track-index=\"{PISTA[cont]}\"\n"
            f"{ind}  data-start=\"{s(a)}\" data-duration=\"{s(b-a)}\" data-media-start=\"{ms(r)}\" data-playback-rate=\"{rr}\"></video>\n")


def bloque(cont, ind):
    return ''.join(vid(t, ind) for t in T if t[6] == cont).rstrip('\n')


def marcas(cont, ind):
    out = ''
    cls, pre = ('esc', 'd') if cont in ('e1', 'e2') else ('cel', 'c')
    for n, x, y, c, nom in TOQUES:
        if c != cont:
            continue
        out += f"{ind}<!-- {n} · {nom} -->\n"
        for k in ('toque', 'onda'):
            ab = 'tq' if k == 'toque' else 'on'
            out += (f"{ind}<div data-hf-id=\"hf-a{ab}{n}\" class=\"{k} {cls}\" id=\"{ab}-{n}\""
                    f" style=\"left: calc({x}px * var(--{pre}-k)); top: calc({y}px * var(--{pre}-k))\"></div>\n")
    return out.rstrip('\n')


# Sonidos: (id, archivo, cuadro de la imagen, acento, volumen, pista, comentario). data-start = (imagen + 1) / 30 − acento.
A, B, C = 'identidad/audio/toque.wav', 'assets/audio/toque-b.wav', 'assets/audio/toque-c.wav'
AP, CO, DE = 'identidad/audio/aparicion.wav', 'identidad/audio/confirmacion.wav', 'identidad/audio/desliz.wav'
DUR = {A: 0.075, B: 0.073, C: 0.077, AP: 0.22, CO: 0.32, DE: 0.36}
SND = [
 # Los 20 del clip (sin la subida ni el sonido de marca); toques a 1,0, confirmaciones a 1,4
 ('snd-desliz-120',DE,120,0.2,1.4,23,'el látigo a la alumna'),
 ('snd-aparicion-120',AP,120,0,1,22,'el «3»'),
 ('snd-aparicion-135',AP,135,0,1,22,'el «5»'),
 ('snd-aparicion-150',AP,150,0,1,22,'el «9»'),
 ('snd-aparicion-165',AP,165,0,1,22,'el «8»'),
 ('snd-confirmacion-180',CO,180,0.1,1.4,24,'«¡Listo! Quedó tu asistencia»'),
 ('snd-aparicion-195',AP,195,0,1,22,'la ceja «ACADEMIA»'),
 ('snd-desliz-240',DE,240,0.2,1,23,'el látigo de vuelta al profesor'),
 ('snd-toque-270',A,270,0,1,21,'toque a en «Presente»'),
 ('snd-aparicion-273',AP,273,0,1,22,'«15 de 18»'),
 ('snd-toque-300',B,300,0,1,21,'toque b en «Presente»'),
 ('snd-aparicion-303',AP,303,0,1,22,'«16 de 18»'),
 ('snd-desliz-360',DE,360,0.2,1,23,'el látigo a quien coordina'),
 ('snd-toque-375',C,375,0,1,21,'toque c en la lista de «Por aprobar»'),
 ('snd-desliz-420',DE,420,0.2,1,23,'la lista salta a «No cumple»'),
 ('snd-toque-480',A,480,0,1,21,'toque a en «Aprobar (9)»'),
 ('snd-toque-600',B,600,0,1,21,'toque b en «Aprobar (9)» del diálogo'),
 ('snd-confirmacion-603',CO,603,0.1,1.4,24,'«¡Listo! 9 graduados, con su certificado.»'),
 ('snd-desliz-615',DE,615,0.2,1,23,'la app salta a los certificados'),
 ('snd-toque-660',C,660,0,1,21,'toque c en «Ver»'),
 # Parte 2 (la rotación del toque sigue desde la c del 660)
 ('snd-desliz-840',DE,840,0.2,1.4,23,'el látigo al escritorio (golpe 1,00)'),
 ('snd-toque-870',A,870,0,1,21,'toque a en «Nuevo curso»'),
 ('snd-toque-900',B,900,0,1,21,'toque b en «En blanco» (iris)'),
 ('snd-toque-915',C,915,0,1,21,'toque c en «Nombre del curso»'),
 ('snd-toque-960',A,960,0,1,21,'«Siguiente» (fuera de cuadro) → «Paso 2 de 5» (la costura de la música)'),
 ('snd-toque-1080',B,1080,0,1,21,'«Siguiente» → «Paso 3 de 5»'),
 ('snd-toque-1140',C,1140,0,1,21,'«Siguiente» → «Paso 4 de 5»'),
 ('snd-toque-1200',A,1200,0,1,21,'«Siguiente» → «Paso 5 de 5»'),
 ('snd-toque-1260',B,1260,0,1,21,'toque b en «Publicar»'),
 ('snd-confirmacion-1268',CO,1268,0.1,1.4,24,'«¡Publicado!» entero (1268)'),
 ('snd-desliz-1320',DE,1320,0.2,1,23,'el látigo de vuelta al celular'),
 ('snd-toque-1380',C,1380,0,1,21,'toque c en «Cuatro»'),
 ('snd-toque-1395',A,1395,0,1,21,'«Siguiente» (fuera de cuadro)'),
 ('snd-toque-1440',B,1440,0,1,21,'toque b en «Verdadero»'),
 ('snd-toque-1455',C,1455,0,1,21,'«Siguiente» (fuera de cuadro)'),
 ('snd-toque-1500',A,1500,0,1,21,'toque a en «Pablo»'),
 ('snd-toque-1515',B,1515,0,1,21,'«Revisar» (fuera de cuadro)'),
 ('snd-confirmacion-1560',CO,1560,0.1,1.4,24,'«Tu nota · 5 / 5» (golpe 1,00)'),
 ('snd-desliz-1680',DE,1680,0.2,1,23,'el látigo hacia abajo, al profesor'),
 ('snd-toque-1800',C,1800,0,1,21,'toque c en «En riesgo» (clímax)'),
 ('snd-aparicion-1803',AP,1803,0,1,22,'el filtro marcado, «En riesgo · 1»'),
 ('snd-desliz-1860',DE,1860,0.2,1,23,'la tabla se corre hasta «Final»'),
 ('snd-desliz-2040',DE,2040,0.2,1,23,'el látigo al escritorio'),
 ('snd-desliz-2100',DE,2100,0.2,1,23,'la app baja a «Alumnos en riesgo»'),
 ('snd-toque-2160',A,2160,0,1,21,'toque a en «Jhon Fredy Lezcano Montoya»'),
 ('snd-aparicion-2165',AP,2165,0,1,22,'la ficha académica ya entró (2165)'),
 ('snd-desliz-2280',DE,2280,0.2,1,23,'el látigo de vuelta al celular'),
 ('snd-toque-2310',B,2310,0,1,21,'toque b en «Código del certificado»'),
 ('snd-toque-2385',C,2385,0,1,21,'toque c en «Verificar»'),
 ('snd-confirmacion-2397',CO,2397,0.1,1.4,24,'«Certificado válido» (2397)'),
]


def sonidos(ind):
    out = ''
    for i, f, n, ac, v, tr, c in SND:
        st = f"{(n + 1)/30-ac:.6f}".rstrip('0').rstrip('.')
        out += (f"{ind}<!-- {n + 1} · {c} -->\n{ind}<audio data-hf-id=\"hf-a{i}\" id=\"{i}\" src=\"{f}\" data-start=\"{st}\" data-duration=\"{DUR[f]}\""
                f" data-track-index=\"{tr}\" data-volume=\"{v:g}\"></audio>\n")
    return out.rstrip('\n')


# ── Frases nuevas (SPEC §2.2): (n, escenario, host ini, host fin, líneas [[(palabra, cuadro)]], salida o None, comentario).
#    El host arranca un cuadro antes del primer pulso y cada palabra un cuadro antes del suyo: su primer cuadro visible es su cuadro.
FRASES = [
 (4, 'esc', 842, 1311, [[('Un', 843), ('curso,', 845), ('en', 847), ('cinco', 849), ('pasos.', 851)]], 1306,
  'P9 · Frase 4: «Un curso, en cinco pasos.», una línea sobre la ventana del escritorio; sale 1306–1310, al arrancar el látigo de vuelta'),
 (5, 'cel', 1321, 1682, [[('Exámenes', 1322), ('que', 1324)], [('se', 1326), ('califican', 1328), ('solos.', 1330)]], 1677,
  'P10 · Frase 5: «Exámenes que / se califican solos.»; sale 1677–1681, con el látigo hacia abajo'),
 (6, 'cel', 1681, 2031, [[('Sabes', 1682), ('quién', 1684)], [('va', 1686), ('en', 1688), ('riesgo.', 1690)]], 2026,
  'P11 · Frase 6: «Sabes quién / va en riesgo.»; sale 2026–2030, al arrancar el látigo al escritorio'),
 (7, 'esc', 2042, 2271, [[('Toda', 2043), ('tu', 2045), ('escuela,', 2047), ('de', 2049), ('un', 2051), ('vistazo.', 2053)]], 2266,
  'P12 · Frase 7: «Toda tu escuela, de un vistazo.», una línea sobre el escritorio; sale 2266–2270, al arrancar el látigo'),
 (8, 'cel', 2281, 2519, [[('Y', 2282), ('cualquiera', 2284)], [('lo', 2286), ('verifica.', 2288)]], 2514,
  'P13 · Frase 8: «Y cualquiera / lo verifica.»; sale 2514–2518, antes de la frase del sitio'),
 (9, 'cel', 2518, 2760, [[('Forma', 2519), ('a', 2521), ('los', 2523), ('<em>líderes</em>', 2525)],
                         [('que', 2527), ('tu', 2529), ('visión', 2531), ('necesita', 2533)]], None,
  'P14 · Frase 9: «Forma a los líderes / que tu visión necesita» (el título de Academia en modulos.ts); «líderes» en itálica dorada. Quieta hasta el corte al cierre (2760)'),
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
          font-size: var(--frase-px);
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
          // Cada palabra arranca un cuadro antes de su cuadro (entrada-palabra: blur 6 → 0, 4 cuadros, power4.out, sin desplazarse).
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
                ws.append(f'<em data-hf-id="hf-f{n}e{k}" class="palabra" id="f{n}-w{k}">{txt[4:-5]}</em>')
            else:
                ws.append(f'<span data-hf-id="hf-f{n}w{k}" class="palabra" id="f{n}-w{k}">{txt}</span>')
            pal.append(f"['#f{n}-w{k}', {cu - h0 - 1}]")
        ls.append(f'          <span data-hf-id="hf-f{n}l{li}" class="linea">' + ' '.join(ws) + '</span>')
    salida = ''
    if sal:
        salida = (f"          tl.to('#f{n}', {{ opacity: 0, filter: 'blur(8px)', duration: F(4), ease: 'power3.in' }}, F({sal - h0})); "
                  f"// {sal}–{sal + 4}\n")
    return PLANT_FRASE.format(com=com, m=m, n=n, dur=s(h1 - h0), lineas='\n'.join(ls), pal=', '.join(pal), salida=salida, fin=h1 - h0)


def hosts_frases(ind):
    out = ''
    pistas = {4: 1, 5: 2, 6: 4, 7: 1, 8: 2, 9: 4}
    for n, m, h0, h1, lin, sal, com in FRASES:
        extra = 'data-hold ' if sal is None else ''
        out += (f"{ind}<!-- {com.split(':')[0]} · host {h0}–{h1} -->\n"
                f"{ind}<div data-hf-id=\"hf-ah{n}\" id=\"frase-{n}\" data-composition-id=\"frase-{n}\" data-composition-src=\"compositions/frase-{n}.html\""
                f" data-track-kind=\"graphics\"\n{ind}  {extra}data-start=\"{s(h0)}\" data-duration=\"{s(h1 - h0)}\" data-track-index=\"{pistas[n]}\""
                f" data-width=\"1920\" data-height=\"1080\"></div>\n")
    return out.rstrip('\n')


def main():
    tpl = open(os.path.join(RAIZ, '_gen', 'index.tpl.html'), encoding='utf-8').read()
    rep = {'@@FRASES@@': hosts_frases(' ' * 6), '@@SONIDOS@@': sonidos(' ' * 6),
           '@@TOQUES@@': ', '.join(str(n) for n, *_ in TOQUES)}
    for cont, ind in (('cam1', 16), ('cam2', 16), ('cam3', 16), ('iris3a', 18), ('iris3b', 18), ('cam4', 16), ('cam5', 16), ('cam6', 16),
                      ('e1', 14), ('i1', 16), ('e2', 14)):
        rep[f'@@V-{cont}@@'] = bloque(cont, ' ' * ind)
        rep[f'@@M-{cont}@@'] = marcas(cont, ' ' * (ind + 2))
    out = tpl
    for k, v in rep.items():
        out = out.replace(k, v)
    assert '@@' not in out, [l for l in out.splitlines() if '@@' in l]
    open(os.path.join(RAIZ, 'index.html'), 'w', encoding='utf-8', newline='\n').write(out)
    for f in FRASES:
        open(os.path.join(RAIZ, 'compositions', f'frase-{f[0]}.html'), 'w', encoding='utf-8', newline='\n').write(frase(*f))
    print('ok', len(T), 'tramos,', len(TOQUES), 'marcas,', len(SND), 'sonidos')


if __name__ == '__main__':
    main()
