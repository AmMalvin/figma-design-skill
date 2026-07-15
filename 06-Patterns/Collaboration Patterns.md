---
title: Collaboration Patterns
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
  - ../05-Components/Buttons.md
  - ../05-Components/Inputs & Forms.md
  - ../05-Components/Feedback Components.md
  - ../05-Components/Data Display.md
  - ../05-Components/Navigation Components.md
  - ../05-Components/Modals, Dialogs & Drawers.md
---

# Collaboration Patterns

## Purpose

This module teaches the AI how to design collaborative workflows that are reliable, scalable, and easy to understand.

Collaboration should help multiple users work together without creating confusion.

---

# Definition

Collaboration is the coordinated interaction between two or more users while working toward a shared goal.

Collaboration should improve communication, coordination, and awareness.

---

# Objectives

After completing this module, the AI should be able to:

- Design collaborative workflows
- Improve team coordination
- Reduce communication friction
- Prevent collaboration conflicts
- Increase transparency
- Scale collaboration across products

---

# Collaboration Philosophy

Every collaboration workflow should answer:

- Who is collaborating?
- What is shared?
- What changed?
- Who performed the action?
- What happens next?

Users should always understand shared activity.

---

# Core Principles

Always:

- Make collaboration visible.
- Preserve user work.
- Identify contributors.
- Explain shared changes.
- Reuse existing components.
- Support accessibility.

Never:

- Hide collaborative actions.
- Lose user work.
- Create conflicting workflows.
- Interrupt active work unnecessarily.
- Duplicate interaction patterns.

---

# Collaboration Lifecycle

Every workflow should define:

- Invite
- Join
- Contribute
- Review
- Resolve
- Complete

Each stage should remain predictable.

---

# Collaboration Types

Common collaboration models include:

- Real-time collaboration
- Asynchronous collaboration
- Review workflows
- Approval workflows
- Team collaboration
- Guest collaboration

Select the collaboration model based on product needs.

---

# Pattern Composition

Collaboration patterns should reuse existing components.

Examples:

- Comments
- Dialogs
- Tables
- Cards
- Notifications
- Menus
- Avatars
- Activity feeds

Avoid collaboration-specific components when reusable components already exist.

---

# Success Metrics

Measure collaboration using:

- Task completion rate
- Review completion rate
- Collaboration frequency
- Resolution time
- Conflict rate
- User satisfaction

Measure successful collaboration instead of interaction volume.

---

# AI Decision Rules

Before approving a collaboration workflow, answer:

- Does it improve collaboration?
- Are contributors clearly identified?
- Is accessibility supported?
- Does it reuse existing components?
- Can users understand shared activity?
- Can developers implement this consistently?

If any answer is negative, redesign the workflow.

---

# Validation Checklist

□ Purpose documented

□ Collaboration lifecycle documented

□ Collaboration types documented

□ Component composition documented

□ Success metrics documented

□ Accessibility reviewed

□ Documentation updated

---

# Collaboration Workflows

## Philosophy

Every collaboration workflow should improve teamwork without interrupting individual work.

Users should always understand:

- Who is involved
- What changed
- When it changed
- What action is expected

Collaboration should increase awareness.

---

# Comments

## Purpose

Allow users to discuss specific content.

Comments should:

- Attach to relevant content
- Support rich text when appropriate
- Display author information
- Display timestamps

Comments should remain connected to their context.

---

# Replies

## Purpose

Organize discussions.

Replies should:

- Remain nested under the original comment
- Preserve conversation order
- Notify relevant participants

Avoid excessively deep nesting.

---

# Mentions

## Purpose

Notify specific users.

Examples:

- @Person
- @Team
- @Reviewer

Mentioned users should receive notifications when appropriate.

Mentions should autocomplete while typing.

---

# Reactions

## Purpose

Allow lightweight feedback.

Examples:

- Like
- Approve
- Celebrate
- Acknowledge

Reactions should complement comments rather than replace discussion.

---

# Presence Indicators

## Purpose

Show who is currently viewing or editing.

Examples:

- Online
- Offline
- Active
- Idle

Presence should update automatically.

---

# Live Cursors

## Purpose

Display where collaborators are working.

Requirements:

- User identity
- Cursor color
- Smooth movement
- Minimal distraction

Live cursors improve awareness during shared editing.

---

# Shared Editing

## Purpose

Allow multiple users to edit simultaneously.

Requirements:

- Real-time updates
- Conflict handling
- Save status
- User attribution

Changes should appear without manual refresh.

---

# Assignments

## Purpose

Assign responsibility.

Assignments should include:

- Assignee
- Due date
- Status
- Priority

Ownership should remain visible.

---

# Reviews

## Purpose

Collect structured feedback.

Review workflows should support:

- Approval
- Requested changes
- Comments
- Completion tracking

Reviews should improve quality before publishing.

---

# Approvals

## Purpose

Authorize important actions.

Examples:

- Publish
- Merge
- Release
- Payment approval

Approval status should remain visible.

---

# Activity Feed

## Purpose

Display chronological collaboration history.

Events may include:

- Comments
- Edits
- Assignments
- Reviews
- Status changes

Activity feeds should support filtering.

---

# Collaboration Selection Guide

Use:

Comments

For discussion.

Replies

For threaded conversations.

Mentions

For notifying people.

Reactions

For lightweight feedback.

Presence Indicators

For awareness.

Live Cursors

For simultaneous editing.

Shared Editing

For collaborative creation.

Assignments

For ownership.

Reviews

For structured evaluation.

Approvals

For controlled decisions.

Activity Feed

For historical visibility.

---

# Workflow Variants

Represent collaboration as reusable patterns.

Recommended properties:

Workflow

- Comment
- Review
- Assignment
- Mention
- Approval
- Shared Editing

State

- Active
- Pending
- Resolved
- Approved
- Rejected
- Archived

Platform

- Web
- Mobile
- Desktop

Avoid duplicate collaboration workflows.

---

# Responsive Behavior

Desktop

- Persistent activity panels
- Side-by-side collaboration
- Rich discussion layouts

Tablet

- Expandable collaboration panels
- Touch-friendly interactions

Mobile

- Bottom sheets
- Simplified discussions
- Compact activity timeline

Collaboration behavior should remain consistent across platforms.

---

# AI Collaboration Selection Engine

Before selecting a collaboration workflow, answer:

- Does this improve teamwork?
- Is contributor identity visible?
- Are notifications appropriate?
- Is accessibility supported?
- Does this reuse existing components?
- Can this scale across products?

If any answer is negative, redesign the workflow.

---

# Validation Checklist

□ Comments documented

□ Replies documented

□ Mentions documented

□ Reactions documented

□ Presence indicators documented

□ Live cursors documented

□ Shared editing documented

□ Assignments documented

□ Reviews documented

□ Approvals documented

□ Activity feed documented

□ Responsive behavior documented