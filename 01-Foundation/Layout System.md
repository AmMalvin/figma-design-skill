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

---

# Resizing Behavior

## Definition

Resizing determines how frames and components respond when their parent, child, or content changes.

Every component should define its resizing behavior.

Never leave resizing to chance.

---

# Hug Contents

## Definition

A frame set to Hug Contents automatically resizes to fit its child elements.

Use Hug Contents for:

- Buttons
- Tags
- Chips
- Badges
- Labels
- Tooltips
- Small cards
- Input fields with dynamic content

Hug Contents should wrap tightly around its content while respecting padding.

---

# Fill Container

## Definition

Fill Container expands an element to occupy all available space inside its parent.

Use Fill Container for:

- Page content
- Main sections
- Text inputs
- Tables
- Dashboard panels
- Lists
- Cards inside responsive layouts

Fill Container creates flexible layouts.

---

# Fixed Size

## Definition

Fixed Size maintains a constant width or height regardless of surrounding changes.

Use Fixed Size for:

- Logos
- Icons
- Avatars
- Images with fixed ratios
- Brand marks
- Floating buttons

Avoid Fixed Size for content that changes frequently.

---

# Minimum Dimensions

Minimum dimensions prevent components from shrinking below a usable size.

Use minimum values for:

- Buttons
- Inputs
- Cards
- Navigation
- Dialogs

Minimum dimensions protect usability.

---

# Maximum Dimensions

Maximum dimensions prevent components from becoming excessively large.

Apply maximum values to:

- Text blocks
- Containers
- Cards
- Dialogs
- Images

Maximum dimensions improve readability.

---

# Responsive Containers

Containers should resize based on:

- Screen size
- Parent size
- Content size
- Available space

Containers should never create unnecessary overflow.

---

# Layout Constraints

Constraints determine how elements behave when a frame changes size.

Common constraints include:

- Left
- Right
- Top
- Bottom
- Center
- Scale

Choose constraints that match the intended responsive behavior.

---

# Auto Resizing

Auto resizing allows layouts to adapt automatically as content changes.

Support:

- Dynamic text
- Variable content
- Localization
- User-generated content
- Accessibility settings

Design for changing content, not fixed examples.

---

# Overflow Handling

Overflow should be intentional.

Use:

- Scrolling
- Clipping
- Wrapping
- Pagination
- Progressive disclosure

Never allow accidental overflow.

---

# Responsive Nesting

Nested layouts should remain predictable.

Each parent controls:

- Direction
- Padding
- Gap
- Alignment

Each child defines:

- Hug Contents
- Fill Container
- Fixed Size

Avoid conflicting resizing rules.

---

# Layout Guides

Layout guides improve consistency.

Use guides for:

- Margins
- Columns
- Gutters
- Safe areas
- Alignment

Guides should be shared across the entire design system.

---

# Frame Behavior

Every frame should define:

- Width behavior
- Height behavior
- Alignment
- Overflow
- Padding
- Gap
- Constraints

Frame behavior should remain predictable across every screen.

---

# AI Layout Engine

Before approving any layout, answer:

- Is the resizing behavior defined?
- Should this element Hug Contents, Fill Container, or remain Fixed?
- Are minimum and maximum dimensions appropriate?
- Will the layout adapt to different screen sizes?
- Is overflow handled correctly?
- Do nested layouts behave predictably?
- Can developers implement this easily?

Revise until every answer is positive.

---

# Validation Checklist

□ Hug Contents applied correctly

□ Fill Container applied correctly

□ Fixed Size reviewed

□ Minimum dimensions defined

□ Maximum dimensions defined

□ Responsive containers validated

□ Constraints documented

□ Overflow handled

□ Nested layouts reviewed

□ Layout guides applied

□ Frame behavior documented