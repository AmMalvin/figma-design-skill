# Interaction design

Owns action/state/feedback. Define intent -> trigger -> precondition -> system work -> response -> next state, including cancellation and recovery.

- Acknowledge input promptly with truthful pending feedback; latency heuristics are not guarantees.
- Optimistic UI suits low-risk recoverable changes with rollback. Money, authorization and irreversible actions need confirmed or explicit pending status.
- Prefer undo for recoverable removal; specific confirmation/review earns its cost for high-consequence action. Repeated generic dialogs teach dismissal.
- Distinguish unavailable, read-only, denied and loading; explain reasons where needed.
- Preserve work during interruption subject to security policy; do not promise unsupported offline persistence.

Keyboard behavior follows semantics: Tab between ordinary controls; arrows in appropriate composites. Define Escape without silent loss. Orient focus at new steps; dynamic updates ordinarily retain focus. Modal containment differs from non-modal panels.

Essential actions need alternatives to hover, gesture and drag. Haptics/sound supplement visible feedback. [Accessibility](Accessibility.md) owns normative requirements; [Motion](../02-Visual-System/Motion.md) owns transitions.

[State Patterns](../06-Patterns/State%20Patterns.md) owns loading, empty, partial, failure, stale, offline and denied states. Verify double activation, back/cancel, content extremes, narrow layouts, keyboard/touch, success and failure. Separate prototype evidence from runtime guarantees.
