---
title: Onboarding Patterns
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
  - ../05-Components/Feedback Components.md
  - ../05-Components/Navigation Components.md
  - ../05-Components/Modals, Dialogs & Drawers.md
---

# Onboarding Patterns

## Purpose

This module teaches the AI how to design onboarding experiences that help users reach value quickly.

Onboarding should reduce uncertainty instead of explaining every feature.

---

# Definition

Onboarding is the user's first guided experience inside a product.

Its goal is to help users complete their first meaningful task successfully.

Onboarding should adapt to user needs rather than forcing every user through the same experience.

---

# Objectives

After completing this module, the AI should be able to:

- Reduce time to first value
- Increase activation
- Minimize abandonment
- Personalize onboarding
- Support accessibility
- Scale onboarding across products

---

# Onboarding Philosophy

Every onboarding experience should answer:

- Who is this user?
- What is their goal?
- What must they learn immediately?
- What can wait until later?

Teach through action whenever possible.

---

# Core Principles

Always:

- Focus on user goals.
- Reduce setup effort.
- Reveal features progressively.
- Save user progress.
- Reuse existing components.
- Support accessibility.

Never:

- Explain every feature at once.
- Require unnecessary setup.
- Force long product tours.
- Interrupt users repeatedly.
- Block users from reaching value.

---

# Onboarding Lifecycle

Every onboarding workflow should define:

- Entry
- Welcome
- Personalization
- Initial setup
- First success
- Feature discovery
- Activation
- Completion

Every stage should move users closer to value.

---

# User Types

Common onboarding audiences include:

- First-time users
- Returning users
- Invited users
- Team members
- Enterprise users
- Administrators

Different users may require different onboarding experiences.

---

# Pattern Composition

Onboarding should reuse existing components.

Examples:

- Buttons
- Forms
- Cards
- Progress indicators
- Checklists
- Tooltips
- Dialogs
- Navigation

Avoid creating onboarding-specific UI when reusable components already exist.

---

# Success Metrics

Measure onboarding using:

- Activation rate
- Time to first value
- Completion rate
- Drop-off rate
- Feature adoption
- User retention

Metrics should guide continuous improvement.

---

# AI Decision Rules

Before approving an onboarding pattern, answer:

- Does it help users reach value quickly?
- Does it avoid unnecessary friction?
- Is accessibility supported?
- Does it reuse existing components?
- Can users skip optional guidance?
- Can developers implement this consistently?

If any answer is negative, redesign the workflow.

---

# Validation Checklist

□ Purpose documented

□ Onboarding lifecycle documented

□ User types documented

□ Component composition documented

□ Success metrics documented

□ Accessibility reviewed

□ Documentation updated


---

# Onboarding Workflows

## Philosophy

Every onboarding workflow should help users reach their first meaningful outcome.

Users should always understand:

- What they need to do
- Why it matters
- What happens next
- How close they are to completion

Teach through interaction.

---

# Welcome Experience

## Purpose

Introduce the product.

A welcome experience should:

- Communicate value
- Set expectations
- Reduce uncertainty
- Encourage continuation

Keep introductions brief.

---

# Personalization

## Purpose

Adapt the product to user needs.

Examples:

- Role
- Industry
- Experience level
- Interests
- Team size

Only request information that improves the experience.

---

# Goal Selection

## Purpose

Understand what users want to achieve.

Examples:

- Build a website
- Design an application
- Manage projects
- Track finances

Goals should personalize later experiences.

---

# Account Setup

## Purpose

Prepare the account for first use.

Examples:

- Profile creation
- Workspace creation
- Team invitation
- Preferences

Only require essential setup.

---

# Progressive Profiling

## Purpose

Collect information over time.

Instead of requesting everything immediately:

- Ask only what is needed now.
- Request additional information later.
- Update profiles gradually.

Reduce initial friction.

---

# Permissions

## Purpose

Request permissions only when required.

Examples:

- Notifications
- Camera
- Microphone
- Location
- Contacts

Explain the benefit before requesting access.

---

# Product Tour

## Purpose

Introduce major areas of the product.

Product tours should:

- Remain optional
- Focus on primary workflows
- Avoid excessive detail

Users should begin using the product quickly.

---

# Interactive Walkthrough

## Purpose

Teach by doing.

Examples:

- Complete first task
- Create first project
- Send first message
- Build first design

Learning through action improves retention.

---

# Onboarding Checklist

## Purpose

Help users track progress.

Examples:

- Complete profile
- Invite teammates
- Create first project
- Explore key features

