---
title: Onboarding & First-Time User Experience Patterns
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
  - ../05-Components/Navigation Components.md
  - ../05-Components/Feedback Components.md
  - ../05-Components/Data Display.md
  - ../05-Components/Modals, Dialogs & Drawers.md
---

# Onboarding & First-Time User Experience Patterns

## Purpose

This module teaches the AI how to design onboarding experiences that help users reach value quickly.

Onboarding should reduce uncertainty while increasing confidence.

---

# Definition

Onboarding is the collection of workflows that help new users understand, configure, and successfully begin using a product.

First-time user experience includes every interaction before a user reaches their first meaningful success.

---

# Objectives

After completing this module, the AI should be able to:

- Design onboarding workflows
- Reduce abandonment
- Improve activation
- Increase product understanding
- Reduce cognitive load
- Scale onboarding across products

---

# Onboarding Philosophy

Every onboarding workflow should answer:

- Why is the user here?
- What should happen first?
- What is the fastest path to value?
- What should be learned now?
- What can wait until later?

Users should experience progress immediately.

---

# Core Principles

Always:

- Help users reach value quickly.
- Explain only what is necessary.
- Reveal complexity progressively.
- Reuse existing components.
- Support accessibility.
- Allow users to continue confidently.

Never:

- Overwhelm users.
- Force unnecessary tutorials.
- Request unnecessary information.
- Interrupt important tasks.
- Duplicate onboarding workflows.

---

# Onboarding Lifecycle

Every workflow should define:

- Welcome
- Orientation
- Setup
- First task
- First success
- Continued learning

Each stage should build confidence.

---

# Onboarding Types

Common onboarding models include:

- Guided onboarding
- Self-guided onboarding
- Progressive onboarding
- Contextual onboarding
- Interactive onboarding
- Enterprise onboarding

Choose the onboarding model based on user needs.

---

# Pattern Composition

Onboarding should reuse existing components.

Examples:

- Buttons
- Forms
- Cards
- Checklists
- Progress indicators
- Empty states
- Dialogs
- Notifications

Avoid onboarding-specific components when reusable components already exist.

---

# Success Metrics

Measure onboarding using:

- Activation rate
- First-task completion
- Time to first value
- Onboarding completion rate
- User retention
- User confidence

Measure successful outcomes instead of screen views.

---

# AI Decision Rules

Before approving an onboarding workflow, answer:

- Does it reduce user effort?
- Does it help users reach value quickly?
- Is accessibility supported?
- Does it reuse existing components?
- Is the workflow predictable?
- Can developers implement this consistently?

If any answer is negative, redesign the workflow.

---

# Validation Checklist

□ Purpose documented

□ Onboarding lifecycle documented

□ Onboarding types documented

□ Component composition documented

□ Success metrics documented

□ Accessibility reviewed

□ Documentation updated

---

# Onboarding Workflows

## Philosophy

Every onboarding workflow should reduce uncertainty while helping users reach their first success.

Users should always understand:

- What to do first
- Why it matters
- What happens next
- How much progress they have made

Onboarding should create confidence from the beginning.

---

# Welcome Screen

## Purpose

Introduce the product and establish expectations.

Requirements:

- Product value proposition
- Primary action
- Secondary action when appropriate
- Optional sign in
- Clear visual hierarchy

The welcome screen should focus on value, not features.

---

# Product Introduction

## Purpose

Explain the core benefit of the product.

Requirements:

- Simple language
- Minimal content
- Clear outcome
- Visual support when appropriate

Avoid lengthy introductions.

---

# User Segmentation

## Purpose

Personalize onboarding.

Examples:

- Individual
- Team
- Student
- Business
- Administrator
- Developer

Only request information that improves the experience.

---

# Setup Wizard

## Purpose

Guide users through required configuration.

Requirements:

- Logical sequence
- Progress indicator
- Save progress
- Skip optional steps
- Review before completion

Keep setup as short as possible.

---

# Product Tours

## Purpose

Introduce major product areas.

Requirements:

- Short sequence
- Skip option
- Resume later
- Focus on key workflows

Tours should never block product usage unnecessarily.

---

# Interactive Walkthroughs

## Purpose

Teach users by completing real tasks.

Requirements:

- Guided actions
- Contextual instructions
- Immediate feedback
- Real product interaction

Learning should happen through doing.

---

# Progressive Onboarding

## Purpose

Introduce features only when they become relevant.

Requirements:

- Contextual education
- Small learning steps
- Delayed complexity
- Feature discovery over time

Avoid introducing advanced functionality too early.

---

# Empty States

## Purpose

Guide users when no data exists.

Examples:

- First project
- First task
- First document
- First customer

Empty states should encourage meaningful action.

---

# Sample Data

## Purpose

Help users understand product capabilities immediately.

Requirements:

- Realistic examples
- Easy removal
- Clear distinction from user data

Sample data should accelerate learning.

---

# Starter Templates

## Purpose

Reduce setup effort.

Examples:

- Project templates
- Dashboard templates
- Report templates
- Workspace templates

Templates should reduce repetitive work.

---

# First Task

## Purpose

Guide users toward their first meaningful action.

Requirements:

- Clear objective
- Minimal steps
- Immediate feedback
- Visible completion

The first task should build confidence.

---

# First Success

## Purpose

Celebrate the user's first completed outcome.

Examples:

- Project created
- Message sent
- Report generated
- Payment received

Acknowledge success without interrupting progress.

---

# Onboarding Selection Guide

Use:

Welcome Screen

For first entry.

Product Introduction

For explaining value.

User Segmentation

For personalization.

Setup Wizard

For required configuration.

Product Tours

For product overview.

Interactive Walkthroughs

For learning by doing.

Progressive Onboarding

For gradual learning.

Empty States

For first-use guidance.

Sample Data

For immediate exploration.

Starter Templates

For faster setup.

First Task

For activation.

First Success

For reinforcement.

---

# Workflow Variants

Represent onboarding as reusable patterns.

Recommended properties:

Workflow

- Welcome
- Tour
- Walkthrough
- Setup
- Empty State
- Template
- First Task

State

- Default
- Active
- Skipped
- Completed
- Paused

Platform

- Web
- Mobile
- Desktop

Avoid duplicate onboarding workflows.

---

# Responsive Behavior

Desktop

- Multi-panel onboarding
- Rich walkthroughs
- Expanded setup

Tablet

- Adaptive layouts
- Touch-friendly controls

Mobile

- Single-column onboarding
- Bottom sheets
- Progressive steps
- Simplified setup

Behavior should remain consistent across platforms.

---

# AI Onboarding Selection Engine

Before selecting an onboarding workflow, answer:

- Does this help users reach value quickly?
- Is unnecessary information removed?
- Is accessibility supported?
- Does this reuse existing components?
- Is the workflow predictable?
- Can this scale across products?

If any answer is negative, redesign the workflow.

---

# Validation Checklist

□ Welcome screen documented

□ Product introduction documented

□ User segmentation documented

□ Setup wizard documented

□ Product tours documented

□ Interactive walkthroughs documented

□ Progressive onboarding documented

□ Empty states documented

□ Sample data documented

□ Starter templates documented

□ First task documented

□ First success documented

□ Responsive behavior documented