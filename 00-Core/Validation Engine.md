---
title: Validation Engine
version: 1.0.0
status: Stable
owner: Design System Skill
category: Core
priority: Critical
last_updated: 2026-07-12
depends_on:
  - AI Identity.md
  - AI Operating Rules.md
  - Design Decision Engine.md
  - Workflow Engine.md
---

# Validation Engine

## Purpose

The Validation Engine defines the mandatory quality assurance process for every artifact produced by the AI.

Validation is not a final step.

Validation occurs throughout the design lifecycle.

No artifact may be considered complete until every required validation gate has passed.

---

# Validation Philosophy

Every design must be:

- Useful
- Usable
- Accessible
- Consistent
- Scalable
- Maintainable
- Documented
- Developer Ready

Visual quality alone never determines success.

---

# Validation Layers

Every artifact must pass all validation layers.

1. Product Validation
2. User Validation
3. UX Validation
4. Accessibility Validation
5. Visual Validation
6. Design System Validation
7. Technical Validation
8. Documentation Validation
9. Governance Validation

Failure at any layer blocks completion.

---

# Layer 1. Product Validation

Confirm:

- Business objective is satisfied
- Success metrics are measurable
- Product goals are supported
- Feature scope is respected

---

# Layer 2. User Validation

Confirm:

- User task is clear
- User flow is efficient
- Cognitive load is minimized
- Error prevention exists
- Recovery paths exist

---

# Layer 3. UX Validation

Evaluate:

- Learnability
- Efficiency
- Discoverability
- Feedback
- Consistency
- Recognition over recall
- Progressive disclosure

---

# Layer 4. Accessibility Validation

Verify:

- WCAG compliance
- Color contrast
- Keyboard navigation
- Focus visibility
- Screen reader compatibility
- Touch target size
- Motion preferences
- Zoom support
- Text scaling

Accessibility issues must be resolved before release.

---

# Layer 5. Visual Validation

Confirm:

- Typography hierarchy
- Spacing consistency
- Alignment
- Grid adherence
- Color usage
- Elevation
- Icon consistency
- Visual hierarchy

Visual refinement must support usability.

---

# Layer 6. Design System Validation

Confirm:

- Semantic tokens used
- Variables used
- Existing components reused
- Existing patterns reused
- Naming conventions followed
- No duplicated assets created

---

# Layer 7. Technical Validation

Review:

- Engineering feasibility
- Auto Layout integrity
- Responsive behavior
- Component properties
- Variant structure
- Library compatibility
- Performance impact

---

# Layer 8. Documentation Validation

Every artifact must include:

- Purpose
- Usage
- Anatomy
- States
- Variants
- Accessibility
- Do
- Don't
- Examples
- Related assets
- Developer notes

---

# Layer 9. Governance Validation

Confirm:

- Repository standards followed
- Version updated
- Changelog prepared
- Review completed
- Ownership assigned
- Deprecation reviewed

---

# Release Checklist

A release is blocked until all items pass.

□ Product goals satisfied

□ User goals satisfied

□ UX validated

□ Accessibility validated

□ Visual review passed

□ Design system review passed

□ Technical review passed

□ Documentation completed

□ Governance completed

---

# Severity Levels

Critical

Release blocked immediately.

High

Must be resolved before release.

Medium

Resolve before the next scheduled release.

Low

Log for future improvement.

---

# Failure Conditions

Immediately stop release if:

- Accessibility fails
- Duplicate components exist
- Semantic tokens are missing
- Documentation is incomplete
- Naming standards are violated
- Engineering rejects implementation
- QA identifies blocking issues

Release may continue only after all blocking issues are resolved.

---

# Validation Principles

Validation is continuous.

Validation is measurable.

Validation is evidence-based.

Validation protects the integrity of the design system.

Quality is never assumed.