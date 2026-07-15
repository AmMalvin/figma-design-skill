---
title: Authentication & Account Patterns
version: 1.0.0
status: Stable
owner: Design System Skill
category: Patterns
priority: Critical
last_updated: 2026-07-15

inherits:
  - ./Pattern Principles.md
  - ../01-Foundation/Accessibility.md
  - ../01-Foundation/User Flows.md
  - ../01-Foundation/Information Architecture.md
  - ../01-Foundation/Responsive Design.md
  - ../05-Components/Inputs & Forms.md
  - ../05-Components/Buttons.md
  - ../05-Components/Feedback Components.md
  - ../05-Components/Navigation Components.md
  - ../05-Components/Modals, Dialogs & Drawers.md
---

# Authentication & Account Patterns

## Purpose

This module teaches the AI how to design secure, accessible, and scalable authentication and account management workflows.

Authentication should balance security with usability.

---

# Definition

Authentication verifies user identity and grants access to protected resources.

Account management enables users to manage their identity, security settings, and profile information throughout the product lifecycle.

---

# Objectives

After completing this module, the AI should be able to:

- Design authentication workflows
- Reduce sign-in friction
- Improve account security
- Support account recovery
- Protect user privacy
- Scale authentication across products

---

# Authentication Philosophy

Every authentication workflow should answer:

- Who is requesting access?
- How is identity verified?
- What level of security is required?
- What happens if verification fails?
- How can access be recovered?

Authentication should build user trust.

---

# Core Principles

Always:

- Minimize sign-in friction.
- Protect user accounts.
- Support account recovery.
- Explain authentication status.
- Reuse existing components.
- Support accessibility.

Never:

- Expose sensitive information.
- Reveal unnecessary security details.
- Lose authentication state unexpectedly.
- Block recovery unnecessarily.
- Duplicate authentication workflows.

---

# Authentication Lifecycle

Every workflow should define:

- Registration
- Verification
- Authentication
- Authorization
- Session
- Recovery
- Sign out

Each stage should remain predictable.

---

# Authentication Types

Common authentication methods include:

- Password authentication
- Passkeys
- Magic links
- One-time codes
- Multi-factor authentication
- Social sign in
- Enterprise single sign-on

Select the authentication method based on product requirements.

---

# Pattern Composition

Authentication patterns should reuse existing components.

Examples:

- Forms
- Buttons
- Dialogs
- Notifications
- Validation
- Progress indicators
- Feedback components

Avoid authentication-specific components when reusable components already exist.

---

# Success Metrics

Measure authentication using:

- Sign-in success rate
- Registration completion rate
- Password reset success rate
- Authentication failure rate
- Recovery completion rate
- Time to sign in

Measure successful access instead of interaction count.

---

# AI Decision Rules

Before approving an authentication workflow, answer:

- Does it protect user accounts?
- Is recovery available?
- Is accessibility supported?
- Does it reuse existing components?
- Is the workflow predictable?
- Can developers implement this consistently?

If any answer is negative, redesign the workflow.

---

# Validation Checklist

□ Purpose documented

□ Authentication lifecycle documented

□ Authentication types documented

□ Component composition documented

□ Success metrics documented

□ Accessibility reviewed

□ Documentation updated

---

# Authentication Workflows

## Philosophy

Every authentication workflow should balance security with usability.

Users should always understand:

- Why authentication is required
- What information is required
- What happens after authentication
- How to recover access

Authentication should minimize unnecessary effort.

---

# Sign Up

## Purpose

Allow new users to create an account.

Requirements:

- Collect only required information
- Validate input
- Explain password requirements
- Verify identity when required
- Confirm successful registration

Registration should remain simple.

---

# Sign In

## Purpose

Allow existing users to access their account.

Requirements:

- Email or username
- Password or alternative authentication
- Password visibility toggle
- Remember me when appropriate
- Forgot password link

Support password managers.

---

# Sign Out

## Purpose

End the authenticated session.

Requirements:

- Clear confirmation when appropriate
- Remove sensitive session data
- Redirect appropriately

Signing out should feel predictable.

---

# Email Verification

## Purpose

Confirm ownership of an email address.

Requirements:

- Verification email
- Resend option
- Expiration handling
- Success confirmation

Verification should not interrupt unrelated workflows.

---

# Phone Verification

## Purpose

Confirm ownership of a phone number.

