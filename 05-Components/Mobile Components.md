---
title: Mobile Components
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
  - ../01-Foundation/Responsive Design.md
  - ../02-Visual-System/Typography.md
  - ../02-Visual-System/Iconography.md
  - ../02-Visual-System/Spacing & Sizing.md
  - ./Component Principles.md
---

# Mobile Components

## Purpose

This module teaches the AI how to design scalable, reusable, accessible, and production-ready mobile components.

Mobile components should prioritize touch interaction, gestures, responsiveness, and platform conventions.

---

# Definition

Mobile components support interactions primarily designed for phones and touch devices.

Examples include:

- Bottom sheets
- Floating action buttons
- Pull-to-refresh
- Swipe actions
- Gesture controls
- Mobile navigation
- Touch feedback

Every component should optimize the mobile experience.

---

# Objectives

After completing this module, the AI should be able to:

- Design reusable mobile components
- Support touch interactions
- Follow platform conventions
- Improve accessibility
- Improve developer implementation
- Scale across products

---

# Mobile Philosophy

Every mobile component should answer:

- Is this optimized for touch?
- Does interaction feel natural?
- Does it reduce user effort?

Mobile interactions should remain fast and predictable.

---

# Core Principles

Always:

- Prioritize touch.
- Support gestures.
- Keep targets easy to reach.
- Maintain accessibility.
- Design reusable components.
- Reduce interaction steps.

Never:

- Depend on hover.
- Hide critical actions.
- Create unreachable controls.
- Ignore platform conventions.
- Use unnecessarily complex gestures.

---

# Why Mobile Components Exist

Mobile components help users:

- Navigate quickly
- Complete tasks
- Perform gestures
- Interact with content
- Reach important actions
- Use applications comfortably with one hand

Every interaction should reduce effort.

---

# Component Anatomy

Every mobile component should define:

- Container
- Primary action
- Secondary action
- Gesture area
- Status indicator
- Optional icon
- Optional label

Each element should have one responsibility.

---

# Touch Targets

Interactive controls should provide touch targets large enough for reliable selection.

Prioritize comfortable spacing between adjacent controls.

---

# Hierarchy

Prioritize:

- Primary action
- Navigation
- Supporting actions
- Secondary information

Hierarchy should support quick scanning.

---

# AI Decision Rules

Before approving a mobile component, answer:

- Is the interaction touch friendly?
- Is accessibility supported?
- Is responsiveness supported?
- Is the component reusable?
- Does it follow platform expectations?
- Can developers implement it consistently?

If any answer is negative, redesign the component.

---

# Validation Checklist

□ Purpose documented

□ Anatomy documented

□ Touch targets documented

□ Hierarchy documented

□ Accessibility reviewed

□ Responsive behavior reviewed

□ Documentation updated

---

# Mobile Component Types

## Philosophy

Every mobile component should belong to one reusable component family.

Different mobile patterns solve different interaction problems while sharing the same design language.

Avoid duplicate mobile components.

---

# Bottom Sheet

## Purpose

Present additional content without leaving the current screen.

Examples:

- Filters
- Share options
- Payment methods
- Settings

Bottom sheets should remain easy to dismiss.

---

# Floating Action Button

## Purpose

Highlight the primary action on a screen.

Examples:

- Create
- Add
- Compose
- Scan

Only one primary floating action button should appear on a screen.

---

# Pull-to-Refresh

## Purpose

Refresh content using a downward gesture.

Examples:

- Feed
- Inbox
- Dashboard
- Notifications

Always provide visible refresh feedback.

---

# Swipe Actions

## Purpose

Reveal contextual actions.

Examples:

- Delete
- Archive
- Pin
- Mark as read

Primary actions should remain discoverable without requiring swipe.

---

# Gesture Navigation

## Purpose

Support natural touch navigation.

Examples:

- Swipe back
- Swipe forward
- Edge gestures
- Drag gestures

Gestures should never replace essential visible controls.

---

# Mobile Search

## Purpose

Help users quickly locate content.

Examples:

- Products
- Contacts
- Messages
- Documents

Search should remain easy to access.

---

# Mobile Tabs

## Purpose

Switch between related views.

Examples:

- Home
- Activity
- Profile
- Settings

Tabs should represent closely related content.

---

# Mobile Drawer

## Purpose

Provide secondary navigation or actions.

Examples:

- Navigation menu
- Filters
- Account settings

Drawers should not interrupt primary tasks.

---

# Mobile Picker

## Purpose

Allow users to select values.

Examples:

- Date
- Time
- Country
- Currency

Pickers should minimize typing.

---

# Action Sheet

## Purpose

Present a focused list of actions.

Examples:

- Share
- Save
- Delete
- Rename

Destructive actions should remain visually distinct.

---

# Touch Feedback

## Purpose

Confirm user interaction.

Examples:

- Ripple
- Highlight
- Scale animation
- Opacity change

Feedback should occur immediately after touch.

---

# Haptic Feedback

## Purpose

Provide physical confirmation for important actions.

Examples:

- Successful payment
- Selection
- Long press
- Error notification

Use haptics sparingly.

---

# Mobile Selection Guide

Use:

Bottom Sheet

For temporary content.

Floating Action Button

For the primary screen action.

Pull-to-Refresh

For refreshing dynamic content.

Swipe Actions

For contextual actions.

Gesture Navigation

For natural navigation.

Mobile Search

For content discovery.

Mobile Tabs

For related views.

Mobile Drawer

For secondary navigation.

Mobile Picker

For structured input.

Action Sheet

For grouped actions.

Touch Feedback

For interaction confirmation.

Haptic Feedback

For tactile confirmation.

---

# Mobile Variants

Represent mobile components as variants.

Recommended properties:

Type

- Bottom Sheet
- FAB
- Pull Refresh
- Swipe
- Gesture
- Search
- Tabs
- Drawer
- Picker
- Action Sheet

State

- Default
- Hover when applicable
- Focus
- Pressed
- Expanded
- Collapsed
- Disabled

Size

- Small
- Medium
- Large

Avoid duplicate component sets.

---

# Responsive Behavior

Phone

- Full mobile patterns
- Thumb-friendly controls

Foldable

- Adaptive layouts
- Multi-pane views

Tablet

- Expanded navigation
- Larger touch targets
- Multi-column layouts

Components should adapt without changing interaction patterns.

---

# AI Mobile Selection Engine

Before selecting a mobile component, answer:

- Is this optimized for touch?
- Is the interaction obvious?
- Does it follow platform conventions?
- Is accessibility supported?
- Is responsiveness supported?
- Can this remain part of one reusable component family?

If any answer is negative, choose a more appropriate mobile pattern.

---

# Validation Checklist

□ Bottom sheet documented

□ Floating action button documented

□ Pull-to-refresh documented

□ Swipe actions documented

□ Gesture navigation documented

□ Mobile search documented

□ Mobile tabs documented

□ Mobile drawer documented

□ Mobile picker documented

□ Action sheet documented

□ Touch feedback documented

□ Haptic feedback documented

□ Variant strategy documented

□ Responsive behavior documented

