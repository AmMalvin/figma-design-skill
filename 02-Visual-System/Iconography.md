---
title: Iconography
version: 1.0.0
status: Stable
owner: Design System Skill
category: Visual System
priority: Critical
last_updated: 2026-07-13

inherits:
  - ../00-Core/Universal Design Principles.md
  - ../01-Foundation/Accessibility.md
  - ../01-Foundation/Layout Systems.md
  - ../02-Visual-System/Color Theory.md
  - ../02-Visual-System/Typography.md
  - ../02-Visual-System/Spacing & Sizing.md
---

# Iconography

## Purpose

This module teaches the AI how to build scalable, accessible, and consistent icon systems for digital products.

Icons should improve communication, not replace it.

Every icon should have a clear purpose.

---

# Definition

Iconography is the system of visual symbols used to communicate actions, objects, states, and concepts.

Icons reduce cognitive effort by allowing users to recognize information quickly.

---

# Objectives

After completing this module, the AI should be able to:

- Build scalable icon systems
- Maintain visual consistency
- Improve recognition
- Improve accessibility
- Create reusable icon tokens
- Support developer implementation
- Improve navigation
- Strengthen product identity

---

# Icon Mindset

Never ask:

"Does this icon look good?"

Always ask:

- Does users recognize it?
- Does it communicate the correct meaning?
- Is it consistent with the icon system?
- Is another icon already solving this problem?
- Will developers reuse it easily?

---

# Core Principles

Always:

- Prioritize recognition.
- Use familiar symbols.
- Keep icons simple.
- Maintain consistency.
- Design reusable icons.
- Follow one visual style.

Never:

- Invent unnecessary symbols.
- Mix icon styles.
- Add decorative details.
- Depend on icons alone.
- Use icons without purpose.

---

# Why Icons Exist

Icons should:

- Communicate actions
- Support navigation
- Reinforce information
- Save interface space
- Improve recognition
- Reduce reading effort

Icons should never create ambiguity.

---

# Icon Roles

Every icon belongs to one purpose.

Examples:

- Navigation
- Action
- Status
- Notification
- File Type
- Social
- Brand
- Media
- System
- Feedback

Every icon should have one primary meaning.

---

# Recognition Over Creativity

Users should recognize icons immediately.

Choose familiarity over originality.

Avoid redesigning universally understood icons.

---

# Consistency

Icons should remain consistent across:

- Products
- Platforms
- Components
- Navigation
- Menus
- Forms
- Tables
- Dashboards

Consistency improves learnability.

---

# AI Decision Rules

Before approving an icon:

- Is the meaning obvious?
- Is the icon reusable?
- Is the style consistent?
- Does accessibility remain intact?
- Will users recognize it immediately?
- Can developers implement it easily?

If any answer is negative, redesign the icon.

---

# Validation Checklist

□ Icon system defined

□ Purpose documented

□ Consistency reviewed

□ Accessibility reviewed

□ Reusability confirmed

□ Documentation updated


---

# Icon Styles

## Definition

An icon style defines the visual appearance shared by every icon in the system.

Every icon should follow the same style.

Never mix styles without a documented reason.

---

# Filled Icons

Filled icons use solid shapes.

Characteristics:

- Strong emphasis
- High visibility
- Bold appearance

Recommended for:

- Active states
- Mobile applications
- Navigation
- Primary actions

Filled icons should remain simple.

---

# Outlined Icons

Outlined icons use strokes instead of filled shapes.

Characteristics:

- Lightweight
- Minimal
- Modern

Recommended for:

- Toolbars
- Secondary actions
- Enterprise products
- Productivity software

Outlined icons are the preferred default for most interface systems.

---

# Duotone Icons

Duotone icons use two visual tones.

Characteristics:

- Increased visual richness
- Better hierarchy
- Brand expression

Use sparingly.

Avoid mixing duotone icons with single-color icons in the same interface.

---

# Sharp Icons

Sharp icons use square edges and precise corners.

Characteristics:

- Technical
- Structured
- Mechanical

Recommended for:

- Enterprise software
- Developer tools
- Data products

Maintain consistency across the entire icon library.

---

# Rounded Icons

Rounded icons use curved corners.

Characteristics:

- Friendly
- Approachable
- Modern

Recommended for:

- Consumer products
- Education
- Healthcare
- Social platforms

Roundness should remain consistent across every icon.

---

# Stroke Icons

Stroke icons rely on line weight rather than filled shapes.

Rules:

- Maintain one stroke width.
- Keep stroke endings consistent.
- Maintain uniform joins.
- Avoid unnecessary detail.

Stroke consistency improves recognition.

---

# Filled vs Outlined

Choose one primary system.

Filled icons should communicate:

- Active
- Selected
- Important

Outlined icons should communicate:

- Default
- Neutral
- Secondary

Avoid mixing both styles randomly.

---

# Icon Families

Icons should belong to organized categories.

Examples:

- Navigation
- Actions
- Files
- Devices
- Media
- Commerce
- Communication
- Security
- Status
- Social

Every icon should have one logical location.

