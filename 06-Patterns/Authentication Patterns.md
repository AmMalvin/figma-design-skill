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