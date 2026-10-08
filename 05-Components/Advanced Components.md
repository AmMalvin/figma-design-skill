# Advanced interaction systems

Routes complex components; do not force calendars, maps, chat, editors, command palettes and Kanban into variants of one Type family.

| System | Non-obvious contract |
| --- | --- |
| Command palette | Visible alternative entry, scope, search vs execute, active result, Escape and focus restoration |
| Chat/assistant | Message order, streaming/pending/failed distinction, retry identity, editing history, unread/scroll behavior and user control over generated action |
| Calendar/scheduler | Locale/time zone, DST ambiguity, availability, overlap, keyboard date/event navigation and accessible list alternative |
| Kanban/timeline | Status/dependencies, move/reorder semantics, drag alternative, conflict and off-screen feedback |
| Rich editor | Text selection, formatting semantics, undo/redo, composition input, paste, autosave/conflict and toolbar focus |
| Map/spatial tool | Location accuracy, pan/zoom/reset, focused item, alternative list/search and permissions |
| Workspace | Region ownership, resizing/collapse, saved layout, focus movement and recoverable customization |

Reuse focused child contracts and keep domain policy local. Define inputs/data needs, supported states, content limits, performance constraints and accessible alternatives before visual polish.

Prototype the most uncertain behavior; runtime-test models Figma cannot represent faithfully. Large virtualized/live surfaces require actual focus/announcement checks. [Prototype Strategy](../04-Figma/Prototype%20Strategy.md), [Component Principles](Component%20Principles.md), [Accessibility](../01-Foundation/Accessibility.md)
