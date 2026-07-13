---
title: Advanced Components
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
  - ../01-Foundation/Responsive Design.md
  - ../02-Visual-System/Typography.md
  - ../02-Visual-System/Iconography.md
  - ../02-Visual-System/Spacing & Sizing.md
  - ./Component Principles.md
---

# Advanced Components

## Purpose

This module teaches the AI how to design scalable, reusable, accessible, and production-ready advanced components.

Advanced components combine multiple UI components into complete interaction systems.

---

# Definition

Advanced components solve complex user tasks through coordinated interactions.

Examples include:

- Command palettes
- AI assistants
- Chat interfaces
- Calendars
- Schedulers
- Kanban boards
- Rich text editors
- Maps
- Onboarding flows

These components combine multiple reusable building blocks.

---

# Objectives

After completing this module, the AI should be able to:

- Design reusable advanced components
- Combine component families consistently
- Support accessibility
- Improve developer implementation
- Maintain scalability
- Reduce design duplication

---

# Advanced Component Philosophy

Every advanced component should answer:

- What user goal does this solve?
- Which reusable components compose it?
- Can it scale across products?

Complexity should never reduce usability.

---

# Core Principles

Always:

- Reuse existing components.
- Maintain consistency.
- Support accessibility.
- Follow platform conventions.
- Document interactions.
- Design for scalability.

Never:

- Duplicate existing components.
- Create inconsistent interactions.
- Ignore accessibility.
- Hide critical functionality.
- Introduce unnecessary complexity.

---

# Why Advanced Components Exist

Advanced components help users:

- Complete complex workflows
- Manage large datasets
- Collaborate
- Create content
- Schedule work
- Navigate sophisticated applications

Every advanced component should simplify complex tasks.

---

# Component Anatomy

Every advanced component should define:

- Container
- Header
- Content area
- Primary actions
- Secondary actions
- Status indicators
- Supporting controls
- Empty states

Each element should have a defined responsibility.

---

# Composition

Advanced components should be built from existing component families.

Examples:

- Buttons
- Inputs
- Cards
- Navigation
- Tables
- Menus
- Media
- Data visualizations

Avoid rebuilding solved patterns.

---

# Hierarchy

Prioritize:

- Primary workflow
- Core content
- Supporting actions
- Secondary information

Hierarchy should guide attention naturally.

---

# AI Decision Rules

Before approving an advanced component, answer:

- Does this reuse existing components?
- Is interaction predictable?
- Is accessibility supported?
- Is responsiveness supported?
- Is implementation scalable?
- Can developers maintain this consistently?

If any answer is negative, redesign the component.

---

# Validation Checklist

□ Purpose documented

□ Anatomy documented

□ Component composition documented

□ Hierarchy documented

□ Accessibility reviewed

□ Responsive behavior reviewed

□ Documentation updated

---

# Advanced Component Types

## Philosophy

Every advanced component should belong to one reusable component family.

Each pattern should solve a complete user workflow while reusing existing foundational components.

Avoid creating duplicate interaction systems.

---

# Command Palette

## Purpose

Provide fast keyboard-driven access to commands, navigation, and search.

Examples:

- Search pages
- Run actions
- Open settings
- Navigate resources

Command palettes should minimize navigation effort.

---

# AI Assistant

## Purpose

Help users complete tasks through conversational interaction.

Examples:

- Writing assistance
- Data analysis
- Workflow automation
- Customer support

AI assistants should always communicate their current status.

---

# Chat Interface

## Purpose

Support real-time or asynchronous conversations.

Examples:

- Team messaging
- Customer support
- AI conversations
- Collaboration

Messages should remain easy to scan.

---

# Calendar

## Purpose

Display events across time.

Examples:

- Meetings
- Deadlines
- Reservations
- Appointments

Calendars should communicate availability clearly.

---

# Scheduler

## Purpose

Manage resources across time.

Examples:

- Staff scheduling
- Equipment booking
- Shift planning
- Project planning

Schedulers should support large datasets.

---

# Kanban Board

## Purpose

Organize work visually.

Examples:

- Agile projects
- Task management
- Recruitment pipeline
- Sales pipeline

Cards should move predictably between columns.

---

# Rich Text Editor

## Purpose

Create and edit formatted content.

Examples:

- Documentation
- Blog posts
- Notes
- Comments

Formatting tools should remain discoverable.

---

# Maps

## Purpose

Display geographic information.

Examples:

- Store locations
- Delivery tracking
- Navigation
- Asset management

Maps should always provide location context.

---

# Timeline Planner

## Purpose

Display long-term planning.

Examples:

- Product roadmap
- Release planning
- Marketing campaigns
- Project schedules

Timelines should communicate dependencies.

---

# Onboarding Flow

## Purpose

Guide first-time users.

Examples:

- Product introduction
- Feature education
- Account setup
- Personalization

