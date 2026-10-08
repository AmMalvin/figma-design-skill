# Responsive design

Owns content-driven adaptation across supported viewports and windows.

Change structure when content/interaction fails, not from a fixed device taxonomy. Test intermediate width, short height, zoom, software keyboard and split windows.

| Region | Specify |
| --- | --- |
| Navigation | Destinations/context preserved through presentation changes |
| Reading | Measure, wrapping and semantic order |
| Forms/toolbars | Wrapping/grouping with visible labels, errors and focused fields |
| Tables | Intentional comparison scroll or task-appropriate summary/detail; hidden data remains accessible |
| Dashboards | Task-priority reordering, not equally shrunk charts |
| Overlays | Task-driven bounded/full-screen/non-modal surface with exit and focus |
| Spatial/media tools | Context/aspect preservation and alternatives to pan/zoom/drag |

Keep essential functions reachable. Preserve selection, query, task state and unfinished work during adaptation. Width does not determine input: a large touch display still needs touch comfort; a narrow device with a keyboard still needs focus.

Deliver representative layouts plus rules between them, overflow and content constraints. Use [Accessibility](Accessibility.md) for reflow/zoom requirements and inspect actual behavior; two static frames do not prove responsiveness.
