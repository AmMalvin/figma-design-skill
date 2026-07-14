---
title: Authentication Patterns
version: 1.0.0
status: Stable
owner: Design System Skill
category: Patterns
priority: Critical
last_updated: 2026-07-14

inherits:
  - ./Pattern Principles.md
  - ../01-Foundation/Accessibility.md
  - ../01-Foundation/User Flows.md
  - ../01-Foundation/Responsive Design.md
  - ../05-Components/Inputs & Forms.md
  - ../05-Components/Feedback Components.md
  - ../05-Components/Modals, Dialogs & Drawers.md
---

# Authentication Patterns

## Purpose

This module teaches the AI how to design secure, accessible, scalable, and reusable authentication workflows.

Authentication patterns establish user identity while minimizing friction.

---

# Definition

Authentication verifies a user's identity before granting access.

Authentication should be treated separately from authorization.

Authentication answers:

"Who is the user?"

Authorization answers:

"What may the user access?"

---

# Objectives

After completing this module, the AI should be able to:

- Design secure authentication flows
- Reduce sign-in friction
- Support multiple authentication methods
- Improve accessibility
- Handle authentication errors
- Maintain workflow consistency

---

# Authentication Philosophy

Every authentication workflow should answer:

- Who is signing in?
- Why is authentication required?
- What is the quickest secure path?
- What happens after success?

Security should never unnecessarily increase user effort.

---

# Core Principles

Always:

- Minimize required input.
- Protect user data.
- Explain security steps.
- Support password managers.
- Preserve user progress.
- Reuse existing components.

Never:

- Request unnecessary information.
- Hide authentication errors.
- Expose sensitive information.
- Create confusing recovery paths.
- Block legitimate users without guidance.

---

# Authentication Lifecycle

Every authentication pattern should define:

- Entry point
- Credential collection
- Identity verification
- Success
- Failure
- Recovery
- Session creation
- Exit

Every stage should be predictable.

---

# Authentication Methods

Support authentication methods appropriate for the product.

Examples:

- Email and password
- Magic link
- Passkey
- Social sign in
- Enterprise single sign-on
- Multi-factor authentication

Offer only methods appropriate for the product context.

---

# Pattern Composition

Authentication patterns should reuse existing components.

Examples:

- Inputs
- Buttons
- Checkboxes
- Alerts
- Dialogs
- Progress indicators
- Loading states
- Feedback components

Avoid creating authentication-specific UI when reusable components already exist.

---

# Security Principles

Authentication should:

- Verify identity
- Protect credentials
- Prevent unauthorized access
- Support secure session management
- Communicate security events clearly

Security should remain understandable.

---

# User Experience Principles

Authentication should:

- Require the fewest practical steps
- Reduce cognitive effort
- Preserve trust
- Provide immediate feedback
- Recover gracefully from mistakes

Authentication should help users succeed.

---

# AI Decision Rules

Before approving an authentication pattern, answer:

- Is security appropriate?
- Is the workflow simple?
- Is accessibility supported?
- Does this reuse existing components?
- Can users recover easily?
- Can developers implement this consistently?

If any answer is negative, redesign the workflow.

---

# Validation Checklist

□ Purpose documented

□ Authentication lifecycle documented

□ Authentication methods documented

□ Component composition documented

□ Security principles documented

□ Accessibility reviewed

□ Documentation updated


---

# Authentication Workflows

## Philosophy

Authentication should verify identity with the fewest practical steps.

Users should always understand:

- Why authentication is required
- Which authentication methods are available
- What happens after authentication
- How to recover from problems

Reduce friction without reducing security.

---

# Sign Up

## Purpose

Create a new user account.

Typical flow:

- Enter identity information
- Verify required fields
- Accept terms when required
- Verify email or phone
- Create session
- Continue onboarding

Only request information required for account creation.

---

# Sign In

## Purpose

Authenticate an existing user.

Typical flow:

