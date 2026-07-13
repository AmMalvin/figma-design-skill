---
title: Tables & Data Grids
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
  - ../02-Visual-System/Typography.md
  - ../02-Visual-System/Spacing & Sizing.md
  - ../02-Visual-System/Iconography.md
  - ./Component Principles.md
---

# Tables & Data Grids

## Purpose

This module teaches the AI how to design scalable, reusable, accessible, and production-ready tables and data grids.

Tables organize structured information for comparison, scanning, and analysis.

---

# Definition

A table presents structured data using rows and columns.

A data grid extends a table by supporting interaction such as sorting, filtering, selection, editing, and bulk operations.

---

# Objectives

After completing this module, the AI should be able to:

- Design reusable tables
- Build scalable data grids
- Improve readability
- Support large datasets
- Maintain accessibility
- Support responsive layouts
- Improve developer implementation
- Scale across products

---

# Table Philosophy

Tables should make structured information easy to scan.

Every table should answer:

- What information is most important?
- Which actions belong in the table?
- Can users compare values quickly?

Avoid unnecessary complexity.

---

# Core Principles

Always:

- Keep columns meaningful.
- Align related data.
- Support scanning.
- Use consistent spacing.
- Prioritize readability.
- Design reusable components.

Never:

- Overcrowd rows.
- Mix unrelated information.
- Hide important actions.
- Use inconsistent alignment.
- Add unnecessary columns.

---

# Why Tables Exist

Tables help users:

- Compare records
- Analyze information
- Review transactions
- Manage users
- Monitor systems
- Perform bulk actions

Tables should improve decision making.

---

# Table Anatomy

Every table should define:

- Container
- Header row
- Column headers
- Data rows
- Cells
- Footer
- Empty state
- Loading state
- Pagination
- Optional toolbar

Each element should have one responsibility.

---

# Header Row

The header row describes every column.

Headers should:

- Remain concise
- Support sorting when applicable
- Align with cell content

Headers should never be ambiguous.

---

# Data Rows

Rows represent individual records.

Every row should remain visually consistent.

Users should distinguish one row from another easily.

---

# Cells

Cells display individual values.

Examples:

- Text
- Number
- Status
- Badge
- Avatar
- Date
- Currency
- Action

Each cell should display one logical value.

---

# Footer

The footer may contain:

- Totals
- Pagination
- Summary
- Bulk actions

Only include information relevant to the dataset.

---

# Information Hierarchy

Tables should prioritize:

- Primary identifier
- Important values
- Supporting metadata
- Available actions

Visual hierarchy should improve scanning.

---

# AI Decision Rules

Before approving a table, answer:

- Is the data organized logically?
- Is scanning easy?
- Is accessibility supported?
- Is responsiveness considered?
- Is the component reusable?
- Can developers implement it consistently?

If any answer is negative, redesign the table.

---

# Validation Checklist

□ Purpose documented

□ Anatomy documented

□ Header row documented

□ Data rows documented

□ Cell structure documented

□ Accessibility reviewed

□ Documentation updated


---

# Table Types

## Philosophy

Every table should belong to one reusable component family.

Different table types solve different data presentation problems while sharing the same foundation.

Avoid building unrelated table components.

---

# Simple Table

## Purpose

Display structured information for quick comparison.

Examples:

- Orders
- Products
- Employees
- Invoices

Rules:

- Static content
- Minimal interaction
- Easy scanning

---

# Data Grid

## Purpose

Display interactive datasets.

Typical capabilities:

- Sorting
- Filtering
- Searching
- Selection
- Editing
- Bulk actions

Data grids support data management.

---

# Comparison Table

## Purpose

Compare multiple options.

Examples:

- Pricing plans
- Product features
- Subscription tiers

Differences should be easy to identify.

---

# Analytics Table

## Purpose

Display reporting data.

Examples:

- Revenue
- Sessions
- Conversion Rate
- Sales

Support numerical comparison.

---

# Financial Table

## Purpose

Display financial records.

Examples:

- Transactions
- Payments
- Expenses
- Budgets

Numbers should align consistently.

---

# Column Types

Columns may contain:

- Text
- Number
- Currency
- Date
- Status
- Badge
- Avatar
- Icon
- Progress
- Button
- Link
- Checkbox

Each column should contain one primary data type.

---

# Row Types

Rows may represent:

- Record
- Summary
- Group
- Total
- Expanded Row
- Child Row

Each row type should remain visually distinct.

---

# Sorting

Sorting changes the order of records.

Supported directions:

- Ascending
- Descending

Users should always know the current sort order.

---

# Filtering

Filtering reduces visible records.

Examples:

- Status
- Date
- Category
- Owner
- Priority

Active filters should remain visible.

---

# Search

Search locates records quickly.

Requirements:

- Fast response
- Relevant results
- Highlight matching values when appropriate

Search should reduce scanning effort.

---

# Pagination

Pagination divides large datasets.

Requirements:

- Current page
- Previous
- Next
- Rows per page
- Total records

Users should understand where they are.

---

# Sticky Header

Sticky headers remain visible while scrolling.

Recommended for:

- Large datasets
- Long tables

Headers should always align with columns.

---

# Sticky Columns

Sticky columns keep important information visible.

Examples:

- Name
- Identifier
- Order Number

Avoid freezing excessive columns.

---

# Row Actions

Rows may contain actions.

Examples:

- View
- Edit
- Delete
- Duplicate
- Share

Actions should remain easy to discover.

---

# Bulk Actions

Bulk actions operate on multiple selected rows.

Examples:

- Delete
- Export
- Archive
- Assign
- Update

Only display bulk actions after selection.

---

# Table Variants

Represent table types as variants.

Recommended properties:

Type

- Simple
- Grid
- Comparison
- Analytics
- Financial

Keep one reusable table family.

---

# Responsive Behavior

Tables should adapt across devices.

Strategies include:

- Horizontal scrolling
- Column priority
- Hidden secondary columns
- Responsive layouts

Preserve critical information first.

---

# AI Table Selection Engine

Before selecting a table type, answer:

- Is structured data required?
- Does the table support the user's task?
- Is scanning efficient?
- Is interaction necessary?
- Is responsiveness supported?
- Can this remain part of one component family?

If any answer is negative, choose a more appropriate presentation.

---

# Validation Checklist

□ Simple table documented

□ Data grid documented

□ Comparison table documented

□ Analytics table documented

□ Financial table documented

□ Column types documented

□ Row types documented

□ Sorting documented

□ Filtering documented

□ Search documented

□ Pagination documented

□ Sticky headers documented

□ Sticky columns documented

□ Row actions documented

□ Bulk actions documented

□ Responsive behavior documented

□ Variant strategy documented