# Mobile components

Owns touch-specific mechanics; [Platform Conventions](../01-Foundation/Platform%20Conventions.md) owns source selection.

Sheets, action sheets, refresh, swipe/reorder and navigation are distinct contracts, not variants of one mobile component. Use the platform's existing controls and current conventions.

Account for hit areas, reach, safe areas, software keyboard, orientation, interruption, system back and external keyboard/assistive input. A FAB or bottom sheet earns use from the task, not mobile width alone.

Gestures accelerate visible actions; essential actions have an accessible alternative. Swipe needs intentional activation, cancellation, feedback and protection against scroll conflicts. Drag/reorder needs a non-drag route. Pull-to-refresh must not be the sole way to refresh.

Haptics supplement visible state. Dynamic text and zoom must not clip content; sticky actions must not cover fields/errors or the system keyboard.

Define offline/queued status only where supported. Preserve progress through backgrounding and session interruption subject to policy.

Verify device/platform behavior, touch and non-touch completion, safe-area edges, long content and rotation. [Responsive Design](../01-Foundation/Responsive%20Design.md), [Accessibility](../01-Foundation/Accessibility.md)
