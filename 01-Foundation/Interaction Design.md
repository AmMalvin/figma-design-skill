---
title: Interaction Design
version: 1.0.0
status: Stable
owner: Design System Skill
category: Foundation
priority: Critical
last_updated: 2026-07-12

inherits:
  - ../00-Core/Universal Design Principles.md
  - ../01-Foundation/Systems Thinking.md
  - ../01-Foundation/Product Thinking.md
  - ../01-Foundation/Human-Centered Design.md
  - ../01-Foundation/Design Thinking.md
  - ../01-Foundation/Cognitive Psychology.md
  - ../01-Foundation/Mental Models.md
---

# Interaction Design

## Purpose

This module teaches the AI how people interact with digital interfaces through touch, mouse, keyboard, voice, gestures, and assistive technologies.

Every interaction should minimize effort while maximizing clarity, confidence, accessibility, and efficiency.

Interaction design is the bridge between user intention and system response.

---

# Definition

Interaction Design defines how users perform actions, receive feedback, recover from errors, and accomplish goals within a digital product.

Every interaction should feel predictable, responsive, and meaningful.

---

# Objectives

After completing this module, the AI should be able to:

- Design intuitive interactions
- Reduce interaction cost
- Improve efficiency
- Improve accessibility
- Improve discoverability
- Improve responsiveness
- Improve feedback
- Reduce errors
- Improve task completion
- Create scalable interaction patterns

---

# Interaction Design Mindset

Never ask:

"Does this interaction look impressive?"

Always ask:

- Is it easy to perform?
- Is it predictable?
- Is feedback immediate?
- Is the interaction accessible?
- Does it reduce effort?
- Does it support user goals?
- Can mistakes be prevented?

---

# Core Principles

Always:

- Reduce interaction cost.
- Keep interactions predictable.
- Provide immediate feedback.
- Prevent errors.
- Support recovery.
- Maintain consistency.
- Respect platform conventions.
- Design for accessibility.

Never:

- Surprise users unnecessarily.
- Hide important actions.
- Delay feedback.
- Require unnecessary steps.
- Introduce inconsistent behavior.

---

# Interaction Lifecycle

Every interaction follows this sequence:

Goal

↓

Intent

↓

Action

↓

System Response

↓

Feedback

↓

Result

↓

Learning

Every stage should be optimized.

---

# Types of Interactions

Support multiple input methods:

- Mouse
- Touch
- Keyboard
- Stylus
- Voice
- Screen Readers
- Switch Devices
- Assistive Technologies

Interactions should remain usable regardless of input method.

---

# Interaction Goals

Every interaction should:

- Be discoverable.
- Be understandable.
- Be efficient.
- Be reversible.
- Be accessible.
- Be consistent.
- Be measurable.

---

# AI Decision Rules

Before approving any interaction:

- Does it reduce effort?
- Is it predictable?
- Is feedback immediate?
- Can users recover from mistakes?
- Is it accessible?
- Is it consistent?
- Does it improve task completion?

Revise until every answer is positive.

---

# Validation Checklist

□ Interaction is discoverable

□ Feedback is immediate

□ Error prevention implemented

□ Error recovery supported

□ Accessibility reviewed

□ Consistency maintained

□ Platform conventions respected

□ Documentation updated


---

# Fitts's Law

## Definition

The time required to acquire a target depends on:

- Distance to the target
- Size of the target

Large, nearby targets are faster and easier to select.

---

# Applying Fitts's Law

Always:

- Make primary actions large.
- Place important controls close to the user's focus.
- Increase touch target size.
- Provide adequate spacing between controls.
- Position frequently used actions in easily reachable areas.

Never:

- Use tiny buttons.
- Place destructive actions close to primary actions.
- Require long pointer movement for common tasks.

---

# Touch Target Guidelines

Interactive elements should:

- Be easy to tap.
- Have sufficient spacing.
- Support different finger sizes.
- Support assistive technologies.

Important actions deserve larger targets than secondary actions.

---

# Hick's Law

## Definition

Decision time increases as the number of choices increases.

Too many options slow users down.

---

# Applying Hick's Law

Reduce unnecessary choices.

Group related options.

Highlight recommended actions.

Progressively reveal advanced functionality.

Avoid presenting every option simultaneously.

---

# Tesler's Law

## Definition

Every system contains unavoidable complexity.

The designer decides whether the complexity belongs to:

- The system
- The user

Move complexity into the system whenever practical.

---

# Applying Tesler's Law

Simplify workflows through:

- Automation
- Smart defaults
- Auto-complete
- Saved preferences
- Templates
- Intelligent recommendations

Users should not perform repetitive work the system can perform.

---

# Interaction Cost

Every interaction has a cost.

Examples include:

- Clicks
- Taps
- Typing
- Scrolling
- Dragging
- Decision making
- Waiting
- Error recovery

