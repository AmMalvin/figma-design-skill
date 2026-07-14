---
title: Pattern Principles
version: 1.0.0
status: Stable
owner: Design System Skill
category: Patterns
priority: Critical
last_updated: 2026-07-13

inherits:
  - ../00-Core/Universal Design Principles.md
  - ../01-Foundation/Accessibility.md
  - ../01-Foundation/User Flows.md
  - ../01-Foundation/Information Architecture.md
  - ../01-Foundation/Responsive Design.md
  - ../05-Components/Component Principles.md
---

# Pattern Principles

## Purpose

This module teaches the AI how to design complete user experiences using reusable components.

Patterns define repeatable solutions for common user goals rather than individual interface elements.

---

# Definition

A pattern is a reusable solution to a recurring UX problem.

Patterns combine multiple components into one complete workflow.

Examples include:

- Authentication
- Search
- Checkout
- Dashboard
- Settings
- Notifications
- Onboarding
- Content management

---

# Objectives

After completing this module, the AI should be able to:

- Build complete workflows
- Reuse existing components
- Improve usability
- Reduce inconsistency
- Support accessibility
- Scale patterns across products

---

# Pattern Philosophy

Every pattern should answer:

- What user problem is being solved?
- What is the expected outcome?
- Which reusable components are required?
- How does success look?

Patterns should optimize user goals rather than interface complexity.

---

# Core Principles

Always:

- Start with the user's goal.
- Reuse existing components.
- Reduce unnecessary steps.
- Maintain consistency.
- Support accessibility.
- Keep workflows predictable.

Never:

- Duplicate solved workflows.
- Introduce unnecessary decisions.
- Mix unrelated goals.
- Break established interaction models.
- Ignore error recovery.

---

# Relationship Between Components and Patterns

Components answer:

"How does this element behave?"

Patterns answer:

"How do multiple elements solve one complete task?"

Components are building blocks.

Patterns are complete user solutions.

---

# Pattern Characteristics

Every pattern should include:

- User goal
- Entry point
- Workflow
- Decision points
- Success state
- Failure state
- Recovery path
- Exit point

Patterns should always have a clear beginning and end.

---

# Pattern Composition

Patterns should reuse existing components.

Examples:

- Buttons
- Forms
- Cards
- Tables
- Navigation
- Feedback
- Dialogs
- Data visualization

Avoid creating new components inside patterns unless absolutely necessary.

---

# Pattern Consistency

Patterns should remain consistent across:

- Products
- Platforms
- Teams
- Screen sizes

Users should recognize familiar workflows immediately.

---

# Pattern Hierarchy

Prioritize:

- User goal
- Primary task
- Supporting actions
- Secondary information

Hierarchy should reduce cognitive effort.

---

# AI Decision Rules

Before approving any pattern, answer:

- Does this solve one clear user goal?
- Does it reuse existing components?
- Is accessibility supported?
- Is the workflow predictable?
- Is implementation scalable?
- Can developers build this consistently?

If any answer is negative, redesign the pattern.

---

# Validation Checklist

□ Purpose documented

□ User goal documented

□ Workflow documented

□ Component composition documented

□ Accessibility reviewed

□ Responsive behavior reviewed

□ Documentation updated


---

# Pattern Lifecycle

## Philosophy

Every pattern should guide users from beginning to completion.

A complete pattern includes:

- Entry
- Progress
- Decisions
- Completion
- Recovery
- Exit

Users should never feel lost during a workflow.

---

# User Journey

Every pattern begins with a user goal.

Examples:

- Sign in
- Purchase a product
- Upload a file
- Schedule a meeting
- Complete onboarding

Design around the user's objective rather than system requirements.

---

# Entry Points

Entry points define how users begin a workflow.

Examples:

- Primary button
- Navigation
- Search result
- Deep link
- Notification
- QR code

Entry points should clearly communicate what happens next.

---

# Exit Points

Exit points define how users leave a workflow.

Examples:

- Success
- Cancel
- Save and close
- Back
- Logout

Users should always understand the result of leaving.

---

# Happy Path

The happy path represents the simplest successful journey.

Characteristics:

- Minimum steps
- No errors
- Clear progression
- Successful completion

Optimize the happy path before edge cases.

---

# Alternate Paths

Users do not always follow the expected route.

Examples:

- Skip onboarding
- Return later
- Change selections
- Edit information
- Repeat a step

