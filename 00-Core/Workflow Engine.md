---
title: Workflow Engine
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
---

# Workflow Engine

## Purpose

The Workflow Engine defines the mandatory sequence the AI must follow for every design task.

The workflow is sequential.

Stages cannot be skipped.

If a stage fails, return to the previous stage before continuing.

---

# Workflow Overview

Every project follows this lifecycle.

1. Understand
2. Discover
3. Audit
4. Plan
5. Design
6. Validate
7. Document
8. Review
9. Deliver
10. Improve

---

# Stage 1. Understand

Goal

Understand exactly what needs to be solved.

Required Outputs

- Product summary
- Business goals
- User goals
- Success metrics
- Constraints
- Assumptions
- Risks

Exit Criteria

The problem statement is clear.

---

# Stage 2. Discover

Goal

Collect enough information before designing.

Activities

- User research
- Competitive review
- Platform conventions
- Accessibility requirements
- Technical limitations

Exit Criteria

The AI understands the design context.

---

# Stage 3. Audit

Goal

Review the existing design system.

Inspect

- Components
- Tokens
- Variables
- Typography
- Icons
- Layouts
- Patterns
- Documentation

Rule

Reuse before creating.

Exit Criteria

No duplicate work is introduced.

---

# Stage 4. Plan

Goal

Create a design strategy.

Deliverables

- User flow
- Information architecture
- Component requirements
- Pattern requirements
- Documentation plan
- Testing plan

Exit Criteria

The implementation plan is approved.

---

# Stage 5. Design

Goal

Produce production-ready design assets.

Requirements

- Auto Layout
- Variables
- Semantic tokens
- Components
- Responsive layouts
- Accessibility
- Naming conventions

Exit Criteria

Design meets system standards.

---

# Stage 6. Validate

Validate against

- WCAG
- Design principles
- Component consistency
- Token usage
- Responsive behavior
- Platform conventions
- Engineering feasibility

Failures require revision.

---

# Stage 7. Document

Document while designing.

Every artifact must include

- Purpose
- Usage
- Anatomy
- Variants
- Accessibility
- Do
- Don't
- Examples
- Related assets
- Engineering notes

---

# Stage 8. Review

Perform reviews with

- Design QA
- Accessibility QA
- Engineering
- Product
- Content
- Stakeholders

Record all findings.

---

# Stage 9. Deliver

Deliver

- Design files
- Components
- Variables
- Documentation
- Release notes
- Handoff notes
- Changelog

---

# Stage 10. Improve

Collect

- Feedback
- Bugs
- Analytics
- Accessibility issues
- Technical debt
- Enhancement requests

Feed improvements into the next release.

---

# Workflow Rules

The AI must never

- Skip discovery
- Skip accessibility
- Skip documentation
- Skip validation
- Skip QA
- Skip developer handoff

Every workflow must complete all stages.

---

# Validation Checklist

□ Problem defined

□ Research completed

□ Existing system audited

□ Design planned

□ Design created

□ Validation passed

□ Documentation completed

□ Review completed

□ Delivery package complete

□ Improvements recorded

---

# Failure Conditions

Restart the workflow if

- Business goals change
- User needs change
- Accessibility requirements change
- Technical constraints change
- Platform changes
- New evidence invalidates previous decisions