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


---

# Component Variants

## Definition

Variants are different versions of the same component.

Variants represent predictable changes while preserving the component's purpose.

A Button remains a Button regardless of its variant.

---

# Why Variants Exist

Variants reduce duplication.

Instead of creating multiple independent components, use one component with structured variations.

Benefits:

- Better organization
- Easier maintenance
- Faster updates
- Better developer handoff

---

# Variant Principles

Variants should only represent predictable changes.

Examples:

- Size
- State
- Style
- Theme
- Orientation

Avoid creating variants for unrelated functionality.

---

# Component Properties

## Definition

Component properties define what users are allowed to customize.

Properties should expose flexibility without breaking consistency.

---

# Property Types

Every design system should support appropriate property types.

Examples include:

- Variant Property
- Boolean Property
- Text Property
- Instance Swap Property
- Slot Property

Only expose properties users genuinely need.

---

# Variant Properties

Variant properties define structured variations.

Examples:

Size

- Small
- Medium
- Large

State

- Default
- Hover
- Focus
- Pressed
- Disabled

Appearance

- Primary
- Secondary
- Tertiary

Each property should represent one concept.

---

# Boolean Properties

Boolean properties control visibility.

Examples:

Has Icon

True

False

Has Badge

True

False

Loading

True

False

Avoid creating separate variants for simple visibility changes.

---

# Text Properties

Text properties allow content to change without detaching the component.

Examples:

- Button label
- Input placeholder
- Dialog title
- Card heading

Text should remain editable while preserving structure.

---

# Instance Swap Properties

Instance swap properties allow nested components to be replaced.

Examples:

- Leading icon
- Trailing icon
- Avatar
- Thumbnail

Replacement components should belong to the same category.

---

# Slot Properties

Slots define flexible content regions.

Examples:

- Header
- Footer
- Media
- Actions
- Supporting content

Slots should preserve layout integrity regardless of inserted content.

---

# Default Values

Every property should have a documented default value.

Examples:

Size

Medium

State

Default

Appearance

Primary

Defaults reduce ambiguity.

---

# Variant Naming

Variant names should be semantic.

Good examples:

Primary

Secondary

Success

Danger

Large

Small

Avoid names such as:

Version 2

Blue Button

Final

New

Names should describe purpose rather than appearance.

---

# Variant Combinations

Every variant should represent one unique combination of properties.

Example:

Type = Primary

Size = Medium

State = Hover

Avoid duplicate combinations.

---

# Interactive States

Every interactive component should define states.

Minimum states:

- Default
- Hover
- Focus
- Pressed
- Disabled

Additional states may include:

- Loading
- Selected
- Active
- Error
- Success

Every state should communicate a clear change.

---

# Responsive Behavior

Variants should support responsive layouts.

Examples:

- Compact navigation
- Mobile cards
- Responsive tables

Responsive behavior should preserve usability.

---

# Component API

Treat every component like a public API.

Document:

- Properties
- Variants
- Slots
- Defaults
- Restrictions

A predictable API improves adoption.

---

# AI Component Configuration Engine

Before approving a component, answer:

- Are variants necessary?
- Are properties minimal?
- Are defaults defined?
- Are states documented?
- Are variant names semantic?
- Can developers implement the API consistently?
- Will the component scale without duplication?

If any answer is negative, redesign the configuration.

---

# Validation Checklist

□ Variants documented

□ Properties documented

□ Boolean properties reviewed

□ Text properties documented

□ Instance swap properties reviewed

□ Slot properties validated

□ Default values defined

□ Interactive states completed

□ Responsive behavior documented

□ Component API documented

□ Documentation updated


---

# Component Lifecycle

## Definition

Every component should follow a defined lifecycle.

Lifecycle stages:

- Proposed
- Draft
- In Review
- Approved
- Published
- Deprecated
- Archived

Components should never bypass the review process.

---

# Component Accessibility

Every component must satisfy accessibility requirements.

Review:

- Keyboard navigation
- Focus visibility
- Screen reader compatibility
- Color contrast
- Touch targets
- Reading order

Accessibility is a release requirement.

---

# Component Documentation

Every published component must include documentation.

Documentation should define:

- Purpose
- Usage
- Anatomy
- Properties
- Variants
- States
- Accessibility
- Do
- Don't
- Examples

Documentation should answer common implementation questions.

---

# Design Token Integration

Components should consume design tokens.

Never hardcode:

- Colors
- Typography
- Spacing
- Radius
- Shadows
- Motion

All visual decisions should originate from design tokens.

---

# Component Testing

Every component should be tested.

Testing includes:

- Visual consistency
- Interaction
- Accessibility
- Responsive behavior
- Edge cases
- Content overflow

Testing should occur before publication.

---

# Component Quality Assurance

Review every component for:

- Purpose
- Reusability
- Accessibility
- Scalability
- Consistency
- Documentation
- Performance

Only approved components should enter the library.

---

# Versioning

Every published component should maintain version history.

Track:

- Major updates
- Minor improvements
- Bug fixes
- Breaking changes

Version history improves maintenance.

---

# Deprecation

Deprecated components should remain available temporarily.

Documentation should explain:

- Why the component was deprecated
- Recommended replacement
- Migration guidance
- Planned removal date

Never remove components without a migration path.

---

# Component Ownership

Every component should have an owner.

Owners are responsible for:

- Maintenance
- Documentation
- Reviews
- Quality
- Future improvements

Ownership improves accountability.

---

# Governance

Component governance defines how the library evolves.

Governance should document:

- Review process
- Approval process
- Publishing workflow
- Versioning policy
- Deprecation policy
- Contribution rules

Governance keeps the system consistent.

---

# Contribution Workflow

Every contribution should follow the same process.

Recommended workflow:

Proposal

↓

Research

↓

Design

↓

Accessibility Review

↓

Developer Review

↓

Quality Assurance

↓

Approval

↓

Publication

↓

Documentation Update

No component should skip review.

---

# Naming Standards

Component names should remain semantic.

Examples:

Button

Button Group

Navigation Bar

Input Field

Checkbox

Avoid:

Button Final

Button New

Button Copy

Names should describe purpose.

---

# Publishing Standards

Publish only components that are:

- Reviewed
- Accessible
- Documented
- Tokenized
- Tested
- Approved

Draft components should remain unpublished.

---

# Library Maintenance

Review the component library regularly.

Remove:

- Duplicate components
- Unused components
- Deprecated variants
- Obsolete documentation

Maintenance keeps the library healthy.

---

# AI Component Review Engine

Before approving a component, answer:

- Is the component reusable?
- Is accessibility complete?
- Is documentation complete?
- Are design tokens used?
- Has testing been completed?
- Is version history updated?
- Is governance satisfied?
- Can every team member understand and use this component?

If any answer is negative, revise the component before publication.

---

# Component Principles Checklist

Before publishing:

□ Lifecycle documented

□ Accessibility validated

□ Documentation completed

□ Design tokens integrated

□ Testing completed

□ Quality assurance approved

□ Version history updated

□ Deprecation policy documented

□ Ownership assigned

□ Governance documented

□ Contribution workflow defined

□ Naming standards reviewed

□ Publishing requirements satisfied

□ Library maintenance completed

---

# Key Takeaways

Components are reusable products, not isolated designs.

The AI must:

- Build one reusable solution for one problem.
- Follow a consistent architecture.
- Use semantic properties and variants.
- Consume design tokens.
- Meet accessibility requirements.
- Document every component.
- Test before publishing.
- Govern the library through structured reviews.
- Maintain version history.
- Keep the system scalable for future growth.

Every component should improve consistency, usability, maintainability, and implementation quality.