Methods may include:

- SMS code
- Voice call
- Authenticator verification

Verification should expire after an appropriate period.

---

# Password Creation

## Purpose

Create secure credentials.

Requirements:

- Show password requirements
- Strength indicator
- Password visibility toggle
- Confirmation field only when required

Avoid unnecessary complexity.

---

# Password Reset

## Purpose

Restore account access.

Requirements:

- Identity verification
- Secure reset link or code
- New password creation
- Confirmation of success

Recovery should protect user privacy.

---

# Password Change

## Purpose

Allow authenticated users to update credentials.

Requirements:

- Current password verification when appropriate
- New password validation
- Confirmation message

Users should understand when changes take effect.

---

# Magic Links

## Purpose

Allow passwordless authentication through email.

Requirements:

- Single-use link
- Expiration time
- Secure verification
- Fallback authentication

Magic links should reduce friction.

---

# Passkeys

## Purpose

Support passwordless authentication using device credentials.

Requirements:

- Device compatibility
- Clear setup guidance
- Recovery options
- Fallback sign-in

Passkeys should improve both security and usability.

---

# Social Sign In

## Purpose

Authenticate using third-party identity providers.

Examples:

- Google
- Apple
- Microsoft
- GitHub

Explain what information will be shared.

---

# Enterprise Single Sign-On

## Purpose

Authenticate using organizational identity providers.

Examples:

- SAML
- OpenID Connect
- Microsoft Entra ID

Enterprise authentication should integrate with organizational policies.

---

# Authentication Selection Guide

Use:

Sign Up

For new users.

Sign In

For returning users.

Sign Out

For ending sessions.

Email Verification

For email ownership.

Phone Verification

For phone ownership.

Password Reset

For account recovery.

Password Change

For credential updates.

Magic Links

For passwordless access.

Passkeys

For modern secure authentication.

Social Sign In

For consumer identity providers.

Enterprise SSO

For organizational authentication.

---

# Workflow Variants

Represent authentication as reusable patterns.

Recommended properties:

Workflow

- Registration
- Sign In
- Sign Out
- Verification
- Recovery
- Passwordless
- SSO

State

- Default
- Verifying
- Authenticated
- Failed
- Locked
- Expired

Platform

- Web
- Mobile
- Desktop

Avoid duplicate authentication workflows.

---

# Responsive Behavior

Desktop

- Side-by-side layouts
- Full authentication options

Tablet

- Adaptive layouts
- Touch-friendly forms

Mobile

- Single-column forms
- Password manager support
- Biometric authentication when available

Authentication behavior should remain consistent across platforms.

---

# AI Authentication Selection Engine

Before selecting an authentication workflow, answer:

- Does this protect user accounts?
- Is sign-in friction minimized?
- Is recovery available?
- Is accessibility supported?
- Does this reuse existing components?
- Can this scale across products?

If any answer is negative, redesign the workflow.

---

# Validation Checklist

□ Sign up documented

□ Sign in documented

□ Sign out documented

□ Email verification documented

□ Phone verification documented

□ Password creation documented

□ Password reset documented

□ Password change documented

□ Magic links documented

□ Passkeys documented

□ Social sign in documented

□ Enterprise SSO documented

□ Responsive behavior documented

---

# Authentication Security

## Philosophy

Security should protect users without interrupting normal work.

Users should always understand:

- Why additional verification is required
- What action is expected
- Whether their account remains secure
- How to recover access

Security should increase trust.

---

# Multi-Factor Authentication

## Purpose

Require additional verification beyond the primary authentication method.

Common factors:

- Authenticator application
- Passkey
- Security key
- SMS verification
- Email verification

Prefer phishing-resistant authentication when supported.

---

# One-Time Passwords

## Purpose

Verify user identity using temporary codes.

Requirements:

- Limited validity
- Single use
- Resend option
- Expiration countdown
- Secure verification

Never reuse OTP codes.

---

# Biometric Authentication

## Purpose

Authenticate using trusted device capabilities.

Examples:

- Fingerprint
- Face recognition
- Device PIN when biometrics are unavailable

Biometrics should verify identity without exposing biometric data.

---

# Session Management

## Purpose

Manage authenticated user sessions securely.

Requirements:

- Session timeout
- Session renewal
- Secure sign out
- Session expiration notification

Users should understand when sessions expire.

---

# Device Management

## Purpose

