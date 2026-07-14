---
title: Data Management Patterns
version: 1.0.0
status: Stable
owner: Design System Skill
category: Patterns
priority: Critical
last_updated: 2026-07-14

inherits:
  - ./Pattern Principles.md
  - ../01-Foundation/Accessibility.md
  - ../01-Foundation/User Flows.md
  - ../01-Foundation/Information Architecture.md
  - ../01-Foundation/Responsive Design.md
  - ../05-Components/Inputs & Forms.md
  - ../05-Components/Buttons.md
  - ../05-Components/Data Visualization Components.md
  - ../05-Components/Feedback Components.md
  - ../05-Components/Navigation Components.md
  - ../05-Components/Modals, Dialogs & Drawers.md
---

# Data Management Patterns

## Purpose

This module teaches the AI how to design reliable, secure, and scalable workflows for managing data.

Data management should help users create, update, organize, and maintain information with confidence.

---

# Definition

Data management is the collection of workflows used to create, view, edit, organize, duplicate, archive, restore, and remove information.

Every workflow should preserve data integrity.

---

# Objectives

After completing this module, the AI should be able to:

- Design reliable CRUD workflows
- Prevent accidental data loss
- Improve editing efficiency
- Support large datasets
- Maintain consistency
- Scale across products

---

# Data Management Philosophy

Every workflow should answer:

- What information is being managed?
- What action is the user performing?
- What changes will occur?
- Can the action be reversed?

Users should remain in control of their data.

---

# Core Principles

Always:

- Preserve user work.
- Confirm destructive actions.
- Save progress appropriately.
- Explain important changes.
- Reuse existing components.
- Support accessibility.

Never:

- Lose user input.
- Hide destructive actions.
- Remove recovery options.
- Surprise users with permanent changes.
- Duplicate interaction patterns unnecessarily.

---

# Data Lifecycle

Every workflow should define:

- Create
- Read
- Update
- Save
- Review
- Archive
- Restore
- Delete

Each stage should be predictable.

---

# Common Data Operations

Typical operations include:

- Create
- View
- Edit
- Duplicate
- Archive
- Restore
- Delete
- Import
- Export
- Bulk update

Choose operations appropriate for the product.

---

# Pattern Composition

Data management should reuse existing components.

Examples:

- Forms
- Tables
- Cards
- Buttons
- Menus
- Dialogs
- Feedback components
- Navigation

Avoid creating workflow-specific components when reusable components already exist.

---

# Success Metrics

Measure data management using:

- Task completion rate
- Save success rate
- Error rate
- Recovery rate
- Time to completion
- User confidence

Measure successful outcomes instead of clicks.

---

# AI Decision Rules

Before approving a data management workflow, answer:

- Does it protect user data?
- Can changes be recovered?
- Is accessibility supported?
- Does it reuse existing components?
- Is the workflow predictable?
- Can developers implement this consistently?

If any answer is negative, redesign the workflow.

---

# Validation Checklist

□ Purpose documented

□ Data lifecycle documented

□ Common operations documented

□ Component composition documented

□ Success metrics documented

□ Accessibility reviewed

□ Documentation updated