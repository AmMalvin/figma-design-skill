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


---

# Overlay Types

## Philosophy

Every overlay should belong to one reusable component family.

Different overlay types solve different interaction problems while sharing the same foundation.

Avoid building unrelated overlay components.

---

# Modal Dialog

## Purpose

Modal dialogs require users to complete or dismiss a focused task before returning to the interface.

Examples:

- Create Project
- Edit Profile
- Sign In
- Settings

Rules:

- Block interaction with the background.
- Keep content focused.
- Provide clear dismissal.

---

# Alert Dialog

## Purpose

Alert dialogs communicate critical information.

Examples:

- Session expired
- Connection lost
- Unsaved changes
- Permission required

Users should immediately understand the message.

---

# Confirmation Dialog

## Purpose

Require confirmation before important actions.

Examples:

- Delete file
- Archive project
- Cancel subscription
- Sign out

The consequence should be obvious.

---

# Side Drawer

## Purpose

Display secondary content without navigating away.

Examples:

- Filters
- Navigation
- Shopping cart
- User details

Drawers should slide from the edge of the screen.

---

# Bottom Sheet

## Purpose

Present contextual actions on mobile devices.

Examples:

- Share
- Sort
- Select option
- Quick actions

Bottom sheets should remain thumb-friendly.

---

# Full-screen Dialog

## Purpose

Support complex tasks that require more space.

Examples:

- Multi-step forms
- Document editing
- Advanced settings

Use only when a standard dialog is insufficient.

---

# Popover

## Purpose

Display contextual information near the triggering element.

Examples:

- Color picker
- Emoji picker
- User preview
- Formatting options

Popovers should remain anchored to their trigger.

---

# Tooltip

## Purpose

Provide brief supporting information.

Examples:

- Button description
- Keyboard shortcut
- Feature explanation

Tooltips should never contain essential information.

---

# Overlay Sizes

Recommended semantic sizes:

- Small
- Medium
- Large
- Extra Large
- Full Screen

Use design tokens for all dimensions.

---

# Overlay Variants

Represent overlay types as variants.

Recommended properties:

Type

- Modal
- Alert
- Confirmation
- Drawer
- Bottom Sheet
- Full Screen
- Popover
- Tooltip

Avoid creating unrelated overlay components.

---

# Dismissal Methods

Supported dismissal methods:

- Close button
- Cancel action
- Escape key
- Outside click when appropriate
- Swipe for mobile sheets

Never trap users without a clear exit.

---

# Responsive Behavior

Desktop

- Modal
- Drawer
- Popover

Tablet

- Modal
- Drawer
- Bottom Sheet

Mobile

- Bottom Sheet
- Full-screen Dialog
- Drawer when appropriate

Choose the overlay that best fits the device.

---

# AI Overlay Selection Engine

Before selecting an overlay, answer:

- Is interruption necessary?
- Is the task short or complex?
- Does the user need background context?
- Is the overlay appropriate for the device?
- Is accessibility supported?
- Can this remain part of one component family?

If any answer is negative, choose a more appropriate overlay.

---

# Validation Checklist

□ Modal dialog documented

□ Alert dialog documented

□ Confirmation dialog documented

□ Side drawer documented

□ Bottom sheet documented

□ Full-screen dialog documented

□ Popover documented

□ Tooltip documented

□ Overlay sizes documented

□ Responsive behavior documented

□ Variant strategy documented