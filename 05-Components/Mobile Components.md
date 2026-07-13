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

---

# Mobile Component States

## Philosophy

Every mobile component should clearly communicate its current interaction state.

Users should immediately understand:

- What is interactive
- What has changed
- What action is available
- What happens next

Interactions should always improve usability.

---

# Default State

The component is ready for interaction.

Requirements:

- Visible content
- Clear actions
- Readable labels
- Stable layout

Default establishes the baseline appearance.

---

# Pressed State

Touch feedback should occur immediately.

Examples:

- Ripple
- Scale animation
- Opacity change
- Background update

Pressed feedback should confirm successful touch.

---

# Focus State

External keyboards and assistive technologies require focus support.

Requirements:

- Visible focus indicator
- Logical navigation order
- High contrast

Never remove focus indicators.

---

# Disabled State

Disabled components communicate temporary unavailability.

Requirements:

- Reduced emphasis
- Readable labels
- No interaction

Explain unavailable actions whenever appropriate.

---

# Expanded State

Expandable components include:

- Bottom sheets
- Drawers
- Pickers
- Search

Expansion should preserve user context.

---

# Collapsed State

Collapsed components should:

- Remain recognizable
- Preserve primary information
- Clearly indicate expandability

Users should understand additional content exists.

---

# Touch Interaction

Touch interactions should support:

- Tap
- Double tap when appropriate
- Long press
- Drag
- Swipe
- Pinch
- Spread

Avoid unnecessary gesture complexity.

---

# Long Press

Long press should reveal secondary actions.

Examples:

- Context menu
- Reorder mode
- Selection mode

Never hide essential actions behind long press.

---

# Drag and Drop

Drag interactions should communicate:

- Pickup
- Movement
- Drop target
- Completion

Provide continuous visual feedback.

---

# Swipe Thresholds

Swipe actions should activate only after intentional movement.

Requirements:

- Clear activation point
- Visual progress
- Easy cancellation

Avoid accidental activation.

---

# Gesture Conflicts

When multiple gestures exist:

- Prioritize primary interaction.
- Avoid overlapping gestures.
- Maintain predictable behavior.

Users should never wonder which gesture will trigger.

---

# Orientation Changes

Components should adapt to:

- Portrait
- Landscape
- Foldable layouts

Orientation changes should preserve user progress.

---

# Safe Areas

Respect device safe areas.

Examples:

- Status bar
- Camera cutout
- Home indicator
- Rounded corners

Important content should remain accessible.

---

# Offline Behavior

Components should communicate offline status.

Examples:

- Cached content
- Pending uploads
- Retry actions
- Synchronization status

Users should always understand connection status.

---

# Motion

Motion should reinforce interaction.

Examples:

- Bottom sheet transition
- FAB expansion
- Swipe animation
- Pull-to-refresh
- Navigation transition

Motion should communicate change.

Avoid decorative animation.

---

# Responsive Behavior

Phone

- Thumb-first layouts
- Gesture navigation
- Compact spacing

Foldable

- Adaptive layouts
- Multi-pane experiences

Tablet

- Larger touch targets
- Expanded navigation
- Multi-column layouts

Interaction patterns should remain consistent across devices.

---

# AI Mobile Interaction Engine

Before approving interaction behavior, answer:

- Is touch interaction obvious?
- Are gestures predictable?
- Are safe areas respected?
- Is accessibility supported?
- Does motion improve understanding?
- Is responsiveness maintained?

If any answer is negative, redesign the interaction.

---

# Validation Checklist

□ Mobile states documented

□ Pressed state documented

□ Focus state documented

□ Disabled state documented

□ Expanded state documented

□ Collapsed state documented

□ Touch interaction documented

□ Long press documented

□ Drag and drop documented

□ Swipe thresholds documented

□ Gesture conflicts documented

□ Orientation changes documented

□ Safe areas documented

□ Offline behavior documented

□ Motion documented

□ Responsive behavior validated


---

# Keyboard Interaction

## Purpose

Mobile devices increasingly support external keyboards.

Interactive mobile components should provide predictable keyboard navigation.

Minimum requirements:

- Tab moves focus
- Shift + Tab moves focus backward
- Arrow keys navigate when appropriate
- Enter activates focused controls
- Space activates supported controls
- Escape dismisses temporary surfaces

