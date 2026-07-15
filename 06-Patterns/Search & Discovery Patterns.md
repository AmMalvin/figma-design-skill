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