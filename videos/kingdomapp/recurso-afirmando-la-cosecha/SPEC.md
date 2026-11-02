# SPEC: Afirmando la cosecha con Kingdom

Storyboard escena por escena. Hay dos clases de escenas:

- **«Estrategia»:** motion design del kit v1.2 (`frame.md` = `_identidad/frame-recurso.md`), con las reglas del Recurso 3: texto cinético, nodos, puntos y chips.
- **«App»:** la interfaz de v2 **recreada en HTML**, la variante «Para líderes» del kit v1.3 (decisión 241). Se ve en `.k-telefono` (pantalla de celular sin el aparato dibujado) o en `.k-ventana-escritorio`, con el texto cinético corto en la otra columna o como titular encima.

Los tiempos salen de `KRecurso.tiempos()`: cada gesto cae en el pulso de la palabra que lo nombra.

## Reglas de la app recreada (fidelidad)

1. **Estructura y textos de las capturas reales** (`assets/referencias/*.webp`, de `frontend-v2/src/ayuda/medios.json`, Kingdom Demo).
   - Se copian iguales el orden de los elementos, las etiquetas, los íconos (Material Symbols), las pestañas, los chips y los botones.
   - Los textos se toman de la captura o de `frontend-v2/public/i18n/es.json`, nunca de memoria. Donde la clave lleva `{v_acompanante}`, va «Acompañante».
2. **Colores y forma de la marca por defecto de Kingdom** (`frontend-v2/src/styles/_tokens.scss`, tema claro):
   - primario `#015bbe` y su contenedor `#d7e2ff`;
   - secundario `#7d5800`; el contenedor del secundario es el chip elegido (sacar el valor del archivo);
   - superficie `#faf9fd`, texto `#1b1b1f`, contenedor de superficie `#efedf1` y borde `#c4c6d0`.

   Letra Inter. Tarjetas de radio 16, diálogos de 28, chips en píldora.

   Las capturas son de Kingdom Demo, que tiene marca violeta. La recreación usa la marca por defecto, que es lo que ve una iglesia sin colores propios. En la barra superior va el logo K de Kingdom y «Kingdom Demo».
3. **Celular:**
   - Ancho lógico de 390 px escalado para que mida unos 820–860 px de alto en el cuadro de 1080.
   - Barra superior: logo, nombre, apps, campana, ayuda y avatar.
   - Barra inferior: Inicio, Mi iglesia y Perfil.
4. **Escritorio:** riel izquierdo (Inicio, Ajustes, Mi iglesia, Perfil), barra superior y pestañas de Membresía (Personas, Seguimiento, Coordinar, Estructura, Tableros, …).
5. **Gestos y cámara:**
   - `.k-dedo`: círculo con onda que cae en el elemento y lo «presiona», con un estado de presionado de 120 ms.
   - `H.escribir()`: el texto aparece letra por letra con su cursor.
   - `H.camara()`: zoom de 1,0 a 1,8 y paneo, `power2.inOut` de 0,8–1,2 s.
   - `.k-foco`: oscurece el resto al 55 % y pone un anillo dorado redondeado sobre el elemento.
   - Las hojas y los diálogos suben como en Material 3.

   Todo determinista y que se pueda buscar en la línea de tiempo (una sola línea de tiempo de GSAP en pausa).
6. **Los datos:** personas ficticias (ver el BRIEF) y fechas relativas. Toda cifra visible (cupos, conteos, embudo) lleva `.k-datos-ejemplo`.
7. **Prohibido:**
   - pantallas o funciones que no estén en las capturas ni en la ayuda;
   - teléfonos con aparato dibujado;
   - logos de terceros (Google y WhatsApp se nombran, no se dibujan);
   - el nombre del libro o de su autor.

## Fuentes (rutas en KingdomApp)

