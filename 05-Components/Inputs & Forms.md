---
title: Inputs & Forms
version: 1.0.0
status: Stable
owner: Design System Skill
category: Components
priority: Critical
last_updated: 2026-07-13

inherits:
  - ../00-Core/Universal Design Principles.md
  - ../01-Foundation/Accessibility.md
  - ../01-Foundation/Layout Systems.md
  - ../02-Visual-System/Color Theory.md
  - ../02-Visual-System/Typography.md
  - ../02-Visual-System/Spacing & Sizing.md
  - ../03-Components/Component Principles.md
---

# Inputs & Forms

## Purpose

This module teaches the AI how to design scalable, accessible, reusable, and production-ready form components.

Forms collect information.

Every field should help users complete tasks with minimal effort.

---

# Definition

An input is a component used to collect, modify, or validate user data.

A form is a structured collection of input components that supports a user goal.

---

# Objectives

After completing this module, the AI should be able to:

- Design reusable input components
- Build accessible forms
- Improve data entry
- Reduce user errors
- Support responsive layouts
- Improve validation
- Improve developer implementation
- Scale form systems

---

# Form Philosophy

Forms should reduce effort.

Every field should answer:

- Why is this information needed?
- Is this field necessary?
- Can this task be completed faster?

Remove unnecessary fields whenever possible.

---

# Core Principles

Always:

- Collect only required information.
- Use clear labels.
- Validate early.
- Support accessibility.
- Maintain consistency.
- Minimize typing.

Never:

- Use placeholder text as labels.
- Ask for unnecessary information.
- Hide validation rules.
- Create inconsistent fields.
- Interrupt user flow unnecessarily.

---

# Why Forms Exist

Forms help users:

- Register
- Sign in
- Search
- Purchase
- Submit requests
- Update information
- Complete workflows

Every form should move users closer to their goal.

---

# Form Anatomy

Every form should define:

- Title
- Description
- Labels
- Input fields
- Helper text
- Validation
- Error messages
- Success feedback
- Primary action
- Secondary action

Each element should have one responsibility.

---

# Input Anatomy

Every input should contain:

- Container
- Label
- Value
- Placeholder
- Helper text
- Validation message
- Optional icon
- Focus indicator

The structure should remain consistent.

---

# Labels

Labels describe the required information.

Good examples:

Email Address

Phone Number

First Name

Company Name

Labels should always remain visible.

---

# Placeholder Text

Placeholder text provides examples.

Examples:

john@example.com

Search products

Enter your full name

Placeholder text should never replace labels.

---

# Helper Text

Helper text provides additional guidance before errors occur.

Examples:

Password must contain at least 8 characters.

We'll never share your email.

Helper text should reduce uncertainty.

---

# Required Fields

Clearly identify required inputs.

Only require information essential to completing the task.

Minimize mandatory fields.

---

# Optional Fields

Optional fields should be clearly identified.

Users should never guess whether information is required.

---

# AI Decision Rules

Before approving a form, answer:

- Is every field necessary?
- Are labels clear?
- Is accessibility supported?
- Is validation predictable?
- Can users complete the form efficiently?
- Can developers implement it consistently?

If any answer is negative, redesign the form.

---

# Validation Checklist

□ Form purpose documented

□ Input anatomy documented

□ Labels reviewed

□ Helper text documented

□ Required fields reviewed

□ Optional fields documented

□ Accessibility reviewed

□ Documentation updated


---

# Input Types

## Philosophy

Every input should belong to one reusable input family.

Different input types collect different kinds of information while maintaining a consistent experience.

Avoid creating unrelated input components when a variant is sufficient.

---

# Text Field

## Purpose

Text fields collect short text values.

Examples:

- First Name
- Last Name
- Company
- City

Rules:

- Single line
- Clear label
- Visible cursor
- Appropriate keyboard
- Predictable validation

---

# Text Area

## Purpose

Text areas collect longer responses.

Examples:

- Description
- Comments
- Feedback
- Biography

Rules:

- Multi-line
- Resizable when appropriate
- Preserve entered content
- Support character limits when required

---

# Number Input

## Purpose

Collect numeric values.

Examples:

- Age
- Quantity
- Price
- Score

Rules:

- Accept only numeric input
- Support minimum and maximum values
- Prevent invalid characters where appropriate

---

# Email Input

## Purpose

Collect email addresses.

Rules:

- Use email keyboard on mobile
- Validate email format
- Preserve capitalization rules
- Support autofill

---

# Password Field

## Purpose

Secure sensitive information.

Requirements:

- Hidden by default
- Show and Hide control
- Password manager support
- Autofill support

Never expose passwords by default.

---

# Search Field

## Purpose

Allow users to search content.

Requirements:

- Search icon
- Clear button
- Fast response
- Preserve search history only when appropriate

Search should begin only when appropriate for performance.

---

# Phone Input

## Purpose

Collect telephone numbers.

Requirements:

- Country support
- Formatting
- Numeric keyboard
- Validation

Support international formats whenever applicable.

---

# Date Picker

## Purpose

Collect dates accurately.

Use date pickers instead of manual typing whenever possible.

Requirements:

- Calendar interface
- Keyboard support
- Accessible navigation
- Locale awareness

---

# Time Picker

## Purpose

Collect time values.

Requirements:

- 12-hour or 24-hour format
- Keyboard support
- Mobile-friendly controls

Use consistent formatting throughout the product.

---

# Select Menu

## Purpose

Allow users to choose one option from a predefined list.

Requirements:

- Clear selected value
- Keyboard navigation
- Search when option count is large
- Accessible announcements

Avoid long unsearchable lists.

---

# Combobox

## Purpose

Allow users to type or select from suggestions.

Recommended for:

- Countries
- Cities
- Users
- Products

Suggestions should update as users type.

---

# Autocomplete

Autocomplete predicts user input.

Benefits:

- Faster completion
- Fewer typing errors
- Better user experience

Suggestions should remain relevant.

---

# Input Variants

Represent input types as variants.

Recommended properties:

Type

- Text
- Email
- Password
- Search
- Number
- Phone
- Date
- Time
- Select
- Combobox
- Text Area

Avoid creating independent components for each type.

---

# Leading Elements

Optional leading content includes:

- Icons
- Country selectors
- Prefixes

Leading elements should support the input purpose.

---

# Trailing Elements

Optional trailing content includes:

- Clear button
- Password toggle
- Status icon
- Validation icon

Trailing elements should not obstruct user input.

---

# Input Selection Guide

Use:

Text

For general text.

Email

For email addresses.

Password

For credentials.

Search

For finding content.

Number

For numeric values.

Phone

For telephone numbers.

Date

For dates.

Time

For time values.

Select

For fixed options.

Combobox

For searchable options.

Text Area

For long responses.

---

# AI Input Selection Engine

Before selecting an input type, answer:

- Is this the simplest control?
- Does it reduce typing?
- Does it improve accuracy?
- Is the input accessible?
- Can this input scale across products?
- Is this already part of the input family?

If any answer is negative, select a more appropriate input.

---

# Validation Checklist

□ Text field documented

□ Text area documented

□ Number input documented

□ Email input documented

□ Password field documented

□ Search field documented

□ Phone input documented

□ Date picker documented

□ Time picker documented

□ Select menu documented

□ Combobox documented

□ Autocomplete documented

□ Variant strategy documented