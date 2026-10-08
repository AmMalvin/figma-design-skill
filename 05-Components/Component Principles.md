# Component architecture

Owns shared anatomy, API and reuse contracts. [Glossary](../00-Core/Glossary.md) distinguishes foundations, tokens, components, composites, patterns, templates, product-specific components, screens and flows.

## Reuse and boundaries

A component represents a genuine repeated interaction need. Reuse an existing contract when purpose/behavior fit; compose when needs differ. Business-specific workflows remain product-owned until a strong reuse case justifies promotion. Do not prohibit useful local components.

Share tokens/language without forcing buttons, switches, links, charts, editors or dialogs into one variant family. Shared anatomy and behavior determine family boundaries. A composite delegates child interaction rather than duplicating it.

## Document the contract

Define purpose/non-use cases, anatomy/slots, data/content, properties/defaults, valid configurations, states, sizing/density, responsive rules, keyboard/focus/semantics, feedback/recovery, content limits and code mapping. [Component Contract](../Templates/Component%20Contract.md)

Use variants for genuine configuration/state differences, text properties for content, booleans for optional visibility and instance swaps for approved replacements. Model independent axes only when valid combinations exist. List invalid combinations; avoid the full Cartesian product or massive Type variants spanning unrelated controls.

Map Figma properties to meaningful code APIs. Preview-only hover/focus states may remain design examples instead of public state props. Current tool support governs composition mechanisms.

## Verification

Exercise actual reuse in at least contrasting contexts when claiming cross-context reuse. Inspect long content, empty/missing data, supported modes/widths and meaningful states/input methods. Do not add irrelevant states to static decoration.

[Accessibility](../01-Foundation/Accessibility.md), [Token Architecture](../03-Design-Tokens/Token%20Architecture.md), [Figma Production](../04-Figma/Figma%20Production.md), [System Governance](../10-Governance/System%20Governance.md) own their standards; specialist modules add behavior rather than repeat them.
