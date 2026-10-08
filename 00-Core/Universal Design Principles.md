# Shared design principles

These principles explain quality decisions. [AI Operating Rules](AI%20Operating%20Rules.md) owns precedence; these do not establish a second hierarchy.

| Principle | Decision rule | Where it fails or needs another approach |
| --- | --- | --- |
| Outcomes before screens | Define a user task and observable success; remove steps that do not aid that task | Fewer clicks are not better if they conceal risk or remove needed review |
| Context before defaults | Account for attention, expertise, network, input method and environment | One layout cannot serve a reading product and an operations workstation equally |
| Recognition and control | Keep critical choices visible; support exit, correction and appropriate undo | Exposing every expert option at once overwhelms novices; disclose advanced work deliberately |
| Clear information relationships | Use proximity, type, alignment and contrast to communicate grouping and order | Enclosing every group in a card produces competing surfaces and poor comparison |
| Consistent contracts | Reuse controls and vocabulary for the same meaning | Consistency of behavior does not require identical composition or density everywhere |
| Expressive visual language | Use composition, typography, imagery and motion to establish relevant character | Novel controls that undermine task completion or system coherence need evidence before adoption |
| Accessibility through the flow | Apply [Accessibility](../01-Foundation/Accessibility.md) to task paths, states and all input methods | A contrast pass alone cannot establish accessible behavior |
| State and feedback | Distinguish pending, success, empty, failure, denied, offline and stale information | A skeleton cannot explain a failed request; a toast cannot hold a critical unresolved error |
| Recovery and integrity | Preserve valid work, describe what committed and provide a safe next action | Blind retry after an uncertain financial commit can duplicate a transaction |
| Reuse at the right layer | Separate system primitives, product patterns and local business compositions | Promoting every screen into the core library increases coupling and maintenance |
| Feasible production | Align component APIs, data needs and adaptive behavior with engineering | A Figma prototype does not prove runtime performance or backend correctness |
| Evidence and honest confidence | Distinguish observed findings, inferred principles and untested assumptions | An award or competitor screen is not proof of usability for this product |

Specialists own quantitative standards and domain decisions; link to them instead of repeating checklists.
