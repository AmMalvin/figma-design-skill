# Spacing and sizing

Owns spatial relationships, shape and task density.

Use the existing scale. Numeric steps are primitive values; names such as inset/control or gap/section can be semantic roles. Do not rename numerical tokens as semantic without a purpose. New scales require product rationale, not a mandatory 8-point preference.

Space communicates grouping: within a control, between related controls, between sections and around regions. Choose rhythm from content/task relationships; do not make every object use equal padding or radius.

Size controls for labels, states and hit areas. Use minimum usable dimensions and flexible content width/height; fixed heights must not clip scaling or long labels. [Accessibility](../01-Foundation/Accessibility.md) owns target requirements and exceptions.

Density supports information throughput. Compact expert comparison and spacious reading can share tokens while differing structurally. A density mode earns maintenance cost only if actual contexts need it. Avoid shrinking touch hit areas to make a compact table.

Radius, border and elevation express boundaries, grouping and layering. Do not impose uniform 12/16px radius on unrelated elements, make every control a pill or add shadows to all containers.

Verify comparison distance, row scanning, touch comfort, grouping and extreme content across [responsive layouts](../01-Foundation/Responsive%20Design.md). Auto Layout mechanics belong in [Layout System](../01-Foundation/Layout%20System.md).
