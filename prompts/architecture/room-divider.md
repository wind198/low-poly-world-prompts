# Room Divider

> **Shared system prompt:** `system/STYLE_AND_ENGINEERING.md` — combine it with this file before asking an AI to implement the model.

## Objective

Create one independent, reusable **room divider** Three.js procedural model for the cohesive low-poly pastel virtual world (garden / park / café / coworking).

## Specific construction instructions

- **Geometry composition:** Tall narrow panel or open shelf frame.
- **Variants:** solid / open-shelf. Support the first variant by default, plus other variants through typed configuration.
- **Approximate outer dimensions:** width 1.80 × depth 0.30 × height 2.10 world units.
- **Placement:** `floor`. Respect the shared system prompt's mounting conventions and explain any attachment-specific origin exception.
- **Silhouette priority:** recognizable in a fixed orthographic isometric view from a normal scene-composer distance. Distinguish the main structural parts using a few clearly separated pastel colors, not intricate details.
- **Constraints:** construct every visible part from minimal built-in Three.js geometry; no external `.glb` / `.obj` assets, no textures, no fine print, no text labels, no photorealistic surfaces.

## Required TypeScript API

```ts
import * as THREE from 'three';

export type RoomDividerVariant = 'solid' | 'open-shelf';
export interface RoomDividerOptions {
  variant?: RoomDividerVariant;
  width?: number;
  depth?: number;
  height?: number;
  primaryColor?: THREE.ColorRepresentation;
  secondaryColor?: THREE.ColorRepresentation;
}

export function createRoomDivider(options?: RoomDividerOptions): THREE.Group;
```

The implementation must preserve the requested approximate bounding box, use sensible default palette tokens from the shared system prompt, and avoid expensive geometry or additional runtime dependencies. Every mesh should be positioned in local coordinates inside the returned group; document how the user places and rotates it in a world composer.

## Verification criteria

- Object is structurally coherent: no separated floating geometry, z-fighting, or invisible important features.
- Main parts and requested variants are recognizable without textures.
- Default no-argument factory works and returns one `THREE.Group`.
- Configurable dimensions and colors take effect predictably.
- Include a short example showing use within an existing Three.js scene.
