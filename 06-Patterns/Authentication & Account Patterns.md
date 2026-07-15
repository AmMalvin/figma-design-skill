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