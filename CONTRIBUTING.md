# Contributing

Make the capability easier to retrieve, reason with and verify. One module owns each cross-cutting rule. Read [AGENTS.md](AGENTS.md), [SKILL.md](SKILL.md) and relevant scoped contracts; a small change does not require rereading every module.

## Change instructions

State purpose, boundary, trigger, rationale, trade-off, failure condition and observable check. Use [Module Blueprint](Templates/Module%20Blueprint.md) where useful. Replace vague quality adjectives with decisions. Do not prescribe a universal style, fixed number of alternatives, identical layout or mandatory lifecycle for every task.

Use the existing numbered domain for new knowledge. Separate a topic only when scope, retrieval or ownership improves. Update [Knowledge Graph](00-Core/Knowledge%20Graph.md) and entrypoint routes when adding a specialist. Check callers before merging; retain compatibility routes when external or protected files may depend on old paths.

Accessibility, token engineering, Figma production, motion, handoff and governance have shared owners. Specialists define their behavior, not duplicated global checklists. Distinguish system components from feature compositions. Meaningful variants do not imply every prop combination needs a frame.

## Sources and evidence

Use the shared [registry and intake](references/README.md), with authority class, exact inspected scope, date, conflicts and adaptation. Uninspected sources cannot contain extracted principles or an invented review date. Source claims and author inference remain distinct. Do not copy a competitor's brand or values.

For a behavior change, choose an applicable scenario and record a reviewable result. Keep generator/evaluator identity and independence explicit. Static documentation checks do not prove product quality. Do not invent users, metrics, research, backend guarantees or tool actions.

## Checks and preservation

Run `python scripts/validate_repository.py`, `python -m unittest discover -s tests -v` and `git diff --check`. Add tooling regressions only for consequential behavior, such as corrupting references, broken retrieval or losing user work. Evaluate design guidance against relevant task artifacts rather than word-matching tests.

The audit baseline records three pre-existing edited files; preserve them unless a later user request explicitly authorizes their change. The hash guard intentionally flags updates; a future authorized change should record provenance and adjust that preservation policy openly, not silently bypass it. Do not edit historical audit evidence to inflate outcomes.

Document consequential changes in CHANGELOG.md. Publishing libraries, changing sharing or deploying artifacts requires the user's applicable scope; local authoring does not imply that authority.