| Clave | Archivo |
|---|---|
| [MS] | `frontend-v2/src/ayuda/es/membresia/mi-seguimiento.md` |
| [CO] | `frontend-v2/src/ayuda/es/membresia/coordinar-el-seguimiento.md` |
| [RP] | `frontend-v2/src/ayuda/es/membresia/registrar-una-persona.md` |
| [RC] | `frontend-v2/src/ayuda/es/membresia/ruta-de-crecimiento.md` |
| [TA] | `frontend-v2/src/ayuda/es/membresia/tableros.md` |
| [SA] | `frontend-v2/src/ayuda/es/membresia/semaforo-de-actividad.md` |
| [AE] | `frontend-v2/src/ayuda/es/membresia/actividad-extra.md` |
| [BF] | `frontend-v2/src/ayuda/es/membresia/buscar-y-filtrar.md` |
| [VO] | `frontend-v2/src/ayuda/es/membresia/ajustes-vocabulario.md` |
| [QR] | `frontend-v2/src/ayuda/es/portal/qr-de-bienvenida.md` |
| [AU] | `frontend-v2/src/ayuda/es/comunicaciones/automatizaciones.md` y `src/app/services/comunicaciones/automatizaciones.ts:45-48` (ejemplo «Bienvenida a quien llega», 60 minutos después de `membresia.persona_creada`) |
| [AV] | `backend/avisos/catalogo.json` («Alguien nuevo para acompañar») |
| [PP] | `frontend-v2/src/ayuda/es/ajustes/personas-y-permisos.md` y `backend/permisos/catalogo.json` (plantilla «Sirve» de Membresía: alcance «a su cargo») |
| [L] | El libro de acogida que entregó el dueño (ideas en palabras propias; **no se nombra**) |

## Escenas

### intro (kit, 6 s)
Título «Afirmando la *cosecha* con Kingdom» y ceja «Recursos · Para líderes».

### gancho (Estrategia) [L]
- Doce puntos dorados (las personas nuevas) entran a una franja de altar. Se cuentan «12» con «Datos de ejemplo».
- En «vuelven» la mayoría se apaga y se va. En «lunes» aparece un calendario con el lunes vacío y un teléfono que no suena (ícono `call`, tenue).
- En «afirmación» la ceja dice «Para el equipo de afirmación».
- En «quede» los puntos vuelven a encenderse y se unen en un grupo.

### cap-1 (kit): «El camino del *nuevo*» · `route`

### camino (Estrategia) [L]
- Un camino horizontal con cuatro etapas: «Te conoce», «Decide», «Vive el domingo» y «Dice sí».
- El punto dorado avanza etapa por etapa en el pulso de cada palabra clave.
- En «tuyo» se ilumina en dorado el tramo entre «Vive el domingo» y «Dice sí», con el rótulo «Afirmación».
- En «camino» el camino sigue más allá del domingo: la línea cruza un rótulo «Lunes» y continúa.
- En «llega» la cámara gira la mirada: aparece un ojo (`visibility`) sobre el punto dorado, que es quien evalúa.

### cap-2 (kit): «Que nadie se quede *sin nombre*» · `person_add`

### registro (App, celular) [QR][RP]
- **Referencias:** `portal__qr-de-bienvenida__01-lista`, `membresia__registrar-una-persona__01-formulario`, `__02-registrar` y `__03-ya-esta`.
- **«registro»:** el celular entra en la columna derecha.
- **«QR de bienvenida»:** una tarjeta de QR grande, la de «Ver en grande (proyectar)», y un punto dorado que la escanea. Después el celular muestra «Nueva persona».
- **«Nueva persona»:** el dedo toca el acceso. Se escriben con `H.escribir()` «Valeria» en Nombres*, «Cardona Ríos» en Apellidos y un teléfono ficticio con el +57.
- **«Cómo llegó»:** foco más zoom a «Cómo llegó*»; el dedo abre la lista y elige «Invitación de alguien» (es una forma de llegar que ya está en la lista: ver la referencia `coordinar…02-nuevos`).
- **«invitó»:** paneo hacia abajo hasta «Quién lo invitó» (la referencia `02-registrar`), con foco; se escribe y se elige «Marta Gómez».
- **Coherencia:** los pasos que salen después (en `llamada` y `ruta`) son los del **flujo de fábrica de esa forma de llegar**. Verificarlos en el código (la plantilla de fábrica de la ruta en `backend/_datos/`, buscar «Llamada de bienvenida») y usarlos tal cual.
- **«llegada»:** sube la hoja «¿Ya está registrada?» con una persona parecida, y el dedo toca «Es esta: registrar su llegada».
- **«llamada de bienvenida»:** sale la confirmación y un chip «Llamada de bienvenida» (el primer paso) aparece junto a la persona.

