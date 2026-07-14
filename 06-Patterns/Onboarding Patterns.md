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