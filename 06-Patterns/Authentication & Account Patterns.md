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