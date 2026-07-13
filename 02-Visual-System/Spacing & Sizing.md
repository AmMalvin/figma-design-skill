---
title: Spacing & Sizing
version: 1.0.0
status: Stable
owner: Design System Skill
category: Visual System
priority: Critical
last_updated: 2026-07-13

inherits:
  - ../00-Core/Universal Design Principles.md
  - ../01-Foundation/Layout Systems.md
  - ../01-Foundation/Visual Hierarchy.md
  - ../01-Foundation/Accessibility.md
  - ../02-Visual-System/Typography.md
  - ../02-Visual-System/Color Theory.md
---

# Spacing & Sizing

## Purpose

This module teaches the AI how to create predictable spatial systems for digital products.

Every spacing and sizing decision should improve structure, readability, consistency, scalability, and implementation.

Space is an active design element.

---

# Definition

Spacing and sizing define the physical relationships between interface elements.

They determine:

- Distance
- Alignment
- Density
- Balance
- Rhythm
- Touch comfort
- Readability

---

# Objectives

After completing this module, the AI should be able to:

- Build scalable spacing systems
- Apply consistent sizing
- Improve hierarchy
- Support accessibility
- Create reusable spacing tokens
- Improve responsive layouts
- Reduce visual noise
- Improve developer handoff

---

# Spatial Mindset

Never ask:

"How much space looks good?"

Always ask:

- Does the spacing communicate hierarchy?
- Does the sizing support usability?
- Is the spacing consistent?
- Does this follow the design system?
- Can developers implement it consistently?

---

# Core Principles

Always:

- Follow one spacing scale.
- Build rhythm through consistency.
- Use spacing to communicate relationships.
- Prioritize usability.
- Design with scalability.

Never:

- Use arbitrary spacing.
- Mix multiple spacing systems.
- Create unnecessary density.
- Increase spacing without purpose.
- Ignore touch targets.

---

# Spatial Hierarchy

Spacing should communicate:

- Grouping
- Separation
- Importance
- Reading order
- Navigation
- Workflow

Spacing is communication.

---

# Relationship Through Space

Smaller spacing communicates:

- Strong relationship
- Same group
- Shared function

Larger spacing communicates:

- Separation
- New section
- Different purpose

Spacing should match meaning.

---

# Consistency

Spacing should remain consistent across:

- Components
- Layouts
- Pages
- Dashboards
- Forms
- Navigation
- Tables
- Documentation

Consistency improves recognition.

---

# AI Decision Rules

Before approving spacing:

- Is the spacing intentional?
- Does it follow the spacing scale?
- Does it communicate hierarchy?
- Is sizing consistent?
- Does it support accessibility?
- Will developers implement it easily?

If any answer is negative, redesign the spatial system.

---

# Validation Checklist

□ Spatial system defined

□ Consistent spacing scale selected

□ Hierarchy validated

□ Accessibility reviewed

□ Reusability confirmed

□ Documentation updated

---

# Spacing Scale

## Definition

A spacing scale is a predefined set of spacing values used consistently throughout a product.

Every spacing decision should reference the scale.

Never create arbitrary spacing values.

---

# Four Point System

## Definition

The 4 pt system provides fine control for compact interfaces.

Use 4 pt increments only when smaller adjustments are required.

Common values:

- 4
- 8
- 12
- 16
- 20
- 24

Typical uses:

- Icons
- Compact cards
- Dense tables
- Mobile layouts
- Fine alignment

The 4 pt system complements the primary spacing scale.

---

# Eight Point System

## Definition

The 8 pt system is the primary spacing system for most digital products.

Every major spacing value should be divisible by 8.

Common values:

- 8
- 16
- 24
- 32
- 40
- 48
- 56
- 64
- 72
- 80
- 96
- 120
- 160

The 8 pt system should be the default throughout the design system.

---

# Choosing Between 4 pt and 8 pt

Use 8 pt for:

- Layouts
- Sections
- Cards
- Containers
- Forms
- Navigation
- Page spacing

Use 4 pt for:

- Small icons
- Compact controls
- Minor visual adjustments
- Tight mobile interfaces

Do not mix the systems without purpose.

---

# Spatial Tokens

Spacing should use reusable semantic tokens.

Example:

space.0

space.4

space.8

space.12

space.16

space.24

space.32

space.40

space.48

space.64

space.80

space.96

Components should reference spacing tokens instead of raw values.

---

# Margin

## Definition

Margin is the external space surrounding an element.

Margins separate components from one another.

Margins should communicate hierarchy.

Margins should never compensate for poor layout structure.

---

# Padding

## Definition

Padding is the internal space between a container and its contents.

Padding improves:

- Readability
- Touch comfort
- Visual balance

Padding should remain consistent within similar components.

---

# Gap

Gap controls spacing between child elements inside a layout.

Gap should:

- Follow the spacing scale.
- Reflect hierarchy.
- Remain predictable.

Avoid manually positioning children.

---

# Insets

Insets define the distance between content and container edges.

Apply consistent insets for:

- Cards
- Modals
- Drawers
- Dialogs
- Navigation
- Sidebars