- Enter credentials
- Verify identity
- Create session
- Redirect to destination

Support returning users with minimal effort.

---

# Password Authentication

Use passwords only when appropriate.

Requirements:

- Secure password creation
- Show password option
- Password manager support
- Strength guidance
- Validation feedback

Never expose passwords.

---

# Magic Link

## Purpose

Authenticate without a password.

Typical flow:

- Enter email
- Receive secure link
- Open link
- Verify identity
- Create session

Clearly communicate link expiration.

---

# Passkeys

## Purpose

Authenticate using device credentials.

Examples:

- Face authentication
- Fingerprint authentication
- Device PIN

Offer passkeys whenever supported.

---

# Social Sign In

## Purpose

Allow authentication using trusted identity providers.

Examples:

- Google
- Apple
- Microsoft
- GitHub

Clearly explain what information is shared.

---

# Enterprise Single Sign-On

## Purpose

Authenticate organizational users.

Examples:

- SAML
- OpenID Connect
- Enterprise identity provider

Enterprise users should reach authentication quickly.

---

# Multi-Factor Authentication

## Purpose

Require an additional verification step.

Examples:

- Authenticator application
- Security key
- SMS code when required
- Email verification

Explain why additional verification is needed.

---

# Session Creation

Successful authentication should:

- Create a secure session
- Restore intended destination
- Load user preferences
- Confirm successful sign in

Avoid unnecessary intermediate screens.

---

# Remember Me

Allow users to remain signed in when appropriate.

Requirements:

- Optional selection
- Clear explanation
- Respect security policies

Do not enable automatically on shared devices.

---

# Sign Out

Signing out should:

- End the current session
- Remove sensitive session data
- Confirm completion
- Redirect appropriately

Users should always know they have signed out successfully.

---

# Authentication Selection Guide

Use:

Sign Up

For first-time users.

Sign In

For returning users.

Password Authentication

When passwords are supported.

Magic Link

When passwordless email authentication is preferred.

Passkeys

When supported devices are available.

Social Sign In

When trusted external identity providers are supported.

Enterprise Single Sign-On

For organizational authentication.

Multi-Factor Authentication

For higher security requirements.

---

# Authentication Variants

Represent authentication workflows as reusable patterns.

Recommended properties:

Method

- Password
- Magic Link
- Passkey
- Social
- Enterprise SSO
- Multi-Factor

State

- Default
- Loading
- Verification
- Success
- Error
- Locked

Platform

- Web
- Mobile
- Desktop

Avoid creating duplicate authentication workflows.

---

# Responsive Behavior

Desktop

- Multi-column layouts
- Expanded authentication options

Tablet

- Simplified layouts
- Touch-friendly controls

Mobile

- Single-column layout
- Device authentication
- Passkey support
- Biometric authentication

Authentication should remain consistent across platforms.

---

# AI Authentication Selection Engine

Before selecting an authentication workflow, answer:

- Is this the simplest secure method?
- Does it match product requirements?
- Is accessibility supported?
- Does it reuse existing components?
- Is recovery available?
- Can developers implement this consistently?

If any answer is negative, choose a more appropriate authentication workflow.

---

# Validation Checklist

□ Sign up documented

□ Sign in documented

□ Password authentication documented

□ Magic link documented

□ Passkeys documented

□ Social sign in documented

□ Enterprise SSO documented

□ Multi-factor authentication documented

□ Session creation documented

□ Remember me documented

□ Sign out documented

□ Variant strategy documented

□ Responsive behavior documented

---

# Recovery & Verification Workflows

## Philosophy

Recovery workflows should restore account access without weakening security.

Users should always understand:

- Why verification is required
- What recovery options are available
- What happens next
- How long recovery remains valid

Recovery should protect legitimate users.

---

# Password Reset

## Purpose

Allow users to securely create a new password.

Typical flow:

- Select Forgot Password
- Enter verified email or username
- Receive recovery link or code
- Verify identity
- Create new password
- Sign in

