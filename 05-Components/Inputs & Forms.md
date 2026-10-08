# Input components

Owns field/control behavior; [Form Workflows](../06-Patterns/Form%20Workflows.md) owns task orchestration.

Choose data semantics before control appearance: text for identifiers/phones (including leading zeroes), numeric controls for actual arithmetic values, radio for mutually exclusive visible choices, checkbox for independent choices, and switch for an immediate setting. Calendar pickers do not replace efficient typed dates in every context.

Keep visible labels, relevant helper/requirements, required/optional convention and associated errors. Placeholder supplies an example, never the only label. Prefix/unit is distinct from entered value; expose it meaningfully.

Different controls share field anatomy/tokens without becoming variants of a text box. Combobox, date picker, file upload and rich text have distinct APIs/keyboard behavior. Use native controls where suitable; consult the relevant [APG patterns](https://www.w3.org/WAI/ARIA/apg/patterns/).

Define validation timing: do not show premature errors while typing a recoverable partial value; check on completion/blur or submit as appropriate. Async checks handle stale responses and pending state. Submission links summary errors to fields and preserves valid input.

Support autofill, password managers, paste, locale formats and software keyboards. Input masks must not trap editing. Distinguish read-only/selectable from disabled, focus from filled and loading from unavailable.

Verify long values, labels, multiple errors, keyboard/scaling, narrow layout and actual code semantics. [Accessibility](../01-Foundation/Accessibility.md), [Component Principles](Component%20Principles.md)