---

# Brand Icon Language

The icon system should reinforce the brand.

Maintain consistency in:

- Shape
- Stroke
- Corner radius
- Detail level
- Perspective
- Alignment

Icons should feel like one family.

---

# Visual Complexity

All icons should have a similar level of detail.

Avoid combining:

- Highly detailed icons
- Extremely simplified icons

Visual consistency improves recognition.

---

# Consistency Rules

Every icon should maintain:

- Similar proportions
- Similar spacing
- Similar stroke weight
- Similar visual balance
- Similar complexity

Consistency is more important than originality.

---

# AI Icon Style Engine

Before approving an icon style, answer:

- Is one visual style used?
- Are stroke widths consistent?
- Are corner radii consistent?
- Does every icon belong to one family?
- Is visual complexity balanced?
- Does the style reinforce the brand?
- Can developers reuse every icon consistently?

If any answer is negative, redesign the icon system.

---

# Validation Checklist

□ Primary icon style selected

□ Filled icon rules documented

□ Outlined icon rules documented

□ Stroke width standardized

□ Corner radius standardized

□ Icon families created

□ Brand icon language defined

□ Visual complexity reviewed

□ Documentation updated


---

# Icon Grid

## Definition

An icon grid is the geometric framework used to create consistent icons.

Every icon should be designed inside the same grid.

The grid defines:

- Size
- Alignment
- Padding
- Safe area
- Visual balance

Never create icons without a defined grid.

---

# Standard Icon Grid

Use one standard icon canvas throughout the system.

Recommended default:

24 × 24 px

The grid should remain consistent across the entire icon library.

---

# Safe Area

The safe area is the drawable region inside the icon grid.

It prevents icons from appearing crowded or visually inconsistent.

Icons should remain inside the safe area unless intentional overshoot improves optical balance.

---

# Keylines

Keylines are construction guides that help maintain consistent proportions.

Use keylines to align:

- Circles
- Squares
- Rectangles
- Diagonal shapes

Keylines improve consistency across the icon library.

---

# Optical Alignment

Icons should appear visually centered.

Visual balance is more important than mathematical centering.

Adjust icons when necessary to achieve optical balance.

Never rely solely on automatic alignment.

---

# Pixel Alignment

Icons should align to the pixel grid.

Benefits:

- Sharper rendering
- Cleaner edges
- Better small-size readability

Avoid half-pixel positioning unless required for stroke rendering.

---

# Stroke Width

Stroke width should remain consistent throughout the icon system.

Choose one standard weight.

Every outlined icon should use the same stroke width unless a documented exception exists.

---

# Stroke Endings

Define one stroke cap style.

Options include:

- Round
- Square
- Butt

Use one style consistently.

---

# Stroke Joins

Corners should use one join style.

Options include:

- Round
- Miter
- Bevel

Maintain consistency across every icon.

---

# Corner Radius

Rounded icons should use predefined radius tokens.

Examples:

radius.icon.none

radius.icon.small

radius.icon.medium

Avoid assigning unique corner radii to individual icons.

---

# Internal Padding

Every icon should maintain consistent internal padding.

Padding creates balanced visual weight across icons with different shapes.

Do not allow vectors to touch the grid boundary unless intentionally designed.

---

# Visual Weight

Icons should appear equally heavy.

Balance:

- Filled areas
- Stroke density
- Empty space
- Shape proportions

Icons should feel equally prominent regardless of shape.

---

# Scaling Rules

Icons should scale proportionally.

Never stretch icons independently in the horizontal or vertical direction.

Preserve:

- Aspect ratio
- Stroke appearance
- Visual balance

---

# Standard Icon Sizes

Supported icon sizes should use semantic tokens.

Examples:

- 16 px
- 20 px
- 24 px
- 32 px
- 40 px
- 48 px
- 64 px

Avoid arbitrary icon dimensions.

---

# SVG Optimization

Icons should be exported as optimized SVG files when supported.

Optimize by:

- Removing unnecessary points
- Simplifying paths
- Eliminating hidden geometry
- Preserving scalability

Optimized SVGs improve rendering performance.

---

# Icon Tokens

Icons should reference reusable tokens.

Examples:

icon.size.sm

icon.size.md

icon.size.lg

icon.stroke.default

icon.radius.default

Avoid hardcoded values inside components.

---

# AI Icon Construction Engine

Before approving an icon, answer:

- Does the icon use the standard grid?
- Is optical alignment correct?
- Is pixel alignment correct?
- Is stroke width consistent?
- Is internal padding balanced?
- Does the icon scale correctly?
- Can developers reuse the icon without modification?

If any answer is negative, redesign the icon.

---

# Validation Checklist

□ Standard grid defined

□ Safe area documented

□ Keylines reviewed

□ Optical alignment validated

□ Pixel alignment verified

□ Stroke width standardized

□ Stroke caps documented

□ Stroke joins documented

□ Corner radius tokens created

□ Internal padding reviewed

□ Icon sizes standardized

□ SVG optimization reviewed

□ Icon tokens documented


