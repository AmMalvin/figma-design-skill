---
title: Feedback Components
version: 1.0.0
status: Stable
owner: Design System Skill
category: Components
priority: Critical
last_updated: 2026-07-13

inherits:
  - ../00-Core/Universal Design Principles.md
  - ../01-Foundation/Accessibility.md
  - ../01-Foundation/Layout Systems.md
  - ../02-Visual-System/Color Theory.md
  - ../02-Visual-System/Typography.md
  - ../02-Visual-System/Iconography.md
  - ../02-Visual-System/Spacing & Sizing.md
  - ./Component Principles.md
---

# Feedback Components

## Purpose

This module teaches the AI how to design scalable, reusable, accessible, and production-ready feedback components.

Feedback helps users understand what has happened, what is happening, and what happens next.

---

# Definition

Feedback components communicate system status, validation, progress, success, warnings, errors, and informational messages.

Feedback should always reduce uncertainty.

---

# Objectives

After completing this module, the AI should be able to:

- Design reusable feedback components
- Communicate system status
- Improve task completion
- Reduce user confusion
- Support accessibility
- Support responsive layouts
- Improve developer implementation
- Scale across products

---

# Feedback Philosophy

Every feedback component should answer:

- What happened?
- Why did it happen?
- What should the user do next?

Feedback should always be actionable.

---

# Core Principles

Always:

- Be timely.
- Be clear.
- Be concise.
- Explain outcomes.
- Suggest recovery when needed.
- Maintain consistency.

Never:

- Use vague language.
- Hide critical information.
- Rely only on color.
- Interrupt users unnecessarily.
- Display unnecessary messages.

---

# Why Feedback Exists

Feedback helps users:

- Confirm actions
- Recover from errors
- Monitor progress
- Understand system status
- Build confidence
- Continue workflows

Feedback should reduce uncertainty.

---

# Feedback Anatomy

Every feedback component should define:

- Container
- Icon
- Title
- Message
- Actions
- Dismiss control
- Status

Each element should have one responsibility.

---

# Status Types

Support these semantic statuses:

- Success
- Information
- Warning
- Error
- Neutral

Status meanings should remain consistent across products.

---

# Message Structure

Messages should contain:

- Short title
- Clear explanation
- Helpful next step when appropriate

Avoid technical language.

---

# Hierarchy

Prioritize:

- Status
- Message
- Action
- Supporting information

The next action should always be obvious.

---

# AI Decision Rules

Before approving a feedback component, answer:

- Is feedback necessary?
- Is the message understandable?
- Is recovery supported?
- Is accessibility complete?
- Is the component reusable?
- Can developers implement it consistently?

If any answer is negative, redesign the feedback component.

---

# Validation Checklist

□ Purpose documented

□ Anatomy documented

□ Status types documented

□ Message structure documented

□ Hierarchy documented

□ Accessibility reviewed

□ Documentation updated


---

# Feedback Types

## Philosophy

Every feedback component should belong to one reusable component family.

Different feedback types solve different communication problems while sharing the same design language.

Avoid creating unrelated feedback components.

---

# Alert

## Purpose

Alerts communicate important information that requires user attention.

Examples:

- Network unavailable
- Payment failed
- Security warning
- Required action

Alerts should remain visible until dismissed or resolved.

---

# Banner

## Purpose

Banners communicate page-level information.

Examples:

- Maintenance notice
- Cookie consent
- Feature announcement
- System update

Banners should not interrupt workflows.

---

# Toast

## Purpose

Toasts communicate temporary confirmation.

Examples:

- Saved successfully
- Copied
- Sent
- Updated

Toasts should disappear automatically after an appropriate duration.

---

# Snackbar

## Purpose

Snackbars communicate temporary feedback while optionally allowing quick recovery.

Examples:

- Message deleted
- Undo available
- Draft saved

Snackbars may contain one primary action.

---

# Inline Message

## Purpose

Inline messages provide feedback close to related content.

Examples:

- Form validation
- Password strength
- Upload status
- Availability check

Inline feedback should appear immediately.

---

# Progress Bar

## Purpose

Communicate task progress.

Examples:

- Upload
- Download
- Installation
- Processing

Progress should update consistently.

---

# Circular Progress

## Purpose

Communicate ongoing work when completion percentage is optional.

Examples:

- Loading
- Synchronizing
- Connecting

Avoid indefinite indicators for long-running tasks when measurable progress exists.

---

# Loading Indicator

## Purpose

Communicate that work is in progress.

Examples:

- Initial loading
- Refreshing
- Searching

Loading indicators should preserve user confidence.

---

# Status Indicator

## Purpose

Communicate the current state of an object.

Examples:

- Active
- Offline
- Pending
- Completed
- Failed

Status indicators should remain consistent across products.

---

# Notification Badge

## Purpose

Communicate unread or pending items.

Examples:

- Messages
- Alerts
- Tasks
- Updates

Badges should represent meaningful information only.

---

# Validation Message

## Purpose

Help users correct input.

Examples:

- Required field
- Invalid email
- Weak password
- Unsupported format

Validation should explain how to recover.

---

# Feedback Selection Guide

Use:

Alert

For important information.

Banner

For page-wide communication.

Toast

For temporary confirmation.

Snackbar

For temporary feedback with recovery.

Inline Message

For contextual guidance.

Progress Bar

For measurable progress.

Circular Progress

For ongoing work.

Loading Indicator

For waiting states.

Status Indicator

For object status.

Notification Badge

For counts and pending items.

Validation Message

For form feedback.

---

# Feedback Variants

Represent feedback as variants.

Recommended properties:

Type

- Alert
- Banner
- Toast
- Snackbar
- Inline
- Progress
- Circular
- Loading
- Status
- Badge
- Validation

Status

- Success
- Information
- Warning
- Error
- Neutral

Avoid creating duplicate feedback components.

---

# Responsive Behavior

Feedback should adapt across devices.

Desktop

- Alerts
- Toasts
- Banners

Tablet

- Alerts
- Snackbars
- Banners

Mobile

- Snackbars
- Bottom banners
- Inline messages

Feedback should remain readable and accessible.

---

# AI Feedback Selection Engine

Before selecting a feedback pattern, answer:

- Is feedback necessary?
- Does the user need immediate attention?
- Should the message interrupt the workflow?
- Is recovery provided?
- Is accessibility supported?
- Can this remain part of one component family?

If any answer is negative, choose a more appropriate feedback pattern.

---

# Validation Checklist

□ Alert documented

□ Banner documented

□ Toast documented

□ Snackbar documented

□ Inline message documented

□ Progress bar documented

□ Circular progress documented

□ Loading indicator documented

□ Status indicator documented

□ Notification badge documented

□ Validation message documented

□ Variant strategy documented

□ Responsive behavior documented


