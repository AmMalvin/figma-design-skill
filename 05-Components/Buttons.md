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


---

# Button Sizes

## Philosophy

Button sizes should support different interface densities while remaining consistent across products.

Never create arbitrary button dimensions.

---

# Standard Sizes

Recommended semantic sizes:

- Extra Small
- Small
- Medium
- Large
- Extra Large

Every size should be defined using design tokens.

---

# Height

Each size should have a fixed height.

Example:

Extra Small

28 px

Small

36 px

Medium

44 px

Large

52 px

Extra Large

60 px

Height should remain consistent for every button of the same size.

---

# Width

Buttons may use:

- Intrinsic width
- Fixed width
- Full width

Choose the width based on layout requirements.

Avoid fixed widths when button labels vary significantly.

---

# Padding

Internal padding should scale with button size.

Padding should provide sufficient breathing room around:

- Labels
- Icons
- Loading indicators

Never allow content to touch the button edge.

---

# Corner Radius

Corner radius should reference design tokens.

Examples:

radius.sm

radius.md

radius.lg

Avoid hardcoded radius values.

---

# Labels

Labels should:

- Begin with a verb
- Be concise
- Use sentence case unless brand guidelines differ
- Describe the outcome

Examples:

Save Changes

Create Account

Continue

Download Report

Avoid generic labels.

---

# Icons

Buttons may include:

- Leading icon
- Trailing icon

Icons should reinforce the action.

Do not use decorative icons.

Maintain consistent spacing between icons and labels.

---

# Icon Only Buttons

Icon-only buttons require:

- Accessible name
- Tooltip when appropriate
- Minimum touch target
- Universally recognized icon

Never rely on the icon alone when the action is unclear.

---

# Button States

Every interactive button should define states.

Minimum states:

- Default
- Hover
- Focus
- Pressed
- Disabled

Optional states:

- Loading
- Success
- Error
- Selected
- Active

Each state should communicate a meaningful change.

---

# Default State

The default state communicates availability.

This should be the baseline appearance.

---

# Hover State

Hover indicates that the button is interactive.

Changes may include:

- Background
- Border
- Shadow
- Elevation

Avoid excessive animation.

---

# Focus State

Focus indicates keyboard navigation.

Requirements:

- Clearly visible
- High contrast
- Never rely only on color

Focus indicators should remain visible until focus moves away.

---

# Pressed State

Pressed confirms interaction.

Visual feedback should occur immediately.

Examples:

- Reduced elevation
- Darker background
- Slight scale reduction

Pressed feedback should feel responsive.

---

# Disabled State

Disabled buttons communicate temporary unavailability.

Requirements:

- Reduced emphasis
- No interaction
- Still readable

Whenever possible, explain why the action is unavailable.

---

# Loading State

Loading prevents duplicate actions.

Requirements:

- Show loading indicator
- Preserve button width
- Disable repeated activation
- Restore previous state after completion

Users should understand that processing is underway.

---

# Success State

Success confirms completion.

Examples:

- Check icon
- Success color
- Confirmation animation

Use success states only when they improve clarity.

---

# Error State

Error communicates failure.

Requirements:

- Explain the problem
- Offer recovery
- Preserve accessibility

Do not rely only on color.

---

# State Transitions

Transitions should feel natural.

Recommended characteristics:

- Fast
- Consistent
- Purposeful

Avoid unnecessary motion.

---

# Responsive Behavior

Buttons should adapt across devices.

Maintain:

- Touch target
- Label readability
- Padding
- Alignment

Do not reduce usability on smaller screens.

---

# AI Button Interaction Engine

Before approving a button, answer:

- Is the size appropriate?
- Is spacing consistent?
- Are all interaction states defined?
- Is keyboard focus visible?
- Is loading behavior documented?
- Does the button remain accessible?
- Can this scale across products?

If any answer is negative, redesign the interaction.

---

# Validation Checklist

□ Button sizes documented

□ Heights standardized

□ Width behavior documented

□ Padding defined

□ Radius tokens applied

□ Labels reviewed

□ Icon usage documented

□ Button states completed

□ Focus visibility verified

□ Loading behavior documented

