---
title: Buttons
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
  - ../02-Visual-System/Iconography.md
  - ./Component Principles.md
---

# Buttons

## Purpose

This module teaches the AI how to design scalable, reusable, accessible, and production-ready buttons.

Buttons trigger actions.

Every button should communicate a clear outcome.

---

# Definition

A button is an interactive component that allows users to perform an action.

Buttons should never be used for navigation unless they intentionally initiate navigation.

---

# Objectives

After completing this module, the AI should be able to:

- Design reusable buttons
- Apply hierarchy correctly
- Build accessible interactions
- Maintain consistency
- Support responsive layouts
- Improve usability
- Improve developer implementation
- Scale across products

---

# Button Philosophy

Buttons exist to help users complete tasks.

Every button should answer:

- What action will happen?
- Why should the user click?
- Is this the primary action?

Buttons should reduce hesitation.

---

# Core Principles

Always:

- Use clear action labels.
- Maintain hierarchy.
- Support accessibility.
- Keep interactions predictable.
- Design reusable buttons.
- Use semantic variants.

Never:

- Use vague labels.
- Create unnecessary button styles.
- Mix hierarchy randomly.
- Hide important actions.
- Duplicate existing buttons.

---

# Why Buttons Exist

Buttons should:

- Trigger actions
- Confirm choices
- Submit information
- Start workflows
- Continue user journeys
- Complete tasks

Buttons should never confuse users.

---

# Button Anatomy

Every button should define:

- Container
- Label
- Optional leading icon
- Optional trailing icon
- Optional loading indicator
- Focus indicator
- Touch target

Each part should have one responsibility.

---

# Container

The container controls:

- Background
- Border
- Padding
- Radius
- Elevation
- Width
- Height

The container should consume design tokens.

---

# Label

The label communicates the action.

Good examples:

Save

Continue

Create Account

Delete Project

Poor examples:

Click Here

Submit

Okay

Button labels should begin with a verb whenever possible.

---

# Button Hierarchy

Every interface should establish a clear hierarchy.

Levels include:

- Primary
- Secondary
- Tertiary
- Destructive

Only one primary button should appear within the same decision area unless a documented exception exists.

---

# Primary Buttons

Primary buttons represent the most important action.

Examples:

- Save
- Continue
- Purchase
- Sign In

Primary buttons should receive the greatest visual emphasis.

---

# Secondary Buttons

Secondary buttons support the primary action.

Examples:

- Cancel
- Back
- Learn More

Secondary buttons should remain visually distinct from primary buttons.

---

# Tertiary Buttons

Tertiary buttons represent low-emphasis actions.

Examples:

- View Details
- Skip
- More Options

They should avoid competing with primary actions.

---

# AI Decision Rules

Before approving any button, answer:

- Is the action clear?
- Is the hierarchy correct?
- Is accessibility supported?
- Is the button reusable?
- Can developers implement it consistently?
- Does it follow design tokens?

If any answer is negative, redesign the button.

---

# Validation Checklist

□ Purpose documented

□ Anatomy defined

□ Hierarchy documented

□ Labels reviewed

□ Accessibility reviewed

□ Documentation updated


---

# Button Types

## Philosophy

Every button should belong to one reusable component family.

Different button types represent different levels of emphasis.

Do not create separate button components when a variant is sufficient.

---

# Primary Button

## Purpose

Primary buttons represent the highest priority action.

Examples:

- Save
- Continue
- Sign In
- Purchase
- Submit

Rules:

- One primary action per decision area
- Highest visual emphasis
- Strongest contrast
- Easy to discover

Avoid multiple primary buttons competing for attention.

---

# Secondary Button

## Purpose

Secondary buttons support the primary action.

Examples:

- Cancel
- Back
- Learn More
- View Details

Rules:

- Lower emphasis than Primary
- Clearly distinguishable
- Should not compete visually with Primary

---

# Tertiary Button

## Purpose

Tertiary buttons represent optional actions.