Allow users to manage trusted devices.

Users should be able to:

- View registered devices
- Rename devices
- Remove devices
- Review recent activity

Device history improves account visibility.

---

# Trusted Devices

## Purpose

Reduce repeated authentication on verified devices.

Requirements:

- User consent
- Revocable trust
- Expiration period
- Device identification

Trusted devices should never bypass high-risk verification.

---

# Account Lockout

## Purpose

Protect accounts from repeated authentication failures.

Requirements:

- Temporary lockout
- Clear explanation
- Recovery options
- Unlock after verification

Avoid permanent lockouts.

---

# Suspicious Activity Detection

## Purpose

Identify potentially risky authentication events.

Examples:

- New device
- New location
- Unusual sign-in time
- Multiple failed attempts
- Impossible travel

Request additional verification when risk increases.

---

# Account Recovery

## Purpose

Restore access when authentication fails.

Recovery options may include:

- Verified email
- Verified phone
- Recovery codes
- Trusted devices
- Identity verification

Recovery should remain secure and understandable.

---

# Reauthentication

## Purpose

Verify identity before sensitive actions.

Examples:

- Password change
- Email change
- Payment confirmation
- Permission changes
- Account deletion

Use reauthentication for high-risk actions.

---

# Security Notifications

## Purpose

Keep users informed about important security events.

Examples:

- New sign in
- Password changed
- MFA enabled
- Device added
- Recovery completed

Notifications should explain what happened and what to do if the activity was unexpected.

---

# Authentication Security Selection Guide

Use:

Multi-Factor Authentication

For stronger authentication.

One-Time Passwords

For temporary verification.

Biometric Authentication

For device-based authentication.

Session Management

For active sessions.

Device Management

For trusted device control.

Trusted Devices

For reducing repeated verification.

Account Lockout

For repeated authentication failures.

Suspicious Activity Detection

For risk-based protection.

Account Recovery

For restoring access.

Reauthentication

For sensitive actions.

Security Notifications

For account awareness.

---

# Workflow Variants

Represent authentication security as reusable patterns.

Recommended properties:

Workflow

- MFA
- OTP
- Biometric
- Session
- Recovery
- Reauthentication
- Device

State

- Default
- Pending
- Verified
- Expired
- Locked
- Failed

Platform

- Web
- Mobile
- Desktop

Avoid duplicate authentication security workflows.

---

# Responsive Behavior

Desktop

- Full security dashboard
- Device management
- Session history

Tablet

- Adaptive layouts
- Touch-friendly controls

Mobile

- Biometric authentication
- Compact security settings
- Device-first verification

Security behavior should remain consistent across platforms.

---

# AI Authentication Security Engine

Before selecting a security workflow, answer:

- Is user identity protected?
- Is additional verification justified?
- Are recovery options available?
- Is accessibility supported?
- Does this reuse existing components?
- Can this scale across products?

If any answer is negative, redesign the workflow.

---

# Validation Checklist

□ Multi-factor authentication documented

□ One-time passwords documented

□ Biometric authentication documented

□ Session management documented

□ Device management documented

□ Trusted devices documented

□ Account lockout documented

□ Suspicious activity detection documented

□ Account recovery documented

□ Reauthentication documented

□ Security notifications documented

□ Responsive behavior documented

---

# Account Management

## Philosophy

Account management should give users control over their identity, preferences, and privacy.

Users should always understand:

- What information is stored
- What information is shared
- What security settings are active
- How to manage their account

Account ownership should remain transparent.

---

# Profile Management

## Purpose

Allow users to manage personal information.

Examples:

- Name
- Avatar
- Email
- Phone number
- Address
- Organization
- Job title

Only collect information required by the product.

---

# Account Preferences

## Purpose

Allow users to customize their experience.

Examples:

- Language
- Time zone
- Theme
- Date format
- Notification preferences
- Accessibility preferences

Preferences should synchronize across supported devices.

---

# Privacy Controls

## Purpose

Allow users to control personal information.

Examples:

- Profile visibility
- Activity visibility
- Search visibility
- Data sharing
- Marketing preferences

Privacy settings should use clear language.

---

# Consent Management

## Purpose

Collect and manage user consent.

Examples:

- Marketing consent
- Analytics consent
- Cookie preferences
- Data processing consent

Users should be able to withdraw consent when appropriate.

---

# Connected Accounts

