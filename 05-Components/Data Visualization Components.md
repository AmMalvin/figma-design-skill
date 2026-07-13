---
title: Data Visualization Components
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
  - ../01-Foundation/Visual Hierarchy.md
  - ../02-Visual-System/Color Theory.md
  - ../02-Visual-System/Typography.md
  - ../02-Visual-System/Iconography.md
  - ../02-Visual-System/Spacing & Sizing.md
  - ./Component Principles.md
---

# Data Visualization Components

## Purpose

This module teaches the AI how to design scalable, reusable, accessible, and production-ready data visualization components.

Data visualizations help users understand information faster by revealing trends, comparisons, relationships, and patterns.

---

# Definition

Data visualization components communicate quantitative and qualitative information through visual representation.

Examples include:

- Charts
- Graphs
- KPIs
- Dashboards
- Timelines
- Gauges
- Heatmaps

Visualizations should support decision making.

---

# Objectives

After completing this module, the AI should be able to:

- Design reusable visualization components
- Improve data comprehension
- Support accessibility
- Build responsive visualizations
- Improve developer implementation
- Scale across products

---

# Visualization Philosophy

Every visualization should answer:

- What is being measured?
- Why does it matter?
- What action should users take?

Visualizations should simplify complex information.

---

# Core Principles

Always:

- Prioritize clarity.
- Remove unnecessary decoration.
- Label data clearly.
- Support accessibility.
- Maintain consistency.
- Design reusable components.

Never:

- Distort data.
- Hide important values.
- Use misleading scales.
- Depend only on color.
- Add unnecessary visual effects.

---

# Why Visualizations Exist

Visualization components help users:

- Compare values
- Discover trends
- Monitor performance
- Detect anomalies
- Track progress
- Make decisions

Every visualization should reduce cognitive effort.

---

# Component Anatomy

Every visualization should define:

- Container
- Title
- Subtitle
- Visualization area
- Labels
- Legend
- Tooltip
- Axis when applicable
- Supporting metrics

Each element should have one responsibility.

---

# Titles

Titles should explain:

- What users are viewing
- Time period when relevant
- Data context

Titles should remain concise.

---

# Legends

Legends explain visual encoding.

They should:

- Match chart colors
- Use clear labels
- Remain easy to scan

Avoid unnecessary legends.

---

# Labels

Labels should remain readable.

Include:

- Values
- Categories
- Units
- Dates when appropriate

Avoid overlapping labels.

---

# Hierarchy

Prioritize:

- Primary insight
- Visualization
- Supporting metrics
- Secondary information

Hierarchy should direct attention naturally.

---

# AI Decision Rules

Before approving a visualization, answer:

- Is the visualization appropriate?
- Is the message clear?
- Is accessibility supported?
- Is responsiveness supported?
- Is the component reusable?
- Can developers implement it consistently?

If any answer is negative, redesign the visualization.

---

# Validation Checklist

□ Purpose documented

□ Anatomy documented

□ Titles documented

□ Legends documented

□ Labels documented

□ Accessibility reviewed

□ Documentation updated


---

# Visualization Types

## Philosophy

Every visualization should belong to one reusable component family.

Different visualization types solve different analytical problems while sharing the same design language.

Avoid creating duplicate visualization components.

---

# KPI Card

## Purpose

Highlight important business metrics.

Examples:

- Revenue
- Active users
- Conversion rate
- Monthly recurring revenue
- Customer satisfaction

KPI cards should emphasize one primary metric.

---

# Line Chart

## Purpose

Display trends over time.

Examples:

- Revenue growth
- Daily users
- Website traffic
- Stock prices

Line charts should clearly communicate direction and change.

---

# Bar Chart

## Purpose

Compare values across categories.

Examples:

- Sales by region
- Product performance
- Department budgets

Bars should share a consistent baseline.

---

# Area Chart

## Purpose

Show trends while emphasizing volume.

Examples:

- Traffic over time
- Revenue accumulation
- Resource usage

Area charts should avoid overlapping multiple filled areas.

---

# Pie Chart

## Purpose

Display proportions of a whole.

Use only when:

- Few categories exist
- Total equals one hundred percent

Avoid excessive slices.

---

# Donut Chart

## Purpose

Display proportions while reserving the center for summary information.

Examples:

- Budget allocation
- Device distribution
- Market share

Center content should provide useful context.

---

# Scatter Plot

## Purpose

Display relationships between variables.

Examples:

- Revenue versus cost
- Height versus weight
- Age versus engagement

Scatter plots help identify correlations and outliers.

---

# Heatmap

## Purpose

Represent values through intensity.

Examples:

- User activity
- Calendar usage
- Performance metrics
- Geographic density

Never rely only on color intensity.

---

# Gauge

## Purpose

Communicate progress toward a target.

Examples:

- Capacity
- System health
- Goal completion

Use gauges sparingly.

---

# Progress Ring

## Purpose

Display completion of a measurable task.

Examples:

- Upload progress
- Profile completion
- Goal tracking

Progress should remain easy to interpret.

---

# Timeline

## Purpose

Display events in chronological order.

Examples:

- Project milestones
- Product roadmap
- Activity history