Checklists should celebrate progress.

---

# Empty State Onboarding

## Purpose

Guide users when no content exists.

Examples:

- No projects
- No documents
- No contacts
- No tasks

Every empty state should suggest a meaningful next action.

---

# Contextual Education

## Purpose

Teach features when users need them.

Examples:

- Tooltips
- Tips
- Inline guidance
- Feature highlights

Avoid interrupting active work.

---

# Onboarding Selection Guide

Use:

Welcome Experience

For introducing the product.

Personalization

For tailoring the experience.

Goal Selection

For understanding user intent.

Account Setup

For essential configuration.

Progressive Profiling

For collecting information gradually.

Permissions

For protected system capabilities.

Product Tour

For introducing the interface.

Interactive Walkthrough

For teaching primary workflows.

Checklist

For activation progress.

Contextual Education

For feature discovery during usage.

---

# Onboarding Variants

Represent onboarding as reusable patterns.

Recommended properties:

Stage

- Welcome
- Setup
- Personalization
- Walkthrough
- Checklist
- Completion

State

- Default
- Loading
- Success
- Error
- Skipped
- Completed

Platform

- Web
- Mobile
- Desktop

Avoid duplicate onboarding workflows.

---

# Responsive Behavior

Desktop

- Multi-column onboarding
- Rich illustrations
- Side-by-side guidance

Tablet

- Adaptive layouts
- Touch-friendly interactions

Mobile

- Single-column flow
- Step-by-step guidance
- Thumb-friendly controls

The onboarding logic should remain consistent across platforms.

---

# AI Onboarding Selection Engine

Before selecting an onboarding workflow, answer:

- Does this reduce time to first value?
- Is personalization necessary?
- Can users skip optional guidance?
- Is accessibility supported?
- Does this reuse existing components?
- Can this scale across products?

If any answer is negative, redesign the onboarding workflow.

---

# Validation Checklist

□ Welcome experience documented

□ Personalization documented

□ Goal selection documented

□ Account setup documented

□ Progressive profiling documented

□ Permissions documented

□ Product tour documented

□ Interactive walkthrough documented

□ Checklist documented

□ Empty state onboarding documented

□ Contextual education documented

□ Responsive behavior documented

---

# Onboarding States

## Philosophy

Every onboarding workflow should communicate its current state.

Users should always understand:

- Where they are
- What is happening
- What remains
- How to continue

Every state should encourage progress.

---

# Loading State

Loading occurs while preparing onboarding resources.

Examples:

- Creating workspace
- Loading templates
- Loading recommendations
- Verifying account

Requirements:

- Stable layout
- Skeleton screens where appropriate
- Progress indicator when duration is known

Avoid blank screens.

---

# Empty State

Empty onboarding states guide users toward their first action.

Examples:

- No projects
- No teammates
- No documents
- No integrations

Every empty state should encourage progress.

---

# Error State

Errors should explain:

- What happened
- Why when known
- How to recover

Examples:

- Retry
- Continue later
- Edit information
- Contact support

Never trap users in an error state.

---

# Skip Flow

Optional onboarding should support skipping.

Requirements:

- Clearly labeled skip action
- Preserve progress
- Allow users to return later

Never force optional education.

---

# Resume Flow

Users should continue from their previous step.

Examples:

- Closed application
- Browser refresh
- Device interruption
- Network interruption

Resume should restore context immediately.

---

# Progress Persistence

Onboarding should save progress continuously.

Save:

- Current step
- User selections
- Completed tasks
- Personalization

Avoid requiring users to restart onboarding.

---

# Feature Unlocks

Introduce capabilities progressively.

Examples:

- Advanced settings
- Team collaboration
- Automation
- Integrations

Unlock features after users understand core functionality.

---

# Milestones

Celebrate meaningful progress.

Examples:

- Profile completed
- First project created
- First teammate invited
- First workflow completed

Milestones reinforce success.

---

# Completion

Completion should communicate:

- Success
- What was achieved
- Recommended next action
- Available resources

Users should know where to go next.

---

# Activation Metrics

Measure onboarding effectiveness using:

- Time to first value
- Completion rate
- Activation rate
- Drop-off rate
- Feature adoption
- Seven-day retention

Measure outcomes rather than screen completion.

---

# Interruption Recovery

Support unexpected interruptions.

Examples:

- Application restart
- Connection loss
- Authentication timeout
- Device change

Recovery should preserve user confidence.

---

# AI Onboarding Evaluation Engine

