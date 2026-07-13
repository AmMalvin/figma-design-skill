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


---

# Card Sizes

## Philosophy

Card sizes should support different content densities while maintaining consistency.

Never create arbitrary dimensions.

---

# Standard Sizes

Recommended semantic sizes:

- Extra Small
- Small
- Medium
- Large
- Extra Large

Every size should reference design tokens.

---

# Width

Cards may use:

- Fixed width
- Flexible width
- Fill container
- Responsive width

Choose the width based on layout requirements.

Avoid unnecessary fixed dimensions.

---

# Height

Cards should expand naturally with content.

Use fixed heights only when consistency improves scanning.

Avoid clipping content.

---

# Internal Padding

Internal padding should remain consistent.

Padding separates:

- Header
- Body
- Footer
- Actions
- Media

Never allow content to touch card edges.

---

# Spacing

Maintain consistent spacing between:

- Headings
- Paragraphs
- Images
- Buttons
- Metadata

Spacing should establish visual hierarchy.

---

# Media

Cards may contain:

- Images
- Videos
- Illustrations
- Charts
- Maps

Media should enhance understanding.

Avoid decorative media without purpose.

---

# Images

Images should:

- Maintain aspect ratio
- Scale responsively
- Support lazy loading when implemented
- Preserve quality

Avoid image distortion.

---

# Avatars

Avatar usage:

- User profiles
- Authors
- Team members
- Organizations

Requirements:

- Consistent sizing
- Circular or documented shape
- Accessible alternative text where applicable

---

# Icons

Icons should:

- Support meaning
- Remain consistent
- Follow icon tokens

Avoid decorative icons that add no value.

---

# Card Actions

Cards may include:

- Primary button
- Secondary button
- Link
- Menu
- Icon button

Actions should remain easy to identify.

---

# Clickable Cards

Entire cards may be interactive.

Requirements:

- Visible hover state
- Visible focus state
- Clear affordance
- Accessible interaction

Users should immediately understand the card is clickable.

---

# Hover State

Hover should communicate interactivity.

Examples:

- Elevation
- Border
- Background
- Shadow

Avoid dramatic visual changes.

---

# Focus State

Focus should support keyboard users.

Requirements:

- Highly visible
- High contrast
- Consistent

Never remove focus indicators.

---

# Pressed State

Pressed confirms interaction.

Examples:

- Reduced elevation
- Slight scale change
- Background adjustment

Pressed feedback should feel immediate.

---

# Selected State

Selection should remain obvious.

Visual cues may include:

- Border
- Background
- Checkmark
- Accent color

Selection should not rely only on color.

---

# Disabled State

Disabled cards communicate temporary unavailability.

Requirements:

- Reduced emphasis
- No interaction
- Clear readability

Explain unavailable actions whenever possible.

---

# Loading State

Loading cards communicate pending content.

Requirements:

- Skeleton layout
- Placeholder content
- Preserved dimensions

Avoid large layout shifts.

---

# Skeleton Cards

Skeleton cards improve perceived performance.

Skeletons should:

- Match final layout
- Preserve spacing
- Minimize layout movement

Replace skeletons immediately after content loads.

---

# Overflow Behavior

Cards should handle long content gracefully.

Strategies include:

- Text wrapping
- Truncation
- Expandable sections
- Scroll only when necessary

Avoid broken layouts.

---

# Responsive Behavior

Cards should adapt across devices.

Maintain:

- Padding
- Hierarchy
- Readability
- Touch targets
- Media proportions

Cards should remain usable at every breakpoint.

---

# AI Card Interaction Engine

Before approving a card, answer:

- Is spacing consistent?
- Is content readable?
- Is media responsive?
- Are interaction states complete?
- Is accessibility supported?
- Can this scale across products?

If any answer is negative, redesign the interaction.

---

# Validation Checklist

□ Card sizes documented

□ Width behavior documented

□ Height behavior documented

□ Padding documented

□ Spacing reviewed

□ Media behavior documented

□ Images documented

□ Avatars documented

□ Actions documented

□ Hover state completed

□ Focus state completed

