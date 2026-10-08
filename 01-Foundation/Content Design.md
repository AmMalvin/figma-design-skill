# Content design

Owns language, microcopy, content models and internationalization.

Write around the user's decision: what happened, meaning, available action. Keep one vocabulary for each concept. Match domain expertise without exposing implementation details that do not help users.

- Labels describe outcomes; "Send transfer" differs from "Continue" at final commitment.
- Keep input labels visible and requirements available before failure.
- Errors state the problem and safe recovery without blame or an invented reason.
- Empty copy distinguishes first use, no matches, missing access and unavailable data.
- Success reflects commitment: "Request received" differs from "Payment completed."
- Confirmation names object, affected scope, consequence and reversibility. Avoid ceremonies for low-risk recoverable actions.
- Place help near the decision; essential information must not depend on a tooltip.

For uncertain money transfer: "We could not confirm the transfer. Check its status before sending again" is safer than a generic retry prompt.

Test minimum/typical/long content, unbroken identifiers, wrapping labels, zero/plural forms and real locale expansion. Key identity, money, date and legal consequences remain retrievable when truncated. Do not squeeze type to fit.

Use locale-aware currency/numbers/time zones and unambiguous dates. Verify RTL logical order/alignment, script coverage and translated content; do not mirror logos or directional data blindly. [Typography](../02-Visual-System/Typography.md) owns glyph/readability choices.

Deliver state copy and content constraints. [Accessibility](Accessibility.md) owns programmatic labels and announcements.
