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

---

# Typography Anatomy

## Definition

Typography anatomy describes the structural parts of individual letterforms.

Understanding typography anatomy helps the AI evaluate readability, accessibility, and visual consistency.

Typography decisions should be based on structure rather than appearance.

---

# Baseline

## Definition

The baseline is the invisible line on which most letters rest.

A consistent baseline creates:

- Alignment
- Rhythm
- Readability

Text should align to a common baseline whenever possible.

---

# Cap Height

Cap height is the height of uppercase letters measured from the baseline.

Cap height influences:

- Visual balance
- Heading appearance
- Alignment

Cap height should remain consistent within a typeface.

---

# X-Height

## Definition

X-height is the height of lowercase letters excluding ascenders and descenders.

Large x-heights improve:

- Small text readability
- Interface legibility
- Mobile usability

For UI design, prefer typefaces with generous x-heights.

---

# Ascenders

Ascenders extend above the x-height.

Examples:

- b
- d
- h
- k
- l

Ascenders improve character recognition.

---

# Descenders

Descenders extend below the baseline.

Examples:

- g
- j
- p
- q
- y

Ensure sufficient line height so descenders never collide with adjacent text.

---

# Stem

A stem is the primary vertical stroke of a character.

Stem thickness contributes to:

- Font weight
- Readability
- Visual personality

---

# Stroke

A stroke is any line forming part of a letter.

Stroke consistency improves:

- Legibility
- Recognition
- Visual harmony

---

# Counter

Counters are enclosed or partially enclosed spaces inside letters.

Examples:

- o
- e
- a
- d
- p

Large counters improve readability at smaller sizes.

---

# Aperture

An aperture is the opening of partially enclosed letters.

Examples:

- c
- e
- s

Open apertures improve clarity on digital screens.

---

# Bowl

A bowl is the curved enclosed portion of a letter.

Examples:

- b
- d
- o
- p

Bowls should remain visually balanced.

---

# Terminal

A terminal is the end of a stroke without a serif.

Terminal shape contributes to the overall personality of the typeface.

---

# Serif

Serifs are decorative finishing strokes.

They influence:

- Tone
- Tradition
- Reading experience

Serifs should match the product context.

---

# Glyph

A glyph is the visual representation of a character.

One character may have multiple glyphs.

Support complete glyph sets for:

- Localization
- Accessibility
- Internationalization

---

# Stroke Contrast

Stroke contrast is the difference between thick and thin strokes.

High contrast creates:

- Elegant appearance
- Editorial feel

Low contrast creates:

- Better screen readability
- Modern interfaces

UI typography generally benefits from moderate to low stroke contrast.

---

# Legibility

Legibility measures how easily individual characters can be distinguished.

Improve legibility through:

- Open counters
- Large x-height
- Clear apertures
- Consistent strokes
- Appropriate font size

Legibility is a property of the typeface.

---

# Readability

Readability measures how easily larger blocks of text can be understood.

Improve readability through:

- Proper line length
- Appropriate line height
- Clear hierarchy
- Consistent spacing
- Logical structure

Readability is a property of the overall layout.

---

# Character Recognition

Every character should remain distinguishable.

Avoid confusing pairs such as:

- I and l
- O and 0
- 1 and l

Choose fonts with clear differentiation for interface text.

---

# AI Typography Analysis Engine

Before selecting a typeface, answer:

- Is the x-height suitable?
- Are counters sufficiently open?
- Are apertures clear?
- Is stroke contrast appropriate?
- Are glyphs complete?
- Is legibility maintained at small sizes?
- Is readability preserved across long content?

Revise until every answer is positive.

---

# Validation Checklist

□ Baseline reviewed

□ Cap height evaluated

□ X-height reviewed

□ Ascenders and descenders validated

□ Counters reviewed

□ Apertures reviewed

□ Stroke contrast evaluated

□ Glyph coverage verified

□ Legibility confirmed

□ Readability validated

□ Documentation updated