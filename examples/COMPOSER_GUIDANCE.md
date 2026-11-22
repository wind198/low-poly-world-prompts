# Composer integration guidance

## Minimal contract

Each generated asset factory returns `THREE.Group` and accepts typed appearance/dimension options. The scene composer owns transforms, selection state, persistence, disposal policy, camera, lights and renderer; the factory owns object-local geometry only.

## Suggested registry metadata

- `id`: stable catalog key, e.g. `cafe/espresso-machine`
- `placement`: `floor | surface | wall | ceiling | water`
- `dimensions`: approximate outer bounding box from `catalog/assets.json`
- `variant`: a typed factory option, stored with scene instances
- `transform`: scene-specific position/rotation/scale (never embedded in asset definition)
- `anchors`: optional named surface mount points on parent objects, e.g. countertop attachments

## Recommended editor behavior

- Create thumbnails using one shared orthographic camera and consistent lighting.
- Snap floor assets to grid; surface assets to designated collision/attachment surfaces.
- Use bounds for rough collision checks; allow precise hand placement where needed.
- Save scene instances as `{ assetId, variant, props, transform }`, not serialized Three.js meshes.
- Put repeated instances behind geometry/material caches; use `InstancedMesh` selectively for abundant small items.
- Validate component assets in isolation before adding world-building prefabs.

## Prompt QA workflow

1. Combine system prompt and asset prompt using `scripts/compose_prompt.py`.
2. Generate code in your actual Three.js repository.
3. Run type-check/lint and inspect in a consistent isometric asset workbench.
4. Verify silhouette, bounds, pivot, shadows, configurable variants, and resource reuse.
5. If model fails, refine only its component prompt; adjust system prompt only for cross-asset defects.
