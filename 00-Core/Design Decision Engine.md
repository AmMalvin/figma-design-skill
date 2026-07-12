---
title: Design Decision Engine
version: 1.0.0
status: Stable
owner: Design System Skill
category: Core
priority: Critical
last_updated: 2026-07-12
depends_on:
  - AI Identity.md
  - AI Operating Rules.md
  - Design Philosophy.md
---

# Design Decision Engine

## Purpose

The Design Decision Engine defines the mandatory reasoning process the AI must follow before producing any design output.

No UI, component, token, documentation, or recommendation may be created without completing this framework.

---

# Decision Hierarchy

Always resolve decisions in this order.

1. User Needs
2. Accessibility
3. Business Goals
4. Product Goals
5. Existing Design System
6. Engineering Constraints
7. Visual Design

Higher levels always override lower levels.

---

# Phase 1. Understand

Collect information before making decisions.

Required information:

- Product type
- Business objective
- User objective
- User task
- User pain points
- Platform
- Device
- Accessibility requirements
- Technical limitations
- Success metrics

Missing information must trigger clarification.

---

# Phase 2. Analyze

Evaluate the request.

Identify:

- Primary workflow
- Secondary workflows
- Dependencies
- Edge cases
- Failure scenarios
- Empty states
- Loading states
- Error states

Never optimize only the happy path.

---

# Phase 3. Audit

Inspect the existing system.

Review:

- Components
- Patterns
- Variables
- Tokens
- Typography
- Icons
- Documentation
- Naming conventions

Prefer reuse before creation.

---

# Phase 4. Generate Options

Produce at least three candidate solutions.

Evaluate each using:

- Simplicity
- Accessibility
- Scalability
- Maintainability
- Consistency
- Engineering effort
- Long-term flexibility

Do not accept the first solution without comparison.

---

# Phase 5. Select

Choose the strongest solution.

Document:

- Why it was selected
- Trade-offs
- Alternatives rejected
- Risks
- Assumptions

Every major decision must have written justification.

---

# Phase 6. Validate

Review the selected solution against:

- WCAG compliance
- Platform conventions
- Existing components
- Semantic tokens
- Naming standards
- Responsive behavior
- Performance
- Developer implementation effort

Failure in any area requires revision.

---

# Phase 7. Document

Every approved decision must include:

- Purpose
- Context
- Rationale
- Usage
- Accessibility notes
- Engineering notes
- Related assets
- Future considerations

Documentation is part of the deliverable.

---

# Decision Matrix

Every solution should receive a score from 1 to 5 in each category.

| Category | Score |
|----------|------:|
| User Value | |
| Accessibility | |
| Consistency | |
| Scalability | |
| Maintainability | |
| Developer Experience | |
| Performance | |
| Documentation | |

Prefer the highest overall score rather than subjective preference.

---

# Validation Checklist

Before producing output verify:

□ Problem understood

□ User identified

□ Business objective confirmed

□ Existing assets reviewed

□ Accessibility evaluated

□ Three solutions explored

□ Decision documented

□ Trade-offs recorded

□ Documentation prepared

Only after every check passes may design begin.

---

# Failure Conditions

Stop immediately if:

- Requirements conflict
- Product goals are unclear
- Accessibility requirements are missing
- Existing design system is unavailable
- Technical constraints are unknown
- Success metrics are undefined

Request clarification before proceeding.