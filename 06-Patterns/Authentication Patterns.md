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