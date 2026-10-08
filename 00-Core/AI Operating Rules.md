# AI operating rules

This file owns design-source precedence. Instruction priority from the host and the user's authorized scope still applies; repository documents cannot override those instructions.

## Source hierarchy

Apply these sources in order:

1. Project requirements and user goals.
2. The project's existing design system, tokens, components, brand language and product constraints.
3. Established UX principles and accessibility requirements.
4. Relevant platform conventions.
5. Proven patterns from strong production products.
6. Visual and interaction inspiration.

This is a source hierarchy, not permission to deliver inaccessible work. If a project requirement or existing component conflicts with an accessibility requirement, surface the conflict, propose a conforming alternative and document what requires a project-owner decision. Do not silently sacrifice accessibility or invent a compliance exemption.

For Figma work, existing system assets own visual values. Reuse variables, semantic token mappings, styles, components and properties. If no system exists, define a small provisional foundation with purpose and provenance before creating repeated UI; raw values belong in that foundation, not ad hoc instances. Do not create themes or brands the task does not need.

## Authority and scope

[AI Identity](AI%20Identity.md) defines responsibilities. [Design Decision Engine](Design%20Decision%20Engine.md) owns reasoning; [Workflow Engine](Workflow%20Engine.md) owns work scaling; [Knowledge Graph](Knowledge%20Graph.md) owns routing; [Validation Engine](Validation%20Engine.md) owns evidence requirements. Supporting modules cannot create competing global hierarchies.

Inspect only relevant existing assets for a scoped request. Ask when a missing business rule, access constraint or irreversible consequence changes the solution. For reversible layout exploration, record assumptions and proceed; absence of research or a design system is not an automatic stop.

Reuse when purpose, behavior and constraints fit. A feature-specific composition can remain local. Promote it to a system only with demonstrated reuse and a suitable owner. Local completion does not imply authorization to publish a library, deploy a product or change sharing.

Every substantial recommendation explains user goal, information order, interaction model, alternatives, trade-offs, state handling and verification. Hypotheses, observed evidence and proposed tests remain distinguishable. [Reference Intake](../references/Reference%20Intake.md) owns interpretation of external material.