Keyboard behavior should remain consistent.

---

# Focus Management

Focus should:

- Always remain visible
- Follow logical navigation
- Move into temporary surfaces
- Return after dismissal

Never lose keyboard focus.

---

# Screen Reader Support

Every mobile component should expose:

- Component role
- Accessible name
- Current state
- Available actions
- Progress when applicable

Users should understand interactions without relying on vision.

---

# Platform Accessibility

Support platform accessibility features.

Examples:

- Dynamic text
- Screen readers
- High contrast
- Reduced motion
- Display zoom

Components should adapt without breaking layouts.

---

# Touch Target Standards

Interactive controls should provide comfortable touch targets.

Requirements:

- Adequate size
- Adequate spacing
- Easy reach
- Clear feedback

Avoid crowded controls.

---

# Haptic Guidance

Use haptic feedback for meaningful events.

Examples:

- Successful action
- Selection
- Confirmation
- Warning
- Error

Avoid excessive haptic feedback.

---

# Safe Area Compliance

Every mobile layout should respect:

- Status bar
- Camera cutout
- Home indicator
- Rounded corners
- Foldable hinges

Critical content should remain accessible.

---

# Responsive Adaptation

Phone

- Thumb-friendly layouts
- Compact navigation
- Gesture-first interaction

Foldable

- Multi-pane layouts
- Adaptive spacing
- Continuous interactions

Tablet

- Expanded navigation
- Larger layouts
- Multi-column experiences

Components should adapt without changing interaction patterns.

---

# Design Token Integration

Mobile components should reference design tokens.

Examples:

mobile.spacing

mobile.radius

mobile.shadow

mobile.touch.target

mobile.safe.area

mobile.focus.ring

mobile.elevation

mobile.motion.duration

Avoid hardcoded values.

---

# Motion Guidelines

Motion should reinforce interaction.

Examples:

- Bottom sheet transition
- FAB transformation
- Drawer animation
- Gesture transition
- Pull-to-refresh

Motion should communicate change.

Avoid decorative animation.

---

# Documentation

Every mobile component should document:

- Purpose
- Anatomy
- Variants
- States
- Accessibility
- Platform behavior
- Responsive behavior
- Usage guidelines
- Do
- Don't
- Examples

Documentation should eliminate implementation ambiguity.

---

# Testing

Every mobile component should be tested for:

- Accessibility
- Keyboard support
- Screen reader compatibility
- Gesture interaction
- Safe area compliance
- Responsive layouts
- Motion
- Performance

Testing should occur before release.

---

# Quality Assurance

Review every mobile component for:

- Accessibility
- Platform consistency
- Responsive behavior
- Design token usage
- Documentation
- Performance

Only approved components belong in the design system.

---

# Versioning

Track changes for:

- New mobile patterns
- Accessibility improvements
- Motion updates
- Bug fixes
- Breaking changes

Maintain complete version history.

---

# Governance

Mobile component updates should include:

- UX review
- Accessibility review
- Engineering review
- QA approval
- Documentation update

Governance maintains consistency.

---

# AI Mobile Review Engine

Before publishing any mobile component, answer:

- Is the interaction touch friendly?
- Is accessibility complete?
- Are platform conventions respected?
- Are design tokens used?
- Is keyboard support complete?
- Has testing been completed?
- Does this scale across products?
- Is interaction predictable?

If any answer is negative, revise the component.

---

# Mobile Components Checklist

Before publishing:

□ Anatomy documented

□ Variants completed

□ States documented

□ Keyboard interaction verified

□ Focus management documented

□ Screen reader support completed

□ Platform accessibility documented

□ Safe areas validated

□ Design tokens integrated

□ Motion documented

□ Testing completed

□ QA approved

□ Version history updated

□ Documentation completed

---

# Key Takeaways

Mobile components support touch-first experiences across phones, tablets, and foldable devices.

The AI must:

- Choose the correct mobile pattern.
- Prioritize touch interaction.
- Respect platform conventions.
- Support keyboard navigation.
- Support screen readers.
- Use design tokens.
- Keep motion meaningful.
- Test every interaction.
- Document every behavior.

Every mobile component should improve usability, accessibility, consistency, and long-term maintainability.