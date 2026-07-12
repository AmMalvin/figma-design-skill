---
title: Typography
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
  - ../02-Visual-System/Color Theory.md
---

# Typography

## Purpose

This module teaches the AI how to create readable, accessible, scalable typography systems for digital products.

Typography is the primary method of communicating information in user interfaces.

Every typography decision should improve understanding.

---

# Definition

Typography is the system of organizing text through font selection, sizing, spacing, hierarchy, rhythm, and alignment to improve communication and usability.

Typography is a functional system.

It is not decoration.

---

# Objectives

After completing this module, the AI should be able to:

- Build typography systems
- Create clear hierarchy
- Improve readability
- Improve accessibility
- Build semantic typography tokens
- Create responsive typography
- Maintain consistency
- Support localization
- Improve developer handoff

---

# Typography Mindset

Never ask:

"Which font looks better?"

Always ask:

- Is this readable?
- Does this improve hierarchy?
- Is the purpose clear?
- Is accessibility maintained?
- Can this scale across products?

---

# Core Principles

Always:

- Prioritize readability.
- Maintain hierarchy.
- Use consistent spacing.
- Build reusable text styles.
- Support accessibility.
- Design for scanning.

Never:

- Use too many fonts.
- Create unnecessary text styles.
- Reduce readability for aesthetics.
- Use decorative fonts for body content.
- Create inconsistent typography.

---

# Typography Goals

Typography should:

- Communicate clearly
- Organize information
- Support scanning
- Reinforce hierarchy
- Improve accessibility
- Strengthen brand identity

---

# Typography Roles

Every product should define:

- Display
- Heading
- Title
- Subtitle
- Body
- Label
- Button
- Caption
- Helper Text
- Overline
- Code

Each role should have one clear purpose.

---

# Typography Consistency

Typography should remain consistent across:

- Pages
- Components
- Forms
- Dashboards
- Tables
- Navigation
- Dialogs
- Documentation

Consistency improves recognition.

---

# AI Decision Rules

Before approving typography:

- Is the hierarchy clear?
- Is readability maintained?
- Is accessibility supported?
- Are styles reusable?
- Does every style have a purpose?
- Can developers implement this consistently?

If any answer is negative, redesign the typography system.

---

# Validation Checklist

□ Typography roles defined

□ Hierarchy established

□ Accessibility reviewed

□ Reusability validated

□ Consistency maintained

□ Documentation updated

---

# Typeface

## Definition

A typeface is the overall design of a set of characters.

Examples:

- Inter
- Roboto
- SF Pro
- Helvetica
- Geist

A typeface defines the visual personality of text.

---

# Font

A font is a specific implementation of a typeface.

Examples:

Inter Regular

Inter Medium

Inter Bold

Inter Black

One typeface contains multiple fonts.

---

# Font Family

A font family is a collection of related fonts sharing the same visual design.

A family typically contains:

- Thin
- Extra Light
- Light
- Regular
- Medium
- Semi Bold
- Bold
- Extra Bold
- Black

Prefer complete font families for scalable design systems.

---

# Font Classification

Digital interfaces commonly use four categories.

- Sans Serif
- Serif
- Monospace
- Display

Each category serves a different purpose.

---

# Sans Serif

Sans serif fonts do not have decorative strokes.

Characteristics:

- Clean
- Modern
- Readable
- Neutral

Recommended for:

- User interfaces
- Dashboards
- Mobile apps
- SaaS products
- Enterprise software

Sans serif should be the default choice for most digital products.

---

# Serif

Serif fonts include small finishing strokes.

Characteristics:

- Traditional
- Formal
- Editorial
- Trustworthy

Recommended for:

- Articles
- Publications
- Long-form reading
- Luxury brands

Avoid serif fonts for dense interface controls.

---

# Monospace

Every character occupies equal horizontal space.

Recommended for:

- Code
- Technical documentation
- Terminal interfaces
- Data tables

Do not use monospace for general body copy.

---

# Display Fonts

Display fonts are designed for large sizes.

Recommended for:

- Hero headlines
- Campaigns
- Marketing
- Branding

Never use display fonts for long paragraphs.

---

# Font Pairing

Limit products to:

- One font family

or

- Two complementary font families

Avoid introducing unnecessary font combinations.

Consistency improves usability.

---

# Brand Typography

Typography contributes to brand recognition.

A typography system should communicate:

- Personality
- Trust
- Professionalism
- Consistency

Typography should reinforce the product identity.

---

# Font Personality

Every typeface communicates characteristics.

Examples include:

- Technical
- Friendly
- Professional
- Elegant
- Playful
- Minimal
- Premium

Choose a personality that aligns with the product.

Avoid conflicting visual messages.

---

# Variable Fonts

## Definition

Variable fonts provide multiple font variations within a single font file.

Common adjustable properties include:

- Weight
- Width
- Optical Size
- Slant
- Italic

Variable fonts improve flexibility while reducing the number of font files required.

---

# Font Licensing

Every font should have an appropriate license.

Before adopting a font, verify:

- Commercial usage
- Distribution rights
- Embedding rights
- Web licensing
- App licensing

Never assume a font is free for commercial use.

---

# Font Performance

Typography affects application performance.

Prefer:

- Variable fonts when appropriate
- Limited font families
- Limited font weights
- Optimized font loading

Reduce unnecessary font assets.

---

# AI Typeface Selection Engine

Before selecting a typeface, answer:

- Is readability the priority?
- Does the typeface match the product?
- Is the font family complete?
- Is the license appropriate?
- Will it scale across platforms?
- Does it support localization?
- Can developers implement it consistently?

Revise until every answer is positive.

---

# Validation Checklist

□ Typeface selected

□ Font family documented

□ Font classification defined

□ Font pairing reviewed

□ Brand typography aligned

□ Variable font evaluated

□ Licensing verified

□ Performance reviewed

□ Documentation updated