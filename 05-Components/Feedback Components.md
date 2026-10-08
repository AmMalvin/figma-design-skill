# Feedback components

Select feedback by consequence and persistence:
- Inline feedback for a local result or correction.
- Banner for ongoing page/system impact.
- Toast for low-risk transient acknowledgement.
- Persistent status/history for consequential or unresolved operations.
- Blocking alert only when users must act before proceeding.

These are separate behavior contracts; shared colors do not make them one universal variant set.

Status says received/pending/committed/failed/uncertain honestly. Critical errors and sole recovery actions cannot disappear in a toast. Temporary feedback needs readable timing, pause behavior when appropriate, dismissal and accessible announcement without stealing focus.

Loading feedback preserves context. Use measured progress only with meaningful measurement; skeletons only when structure is predictable. Empty, denied, offline and failed are distinct, not interchangeable "no data."

Polite announcements suit routine updates; assertive announcements require real urgency. Avoid announcing every keystroke/progress tick. Durable inline feedback can remove the need for a toast.

Specify ordering/deduplication, timeout, action, dismissal, focus and persistence. Verify overlapping messages, repeated requests, screen reader/keyboard intent, narrow layout and reduced motion. [State Patterns](../06-Patterns/State%20Patterns.md), [Accessibility](../01-Foundation/Accessibility.md)