Never reveal whether an account exists.

---

# Account Recovery

## Purpose

Restore account access when normal authentication fails.

Examples:

- Lost password
- Lost device
- Lost passkey
- Lost authenticator application

Recovery should verify identity before restoring access.

---

# Email Verification

## Purpose

Verify ownership of an email address.

Typical flow:

- Register account
- Send verification email
- Select verification link
- Confirm ownership
- Activate account

Verification links should expire.

---

# Phone Verification

## Purpose

Verify ownership of a phone number.

Examples:

- SMS code
- Voice verification

Phone verification should support secure recovery.

---

# Account Lockout

## Purpose

Protect accounts from repeated failed authentication.

Requirements:

- Temporary lock
- Clear explanation
- Recovery guidance

Users should understand how access is restored.

---

# Rate Limiting

Authentication endpoints should prevent abuse.

Examples:

- Login attempts
- Password reset requests
- Verification requests

Protection should reduce automated attacks.

---

# Session Expiration

Sessions should expire according to product security requirements.

Examples:

- Inactivity timeout
- Maximum session duration
- Forced reauthentication

Users should receive appropriate notice when possible.

---

# Device Management

Allow users to review trusted devices.

Typical capabilities:

- Current device
- Previous devices
- Active sessions
- Remove device
- Rename device

Users should remain in control of account access.

---

# Trusted Devices

Trusted devices reduce unnecessary authentication prompts.

Requirements:

- Explicit user consent
- Secure storage
- Easy removal

Never trust devices automatically.

---

# Authentication Errors

Authentication errors should explain:

- What happened
- What users should do next

Avoid exposing sensitive security information.

Examples:

- Incorrect credentials
- Expired verification
- Invalid recovery code
- Session expired

Messages should remain understandable.

---

# Security Notifications

Notify users of important security events.

Examples:

- Password changed
- New device
- New location
- Recovery completed
- Multi-factor authentication updated

Notifications should build trust.

---

# Recovery Selection Guide

Use:

Password Reset

For forgotten passwords.

Account Recovery

When users lose authentication methods.

Email Verification

For new accounts.

Phone Verification

When phone ownership is required.

Account Lockout

To reduce repeated failed authentication attempts.

Trusted Devices

To reduce repeated verification on known devices.

---

# Recovery Variants

Represent recovery workflows as reusable patterns.

Recommended properties:

Recovery Type

- Password
- Email
- Phone
- Passkey
- Device
- Multi-Factor

State

- Default
- Verification
- Loading
- Success
- Error
- Expired
- Locked

Platform

- Web
- Mobile
- Desktop

Avoid duplicate recovery workflows.

---

# Responsive Behavior

Desktop

- Expanded forms
- Device management dashboard

Tablet

- Adaptive layouts
- Touch-friendly verification

Mobile

- One-time code autofill
- Passkey support
- Biometric recovery
- Simplified verification

Recovery should remain consistent across platforms.

---

# AI Authentication Recovery Engine

Before approving a recovery workflow, answer:

- Is identity verified?
- Is account enumeration prevented?
- Is recovery understandable?
- Is accessibility supported?
- Does this reuse existing components?
- Can developers implement this consistently?

If any answer is negative, redesign the workflow.

---

# Validation Checklist

□ Password reset documented

□ Account recovery documented

□ Email verification documented

□ Phone verification documented

□ Account lockout documented

□ Rate limiting documented

□ Session expiration documented

□ Device management documented

□ Trusted devices documented

□ Authentication errors documented

□ Security notifications documented

□ Responsive behavior documented

---

# Accessibility Across Authentication

## Purpose

Authentication should be accessible to every user.

Users should be able to authenticate regardless of:

- Device
- Input method
- Ability
- Platform

Accessibility should exist throughout the authentication journey.

---

# Keyboard Navigation

Authentication workflows should fully support keyboard interaction.

