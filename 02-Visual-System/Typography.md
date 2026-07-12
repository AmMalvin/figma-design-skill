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

---

# Typography Scale

## Definition

A typography scale is a structured set of font sizes used throughout a product.

A consistent scale creates:

- Hierarchy
- Rhythm
- Predictability
- Reusability

Never create random font sizes.

---

# Base Font Size

The base font size is the foundation of the typography system.

Most digital products use:

16 px

as the default body text size.

All other typography should scale from this foundation.

---

# Modular Scale

A modular scale uses mathematical ratios to generate font sizes.

Common ratios include:

- Minor Second
- Major Second
- Minor Third
- Major Third
- Perfect Fourth

Use modular scales as guidance rather than strict rules.

Readability always takes priority.

---

# Display Text

Display text is the largest typography in the system.

Use for:

- Hero headlines
- Marketing pages
- Landing pages

Display text should never be used for body content.

---

# Heading Levels

Every system should define consistent heading levels.

Recommended hierarchy:

- Display
- Heading 1
- Heading 2
- Heading 3
- Heading 4
- Heading 5
- Heading 6

Each level should have a distinct purpose.

---

# Body Text

Body text communicates primary information.

Body text should prioritize:

- Readability
- Comfortable scanning
- Accessibility

Avoid excessively small body text.

---

# Supporting Text

Supporting text includes:

- Captions
- Labels
- Helper text
- Metadata
- Footnotes

Supporting text should remain readable while carrying less visual emphasis.

---

# Font Weight

Font weight creates hierarchy without changing size.

Common weights:

- Thin
- Extra Light
- Light
- Regular
- Medium
- Semi Bold
- Bold
- Extra Bold
- Black

Avoid using every available weight.

Limit products to a small, consistent set.

---

# Line Height

## Definition

Line height controls vertical spacing between lines of text.

General guidance:

Display Text

- Tight spacing

Headings

- Moderate spacing

Body Text

- More generous spacing

Supporting Text

- Balanced spacing

Line height should improve readability rather than maximize density.

---

# Letter Spacing

Letter spacing adjusts the distance between characters.

Use letter spacing to:

- Improve readability
- Support large headings
- Improve uppercase text
- Balance typography

Avoid excessive tracking.

---

# Paragraph Spacing

Paragraph spacing separates blocks of text.

Paragraph spacing should communicate structure.

Do not rely on empty lines alone.

---

# Line Length

Readable paragraphs should maintain comfortable line lengths.

Avoid:

- Extremely short lines
- Extremely long lines

Long lines reduce reading efficiency.

---

# Text Alignment

Supported alignments:

- Left
- Center
- Right
- Justified

For left-to-right languages:

Prefer left alignment for body content.

Center alignment should be reserved for short content.

Avoid justified text in user interfaces unless specifically required.

---

# Responsive Typography

Typography should adapt across screen sizes.

Responsive adjustments may include:

- Font size
- Line height
- Letter spacing
- Display scale

Maintain hierarchy across every breakpoint.

---

# Typography Tokens

Typography should use reusable semantic tokens.

Examples:

type.display.large

type.heading.h1

type.heading.h2

type.body.large

type.body.default

type.body.small

type.caption

type.label

Components should reference typography tokens instead of raw values.

---

# AI Typography Scale Engine

Before approving typography, answer:

- Is the scale consistent?
- Does each size have a purpose?
- Is hierarchy obvious?
- Is body text readable?
- Is line height appropriate?
- Is letter spacing balanced?
- Are typography tokens reusable?
- Will the system scale across products?

Revise until every answer is positive.

---

# Validation Checklist

□ Base font size defined

□ Typography scale completed

□ Heading hierarchy documented

□ Body text validated

□ Font weights reviewed

□ Line height optimized

□ Letter spacing reviewed

□ Paragraph spacing defined

□ Responsive typography validated

□ Typography tokens documented


---

# Typography Accessibility

## Definition

Typography accessibility ensures text is readable, understandable, and usable by everyone.

Readable typography is essential for usability.

Accessibility takes priority over aesthetics.

---

# Accessible Typography Principles

Always:

- Prioritize readability.
- Maintain sufficient text size.
- Use appropriate line height.
- Maintain strong contrast.
- Support text scaling.
- Use clear hierarchy.

Never:

- Depend on tiny text.
- Compress line spacing.
- Use decorative fonts for interface content.
- Reduce readability for visual style.

---

# Responsive Typography

Typography should adapt across screen sizes.

Adjust when necessary:

- Font size
- Line height
- Letter spacing
- Layout width

Hierarchy should remain consistent regardless of device.

---

# Localization

Typography should support multiple languages.

Consider:

- Character width
- Word length
- Reading direction
- Font availability
- Line expansion

Design layouts that accommodate translated content.

---

# Internationalization

Typography systems should support:

- Latin
- Arabic
- Cyrillic
- CJK
- Indic
- Other supported writing systems

Avoid assumptions that every language behaves like English.

---

# Writing Systems

Different writing systems require different typography behavior.

Support:

- Left-to-right
- Right-to-left
- Vertical writing where applicable

Typography should adapt without breaking layout consistency.

---

# Numeric Typography

Numbers require dedicated attention.

Support:

- Tabular figures
- Proportional figures
- Currency
- Percentages
- Dates
- Time
- Financial values

Use tabular figures for dashboards, tables, and analytics.

---

# Code Typography

Code requires different typography rules.

Use:

- Monospace fonts
- Consistent indentation
- Distinguishable characters
- Appropriate line height

Never display code using proportional body fonts.

---

# OpenType Features

OpenType features improve typography when supported by the chosen font.

Examples include:

- Ligatures
- Small Caps
- Stylistic Sets
- Character Variants
- Tabular Figures
- Old Style Figures

Only enable features that improve readability or support the intended design. :contentReference[oaicite:1]{index=1}

---

# Typography Tokens

Typography should use semantic tokens.

Example structure:

Primitive

↓

Semantic

↓

Component

↓

Screen

Examples:

type.display.large

type.heading.h1

type.heading.h2

type.body.default

type.caption

type.label

Components should reference typography tokens rather than raw values.

---

# Typography Quality Assurance

Review every typography system for:

- Readability
- Accessibility
- Hierarchy
- Consistency
- Responsiveness
- Localization support
- Token usage
- Performance

Typography should remain predictable throughout the product.

---

# AI Typography Decision Engine

Before approving typography, answer:

- Is every text style purposeful?
- Is hierarchy obvious?
- Is accessibility maintained?
- Does typography support localization?
- Are semantic typography tokens used?
- Is responsive behavior defined?
- Are OpenType features used appropriately?
- Can developers implement the system consistently?

If any answer is negative, redesign the typography system.

---

# Typography Checklist

Before publishing:

□ Typography roles documented

□ Typeface selected

□ Typography scale completed

□ Hierarchy validated

□ Font weights reviewed

□ Line height optimized

□ Letter spacing reviewed

□ Accessibility verified

□ Localization supported

□ Responsive typography validated

□ OpenType features reviewed

□ Numeric typography documented

□ Code typography documented

□ Typography tokens completed

□ Documentation updated

---

# Key Takeaways

Typography is the foundation of digital communication.

The AI must:

- Build semantic typography systems.
- Maintain clear hierarchy.
- Prioritize readability.
- Support accessibility.
- Create responsive typography.
- Design for localization.
- Use reusable typography tokens.
- Keep typography consistent across every product.
- Optimize for implementation by developers.

Every typography decision should improve communication, comprehension, and usability.