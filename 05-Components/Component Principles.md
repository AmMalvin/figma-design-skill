---
title: Component Principles
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
  - ../01-Foundation/Visual Hierarchy.md
  - ../02-Visual-System/Color Theory.md
  - ../02-Visual-System/Typography.md
  - ../02-Visual-System/Spacing & Sizing.md
  - ../02-Visual-System/Iconography.md
---

# Component Principles

## Purpose

This module teaches the AI how to design reusable, scalable, accessible, and production-ready UI components.

Every component should solve one problem well.

Components are the building blocks of every interface.

---

# Definition

A component is a reusable interface element with defined structure, behavior, appearance, and functionality.

Components should behave consistently regardless of where they are used.

---

# Objectives

After completing this module, the AI should be able to:

- Build reusable components
- Design scalable component libraries
- Improve consistency
- Support accessibility
- Reduce duplication
- Improve maintainability
- Improve developer handoff
- Support future growth

---

# Component Mindset

Never ask:

"Does this component look good?"

Always ask:

- Does it solve one problem?
- Is it reusable?
- Is it accessible?
- Can developers implement it consistently?
- Does it belong in the design system?

---

# Core Principles

Always:

- Build reusable components.
- Keep components focused.
- Design for scalability.
- Maintain accessibility.
- Support consistency.
- Document behavior.

Never:

- Duplicate components.
- Build page-specific components.
- Combine unrelated functionality.
- Hardcode design decisions.
- Ignore usability.

---

# Why Components Exist

Components should:

- Reduce repetition
- Increase consistency
- Accelerate design
- Simplify development
- Improve maintenance
- Improve collaboration

Every component should save time.

---

# Single Responsibility

Every component should perform one primary function.

Examples:

Button

One responsibility:

Trigger an action.

Input

One responsibility:

Collect information.

Badge

One responsibility:

Communicate status.

Avoid combining unrelated responsibilities.

---

# Reusability

Components should work across:

- Pages
- Features
- Products
- Platforms

A reusable component should not depend on one screen.

---

# Consistency

Every instance of the same component should behave identically.

Consistency includes:

- Appearance
- Behavior
- Accessibility
- Interaction
- Documentation

---

# Predictability

Users should know how a component behaves before interacting with it.

Unexpected behavior reduces trust.

---

# Scalability

Every component should support future growth.

Scalability includes:

- Variants
- Themes
- Responsive layouts
- Localization
- Accessibility

Design for tomorrow, not only today.

---

# Composition

Large components should be built from smaller reusable components.

Composition improves:

- Flexibility
- Maintenance
- Reusability

Avoid rebuilding existing functionality.

---

# AI Decision Rules

Before approving any component, answer:

- Does it solve one problem?
- Is it reusable?
- Is it accessible?
- Is behavior predictable?
- Can it scale?
- Will developers implement it consistently?

If any answer is negative, redesign the component.

---

# Validation Checklist

□ Component purpose defined

□ Single responsibility verified

□ Reusability reviewed

□ Accessibility reviewed

□ Scalability validated

□ Documentation updated


---

# Component Anatomy

## Definition

Component anatomy defines the structural parts of a component.

Every component should have a predictable internal structure.

Structure should remain consistent across the entire design system.

---

# Anatomy Principles

Every component should define:

- Container
- Content
- Slots
- Actions
- States
- Properties

Each part should have one clear responsibility.

---

# Container

The container is the outer structure of a component.

The container controls:

- Size
- Layout
- Padding
- Background
- Border
- Elevation

The container should never contain business logic.

---

# Content Area

The content area displays information.

Examples include:

- Text
- Images
- Icons
- Media
- Data
- Lists

Content should remain independent from layout.

---

# Primary Content

Primary content communicates the main purpose.

Examples:

- Button label
- Card title
- Dialog heading
- Input value

Every component should have one primary focus.

---

# Supporting Content

Supporting content adds context.

Examples:

- Description
- Helper text
- Metadata
- Secondary labels
- Badges

Supporting content should never compete with primary content.

---

# Actions

Actions define user interaction.

Examples:

- Button
- Link
- Menu
- Toggle
- Close control

Actions should remain clearly identifiable.

---

# Slots

## Definition

Slots are predefined regions where content or nested components can be inserted.

Slots improve flexibility while preserving component structure.

Examples:

- Leading icon
- Trailing icon
- Header
- Footer
- Media
- Actions

Slots should have documented constraints.

---

# Parent Components

Parent components organize child components.

Responsibilities include:

- Layout
- Spacing
- Alignment
- Relationships

Parents should not duplicate child behavior.

---

# Child Components

Child components perform individual responsibilities.

Examples:

- Avatar
- Badge
- Icon
- Button
- Checkbox

Children should remain reusable outside the parent.

---

# Nested Components

Components may contain other reusable components.

Examples:

Card

- Avatar
- Heading
- Button
- Badge

Navigation

- Logo
- Menu item
- Avatar
- Notification

Composition improves maintainability.

---

# Atomic Design

Build interfaces from progressively larger building blocks.

Levels include:

- Tokens
- Primitive Components
- Composite Components
- Patterns
- Templates
- Screens

Avoid skipping levels without a documented reason.

---

# Component Relationships

Relationships should be explicit.

Examples:

Button belongs to Form.

Avatar belongs to User Profile.

Menu Item belongs to Navigation.

Relationships improve consistency.

---

# Separation of Responsibilities

Visual styling should remain separate from:

- Business logic
- Data
- Navigation
- State management

Components should remain presentation-focused whenever possible.

---

# AI Component Architecture Engine

Before approving component architecture, answer:

- Does every part have one responsibility?
- Are slots clearly defined?
- Can child components be reused?
- Is composition used instead of duplication?
- Is the hierarchy logical?
- Can developers implement this consistently?

If any answer is negative, redesign the component architecture.

---

# Validation Checklist

□ Component anatomy documented

□ Container defined

□ Content areas documented

□ Slots documented

□ Parent-child relationships reviewed

□ Nested components validated

□ Atomic design structure defined

□ Component relationships documented

□ Responsibilities separated

□ Documentation updated