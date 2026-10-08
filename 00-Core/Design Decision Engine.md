# Design decision engine

Use for substantial recommendations. Small known corrections need only the affected rationale and check.

## Before visual styling

Answer the questions that affect this task:

- Who uses the interface, in what context, and what outcome are they trying to achieve?
- What information matters first, what decision follows, what deserves emphasis and what remains secondary?
- Which interaction model matches frequency, expertise, risk, data and input method?
- What errors are likely? What happens while waiting, with no data, large datasets, long text or missing permission?
- How does the flow behave on narrow screens, with keyboard and with touch?
- What happens after failure, after success and after interruption?
- Which parts belong in the core system, a reusable product pattern or only this feature?

Write unknowns as assumptions with their consequence. Research the assumption most likely to invalidate the solution. Do not invent users, policies, backend guarantees or reference findings.

## Choose a model, then a composition

Compare meaningful alternatives when the interaction or structure is uncertain. Two genuinely different models are more useful than three cosmetic versions. Explain why the selected model suits the task and when a rejected alternative would be better.

Resolve conflicts with [source precedence](AI%20Operating%20Rules.md). Hard requirements cannot be averaged away by a score. Consider effort and feasibility alongside task completion, accessibility, product fit and visual quality.

Record consequential decisions with [Design Decision](../Templates/Design%20Decision.md): evidence, options, choice, drawback, failure condition and validation. A claim such as ?clean? or ?modern? needs replacement with an observable outcome, such as faster comparison, clearer grouping or visible recovery.

## Example

A payments review screen needs recipient identity, amount, fees and finality before the committing action. A compact review summary preserves context; an extra confirmation dialog only earns its cost when it reveals a new consequence or materially prevents a high-cost error. Optimistic success fails when transfer status is unknown.

A creative workspace can expose several simultaneous tools because experts compare and manipulate content continuously. A single oversized CTA or universal card dashboard would weaken the task. Test tool discovery, editing continuity and reversible operations instead.