Examples:

- Skip
- Maybe Later
- More
- Details

Rules:

- Low emphasis
- Minimal visual weight
- Still clearly interactive

---

# Ghost Button

Ghost buttons have little or no background.

Recommended for:

- Toolbars
- Cards
- Inline actions
- Secondary interfaces

Ghost buttons should remain discoverable through hover and focus states.

---

# Link Button

Link buttons appear similar to hyperlinks.

Use for:

- Secondary navigation
- Inline actions
- Read More
- Documentation

Do not use link buttons for destructive actions.

---

# Icon Button

## Purpose

Icon buttons communicate actions using icons.

Examples:

- Search
- Settings
- Close
- Favorite
- Share

Rules:

- Use universally recognized icons
- Maintain minimum touch targets
- Provide accessible labels
- Include tooltips where meaning is unclear

Icons should never replace text when the action is ambiguous.

---

# Floating Action Button

Floating Action Buttons represent one high-priority action.

Examples:

- Create
- Compose
- Add

Rules:

- One FAB per screen
- Fixed position
- High visibility

Avoid multiple FABs on the same screen.

---

# Split Button

Split buttons combine:

- Primary action
- Secondary menu

Use when one action is common but alternatives exist.

Example:

Export

↓

Export PDF

Export PNG

Export CSV

The primary action should remain immediately accessible.

---

# Segmented Button

Segmented buttons allow users to choose one option from a small group.

Examples:

- Grid / List
- Monthly / Yearly
- Light / Dark

Rules:

- Clearly indicate the selected option
- Keep options mutually exclusive
- Maintain equal visual weight

---

# Toggle Button

Toggle buttons switch between two persistent states.

Examples:

- Bold
- Italic
- Favorite
- Mute

Rules:

- Clearly display On and Off states
- Preserve state after interaction
- Do not use for temporary actions

---

# Loading Button

Loading buttons communicate that an action is in progress.

Requirements:

- Replace or accompany the label with a loading indicator
- Prevent duplicate submissions
- Preserve button dimensions
- Restore the previous state after completion

Users should understand that processing is underway.

---

# Destructive Button

Destructive buttons perform irreversible actions.

Examples:

- Delete
- Remove
- Reset
- Archive Permanently

Rules:

- Use destructive styling
- Require confirmation for high-risk actions
- Separate from primary actions
- Avoid accidental activation

---

# Disabled Button

Disabled buttons indicate that an action is unavailable.

Rules:

- Remain visible
- Clearly appear inactive
- Never be the only explanation

Whenever possible, explain why the action is unavailable.

---

# Button Selection Guide

Use:

Primary

For the main task.

Secondary

For supporting tasks.

Tertiary

For optional actions.

Ghost

For low-emphasis interface actions.

Link

For inline navigation.

Icon

For compact actions.

FAB

For one dominant screen action.

Split

For primary action with alternatives.

Segmented

For mutually exclusive choices.

Toggle

For persistent states.

Loading

During processing.

Destructive

For irreversible actions.

---

# Variant Strategy

Represent button types as variants.

Recommended properties:

Type

- Primary
- Secondary
- Tertiary
- Ghost
- Link
- Icon
- FAB
- Split
- Segmented
- Toggle
- Loading
- Destructive

Avoid separate component files for each button type.

---

# AI Button Hierarchy Engine

Before approving a button type, answer:

- Is this the correct hierarchy?
- Is another button type more appropriate?
- Is the action reversible?
- Is accessibility maintained?
- Is the button reusable?
- Does this remain part of one component family?

If any answer is negative, redesign the button.

---

# Validation Checklist

□ Primary button documented

□ Secondary button documented

□ Tertiary button documented

□ Ghost button documented

□ Link button documented

□ Icon button documented

□ Floating Action Button documented

□ Split button documented

□ Segmented button documented

□ Toggle button documented

□ Loading button documented

□ Destructive button documented

□ Variant strategy documented