Before approving an onboarding workflow, answer:

- Is progress saved automatically?
- Can users skip optional guidance?
- Can users resume later?
- Are milestones meaningful?
- Is accessibility supported?
- Does this reuse existing components?

If any answer is negative, redesign the onboarding workflow.

---

# Validation Checklist

□ Loading state documented

□ Empty state documented

□ Error state documented

□ Skip flow documented

□ Resume flow documented

□ Progress persistence documented

□ Feature unlocks documented

□ Milestones documented

□ Completion documented

□ Activation metrics documented

□ Interruption recovery documented

□ Responsive behavior validated


---

# Accessibility Across Onboarding

## Purpose

Every onboarding experience should be accessible from beginning to completion.

Users should be able to complete onboarding regardless of:

- Device
- Input method
- Ability
- Platform

Accessibility should exist throughout the journey.

---

# Keyboard Navigation

Onboarding should fully support keyboard interaction.

Requirements:

- Logical tab order
- Visible focus
- Enter activates primary actions
- Escape closes temporary interfaces
- Arrow keys navigate step indicators when appropriate

Users should complete onboarding without a mouse.

---

# Focus Management

Focus should:

- Move logically between steps
- Remain visible
- Enter dialogs automatically
- Return after dialogs close
- Never become trapped unintentionally

Focus should always reflect the user's current task.

---

# Screen Reader Support

Onboarding should expose:

- Current step
- Total number of steps
- Progress
- Required fields
- Validation errors
- Completion messages

Users should always understand their progress.

---

# Responsive Onboarding

Desktop

- Multi-column layouts
- Rich illustrations
- Context panels

Tablet

- Adaptive layouts
- Touch-friendly controls

Mobile

- Single-column flow
- Thumb-friendly controls
- Progressive disclosure
- Minimal typing

Workflow logic should remain consistent across devices.

---

# Design Token Integration

Onboarding should reference design tokens.

Examples:

onboarding.spacing

onboarding.radius

onboarding.elevation

onboarding.focus.ring

onboarding.motion.duration

onboarding.success.color

onboarding.warning.color

onboarding.error.color

Avoid hardcoded values.

---

# Documentation Standards

Every onboarding workflow should document:

- Purpose
- Target users
- User goal
- Entry point
- Workflow
- States
- Accessibility
- Responsive behavior
- Components used
- Success metrics
- Usage guidelines
- Do
- Don't
- Examples

Documentation should remove implementation ambiguity.

---

# Testing Strategy

Every onboarding workflow should be tested for:

- Accessibility
- Keyboard navigation
- Screen reader compatibility
- Responsive layouts
- Progress persistence
- Resume flow
- Error recovery
- Performance

Testing should validate the complete onboarding experience.

---

# Quality Assurance

Review every onboarding workflow for:

- User goal alignment
- Accessibility
- Workflow consistency
- Component reuse
- Responsive behavior
- Documentation
- Performance

Only approved onboarding patterns belong in the design system.

---

# Versioning

Track changes for:

- New onboarding flows
- Accessibility improvements
- Activation improvements
- Feature education updates
- Bug fixes
- Breaking changes

Maintain complete version history.

---

# Governance

Onboarding updates should include:

- UX review
- Accessibility review
- Product review
- Engineering review
- QA approval
- Documentation update

Governance maintains long-term consistency.

---

# AI Onboarding Review Engine

Before publishing any onboarding workflow, answer:

- Does this reduce time to first value?
- Is accessibility complete?
- Is progress saved automatically?
- Can users skip optional guidance?
- Are design tokens used?
- Has testing been completed?
- Does this reuse existing components?
- Can this scale across products?

If any answer is negative, revise the workflow.

---

# Onboarding Checklist

Before publishing:

□ User types documented

□ Workflow documented

□ Personalization documented

□ Accessibility completed

□ Keyboard navigation verified

□ Screen reader support completed

□ Progress persistence verified

□ Responsive behavior validated

□ Design tokens integrated

□ Success metrics documented

□ Testing completed

□ QA approved

□ Version history updated

□ Documentation completed

---

# Key Takeaways

Onboarding should help users reach value as quickly as possible.

The AI must:

- Teach through interaction.
- Reduce setup effort.
- Support progressive disclosure.
- Preserve user progress.
- Support keyboard navigation.
- Support screen readers.
- Use design tokens.
- Measure activation.
- Test complete onboarding journeys.
- Document every workflow.

Every onboarding pattern should improve activation, accessibility, consistency, and long-term maintainability.