# Notifications and communication

Owns event relevance, channel, timing, user control and history. Local UI feedback lives in [Feedback Components](../05-Components/Feedback%20Components.md).

For each event specify recipient, value, urgency, action, channel, deduplication, timing, preference and persistence. A channel is a delivery contract, not a Figma Type variant.

Use inline/in-app for active task context; push for valuable timely external events with actual permission; email/digest for durable asynchronous work. SMS or high-urgency alerts require a justified product need. Do not send messages or subscribe users merely because a design specifies them.

Separate unread from unresolved/action-required. Mark-read must not imply the task is completed. Group repeats while preserving critical events and accurate counts. Deep links honor access and preserve orientation.

Preferences define per-channel/type control, quiet hours/time zone, snooze, critical exceptions and clear status. Device permission differs from product preference. Honor declines without repetitive prompts.

Delivery failed/delayed, duplicated event, stale destination, expired access and deleted resource need safe fallbacks. Unresolved critical information cannot vanish as a transient toast.

Announce relevant updates without unexpected focus jumps. Verify long content, multiple messages, ordering/history, keyboard/narrow layout and actual delivery semantics. [Content Design](../01-Foundation/Content%20Design.md), [State Patterns](State%20Patterns.md)