□ Pressed state completed

□ Selected state completed

□ Disabled state documented

□ Loading state documented

□ Skeleton cards documented

□ Responsive behavior validated


---

# Keyboard Interaction

## Purpose

Interactive cards should be fully operable using a keyboard.

Minimum requirements:

- Tab moves focus
- Shift + Tab moves focus backward
- Enter activates clickable cards
- Space activates controls when appropriate

Keyboard interaction should match user expectations.

---

# Focus Management

Focus should:

- Always remain visible
- Follow a logical order
- Never become trapped
- Return predictably after dialogs close

Never remove focus indicators.

---

# Accessibility Requirements

Every card should support:

- Keyboard navigation
- Screen readers
- Sufficient color contrast
- Visible focus
- Meaningful headings
- Accessible actions

Accessibility is mandatory.

---

# Screen Reader Support

Cards should expose meaningful information.

Interactive cards should provide:

- Accessible name
- Role
- State
- Action

Informational cards should maintain proper document structure.

---

# Card Collections

Cards often appear in groups.

Examples:

- Product grids
- Dashboards
- News feeds
- Search results
- User directories

Collections should maintain:

- Consistent spacing
- Predictable alignment
- Responsive layouts

---

# Grid Behavior

Cards should align to the layout grid.

Requirements:

- Consistent gutters
- Equal spacing
- Responsive columns
- Predictable wrapping

Avoid irregular alignment.

---

# Empty States

Cards should communicate when content is unavailable.

Examples:

- No products
- No messages
- No notifications
- No search results

Provide a helpful next action whenever possible.

---

# Responsive Adaptation

Cards should adapt across:

- Mobile
- Tablet
- Desktop
- Large displays

Maintain:

- Hierarchy
- Readability
- Touch targets
- Media proportions

Do not sacrifice usability.

---

# Design Token Integration

Cards should reference design tokens.

Examples:

card.padding

card.radius

card.background

card.border

card.shadow

card.spacing

Avoid hardcoded values.

---

# Motion Guidelines

Motion should support understanding.

Appropriate uses:

- Hover transitions
- Card expansion
- Selection feedback
- Loading transitions

Motion should remain subtle.

Avoid decorative animation.

---

# Documentation

Every card should document:

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

Every card should be tested for:

- Accessibility
- Keyboard interaction
- Responsive layouts
- Overflow behavior
- State transitions
- Loading behavior
- Performance

Testing should occur before release.

---

# Quality Assurance

Review every card for:

- Visual consistency
- Accessibility
- Responsive behavior
- Design token usage
- Documentation
- Performance

Only approved cards belong in the design system.

---

# Versioning

Track changes for:

- New variants
- Layout improvements
- Accessibility enhancements
- Bug fixes
- Breaking changes

Maintain complete version history.

---

# Governance

Card updates should follow a structured review process.

Every update should include:

- UX review
- Accessibility review
- Developer review
- QA approval
- Documentation update

Governance maintains consistency.

---

# AI Card Review Engine

Before publishing any card, answer:

- Is the content grouped logically?
- Is hierarchy immediately clear?
- Is the card reusable?
- Is accessibility complete?
- Are interaction states documented?
- Are design tokens used?
- Has testing been completed?
- Can this card scale across products?

If any answer is negative, revise the card.

---

# Cards Checklist

Before publishing:

□ Card anatomy documented

□ Variants completed

□ States documented

□ Keyboard interaction verified

□ Accessibility completed

□ Responsive behavior validated

□ Empty states documented

□ Design tokens integrated

□ Motion documented

□ Testing completed

□ QA approved

□ Version history updated

□ Documentation completed

---

# Key Takeaways

Cards organize related information into reusable containers.

The AI must:

- Group related content.
- Maintain clear hierarchy.
- Build reusable variants.
- Support keyboard and screen readers.
- Adapt cards across screen sizes.
- Use design tokens.
- Keep interactions predictable.
- Test every interaction state.
- Document every behavior.
- Govern changes through structured review.

Every card should improve readability, discoverability, accessibility, and long-term maintainability.