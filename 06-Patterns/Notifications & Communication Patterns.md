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