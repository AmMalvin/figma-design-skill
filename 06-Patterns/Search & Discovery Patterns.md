---
title: Search & Discovery Patterns
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
  - ../05-Components/Search.md
  - ../05-Components/Inputs & Forms.md
  - ../05-Components/Data Display.md
  - ../05-Components/Navigation Components.md
  - ../05-Components/Feedback Components.md
  - ../05-Components/Buttons.md
---

# Search & Discovery Patterns

## Purpose

This module teaches the AI how to design fast, predictable, and scalable search and discovery experiences.

Search should help users find information with minimal effort.

---

# Definition

Search allows users to locate known information using queries.

Discovery helps users explore relevant information through browsing, recommendations, filtering, and navigation.

---

# Objectives

After completing this module, the AI should be able to:

- Design search experiences
- Improve findability
- Support exploration
- Reduce search effort
- Improve search relevance
- Scale search across products

---

# Search Philosophy

Every search workflow should answer:

- What is the user trying to find?
- How quickly can they find it?
- How can results be refined?
- What happens when nothing is found?
- How can new content be discovered?

Search should reduce effort.

---

# Core Principles

Always:

- Prioritize relevant results.
- Support refinement.
- Preserve search context.
- Reuse existing components.
- Support accessibility.
- Explain search status.

Never:

- Hide search unexpectedly.
- Return confusing results.
- Lose user queries unnecessarily.
- Force advanced search.
- Duplicate search workflows.

---

# Search Lifecycle

Every workflow should define:

- Search entry
- Query
- Suggestions
- Results
- Refinement
- Selection
- Completion

Each stage should remain predictable.

---

# Search Types

Common search models include:

- Global search
- Local search
- Keyword search
- Full-text search
- Faceted search
- Semantic search
- Advanced search

Choose the model based on user needs.

---

# Pattern Composition

Search should reuse existing components.

Examples:

- Inputs
- Buttons
- Lists
- Tables
- Cards
- Filters
- Badges
- Empty states
- Pagination

Avoid search-specific components when reusable components already exist.

---

# Success Metrics

Measure search using:

- Search success rate
- Time to result
- Query refinement rate
- Zero-result rate
- Result selection rate
- Task completion rate

Measure successful discovery instead of search volume.

---

# AI Decision Rules

Before approving a search workflow, answer:

- Does it help users find information quickly?
- Is refinement available?
- Is accessibility supported?
- Does it reuse existing components?
- Is the workflow predictable?
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

# Search Entry Workflows

## Philosophy

Every search workflow should reduce effort while improving findability.

Users should always understand:

- What can be searched
- Where they are searching
- How to refine results
- What happens after submitting a query

Search should feel immediate.

---

# Global Search

## Purpose

Allow users to search across the entire product.

Requirements:

- Always accessible
- Consistent location
- Broad search scope
- Fast response
- Preserve entered query

Global search should search everything users expect.

---

# Local Search

## Purpose

Search within the current section.

Examples:

- Projects
- Messages
- Files
- Customers
- Reports

Clearly communicate the current search scope.

---

# Search Bar

## Purpose

Provide a clear search entry point.

Requirements:

- Visible search field
- Search icon
- Accessible label
- Clear placeholder
- Clear button

Search fields should remain easy to locate.

---

# Autocomplete

## Purpose

Reduce typing effort.

Requirements:

- Relevant suggestions
- Keyboard navigation
- Mouse selection
- Highlight matching text
- Maximum of 5 to 10 suggestions

Only show high-quality suggestions.

---

# Search Suggestions

## Purpose

Help users form better queries.

Examples:

- Popular searches
- Predicted queries
- Categories
- Related topics

Suggestions should remain relevant.

---

# Recent Searches

## Purpose

Allow users to repeat previous searches.

Requirements:

- Most recent first
- Easy removal
- Privacy controls
- Optional clearing

Users should control search history.

---

# Saved Searches

## Purpose

Allow users to reuse complex searches.

Requirements:

- Custom name
- Editable
- Deletable
- Shareable when appropriate

Saved searches should reduce repetitive work.

---

# Voice Search

## Purpose

Allow spoken search input.

Requirements:

- Clear activation
- Permission handling
- Visible listening state
- Editable transcript

Voice search should always allow manual editing.

---

# Image Search

## Purpose

Allow users to search using images.

Examples:

- Product lookup
- Visual similarity
- Document recognition

Provide clear upload guidance.

---

# Advanced Search

## Purpose

Support complex search requirements.

Examples:

- Multiple fields
- Date ranges
- Boolean logic
- Metadata filters

Advanced search should remain optional.

---

# Search Scopes

## Purpose

Allow users to limit where search applies.

Examples:

- Entire workspace
- Current project
- Files only
- Messages only
- Users only

Scopes should always remain visible.

---

# Search Selection Guide

Use:

Global Search

For searching the entire product.

Local Search

For searching the current section.

Autocomplete

For reducing typing.

Search Suggestions

For improving queries.

Recent Searches

For repeated searches.

Saved Searches

For recurring workflows.

Voice Search

For hands-free interaction.

Image Search

For visual lookup.

Advanced Search

For complex filtering.

Search Scopes

For narrowing results.

---

# Workflow Variants

Represent search entry as reusable patterns.

Recommended properties:

Workflow

- Global
- Local
- Suggestion
- Autocomplete
- Voice
- Image
- Advanced

State

- Idle
- Typing
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

- Persistent search bar
- Expanded suggestions
- Advanced search panel

Tablet

- Adaptive layouts
- Touch-friendly suggestions

Mobile

- Full-screen search
- Bottom sheet filters
- Compact autocomplete
- Voice search when available

Search behavior should remain consistent across platforms.

---

# AI Search Selection Engine

Before selecting a search workflow, answer:

- Does this reduce search effort?
- Are suggestions relevant?
- Is accessibility supported?
- Does this reuse existing components?
- Is the workflow predictable?
- Can this scale across products?

If any answer is negative, redesign the workflow.

---

# Validation Checklist

□ Global search documented

□ Local search documented

□ Search bar documented

□ Autocomplete documented

□ Search suggestions documented

□ Recent searches documented

□ Saved searches documented

□ Voice search documented

□ Image search documented

□ Advanced search documented

□ Search scopes documented

□ Responsive behavior documented