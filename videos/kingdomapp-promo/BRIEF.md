---
workflow: product-launch-video
flow: automation
storyboard: no
message: "KingdomApp reemplaza hojas de cálculo, chats sueltos y apps separadas por una sola plataforma que administra toda la operación de una iglesia multi-sede."
destination: web
aspect: 1920x1080
language: es
audience: pastores y líderes/administradores de iglesias multi-sede evaluando o adoptando software de gestión
length: 161.5s
angle: problem-solution
narration: yes
---

## Intent

Video de presentación funcional de KingdomApp (sistema de gestión de iglesias y ministerios, multi-tenant SaaS), para mostrar en reuniones/juntas administrativas y embeber en material comercial. Ángulo problema → solución: hoy una iglesia coordina membresía, eventos, discipulado, finanzas y comunicación con herramientas sueltas (Excel, WhatsApp personal, papel); KingdomApp lo centraliza todo en una sola app. Tono: profesional pero cálido, confiable — no corporativo/frío, es una herramienta para el cuidado pastoral tanto como para la operación.

**v2 — cobertura completa (revisión explícita del usuario tras ver el preview v1: "le veo muy simplificada la información de lo que hace cada módulo, falta más detalle"):** el usuario compartió su propuesta comercial en PDF (19 páginas, 9 categorías de módulo) como referencia de profundidad y pidió cobertura completa tipo PDF — las 9 categorías (Discipulado y Membresía, Eventos/Accesos, Kids, Kingdom Academy, Finanzas/Wallet, Comunicación, Alabanza, Presencia Digital, Analítica/Reportes) con 3-4 bullets concretos cada una, actualizadas con lo más reciente de la app (separación discipulado/liderazgo + organigrama, WhatsApp con línea propia). Se añade Misiones como diferenciador adicional (no está en el PDF de referencia pero es un módulo real y reciente) y "Totalmente Parametrizable" como cierre de la sección de módulos. Resultado aceptado explícitamente por el usuario: ~2:42 min (161.5s reales, tras generar la narración), en el límite superior de lo que soporta este flujo narrativo especializado.

## Assets

- F:\Proyectos\KingdomApp\frontend\public\kingdom_logo.png — logo oficial de la app; DEBE abrir el video (portada/primer frame).

## Customizations

- Portada de apertura con el logo (requisito explícito del usuario, no opcional).

## Notes

- No hay URL pública capturable de la app (SaaS privado detrás de login) → modo no-capture: construir visuales ilustrados/gráficos (tipografía, íconos, diagramas simples) en vez de capturas reales de pantalla.
- Fuente de contenido/mensajes: F:\Proyectos\KingdomApp\docs\modulos-app.md — documentación funcional en español de cada módulo, en lenguaje de negocio orientado a usuario (no técnico). Usar esa redacción como base para los beats/guion, no leerla literalmente (VO_MODE: restructured — reescribir para narración hablada).
- Revisión de una sola pasada (storyboard: no, elegido explícitamente por el usuario) — sin paradas de revisión intermedia; sí se revisa el preview final antes de renderizar (gate obligatorio).
- Sin sesión de HeyGen bloqueada: usuario autenticado (cuenta alejo.skilled@gmail.com, plan free) — usar voz/BGM vía HeyGen.
