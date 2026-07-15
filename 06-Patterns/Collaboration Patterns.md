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

---

# Collaboration Management

## Philosophy

Collaboration should remain transparent throughout every workflow.

Users should always understand:

- What changed
- Who made the change
- Who has access
- What requires attention

Every collaborative action should remain visible.

---

# Notifications

## Purpose

Keep collaborators informed.

Notifications may communicate:

- New comments
- Mentions
- Assignments
- Reviews
- Approvals
- Status updates

Only notify users when the information is relevant.

---

# Conflict Resolution

## Purpose

Resolve competing actions safely.

Conflict resolution should:

- Explain the conflict
- Identify contributors
- Present available options
- Preserve user work

Never discard changes automatically.

---

# Concurrent Editing

## Purpose

Support multiple users editing simultaneously.

Requirements:

- Real-time updates
- Save indicators
- User attribution
- Conflict detection

Concurrent editing should feel predictable.

---

# Permission Changes

## Purpose

Manage access safely.

Permission updates should communicate:

- Previous permission
- New permission
- Effective date
- Person making the change

Users should understand why access changed.

---

# Role Management

## Purpose

Assign responsibilities.

Examples:

- Owner
- Administrator
- Editor
- Reviewer
- Viewer
- Guest

Roles should communicate capabilities clearly.

---

# Sharing

## Purpose

Allow secure access to resources.

Sharing options may include:

- Individual users
- Teams
- Public access
- Restricted access
- Link sharing

Sharing should follow product security rules.

---

# Invitations

## Purpose

Invite collaborators into a workspace.

Invitations should include:

- Resource name
- Inviter
- Assigned role
- Expiration when applicable

Pending invitations should remain visible.

---

# Guest Access

## Purpose

Provide temporary collaboration.

Guest users should receive:

- Limited permissions
- Clear restrictions
- Expiration when appropriate

Guest access should minimize unnecessary risk.

---

# Audit History

## Purpose

Track collaboration activity.

Events may include:

- Comments
- Reviews
- Permission updates
- Assignments
- Status changes
- Shared access

Audit history improves accountability.

---

# Collaboration Analytics

## Purpose

Measure collaboration effectiveness.

Examples:

- Review completion time
- Response time
- Collaboration frequency
- Active contributors
- Resolution time

Measure outcomes rather than message volume.

---

# Offline Collaboration

## Purpose

Support collaboration during connectivity loss.

Requirements:

- Local changes
- Synchronization queue
- Conflict recovery
- Save indicators

Users should understand synchronization status.

---

# Collaboration Selection Guide

Use:

Notifications

For awareness.

Conflict Resolution

For competing changes.

Concurrent Editing

For real-time collaboration.

Permission Changes

For access updates.

Role Management

For responsibility assignment.

Sharing

For resource access.

Invitations

For onboarding collaborators.

Guest Access

For temporary participation.

Audit History

For accountability.

Collaboration Analytics

For performance insights.

Offline Collaboration

For interrupted connectivity.

---

# Workflow Variants

Represent collaboration management as reusable patterns.

Recommended properties:

Workflow

- Notification
- Permission
- Sharing
- Invitation
- Conflict
- Audit

State

- Pending
- Active
- Synced
- Conflict
- Expired
- Completed

Platform

- Web
- Mobile
- Desktop

Avoid duplicate collaboration workflows.

---

# Responsive Behavior

Desktop

- Persistent activity panels
- Rich audit history
- Advanced permission management

Tablet

- Expandable collaboration panels
- Adaptive permission dialogs

Mobile

- Simplified notifications
- Compact activity timeline
- Bottom sheet sharing

Workflow behavior should remain consistent across devices.

---

# AI Collaboration Evaluation Engine

Before approving a workflow, answer:

- Is collaboration transparent?
- Are permissions understandable?
- Are notifications relevant?
- Is accessibility supported?
- Does this reuse existing components?
- Can this scale across products?

If any answer is negative, redesign the workflow.

---

# Validation Checklist

□ Notifications documented

□ Conflict resolution documented

□ Concurrent editing documented

□ Permission changes documented

□ Role management documented

□ Sharing documented

□ Invitations documented

□ Guest access documented

□ Audit history documented

