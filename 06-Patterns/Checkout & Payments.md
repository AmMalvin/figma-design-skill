# Checkout and payments

Owns transaction review, commitment and trustworthy recovery. Financial policy, tax, eligibility, fees and security are supplied constraints; do not invent them.

Keep item/recipient identity, amount/currency, fees/tax/total, timing and finality visible at the decision. Users can correct relevant details without losing valid work. Checkout stages follow real dependency, not a mandatory wizard.

Make final-action wording reflect actual commitment. An additional confirmation earns use only through a new consequence or high-cost error prevention. Required authorization follows policy.

Separate request received, authorization pending, processing, confirmed, declined, partial and unknown outcome. Do not show optimistic payment success. Duplicate prevention/idempotency/status reconciliation require a real service contract; UI disabling alone is insufficient.

On unknown status, preserve transaction identity and direct users to authoritative status before retry. Failed payment keeps permitted input and explains a safe alternative. Receipt/reference and history are durable enough for follow-up.

Handle changed price/availability, unsupported method, expiry, declined authentication, interruption, network loss after commit and refund/cancellation rules. Never promise reversal beyond policy.

Test long identities, large/negative/locale-formatted amounts where supported, narrow/software-keyboard layouts, keyboard/assistive review and all consequential states. [Form Workflows](Form%20Workflows.md), [State Patterns](State%20Patterns.md), [Content Design](../01-Foundation/Content%20Design.md)