Users should always understand the next step.

---

# Wizard

## Purpose

Guide users through structured multi-step tasks.

Examples:

- Checkout
- Registration
- Configuration
- Data import

Progress should always remain visible.

---

# Workspace Layout

## Purpose

Support complex productivity workflows.

Examples:

- IDE
- Analytics dashboard
- Design tools
- CRM systems

Layouts should support customization when appropriate.

---

# Advanced Component Selection Guide

Use:

Command Palette

For fast navigation and commands.

AI Assistant

For conversational assistance.

Chat Interface

For messaging.

Calendar

For date-based information.

Scheduler

For resource planning.

Kanban Board

For workflow management.

Rich Text Editor

For formatted content.

Maps

For geographic information.

Timeline Planner

For long-term planning.

Onboarding Flow

For new user guidance.

Wizard

For structured workflows.

Workspace Layout

For productivity applications.

---

# Advanced Component Variants

Represent advanced components as variants.

Recommended properties:

Type

- Command Palette
- AI Assistant
- Chat
- Calendar
- Scheduler
- Kanban
- Rich Text
- Maps
- Timeline
- Onboarding
- Wizard
- Workspace

State

- Default
- Hover
- Focus
- Expanded
- Collapsed
- Loading
- Empty
- Error

Size

- Small
- Medium
- Large

Avoid duplicate component sets.

---

# Responsive Behavior

Desktop

- Full workspace layouts
- Multi-pane interfaces
- Rich interactions

Tablet

- Adaptive panels
- Split views
- Responsive controls

Mobile

- Simplified workflows
- Bottom sheets
- Progressive disclosure

Complex workflows should remain usable across all screen sizes.

---

# AI Advanced Component Selection Engine

Before selecting an advanced component, answer:

- Does this solve the complete workflow?
- Does it reuse existing components?
- Is interaction predictable?
- Is accessibility supported?
- Is responsiveness supported?
- Can this remain part of one reusable component family?

If any answer is negative, choose a more appropriate pattern.

---

# Validation Checklist

□ Command palette documented

□ AI assistant documented

□ Chat interface documented

□ Calendar documented

□ Scheduler documented

□ Kanban board documented

□ Rich text editor documented

□ Maps documented

□ Timeline planner documented

□ Onboarding flow documented

□ Wizard documented

□ Workspace layout documented

□ Variant strategy documented

□ Responsive behavior documented


---

# Advanced Component States

## Philosophy

Every advanced component should clearly communicate its current interaction state.

Users should immediately understand:

- What is happening
- What is interactive
- What has changed
- What action is available

Interactions should reduce cognitive effort.

---

# Default State

The component is ready for interaction.

Requirements:

- Stable layout
- Clear actions
- Readable content
- Visible navigation

Default establishes the baseline experience.

---

# Loading State

Loading communicates that work is in progress.

Examples:

- Loading workspace
- Loading messages
- Loading calendar events
- Loading AI responses

Provide skeleton screens whenever possible.

Avoid layout shifts.

---

# Empty State

Empty states explain why content is unavailable.

Examples:

- No conversations
- No tasks
- No calendar events
- No search results

Offer a clear next action.

---

# Error State

Errors should explain:

- What failed
- Why when known
- How users can recover

Examples:

- Retry
- Refresh
- Reconnect
- Contact support

Avoid technical language.

---

# Selection State

Selection should remain obvious.

Examples:

- Selected task
- Selected conversation
- Selected event
- Selected document

Selection should never depend only on color.

---

# Collaboration State

Collaborative components should communicate:

- Active users
- Editing status
- Presence
- Cursor position
- Shared updates

Users should understand when others are collaborating.

---

# Drag and Drop

Advanced workflows may support drag interactions.

Examples:

- Kanban cards
- Calendar events
- Files
- Dashboard widgets

Provide continuous visual feedback.

---

# Keyboard Shortcuts

Support productivity through shortcuts.

Examples:

- Search
- Command palette
- Save
- Undo
- Redo
- Navigation

Document every supported shortcut.

---

# Real-time Updates

Components should communicate live changes.

Examples:

- Incoming messages
- Calendar updates
- Task assignments
- AI responses

Updates should avoid interrupting user workflows.

---

# Offline Behavior

Communicate offline status clearly.

Examples:

- Cached content
- Pending changes
- Synchronization
- Retry actions

Users should understand what is available offline.

---

# Notifications

Advanced workflows may surface contextual notifications.

Examples:

- Assignment completed
- Collaboration request
- Import completed
- AI response available

Notifications should remain relevant and actionable.

---

# Motion

Motion should reinforce workflow changes.

Examples:

- Card movement
- Panel transitions
- AI response animation
- Calendar updates
- Wizard progression

Motion should communicate change.

Avoid decorative animation.

---

# Responsive Behavior

Desktop

- Multi-pane layouts
- Rich editing
- Collaboration

