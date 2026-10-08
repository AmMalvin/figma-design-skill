# Design QA

Owns verification of the intended contract. [Design Critique](Design%20Critique.md) owns diagnosis/ratings.

Build checks from the task and risk. Include realistic primary/alternate paths, loading/empty/failure, denied access, long content, large data, double activation, interruption and recovery where relevant.

Static/Figma checks inspect rendering, hierarchy, overflow, binding, property, composition and supported modes/widths. Prototype checks execute linked behavior and focus only where faithfully modeled. Runtime checks exercise keyboard/touch, actual screen-reader semantics, browser/platform history, asynchronous races, backend commit and data scale.

Record environment, artifact/version, task/input, expected outcome, observed outcome, evidence location and issue severity. Unrun checks remain unrun. Simulated backend status or a designed focus ring does not prove production correctness.

Accessibility verification uses [Accessibility](../01-Foundation/Accessibility.md). Token/component checks use [Token Architecture](../03-Design-Tokens/Token%20Architecture.md) and [Component Principles](../05-Components/Component%20Principles.md). Check component composition, not only isolated specimens.

For repository changes run `python scripts/validate_repository.py` and `python -m unittest discover -s tests -v`. These verify links, schemas, routing and preservation, not the aesthetic quality of generated screens.

[Scenarios](evaluations/README.md) define representative behavioral tests. Record structural, author walkthrough and independent/observed evaluation separately. Do not report scenario availability as a completed behavioral test.
