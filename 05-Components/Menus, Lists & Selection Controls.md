---
title: Menus, Lists & Selection Controls
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
  - ../02-Visual-System/Spacing & Sizing.md
  - ../02-Visual-System/Iconography.md
  - ./Component Principles.md
---

# Menus, Lists & Selection Controls

## Purpose

This module teaches the AI how to design scalable, reusable, accessible, and production-ready menus, lists, and selection controls.

These components help users discover options, navigate content, and make choices.

---

# Definition

Menus present available actions.

Lists organize related content.

Selection controls allow users to choose one or multiple options.

---

# Objectives

After completing this module, the AI should be able to:

- Design reusable menu systems
- Build scalable list components
- Create accessible selection controls
- Improve discoverability
- Support responsive layouts
- Improve developer implementation
- Scale across products

---

# Component Philosophy

Every component should answer:

- What choice is being presented?
- How many options may be selected?
- What happens after selection?

Selection should always be predictable.

---

# Core Principles

Always:

- Keep choices clear.
- Group related options.
- Use consistent spacing.
- Support keyboard interaction.
- Maintain accessibility.
- Design reusable components.

Never:

- Overload menus.
- Hide important actions.
- Mix unrelated options.
- Create ambiguous labels.
- Duplicate similar components.

---

# Why These Components Exist

Menus, lists, and selection controls help users:

- Navigate interfaces
- Choose options
- Trigger actions
- Filter information
- Configure settings
- Complete forms

These components reduce decision effort.

---

# Component Anatomy

Every component should define:

- Container
- Label
- Supporting text
- Icon when applicable
- Selection indicator
- Action area
- Optional metadata

Each element should have one responsibility.

---

# Labels

Labels should:

- Clearly describe the option
- Remain concise
- Avoid ambiguity

Users should understand every option before selecting it.

---

# Supporting Information

Supporting content may include:

- Description
- Status
- Shortcut
- Count
- Metadata

Only include information that improves decision making.

---

# Selection Indicators

Selection indicators communicate state.

Examples:

- Checkmark
- Radio indicator
- Switch thumb
- Active highlight

Selection should always remain visible.

---

# Information Hierarchy

Prioritize:

- Primary label
- Selection state
- Supporting information
- Secondary metadata

Hierarchy should improve scanning.

---

# AI Decision Rules

Before approving a component, answer:

- Is the choice clear?
- Is the correct selection pattern used?
- Is accessibility supported?
- Is the component reusable?
- Is responsiveness supported?
- Can developers implement it consistently?

If any answer is negative, redesign the component.

---

# Validation Checklist

□ Purpose documented

□ Anatomy documented

□ Labels documented

□ Supporting information documented

□ Selection indicators documented

□ Accessibility reviewed

□ Documentation updated


---

# Component Types

## Philosophy

Every menu, list, and selection control should belong to one reusable component family.

Different component types solve different interaction problems while sharing the same design language.

Avoid creating duplicate components.

---

# Dropdown Menu

## Purpose

Display a list of actions or options.

Examples:

- Account menu
- Sort options
- Filter options
- Overflow actions

Dropdown menus should remain compact.

---

# Context Menu

## Purpose

Display actions related to a selected object.

Examples:

- Right-click menu
- File actions
- Table row actions
- Image actions

Context menus should appear near the triggering element.

---

# Command Menu

## Purpose

Provide fast access to commands.

Examples:

- Search commands
- Navigation
- Quick actions
- Keyboard shortcuts

Command menus should prioritize speed.

---

# Action Menu

## Purpose

Present a small set of related actions.

Examples:

- Edit
- Share
- Duplicate
- Delete

Actions should remain concise.

---

# Navigation Menu

## Purpose

Help users move between sections.

Examples:

- Sidebar
- Top navigation
- Mobile navigation
- Settings navigation

Navigation should remain predictable.

---

# List View

## Purpose

Display structured collections.

Examples:

- Files
- Messages
- Contacts
- Tasks

Lists should support efficient scanning.

---

# Checkbox

## Purpose

Allow multiple selections.

Examples:

- Filters
- Permissions
- Settings
- Preferences

Checkboxes support zero, one, or many selections.

---

# Radio Button

## Purpose

Allow one selection from multiple options.

Examples:

- Payment method
- Theme
- Language
- Shipping option

Only one option may remain selected.

---

# Switch

## Purpose

Toggle a setting immediately.

Examples:

- Dark mode
- Notifications
- Privacy settings
- Location services

Switches represent immediate state changes.

---

# Segmented Control

## Purpose

Switch between related views.

Examples:

- Grid or List
- Monthly or Yearly
- Personal or Team

Segmented controls should contain a small number of options.

---

# Chip

## Purpose

Represent compact information or selections.

Examples:

- Filter chip
- Choice chip
- Input chip
- Status chip

Chips should remain concise.

---

# Selection Guide

Use:

Dropdown Menu

For multiple actions.

Context Menu

For object-specific actions.

Command Menu

For keyboard-driven workflows.

