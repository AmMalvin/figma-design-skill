# Design critique rubric

Owns evidence-based review. Inspect the actual screens, flow/prototype or code when available before critique. With only a specification, report a specification review.

## Findings and ratings

Each finding records task/state, observed evidence, consequence, severity, fix, trade-off and verification. Confidence is separate from severity. Critical means unsafe commitment/data loss or inability to perform the essential task; high means a serious task/access barrier; medium means meaningful friction; low means limited polish.

Rate each applicable dimension: 0 absent/failed, 1 weak, 2 viable with material issues, 3 strong with appropriate evidence, 4 exceptional with demonstrated context-specific refinement. Use U for uninspected/untested and N/A with a reason. Do not treat U as passed or compute an average that hides blockers.

| Dimension | Evidence to inspect |
| --- | --- |
| User-goal alignment | Proposed outcome and actual user/task/context |
| Task completion | Complete path and critical decision/commit |
| Information architecture | Predictable organization, scope, labels and wayfinding |
| Interaction clarity | Discoverable actions and accurate expectation |
| Visual hierarchy | Information/decision priority and meaningful emphasis |
| Typography | Readable roles, rendering, scale and content fit |
| Spacing | Grouping, rhythm, comparison distance and targets |
| Composition | Task-appropriate regions and balance |
| Density | Necessary context visible for expertise/input |
| Color | Semantic emphasis, status and supported mode meaning |
| Accessibility | Applicable standards and complete input/assistive paths |
| Feedback | Truthful timely pending/result status |
| Error prevention | Protection proportional to consequence |
| Recovery | Valid work preserved and safe correction/retry |
| Responsive behavior | Intermediate widths, overflow, scaling and task continuity |
| Platform appropriateness | Familiar lifecycle/input/navigation and justified deviations |
| Design-system consistency | Existing roles/styles/bindings, documented exceptions |
| Component reuse | Correct contracts and justified layer of new reuse |
| Content quality | Decision-oriented labels, copy and locale/long-content behavior |
| Motion | Purpose, interruption, preferences and no delayed task |
| Performance perception | Context preserved and truthful progress, no invented latency claims |
| Edge cases | Empty/large/long/denied/offline/partial/interrupted states |
| Implementation feasibility | Data/API/tool capabilities and cost/dependencies |
| Originality | Relevant product insight and distinct composition without unnecessary relearning |
| Polish | Optical alignment, rendering, rhythm, transitions and finish under real content |

## Decision

Approve the inspected scope only when critical/high blockers are resolved and material unknowns are explicit. Attractive color/composition cannot compensate for unsafe retry, inaccessible actions or unusable flows. A restrained design with clear hierarchy and task fit outranks decoration with weak UX.

Prioritize fixes by consequence and leverage. Explain when an alternative pattern is better; do not prescribe a new design merely because it matches personal taste.

[Design QA](Design%20QA.md) owns verification. [Evaluation scenarios](evaluations/README.md) test whether the skill avoids a repeated formula across contexts.
