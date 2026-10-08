# Validation engine

A claim of quality needs evidence at the level the artifact permits. Use [Design Critique](../09-QA/Design%20Critique.md) for review and [Design QA](../09-QA/Design%20QA.md) for verification.

## Evidence levels

- Intended: written behavior and state specifications.
- Inspected: static layout, content, bindings or prototype interactions actually examined.
- Observed: a task executed in a prototype or runtime with recorded results.
- Validated with users: an actual study with participants, tasks and findings.

Do not turn one level into another. Figma annotations can specify accessible names and focus; they cannot prove screen-reader compatibility. Label an untested flow as such.

## Completion gates

The requested scope is delivered; critical/high issues affecting that scope are resolved or explicitly remain blocked; consequential assumptions and verification limits are reported. Applicable checks include goal/task fit, information/interaction clarity, accessible behavior, visual hierarchy/polish, system alignment, responsive content and engineering feasibility.

A failed critical check cannot be offset by aesthetic scores. A library release additionally follows [System Governance](../10-Governance/System%20Governance.md); a local exploration does not need invented publication approval.

## Repository validation

Run the repository validator and test suite for changes to instructions, routing or structured data. Use representative [evaluation scenarios](../09-QA/evaluations/README.md) to test decisions, not only wording. Static link/schema checks establish repository integrity; behavioral runs establish whether instructions help design work. Record each separately in [Validation Report](../09-QA/Validation%20Report.md).
