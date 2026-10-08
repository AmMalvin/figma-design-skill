# Settings and permissions

Owns configuration and authorization UX. Authentication establishes identity; permissions determine capability.

Organize settings by user task/scope (personal, resource, workspace, organization), not internal API grouping. Use clear labels/search for larger settings sets. Distinguish immediate, explicit save, autosaved draft and policy-managed changes.

For roles, show meaningful capabilities, resource scope, inheritance and effective access. A permissions matrix suits systematic comparison; a role selector plus detail suits simple assignment. Do not make switches ambiguous between preview and immediate grant.

Prevent accidental lockout, loss of the last required owner and unsafe public access according to actual service rules. Preview affected users/resources and consequential grants/revocations; use confirmation where risk warrants it. Do not invent allowable roles or policy.

Handle pending invitation, expired/revoked access, mixed/bulk assignment, forbidden action, inherited read-only setting, conflict and partial update. Revocation mid-task preserves allowed work and explains next action without exposing protected content.

Visibility can explain missing privilege when disclosure is safe; hide inaccessible sensitive resources where policy requires. UI controls never replace server enforcement.

Verify long role/member names, many resources, narrow viewport, keyboard/table semantics, cancellation and actual committed privileges. [Data Management](Data%20Management%20Patterns.md), [Account lifecycle](Authentication%20%26%20Account%20Patterns.md), [Accessibility](../01-Foundation/Accessibility.md)
