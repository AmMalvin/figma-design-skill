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