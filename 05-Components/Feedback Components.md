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


---

# Feedback States

## Philosophy

Every feedback component should clearly communicate its current state.

Users should immediately understand:

- What happened
- What is happening
- What they should do next

Every feedback pattern should behave consistently.

---

# Default State

The feedback component is visible and ready for interaction.

Requirements:

- Clear message
- Appropriate status
- Visible actions when applicable

---

# Dismissible Feedback

Some feedback should allow manual dismissal.

Supported methods:

- Close button
- Swipe on mobile
- Keyboard dismissal when appropriate

Users should remain in control.

---

# Auto-dismiss Behavior

Temporary feedback should disappear automatically.

Examples:

- Toast
- Snackbar

Requirements:

- Enough time to read
- Pause on interaction when appropriate
- Never disappear before users understand the message

---

# Persistent Feedback

Persistent feedback remains visible until resolved.

Examples:

- Security warning
- Billing issue
- Failed synchronization

Persistent messages should remain actionable.

---

# Success State

Success confirms completed actions.

Examples:

- Changes saved
- Profile updated
- Payment completed

Success should reinforce confidence.

---

# Information State

Information provides additional context.

Examples:

- Feature available
- Scheduled maintenance
- Tips

Information should not interrupt workflows.

---

# Warning State

Warnings communicate potential problems.

Examples:

- Low storage
- Unsaved changes
- Subscription expiring

Warnings should encourage preventive action.

---

# Error State

Errors communicate failures.

Every error should explain:

- What happened
- Why it happened when known
- How to recover

Avoid technical language.

---

# Recovery Actions

Errors should provide recovery.

Examples:

- Retry
- Edit
- Contact support
- Undo
- Refresh

Recovery should remain obvious.

---

# Loading State

Loading feedback communicates ongoing work.

Requirements:

- Preserve layout
- Prevent unnecessary movement
- Clearly indicate progress

Users should never wonder whether the system is working.

---

# Skeleton Loading

Skeletons improve perceived performance.

Requirements:

- Match the final layout
- Preserve spacing
- Minimize layout shifts

Replace skeletons immediately after content loads.

---

# Empty State

Empty states explain why content is unavailable.

Examples:

- No notifications
- No search results
- No messages
- No activity

Provide a useful next step whenever possible.

---

# Hover State

Hover should indicate interaction when applicable.

Examples:

- Dismiss button
- Action button
- Retry button

Avoid unnecessary hover effects.

---

# Focus State

Focus supports keyboard users.

Requirements:

- High visibility
- Consistent appearance
- High contrast

Never remove focus indicators.

---

# Disabled State

Disabled actions communicate temporary unavailability.

Requirements:

- Clearly inactive
- Still readable
- Explain why when appropriate

Avoid confusing disabled and loading states.

---

# Motion

Motion should reinforce understanding.

Examples:

- Toast entrance
- Banner expansion
- Progress updates
- Snackbar dismissal

Motion should communicate state changes.

Avoid decorative animation.

---

# Responsive Behavior

Desktop

- Toast
- Banner
- Alert

Tablet

- Snackbar
- Banner
- Alert

Mobile

- Snackbar
- Bottom banner
- Inline feedback

Feedback should remain readable across all devices.

---

# AI Feedback Interaction Engine

Before approving feedback behavior, answer:

- Is the message clear?
- Is timing appropriate?
- Is dismissal predictable?
- Is recovery available?
- Is accessibility supported?
- Does motion improve understanding?

If any answer is negative, redesign the interaction.

---

# Validation Checklist

□ Feedback states documented

□ Dismiss behavior documented

□ Auto-dismiss documented

□ Persistent feedback documented

□ Success state documented

□ Information state documented

□ Warning state documented

□ Error state documented

□ Recovery actions documented

□ Loading state documented

□ Skeleton loading documented

□ Empty state documented

□ Hover state completed

□ Focus state completed

□ Disabled state documented

□ Motion documented

□ Responsive behavior validated


---

# Keyboard Interaction

## Purpose

Every interactive feedback component should be fully operable using a keyboard.

Minimum requirements:

