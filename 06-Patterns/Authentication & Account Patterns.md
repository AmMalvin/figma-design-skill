# Account lifecycle

Owns profile, identity/provider/device management, privacy, consent and account closure. Entry/verification/recovery are defined once in [Authentication Patterns](Authentication%20Patterns.md).

Show what users can view/change, what takes effect immediately, what needs verification, and what is controlled by an organization. Differentiate profile data, authentication credentials and permissions.

For connected providers/trusted devices, show scope, last-known activity where reliable, revoke action and recovery implications. Do not let unlinking the sole access method strand users; inspect actual policy.

Privacy/consent controls explain purpose and consequence with real choices. Device permission, product consent and communication subscription are distinct mechanisms. Do not invent data-retention periods or legal requirements.

Deletion/closure review describes affected data/resources, irreversible effects, dependent members, ownership transfer and supported grace/recovery. Reauthentication and confirmation follow actual risk/policy, not a universal ritual. Cancellation must not be concealed.

Settings save, denied/org-managed, validation, pending/failure and uncertain commit need clear feedback. Preserve editable values on recoverable failure.

[Settings & Permissions](Settings%20%26%20Permissions.md), [Content Design](../01-Foundation/Content%20Design.md), [State Patterns](State%20Patterns.md)
