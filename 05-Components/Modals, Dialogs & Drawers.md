# Dialogs, drawers and overlays

Choose a surface from the task: inline/page work for long or navigable tasks; non-modal detail when context comparison must continue; modal dialog for a bounded interruption needing resolution. A drawer's position does not determine modality.

Specify trigger, heading, initial focus, background availability, scroll, exit, dirty work, pending operation and restoration. For modal content contain focus and make background inert; for non-modal content preserve logical navigation. If a trigger disappears, restore to a meaningful continuation. [Modal dialog pattern](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/)

Use Escape as a predictable dismissal where applicable; outside-click dismissal must not silently lose consequential work. Provide a visible exit. Avoid nested modal layers; a necessary child interaction needs clear top-layer behavior and restoration.

Do not make Enter universally commit a destructive action or a multiline form. Confirmation exposes new consequence, affected scope and reversibility; low-risk undo often performs better.

Popover/tooltip/dialog are distinct semantics and APIs. Tooltips contain supplemental information, not essential instructions or complex actions.

Verify viewport edges, narrow/short windows, software keyboard, content overflow, focused errors, loading/failure, cancellation and stacked interaction only if supported. [Component Principles](Component%20Principles.md), [Accessibility](../01-Foundation/Accessibility.md)
