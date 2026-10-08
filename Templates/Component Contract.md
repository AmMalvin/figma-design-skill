# Component contract

- Purpose and exclusion: reusable interaction need, replacement when it fails.
- Anatomy: required/optional content and region relationships.
- API: meaningful properties, types, defaults and invalid combinations.
- States: trigger, appearance, semantics, interaction and recovery.
- Sizing: content-driven bounds, density, overflow, resizing and localization.
- Input/accessibility: element/role, accessible name, focus, keyboard, touch, status and reduced motion.
- Content: limits, long strings, icons, error copy and empty values.
- System: existing variables/styles, modes and component references.
- Code alignment: conceptual prop mapping, service assumptions and responsibility boundaries.
- Verification: representative valid/invalid configurations, rendered content and runtime checks.
- Change: consumers, compatibility and migration if this modifies an existing contract.

Use text, visibility and instance swaps where appropriate; create variants for genuinely different configurations or states. Do not multiply every combination mechanically. A design contract does not demonstrate runtime conformance.
