# Platform conventions

Owns platform fit. Maintain coherent product language while adapting navigation, controls, gestures, accessibility and lifecycle.

Consult [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/) for Apple work and the relevant [Fluent platform](https://fluent2.microsoft.design/) for cross-platform architecture. Android work follows its chosen native/Material system; verify current official guidance for affected behavior.

Inspect platform/version and available components before specifying back, sheets, keyboard, safe areas, scaling, notifications or OS authentication. Do not impose CSS units on native targets.

Web respects semantics, browser history, links, deep links and keyboard. Desktop accounts for resizable windows, shortcuts, pointer precision and multi-pane work. Mobile accounts for touch, safe areas, software keyboard, interruption, rotation and system back. These are considerations, not one composition.

A departure needs gain, relearning cost, accessible fallback and a test. The [catalog](../references/catalog.json) records source evidence: retrieving a JS-only landing page does not prove detailed behavior was inspected.

Connect [Mobile Components](../05-Components/Mobile%20Components.md) and [Responsive Design](Responsive%20Design.md).
