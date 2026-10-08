# Accessibility

Owns the accessibility baseline and verification boundaries. Use WCAG 2.2 Level AA for web; native work also follows relevant platform accessibility guidance. Conformance requires all applicable criteria, not this shortlist. [WCAG 2.2](https://www.w3.org/TR/WCAG22/)

## Quantitative checks

| Concern | Check |
| --- | --- |
| Text contrast | 4.5:1 for normal text; 3:1 for large text (18 pt regular or 14 pt bold). Measure actual adjacent backgrounds, including imagery and overlays. Apply exceptions only when the criterion permits. [SC 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) |
| Non-text contrast | Necessary control boundaries/states and meaningful graphics need 3:1 against adjacent colors, subject to the criterion's exceptions. Decorative borders are not all required indicators. [SC 1.4.11](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html) |
| Pointer targets | AA minimum is 24 x 24 CSS px or an applicable spacing/equivalent/inline/user-agent/essential exception. Record exceptions. Larger hit areas can improve touch usability; 44 x 44 is the enhanced AAA criterion, not the AA minimum. [SC 2.5.8](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) |
| Reflow | Equivalent 320 CSS px width for vertically scrolling web content without loss or two-dimensional scrolling, except task-essential two-dimensional content. Tables/charts need an intentional accessible strategy. [SC 1.4.10](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html) |

## Behavior contract

Specify meaningful name, role, value and state; visible labels/headings; logical reading/focus order; keyboard completion without traps; visible unobscured focus; status/error announcements; non-color cues; alternatives to dragging; text scaling/spacing, zoom and user motion preferences. [WCAG interaction requirements](https://www.w3.org/TR/WCAG22/)

Prefer native semantics. Links navigate; buttons act. Menus, listboxes, comboboxes, tabs and navigation have different keyboard models. Choose the appropriate [APG pattern](https://www.w3.org/WAI/ARIA/apg/patterns/) and inspect the runtime component. ARIA does not supply interaction code.

Dialogs define opening focus, modal containment, exit and restoration; the modal background is inert. If the trigger disappears, choose logical continuation. Dynamic results and toasts ordinarily preserve focus. [Modal dialog guidance](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/)

Authentication supports password managers, paste and accessible alternatives to cognitive-function tests. [SC 3.3.8](https://www.w3.org/WAI/WCAG22/Understanding/accessible-authentication-minimum.html)

## Evidence

Static design: measure contrast/hit areas; annotate semantic structure, focus, keyboard, announcements and error links; inspect long content and reflow. Runtime: execute the complete task with keyboard and representative assistive technology, including failure/dismissal. Automated checks supplement manual tests. Report environment, actual result and unresolved barrier. A Figma frame cannot prove screen-reader compatibility.

Connect [Design QA](../09-QA/Design%20QA.md) and relevant component/pattern contracts.
