# Developer handoff

Owns the design-to-code contract. Supply enough detail for implementation without inventing backend capabilities.

| Concern | Specify |
| --- | --- |
| Structure | Regions, content order, sizing/overflow and responsive rules between example frames |
| Reuse | Existing component/variable/style IDs and code mappings; justified new contracts |
| API | Meaningful props/defaults, valid combinations, state ownership and local business logic |
| Data | Schema/format assumptions, precision, locale, access, freshness, pagination and loading boundaries |
| Interaction | Trigger/preconditions, focus/keyboard/touch, pending/commit, cancel, error and recovery |
| Content | Labels, helper/error/success/empty copy, long content and translation constraints |
| Accessibility | Semantic roles/names, reading order, focus/announcement intent, contrast/targets and required runtime checks |
| Motion | Purpose, existing tokens, interruption and reduced-motion behavior |
| Validation | Acceptance tasks, actual checks and untested implementation requirements |

Confirm implementation feasibility against known framework, service and code contracts. A Figma variant does not necessarily imply a runtime prop; a mockup of offline/undo/idempotent transfer does not establish service support.

Use acceptance criteria tied to observable outcomes: after a failed submission valid input remains; an uncertain transfer status does not invite blind resend; a selected page differs from all matching records.

Record owner and migration where shared assets change. [System Governance](../10-Governance/System%20Governance.md) owns release policy; [Design QA](../09-QA/Design%20QA.md) owns verification.