Navigation Menu

For moving between sections.

List View

For collections.

Checkbox

For multiple selections.

Radio Button

For single selection.

Switch

For immediate on or off settings.

Segmented Control

For switching between views.

Chip

For compact selections or filters.

---

# Component Variants

Represent these patterns as variants.

Recommended properties:

Type

- Dropdown
- Context
- Command
- Action
- Navigation
- List
- Checkbox
- Radio
- Switch
- Segmented
- Chip

State

- Default
- Hover
- Focus
- Pressed
- Selected
- Disabled

Avoid creating duplicate component sets.

---

# Responsive Behavior

Desktop

- Dropdown
- Context menu
- Sidebar navigation

Tablet

- Dropdown
- Navigation drawer
- List

Mobile

- Bottom sheet menu
- List
- Segmented control
- Chips

Choose the pattern that best fits the device.

---

# AI Selection Engine

Before selecting a component, answer:

- Is the correct selection pattern used?
- How many options may users select?
- Is the interaction predictable?
- Is accessibility supported?
- Is responsiveness supported?
- Can this remain part of one reusable component family?

If any answer is negative, choose a more appropriate component.

---

# Validation Checklist

□ Dropdown menu documented

□ Context menu documented

□ Command menu documented

□ Action menu documented

□ Navigation menu documented

□ List view documented

□ Checkbox documented

□ Radio button documented

□ Switch documented

□ Segmented control documented

□ Chip documented

□ Variant strategy documented

□ Responsive behavior documented


---

# Component States

## Philosophy

Every interactive component should clearly communicate its current state.

Users should immediately understand:

- Whether the component is interactive
- Whether it is selected
- Whether it is disabled
- What will happen after interaction

States should remain consistent across every component.

---

# Default State

The component is available for interaction.

Requirements:

- Clear label
- Visible boundaries when appropriate
- Readable content

Default should establish the baseline appearance.

---

# Hover State

Hover communicates interactivity.

Examples:

- Background change
- Border change
- Elevation
- Icon color update

Hover should never hide important information.

---

# Focus State

Focus supports keyboard users.

Requirements:

- High visibility
- High contrast
- Consistent appearance

Never remove focus indicators.

---

# Pressed State

Pressed confirms interaction.

Examples:

- Reduced elevation
- Slight color change
- Scale adjustment

Pressed feedback should feel immediate.

---

# Selected State

Selection should remain obvious.

Visual indicators may include:

- Checkmark
- Filled radio indicator
- Active background
- Accent border

Selection should never rely only on color.

---

# Disabled State

Disabled components communicate temporary unavailability.

Requirements:

- Reduced emphasis
- Readable labels
- No interaction

Explain unavailable actions whenever appropriate.

---

# Indeterminate Checkbox

Indeterminate checkboxes communicate partial selection.

Examples:

- Parent folders
- Group permissions
- Multi-select lists

Indeterminate is neither selected nor unselected.

---

# Nested Menus

Nested menus organize related actions.

Requirements:

- Clear hierarchy
- Visible parent item
- Predictable expansion
- Easy dismissal

Avoid excessive nesting.

---

# Multi-select Lists

Multi-select lists support selecting multiple records.

Examples:

- Users
- Files
- Products
- Categories

Selection should remain visible during scrolling.

---

# Searchable Lists

Large lists should support searching.

Requirements:

- Fast filtering
- Matching highlights when appropriate
- Clear empty state

Search should reduce scanning effort.

---

# Virtualized Lists

Large datasets should use virtualization.

Recommended for:

- Thousands of records
- Enterprise software
- Admin dashboards

Virtualization should remain invisible to users.

---

# Keyboard Navigation

Menus and lists should support:

- Arrow keys
- Tab
- Shift + Tab
- Enter
- Escape
- Space where appropriate

Navigation should remain predictable.

---

# Motion

Motion should reinforce understanding.

Examples:

- Menu expansion
- Menu collapse
- Chip removal
- Switch transition
- List expansion

Motion should communicate relationships.

Avoid decorative animation.

---

# Responsive Behavior

Desktop

- Dropdown menus
- Context menus
- Navigation menus

Tablet

- Drawers
- Lists
- Segmented controls

Mobile

- Bottom sheets
- Lists
- Chips
- Full-width selectors

Components should remain easy to use across devices.

---

# AI Interaction Engine

Before approving interaction behavior, answer:

- Is selection obvious?
- Is keyboard navigation complete?
- Is hierarchy clear?
- Is accessibility supported?
- Does motion improve understanding?
- Is responsiveness maintained?

If any answer is negative, redesign the interaction.

---

# Validation Checklist

□ Component states documented

□ Hover state documented

□ Focus state documented

□ Pressed state documented

□ Selected state documented

□ Disabled state documented

□ Indeterminate checkbox documented

□ Nested menus documented

□ Multi-select lists documented

□ Searchable lists documented

□ Virtualized lists documented

□ Keyboard navigation documented

□ Motion documented

□ Responsive behavior validated