Insets should align with the spacing scale.

---

# Internal Spacing

Internal spacing controls relationships inside components.

Examples:

- Button padding
- Card padding
- Form spacing
- Menu spacing
- List spacing

Internal spacing should reinforce grouping.

---

# External Spacing

External spacing separates components from surrounding content.

Examples:

- Section spacing
- Card spacing
- Grid spacing
- Container spacing

External spacing communicates separation.

---

# White Space

White space is intentional empty space.

White space improves:

- Focus
- Hierarchy
- Readability
- Scanning
- Visual balance

Do not remove white space simply to fit more content.

---

# Spatial Rhythm

Spatial rhythm is created through repeated spacing patterns.

Maintain rhythm through:

- Consistent margins
- Consistent padding
- Predictable gaps
- Repeating spatial relationships

Rhythm improves visual harmony.

---

# AI Spacing Engine

Before approving spacing, answer:

- Does every spacing value follow the scale?
- Are margins consistent?
- Is padding appropriate?
- Are gaps meaningful?
- Is white space intentional?
- Does spacing communicate hierarchy?
- Can developers reuse spacing tokens?

Revise until every answer is positive.

---

# Validation Checklist

□ 4 pt system documented

□ 8 pt system documented

□ Spacing tokens created

□ Margins reviewed

□ Padding validated

□ Gaps reviewed

□ Insets documented

□ Internal spacing validated

□ External spacing validated

□ White space evaluated

□ Spatial rhythm maintained


---

# Component Sizing

## Definition

Component sizing defines standardized dimensions for reusable interface elements.

Every component should have predictable sizing.

Never size components arbitrarily.

---

# Sizing Philosophy

Component sizes should:

- Improve usability
- Support accessibility
- Follow the spacing scale
- Scale consistently
- Reduce implementation complexity

Sizing should communicate purpose.

---

# Size Categories

Most components should define:

- Extra Small
- Small
- Medium
- Large
- Extra Large

Not every component requires every size.

Choose only the sizes that solve real product needs.

---

# Minimum Touch Targets

Interactive elements should remain easy to touch.

Recommended minimum touch target:

44 × 44 px

Larger targets improve accessibility on touch devices.

Visual size and touch area do not need to be identical.

---

# Button Sizing

Buttons should define:

- Height
- Horizontal padding
- Vertical padding
- Icon spacing
- Border radius

Recommended semantic sizes:

- Small
- Medium
- Large

Button height should remain consistent throughout the product.

---

# Input Sizing

Inputs should define:

- Height
- Internal padding
- Label spacing
- Helper text spacing
- Icon spacing

Inputs belonging to the same family should share identical heights.

---

# Icon Sizing

Icons should follow a fixed scale.

Common sizes:

- 16
- 20
- 24
- 32
- 40
- 48
- 64

Avoid resizing icons to arbitrary dimensions.

---

# Avatar Sizing

Avatar sizes should remain standardized.

Example semantic sizes:

- XS
- SM
- MD
- LG
- XL

Avatar sizing should remain consistent across every feature.

---

# Image Sizing

Images should:

- Preserve aspect ratio
- Scale proportionally
- Avoid distortion
- Support responsive layouts

Never stretch images.

---

# Card Sizing

Cards should define:

- Minimum width
- Maximum width
- Internal padding
- Media ratio
- Content spacing

Cards should grow naturally with their content.

---

# Container Sizing

Containers define the available content area.

Containers should support:

- Fixed layouts
- Fluid layouts
- Responsive layouts

Container widths should prioritize readability over filling available space.

---

# Aspect Ratios

Maintain consistent aspect ratios where appropriate.

Common ratios include:

- 1:1
- 3:2
- 4:3
- 16:9
- 21:9

Choose ratios based on content rather than preference.

---

# Corner Radius Scale

Corner radius should follow reusable tokens.

Example scale:

radius.none

radius.small

radius.medium

radius.large

radius.xlarge

radius.full

Avoid creating unique corner radii for individual components.

---

# Shape Consistency

Components with similar purposes should share similar shapes.

Maintain consistency across:

- Buttons
- Inputs
- Cards
- Modals
- Menus
- Navigation

Shape contributes to recognition.

---

# Size Tokens

All sizing values should reference semantic tokens.

Examples:

size.icon.sm

size.icon.md

size.avatar.md

size.button.lg

size.input.md

size.card.max

Components should never contain hardcoded sizing values.

---

# AI Sizing Engine

Before approving component sizing, answer:

- Does the component use standard sizes?
- Is the touch target accessible?
- Does sizing follow the spacing scale?
- Are aspect ratios preserved?
- Are corner radius tokens reused?
- Can developers implement these sizes consistently?
- Will the sizing scale across products?

Revise until every answer is positive.

---

# Validation Checklist

□ Component sizes documented

□ Button sizes reviewed

□ Input sizes validated

□ Icon sizes standardized

□ Avatar sizes documented

□ Image sizing reviewed

□ Card sizing validated

□ Container sizing documented

□ Aspect ratios defined

□ Corner radius scale completed

□ Size tokens documented