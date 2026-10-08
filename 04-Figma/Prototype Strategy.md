# Prototype strategy

Owns fidelity and test coverage. Prototype the uncertainty, not every possible screen.

| Question | Useful fidelity |
| --- | --- |
| Structure/sequence/findability | Low-fidelity flow with meaningful labels and decisions |
| Validation, disclosure, navigation or recovery | Interactive states with realistic data and back/cancel |
| Type, composition and visual character | High-fidelity frames with actual content and system bindings |
| Latency, keyboard, assistive technology or complex data | Runtime prototype when Figma cannot faithfully demonstrate it |

Define the hypothesis, task, start state, success, critical error and observations. Include decision points, denied/empty/loading/failure, interruption and return where they can invalidate the model.

Use variables/conditionals/interactive components only where current capabilities and test needs justify them. Do not let an unavailable prototype feature prevent a clear behavior specification.

A clickable path is not evidence of discoverability if it was coached. Record prototype limitations and unimplemented branches. [Design Research](../01-Foundation/Design%20Research.md) owns study methods; [Design QA](../09-QA/Design%20QA.md) owns verification.
