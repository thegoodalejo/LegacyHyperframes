# LegacyHyperframes

Proyecto independiente para generar videos (promos, explicativos, demos) a partir de
documentación o briefs, usando [HyperFrames](https://hyperframes.heygen.com) sobre Claude Code.

Nace como extracción del trabajo hecho para el video de presentación de KingdomApp
(`videos/kingdomapp-promo/`), separado para poder reutilizarse con cualquier proyecto/documentación,
no solo con KingdomApp.

## Cómo funciona

Este repo trae instalados los skills de HyperFrames (`.claude/skills/`, `.agents/skills/`) para
Claude Code. Para crear un video nuevo:

1. Abre Claude Code en este repo.
2. Invoca `/hyperframes` — confirma el brief (mensaje, audiencia, duración, fuente de contenido) y
   enruta al workflow correcto (`/faceless-explainer` para texto/doc sin sitio ni captura,
   `/product-launch-video` para un producto/URL, etc.).
3. El proyecto del video queda en `videos/<nombre-del-video>/` con su propio `BRIEF.md`,
   `STORYBOARD.md`, `SCRIPT.md`, composición HTML y assets.

Ver `.claude/skills/hyperframes/` para el mapa completo de workflows y capacidades.

## Estructura

```
videos/
  <nombre-del-video>/
    BRIEF.md            — intención, audiencia, mensaje, duración
    SCRIPT.md            — guion narrado
    STORYBOARD.md         — plan escena a escena
    compositions/         — HTML de cada escena
    assets/                — logo, bgm, sfx, voz
    renders/                — MP4 final
```

## Videos de LegacyEnterprise

`videos/legacyenterprise/` tiene su propio flujo (tutoriales de la wiki con la **interfaz real** grabada, kit de identidad y voz Kokoro local
fija): ver [`videos/legacyenterprise/README.md`](videos/legacyenterprise/README.md). La voz usa el entorno `.venv-tts/` (fuera de git), creado
desde `requirements-tts.txt`.

## Ejemplo incluido

`videos/kingdomapp-promo/` — video de presentación funcional de KingdomApp (161.5s, es),
generado a partir de `docs/modulos-app.md` del monorepo de KingdomApp. Sirve como referencia
de un proyecto completo end-to-end (brief → guion → storyboard → render).

## Requisitos

- [Claude Code](https://claude.com/claude-code)
- Node.js (el CLI de HyperFrames se invoca vía `npx`, sin instalación global)
- Cuenta HeyGen (para voz/BGM vía TTS) si el video lleva narración generada
