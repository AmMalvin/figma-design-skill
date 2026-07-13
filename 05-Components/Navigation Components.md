---
title: Navigation Components
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
  - ../02-Visual-System/Typography.md
  - ../02-Visual-System/Iconography.md
  - ../02-Visual-System/Spacing & Sizing.md
  - ./Component Principles.md
---

# Navigation Components

## Purpose

This module teaches the AI how to design scalable, reusable, accessible, and production-ready navigation systems.

Navigation helps users understand structure, orientation, and movement throughout an application.

---

# Definition

Navigation components allow users to:

- Move between pages
- Discover features
- Understand location
- Return to previous sections
- Complete workflows

Navigation should reduce cognitive effort.

---

# Objectives

After completing this module, the AI should be able to:

- Design reusable navigation systems
- Improve wayfinding
- Support responsive layouts
- Maintain accessibility
- Improve developer implementation
- Scale across products

---

# Navigation Philosophy

Every navigation component should answer:

- Where am I?
- Where can I go?
- How do I return?

Navigation should never create uncertainty.

---

# Core Principles

Always:

- Keep navigation predictable.
- Group related destinations.
- Highlight the current location.
- Support keyboard interaction.
- Maintain consistency.
- Design reusable components.

Never:

- Hide important destinations.
- Overcrowd navigation.
- Change navigation patterns unnecessarily.
- Use ambiguous labels.
- Duplicate navigation structures.

---

# Why Navigation Exists

Navigation helps users:

- Explore products
- Complete workflows
- Switch sections
- Find information
- Return to previous locations
- Understand hierarchy

Navigation should reduce friction.

---

# Navigation Anatomy

Every navigation component should define:

- Container
- Navigation items
- Active indicator
- Icons
- Labels
- Optional badges
- Optional dividers

Each element should have one responsibility.

---

# Navigation Items

Each navigation item should include:

- Label
- Destination
- Optional icon
- Optional badge

Labels should remain concise.

---

# Active Indicator

The active indicator communicates the current location.

Examples:

- Background
- Border
- Underline
- Accent bar

Active state should remain visible.

---

# Hierarchy

Prioritize:

- Current location
- Primary destinations
- Secondary destinations
- Supporting actions

Hierarchy should improve orientation.

---

# AI Decision Rules

Before approving navigation, answer:

- Is orientation obvious?
- Is hierarchy clear?
- Is accessibility supported?
- Is the navigation reusable?
- Is responsiveness supported?
- Can developers implement it consistently?

If any answer is negative, redesign the navigation.

---

# Validation Checklist

□ Purpose documented

□ Anatomy documented

□ Navigation items documented

□ Active indicator documented

□ Hierarchy documented

□ Accessibility reviewed

□ Documentation updated


---

# Navigation Types

## Philosophy

Every navigation pattern should belong to one reusable component family.

Different navigation patterns solve different navigation problems while sharing the same design language.

Avoid creating duplicate navigation components.

---

# App Bar

## Purpose

Provide global navigation and primary application actions.

Typical content:

- Logo
- Page title
- Search
- Notifications
- User profile
- Primary actions

The app bar should remain visible when appropriate.

---

# Top Navigation

## Purpose

Navigate between primary sections.

Examples:

- Marketing websites
- SaaS dashboards
- Documentation
- Enterprise software

Top navigation should contain only primary destinations.

---

# Bottom Navigation

## Purpose

Provide quick access to primary destinations on mobile.

Recommended:

- Three to five destinations

Each destination should:

- Include an icon
- Include a label
- Clearly indicate the active destination

---

# Sidebar

## Purpose

Display persistent navigation for complex applications.

Examples:

- Admin panels
- CRM systems
- Analytics platforms
- Design tools

Sidebars should support hierarchy.

---

# Navigation Rail

## Purpose

Provide compact navigation.

Recommended for:

- Tablet
- Desktop
- Large screens

Navigation rails prioritize icons while preserving accessibility.

---

# Tabs

## Purpose

Switch between related views without changing context.

Examples:

- Profile sections
- Settings
- Dashboard pages
- Product details

Tabs should not navigate between unrelated pages.

---

# Breadcrumbs

## Purpose

Communicate location within a hierarchy.

Examples:

Home

Products

Laptops

MacBook Pro

Breadcrumbs should support upward navigation.

---

# Pagination

## Purpose

Navigate through paginated content.

Examples:

- Search results
- Products
- Reports
- Tables

Users should always understand their current page.

---

# Stepper

## Purpose

Guide users through sequential workflows.

Examples:

- Checkout
- Registration
- Onboarding
- Multi-step forms

Steppers should clearly indicate progress.

---

# Tree Navigation

## Purpose

Display hierarchical information.

Examples:

- File explorer
- Documentation
- Organization charts
- Folder structures

Tree navigation should support expansion and collapse.

---

# Navigation Selection Guide

Use:

App Bar

For global application controls.

Top Navigation

For primary website sections.

Bottom Navigation

For mobile destinations.

Sidebar

For complex applications.

Navigation Rail

For compact desktop navigation.

Tabs

For switching between related content.

Breadcrumbs

For hierarchical location.

Pagination

For large collections.

Stepper

For sequential workflows.

Tree Navigation

For nested information.

---

# Navigation Variants

Represent navigation as variants.

Recommended properties:

Type

- App Bar
- Top
- Bottom
- Sidebar
- Rail
- Tabs
- Breadcrumbs
- Pagination
- Stepper
- Tree

State

- Default
- Hover
- Focus
- Active
- Disabled

Size

- Small
- Medium
- Large

Avoid creating duplicate navigation systems.

---

# Responsive Behavior

Desktop

- Sidebar
- Top navigation
- Navigation rail

Tablet

- Navigation rail
- Sidebar
- Tabs

Mobile

- Bottom navigation
- App bar
- Bottom sheet navigation

Choose the navigation pattern that best fits the device.

---

# AI Navigation Selection Engine

Before selecting a navigation pattern, answer:

- Does the pattern match the information architecture?
- Is navigation predictable?
- Is hierarchy clear?
- Is accessibility supported?
- Is responsiveness supported?
- Can this remain part of one reusable component family?

If any answer is negative, choose a more appropriate navigation pattern.

---

# Validation Checklist

□ App bar documented

□ Top navigation documented

□ Bottom navigation documented

□ Sidebar documented

□ Navigation rail documented

□ Tabs documented

□ Breadcrumbs documented

□ Pagination documented

□ Stepper documented

□ Tree navigation documented

□ Variant strategy documented

□ Responsive behavior documented