Tablet

- Adaptive panels
- Split layouts
- Responsive controls

Mobile

- Simplified workflows
- Bottom sheets
- Progressive disclosure

Complex workflows should remain usable on every device.

---

# AI Advanced Interaction Engine

Before approving interaction behavior, answer:

- Is the workflow obvious?
- Are state changes clear?
- Is collaboration understandable?
- Is accessibility supported?
- Does motion improve understanding?
- Is responsiveness maintained?

If any answer is negative, redesign the interaction.

---

# Validation Checklist

□ Component states documented

□ Loading state documented

□ Empty state documented

□ Error state documented

□ Selection state documented

□ Collaboration state documented

□ Drag and drop documented

□ Keyboard shortcuts documented

□ Real-time updates documented

□ Offline behavior documented

□ Notifications documented

□ Motion documented

□ Responsive behavior validated


---

# Keyboard Interaction

## Purpose

Every advanced component should fully support keyboard navigation.

Minimum requirements:

- Tab moves focus
- Shift + Tab moves focus backward
- Arrow keys navigate items when applicable
- Enter activates focused controls
- Space activates supported controls
- Escape closes temporary surfaces
- Home moves to the beginning
- End moves to the end

Keyboard interaction should remain predictable.

---

# Focus Management

Focus should:

- Always remain visible
- Follow logical navigation order
- Move into newly opened interfaces
- Return after dismissal
- Never become trapped unless intentionally contained

Never lose keyboard focus.

---

# Screen Reader Support

Advanced components should expose:

- Component role
- Accessible name
- Current state
- Status updates
- Available actions
- Progress when applicable

Users should understand complex workflows without relying on vision.

---

# Accessibility Semantics

Every advanced component should communicate:

- Purpose
- Relationships
- Hierarchy
- Current context
- Active selection

Semantics should accurately describe behavior.

---

# Collaboration Accessibility

Collaborative experiences should expose:

- Active collaborators
- Presence
- Editing status
- Notifications
- Shared updates

Collaboration should remain understandable for every user.

---

# Responsive Adaptation

Desktop

- Multi-panel layouts
- Advanced editing
- Rich workflows

Tablet

- Adaptive panels
- Split layouts
- Touch optimization

Mobile

- Progressive disclosure
- Simplified workflows
- Bottom sheets
- Compact editing

Complex workflows should remain usable across every device.

---

# Design Token Integration

Advanced components should reference design tokens.

Examples:

advanced.spacing

advanced.radius

advanced.shadow

advanced.surface

advanced.focus.ring

advanced.elevation

advanced.motion.duration

advanced.border

Avoid hardcoded values.

---

# Motion Guidelines

Motion should communicate workflow changes.

Examples:

- Panel transitions
- Card movement
- Calendar updates
- AI response generation
- Drag completion
- Wizard progression

Motion should reinforce understanding.

Avoid decorative animation.

---

# Documentation

Every advanced component should document:

- Purpose
- Anatomy
- Component composition
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

Every advanced component should be tested for:

- Accessibility
- Keyboard interaction
- Screen reader compatibility
- Collaboration
- Drag and drop
- Responsive layouts
- Motion
- Performance

Testing should occur before release.

---

# Quality Assurance

Review every advanced component for:

- Accessibility
- Workflow consistency
- Responsive behavior
- Design token usage
- Documentation
- Performance

Only approved components belong in the design system.

---

# Versioning

Track changes for:

- New component patterns
- Accessibility improvements
- Motion updates
- Bug fixes
- Breaking changes

Maintain complete version history.

---

# Governance

Advanced component updates should include:

- UX review
- Accessibility review
- Engineering review
- QA approval
- Documentation update

Governance maintains consistency across products.

---

# AI Advanced Component Review Engine

Before publishing any advanced component, answer:

- Does this reuse existing components?
- Is the workflow intuitive?
- Is accessibility complete?
- Are design tokens used?
- Is keyboard interaction supported?
- Has testing been completed?
- Does this scale across products?
- Is interaction predictable?

If any answer is negative, revise the component.

---

# Advanced Components Checklist

Before publishing:

□ Anatomy documented

□ Component composition documented

□ Variants completed

□ States documented

□ Keyboard interaction verified

□ Focus management documented

□ Screen reader support completed

□ Responsive behavior validated

□ Design tokens integrated

□ Motion documented

□ Testing completed

□ QA approved

□ Version history updated

□ Documentation completed

---

# Key Takeaways

Advanced components combine reusable UI building blocks into complete workflow systems.

The AI must:

- Reuse existing components.
- Preserve workflow consistency.
- Support keyboard navigation.
- Support screen readers.
- Use design tokens.
- Keep motion meaningful.
- Test every interaction.
- Document every behavior.

Every advanced component should improve scalability, accessibility, consistency, and long-term maintainability.