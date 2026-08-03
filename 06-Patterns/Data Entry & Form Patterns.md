---
title: Data Entry & Form Patterns
version: 1.0.0
status: Stable
owner: Design System Skill
category: Patterns
priority: Critical
last_updated: 2026-07-15

inherits:
  - ./Pattern Principles.md
  - ../01-Foundation/Accessibility.md
  - ../01-Foundation/User Flows.md
  - ../01-Foundation/Information Architecture.md
  - ../01-Foundation/Responsive Design.md
  - ../05-Components/Inputs & Forms.md
  - ../05-Components/Buttons.md
  - ../05-Components/Feedback Components.md
  - ../05-Components/Data Display.md
  - ../05-Components/Modals, Dialogs & Drawers.md
---

# Data Entry & Form Patterns

## Purpose

This module teaches the AI how to design efficient, accessible, and scalable data entry workflows.

Forms should reduce effort while improving data quality.

---

# Definition

Data entry patterns define how users provide, edit, validate, review, and submit information.

They include simple forms, complex enterprise workflows, multi-step processes, and collaborative data entry.

---

# Objectives

After completing this module, the AI should be able to:

- Design efficient forms
- Reduce completion time
- Prevent errors
- Improve data quality
- Support accessibility
- Scale forms across products

---

# Form Philosophy

Every form should answer:

- What information is required?
- Why is it needed?
- How can effort be reduced?
- How can errors be prevented?
- What happens after submission?

Forms should help users complete tasks confidently.

---

# Core Principles

Always:

- Ask only for necessary information.
- Organize fields logically.
- Reduce typing whenever possible.
- Reuse existing components.
- Support accessibility.
- Preserve user progress.

Never:

- Request unnecessary data.
- Overwhelm users with long forms.
- Hide validation rules.
- Lose entered information.
- Duplicate workflows.

---

# Form Lifecycle

Every workflow should define:

- Entry
- Data collection
- Validation
- Review
- Submission
- Confirmation

Each stage should remain predictable.

---

# Form Types

Common form models include:

- Single-page form
- Multi-step form
- Wizard
- Inline editing
- Bulk editing
- Dynamic form
- Enterprise data entry

Choose the form model based on task complexity.

---

# Pattern Composition

Forms should reuse existing components.

Examples:

- Text fields
- Dropdowns
- Checkboxes
- Radio buttons
- Date pickers
- Upload controls
- Buttons
- Progress indicators
- Error messages

Avoid creating form-specific components when reusable components already exist.

---

# Success Metrics

Measure forms using:

- Completion rate
- Completion time
- Error rate
- Validation rate
- Abandonment rate
- User satisfaction

Measure successful task completion rather than submission volume.

---

# AI Decision Rules

Before approving a form workflow, answer:

- Does this reduce user effort?
- Is only necessary data requested?
- Is accessibility supported?
- Does this reuse existing components?
- Is validation clear?
- Can developers implement this consistently?

If any answer is negative, redesign the workflow.

---

# Validation Checklist

□ Purpose documented

□ Form lifecycle documented

□ Form types documented

□ Component composition documented

□ Success metrics documented

□ Accessibility reviewed

□ Documentation updated

---

# Form Completion & Submission

## Philosophy

Users should successfully complete forms with confidence.

Users should always understand:

- What is happening
- What remains
- What failed
- How to recover
- Whether submission succeeded

Completion should never create uncertainty.

---

# File Uploads

## Purpose

Allow users to attach files to a form.

Requirements:

- Supported file types
- Maximum file size
- Multiple upload support when appropriate
- Remove uploaded file
- Replace uploaded file

Users should immediately understand upload requirements.

---

# Drag and Drop Upload

## Purpose

Reduce effort when uploading files.

Requirements:

- Large drop zone
- Click-to-upload alternative
- Drag-over state
- Keyboard accessibility
- Mobile fallback

Drag and drop should never be the only upload method.

---

# Multiple File Uploads

## Purpose

Allow several files in one workflow.

Requirements:

- Individual file status
- Remove individual files
- Retry failed uploads
- Maximum file count
- File ordering when relevant

Each file should remain independently manageable.

---

# Upload Progress

## Purpose

Communicate upload status.

Requirements:

- Progress indicator
- Percentage when appropriate
- Upload speed when useful
- Cancel upload
- Retry failed uploads

Users should never wonder whether uploads are progressing.

---

# Validation Summary

## Purpose

Summarize validation errors after submission.

Requirements:

- Display at top of form
- Link to each invalid field
- Preserve entered values
- Explain how to resolve errors

Validation summaries should complement inline validation.

---

# Error Recovery

## Purpose

Help users recover from submission problems.

Examples:

- Network interruption
- Validation failure
- Server error
- Upload failure
- Session timeout

Recovery should preserve completed work.

---

# Confirmation Screen

## Purpose

Confirm successful submission.

Requirements:

- Clear success message
- Submission reference when appropriate
- Summary of submitted data
- Next available actions

Confirmation should remove uncertainty.

---

# Success Flow

## Purpose

Guide users after successful completion.

Examples:

- View submitted record
- Download receipt
- Return to dashboard
- Create another record
- Share confirmation

Success flows should encourage the next logical action.

---

# Cancellation Flow

## Purpose

Allow users to safely abandon the workflow.

Requirements:

- Confirmation before losing data
- Save draft option
- Explain consequences
- Return to previous screen

Cancellation should prevent accidental loss.

---

# Undo

## Purpose

Allow users to reverse recent actions.

Examples:

- Delete record
- Remove upload
- Archive item
- Restore draft

Undo should be available whenever practical.

---

# Bulk Editing

## Purpose

Modify multiple records efficiently.

Requirements:

- Multi-selection
- Batch validation
- Preview changes
- Partial failure handling
- Undo when appropriate

Bulk editing should remain predictable.

---

# Form Completion Selection Guide

Use:

File Uploads

For attaching documents or media.

Drag and Drop Upload

For desktop upload workflows.

Multiple File Uploads

For batch attachments.

Upload Progress

For long-running uploads.

Validation Summary

For submission errors.

Error Recovery

For failed submissions.

Confirmation Screen

For successful completion.

Success Flow

For post-submission guidance.

Cancellation Flow

For abandoning workflows.

Undo

For reversible actions.

Bulk Editing

For multi-record operations.

---

# Workflow Variants

Represent form completion as reusable patterns.

Recommended properties:

Workflow

- Upload
- Validation
- Confirmation
- Recovery
- Bulk Edit
- Undo

State

- Uploading
- Validating
- Submitted
- Failed
- Cancelled
- Completed

Platform

- Web
- Mobile
- Desktop

Avoid duplicate completion workflows.

---

# Responsive Behavior

Desktop

- Side-by-side uploads
- Rich progress indicators
- Bulk editing tables

Tablet

- Adaptive layouts
- Touch-friendly uploads

Mobile

- Camera integration
- Native file picker
- Compact progress cards
- Single-column review

Behavior should remain consistent across platforms.

---

# AI Form Optimization Engine

Before selecting a completion workflow, answer:

- Is user input preserved?
- Is recovery straightforward?
- Is accessibility supported?
- Does this reuse existing components?
- Is completion status clear?
- Can this scale across products?

If any answer is negative, redesign the workflow.

---

# Validation Checklist

□ File uploads documented

□ Drag and drop documented

□ Multiple uploads documented

□ Upload progress documented

□ Validation summary documented

□ Error recovery documented

□ Confirmation screen documented

□ Success flow documented

□ Cancellation flow documented

□ Undo documented

□ Bulk editing documented

□ Responsive behavior documented