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


---

# Media States

## Philosophy

Every media component should clearly communicate its current state.

Users should immediately understand:

- What media is available
- Whether media is loading
- Whether interaction is possible
- What actions are available

Interactions should always improve usability.

---

# Default State

The media is ready for interaction.

Requirements:

- Complete media rendering
- Visible controls when appropriate
- Readable metadata
- Consistent layout

Default establishes the baseline presentation.

---

# Hover State

Hover communicates available interactions.

Examples:

- Reveal controls
- Display metadata
- Show quick actions
- Highlight media

Hover should never hide essential information.

---

# Focus State

Focus supports keyboard users.

Requirements:

- Visible focus ring
- High contrast
- Logical navigation order

Never remove focus indicators.

---

# Selected State

Selection should remain obvious.

Visual indicators may include:

- Border
- Overlay
- Checkmark
- Highlight

Selection should never rely only on color.

---

# Loading State

Loading communicates media retrieval.

Requirements:

- Skeleton placeholder
- Loading indicator
- Stable layout
- Preserved dimensions

Avoid layout shifts.

---

# Empty State

Empty states explain missing media.

Examples:

- No uploads
- No gallery items
- No recordings
- No preview available

Provide a useful next action.

---

# Error State

Errors should explain:

- What failed
- Why when known
- How users can recover

Examples:

- Retry
- Refresh
- Upload again
- Contact support

Avoid technical language.

---

# Upload Progress

Upload components should communicate:

- Progress percentage
- Remaining time when available
- Upload status
- Completion
- Failure

Progress should update continuously.

---

# Playback Controls

Media playback should support:

- Play
- Pause
- Stop
- Seek
- Volume
- Playback speed when appropriate

Controls should remain easy to access.

---

# Zoom

Images and documents may support zoom.

Requirements:

- Smooth scaling
- Reset zoom
- Preserve quality
- Maintain orientation

Users should never lose context.

---

# Full-screen Mode

Large media should support focused viewing.

Examples:

- Video
- Images
- Presentations
- Documents

Provide an obvious exit.

---

# Captions and Subtitles

Video and audio should support captions when available.

Requirements:

- Easy activation
- Readable typography
- Proper synchronization

Captions improve accessibility.

---

# Animation

Animation should communicate change.

Examples:

- Upload progress
- Image loading
- Gallery transitions
- Carousel movement
- Video controls

Animation should reinforce interaction.

Avoid decorative animation.

---

# Responsive Behavior

Desktop

- Large galleries
- Rich previews
- Advanced controls

Tablet

- Medium previews
- Touch controls
- Responsive layouts

Mobile

- Full-width media
- Swipe gestures
- Compact controls

Media should remain usable across all devices.

---

# AI Media Interaction Engine

Before approving media behavior, answer:

- Is interaction obvious?
- Are controls discoverable?
- Is upload progress clear?
- Is playback intuitive?
- Is accessibility supported?
- Does animation improve understanding?

If any answer is negative, redesign the interaction.

---

# Validation Checklist

□ Media states documented

□ Hover state documented

□ Focus state documented

□ Selected state documented

□ Loading state documented

□ Empty state documented

□ Error state documented

□ Upload progress documented

□ Playback controls documented

□ Zoom documented

□ Full-screen mode documented

□ Captions documented

□ Animation documented

□ Responsive behavior validated

---

# Keyboard Interaction

## Purpose

Every interactive media component should support keyboard navigation.

Minimum requirements:

- Tab moves focus
- Shift + Tab moves focus backward
- Enter activates the focused control
- Space plays or pauses media when applicable
- Arrow keys adjust playback or navigate galleries when appropriate
- Escape closes temporary media views

Keyboard interaction should remain predictable.

---

# Focus Management

Focus should:

- Always remain visible
- Follow a logical order
- Move into opened media viewers
- Return to the triggering control after closing

Never lose keyboard focus.

---

# Alternative Text

Images should include meaningful alternative text.

Alternative text should:

- Describe important content
- Explain functional images
- Ignore purely decorative images

Alternative text should communicate purpose rather than appearance.

---

# Screen Reader Support

Media components should expose:

- Media type
- Title
- Description
- Current state
- Duration when applicable
- Playback status
- Upload status

Users should understand the media without relying on vision.

---

# Accessible Media Controls

Controls should expose:

- Play
- Pause
- Stop
- Previous
- Next
- Volume
- Mute
- Full-screen
- Download when available

Every control should have an accessible name.

---

# Audio Descriptions

Videos containing important visual information should support audio descriptions when appropriate.

Audio descriptions should:

- Explain essential visual events
- Avoid interrupting dialogue
- Remain synchronized

Accessibility should extend beyond captions.

---

# Color Accessibility

Media components should never rely only on color.

Combine color with:

- Icons
- Labels
- Borders
- Patterns
- Status indicators

Every state should remain distinguishable.

---

# Responsive Adaptation

Desktop

- Rich media controls
- Multi-column galleries
- Advanced previews

Tablet

- Touch-friendly controls
- Responsive galleries
- Medium previews

Mobile

- Full-width media
- Swipe interactions
- Compact controls
- Camera integration

Media should remain usable on every screen size.

---

# Design Token Integration

Media components should reference design tokens.

Examples:

media.radius

media.shadow

media.border

media.placeholder.background

media.caption.color

media.overlay.background

media.focus.ring

media.spacing

Avoid hardcoded values.

---

# Motion Guidelines

Motion should reinforce interaction.

Examples:

- Image fade in
- Upload progress
- Gallery transition
- Carousel movement
- Video controls
- Zoom transition

Motion should communicate change.

Avoid decorative animation.

---

# Documentation

Every media component should document:

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

Every media component should be tested for:

- Accessibility
- Keyboard interaction
- Screen reader support
- Alternative text
- Responsive layouts
- Upload behavior
- Playback controls
- Motion
- Performance

Testing should occur before release.

---

# Quality Assurance

Review every media component for:

- Accessibility
- Visual consistency
- Responsive behavior
- Design token usage
- Documentation
- Performance

Only approved media components belong in the design system.

---

# Versioning

Track changes for:

- New media types
- Accessibility improvements
- Motion updates
- Bug fixes
- Breaking changes

Maintain complete version history.

---

# Governance

Media updates should include:

- UX review
- Accessibility review
- Engineering review
- QA approval
- Documentation update

Governance maintains long-term consistency.

---

# AI Media Review Engine

Before publishing any media component, answer:

- Is the media appropriate?
- Is accessibility complete?
- Are alternative text requirements documented?
- Are design tokens used?
- Is keyboard interaction supported?
- Has testing been completed?
- Does this scale across products?
- Is interaction predictable?

If any answer is negative, revise the component.

---

# Media Components Checklist

Before publishing:

□ Media anatomy documented

□ Variants completed

□ States documented

□ Keyboard interaction verified

□ Focus management documented

□ Alternative text documented

□ Screen reader support completed

□ Responsive behavior validated

□ Design tokens integrated

□ Motion documented

□ Testing completed

□ QA approved

□ Version history updated

□ Documentation completed

---

# Key Takeaways

Media components present images, video, audio, documents, and uploaded content in a consistent and accessible way.

The AI must:

- Choose the correct media component.
- Preserve media quality.
- Support keyboard navigation.
- Support screen readers.
- Provide alternative text.
- Use design tokens.
- Keep motion meaningful.
- Test every interaction.
- Document every behavior.

Every media component should improve accessibility, consistency, performance, and long-term maintainability.