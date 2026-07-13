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

