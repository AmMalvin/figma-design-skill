# Analytics specification

Fixture: enterprise-dashboard scenario. Existing compact table, severity roles and chart palette. This is a written interaction specification, not a rendered dashboard.

## Analytical question and composition

An operations analyst compares incident rate by service and asks which change explains a spike. Use a comparison time series with a service table and a contextual investigation region. A shared period/filter row controls the comparison. Selected service and time interval connect both representations.

Multiple simultaneous priorities are intentional: the analyst watches change while inspecting evidence. A single large KPI hero would obscure relationships. For a small dataset and a single known exception, a list/detail workflow could replace the analytical workspace.

Show units, period, source and freshness. Chart gaps represent missing measurements. Use a zero baseline where bar-length comparison requires it; a time-series scale follows the analytical question with transparent labeling.

## Behavioral contract

| Situation | Response |
| --- | --- |
| Filter change | Preserve usable previous context while reporting requested update |
| Partial source delay | Identify source and freshness; do not show missing observations as zero |
| Select service/interval | Update linked detail without silently discarding global filters |
| Inspect then return | Restore selected interval, table sort and scroll |
| No incidents | Explain observed zero only when the source is available |
| No matching services | Offer filter recovery; distinguish from unavailable data |
| Bulk action | Expose selection scope and item-level outcome, if the task actually requires actions |

The read-only table uses native table semantics and focusable sorting/detail controls. Do not make every passive cell a Tab stop. An editable spreadsheet-like model would require a separate grid contract.

## Responsive and system decisions

Retain essential service/rate/freshness comparison on narrow screens; detail can become a separate view with preserved context. Intentionally scrolling a two-dimensional comparison is justified only for the comparison region. The rest of the page reflows.

Reuse semantic chart, severity, text and compact spacing roles. No new glow, floating card grid or brand color is needed. Provide accessible chart summary and data view; distinguish series using labels and more than color. Virtualization, sorting semantics and assistive-technology reading require implementation tests.

## Handoff and critique

Service assumptions: incident-rate definition, denominator, time zone, source update times and permitted service access. Performance perception comes from usable retained context and truthful update status, not decorative animation.

The specification addresses comparative task structure and stale data. Real data scale, label collisions, typography, component binding, focus and query latency remain unverified. Critique should prioritize a misleading freshness claim above attractive chart styling.