Alternate paths should remain predictable.

---

# Decision Points

Decision points require user choice.

Examples:

- Select a payment method
- Choose a subscription
- Confirm deletion
- Pick a delivery option

Present only the information needed for the decision.

---

# Progressive Disclosure

Reveal information only when needed.

Examples:

- Advanced settings
- Optional fields
- Additional filters
- Expanded details

Reduce cognitive load by avoiding unnecessary information.

---

# Error Recovery

Every pattern should include recovery.

Examples:

- Retry
- Undo
- Reset
- Edit input
- Restore progress

Errors should never block user progress permanently.

---

# Success State

Success confirms completion.

Examples:

- Confirmation message
- Receipt
- Success screen
- Updated dashboard

Clearly communicate what happened and what users can do next.

---

# Pattern Composition

Patterns should combine reusable components.

Examples:

- Navigation
- Forms
- Buttons
- Dialogs
- Cards
- Tables
- Feedback
- Media

Never recreate components inside a pattern.

---

# Pattern Scalability

Patterns should adapt across:

- Products
- Teams
- Platforms
- Screen sizes
- Languages

Scalability should not change workflow logic.

---

# AI Pattern Evaluation Engine

Before approving a pattern, answer:

- Does this solve one user goal?
- Is the workflow complete?
- Are decision points obvious?
- Is recovery possible?
- Does it reuse existing components?
- Can this scale across products?

If any answer is negative, redesign the pattern.

---

# Validation Checklist

□ Pattern lifecycle documented

□ User journey documented

□ Entry points documented

□ Exit points documented

□ Happy path documented

□ Alternate paths documented

□ Decision points documented

□ Progressive disclosure documented

□ Error recovery documented

□ Success state documented

□ Pattern composition documented

□ Pattern scalability documented

---

# Pattern States

## Philosophy

Every pattern should communicate its current workflow state.

Users should immediately understand:

- Where they are
- What is happening
- What action is required
- What happens next

Workflow states should reduce uncertainty.

---

# Loading Pattern

Loading patterns communicate progress while preparing content.

Examples:

- Authentication
- Dashboard loading
- Search
- Checkout
- AI response generation

Requirements:

- Stable layout
- Skeleton screens when possible
- Progress indicators when appropriate

Avoid unnecessary waiting.

---

# Empty Pattern

Empty patterns explain the absence of content.

Examples:

- No notifications
- No search results
- No uploaded files
- No scheduled events

Every empty pattern should provide a meaningful next action.

---

# Error Pattern

Every workflow should include recovery.

Errors should communicate:

- What happened
- Why when known
- How users recover

Examples:

- Retry
- Edit input
- Restore connection
- Contact support

Errors should never permanently block progress.

---

# Confirmation Pattern

Confirmation patterns reassure users after important actions.

Examples:

- Purchase completed
- Password updated
- File uploaded
- Booking confirmed

Communicate:

- What happened
- What happens next
- Available follow-up actions

---

# Undo Pattern

Whenever possible, allow users to reverse recent actions.

Examples:

- Delete
- Archive
- Move
- Remove
- Dismiss

Undo reduces the impact of mistakes.

---

# Multi-step Workflow

Complex workflows should divide work into manageable steps.

Examples:

- Registration
- Checkout
- Tax filing
- Product configuration

Requirements:

- Visible progress
- Current step
- Previous step
- Next step

Users should always know their progress.

---

# Conditional Flow

Some workflows depend on user choices.

Examples:

- Payment method
- Shipping option
- Business account
- Personal account

Only reveal relevant steps.

---

# Interrupted Journey

Users may leave before completion.

Examples:

- App closed
- Connection lost
- Incoming phone call
- Browser refresh

Patterns should preserve progress whenever possible.

---

# Resumable Journey

Users should resume unfinished work.

Examples:

- Draft forms
- Checkout
- Onboarding
- Applications

Restore users to their previous step whenever possible.

---

# Pattern Consistency

Every workflow should maintain:

- Navigation
- Feedback
- Terminology
- Interaction model
- Component usage

Consistency reduces learning effort.

---

# AI Workflow Evaluation Engine

Before approving a workflow, answer:

- Does every state exist?
- Can users recover from errors?
- Can users resume progress?
- Are confirmations clear?
- Does the workflow reuse existing components?
- Can this scale across products?

