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

---

# Data Management Workflows

## Philosophy

Every data management workflow should preserve user confidence.

Users should always understand:

- What action they are performing
- What data will change
- Whether the action can be reversed
- What happens next

Data should never disappear unexpectedly.

---

# Create

## Purpose

Create a new record.

Typical flow:

- Start creation
- Enter required information
- Validate input
- Save
- Confirm success
- Open created record when appropriate

Only request required information.

---

# View

## Purpose

Display information clearly.

Views should:

- Prioritize important information
- Support scanning
- Provide related actions
- Preserve context

Reading data should require minimal effort.

---

# Edit

## Purpose

Modify existing information.

Requirements:

- Prefilled values
- Clear editable fields
- Validation
- Save or cancel actions

Users should never lose existing information unintentionally.

---

# Save

## Purpose

Persist user changes.

Requirements:

- Clear save action
- Immediate feedback
- Preserve user input on failure
- Prevent duplicate submissions

Every save should communicate its outcome.

---

# Autosave

## Purpose

Reduce accidental data loss.

Use autosave when:

- Editing long content
- Creating documents
- Drafting messages
- Writing notes

Avoid mixing explicit save and autosave within the same form.

---

# Duplicate

## Purpose

Create a copy of an existing record.

Duplicate:

- Content
- Structure
- Configuration

Do not duplicate unique identifiers.

---

# Delete

## Purpose

Remove information.

Requirements:

- Confirmation for destructive actions
- Explain consequences
- Undo when supported
- Permanent deletion only when necessary

Delete should never be accidental.

---

# Archive

## Purpose

Hide inactive information without deleting it.

Archived records should:

- Remain recoverable
- Be clearly identified
- Be excluded from active views by default

Archive instead of deleting whenever practical.

---

# Restore

## Purpose

Return archived information to active use.

Restore should:

- Preserve original data
- Return to the appropriate location
- Confirm completion

Recovery should be simple.

---

# Import

## Purpose

Bring external data into the product.

Requirements:

- Supported formats
- Validation
- Error reporting
- Import preview when appropriate

Prevent duplicate imports when possible.

---

# Export

## Purpose

Allow users to retrieve their data.

Examples:

- CSV
- Excel
- PDF
- JSON

Exports should preserve important information.

---

# Bulk Operations

## Purpose

Perform actions on multiple records.

Examples:

- Delete
- Archive
- Restore
- Update status
- Assign ownership

Always communicate the number of affected records.

---

# Data Management Selection Guide

Use:

Create

For new records.

View

For reading information.

Edit

For modifying existing information.

Save

For explicit persistence.

Autosave

For long-form editing.

Duplicate

For reusable records.

Archive

For reversible removal.

Delete

For permanent removal.

Import

For external data.

Export

For sharing or backup.

Bulk Operations

For repeated actions across multiple records.

---

# Workflow Variants

Represent workflows as reusable patterns.

Recommended properties:

Operation

- Create
- View
- Edit
- Save
- Duplicate
- Delete
- Archive
- Restore
- Import
- Export
- Bulk

State

- Default
- Editing
- Saving
- Success
- Error
- Archived

Platform

- Web
- Mobile
- Desktop

Avoid duplicate CRUD workflows.

---

# Responsive Behavior

Desktop

- Multi-panel layouts
- Side-by-side editing
- Large tables

Tablet

- Adaptive forms
- Expandable panels

Mobile

- Single-column forms
- Bottom sheets
- Progressive editing

Workflow logic should remain consistent across platforms.

---

# AI Data Management Selection Engine

Before selecting a workflow, answer:

- Does this protect user data?
- Is recovery available?
- Are destructive actions confirmed?
- Is accessibility supported?
- Does this reuse existing components?
- Can this scale across products?

If any answer is negative, redesign the workflow.

---

# Validation Checklist

□ Create documented

□ View documented

□ Edit documented

□ Save documented

□ Autosave documented

□ Duplicate documented

□ Delete documented

□ Archive documented

□ Restore documented

□ Import documented

□ Export documented

□ Bulk operations documented

□ Responsive behavior documented

---

# Data Integrity Workflows

