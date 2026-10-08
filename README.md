# Figma design skill

A task-routed design capability for product framing, UX structure, interaction, visual craft, design systems and Figma production. It uses project requirements and the existing product language before external patterns or inspiration.

Start with [SKILL.md](SKILL.md). [AGENTS.md](AGENTS.md) is the concise repository operating contract. Specialist modules add depth without requiring a full-repository read for every change.

## Use

Ask for the outcome, such as ?Design a responsive bid comparison using our existing table and tokens? or ?Critique this transfer flow, including unknown payment status.? Supply relevant project/system context and references where available. The entrypoint routes to the right owners; missing critical business rules are surfaced rather than invented.

This is one skill bundle. To use it as an installed skill, retain SKILL.md and its relative supporting folders together in the host's supported skill location. It is not registered globally by this audit. Figma tools are supplied by the host; obey their skill prerequisites and inspect actual file/library capabilities before writes. The repository itself has no runtime UI or Figma connector.

## Architecture and ownership

| Area | Responsibility |
| --- | --- |
| 00-Core | Source authority, role, decisions, workflow, evidence and routing |
| 01-Foundation | Product/research, IA, interaction, content, accessibility and responsive/platform reasoning |
| 02-Visual-System | Project-grounded color/type/spacing/icons, art direction and motion |
| 03-Design-Tokens | Primitive/semantic/component roles, aliases, modes and migration |
| 04-Figma | Production, existing assets, properties/bindings and prototype fidelity |
| 05-Components | Reusable control contracts and genuine configuration/state needs |
| 06-Patterns | Task flows, recovery, permissions, payments, search, forms and dense data |
| 07-Documentation / 08-Handoff | Reviewable decisions and implementation contracts |
| 09-QA | Critique, QA, audit evidence and contrasting evaluation scenarios |
| 10-Governance | Shared-library evolution, ownership and migration |
| references | One classified registry, metadata inbox and evidence-aware extraction |
| Templates | Small optional brief, decision, component, reference and evaluation contracts |

The [Knowledge Graph](00-Core/Knowledge%20Graph.md) is the detailed task map. No original domain folders were moved or removed. Compatibility paths preserve existing callers.

## References

Paste sources into the task or use [reference intake](references/Reference%20Intake.md):

```powershell
python scripts/reference_intake.py add --source "https://example.com/flow" --question "How does recovery preserve input?" --platform web
python scripts/reference_intake.py list
```

The helper only queues metadata. Inspect sources before extracting principles and proposing UI; translate useful logic through local tokens/components. Standards, production patterns and visual inspiration have distinct authority. Source records include dates and access limits.

## Verification

Python 3.10 or newer is sufficient for repository tooling; no third-party package is needed.

```powershell
python scripts/validate_repository.py
python -m unittest discover -s tests -v
git diff --check
```

The validator checks local file links, declared dependencies, reference records, skill-to-scenario route reachability and preservation of the three pre-existing user edits. The captured raw hashes remain recorded; LF-normalized hashes also accept Git's CRLF/LF checkout conversion while detecting content changes. It does not test URL availability, fragment anchors, aesthetics, Figma rendering or runtime accessibility.

[Evaluation scenarios](09-QA/evaluations/README.md) cover sixteen distinct tasks. [Worked examples](09-QA/evaluations/examples/README.md) and author walkthroughs show reasoning and critique; independent artifact-based generation remains a separate check.

## Audit evidence

See [Architecture Audit](09-QA/Architecture%20Audit.md), [File Audit](09-QA/File%20Audit.md) and [Validation Report](09-QA/Validation%20Report.md) for the complete before/after assessment, changed/created lists, measured checks and remaining limits. MIT [license](LICENSE); original copyright retained.
