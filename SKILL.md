---
name: figma-design-skill
description: Design and critique product flows, interfaces, components and design systems, including Figma production and developer handoff. Use for product, UX, interaction, visual and system design decisions; load only task-relevant supporting modules.
---

# Figma design skill

Turn a user goal into a coherent, usable and refined experience. The repository provides design judgment and production standards; it does not supply a universal product theme or guarantee access to Figma tools.

## Start at the requested outcome

Identify the user, task, context, next decision, existing product language and requested deliverable. Read [AI Operating Rules](00-Core/AI%20Operating%20Rules.md) for source precedence and [Design Decision Engine](00-Core/Design%20Decision%20Engine.md) for substantial design decisions.

Use the project's existing system as the visual source of truth. Inspect supplied references before proposing UI through [reference intake](references/Reference%20Intake.md). If an asset cannot be accessed, record the limit and continue work that does not depend on it.

Read applicable scoped guidance when using [visual modules](02-Visual-System/AGENTS.md), [patterns](06-Patterns/AGENTS.md), [Figma production](04-Figma/AGENTS.md) or [evaluation](09-QA/AGENTS.md). Nested contracts may not be automatically loaded when the session starts at the repository root or uses this bundle as an installed skill.

Choose the relevant route; do not read every module:

| Request | Read |
| --- | --- |
| Product framing, research or competitive analysis | [Product Thinking](01-Foundation/Product%20Thinking.md), [Design Research](01-Foundation/Design%20Research.md) |
| Flow, navigation or content-heavy product | [Information Architecture](01-Foundation/Information%20Architecture.md), [User Journey Mapping](01-Foundation/User%20Journey%20Mapping.md), [Content Design](01-Foundation/Content%20Design.md) |
| Interaction, state, form or recovery | [Interaction Design](01-Foundation/Interaction%20Design.md), [Pattern Principles](06-Patterns/Pattern%20Principles.md), relevant [pattern route](00-Core/Knowledge%20Graph.md) |
| Visual composition or art direction | [Visual Hierarchy](01-Foundation/Visual%20Hierarchy.md), [Art Direction](02-Visual-System/Art%20Direction.md), relevant typography/color/spacing module |
| Mobile, web, desktop or responsive work | [Responsive Design](01-Foundation/Responsive%20Design.md), [Platform Conventions](01-Foundation/Platform%20Conventions.md), [Layout System](01-Foundation/Layout%20System.md) |
| Dashboard, analytics or dense data | [Data-Dense Interfaces](06-Patterns/Data-Dense%20Interfaces.md), [Tables](05-Components/Tables%20%26%20Data%20Grids.md), [Data Visualization](05-Components/Data%20Visualization%20Components.md) |
| Component, token or shared library | [Component Principles](05-Components/Component%20Principles.md), [Token Architecture](03-Design-Tokens/Token%20Architecture.md), [System Governance](10-Governance/System%20Governance.md) |
| Create or update Figma artifacts | [Figma Production](04-Figma/Figma%20Production.md), [Prototype Strategy](04-Figma/Prototype%20Strategy.md); obey available tool-specific skills |
| Critique, QA or evaluation | [Design Critique](09-QA/Design%20Critique.md), [Design QA](09-QA/Design%20QA.md), relevant [evaluation scenario](09-QA/evaluations/README.md) |
| Handoff or specifications | [Design Documentation](07-Documentation/Design%20Documentation.md), [Developer Handoff](08-Handoff/Developer%20Handoff.md) |

Read [Accessibility](01-Foundation/Accessibility.md) when changing interactive behavior, contrast, navigation, data presentation or responsive layout. For motion decisions, read [Motion](02-Visual-System/Motion.md).

## Produce the appropriate evidence

For a small correction, state the change, rationale and relevant check. For a substantial design, provide task/information priorities, an interaction model, meaningful alternate and failure paths, system reuse, responsive behavior and a concise critique. Use [Design Brief](Templates/Design%20Brief.md) and [Design Decision](Templates/Design%20Decision.md) only where they help review.

Choose visual structure from the task: ledger comparison, messaging continuity, editorial reading and creative workspaces require different composition and density. Tokens create coherence, not identical layouts. Distinguish reusable system primitives from feature-specific business compositions.

Use [Workflow Engine](00-Core/Workflow%20Engine.md) to scale work and [Validation Engine](00-Core/Validation%20Engine.md) to report confidence. A static mockup can demonstrate intended focus, copy, states and hierarchy; screen-reader behavior and backend correctness need runtime evidence.
