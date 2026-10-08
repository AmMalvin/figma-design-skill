# Data management

Owns record lifecycle, persistence, batch integrity and recovery.

Define create/view/edit/draft/publish/archive/delete/restore/import/export from actual domain semantics. Archive is not always a substitute for deletion; distinguish visibility, retention and irreversible removal.

Choose explicit save or autosave per commitment boundary. Show saving/saved/failed/queued/stale state, version and conflict where relevant. Draft autosave can coexist with explicit publish if effects are clearly different.

Preserve valid work on recoverable failure. Retry safety depends on whether a commit occurred; unknown status requires reconciliation before repeating consequential operations. Do not promise undo/restore beyond the service's capabilities.

Concurrent edits need detection and a clear compare/merge/reload path without silently dropping local work. Historical versions and audit events reflect authoritative data, not fabricated reassurance.

Bulk operations show selected scope/count, eligible/ineligible items, preview, commit, partial success and retry only failed items when safe. Import previews map fields, detect duplicates, explain invalid rows and separate upload from processing. Exports show scope, format, permission and completion/failure.

Adapt editing surfaces by task complexity and need for comparison; do not make every edit a modal. Verify back/cancel, interruption, large data, access changes, narrow layout and keyboard flow.

[Form Workflows](Form%20Workflows.md), [Tables](../05-Components/Tables%20%26%20Data%20Grids.md), [Collaboration](Collaboration%20Patterns.md), [State Patterns](State%20Patterns.md)