## Purpose

Manage linked authentication providers.

Examples:

- Google
- Apple
- Microsoft
- GitHub
- Enterprise identity provider

Users should be able to connect and disconnect providers safely.

---

# Account Deletion

## Purpose

Allow users to permanently remove their account.

Requirements:

- Identity verification
- Clear consequences
- Confirmation
- Recovery period when supported

Deletion should never happen accidentally.

---

# Accessibility Across Authentication

## Purpose

Authentication should remain accessible.

Support:

- Keyboard navigation
- Screen readers
- High contrast
- Zoom
- Reduced motion
- Voice input

Accessibility should exist throughout every authentication workflow.

---

# Keyboard Navigation

Authentication should support:

- Logical tab order
- Visible focus
- Keyboard shortcuts when appropriate
- Enter to submit
- Escape to dismiss temporary interfaces

Authentication should not require a mouse.

---

# Focus Management

Focus should:

- Move logically
- Enter dialogs automatically
- Return after dialogs close
- Remain visible
- Never become trapped

Focus should always indicate the active task.

---

# Screen Reader Support

Authentication should expose:

- Labels
- Required fields
- Validation errors
- Password requirements
- Authentication status
- Recovery guidance
- Security notifications

Users should understand authentication without relying on visual cues.

---

# Responsive Authentication

Desktop

- Full account settings
- Multi-panel layouts
- Security dashboard

Tablet

- Adaptive layouts
- Touch-friendly controls

Mobile

- Single-column workflows
- Biometric authentication
- Simplified recovery
- Device-first interactions

Behavior should remain consistent across platforms.

---

# Performance

Authentication should:

- Respond quickly
- Minimize unnecessary requests
- Preserve entered information
- Recover gracefully from failures
- Synchronize account updates efficiently

Performance should reduce user friction.

---

# Design Token Integration

Authentication should reference design tokens.

Examples:

authentication.spacing

authentication.radius

authentication.focus.ring

authentication.motion.duration

authentication.success.color

authentication.warning.color

authentication.error.color

Avoid hardcoded values.

---

# Documentation Standards

Every authentication workflow should document:

- Purpose
- User goal
- Security requirements
- Workflow
- States
- Recovery options
- Accessibility
- Responsive behavior
- Components used
- Usage guidelines
- Do
- Don't
- Examples

Documentation should remove implementation ambiguity.

---

# Testing Strategy

Every authentication workflow should be tested for:

- Accessibility
- Keyboard navigation
- Screen reader compatibility
- Registration
- Sign in
- Recovery
- MFA
- Session handling
- Responsive layouts
- Performance

Testing should validate the complete authentication experience.

---

# Quality Assurance

Review every workflow for:

- Security
- Accessibility
- Workflow consistency
- Component reuse
- Responsive behavior
- Documentation
- Performance

Only approved authentication workflows belong in the design system.

---

# Versioning

Track changes for:

- Security improvements
- Authentication updates
- Accessibility improvements
- Privacy updates
- Bug fixes
- Breaking changes

Maintain complete version history.

---

# Governance

Authentication updates should include:

- UX review
- Accessibility review
- Security review
- Product review
- Engineering review
- QA approval
- Documentation update

Governance protects long-term consistency.

---

# AI Authentication Review Engine

Before publishing any authentication workflow, answer:

- Is user identity protected?
- Is authentication friction minimized?
- Are recovery options available?
- Is accessibility complete?
- Are design tokens used?
- Has testing been completed?
- Does this reuse existing components?
- Can this scale across products?

If any answer is negative, revise the workflow.

---

# Authentication Checklist

Before publishing:

□ Authentication workflows documented

□ Authentication security documented

□ Account management documented

□ Accessibility completed

□ Keyboard navigation verified

□ Screen reader support completed

□ Recovery workflows validated

□ Responsive behavior validated

□ Design tokens integrated

□ Testing completed

□ QA approved

□ Version history updated

□ Documentation completed

---

# Key Takeaways

Authentication should protect users while keeping access simple.

The AI must:

- Protect user identity.
- Reduce authentication friction.
- Support secure recovery.
- Support keyboard navigation.
- Support screen readers.
- Use design tokens.
- Test complete authentication workflows.
- Document every workflow.
- Reuse existing components.
- Scale across products.

Every authentication pattern should improve security, accessibility, consistency, privacy, and long-term maintainability.