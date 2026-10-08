# Motion

Owns transition purpose, timing, interruption and reduced-motion behavior.

Use motion to explain causality, spatial continuity, state or direct manipulation. Identify trigger, changed property, start/end state, duration/easing source, interruption/reversal and reduced-motion alternative. Existing motion tokens/conventions govern; do not invent one timing for every distance and task.

A menu entrance can connect trigger and surface; a long decorative entrance delays action. A progress animation must not imply measured completion when none exists. Avoid using animation to hide latency, inaccessible state or hierarchy problems.

Respect reduced motion by removing or simplifying nonessential spatial movement while preserving immediate state feedback. Avoid autoplay distraction, flashing and continuous decorative movement. Essential task information must remain understandable in the alternative.

Define focus/hit testing during transitions, rapid repeat actions, reversed state changes, cancellation, background updates and performance constraints. Favor properties the implementation can animate smoothly; a prototype is not proof of frame rate.

Inspect transition in context, not only isolated keyframes. Verify that it never blocks urgent controls or steals focus. [Interaction Design](../01-Foundation/Interaction%20Design.md), [Accessibility](../01-Foundation/Accessibility.md), [Prototype Strategy](../04-Figma/Prototype%20Strategy.md)
