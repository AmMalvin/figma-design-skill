# State patterns

Owns meaning and recovery of non-happy paths. Choose the state from its cause, not one generic empty illustration.

| State | Meaning and response |
| --- | --- |
| First-use empty | No content yet; explain value and appropriate creation/import |
| No matches | Existing corpus filtered away; preserve query and offer refinement/reset |
| Denied/read-only | Effective access limits task; explain permitted reason and next route without leaking private data |
| Loading/pending | Work accepted but incomplete; truthful acknowledgement/progress with stable context |
| Partial data/success | Identify completed/missing/failed scope and safe action on remainder |
| Stale/offline | Show last-known freshness and supported capability; queued work differs from saved server state |
| Error | Explain known failure, preserve safe input and actionable recovery |
| Unknown commitment | Reconcile status before repeating a consequential operation |
| Success | Show confirmed outcome/reference, resulting state and useful next action |
| Interrupted | Restore permitted draft/context or explain expiry/loss and restart safely |

Skeletons fit predictable initial structure, not every wait. Short work may need only inline pending; long work needs useful status and cancel/background behavior where supported. Never fabricate percentage or remaining time.

Preserve focus and user control through background updates. Announce meaningful status, not every tick. Avoid illustration/celebration as a mandatory pattern.

Specify cause, data shown/hidden, available actions, persistence, focus/announcement and backend dependency. Exercise missing data, service failure, long text, huge data, repeated attempts and changed permissions. [Accessibility](../01-Foundation/Accessibility.md), [Interaction Design](../01-Foundation/Interaction%20Design.md)