## Philosophy

Users should never wonder whether their work is safe.

Every editing workflow should communicate:

- Current status
- Save status
- Synchronization status
- Recovery options

Users should remain confident throughout editing.

---

# Drafts

## Purpose

Allow users to work before publishing or finalizing.

Drafts should:

- Save progress
- Remain editable
- Support review
- Support publishing

Drafts reduce pressure during creation.

---

# Unsaved Changes

## Purpose

Protect users from accidental data loss.

Requirements:

- Detect modifications
- Warn before leaving
- Preserve entered information
- Offer save or discard actions

Never discard changes silently.

---

# Validation

## Purpose

Ensure submitted data is accurate.

Validation should:

- Prevent invalid submissions
- Explain errors clearly
- Preserve valid input
- Support correction

Validation should help rather than punish.

---

# Conflict Resolution

## Purpose

Handle simultaneous edits safely.

Users should understand:

- What changed
- Who changed it
- Available options

Never overwrite data without warning.

---

# Version History

## Purpose

Allow users to review and restore previous versions.

Version history should display:

- Timestamp
- Author
- Summary of changes
- Restore action

Previous versions should remain recoverable.

---

# Audit Log

## Purpose

Record important system actions.

Typical events:

- Record created
- Record updated
- Record deleted
- Permission changed
- Status changed

Audit logs improve accountability.

---

# Data Synchronization

## Purpose

Keep information consistent across devices.

Synchronization should:

- Preserve edits
- Detect conflicts
- Recover gracefully
- Communicate status

Synchronization should feel automatic.

---

# Offline Editing

## Purpose

Allow work without a network connection.

Requirements:

- Local storage
- Queue pending changes
- Synchronize when online
- Resolve conflicts when needed

Users should continue working whenever possible.

---

# Merge Conflicts

## Purpose

Resolve conflicting edits.

Provide:

- Side-by-side comparison
- Difference highlighting
- Manual selection
- Final confirmation

Users should control the final outcome.

---

# Record Locking

## Purpose

Prevent conflicting edits for sensitive records.

Examples:

- Financial transactions
- Legal records
- Administrative settings

Communicate when a record is locked and why.

---

# Ownership Transfer

## Purpose

Move responsibility from one user to another.

Examples:

- Project reassignment
- Customer ownership
- Team transfer

Transfers should preserve history and permissions.

---

# Data Integrity Selection Guide

Use:

Drafts

For unfinished work.

Unsaved Changes

To prevent accidental loss.

Validation

For input accuracy.

Conflict Resolution

For collaborative editing.

Version History

For recovery.

Audit Log

For accountability.

Data Synchronization

For multi-device usage.

Offline Editing

For unreliable networks.

Merge Conflicts

For simultaneous edits.

Record Locking

For sensitive records.

Ownership Transfer

For reassignment workflows.

---

# Workflow Variants

Represent integrity workflows as reusable patterns.

Recommended properties:

Workflow

- Draft
- Validation
- Sync
- Conflict
- Version
- Audit
- Offline
- Lock

State

- Default
- Editing
- Saving
- Synced
- Conflict
- Offline
- Error

Platform

- Web
- Mobile
- Desktop

Avoid duplicate integrity workflows.

---

# Responsive Behavior

Desktop

- Side-by-side comparisons
- Full version history
- Rich audit tables

Tablet

- Adaptive layouts
- Expandable history panels

Mobile

- Simplified comparisons
- Timeline history
- Compact synchronization indicators

Workflow behavior should remain consistent across platforms.

---

# AI Data Integrity Engine

Before approving a workflow, answer:

- Can users recover lost work?
- Are conflicts handled safely?
- Is version history available?
- Is accessibility supported?
- Does this reuse existing components?
- Can this scale across products?

If any answer is negative, redesign the workflow.

---

# Validation Checklist

□ Drafts documented

□ Unsaved changes documented

□ Validation documented

□ Conflict resolution documented

□ Version history documented

□ Audit log documented

□ Data synchronization documented

□ Offline editing documented

□ Merge conflicts documented

□ Record locking documented

□ Ownership transfer documented

□ Responsive behavior documented