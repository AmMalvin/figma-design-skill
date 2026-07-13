---
title: Navigation
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
  - ../02-Visual-System/Iconography.md
  - ./Component Principles.md
---

# Navigation

## Purpose

This module teaches the AI how to design scalable, reusable, accessible, and production-ready navigation systems.

Navigation helps users move through products with confidence.

---

# Definition

Navigation is the collection of components that help users understand location, discover content, and move between destinations.

Navigation should always support user goals.

---

# Objectives

After completing this module, the AI should be able to:

- Design consistent navigation
- Improve discoverability
- Reduce navigation effort
- Support accessibility
- Scale navigation systems
- Improve orientation
- Support responsive layouts
- Improve developer implementation

---

# Navigation Philosophy

Navigation should answer three questions:

- Where am I?
- Where can I go?
- How do I return?

Users should never feel lost.

---

# Core Principles

Always:

- Keep navigation predictable.
- Use clear labels.
- Group related destinations.
- Maintain consistency.
- Highlight the current location.
- Support keyboard navigation.

Never:

- Hide important destinations.
- Use vague labels.
- Change navigation patterns between pages.
- Create unnecessary menu levels.
- Overload navigation.

---

# Why Navigation Exists

Navigation helps users:

- Explore
- Discover
- Switch contexts
- Complete workflows
- Return to previous locations
- Understand product structure

Navigation should reduce cognitive effort.

---

# Navigation Anatomy

Every navigation component should define:

- Container
- Brand area
- Navigation items
- Current destination
- Optional icons
- Optional badges
- Optional actions

Each element should have one responsibility.

---

# Navigation Items

Every navigation item should contain:

- Label
- Destination
- Optional icon
- Optional badge
- Active state

Navigation items should remain consistent.

---

# Navigation Hierarchy

Navigation should establish clear levels.

Typical levels include:

- Global navigation
- Section navigation
- Local navigation
- Contextual navigation

Avoid mixing hierarchy levels.

---

# Active Destination

Always indicate the current location.

The active destination should remain visually distinct.

Users should immediately understand where they are.

---

# Labels

Navigation labels should:

- Be concise
- Describe destinations
- Remain consistent
- Avoid marketing language

Prefer nouns over vague actions.

---

# Information Architecture

Navigation should reflect product structure.

Group related destinations together.

Avoid unnecessary nesting.

---

# AI Decision Rules

Before approving navigation, answer:

- Can users find important destinations?
- Is the hierarchy clear?
- Are labels understandable?
- Is accessibility supported?
- Is navigation reusable?
- Can developers implement this consistently?

If any answer is negative, redesign the navigation.

---

# Validation Checklist

□ Navigation purpose documented

□ Anatomy documented

□ Hierarchy defined

□ Active state documented

□ Labels reviewed

□ Accessibility reviewed

□ Documentation updated


---

# Navigation Types

## Philosophy

Navigation patterns should solve different navigation problems while remaining part of one reusable system.

Each navigation type should have a clearly defined purpose.

Avoid mixing multiple navigation patterns without justification.

---

# Top Navigation

## Purpose

Top navigation provides access to the primary sections of a product.

Common content:

- Brand
- Primary destinations
- Search
- Notifications
- User profile
- Primary actions

Top navigation should remain consistent across related pages.

---

# Side Navigation

## Purpose

Side navigation supports products with many destinations.

Examples:

- Dashboards
- Admin panels
- Enterprise software
- Documentation

Rules:

- Organize destinations into logical groups.
- Highlight the active destination.
- Support expandable sections.

---

# Bottom Navigation

## Purpose

Bottom navigation supports mobile applications.

Recommended:

- Three to five primary destinations

Requirements:

- Persistent visibility
- Large touch targets
- Clear active state

Avoid more than five destinations.

---

# Navigation Rail

## Purpose

Navigation rails provide compact navigation for tablets and large screens.

Recommended for:

- Productivity tools
- Enterprise applications
- Multi-panel layouts

Navigation rails should expand when additional context is needed.

---

# Mega Menu

## Purpose

Mega menus organize many navigation options.

Requirements:

- Logical grouping
- Clear headings
- Scannable layout
- Consistent spacing

Avoid overwhelming users with unnecessary options.

---

# Dropdown Menu

## Purpose

Dropdown menus reveal secondary options.

Use for:

- Account actions
- Filters
- Settings
- Secondary navigation

Menus should close predictably after selection.

---

# Context Menu

## Purpose

Context menus expose actions related to the selected object.

Examples:

- Rename
- Duplicate
- Delete
- Share

Only include actions relevant to the current context.

---

# Hamburger Menu

## Purpose

Hamburger menus collapse navigation into a compact interface.

Recommended for:

- Mobile devices
- Responsive layouts

Do not hide frequently used actions unnecessarily.

---

# Utility Navigation

Utility navigation contains supporting actions.

Examples:

- Settings
- Help
- Language
- Notifications
- User Profile

Utility navigation should remain visually separate from primary navigation.

---

# Secondary Navigation

Secondary navigation helps users move within a section.

Examples:

- Product categories
- Settings pages
- Documentation sections

Secondary navigation should never compete with global navigation.

---

# Navigation Selection Guide

Use:

Top Navigation

For websites and general applications.

Side Navigation

For complex products with many destinations.

Bottom Navigation

For mobile applications.

Navigation Rail

For tablet and desktop productivity tools.

Mega Menu

For large information architectures.

Dropdown Menu

For compact option lists.

Context Menu

For object-specific actions.

Hamburger Menu

For responsive navigation.

Utility Navigation

For supporting actions.

Secondary Navigation

For subsection navigation.

---

# Responsive Navigation

Navigation should adapt to screen size.

Examples:

Desktop

Top Navigation + Side Navigation

Tablet

Navigation Rail

Mobile

Bottom Navigation or Hamburger Menu

Do not remove essential destinations on smaller screens.

---

# Navigation Variants

Represent navigation patterns as variants.

Recommended properties:

Type

- Top
- Side
- Bottom
- Rail
- Mega Menu
- Dropdown
- Context
- Hamburger
- Utility
- Secondary

Avoid building unrelated navigation components.

---

# AI Navigation Selection Engine

Before selecting a navigation pattern, answer:

- How many destinations exist?
- What device is being used?
- How often are destinations accessed?
- Is the hierarchy clear?
- Is accessibility supported?
- Can this navigation scale?

If any answer is negative, choose a more appropriate navigation pattern.

---

# Validation Checklist

□ Top navigation documented

□ Side navigation documented

□ Bottom navigation documented

□ Navigation rail documented

□ Mega menu documented

□ Dropdown menu documented

□ Context menu documented

□ Hamburger menu documented

□ Utility navigation documented

□ Secondary navigation documented

□ Responsive behavior documented

□ Variant strategy documented