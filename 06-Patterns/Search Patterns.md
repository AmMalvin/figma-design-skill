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