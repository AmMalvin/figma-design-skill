# Token architecture

Owns reusable values, aliasing, modes and code alignment. Project tokens are the source of truth; names below illustrate concepts, not required replacements.

| Layer | Role | Example |
| --- | --- | --- |
| Primitive | Raw reusable value | palette/neutral/900 |
| Semantic | Purpose/context | color/text/default -> palette/neutral/900 |
| Component | Necessary local contract | button/primary/background -> color/action/primary |
| Usage | Bound role at the instance | Button fill references the existing semantic/component token |

Equal values do not imply equal purpose. Different semantic roles may alias the same primitive today and diverge later. Avoid cycles, unresolved aliases, duplicated meanings and tokenizing every one-off dimension.

## Figma and code

Map token name, type, collection, mode, alias/value, applicable property and code name. Preserve IDs/consumer bindings when updating. Separate primitive palette from semantic roles where it improves ownership. Modes describe supported contexts such as theme; do not create combinations of brand/theme/density/locales without actual demand.

Figma variables represent typed reusable values; styles can represent composite property sets. Bind supported properties to variables and use shared text/effect styles or documented token mappings for composites or tool limits. Do not claim every shadow, gradient or motion contract is one directly bindable variable. [Figma variable guide](https://help.figma.com/hc/en-us/articles/15339657135383-Guide-to-variables-in-Figma)

Review token purpose with [Atlassian's token documentation](https://atlassian.design/foundations/tokens/); adapt the concept, not its palette or names. Use code token formats already adopted by the project. This repository contains no universal product token set.

## Change and verify

Inspect alias graph and consumer impact; change at the owner; validate every supported mode for contrast, legibility and role meaning; inspect bound instances and exported code mappings. Record exceptions and migration for renamed/deprecated roles.

A new provisional foundation includes values, purpose, provenance, scope and evidence. It remains local until reuse and governance justify promotion. [Component Principles](../05-Components/Component%20Principles.md), [System Governance](../10-Governance/System%20Governance.md)
