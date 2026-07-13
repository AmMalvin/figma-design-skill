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


---

# Navigation Components

## Philosophy

Navigation components help users understand structure, progress, and location.

Each component should solve one navigation problem.

Avoid using multiple components for the same purpose.

---

# Tabs

## Purpose

Tabs organize related content within the same page.

Examples:

- Overview
- Analytics
- Settings
- Billing

Rules:

- Tabs switch content without changing the overall context.
- Clearly indicate the active tab.
- Keep labels concise.
- Avoid more than seven visible tabs.

---

# Breadcrumbs

## Purpose

Breadcrumbs show the user's current location within a hierarchy.

Example:

Home

>

Products

>

Laptops

>

Gaming

Requirements:

- Display the current page.
- Support navigation to previous levels.
- Use concise labels.

Do not use breadcrumbs as primary navigation.

---

# Pagination

## Purpose

Pagination divides large collections into manageable pages.

Requirements:

- Display the current page.
- Allow previous and next navigation.
- Support direct page selection when appropriate.

Avoid pagination for small datasets.

---

# Stepper

## Purpose

Steppers communicate progress through sequential tasks.

Examples:

- Account Setup
- Checkout
- Onboarding
- Verification

Requirements:

- Clearly indicate the current step.
- Show completed steps.
- Prevent confusion about progress.

---

# Tree Navigation

## Purpose

Tree navigation displays hierarchical information.

Recommended for:

- File explorers
- Documentation
- Category management
- Organization charts

Expandable nodes should clearly communicate their state.

---

# Accordion Navigation

## Purpose

Accordions reveal or hide related navigation items.

Requirements:

- Clear expand and collapse controls.
- Preserve user context.
- Avoid unnecessary nesting.

---

# Navigation States

Every navigation component should define:

- Default
- Hover
- Focus
- Active
- Selected
- Expanded
- Collapsed
- Disabled

Each state should communicate meaningful feedback.

---

# Default State

The default state communicates availability.

No destination should appear selected unless it represents the current location.

---

# Hover State

Hover confirms interactivity.

Visual changes may include:

- Background
- Text color
- Underline
- Elevation

Avoid excessive visual changes.

---

# Focus State

Focus supports keyboard navigation.

Requirements:

- Highly visible
- High contrast
- Consistent across all navigation components

Never remove focus indicators.

---

# Active State

The active state identifies the current destination.

Users should immediately understand where they are.

Only one destination should normally appear active within the same navigation level.

---

# Selected State

Selected items indicate user choice.

Examples:

- Selected filter
- Selected category
- Selected workspace

Selected differs from Active.

---

# Expanded State

Expanded navigation reveals child destinations.

Expanded groups should remain visually connected.

---

# Collapsed State

Collapsed navigation hides secondary destinations.

Users should understand additional content exists.

---

# Disabled State

Disabled navigation communicates temporary unavailability.

Requirements:

- Clearly inactive
- Still readable
- Never misleading

Whenever possible, explain why an item is unavailable.

---

# Responsive Navigation

Navigation should adapt across devices.

Examples:

Desktop

Top Navigation

+

Side Navigation

Tablet

Navigation Rail

Expandable Side Navigation

Mobile

Bottom Navigation

Hamburger Menu

Collapsible Sections

Navigation should preserve discoverability.

---

# Motion

Motion should reinforce navigation.

Examples:

- Expand
- Collapse
- Slide
- Fade
- Indicator movement

Motion should improve understanding.

Avoid decorative animation.

---

# AI Navigation Interaction Engine

Before approving navigation behavior, answer:

- Is the current location obvious?
- Are interaction states complete?
- Is keyboard navigation supported?
- Does responsive behavior preserve usability?
- Does motion improve understanding?
- Can users recover if they navigate incorrectly?

If any answer is negative, redesign the interaction.

---

# Validation Checklist

□ Tabs documented

□ Breadcrumbs documented

□ Pagination documented

□ Stepper documented

□ Tree navigation documented

□ Accordion documented

□ Navigation states completed

□ Responsive behavior documented

□ Motion documented

□ Accessibility reviewed


---

# Keyboard Navigation

## Purpose

Every navigation component should be fully operable using a keyboard.

Minimum requirements:

- Tab moves focus
- Shift + Tab moves focus backward
- Enter activates navigation items
- Space activates controls when appropriate
- Arrow keys navigate grouped items
- Escape closes temporary navigation

Keyboard interaction should match user expectations.

---

# Focus Management

Focus should:

- Always remain visible
- Follow a logical order
- Never become trapped
- Return predictably after closing menus or drawers

Never remove focus indicators.

---

# Screen Reader Support

Navigation should expose meaningful information.

Every navigation item should have:

- Accessible name
- Role
- Current state
- Expanded state when applicable

Users should understand navigation without visual cues.

---

# Search Within Navigation

Large products should provide navigation search.

Examples:

- Documentation
- Enterprise software
- Developer tools
- Knowledge bases

Search results should prioritize relevance.

---

# Navigation Badges

Badges communicate status.

Examples:

- Notifications
- Updates
- Unread messages
- Pending tasks

Rules:

- Use only when meaningful.
- Keep counts readable.
- Avoid excessive badge usage.

Badges should not replace navigation labels.

---

# Empty Navigation States

Empty navigation should communicate why content is unavailable.

Examples:

- No recent projects
- No saved items
- No notifications

Provide a helpful next action whenever possible.

---

# Responsive Adaptation

Navigation should adapt without losing functionality.

Examples:

Desktop

Top Navigation + Side Navigation

Tablet

Navigation Rail

Expandable Navigation

Mobile

Bottom Navigation

Hamburger Navigation

Essential destinations should always remain reachable.

---

# Design Token Integration

Navigation should consume design tokens.

Examples:

navigation.height

navigation.padding

navigation.background

navigation.border

navigation.item.active

navigation.focus.ring

Never hardcode visual values.

---

# Motion Guidelines

Motion should support orientation.

Appropriate uses:

- Menu expansion
- Drawer opening
- Active indicator movement
- Breadcrumb transitions
- Tab indicator movement

Motion should improve understanding.

Avoid decorative animation.

---

# Documentation

Every navigation component should document:

- Purpose
- Anatomy
- Variants
- States
- Accessibility
- Responsive behavior
- Usage guidelines
- Do
- Don't
- Examples

Documentation should eliminate implementation ambiguity.

---

# Testing

Every navigation component should be tested for:

- Keyboard interaction
- Screen readers
- Responsive layouts
- Active states
- Focus management
- Motion
- Performance
- Content overflow

Testing should occur before release.

---

# Quality Assurance

Review every navigation component for:

- Discoverability
- Consistency
- Accessibility
- Responsive behavior
- Design token usage
- Documentation
- Performance

Only approved navigation belongs in the design system.

---

# Versioning

Maintain version history for:

- New navigation patterns
- Interaction changes
- Accessibility improvements
- Bug fixes
- Breaking changes

Version history supports long-term maintenance.

---

# Governance

Navigation changes should follow a structured review process.

Every update should include:

- UX review
- Accessibility review
- Developer review
- QA approval
- Documentation update

Consistency depends on governance.

---

# AI Navigation Review Engine

Before publishing any navigation component, answer:

- Is the navigation hierarchy clear?
- Is the current location obvious?
- Is keyboard support complete?
- Is screen reader support complete?
- Does responsive behavior preserve usability?
- Are design tokens used?
- Has testing been completed?
- Can this navigation scale across products?

If any answer is negative, revise the navigation.

---

# Navigation Checklist

Before publishing:

□ Navigation patterns documented

□ States completed

□ Keyboard interaction verified

□ Screen reader support completed

□ Responsive behavior validated

□ Search behavior documented

□ Badge behavior documented

□ Empty states documented

□ Design tokens integrated

□ Motion documented

□ Testing completed

□ QA approved

□ Version history updated

□ Documentation completed

---

# Key Takeaways

Navigation helps users understand structure and move confidently through a product.

The AI must:

- Build reusable navigation systems.
- Maintain clear information architecture.
- Highlight the current location.
- Support keyboard and screen readers.
- Adapt navigation across devices.
- Use design tokens.
- Keep interactions predictable.
- Test every navigation pattern.
- Document every behavior.
- Govern navigation through consistent review.

Every navigation component should improve orientation, discoverability, accessibility, and long-term maintainability.