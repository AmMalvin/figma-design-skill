---
title: Cards
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
  - ../02-Visual-System/Iconography.md
  - ./Component Principles.md
---

# Cards

## Purpose

This module teaches the AI how to design scalable, reusable, accessible, and production-ready card components.

Cards organize related information into reusable containers.

---

# Definition

A card is a container that groups related content and actions into a single interactive or informational unit.

Cards improve readability by separating content into manageable sections.

---

# Objectives

After completing this module, the AI should be able to:

- Design reusable cards
- Build flexible layouts
- Improve information hierarchy
- Support responsive layouts
- Maintain accessibility
- Improve consistency
- Improve developer implementation
- Scale across products

---

# Card Philosophy

Cards should organize information.

Every card should answer:

- What information belongs together?
- What action can users perform?
- Does the content support one purpose?

Each card should represent one meaningful object.

---

# Core Principles

Always:

- Group related content.
- Maintain clear hierarchy.
- Keep layouts consistent.
- Support responsive resizing.
- Design reusable components.
- Use semantic variants.

Never:

- Mix unrelated content.
- Create oversized cards.
- Duplicate layouts unnecessarily.
- Hide important actions.
- Overload cards with information.

---

# Why Cards Exist

Cards help users:

- Browse content
- Compare information
- Complete actions
- Discover products
- Read summaries
- Navigate collections

Cards should improve scanning.

---

# Card Anatomy

Every card should define:

- Container
- Header
- Body
- Footer
- Media
- Actions
- Optional badge
- Optional status

Each section should have one responsibility.

---

# Container

The container controls:

- Width
- Height
- Padding
- Border
- Radius
- Elevation
- Background

The container should use design tokens.

---

# Header

The header introduces the content.

Examples:

- Product name
- User profile
- Article title
- Dashboard widget title

The header should communicate the card's purpose.

---

# Body

The body contains the primary information.

Examples:

- Description
- Statistics
- Metadata
- Preview
- Summary

Avoid unnecessary content.

---

# Footer

The footer contains supporting actions.

Examples:

- Buttons
- Links
- Status
- Metadata

The footer should remain visually separated from the body.

---

# Card Hierarchy

Cards should establish hierarchy through:

- Typography
- Spacing
- Color
- Layout
- Visual weight

Important information should appear first.

---

# AI Decision Rules

Before approving a card, answer:

- Is the content related?
- Is hierarchy clear?
- Is accessibility supported?
- Is the card reusable?
- Does it support responsive layouts?
- Can developers implement it consistently?

If any answer is negative, redesign the card.

---

# Validation Checklist

□ Purpose documented

□ Anatomy documented

□ Header defined

□ Body defined

□ Footer defined

□ Accessibility reviewed

□ Documentation updated


---

# Card Types

## Philosophy

Every card should belong to one reusable component family.

Different card types represent different content structures while sharing the same foundation.

Avoid creating unrelated card components when variants are sufficient.

---

# Basic Card

## Purpose

Display related information inside a simple container.

Examples:

- Information
- Summary
- Announcement
- Feature

Rules:

- Minimal layout
- Clear hierarchy
- Optional actions

Basic cards should remain flexible.

---

# Product Card

## Purpose

Display products.

Typical content:

- Product image
- Product name
- Price
- Rating
- Availability
- Primary action

Product cards should help users compare items quickly.

---

# Profile Card

## Purpose

Display people or organizations.

Examples:

- User
- Team member
- Author
- Company

Typical content:

- Avatar
- Name
- Role
- Description
- Actions

Profile cards should establish identity clearly.

---

# Dashboard Card

## Purpose

Display dashboard information.

Examples:

- Revenue
- Sales
- Active Users
- Performance

Typical content:

- Metric
- Trend
- Status
- Action

Dashboard cards should prioritize readability.

---

# Statistics Card

## Purpose

Present numerical information.

Examples:

- Total Orders
- Conversion Rate
- Revenue
- Sessions

Rules:

- Large metric
- Supporting context
- Trend indicator
- Optional comparison

Statistics should be immediately understandable.

---

# Media Card

## Purpose

Display visual content.

Examples:

- Video
- Image
- Gallery
- Course

Requirements:

- Media preview
- Title
- Description
- Action

Media should remain the primary visual focus.

---

# Article Card

## Purpose

Preview written content.

Typical content:

- Cover image
- Title
- Summary
- Author
- Reading time
- Category

Users should understand the article before opening it.

---

# Pricing Card

## Purpose

Compare pricing plans.

Typical content:

- Plan name
- Price
- Features
- CTA
- Highlighted plan

Pricing cards should simplify comparison.

---

# Interactive Card

## Purpose

Support direct interaction.

Examples:

- Selectable card
- Expandable card
- Clickable card
- Navigation card

Users should clearly understand that the card is interactive.

---

# Expandable Card

## Purpose

Reveal additional information.

Requirements:

- Clear expand control
- Smooth expansion
- Preserve surrounding layout

Expanded content should remain organized.

---

# Selection Card

## Purpose

Allow users to choose an option.

Examples:

- Payment method
- Shipping option
- Subscription plan

Requirements:

- Selected state
- Keyboard support
- Accessible labels

Selection should remain obvious.

---

# Status Card

## Purpose

Communicate system status.

Examples:

- Success
- Warning
- Error
- Information

Status should be understandable without relying only on color.

---

# Card Selection Guide

Use:

Basic Card

For general grouped content.

Product Card

For commerce.

Profile Card

For people.

Dashboard Card

For analytics.

Statistics Card

For metrics.

Media Card

For visual content.

Article Card

For editorial content.

Pricing Card

For plan comparison.

Interactive Card

For user actions.

Expandable Card

For progressive disclosure.

Selection Card

For choosing options.

Status Card

For system feedback.

---

# Card Variants

Represent card types as variants.

Recommended properties:

Type

- Basic
- Product
- Profile
- Dashboard
- Statistics
- Media
- Article
- Pricing
- Interactive
- Expandable
- Selection
- Status

Avoid creating unrelated card components.

---

# Responsive Behavior

Cards should adapt to available space.

Requirements:

- Flexible width
- Flexible height
- Responsive media
- Content reflow
- Consistent spacing

Cards should remain readable across devices.

---

# AI Card Selection Engine

Before selecting a card type, answer:

- Does this card represent one object?
- Is the layout appropriate?
- Is the hierarchy clear?
- Is responsiveness supported?
- Is the card reusable?
- Can this remain part of one component family?

If any answer is negative, choose a better card variant.

---

# Validation Checklist

□ Basic card documented

□ Product card documented

□ Profile card documented

□ Dashboard card documented

□ Statistics card documented

□ Media card documented

□ Article card documented

□ Pricing card documented

□ Interactive card documented

□ Expandable card documented

□ Selection card documented

□ Status card documented

□ Variant strategy documented

□ Responsive behavior documented