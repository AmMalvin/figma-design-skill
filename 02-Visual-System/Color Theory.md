---
title: Color Theory
version: 1.0.0
status: Stable
owner: Design System Skill
category: Visual System
priority: Critical
last_updated: 2026-07-12

inherits:
  - ../00-Core/Universal Design Principles.md
  - ../01-Foundation/Accessibility.md
  - ../01-Foundation/Cognitive Psychology.md
  - ../01-Foundation/Visual Hierarchy.md
  - ../01-Foundation/Layout Systems.md
---

# Color Theory

## Purpose

This module teaches the AI how to build accessible, scalable, consistent color systems for digital products.

The AI should understand color as a communication system rather than decoration.

Every color should communicate purpose.

---

# Definition

Color Theory is the practice of selecting, organizing, and applying colors to improve usability, accessibility, hierarchy, branding, and emotional communication.

Every color should have a defined role.

---

# Objectives

After completing this module, the AI should be able to:

- Build accessible color systems
- Create semantic color tokens
- Design light and dark themes
- Improve visual hierarchy
- Improve readability
- Communicate status
- Reinforce branding
- Reduce visual noise
- Support scalability

---

# Color Mindset

Never ask:

"Which color looks better?"

Always ask:

- What does this color communicate?
- Does it improve usability?
- Does it strengthen hierarchy?
- Is it accessible?
- Does it belong in the design system?

---

# Core Principles

Always:

- Assign every color a purpose.
- Build semantic color systems.
- Support accessibility.
- Maintain consistency.
- Use neutral colors generously.
- Test contrast.

Never:

- Choose colors randomly.
- Depend on color alone.
- Create duplicate semantic colors.
- Use brand colors everywhere.
- Overuse saturated colors.

---

# Color Roles

Every product should define:

- Brand colors
- Neutral colors
- Semantic colors
- Surface colors
- Text colors
- Border colors
- Interactive colors
- Overlay colors

Each role should remain independent.

---

# Primitive Colors

Primitive colors are raw color values.

Examples:

Blue 50

Blue 100

Blue 200

...

Blue 900

Primitive colors should never reference product meaning.

---

# Semantic Colors

Semantic colors communicate purpose.

Examples:

Primary

Secondary

Success

Warning

Danger

Info

Background

Surface

Border

Text

Link

Focus

Semantic colors should reference primitive colors.

Never hardcode primitive values into components.

---

# Color Communication

Color should communicate:

- Status
- Priority
- Feedback
- Interaction
- Hierarchy
- Branding
- Accessibility

Color should never be purely decorative.

---

# Emotional Communication

Color influences perception.

The AI should understand emotional associations without depending on stereotypes.

Evaluate color choices within:

- Brand identity
- Product context
- User expectations
- Accessibility requirements

---

# AI Decision Rules

Before approving any color:

- Does it have a defined purpose?
- Is it semantic?
- Does it improve usability?
- Is accessibility maintained?
- Is the color reusable?
- Can it scale across themes?

If any answer is negative, redesign the color system.

---

# Validation Checklist

□ Primitive palette defined

□ Semantic palette defined

□ Color roles documented

□ Accessibility reviewed

□ Reusability validated

□ Scalability reviewed

□ Documentation updated

---

# Color Wheel

## Definition

The color wheel is the foundation of color relationships.

It organizes colors by hue and helps designers create balanced and harmonious color systems.

Every color decision should begin with an understanding of the color wheel.

---

# Primary Colors

Primary colors cannot be created by mixing other colors.

Digital interfaces commonly use RGB as the underlying color model.

Primary RGB colors:

- Red
- Green
- Blue

These combine to create every display color.

---

# Secondary Colors

Secondary colors are created by combining two primary colors.

Examples:

- Cyan
- Magenta
- Yellow

Understanding relationships between hues helps create predictable palettes.

---

# Tertiary Colors

Tertiary colors sit between primary and secondary colors.

They create smoother transitions across palettes.

Examples include:

- Blue Green
- Yellow Green
- Red Orange
- Blue Violet

---

# Hue

## Definition

Hue is the position of a color on the color wheel.

Hue is measured from:

0°

↓

360°

Changing hue changes the perceived color without changing brightness or saturation.

---

# Saturation

## Definition

Saturation controls color intensity.

High saturation creates:

- Strong emphasis
- Vibrant interfaces
- Bold accents

Low saturation creates:

- Calm interfaces
- Neutral surfaces
- Supporting content

Avoid excessive saturation throughout the interface.

---

# Value

## Definition

Value represents how light or dark a color appears.

Higher value creates lighter colors.

Lower value creates darker colors.

Value strongly influences readability and contrast.

---

# Brightness

Brightness controls perceived light intensity.

Use brightness to:

- Build color scales
- Create elevation
- Improve readability
- Support dark mode

Brightness should reinforce hierarchy.

---

# Tint

A tint is created by adding white.

Use tints for:

- Backgrounds
- Subtle highlights
- Soft surfaces
- Hover states

---

# Shade

A shade is created by adding black.

Use shades for:

- Text
- Borders
- Active states
- Strong emphasis

---

# Tone

A tone is created by reducing color intensity with neutral gray.

Tones improve:

- Sophistication
- Readability
- Balance
- Large interfaces

Avoid using fully saturated colors for every UI element.

---

# Color Temperature

Colors are generally perceived as:

Warm

- Red
- Orange
- Yellow

Cool

- Blue
- Green
- Purple

Temperature influences emotional perception and hierarchy.

Choose temperature intentionally.

---

# Color Harmony

## Definition

Color harmony describes combinations of colors that work well together.

Harmony improves:

- Readability
- Balance
- Recognition
- Brand consistency

Harmony should support communication rather than decoration.

---

# Monochromatic Harmony

Uses different values and saturations of one hue.

Benefits:

- Consistency
- Simplicity
- Strong branding
- Easy maintenance

Recommended for enterprise applications.

---

# Analogous Harmony

Uses neighboring hues on the color wheel.

Benefits:

- Smooth transitions
- Natural appearance
- Low visual tension

Useful for illustrations and supporting interfaces.

---

# Complementary Harmony

Uses colors opposite each other on the color wheel.

Benefits:

- High contrast
- Strong emphasis
- Clear focal points

Use complementary colors carefully.

Excessive use creates visual fatigue.

---

# Split Complementary

Uses one base color and the two adjacent colors opposite it.

Provides:

- Strong contrast
- Better balance
- Greater flexibility

Suitable for modern interfaces.

---

# Triadic Harmony

Uses three evenly spaced hues.

Benefits:

- Balanced variety
- Strong differentiation
- Visual energy

Maintain one dominant color.

Use the others as supporting colors.

---

# Tetradic Harmony

Uses four hues arranged as two complementary pairs.

Suitable for:

- Complex dashboards
- Data visualization
- Rich visual systems

Maintain clear visual hierarchy.

---

# AI Color Selection Rules

Before selecting colors, answer:

- Does each color have a purpose?
- Is the harmony appropriate?
- Is saturation balanced?
- Does value support readability?
- Does temperature reinforce the intended experience?
- Will the palette scale across themes?

Revise until every answer is positive.

---

# Validation Checklist

□ Hue relationships reviewed

□ Saturation balanced

□ Value hierarchy defined

□ Tints created

□ Shades created

□ Tones created

□ Color harmony selected

□ Temperature evaluated

□ Palette documented