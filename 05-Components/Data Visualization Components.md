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