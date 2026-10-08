# Form workflows

Canonical orchestration guide. [Inputs & Forms](../05-Components/Inputs%20%26%20Forms.md) owns controls; [supplemental notes](Data%20Entry%20%26%20Form%20Patterns.md) preserve existing completion/upload guidance.

Collect only information needed for the task. Group by meaning and dependency. A long form need not become a wizard automatically: use steps for real stages, otherwise support sectional review and navigation.

Specify validation timing, conditional fields, cross-field rules, async checks, server errors and recovery. Avoid premature errors on incomplete typing. After failed submit provide a summary with field links and a logical focus target; preserve valid work and explain new requirements.

Choose explicit save, draft/autosave or immediate commit deliberately. Show saved/saving/failed/queued truthfully. Sensitive changes may need explicit review even when draft content autosaves; distinguish those commitments.

Enter should not unexpectedly submit multiline text or commit high-risk operations. Cancellation/back preserves progress or explains actual loss. Do not promise local persistence beyond product/security policy.

Uploads support browse/native picker, file limits/types, per-file progress/cancel/remove/retry and processing status. Batch work describes validation and partial failure per record.

Test long labels/values, paste/autofill, localization, multiple errors, conditional step changes, session interruption, narrow viewport/software keyboard and keyboard/assistive flow. A sticky action bar must not cover error/focus targets.

Example: an enterprise application needs draft state, section completeness and review; a short settings edit may need only one field and an immediate result. Neither requires a card per input.

[Accessibility](../01-Foundation/Accessibility.md), [Content Design](../01-Foundation/Content%20Design.md), [Data Management](Data%20Management%20Patterns.md)