□ Collaboration analytics documented

□ Offline collaboration documented

□ Responsive behavior documented


---

# Accessibility Across Collaboration

## Purpose

Every collaboration workflow should be accessible.

Users should collaborate regardless of:

- Device
- Input method
- Ability
- Platform

Accessibility should exist throughout every collaborative experience.

---

# Keyboard Navigation

Collaboration should fully support keyboard interaction.

Requirements:

- Logical tab order
- Visible focus
- Keyboard shortcuts where appropriate
- Enter submits actions when appropriate
- Escape closes temporary interfaces

Users should never require a mouse.

---

# Focus Management

Focus should:

- Move logically
- Remain visible
- Enter dialogs automatically
- Return after dialogs close
- Never become trapped unintentionally

Focus should always indicate the current task.

---

# Screen Reader Support

Collaboration should expose:

- Comment authors
- Timestamps
- Assignment status
- Review status
- Approval status
- Notification updates
- Presence information
- Activity summaries

Users should understand collaborative activity without visual cues.

---

# Responsive Collaboration

Desktop

- Persistent activity panels
- Multi-column discussions
- Rich review interfaces

Tablet

- Expandable collaboration panels
- Adaptive layouts
- Touch-friendly controls

Mobile

- Bottom sheet discussions
- Compact activity feeds
- Simplified review workflows
- Optimized notifications

Workflow behavior should remain consistent across devices.

---

# Performance

Collaboration should:

- Update efficiently
- Synchronize quickly
- Preserve user work
- Minimize unnecessary refreshes
- Handle concurrent activity smoothly

Performance should support uninterrupted teamwork.

---

# Design Token Integration

Collaboration should reference design tokens.

Examples:

collaboration.spacing

collaboration.radius

collaboration.focus.ring

collaboration.motion.duration

collaboration.success.color

collaboration.warning.color

collaboration.error.color

collaboration.presence.color

Avoid hardcoded values.

---

# Documentation Standards

Every collaboration workflow should document:

- Purpose
- User goal
- Participants
- Workflow
- States
- Notifications
- Permissions
- Accessibility
- Responsive behavior
- Components used
- Usage guidelines
- Do
- Don't
- Examples

Documentation should eliminate implementation ambiguity.

---

# Testing Strategy

Every collaboration workflow should be tested for:

- Accessibility
- Keyboard navigation
- Screen reader compatibility
- Shared editing
- Notification delivery
- Permission handling
- Conflict resolution
- Responsive layouts
- Performance

Testing should validate the complete collaboration experience.

---

# Quality Assurance

Review every workflow for:

- Collaboration clarity
- Accessibility
- Workflow consistency
- Component reuse
- Responsive behavior
- Documentation
- Performance

Only approved workflows belong in the design system.

---

# Versioning

Track changes for:

- Workflow improvements
- Accessibility improvements
- Notification updates
- Permission updates
- Bug fixes
- Breaking changes

Maintain complete version history.

---

# Governance

Collaboration updates should include:

- UX review
- Accessibility review
- Product review
- Engineering review
- QA approval
- Documentation update

Governance protects long-term consistency.

---

# AI Collaboration Review Engine

Before publishing any workflow, answer:

- Is collaboration transparent?
- Is accessibility complete?
- Are permissions understandable?
- Are notifications relevant?
- Are design tokens used?
- Has testing been completed?
- Does this reuse existing components?
- Can this scale across products?

If any answer is negative, revise the workflow.

---

# Collaboration Checklist

Before publishing:

□ Collaboration workflows documented

□ Collaboration management documented

□ Accessibility completed

□ Keyboard navigation verified

□ Screen reader support completed

□ Notification behavior verified

□ Responsive behavior validated

□ Design tokens integrated

□ Testing completed

□ QA approved

□ Version history updated

□ Documentation completed

---

# Key Takeaways

Collaboration should help people work together without creating confusion.

The AI must:

- Make shared work visible.
- Preserve user work.
- Support keyboard navigation.
- Support screen readers.
- Use design tokens.
- Handle permissions clearly.
- Test complete workflows.
- Document every workflow.
- Reuse existing components.
- Scale across products.

Every collaboration pattern should improve teamwork, accessibility, consistency, transparency, and long-term maintainability.