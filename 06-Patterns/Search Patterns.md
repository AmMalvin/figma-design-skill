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

---

# Search States

## Philosophy

Every search workflow should clearly communicate its current state.

Users should always understand:

- What is happening
- Whether search is working
- How many results are available
- What they should do next

Search should never leave users uncertain.

---

# Loading Results

## Purpose

Communicate that search is processing.

Requirements:

- Skeleton results when appropriate
- Loading indicator
- Preserve search query
- Avoid layout shifts

Loading should feel responsive.

---

# Search Results

## Purpose

Present relevant information clearly.

Results should:

- Prioritize relevance
- Be easy to scan
- Highlight useful metadata
- Support quick actions

Show the best matches first.

---

# Empty Results

## Purpose

Explain when no matches are found.

Requirements:

- Explain no results
- Preserve the user's query
- Suggest refinements
- Offer alternative actions

Never present a blank screen.

---

# Error State

Errors should communicate:

- What happened
- Why when known
- How users recover

Examples:

- Retry search
- Check connection
- Modify query

Errors should not erase the search query.

---

# No Match Guidance

Help users improve unsuccessful searches.

Examples:

- Check spelling
- Use fewer keywords
- Remove filters
- Search broader categories

Guidance should reduce repeated failures.

---

# Query Correction

Suggest corrections when appropriate.

Examples:

- Spelling corrections
- Similar terms
- Singular or plural variations
- Common aliases

Never replace the original query automatically.

---

# Search Highlighting

Highlight matching content.

Examples:

- Matching keywords
- Matching names
- Matching descriptions

Highlighting should improve scanning.

---

# Search Result Grouping

Group related results when appropriate.

Examples:

- Products
- Documents
- Users
- Projects
- Commands

Grouping should improve navigation.

---

# Pagination

Use pagination when:

- Result sets are large
- Users frequently revisit previous pages
- Stable navigation is required

Display:

- Current page
- Total pages when known
- Previous
- Next

Pagination should preserve filters and sorting.

---

# Infinite Scrolling

Use infinite scrolling when:

- Users are browsing
- Discovery is the primary goal
- Content loads continuously

Requirements:

- Visible loading feedback
- Preserve scroll position
- Prevent duplicate loading

Avoid infinite scrolling when users need precise navigation.

---

# Search Persistence

Preserve:

- Search query
- Active filters
- Sorting
- Scroll position
- Selected scope

Users should not lose search context.

---

# Search Analytics

Measure:

- Query success
- Zero-result searches
- Refinement rate
- Result selection rate
- Average search time
- Search abandonment

Analytics should improve future search quality.

---

# AI Search Evaluation Engine

Before approving a search workflow, answer:

- Are results relevant?
- Is loading communicated?
- Can users recover from failed searches?
- Are queries preserved?
- Is accessibility supported?
- Does this reuse existing components?

If any answer is negative, redesign the workflow.

---

# Validation Checklist

□ Loading results documented

□ Search results documented

□ Empty results documented

□ Error state documented

□ No match guidance documented

□ Query correction documented

□ Search highlighting documented

□ Result grouping documented

□ Pagination documented

□ Infinite scrolling documented

□ Search persistence documented

□ Search analytics documented


---

# Accessibility Across Search

## Purpose

Every search experience should be accessible from beginning to completion.

Users should be able to search regardless of:

- Device
- Input method
- Ability
- Platform

Accessibility should exist throughout the search journey.

---

# Keyboard Navigation

Search should fully support keyboard interaction.

Requirements:

- Logical tab order
- Visible focus
- Arrow key navigation for suggestions
- Enter selects highlighted suggestions
- Escape closes suggestions
- Tab moves naturally between controls

Users should complete search without a mouse.

---

# Focus Management

Focus should:

- Move to the search field when appropriate
- Remain visible
- Enter suggestion lists
- Return after temporary interfaces close
- Never become trapped unintentionally

Focus should always reflect the current task.

---

# Screen Reader Support

Search should expose:

- Search field label
- Placeholder guidance
- Number of search results
- Active filters
- Suggested queries
- Loading status
- Empty results
- Error messages

Users should always understand the current search state.

---

# Responsive Search

Desktop

- Persistent search field
- Advanced filtering
- Multi-column results
- Keyboard shortcuts

Tablet

- Adaptive layouts
- Expandable filters
- Responsive result grids

Mobile

- Full-screen search
- Bottom sheet filters
- Voice search
- Thumb-friendly interactions

Search behavior should remain consistent across devices.

---

# Search Performance

Search should:

- Respond quickly
- Preserve user input
- Minimize unnecessary loading
- Avoid blocking interactions
- Load additional results efficiently

Performance should support continuous searching.

---

# Design Token Integration

Search should reference design tokens.

Examples:

search.spacing

search.radius

search.focus.ring

search.motion.duration

search.highlight.color

search.border.color

search.background.color

Avoid hardcoded values.

---

# Documentation Standards

Every search workflow should document:

- Purpose
- User goal
- Search scope
- Workflow
- States
- Filters
- Sorting
- Accessibility
- Responsive behavior
- Components used
- Usage guidelines
- Do
- Don't
- Examples

Documentation should remove implementation ambiguity.

---

# Testing Strategy

Every search workflow should be tested for:

- Accessibility
- Keyboard navigation
- Screen reader compatibility
- Responsive layouts
- Loading performance
- Empty results
- Error recovery
- Filter behavior
- Sorting
- Search persistence

Testing should validate the complete search experience.

---

# Quality Assurance

Review every search workflow for:

- Result relevance
- Accessibility
- Workflow consistency
- Component reuse
- Responsive behavior
- Documentation
- Performance

Only approved search patterns belong in the design system.

---

# Versioning

Track changes for:

- Search improvements
- Ranking updates
- Accessibility improvements
- Performance optimizations
- Bug fixes
- Breaking changes

Maintain complete version history.

---

# Governance

Search updates should include:

- UX review
- Accessibility review
- Product review
- Engineering review
- QA approval
- Documentation update

Governance ensures long-term consistency.

---

# AI Search Review Engine

Before publishing any search workflow, answer:

- Are results relevant?
- Is accessibility complete?
- Is keyboard navigation supported?
- Are filters intuitive?
- Is search context preserved?
- Are design tokens used?
- Has testing been completed?
- Does this reuse existing components?

If any answer is negative, revise the workflow.

---

# Search Checklist

Before publishing:

□ Search workflow documented

□ Search states documented

□ Filters documented

□ Sorting documented

□ Accessibility completed

□ Keyboard navigation verified

□ Screen reader support completed

□ Responsive behavior validated

□ Search performance validated

□ Design tokens integrated

□ Testing completed

□ QA approved

□ Version history updated

□ Documentation completed

---

# Key Takeaways

Search should help users find information with the least possible effort.

The AI must:

- Prioritize relevant results.
- Reduce typing.
- Preserve search context.
- Support progressive refinement.
- Support keyboard navigation.
- Support screen readers.
- Use design tokens.
- Optimize performance.
- Test complete search workflows.
- Document every search experience.

Every search pattern should improve discoverability, accessibility, consistency, performance, and long-term maintainability.