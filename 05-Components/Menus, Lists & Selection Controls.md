# Menus, lists and selection

Choose the semantic model:
- Action menu runs commands.
- Navigation list contains links.
- Listbox selects options.
- Combobox combines input and a popup.
- Checkbox/radio/switch model independent choice, exclusive choice or immediate setting.

They may share visual tokens but not one giant Type variant. Plain lists retain native Tab/link behavior; menus/listboxes use their appropriate composite keyboard model. Do not add arrows to every list.

Specify opening trigger, initial focus/active item, arrow/typeahead behavior, selection, Escape and restoration. Editable comboboxes preserve native text editing; where the model uses an active descendant, DOM focus stays in the input. [Combobox pattern](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/)

Keep selected state separate from focus/hover. Group labels, count, shortcuts and disabled explanations only when helpful. Indeterminate checkbox means partial group selection, not an arbitrary third choice.

Large collections need search/pagination or carefully verified virtualization. Preserve off-screen selections and meaningful position/count; do not claim virtualization is invisible to assistive technology without testing.

Verify pointer/touch, keyboard, opening at viewport edges, long labels, empty results and no hover-only actions. [Component Principles](Component%20Principles.md), [Accessibility](../01-Foundation/Accessibility.md)