If any answer is negative, redesign the workflow.

---

# Pattern Quality Checklist

□ Loading pattern documented

□ Empty pattern documented

□ Error pattern documented

□ Confirmation pattern documented

□ Undo pattern documented

□ Multi-step workflow documented

□ Conditional flow documented

□ Interrupted journey documented

□ Resumable journey documented

□ Pattern consistency documented

□ AI workflow evaluation documented


---

# Accessibility Across Workflows

## Purpose

Every pattern should remain accessible from beginning to completion.

Accessibility should exist throughout the entire workflow rather than individual screens.

---

# Keyboard Navigation

Patterns should support complete keyboard navigation.

Requirements:

- Logical tab order
- Visible focus
- Keyboard shortcuts when appropriate
- Escape for temporary interfaces
- Enter for primary actions

Users should complete every workflow without a mouse.

---

# Focus Management

Focus should:

- Move logically
- Remain visible
- Enter temporary interfaces
- Return after dismissal
- Never become trapped unless intentionally contained

Focus should always reflect user context.

---

# Screen Reader Guidance

Patterns should expose:

- Workflow purpose
- Current step
- Available actions
- Progress
- Errors
- Success messages

Users should understand where they are at every stage.

---

# Workflow Accessibility

Every workflow should support:

- Keyboard navigation
- Screen readers
- High contrast
- Reduced motion
- Responsive layouts
- Zoom

Accessibility should remain consistent across the entire journey.

---

# Responsive Workflows

Patterns should adapt across:

Desktop

- Full workflows
- Multi-panel layouts
- Advanced productivity

Tablet

- Adaptive layouts
- Split views
- Touch optimization

Mobile

- Simplified flows
- Progressive disclosure
- Bottom sheets
- Thumb-friendly interactions

Workflow logic should remain unchanged across devices.

---

# Design Token Integration

Patterns should reference design tokens instead of hardcoded values.

Examples:

pattern.spacing

pattern.radius

pattern.elevation

pattern.motion.duration

pattern.focus.ring

pattern.success.color

pattern.error.color

pattern.warning.color

Avoid hardcoded styling.

---

# Documentation Standards

Every pattern should document:

- Purpose
- User goal
- Entry point
- Exit point
- Workflow
- Decision points
- States
- Accessibility
- Responsive behavior
- Components used
- Usage guidelines
- Do
- Don't
- Examples

Documentation should remove implementation ambiguity.

---

# Testing Strategy

Every pattern should be tested for:

- Accessibility
- Keyboard navigation
- Screen reader compatibility
- Responsive layouts
- Error recovery
- Alternate paths
- Performance
- User completion

Testing should validate the complete workflow.

---

# Quality Assurance

Review every pattern for:

- User goal alignment
- Workflow consistency
- Accessibility
- Component reuse
- Responsive behavior
- Documentation
- Performance

Only approved patterns belong in the design system.

---

# Versioning

Track changes for:

- New workflows
- Accessibility improvements
- Workflow refinements
- Bug fixes
- Breaking changes

Maintain complete version history.

---

# Governance

Pattern updates should include:

- UX review
- Accessibility review
- Engineering review
- QA approval
- Documentation update

Governance ensures long-term consistency.

---

# AI Pattern Review Engine

Before publishing any pattern, answer:

- Does this solve one user goal?
- Does it reuse existing components?
- Is accessibility complete?
- Are design tokens used?
- Is keyboard navigation supported?
- Has testing been completed?
- Does this scale across products?
- Is the workflow predictable?

If any answer is negative, revise the pattern.

---

# Pattern Principles Checklist

Before publishing:

□ User goal documented

□ Workflow documented

□ Entry and exit points documented

□ Decision points documented

□ Pattern states documented

□ Accessibility completed

□ Keyboard navigation verified

□ Screen reader support completed

□ Responsive behavior validated

□ Design tokens integrated

□ Testing completed

□ QA approved

□ Version history updated

□ Documentation completed

---

# Key Takeaways

Patterns define complete user journeys built from reusable components.

The AI must:

- Start with the user's goal.
- Reuse existing components.
- Keep workflows predictable.
- Support keyboard navigation.
- Support screen readers.
- Use design tokens.
- Test complete workflows.
- Document every decision.
- Design for scalability.

Every pattern should improve usability, accessibility, consistency, and long-term maintainability across every product built with the design system.