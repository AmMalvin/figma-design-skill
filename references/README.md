# Shared design references

Use this registry for research and principle extraction, not as a second design system. Source precedence belongs to [AI Operating Rules](../00-Core/AI%20Operating%20Rules.md).

[catalog.json](catalog.json) holds curated records. [intake.json](intake.json) holds user submissions awaiting inspection. [catalog.schema.json](catalog.schema.json) defines the shared entry contract. Categories are tags, so one source can serve several tasks without duplicate libraries or ten mostly empty folders.

| Category | Purpose and limit |
| --- | --- |
| standards | WCAG and interaction specifications; distinguish normative requirements from examples |
| product-benchmarks | Shipped behavior and complete flows; popularity does not demonstrate usability |
| visual-inspiration | Composition, typography and art direction; never outranks task, system or accessibility |
| interaction-patterns | Focus, keyboard, feedback and recovery models |
| mobile-patterns | Native/touch context; verify target OS and version |
| web-patterns | Browser semantics, responsive structure and web flows |
| dashboard-patterns | Comparison, monitoring and investigation; data relationships precede charts |
| motion-patterns | Timing, continuity and interruption; inspect actual motion, not still screenshots |
| design-system-references | Tokens, component contracts, libraries and evolution |
| reference-evaluation | Methods for judging fit and evidence; [Reference Evaluation](Reference%20Evaluation.md) owns the method |

Find records by category and pattern, then inspect the relevant source again when details may have changed. Authority classes describe the source's proper role, not blanket approval of its every example. The initial registry includes source overviews as well as inspected documentation; it does not claim that a complete production flow or award site was tested.

Apple HIG's landing page exposed a JavaScript shell; its first-party accessibility JSON was subsequently inspected. Awwwards could not be retrieved. Mobbin and CSS Design Awards were inspected as catalogs, and GOV.UK as a public service entry, without executing downstream flows. Those limits are recorded in each entry; do not fill missing observations from reputation.

Keep external observations in this area. Specialists link here rather than copy source lists. License and access restrictions still apply; retain a short description and source location rather than copying an entire library.