- Tab moves focus
- Shift + Tab moves focus backward
- Enter activates actions
- Space activates controls when appropriate
- Escape dismisses temporary feedback when supported

Keyboard interaction should remain predictable.

---

# Focus Management

Focus should:

- Remain visible
- Follow logical order
- Move to actionable feedback when appropriate
- Return naturally after dismissal

Never remove focus indicators.

---

# Screen Reader Support

Feedback should be announced appropriately.

Support:

- Status updates
- Validation messages
- Progress changes
- Error messages
- Success confirmations

Users should understand feedback without relying on visual cues.

---

# Live Regions

Dynamic feedback should use appropriate live announcements.

Recommended behavior:

- Success messages use polite announcements.
- Critical errors use assertive announcements only when immediate attention is required.
- Progress updates avoid excessive announcements.

Avoid repeatedly announcing identical information.

---

# Accessible Status Communication

Status should never rely only on color.

Combine:

- Icon
- Text
- Label
- Visual styling

Every status should remain understandable.

---

# Color Accessibility

Every feedback component should:

- Meet contrast requirements
- Remain distinguishable in grayscale
- Support users with color vision deficiencies

Status should remain identifiable without color.

---

# Responsive Adaptation

Desktop

- Toasts
- Alerts
- Banners

Tablet

- Snackbars
- Alerts
- Inline feedback

Mobile

- Snackbars
- Bottom banners
- Inline validation

Feedback should remain readable across screen sizes.

---

# Design Token Integration

Feedback components should reference design tokens.

Examples:

feedback.success.background

feedback.warning.background

feedback.error.background

feedback.info.background

feedback.padding

feedback.radius

feedback.icon.size

feedback.focus.ring

Avoid hardcoded values.

---

# Motion Guidelines

Motion should communicate state changes.

Examples:

- Toast entrance
- Snackbar exit
- Progress updates
- Banner expansion

Motion should improve understanding.

Avoid decorative animation.

---

# Documentation

Every feedback component should document:

- Purpose
- Anatomy
- Variants
- States
- Accessibility
- Responsive behavior
- Usage guidelines
- Do
- Don't
- Examples

Documentation should remove implementation ambiguity.

---

# Testing

Every feedback component should be tested for:

- Accessibility
- Keyboard interaction
- Screen readers
- Responsive layouts
- Status communication
- Timing
- Motion
- Performance

Testing should occur before release.

---

# Quality Assurance

Review every feedback component for:

- Clarity
- Accessibility
- Consistency
- Responsive behavior
- Design token usage
- Documentation
- Performance

Only approved feedback components belong in the design system.

---

# Versioning

Track changes for:

- New feedback patterns
- Accessibility improvements
- Motion updates
- Bug fixes
- Breaking changes

Maintain complete version history.

---

# Governance

Feedback updates should include:

- UX review
- Accessibility review
- Engineering review
- QA approval
- Documentation update

Governance maintains long-term consistency.

---

# AI Feedback Review Engine

Before publishing any feedback component, answer:

- Is the message understandable?
- Is the correct feedback pattern used?
- Is recovery provided when necessary?
- Is accessibility complete?
- Are design tokens used?
- Has testing been completed?
- Does this scale across products?
- Is timing appropriate?

If any answer is negative, revise the component.

---

# Feedback Components Checklist

Before publishing:

□ Feedback anatomy documented

□ Variants completed

□ States documented

□ Keyboard interaction verified

□ Screen reader support completed

□ Live regions documented

□ Responsive behavior validated

□ Design tokens integrated

□ Motion documented

□ Testing completed

□ QA approved

□ Version history updated

□ Documentation completed

---

# Key Takeaways

Feedback communicates system status, progress, validation, and outcomes.

The AI must:

- Choose the correct feedback pattern.
- Communicate clearly.
- Provide recovery when needed.
- Support keyboard and screen readers.
- Avoid relying only on color.
- Use design tokens.
- Keep motion meaningful.
- Test every interaction.
- Document every behavior.
- Govern changes through structured review.

Every feedback component should improve clarity, accessibility, confidence, and long-term maintainability.