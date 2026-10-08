# Buttons and action controls

Use buttons for actions and links for destinations. Visual appearance does not change semantics. Keep toggle, split-action and ordinary button behaviors distinct even when they share styling.

Choose emphasis within the current decision region. A primary committing action needs a clear outcome label; expert toolbars may have many equal-priority actions. Destructive styling reflects consequence, not every removal.

Content width is intrinsic or fills a task-appropriate container. Preserve labels during loading or provide an equivalent name; prevent duplicate commitment and keep dimensions stable. Explain disabled/unavailable state outside inaccessible hover-only help. Toggle controls expose persistent on/off state.

Keyboard: native buttons activate through Enter/Space; links through their native behavior. Icon-only controls need accessible names and visible/contextual explanations where ambiguous. Focus differs from hover/pressed/selection. Hit area can exceed glyph size without overlapping neighbors.

Specify default, hover when applicable, focus, pressed, disabled, pending and relevant result/error feedback. Do not mandate fixed pixel heights across projects; use existing token sizes and [target requirements](../01-Foundation/Accessibility.md).

Example: "Save draft" can confirm inline; "Send payment" needs truthful commitment/status. Neither needs a decorative success animation by default.

Contract and reuse: [Component Principles](Component%20Principles.md). Risk review: [Checkout & Payments](../06-Patterns/Checkout%20%26%20Payments.md).
