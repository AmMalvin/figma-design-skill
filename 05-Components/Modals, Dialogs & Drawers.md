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


---

# Overlay States

## Philosophy

Every overlay should communicate its current interaction state.

Users should always understand:

- What is happening
- What action is expected
- How to leave

Every overlay should behave consistently.

---

# Default State

The overlay is fully visible and ready for interaction.

Requirements:

- Visible title
- Visible actions
- Background blocked when modal
- Initial focus assigned

---

# Opening Behavior

Opening should feel immediate and predictable.

Requirements:

- Display overlay above content
- Move focus into the overlay
- Prevent interaction with blocked content
- Preserve background state

Avoid unexpected layout shifts.

---

# Closing Behavior

Closing should return users safely to the previous context.

Requirements:

- Restore previous screen
- Restore focus to the triggering element
- Preserve unfinished work when appropriate

Never leave users without orientation.

---

# Focus Trap

Modal overlays should trap keyboard focus.

Requirements:

- Tab cycles within the overlay
- Shift + Tab cycles backward
- Focus never escapes into the background

Focus trapping applies only while the modal is open.

---

# Focus Restoration

After dismissal:

- Return focus to the trigger
- Restore previous keyboard position
- Maintain workflow continuity

Users should never lose their place.

---

# Stacked Overlays

Avoid multiple stacked overlays.

If stacking is unavoidable:

- Clearly establish hierarchy
- Allow predictable dismissal
- Prevent focus conflicts

Prefer replacing an existing overlay instead.

---

# Overlay Actions

Every overlay should define:

- Primary action
- Secondary action
- Cancel action when appropriate
- Destructive action when necessary

Primary actions should remain visually dominant.

---

# Loading State

Loading overlays communicate ongoing work.

Examples:

- Saving
- Uploading
- Processing
- Synchronizing

Preserve layout during loading.

---

# Progress Indicators

Long-running tasks should display progress.

Supported patterns:

- Progress bar
- Circular indicator
- Percentage
- Step indicator

Users should understand whether progress is occurring.

---

# Success State

Success confirms task completion.

Examples:

- Changes saved
- Payment completed
- File uploaded

Provide a clear next step when appropriate.

---

# Error State

Errors should explain:

- What failed
- Why it failed
- How to recover

Avoid technical language.

---

# Empty State

Empty overlays should explain why no content exists.

Examples:

- No results
- No notifications
- No available items

Offer a useful action whenever possible.

---

# Destructive Actions

Destructive actions require additional clarity.

Examples:

- Delete
- Remove
- Reset
- Archive permanently

Use confirmation dialogs when recovery is difficult.

---

# Scroll Behavior

Scrolling should remain predictable.

Requirements:

- Body scrolls when necessary
- Header remains visible when appropriate
- Footer actions remain accessible

Avoid nested scrolling whenever possible.

---

# Responsive Behavior

Desktop

- Centered modal
- Side drawer
- Popover

Tablet

- Large modal
- Drawer
- Bottom sheet

Mobile

- Bottom sheet
- Full-screen dialog

Choose the layout that best supports the task.

---

# Motion

Motion should reinforce understanding.

Examples:

- Fade
- Slide
- Scale
- Drawer transition
- Bottom sheet movement

Motion should communicate spatial relationships.

Avoid decorative animation.

---

# AI Overlay Interaction Engine

Before approving overlay behavior, answer:

- Is focus managed correctly?
- Is dismissal obvious?
- Are loading states defined?
- Can users recover from errors?
- Is responsiveness supported?
- Does motion improve understanding?

If any answer is negative, redesign the interaction.

---

# Validation Checklist

□ Opening behavior documented

□ Closing behavior documented

□ Focus trap documented

□ Focus restoration documented

□ Overlay actions documented

□ Loading state documented

□ Progress indicators documented

□ Success state documented

□ Error state documented

□ Empty state documented

□ Destructive actions documented

□ Scroll behavior documented

□ Responsive behavior documented

□ Motion documented