Timelines should clearly communicate sequence.

---

# Sparkline

## Purpose

Display compact trends alongside data.

Examples:

- KPI cards
- Financial reports
- Analytics tables

Sparklines should supplement larger metrics.

---

# Legend

## Purpose

Explain visual encoding.

Legends should include:

- Category labels
- Colors
- Symbols
- Patterns when required

Place legends close to the visualization.

---

# Visualization Selection Guide

Use:

KPI Card

For single metrics.

Line Chart

For trends over time.

Bar Chart

For comparisons.

Area Chart

For cumulative trends.

Pie Chart

For simple proportions.

Donut Chart

For proportions with summary information.

Scatter Plot

For relationships.

Heatmap

For density and intensity.

Gauge

For target progress.

Progress Ring

For completion.

Timeline

For chronological events.

Sparkline

For compact trend summaries.

---

# Visualization Variants

Represent visualizations as variants.

Recommended properties:

Type

- KPI
- Line
- Bar
- Area
- Pie
- Donut
- Scatter
- Heatmap
- Gauge
- Progress Ring
- Timeline
- Sparkline

State

- Default
- Hover
- Focus
- Selected
- Loading
- Empty

Size

- Small
- Medium
- Large

Avoid creating duplicate visualization components.

---

# Responsive Behavior

Desktop

- Full dashboards
- Multi-chart layouts
- Complex analytics

Tablet

- Two-column dashboards
- Medium charts
- KPI grids

Mobile

- KPI cards
- Compact charts
- Horizontal scrolling when necessary

Visualizations should remain readable across all devices.

---

# AI Visualization Selection Engine

Before selecting a visualization, answer:

- What relationship is being communicated?
- Is comparison or trend more important?
- Is the visualization easy to understand?
- Is accessibility supported?
- Is responsiveness supported?
- Can this remain part of one reusable component family?

If any answer is negative, choose a more appropriate visualization.

---

# Validation Checklist

□ KPI card documented

□ Line chart documented

□ Bar chart documented

□ Area chart documented

□ Pie chart documented

□ Donut chart documented

□ Scatter plot documented

□ Heatmap documented

□ Gauge documented

□ Progress ring documented

□ Timeline documented

□ Sparkline documented

□ Legend documented

□ Variant strategy documented

□ Responsive behavior documented

---

# Visualization States

## Philosophy

Every visualization should clearly communicate its current state.

Users should immediately understand:

- What data is displayed
- What is interactive
- What has changed
- What actions are available

Interactions should improve understanding.

---

# Default State

The visualization is fully rendered.

Requirements:

- Complete dataset
- Readable labels
- Visible legend
- Appropriate scaling

Default should establish the baseline presentation.

---

# Hover State

Hover reveals additional information.

Examples:

- Exact value
- Category
- Date
- Percentage
- Comparison

Hover should never hide existing information.

---

# Focus State

Focus supports keyboard navigation.

Requirements:

- Visible focus indicator
- High contrast
- Logical navigation order

Never remove focus indicators.

---

# Selected State

Selection highlights one or more data points.

Visual indicators may include:

- Accent outline
- Fill change
- Opacity adjustment
- Persistent tooltip

Selection should remain obvious.

---

# Loading State

Loading communicates that data is being retrieved.

Requirements:

- Skeleton placeholders
- Loading indicator
- Stable layout

Avoid unnecessary layout shifts.

---

# Empty State

Empty states explain why data is unavailable.

Examples:

- No records
- No matching filters
- No activity
- No results

Offer a useful next step whenever possible.

---

# Error State

Errors should explain:

- What failed
- Why when known
- How to recover

Provide actions such as:

- Retry
- Refresh
- Contact support

Avoid technical language.

---

# Tooltip Behavior

Tooltips provide contextual information.

Recommended content:

- Label
- Value
- Unit
- Percentage
- Date
- Comparison

Tooltips should never obscure critical information.

---

# Drill-down Interaction

Drill-down allows deeper exploration.

Examples:

- Year to month
- Region to city
- Category to product

Always provide a clear path back.

---

# Filtering

Filtering reduces visible data.

Requirements:

- Immediate feedback
- Clear active filters
- Easy reset

Filters should never modify the original dataset.

---

# Zoom and Pan

Large visualizations may support:

- Zoom
- Pan
- Reset view

Users should never lose orientation.

---

# Cross-highlighting

Related visualizations should communicate together.

Examples:

- Selecting a bar highlights a table row.
- Selecting a region updates KPI cards.
- Selecting a category filters supporting charts.

Relationships should remain obvious.

---

# Animation

Animation should communicate change.

Examples:

- Chart updates
- Filter transitions
- Data refresh
- Drill-down transitions

Animation should improve comprehension.

Avoid decorative animation.

---

# Responsive Behavior

Desktop

- Multi-chart dashboards
- Interactive exploration
- Detailed tooltips

Tablet

- Simplified dashboards
- Medium-sized charts
- Reduced labels

Mobile

- KPI cards
- Compact charts
- Horizontal scrolling when required

Visualizations should remain understandable across devices.

---

# AI Visualization Interaction Engine

