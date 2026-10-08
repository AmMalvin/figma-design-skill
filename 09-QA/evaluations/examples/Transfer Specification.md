# Transfer specification

Fixture: consumer mobile-transfer scenario. Existing native controls, ledger typography and semantic roles are supplied conceptually; concrete Figma IDs and values are not supplied. This is intended design evidence.

## Task and structure

A returning customer sends money to a saved beneficiary. Recipient identity, source account and total debit matter before commitment. Use a sequence: recipient, amount/account, review, submission, status and receipt. The review is a compact label/value composition, not a tile dashboard. Retain edit links to the relevant prior section.

A single-page transfer could be faster for highly familiar low-risk repeat actions. Here the explicit review creates a useful commitment boundary because fees and uncertain payment status matter. Do not turn every field into a separate wizard step.

## State contract

| State/event | Visible response | Next action and data rule |
| --- | --- | --- |
| Recipient selected | Verified identifying details permitted by policy | Choose amount/account; long names remain readable |
| Invalid amount | Specific reason near field, linked summary if appropriate | Correct value; preserve recipient and account |
| Review | Recipient, amount, fee, currency, account and total debit | Edit or submit; price/fee changes require updated review |
| Submitting | Pending request; no duplicate local action | Maintain request identity; do not claim funds moved |
| Timeout | Status unknown, reference and checking explanation | Reconcile with service/history before any retry |
| Confirmed failure | Actionable reason without sensitive leakage | Correct/retry only as permitted by service |
| Confirmed success | Actual result and receipt | View history or begin a separate transfer |
| Back/interruption | Explain whether request has committed | Preserve uncommitted input according to security policy |

## System and interaction

Use existing native inputs, buttons, review text and receipt pattern. Semantic pending, error and success roles reflect actual state; do not choose colors by fintech stereotype. Large text may reflow review rows vertically. Keep the action reachable with the keyboard visible without obscuring errors. Touch and keyboard behavior follow the verified platform; equivalent web behavior needs labels, logical order and visible focus.

Intended failure focus goes to the first invalid field or review summary appropriate to the chosen platform. Status updates need a non-disruptive accessible announcement in runtime. No animation is required to establish success. Reduced-motion alternatives preserve all information.

## Handoff and critique

Service contract: stable transfer identity, status lookup, authoritative fee/currency and retry policy. A disabled button alone cannot guarantee idempotency. Open questions: actual authentication/limits, draft retention and target native OS conventions.

Critical unknown-status handling is specified. Remaining checks: real component bindings, text/contrast rendering, target geometry, focus/announcements, offline service behavior and duplicate-request protection. Ready for a prototype/specification review; no release approval follows from this document.
