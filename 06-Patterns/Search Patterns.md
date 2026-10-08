# Search and refinement

Canonical search behavior; [supplemental discovery notes](Search%20%26%20Discovery%20Patterns.md) provide additional entry/discovery candidates.

Identify known-item lookup versus exploratory browsing, corpus/scope, permissions, ranking and result data. Keep scope/query/filters/sort visible enough to explain the result. Do not leak hidden resources through suggestions/counts.

Suggestions accelerate input when relevant; they must not interrupt typing, rewrite the query silently or unexpectedly move focus. A combobox needs its proper keyboard/active-item model; a simple submitted search need not be a combobox. [Selection Controls](../05-Components/Menus,%20Lists%20%26%20Selection%20Controls.md)

Handle pending requests, cancellation and out-of-order responses so stale results never overwrite a newer query. Choose submit/debounce/explicit filter apply from latency and task; do not prescribe one arbitrary delay. Preserve the query on failure.

Define facet semantics (often OR within a facet and AND across facets, but confirm the data model), counts, multi-select, apply/reset and incompatible filters. Active filters are removable; sorting does not erase them.

Results expose identity, useful metadata and why a match helps. Distinguish no records, no matches, denied corpus, error and offline. Zero matches offer safe broadening/clear filters without losing query.

Pagination fits bounded/revisited results; continuous load fits exploration and needs return-position, no duplicates and reachable footer/controls. Preserve state through detail and back; choose URL/history persistence where appropriate.

Do not announce every keystroke or shift focus into changing results. Provide meaningful settled result status. Search history is user-controlled and privacy-aware.

Verify typical/ambiguous/typo/long queries, filters, rapidly changed requests, huge/no results, keyboard/touch and narrow layouts. Ranking quality needs actual data evidence, not a plausible mockup.

[Information Architecture](../01-Foundation/Information%20Architecture.md), [Accessibility](../01-Foundation/Accessibility.md), [Reference Intake](../references/Reference%20Intake.md)
