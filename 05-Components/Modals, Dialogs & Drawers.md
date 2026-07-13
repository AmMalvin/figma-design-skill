---
title: Modals, Dialogs & Drawers
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
  - ../02-Visual-System/Spacing & Sizing.md
  - ./Component Principles.md
---

# Modals, Dialogs & Drawers

## Purpose

This module teaches the AI how to design scalable, reusable, accessible, and production-ready overlay components.

Overlays temporarily interrupt the current interface to present focused information or actions.

---

# Definition

An overlay is content displayed above the current interface.

Common overlay patterns include:

- Modal
- Dialog
- Drawer
- Bottom Sheet
- Full-screen Overlay

---

# Objectives

After completing this module, the AI should be able to:

- Design reusable overlays
- Reduce unnecessary interruptions
- Improve task completion
- Maintain accessibility
- Support responsive layouts
- Improve developer implementation
- Scale across products

---

# Overlay Philosophy

Every overlay should answer:

- Why is interruption necessary?
- What action should the user take?
- How does the user leave?

Only interrupt users when necessary.

---

# Core Principles

Always:

- Keep overlays focused.
- Limit content.
- Provide clear actions.
- Support keyboard interaction.
- Restore focus after closing.
- Maintain accessibility.

Never:

- Nest multiple modal dialogs.
- Hide dismissal controls.
- Interrupt simple workflows.
- Overload overlays with content.
- Block users unnecessarily.

---

# Why Overlays Exist

Overlays help users:

- Confirm actions
- Complete focused tasks
- View additional information
- Edit records
- Select options
- Resolve important decisions

Use overlays intentionally.

---

# Overlay Anatomy

Every overlay should define:

- Scrim
- Surface
- Header
- Body
- Footer
- Actions
- Close control

Each section should have one responsibility.

---

# Scrim

The scrim separates the overlay from background content.

Requirements:

- Covers the viewport
- Reduces background emphasis
- Maintains accessibility

The scrim should not distract users.

---

# Surface

The surface contains the overlay content.

The surface defines:

- Width
- Height
- Padding
- Border radius
- Elevation
- Background

Surface styling should use design tokens.

---

# Header

The header introduces the overlay.

Typical content:

- Title
- Subtitle
- Optional close button

The purpose should be immediately clear.

---

# Body

The body contains the primary content.

Examples:

- Forms
- Messages
- Details
- Lists
- Settings

Keep body content concise.

---

# Footer

The footer contains actions.

Typical actions:

- Primary
- Secondary
- Cancel
- Destructive

Actions should remain easy to scan.

---

# Overlay Hierarchy

Visual hierarchy should prioritize:

- Title
- Primary content
- Primary action
- Secondary action

Important information should appear first.

---

# AI Decision Rules

Before approving an overlay, answer:

- Is interruption necessary?
- Is the content focused?
- Is dismissal obvious?
- Is accessibility supported?
- Is the overlay reusable?
- Can developers implement it consistently?

If any answer is negative, redesign the overlay.

---

# Validation Checklist

□ Purpose documented

□ Anatomy documented

□ Scrim documented

□ Surface documented

□ Header documented

□ Body documented

□ Footer documented

□ Accessibility reviewed

□ Documentation updated