□ Responsive behavior validated


---

# Keyboard Interaction

## Purpose

Buttons should be fully operable using a keyboard.

Minimum requirements:

- Tab moves focus
- Shift + Tab moves focus backward
- Enter activates the button
- Space activates the button when appropriate

Keyboard users should receive the same functionality as pointer users.

---

# Focus Management

Focus should:

- Always remain visible
- Follow logical order
- Never become trapped
- Return predictably after dialogs close

Focus indicators should never be removed.

---

# Touch Interaction

Buttons should support comfortable touch interaction.

Requirements:

- Large touch target
- Adequate spacing
- Easy thumb reach
- Clear feedback

Touch interactions should prevent accidental activation.

---

# Minimum Touch Target

Recommended minimum touch target:

44 × 44 px

Larger touch targets improve usability on touch devices.

---

# Button Groups

Button groups organize related actions.

Examples:

- Yes / No
- Save / Cancel
- Grid / List

Rules:

- Maintain consistent spacing
- Preserve hierarchy
- Keep related actions together

---

# Overflow Behavior

Buttons should adapt gracefully to limited space.

Strategies include:

- Text wrapping when appropriate
- Label truncation only as a last resort
- Responsive resizing
- Moving secondary actions into menus

Avoid clipping button content.

---

# Accessibility Requirements

Every button should support:

- Keyboard navigation
- Screen readers
- Focus visibility
- Sufficient color contrast
- Accessible names
- Meaningful labels

Accessibility is mandatory.

---

# Screen Reader Support

Every button should expose an accessible name.

Examples:

Good:

Save Changes

Delete Project

Download Report

Avoid unnamed icon-only buttons.

---

# Design Token Integration

Buttons should reference design tokens.

Examples:

button.height.md

button.padding.md

button.radius.md

button.primary.background

button.primary.text

button.focus.ring

Avoid hardcoded values.

---

# Motion Guidelines

Motion should reinforce interaction.

Appropriate uses:

- Hover transition
- Press feedback
- Loading animation
- Success confirmation

Animation should remain subtle and purposeful.

---

# Documentation

Every published button should document:

- Purpose
- Anatomy
- Variants
- Properties
- States
- Accessibility
- Usage guidelines
- Do
- Don't
- Code examples

Documentation should remove implementation ambiguity.

---

# Testing

Every button should be tested for:

- Visual consistency
- Accessibility
- Keyboard support
- Touch interaction
- Responsive layouts
- State transitions
- Loading behavior
- Content overflow

Testing should occur before release.

---

# Quality Assurance

Review every button for:

- Correct hierarchy
- Clear labels
- Consistent spacing
- Proper states
- Accessibility
- Token usage
- Responsive behavior
- Documentation

Only approved buttons belong in the library.

---

# Versioning

Track every change.

Document:

- New variants
- Updated behavior
- Bug fixes
- Breaking changes
- Deprecated variants

Maintain a complete version history.

---

# AI Button Review Engine

Before publishing any button, answer:

- Is the action immediately clear?
- Is the hierarchy correct?
- Are all states documented?
- Is accessibility complete?
- Are design tokens used?
- Is keyboard interaction supported?
- Is touch interaction optimized?
- Has testing been completed?
- Can this button be reused across products?

If any answer is negative, revise the button.

---

# Buttons Checklist

Before publishing:

□ Hierarchy documented

□ Variants completed

□ Sizes standardized

□ States documented

□ Labels reviewed

□ Icon usage validated

□ Keyboard support verified

□ Touch targets validated

□ Accessibility completed

□ Design tokens integrated

□ Motion documented

□ Testing completed

□ QA approved

□ Version history updated

□ Documentation completed

---

# Key Takeaways

Buttons guide users through every product.

The AI must:

- Choose the correct button hierarchy.
- Build one reusable button family.
- Use semantic variants and properties.
- Support keyboard and touch interaction.
- Consume design tokens.
- Meet accessibility requirements.
- Keep labels clear and action-oriented.
- Test every interaction state.
- Document every behavior.
- Maintain consistency across all platforms.

Every button should communicate confidence, clarity, and a predictable outcome.