### cap-3 (kit): «Repartir la *cosecha*» · `diversity_3`

### repartir (App, escritorio) [CO][AV]
- **Referencias:** `membresia__coordinar-el-seguimiento__02-nuevos` y `__01-resumen`.
- **«Coordinar»:** la ventana de escritorio con la pestaña «Coordinar» activa y el chip «Nuevos 12». Debajo, «12 personas nuevas esperan Acompañante.» y la lista con cómo llegó, la fecha y la red.
- **«Repartir»:** foco en el botón «Repartir» y el dedo lo toca. Las filas vuelan en arco a tres columnas, una por acompañante (Marta, Julián y Ana), con «Acompaña a N de M» en cada una.
- **«Asignar»:** foco en «Asignar» de una fila.
- **«acompañar»:** en un celular pequeño que entra por un lado cae el aviso «Alguien nuevo para acompañar» (estilo de notificación de la app, sin logos de terceros).
- **«carga»:** el chip «Quienes acompañan», con tarjetas de carga y los pendientes «2 en rojo» y «1 sin llamar». No hay captura de esta vista: se arma con los textos de [CO] y de i18n.
- **«resumen»:** el chip «Resumen», con las tarjetas de cifras de la referencia `01-resumen`: «En rojo», «Sin llamar a tiempo», «Nuevos sin Acompañante», «Por vencer», «En ruta», con números de ejemplo. Zoom a «En rojo» y «Sin llamar a tiempo».

### cap-4 (kit): «La llamada que *abraza*» · `call`

### llamada (App, celular) [MS]
- **Referencias:** `membresia__mi-seguimiento__01-lista`, `__02-reporte` y `__03-resultado`.
- **«llamada»:** a la izquierda, el texto cinético con el contraste entre «informa» (gris) y «abraza» (dorado).
- **«Mi seguimiento»:** el celular con «Mi seguimiento», la pestaña «Seguimiento» y el chip «Acompañados 3». La tarjeta de Valeria lleva «Por vencer», el paso «Llamada de bienvenida», «Hace 1 día · vence en 1 día» y «Después: …», con el paso siguiente del flujo de fábrica de «Invitación de alguien».
- **«a tiempo»:** foco en el chip del semáforo, que cambia de «A tiempo» a «Por vencer» y luego a «Vencido» y vuelve.
- **«Marcar cumplido»:** el dedo toca el teléfono de la tarjeta (onda) y luego «Marcar cumplido». Sube el diálogo «Reporte del paso» y se marca «Contestó». En «Petición de oración» se escribe «Por su familia», y en «Observaciones», «Quiere conocer la casa de paz».
- **«intento»:** foco en «Solo registrar el intento».
- **«siguiente»:** el dedo toca «Marcar cumplido» y el diálogo cambia al resultado: «"Llamada de bienvenida" cumplido · Ahora va en: …», con los botones «Elegir otro paso» y «Listo». Usar el paso siguiente real del flujo de fábrica.
- **«formulario»:** un recuadro sobre el formulario con un rótulo del kit: «Tu formulario». No se recrea el editor.

### consejos (Estrategia) [L][AU][AE]
- Cinco tarjetas `.k-recurso-tarjeta` que entran de a una:
  - «Preséntate y da gracias» (`waving_hand`);
  - «Escucha más de lo que hablas» (`hearing`);
  - «Ora, si te lo permite» (`volunteer_activism`);
  - «Breve, sin preguntas personales» (`timer`);
  - «Invita a algo concreto» (`event`).
