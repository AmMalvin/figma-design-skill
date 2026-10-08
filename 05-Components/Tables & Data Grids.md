# Tables and data grids

Use tables for aligned record comparison. Use an interactive grid only when cell-level editing/navigation demands it; an ARIA grid imposes a different keyboard contract than a semantic HTML table.

Choose primary identifier, comparison columns, units, precision, missing-value notation and row actions from the task. Align comparable numeric values and keep headers associated. Financial zero is not missing data.

Sorting states its column/direction; filters/search show scope and query. Sorting/pagination must not erase intended selections. "Select page" and "Select all matching" are different contracts; display count/scope and partial-selection state.

Inline editing specifies enter/edit/save/cancel, validation, conflict and pending/failed commit. Bulk work previews affected scope and handles partial failures. Sticky headers/columns must not obscure focused content.

For narrow screens, preserve task-essential comparison through intentional horizontal scrolling or a suitable summary/detail route. Do not hide fields without accessible retrieval or automatically turn every row into a card.

Large data may need server pagination, cursor loading or virtualization. Coordinate dataset scope/count, loading, focus retention, accessible headers/indexes and off-screen selection; performance claims need runtime evidence.

Verify long cells, localization, no rows/no matches/denied/error/stale data, selection across pages, keyboard and supported widths. Study [Carbon data tables](https://carbondesignsystem.com/components/data-table/usage/) as pattern guidance, adapted to the project. [Data-Dense Interfaces](../06-Patterns/Data-Dense%20Interfaces.md), [Accessibility](../01-Foundation/Accessibility.md)