Before approving visualization behavior, answer:

- Is interaction meaningful?
- Is exploration intuitive?
- Are tooltips useful?
- Is drill-down predictable?
- Is accessibility supported?
- Does animation improve understanding?

If any answer is negative, redesign the interaction.

---

# Validation Checklist

□ Visualization states documented

□ Hover state documented

□ Focus state documented

□ Selected state documented

□ Loading state documented

□ Empty state documented

□ Error state documented

□ Tooltip behavior documented

□ Drill-down documented

□ Filtering documented

□ Zoom and pan documented

□ Cross-highlighting documented

□ Animation documented

□ Responsive behavior validated

---

# Keyboard Interaction

## Purpose

Every interactive visualization should support keyboard navigation.

Minimum requirements:

- Tab moves focus
- Shift + Tab moves focus backward
- Arrow keys navigate data points when applicable
- Enter selects a focused element
- Escape closes temporary overlays
- Home moves to the first data point
- End moves to the last data point

Keyboard interaction should remain predictable.

---

# Focus Management

Focus should:

- Always remain visible
- Follow a logical order
- Move into interactive visualizations
- Return to the triggering control after closing overlays

Never lose keyboard focus.

---

# Screen Reader Support

Visualizations should expose:

- Chart title
- Chart type
- Summary
- Data labels
- Units
- Current selection

Users should understand the visualization without relying on sight.

---

# Accessible Chart Semantics

Every visualization should communicate:

- Purpose
- Data source when appropriate
- Current state
- Relationships
- Important insights

Semantics should accurately represent the visualization.

---

# Color Accessibility

Visualizations should never rely only on color.

Combine color with:

- Labels
- Patterns
- Shapes
- Icons
- Line styles
- Direct annotations

Every dataset should remain distinguishable.

---

# Data Labels

Labels should:

- Display meaningful values
- Avoid overlap
- Include units when required
- Support responsive layouts

Hide labels only when readability is improved.

---

# Legends

Legends should:

- Match the visual encoding
- Remain close to the visualization
- Preserve reading order
- Support keyboard navigation when interactive

Avoid unnecessary legends.

---

# Responsive Adaptation

Desktop

- Multi-chart dashboards
- Rich interaction
- Expanded legends

Tablet

- Simplified layouts
- Reduced labels
- Medium-sized charts

Mobile

- KPI cards
- Compact charts
- Scrollable visualizations
- Progressive disclosure

Visualizations should remain understandable on every device.

---

# Design Token Integration

Visualization components should reference design tokens.

Examples:

chart.background

chart.grid.color

chart.axis.color

chart.label.color

chart.tooltip.background

chart.radius

chart.spacing

chart.focus.ring

Avoid hardcoded values.

---

# Motion Guidelines

Motion should reinforce understanding.

Examples:

- Data updates
- Chart transitions
- Tooltip appearance
- Filter animation
- Drill-down transition

Motion should communicate change.

Avoid decorative animation.

---

# Documentation

Every visualization should document:

- Purpose
- Anatomy
- Variants
- States
- Accessibility
- Responsive behavior
- Usage guidelines
- Do
- Don't
- Examples

Documentation should eliminate implementation ambiguity.

---

# Testing

Every visualization should be tested for:

- Accessibility
- Keyboard interaction
- Screen reader support
- Responsive layouts
- Tooltip behavior
- Drill-down interaction
- Filtering
- Motion
- Performance

Testing should occur before release.

---

# Quality Assurance

Review every visualization for:

- Accuracy
- Accessibility
- Visual consistency
- Responsive behavior
- Design token usage
- Documentation
- Performance

Only approved visualizations belong in the design system.

---

# Versioning

Track changes for:

- New visualization types
- Accessibility improvements
- Motion updates
- Bug fixes
- Breaking changes

Maintain complete version history.

---

# Governance

Visualization updates should include:

- UX review
- Accessibility review
- Engineering review
- QA approval
- Documentation update

Governance maintains long-term consistency.

---

# AI Visualization Review Engine

Before publishing any visualization, answer:

- Is the chosen visualization appropriate?
- Is the primary insight obvious?
- Is accessibility complete?
- Are design tokens used?
- Is keyboard navigation supported?
- Has testing been completed?
- Does this scale across products?
- Is interaction predictable?

If any answer is negative, revise the visualization.

---

# Data Visualization Components Checklist

Before publishing:

□ Visualization anatomy documented

□ Variants completed

□ States documented

□ Keyboard interaction verified

□ Focus management documented

□ Screen reader support completed

□ Color accessibility validated

□ Responsive behavior validated

□ Design tokens integrated

□ Motion documented

□ Testing completed

□ QA approved

□ Version history updated

□ Documentation completed

---

# Key Takeaways

Data visualization components transform complex information into understandable insights.

The AI must:

- Choose the correct visualization.
- Preserve data accuracy.
- Highlight meaningful insights.
- Support keyboard navigation.
- Support screen readers.
- Avoid relying only on color.
- Use design tokens.
- Keep motion meaningful.
- Test every interaction.
- Document every behavior.

Every visualization should improve comprehension, accessibility, consistency, and long-term maintainability.