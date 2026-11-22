# Low-Poly Three.js World — Prompt Repository

**189 component-specific prompts** organized into **8 groups**, plus one shared system prompt, machine-readable asset registry, and coverage validator. This repository contains **prompts**, not prebuilt Three.js models.

## Repository structure

```text
system/STYLE_AND_ENGINEERING.md     shared visual theme + TypeScript contract
catalog/INDEX.md                   grouped, clickable component list
catalog/assets.json                machine-readable registry + geometry + bounds
prompts/<category>/<asset>.md      exactly one implementation prompt per asset
scripts/validate.py                verifies registry/prompt completeness
scripts/compose_prompt.py          emits system + selected asset prompt
examples/COMPOSER_GUIDANCE.md      recommendations for integration into asset editor
```

## Usage

1. Browse [`catalog/INDEX.md`](catalog/INDEX.md) and choose a component.
2. Combine the shared system instructions with the corresponding component prompt, maintaining system > component priority.
3. Paste into your coding agent, or use the compose script:

```bash
python scripts/compose_prompt.py cafe/espresso-machine > espresso-machine-prompt.md
python scripts/compose_prompt.py nature/round-canopy-tree > tree-prompt.md
```

4. Generate one `.ts` file implementing the factory. Validate its appearance in your asset workbench before registering it in the composer.

## Validate repository

```bash
python scripts/validate.py
```

## Design conventions

- Units are meters-ish: 1 Three.js world unit ~= 1 meter. +Y up; +Z front.
- Each object returns one `THREE.Group` with typed options.
- Matte solid colors, pastel palette, primitive-only geometry, minimal polygon count.
- Floor/surface object origins are bottom-center. Wall, water, ceiling objects use documented mounting conventions.
- Components are standalone; complex assemblies should compose these primitives/objects rather than duplicate them.
- `catalog/assets.json` includes placement and dimensions for future snap-to-surface placement and editor search.

## Scope

Groups and counts:

- `nature`: 23
- `outdoor-architecture`: 20
- `park-street`: 24
- `cafe`: 28
- `workspace`: 26
- `architecture`: 20
- `lighting-decor`: 16
- `small-props`: 32

### Recommended build path

Build shared geometry helpers first, then Nature and Architecture foundation, then furniture and props. Generate assets individually, inspect in an orthographic workbench, and add only reviewed factories to the real asset library. Asset definitions are *prompt specs*; generated TypeScript should live in a separate source package, not inside `prompts/`.
