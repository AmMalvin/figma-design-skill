---
title: Layout Systems
version: 1.0.0
status: Stable
owner: Design System Skill
category: Foundation
priority: Critical
last_updated: 2026-07-12

inherits:
  - ../00-Core/Universal Design Principles.md
  - ../01-Foundation/Systems Thinking.md
  - ../01-Foundation/Product Thinking.md
  - ../01-Foundation/Human-Centered Design.md
  - ../01-Foundation/Design Thinking.md
  - ../01-Foundation/Cognitive Psychology.md
  - ../01-Foundation/Mental Models.md
  - ../01-Foundation/Interaction Design.md
  - ../01-Foundation/Information Architecture.md
  - ../01-Foundation/Visual Hierarchy.md
---

# Layout Systems

## Purpose

This module teaches the AI how to create scalable, responsive, production-ready layouts that work across web, mobile, tablet, desktop, and enterprise applications.

Every layout should support usability, accessibility, consistency, responsiveness, and developer implementation.

Layout decisions should be intentional rather than decorative.

---

# Definition

A Layout System is the structural framework that controls the placement, spacing, sizing, alignment, and responsiveness of every interface element.

It creates predictable relationships between components.

---

# Objectives

After completing this module, the AI should be able to:

- Build responsive layouts
- Create scalable page structures
- Apply spacing systems
- Build reusable layout patterns
- Improve consistency
- Improve readability
- Support accessibility
- Improve developer handoff
- Reduce layout complexity

---

# Layout System Mindset

Never ask:

"Where should this component go?"

Always ask:

- Does the layout support user goals?
- Is the structure scalable?
- Is spacing consistent?
- Will this adapt across screen sizes?
- Can developers implement this easily?

---

# Core Principles

Always:

- Design with structure.
- Use layout grids.
- Apply consistent spacing.
- Build responsive layouts.
- Align to a defined system.
- Design with Auto Layout.
- Minimize layout exceptions.

Never:

- Place elements arbitrarily.
- Mix spacing scales.
- Ignore responsiveness.
- Break alignment.
- Build layouts that cannot scale.

---

# Layout Goals

Every layout should:

- Organize information
- Improve readability
- Guide attention
- Support interaction
- Scale across devices
- Reduce cognitive effort

---

# Structural Hierarchy

Every interface should define:

Page

↓

Sections

↓

Containers

↓

Groups

↓

Components

↓

Content

Each level should have a clear responsibility.

---

# Layout Consistency

Consistency should exist across:

- Pages
- Components
- Sections
- Dashboards
- Forms
- Tables
- Navigation
- Cards

The same layout rules should apply throughout the product.

---

# AI Decision Rules

Before approving any layout:

- Is the structure logical?
- Is spacing consistent?
- Does the layout scale?
- Is alignment maintained?
- Is responsiveness considered?
- Can developers implement it efficiently?

If any answer is negative, redesign the layout.

---

# Validation Checklist

□ Structural hierarchy defined

□ Layout consistency maintained

□ Responsive behavior considered

□ Alignment reviewed

□ Spacing reviewed

□ Accessibility reviewed

□ Scalability validated

□ Documentation updated

---

# Auto Layout

## Definition

Auto Layout is the primary layout system for building responsive interfaces in Figma.

It automatically manages:

- Position
- Size
- Alignment
- Spacing
- Padding
- Distribution
- Resizing

Every production-ready component should use Auto Layout whenever appropriate.

---

# Benefits of Auto Layout

Auto Layout improves:

- Responsiveness
- Scalability
- Consistency
- Component reuse
- Design speed
- Developer handoff

Avoid manual positioning whenever possible.

---

# Auto Layout Direction

Auto Layout supports:

## Vertical

Use for:

- Forms
- Lists
- Sidebars
- Cards
- Settings pages

Content flows vertically.

---

## Horizontal

Use for:

- Navigation bars
- Button groups
- Toolbars
- Tags
- Menus

Content flows horizontally.

---

## Grid

Use for:

- Dashboards
- Gallery layouts
- Tables
- Bento layouts
- Card collections

Choose the flow that best matches the content structure.

---

# Parent and Child Relationships

Every Auto Layout contains:

Parent Frame

↓

Child Elements

The parent controls:

- Padding
- Direction
- Gap
- Alignment
- Distribution

Children inherit layout behavior.

---

# Nested Auto Layout

Complex interfaces should combine multiple Auto Layout frames.

Example:

Page

↓

Section

↓

Card

↓

Header

↓

Button Group

↓

Buttons

Each level manages its own spacing and alignment.

---

# Padding

Padding creates internal spacing between the container and its content.

Padding should remain consistent throughout the design system.

Never substitute padding with manually positioned elements.

---

# Gap

Gap controls spacing between child elements.

Gap should:

- Follow the spacing scale.
- Remain consistent.
- Reflect hierarchy.

Avoid arbitrary gap values.

---

# Alignment

Support alignment through:

- Start
- Center
- End
- Space Between
- Stretch

Alignment should reinforce hierarchy.

---

# Distribution

Content should distribute intentionally.

Common options:

- Packed
- Space Between

Choose the option that best supports the layout goal.

---

# AI Decision Rules

Before approving any Auto Layout:

- Is Auto Layout appropriate?
- Is the direction correct?
- Is spacing consistent?
- Is padding defined?
- Are parent-child relationships clear?
- Are nested layouts logical?

Revise until every answer is positive.

---

# Validation Checklist

□ Auto Layout applied

□ Direction selected

□ Parent-child hierarchy defined

□ Padding consistent

□ Gap consistent

□ Alignment reviewed

□ Nested layouts validated

□ Documentation updated