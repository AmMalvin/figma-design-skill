---
title: Notifications & Communication Patterns
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
  - ../05-Components/Feedback Components.md
  - ../05-Components/Buttons.md
  - ../05-Components/Badges.md
  - ../05-Components/Navigation Components.md
  - ../05-Components/Modals, Dialogs & Drawers.md
  - ../05-Components/Data Display.md
---

# Notifications & Communication Patterns

## Purpose

This module teaches the AI how to design communication systems that are timely, useful, accessible, and scalable.

Communication should inform users without overwhelming them.

---

# Definition

Notifications communicate important events.

Communication patterns include every workflow used to inform, remind, warn, confirm, or engage users throughout the product lifecycle.

---

# Objectives

After completing this module, the AI should be able to:

- Design notification systems
- Select appropriate communication channels
- Reduce notification fatigue
- Improve message relevance
- Support accessibility
- Scale communication across products

---

# Communication Philosophy

Every communication workflow should answer:

- What happened?
- Why is the user being informed?
- Is action required?
- Which channel is appropriate?
- When should the message be delivered?

Communication should respect user attention.

---

# Core Principles

Always:

- Deliver relevant information.
- Choose the appropriate communication channel.
- Respect user preferences.
- Explain required actions.
- Reuse existing components.
- Support accessibility.

Never:

- Send unnecessary notifications.
- Interrupt users without reason.
- Duplicate notifications across channels unnecessarily.
- Hide important communication.
- Overwhelm users.

---

# Communication Lifecycle

Every workflow should define:

- Event
- Trigger
- Channel selection
- Delivery
- User interaction
- Completion

Each stage should remain predictable.

---

# Communication Types

Common communication models include:

- In-app notifications
- Push notifications
- Email
- SMS
- System alerts
- Announcements
- Reminders
- Activity feeds

Choose the communication type based on urgency and user context.

---

# Pattern Composition

Communication patterns should reuse existing components.

Examples:

- Alerts
- Badges
- Banners
- Cards
- Dialogs
- Toasts
- Buttons
- Lists

Avoid creating communication-specific components when reusable components already exist.

---

# Success Metrics

Measure communication using:

- Delivery rate
- Open rate
- Read rate
- Action completion rate
- Notification dismissal rate
- Notification opt-out rate

Measure successful communication rather than message volume.

---

# AI Decision Rules

Before approving a communication workflow, answer:

- Is the communication valuable?
- Is the correct channel selected?
- Is accessibility supported?
- Does it reuse existing components?
- Is the timing appropriate?
- Can developers implement this consistently?

If any answer is negative, redesign the workflow.

---

# Validation Checklist

□ Purpose documented

□ Communication lifecycle documented

□ Communication types documented

□ Component composition documented

□ Success metrics documented

□ Accessibility reviewed

□ Documentation updated


---

# Notification Channels

## Philosophy

Every notification should communicate useful information through the appropriate channel.

Users should always understand:

- What happened
- Why they are being notified
- Whether action is required
- Where to find more information

Notifications should respect user attention.

---

# In-App Notifications

## Purpose

Inform users while they are actively using the product.

Requirements:

- Immediate visibility
- Non-blocking presentation
- Clear action when required
- Easy dismissal

In-app notifications should support ongoing work.

---

# Toast Notifications

## Purpose

Provide temporary feedback after user actions.

Examples:

- Item saved
- Changes published
- File uploaded
- Settings updated

Toasts should disappear automatically unless action is required.

---

# Push Notifications

## Purpose

Reach users outside the application.

Requirements:

- User permission
- Relevant timing
- Concise content
- Direct deep link
- Respect notification settings

Push notifications should only be used for valuable events.

---

# Email Notifications

## Purpose

Deliver information that users may review later.

Examples:

- Account activity
- Reports
- Security alerts
- Billing updates
- Collaboration events

Emails should remain readable and actionable.

---

# SMS Notifications

## Purpose

Deliver urgent information.

Examples:

- Verification codes
- Security alerts
- Critical account updates

SMS should only be used for high-priority communication.

---

# Browser Notifications

## Purpose

Notify users while using supported browsers.

Requirements:

- Explicit permission
- Relevant timing
- Clear destination
- Easy dismissal

Avoid unnecessary browser notifications.

---

# Notification Center

## Purpose

Provide a persistent history of notifications.

Requirements:

- Read and unread states
- Chronological ordering
- Filtering
- Bulk actions
- Search when appropriate

Users should always be able to review missed notifications.

---

# Notification Badges

## Purpose

Indicate unread activity.

Requirements:

- Accurate count
- Automatic updates
- Clear reset behavior
- Accessible labels

Badges should communicate status without distracting users.

---

# Announcements

## Purpose

Communicate important product updates.

Examples:

- New features
- Scheduled maintenance
- Policy updates
- Service improvements

Announcements should remain dismissible unless legally required.

---

# System Alerts

## Purpose

Communicate urgent system events.

Examples:

- Service outage
- Payment failure
- Security issue
- Data synchronization failure

System alerts should clearly explain the impact and required action.

---

# Reminders

## Purpose

Help users complete unfinished tasks.

Examples:

- Upcoming deadline
- Incomplete profile
- Pending approval
- Expiring subscription

Reminders should encourage action without becoming repetitive.

---

# Communication Selection Guide

Use:

In-App Notifications

For active users.

Toast Notifications

For immediate task feedback.

Push Notifications

For timely external updates.

Email Notifications

For important non-urgent communication.

SMS Notifications

For critical and time-sensitive events.

Browser Notifications

For desktop engagement.

Notification Center

For persistent notification history.

Notification Badges

For unread status.

Announcements

For product-wide communication.

System Alerts

For urgent issues.

Reminders

For unfinished tasks.

---

# Workflow Variants

Represent communication channels as reusable patterns.

Recommended properties:

Workflow

- In-App
- Toast
- Push
- Email
- SMS
- Browser
- Announcement
- Reminder

State

- Pending
- Delivered
- Read
- Unread
- Dismissed
- Expired

Platform

- Web
- Mobile
- Desktop

Avoid duplicate communication workflows.

---

# Responsive Behavior

Desktop

- Persistent notification center
- Rich notification previews
- Multi-column inbox

Tablet

- Adaptive notification layouts
- Touch-friendly interactions

Mobile

- Compact notifications
- Native push integration
- Bottom sheet notification center

Communication behavior should remain consistent across platforms.

---

# AI Communication Selection Engine

Before selecting a communication channel, answer:

- Is this the correct channel?
- Is the message valuable?
- Is accessibility supported?
- Does this reuse existing components?
- Is the timing appropriate?
- Can this scale across products?

If any answer is negative, redesign the workflow.

---

# Validation Checklist

□ In-app notifications documented

□ Toast notifications documented

□ Push notifications documented

□ Email notifications documented

□ SMS notifications documented

□ Browser notifications documented

□ Notification center documented

□ Notification badges documented

□ Announcements documented

□ System alerts documented

□ Reminders documented

□ Responsive behavior documented