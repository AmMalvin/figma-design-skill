---
title: Media Components
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
  - ../02-Visual-System/Iconography.md
  - ../02-Visual-System/Spacing & Sizing.md
  - ./Component Principles.md
---

# Media Components

## Purpose

This module teaches the AI how to design scalable, reusable, accessible, and production-ready media components.

Media components communicate information through images, video, audio, documents, and interactive visual assets.

---

# Definition

Media components present, preview, upload, organize, and interact with digital content.

Examples include:

- Images
- Avatars
- Videos
- Audio
- Galleries
- Carousels
- File previews
- Upload areas

Media should improve understanding without distracting users.

---

# Objectives

After completing this module, the AI should be able to:

- Design reusable media components
- Support responsive media
- Improve accessibility
- Optimize media presentation
- Improve developer implementation
- Scale across products

---

# Media Philosophy

Every media component should answer:

- What content is being presented?
- Why is it relevant?
- How can users interact with it?

Media should support user goals.

---

# Core Principles

Always:

- Preserve quality.
- Maintain aspect ratios.
- Optimize loading.
- Support accessibility.
- Design reusable components.
- Keep interactions predictable.

Never:

- Stretch media.
- Crop important information.
- Autoplay disruptive media.
- Depend only on visuals.
- Hide essential controls.

---

# Why Media Components Exist

Media components help users:

- View content
- Consume information
- Upload files
- Compare assets
- Preview documents
- Complete workflows

Media should improve comprehension.

---

# Component Anatomy

Every media component should define:

- Container
- Media content
- Placeholder
- Caption
- Metadata
- Controls
- Status
- Actions

Each element should have one responsibility.

---

# Captions

Captions should:

- Explain the media
- Add context
- Remain concise

Captions should never repeat obvious information.

---

# Metadata

Metadata may include:

- File size
- Resolution
- Duration
- Format
- Upload date
- Owner

Only display information useful to users.

---

# Hierarchy

Prioritize:

- Primary media
- Controls
- Caption
- Metadata
- Secondary actions

Hierarchy should direct attention naturally.

---

# AI Decision Rules

Before approving a media component, answer:

- Is the media appropriate?
- Is interaction clear?
- Is accessibility supported?
- Is responsiveness supported?
- Is the component reusable?
- Can developers implement it consistently?

If any answer is negative, redesign the component.

---

# Validation Checklist

□ Purpose documented

□ Anatomy documented

□ Captions documented

□ Metadata documented

□ Hierarchy documented

□ Accessibility reviewed

□ Documentation updated

---

# Media Types

## Philosophy

Every media component should belong to one reusable component family.

Different media types solve different presentation problems while sharing the same design language.

Avoid creating duplicate media components.

---

# Image

## Purpose

Present visual information.

Examples:

- Product images
- Hero images
- Blog images
- Illustrations

Images should preserve their original aspect ratio whenever possible.

---

# Avatar

## Purpose

Represent a person, organization, or system.

Examples:

- User profile
- Team member
- Organization
- AI assistant

Avatars should remain recognizable at every supported size.

---

# Icon

## Purpose

Communicate meaning through simplified graphics.

Examples:

- Navigation
- Actions
- Status
- Categories

Icons should support labels instead of replacing them when clarity is important.

---

# Video Player

## Purpose

Present video content.

Examples:

- Tutorials
- Product demos
- Training
- Marketing videos

Video controls should remain easy to access.

---

# Audio Player

## Purpose

Present spoken or recorded audio.

Examples:

- Podcasts
- Voice messages
- Music
- Interviews

Playback controls should remain visible.

---

# Gallery

## Purpose

Display related media collections.

Examples:

- Product galleries
- Photo albums
- Portfolios
- Documentation

Galleries should support efficient browsing.

---

# Carousel

## Purpose

Display multiple items within limited space.

Examples:

- Featured products
- Testimonials
- Promotions
- Image collections

Carousels should avoid hiding important information.

---

# Lightbox

## Purpose

Display media in a focused viewing experience.

Examples:

- Image preview
- Video preview
- Gallery expansion

Lightboxes should reduce surrounding distractions.

---

# File Preview

## Purpose

Preview uploaded files before opening or downloading.

Examples:

- PDF
- Document
- Spreadsheet
- Presentation

Previews should communicate file type clearly.

---

# File Upload

## Purpose

Allow users to upload media or documents.

Examples:

- Images
- Videos
- Audio
- Documents

Upload requirements should remain visible.

---

# Drag and Drop Upload

## Purpose

Provide a faster upload experience.

Requirements:

- Drop target
- Hover feedback
- Upload progress
- Error handling

Users should immediately understand where files may be dropped.

---

# Media Placeholder

## Purpose

Reserve space before media becomes available.

Examples:

- Image loading
- Video thumbnail
- Avatar placeholder
- File preview loading

Placeholders should reduce layout shifts.

---

# Media Selection Guide

Use:

Image

For visual content.

Avatar

For identity.

Icon

For symbolic actions.

Video Player

For video playback.

Audio Player

For audio playback.

Gallery

For collections.

Carousel

For rotating content.

Lightbox

For focused viewing.

File Preview

For uploaded content.

File Upload

For selecting files.

Drag and Drop Upload

For desktop upload workflows.

Media Placeholder

For loading states.

---

# Media Variants

Represent media components as variants.

Recommended properties:

Type

- Image
- Avatar
- Icon
- Video
- Audio
- Gallery
- Carousel
- Lightbox
- Preview
- Upload
- Drag Drop
- Placeholder

State

- Default
- Hover
- Focus
- Loading
- Empty
- Error
- Disabled

Size

- Small
- Medium
- Large

Avoid creating duplicate component sets.

---

# Responsive Behavior

Desktop

- Large galleries
- Rich previews
- Drag and drop upload

Tablet

- Responsive galleries
- Medium previews
- Touch-friendly controls

Mobile

- Full-width media
- Swipe galleries
- Camera upload
- Compact previews

Media should remain usable across all screen sizes.

---

# AI Media Selection Engine

Before selecting a media component, answer:

- Is this the correct media type?
- Is interaction obvious?
- Is accessibility supported?
- Is responsiveness supported?
- Can this remain part of one reusable component family?
- Will developers implement this consistently?

If any answer is negative, choose a more appropriate media component.

---

# Validation Checklist

□ Image documented

□ Avatar documented

□ Icon documented

□ Video player documented

□ Audio player documented

□ Gallery documented

□ Carousel documented

□ Lightbox documented

□ File preview documented

□ File upload documented

□ Drag and drop upload documented

□ Media placeholder documented

□ Variant strategy documented

□ Responsive behavior documented