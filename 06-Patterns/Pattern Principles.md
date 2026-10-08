# Pattern contracts

Owns reusable workflow structure. Components describe element behavior; patterns coordinate user decisions and system responses.

Define user/task/context, entry/preconditions, information priority, decisions, components, transitions, success/commitment, exit, alternate paths and recovery. Include loading/empty/error/permission/interruption only where meaningful; do not add irrelevant states to fill a checklist.

Choose single page, steps, inline edit, panel or full page from dependency/risk/context. Multi-step flows help distinct prerequisite groups but impede comparison and cross-field review. Preserve back/edit and a truthful progress model.

Reuse component behavior; keep domain policy local. A common workflow can become a product pattern without entering the core library.

Map uncertainty and backend boundaries: pending differs from committed, failed differs from unknown. Critical operations need safe status/retry semantics. [State Patterns](State%20Patterns.md)

Keep task logic coherent across platforms while adapting presentation, input and navigation. Do not require identical interaction surfaces everywhere. [Responsive Design](../01-Foundation/Responsive%20Design.md)

Deliver a flow/state contract, system reuse, relevant copy and verification. Use [Design Critique](../09-QA/Design%20Critique.md) for assessment and [Developer Handoff](../08-Handoff/Developer%20Handoff.md) for implementation dependencies.
