# Workflow engine

Scale work to the requested deliverable and consequence. The shared loop is understand -> inspect -> decide -> make -> critique -> verify -> deliver; it is not a mandatory set of separate artifacts.

| Work | Minimum useful process |
| --- | --- |
| Small copy, spacing or known-state correction | Inspect affected context and callers; make the change; verify the relevant behavior or rendering |
| New screen or complete feature flow | Frame the outcome; map decisions and states; inspect system and supplied references; choose structure; design; critique; verify representative content/input widths; hand off behavior |
| Reusable component or token change | Inspect instances and code contracts; define API/aliases/states; exercise modes and composition; document compatibility and migration |
| Research or critique request | Inspect evidence; synthesize findings with severity and confidence; recommend the next useful action without claiming implementation |
| Publishing a shared library | Prepare the concrete reviewed change and consumer impact; follow the project's existing release authority |

For new product work, use [Design Brief](../Templates/Design%20Brief.md). For uncertain interactions, use [Prototype Strategy](../04-Figma/Prototype%20Strategy.md). For references, inspect through [Reference Intake](../references/Reference%20Intake.md) before proposing UI.

Revise only the parts invalidated by new evidence. A viewport change does not require restarting product discovery. Record trade-offs and relevant checks during work; do not manufacture stakeholder approvals or require human review for every reversible local change.

Delivery includes the requested artifact, important reasoning, evidence of checks and any consequential limits. [Validation Engine](Validation%20Engine.md) defines the difference between intended and observed behavior.
