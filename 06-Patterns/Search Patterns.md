---
title: Search Patterns
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
  - ../05-Components/Navigation Components.md
  - ../05-Components/Feedback Components.md
  - ../05-Components/Data Visualization Components.md
---

# Search Patterns

## Purpose

This module teaches the AI how to design fast, relevant, accessible, and scalable search experiences.

Search should help users locate information with the fewest possible interactions.

---

# Definition

Search enables users to locate information, content, people, products, or actions using keywords, filters, and refinement tools.

Search should prioritize relevance over quantity.

---

# Objectives

After completing this module, the AI should be able to:

- Design intuitive search workflows
- Improve search efficiency
- Reduce search abandonment
- Support progressive refinement
- Improve result relevance
- Scale search across products

---

# Search Philosophy

Every search experience should answer:

- What is the user trying to find?
- How quickly can results appear?
- How can users refine results?
- What happens when nothing matches?

Search should reduce effort rather than increase navigation.

---

# Core Principles

Always:

- Prioritize relevance.
- Support refinement.
- Show useful feedback.
- Preserve search context.
- Reuse existing components.
- Support accessibility.

Never:

- Return irrelevant results first.
- Hide available filters.
- Lose user queries.
- Require unnecessary typing.
- Force users through multiple screens.

---

# Search Lifecycle

Every search workflow should define:

- Entry
- Query
- Suggestions
- Results
- Refinement
- Selection
- Completion

Every stage should reduce effort.

---

# Search Types

Common search experiences include:

- Global search
- Local search
- Command search
- Product search
- Document search
- User search

Select the search type based on user intent.

---

# Pattern Composition

Search patterns should reuse existing components.

Examples:

- Search fields
- Buttons
- Filters
- Chips
- Lists
- Tables
- Cards
- Empty states

Avoid creating search-specific UI when reusable components already exist.

---

# Success Metrics

Measure search using:

- Search success rate
- Time to result
- Zero-result rate
- Query refinement rate
- Search abandonment
- Result selection rate

Measure outcomes instead of search volume.

---

# AI Decision Rules

Before approving a search pattern, answer:

- Does search reduce effort?
- Are relevant results prioritized?
- Is accessibility supported?
- Does this reuse existing components?
- Can users refine results easily?
- Can developers implement this consistently?

If any answer is negative, redesign the workflow.

---

# Validation Checklist

□ Purpose documented

□ Search lifecycle documented

□ Search types documented

□ Component composition documented

□ Success metrics documented

□ Accessibility reviewed

□ Documentation updated


---

# Search Workflows

## Philosophy

Every search workflow should reduce the effort required to find information.

Users should always understand:

- What they are searching
- What results are available
- How to refine results
- What to do when results are unavailable

Search should minimize typing.

---

# Search Field

## Purpose

Provide the primary entry point for search.

Requirements:

- Visible placeholder
- Clear search icon
- Clear button
- Keyboard support
- Autofocus when appropriate

Search fields should communicate searchable content.

---

# Autocomplete

## Purpose

Reduce typing effort.

Suggestions should appear while users type.

Suggestions may include:

- Matching queries
- Products
- Documents
- Users
- Commands

Autocomplete should never interrupt typing.

---

# Search Suggestions

## Purpose

Guide users toward useful searches.

Examples:

- Predicted queries
- Categories
- Popular keywords
- Related searches

Suggestions should improve discovery.

---

# Recent Searches

## Purpose

Help users quickly repeat previous searches.

Requirements:

- Clearly separated
- Easy removal
- Privacy aware

Allow users to clear search history.

---

# Popular Searches

## Purpose

Help users discover common searches.

Examples:

- Trending products
- Frequently viewed topics
- Common documents

Popular searches should remain relevant.

---

# Search History

## Purpose

Allow users to revisit previous searches.

Requirements:

- Easy access
- Easy deletion
- Privacy controls

Search history should never expose sensitive information.

---

# Voice Search

## Purpose

Support spoken queries.

Requirements:

- Clear microphone action
- Permission guidance
- Visible listening state
- Error handling

Provide a text alternative.

---

# Filters

## Purpose

Reduce result sets.

Examples:

- Category
- Date
- Status
- Price
- Author
- Type

Filters should be easy to remove.

---

# Faceted Search

## Purpose

Allow users to refine results across multiple attributes.

Examples:

- Brand
- Color
- Size
- Department
- File type

Users should combine multiple filters.

---

# Sorting

## Purpose

Reorder search results.

Examples:

- Relevance
- Date
- Alphabetical
- Price
- Rating

Default sorting should prioritize relevance.

---

# Saved Searches

## Purpose

Allow users to reuse common searches.

Examples:

- Saved filters
- Saved queries
- Notifications

Saved searches should update automatically when appropriate.

---

# Search Selection Guide

Use:

Search Field

For entering search terms.

Autocomplete

To reduce typing.

Search Suggestions

To encourage discovery.

Recent Searches

For repeated queries.

Popular Searches

For exploration.

Voice Search

For hands-free input.

Filters

For narrowing results.

Faceted Search

For complex refinement.

Sorting

For ordering results.

Saved Searches

For repeated workflows.

---

# Search Variants

Represent search as reusable patterns.

Recommended properties:

Type

- Global
- Local
- Command
- Product
- Document
- User

State

- Default
- Typing
- Suggesting
- Loading
- Results
- Empty
- Error

Platform

- Web
- Mobile
- Desktop

Avoid duplicate search workflows.

---

# Responsive Behavior

Desktop

- Persistent search
- Advanced filters
- Multi-column results

Tablet

- Adaptive layouts
- Expandable filters

Mobile

- Full-screen search
- Bottom sheet filters
- Voice search
- Compact results

Search behavior should remain consistent across platforms.

---

# AI Search Selection Engine

Before selecting a search workflow, answer:

- Does this reduce typing?
- Are relevant suggestions available?
- Can users refine results easily?
- Is accessibility supported?
- Does this reuse existing components?
- Can this scale across products?

If any answer is negative, redesign the search workflow.

---

# Validation Checklist

□ Search field documented

□ Autocomplete documented

□ Search suggestions documented

□ Recent searches documented

□ Popular searches documented

□ Search history documented

□ Voice search documented

□ Filters documented

□ Faceted search documented

□ Sorting documented

□ Saved searches documented

□ Responsive behavior documented