Requirements:

- Logical tab order
- Visible focus
- Enter submits forms
- Escape dismisses temporary interfaces
- Keyboard shortcuts where appropriate

Authentication should never require a mouse.

---

# Focus Management

Focus should:

- Move logically
- Remain visible
- Enter dialogs automatically
- Return after dialogs close
- Never become trapped unintentionally

Focus should always indicate the current task.

---

# Screen Reader Support

Authentication should expose:

- Form labels
- Field requirements
- Validation errors
- Authentication progress
- Success messages
- Recovery guidance

Users should understand every authentication step.

---

# Password Manager Support

Authentication should support password managers.

Requirements:

- Proper field labels
- Username autocomplete
- Password autocomplete
- New password fields
- Current password fields

Avoid blocking password manager behavior.

---

# Passkey Experience

When passkeys are available:

- Explain what a passkey is
- Explain why it is secure
- Allow fallback authentication
- Clearly communicate device prompts
- Support passkey management

Users should understand every passkey interaction.

---

# Responsive Authentication

Desktop

- Expanded authentication options
- Multi-column layouts when appropriate

Tablet

- Adaptive layouts
- Touch-friendly controls

Mobile

- Single-column forms
- Biometric authentication
- Passkeys
- One-time code autofill

Authentication should remain consistent across platforms.

---

# Design Token Integration

Authentication should reference design tokens.

Examples:

auth.spacing

auth.radius

auth.focus.ring

auth.motion.duration

auth.success.color

auth.warning.color

auth.error.color

Avoid hardcoded values.

---

# Documentation Standards

Every authentication workflow should document:

- Purpose
- Entry point
- Authentication method
- Recovery options
- States
- Accessibility
- Security considerations
- Responsive behavior
- Components used
- Usage guidelines
- Do
- Don't
- Examples

Documentation should eliminate implementation ambiguity.

---

# Testing Strategy

Every authentication workflow should be tested for:

- Accessibility
- Keyboard navigation
- Screen reader compatibility
- Password manager compatibility
- Passkey support
- Responsive layouts
- Error recovery
- Performance

Testing should validate the complete authentication journey.

---

# Quality Assurance

Review every authentication workflow for:

- Security
- Accessibility
- Workflow consistency
- Component reuse
- Responsive behavior
- Documentation
- Performance

Only approved authentication patterns belong in the design system.

---

# Versioning

Track changes for:

- Authentication methods
- Accessibility improvements
- Security updates
- Recovery improvements
- Bug fixes
- Breaking changes

Maintain complete version history.

---

# Governance

Authentication updates should include:

- UX review
- Security review
- Accessibility review
- Engineering review
- QA approval
- Documentation update

Governance protects consistency and security.

---

# AI Authentication Review Engine

Before publishing any authentication workflow, answer:

- Is security appropriate?
- Is accessibility complete?
- Is keyboard navigation supported?
- Is password manager support verified?
- Is passkey support documented?
- Does this reuse existing components?
- Has testing been completed?
- Can this scale across products?

If any answer is negative, revise the workflow.

---

# Authentication Checklist

Before publishing:

□ Authentication method documented

□ Sign up documented

□ Sign in documented

□ Recovery documented

□ Accessibility completed

□ Keyboard navigation verified

□ Screen reader support completed

□ Password manager support verified

□ Passkey support documented

□ Responsive behavior validated

□ Design tokens integrated

□ Testing completed

□ QA approved

□ Version history updated

□ Documentation completed

---

# Key Takeaways

Authentication patterns establish secure user identity while minimizing friction.

The AI must:

- Choose the simplest secure authentication method.
- Reuse existing components.
- Support password managers.
- Support passkeys.
- Support keyboard navigation.
- Support screen readers.
- Use design tokens.
- Test complete authentication journeys.
- Document every authentication workflow.

Every authentication pattern should improve security, accessibility, consistency, and long-term maintainability.