- **«bienvenida»:** un globo de mensaje con «1 h después» y el rótulo «Si tu iglesia tiene Comunicaciones».
- **«actividad extra»:** un chip «Actividad extra: Visita · Consejería · Oración».

### cap-5 (kit): «De visitante a *familia*» · `diversity_1`

### ruta (App, celular, y diagrama) [RC][MS]
- **Referencias:** `membresia__la-ficha__02-tarjetas` (tarjeta «Avance») y `membresia__mi-seguimiento__01-lista` (chip «Casa de paz · ¿cuál?»).
- **«ruta de crecimiento»:** a la izquierda, los pasos de fábrica como una escalera de chips: Llega a la iglesia → Se conecta con una casa de paz → Inicia clases de la visión → Empieza a servir.
- **«solos»:** tres pasos se marcan solos con un rayo pequeño y los rótulos «al asistir», «al empezar un curso» y «al unirse a un equipo».
- **«cercanas»:** en el celular, foco en el chip «Casa de paz · ¿cuál?» y el dedo lo toca. No se recrea la lista de cercanas: el chip late y sale el rótulo «Las más cercanas».
- **«logro»:** una medalla del kit y el texto «¡Se conectó con la iglesia!» con confeti mínimo del kit (sin partículas libres).

### semaforo (Estrategia) [SA]
- Cuatro puntos: verde, amarillo, rojo y «Sin actividad», con las reglas de color del Recurso 3.
- **«semáforo de actividad»:** un punto pasa de verde a amarillo mientras corren tres íconos de «sin»: `event_busy`, `school` y `smartphone`.
- **«llamada»:** el punto amarillo se convierte en una persona con un teléfono que suena.

### cap-6 (kit): «Lo que se mide, *se cuida*» · `monitoring`

### tableros (App, escritorio y celular) [TA][BF]
- **Referencias:** `membresia__tableros__02-ruta`, `__01-resumen` y `membresia__buscar-y-filtrar__04-filtrada`.
- **«Tableros»:** la ventana de escritorio con «Tableros» y el chip «Ruta». Las barras del «Embudo del flujo» crecen paso a paso, con los conteos, el % y los días promedio de ejemplo.
- **«Estancados»:** paneo hacia abajo hasta «Estancados» (el título es de [TA]; la tarjeta se arma con su texto), con foco.
- **«funciona»:** el chip «Personas» y las barras de «nuevas por forma de llegar» (Casa de paz, Invitación, Culto o evento, Redes) de ejemplo.
- **«filtros»:** el celular con la lista filtrada (referencia `04-filtrada`) y los chips de filtro «Fecha de llegada: este mes» y «Red: Sin red».
- **«reunión»:** de vuelta al escritorio, el dedo toca el botón de descarga y sale el menú «PDF» / «Excel».
- **«nuestra»:** a la izquierda, el texto cinético con un globo de pregunta (`forum`).

### cap-7 (kit): «Afirmados que *afirman*» · `all_inclusive`

### multiplicar (Estrategia, con un toque de App) [CO][PP][VO]
- Un punto dorado (Valeria) se vuelve azul (acompañante) y de él salen dos dorados nuevos. El patrón se repite dos veces: multiplicación.
- **«cupo»:** una tarjeta de «Quienes acompañan» con «Acompaña a 0 de 3» (recreada, de ejemplo).
- **«solo»:** un candado sobre la tarjeta de una persona.
- **«consolidadores»:** un campo recreado «Acompañante» que se borra y se escribe «Consolidador» con `H.escribir()`, como en Ajustes → Vocabulario.
- **«familia»:** los puntos se agrupan en una forma de casa.

### resumen (Estrategia)
Cinco verbos en fila con sus íconos: Registra (`person_add`), Reparte (`diversity_3`), Llama (`call`), Acompaña (`route`) y Mide (`monitoring`). Al final, «alguien que Dios te *confió*».

### llamado (kit) y cierre (kit, llamado `acompanamiento`, contacto `whatsapp`)
