# Figma production

Owns inspectable, editable Figma artifacts. Relevant tool skills own API mechanics.

## Inspect first

Identify file/page/node scope, existing library components, variants/properties, variables/modes, styles, fonts, naming and code mappings. Record inaccessible libraries instead of recreating them as if absent. Consult current official documentation when capability/API support is uncertain.

Use existing tokens/components before creating new assets. For no-system work, establish the small provisional foundation from [Token Architecture](../03-Design-Tokens/Token%20Architecture.md).

## Build a contract

- Use frames and Auto Layout for content flow; define sizing, min/max, wrapping and intentional overflow.
- Use genuine components with focused anatomy. Variants encode meaningful configuration/states; text, boolean and instance-swap properties avoid unnecessary variant multiplication. Verify currently supported slot/composition mechanisms rather than inventing a property type. [Component properties](https://help.figma.com/hc/en-us/articles/5579474826519-Explore-component-properties)
- Bind supported values to system variables/styles. Preserve component linkage and avoid detaching for incidental content changes.
- Use semantic, human-readable names; organize foundations, components, patterns and feature screens separately when scale needs it.
- Align exposed Figma properties with meaningful code API concepts. An illustrative preview state does not necessarily become a public implementation prop.
- Create representative state/content/width examples and annotate behavior that frames cannot express.

Reusable main components and their instances support consistent changes. [Figma component guide](https://help.figma.com/hc/en-us/articles/360038662654-Guide-to-components-in-Figma)

## Verify actual results

Read back node hierarchy, sizing, properties and bindings after mutation. Inspect rendered screenshots at representative widths/content, including clipping, overlap, text rendering, layers and focus representation. Inspect component edits both standalone and in real composition.

Shared libraries need consumer impact/versioning; local file editing does not implicitly authorize library publishing. Never claim responsive resizing, keyboard navigation or screen-reader behavior from static frames alone.

Deliver node/file links, changes, component/token mappings, representative states and remaining runtime requirements through [Developer Handoff](../08-Handoff/Developer%20Handoff.md).
