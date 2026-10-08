# System governance

Owns shared-library evolution, ownership and compatibility. Apply only when changes affect reusable contracts or publishing; local exploration does not need a governance ceremony.

Distinguish foundation, primitive/semantic/component tokens, core components, composites, patterns, templates and product-specific assets. Keep business policy out of core until repeated use and ownership justify it.

A proposal states problem, existing alternatives, reuse evidence, contract, affected consumers, accessibility/engineering risks and migration. Ownership is a responsible role/person from the actual project, not a fabricated approval.

Review proportional to impact: rename, removal or behavioral API changes need consumer checks and migration; compatible content fixes need less process. Follow existing project release/versioning policy rather than automatically assigning a major version to every visual change.

Maintain one authoritative definition. Equal appearance/value alone does not justify merging semantic roles or components with different behavior. Deprecation records replacement, consumer impact and supported transition; remove only after dependency inspection and authorized scope.

Library publishing follows actual project authority/tool access. A prepared local artifact can be complete while publishing is outside the task. Do not label draft assets approved or invent stakeholder sign-off.

Monitor recurring defects, adoption, inaccessible contracts, orphaned assets and migration debt when maintenance is requested. [Component Principles](../05-Components/Component%20Principles.md), [Token Architecture](../03-Design-Tokens/Token%20Architecture.md)