Reduce interaction cost whenever possible.

---

# Efficiency

Efficient interfaces:

- Minimize steps.
- Eliminate repetition.
- Preserve user context.
- Reduce navigation.
- Support shortcuts.
- Remember previous choices.

Efficiency should never reduce clarity.

---

# Progressive Disclosure

Present only the information needed for the current task.

Reveal advanced functionality when appropriate.

Benefits include:

- Reduced cognitive load
- Faster decisions
- Cleaner interfaces
- Improved learnability

---

# AI Decision Rules

Before approving any interaction:

- Is the target easy to acquire?
- Are unnecessary choices removed?
- Has complexity been shifted to the system?
- Is interaction cost minimized?
- Can the workflow be completed more efficiently?
- Is progressive disclosure applied where appropriate?

Revise until every answer is positive.

---

# Validation Checklist

□ Fitts's Law applied

□ Hick's Law applied

□ Tesler's Law applied

□ Touch targets reviewed

□ Interaction cost minimized

□ Workflow simplified

□ Progressive disclosure implemented

□ Efficiency improved


---

# Doherty Threshold

## Definition

Productivity increases when users receive system feedback within approximately 400 milliseconds.

Users should never wonder whether the system received their action.

Fast feedback maintains flow.

---

# Applying the Doherty Threshold

The AI should:

- Respond immediately to user input.
- Display optimistic UI where appropriate.
- Show loading indicators for longer operations.
- Use skeleton screens instead of blank pages.
- Preserve interaction momentum.

Every interaction exceeding 400 milliseconds should communicate progress.

---

# Goal Gradient Effect

## Definition

People become increasingly motivated as they approach a goal.

Visible progress encourages task completion.

---

# Applying the Goal Gradient Effect

Support motivation through:

- Progress bars
- Step indicators
- Completion percentages
- Checklists
- Milestone celebrations
- Task counters

Always communicate remaining effort.

---

# Peak-End Rule

## Definition

Users remember experiences primarily by:

- The emotional peak
- The ending

The overall duration is less influential than these moments.

---

# Applying the Peak-End Rule

Pay special attention to:

- Onboarding completion
- Successful purchases
- Account creation
- Achievement moments
- Confirmation screens
- Final checkout

End important workflows positively.

---

# Von Restorff Effect

## Definition

Items that stand out are remembered more easily.

Visual emphasis should communicate importance.

---

# Applying the Von Restorff Effect

Highlight:

- Primary actions
- Critical notifications
- Important status changes
- Emergency alerts
- Key metrics

Avoid highlighting multiple competing elements.

Only one primary focal point should exist within a given context.

---

# Serial Position Effect

## Definition

People remember the first and last items in a sequence better than those in the middle.

---

# Applying the Serial Position Effect

Place the most important actions:

- At the beginning
- At the end

Avoid hiding critical information in the middle of long lists.

---

# Zeigarnik Effect

## Definition

People naturally remember unfinished tasks.

Visible incomplete work encourages completion.

---

# Applying the Zeigarnik Effect

Use:

- Draft indicators
- Progress tracking
- Resume functionality
- Recently viewed items
- Continue buttons

Support users returning to unfinished work.

---

# Feedback Loops

Every interaction should produce meaningful feedback.

Feedback should communicate:

- What happened
- Why it happened
- What happens next
- Whether user action is required

Feedback should never create uncertainty.

---

# System Status

Users should always know the current system state.

Display:

- Loading
- Saving
- Syncing
- Processing
- Uploading
- Downloading
- Completed
- Failed

Never leave users wondering whether work is in progress.

---

# Loading States

When operations require time:

Display:

- Skeleton screens
- Progress indicators
- Estimated completion when possible
- Contextual messages

Avoid blank screens.

Avoid frozen interfaces.

---

# Empty States

An empty state should explain:

- Why nothing is shown
- What users can do next
- How to get started
- What value exists

Every empty state should guide action.

---

# Success States

Successful actions should provide:

- Confirmation
- Positive reinforcement
- Clear next steps
- Updated system status

Avoid interrupting users with unnecessary dialogs.

---

# Error States

Every error message should include:

- What happened
- Why it happened
- How to fix it
- Recovery options

Never blame the user.

Never use vague messages.

---

# AI Decision Rules

Before approving any interaction, answer:

- Does feedback appear immediately?
- Is progress visible?
- Are important actions emphasized?
- Are loading states informative?
- Are empty states helpful?
- Are success states meaningful?
- Can users recover from every error?
- Is the interaction memorable for the right reasons?

Revise until every answer is positive.

---

# Validation Checklist

□ Doherty Threshold considered

□ Progress visible

□ Feedback immediate

□ Peak moments improved

□ Primary actions emphasized

□ Loading states implemented

□ Empty states designed

□ Success states designed

□ Error recovery supported

□ System status always visible