# Authentication

Owns identity entry, verification and recovery. [Account lifecycle](Authentication%20%26%20Account%20Patterns.md) owns ongoing identity controls; [Settings & Permissions](Settings%20%26%20Permissions.md) owns authorization UX.

Use the product's actual authentication methods and security policy. Do not promise passkeys, biometrics, SSO or trust features because they are fashionable. Explain supported options, fallback, device/system prompts and what happens after success.

Preserve intended destination and permitted draft context through sign-in/expiry. Support password managers, paste/autofill, visible requirements and accessible verification. Avoid needless password confirmation or inaccessible cognitive tests. [Accessibility](../01-Foundation/Accessibility.md)

Define credential errors, pending, rate-limit/lock states, expired/used links, lost factor/device, resend timing and recovery. Error wording protects sensitive account existence where policy requires it while still giving legitimate users a useful next action. A client design cannot enforce security guarantees.

For codes/links, allow correction and supported paste/autofill; a countdown must reflect actual expiry and not pressure unnecessarily. Do not classify arbitrary verification methods as independent security factors without security review.

Reauthentication should be tied to actual sensitive-action policy. State cancellation and pending work behavior. Authentication failure cannot become an unexplained dead end.

Verify returning/new/invited users, multiple methods, interruption, expired links, narrow viewport/software keyboard, keyboard and actual assistive flow. Record policy questions and implementation dependencies.
