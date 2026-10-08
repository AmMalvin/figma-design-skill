# Sequential author walkthroughs

Date: 2026-10-08. Generator and reviewer: the repository audit author in one continuous session. Evaluator criteria were visible. Independence: none. Artifact: the written specifications below. No Figma frames, browser interactions, screen-reader tests or user studies were executed. These outcomes demonstrate reasoning coverage and retrievable guidance, not observed product performance.

The newcomer check starts at SKILL.md, follows the relevant route and shared owners, and asks whether a reader could obtain a complete contract without reading the entire repository. The static validator separately verifies graph reachability. All sixteen walkthroughs have intended state, system and task decisions; visual polish and runtime accessibility remain unknown.

## Consumer mobile banking transfer

Route: [Checkout & Payments](../../06-Patterns/Checkout%20%26%20Payments.md), [Mobile Components](../../05-Components/Mobile%20Components.md), [Accessibility](../../01-Foundation/Accessibility.md).

Information model: Recipient -> amount/account -> review -> submit -> status/receipt.

A linear native task flow keeps recipient and debit total before commitment. Retain the selected recipient and amount when returning to edit; use a readable review list rather than dashboard cards.

A timeout displays checking status with a reference and history access. Reconcile the same request before exposing a safe retry; delivery status comes from the service.

Keep long beneficiary names readable, enlarge native text, avoid keyboard overlap and specify focus on the first invalid field. Loss of connectivity preserves the uncommitted draft; sensitive persistence follows supplied policy.

Reuse native inputs, existing status roles and receipt pattern. Platform metrics and security policy require the actual target OS and product rules.

Review: task-specific structure and recovery are specified. Stress cases (320 CSS equivalent narrow web fallback; Large text; Long beneficiary name; Offline then reconnect) are addressed as intended behavior; none was executed. No arbitrary system values are introduced. Ready for a scoped prototype/specification review; runtime and rendered-quality approval remains pending.

## Enterprise incident analytics

Route: [Data-Dense Interfaces](../../06-Patterns/Data-Dense%20Interfaces.md), [Data Visualization Components](../../05-Components/Data%20Visualization%20Components.md), [Tables & Data Grids](../../05-Components/Tables%20%26%20Data%20Grids.md).

Information model: Comparison workspace -> selected anomaly -> linked investigation.

Place a time-series comparison beside a dense service table with a persistent period/filter context. Multiple priorities can remain visible because expert monitoring needs simultaneous scanning.

Retain last known data with timestamp and source-level partial/stale markers. Missing observations remain gaps rather than zero. Drill-back restores comparison and sort context.

Use native table semantics for reading; explicit controls for sorting and row details. Chart access includes a textual summary and data alternative. Narrow layouts keep selection and essential comparisons available.

Reuse compact density and semantic severity roles. No decorative chart appears unless its analytical question and data source are specified.

Review: task-specific structure and recovery are specified. Stress cases (100000 rows; Missing observations; Multiple time zones; Narrow viewport) are addressed as intended behavior; none was executed. No arbitrary system values are introduced. Ready for a scoped prototype/specification review; runtime and rendered-quality approval remains pending.

## Responsive SaaS scheduling feature

Route: [Responsive Design](../../01-Foundation/Responsive%20Design.md), [Advanced Components](../../05-Components/Advanced%20Components.md), [Form Workflows](../../06-Patterns/Form%20Workflows.md).

Information model: Choose time/zone -> attendee details -> verify availability -> confirmation.

The slot list is primary on narrow screens; a calendar overview is supplementary where it helps choice. Typed date access offers an alternative to spatial selection.

Revalidate at commitment. If a slot becomes unavailable, preserve details and suggest available alternatives; do not silently move the booking.

Display the event time zone and the user's comparison time when necessary. Specify DST ambiguity handling as a service constraint. Keep focus on the conflict explanation and next choice.

Reuse calendar and form primitives; the booking composition stays feature-specific. Confirmation reflects actual booking state.

Review: task-specific structure and recovery are specified. Stress cases (DST boundary; Long attendee names; Keyboard-only input; Network conflict) are addressed as intended behavior; none was executed. No arbitrary system values are introduced. Ready for a scoped prototype/specification review; runtime and rendered-quality approval remains pending.

## Financial reconciliation

Route: [Tables & Data Grids](../../05-Components/Tables%20%26%20Data%20Grids.md), [Data Management Patterns](../../06-Patterns/Data%20Management%20Patterns.md), [Data-Dense Interfaces](../../06-Patterns/Data-Dense%20Interfaces.md).

Information model: Paired ledger comparison -> candidate match -> review discrepancy -> post.

Use aligned monetary columns and paired selection rather than unrelated tiles. Unmatched totals and currency context remain visible during matching.

A match suggestion is tentative until confirmed; posting is a separate service transition. Batch results show individual failures without undoing successful records.

Restricted records expose only allowed metadata; not a guessed amount. Narrow comparison can use a focused pair/detail view with explicit access to all fields.

Use financial table and money roles; preserve identifiers and locale-aware formats. Backend reconciliation rules need supplied domain policy.

Review: task-specific structure and recovery are specified. Stress cases (Multi-currency; 10000 records; Permission loss; Long invoice identifiers) are addressed as intended behavior; none was executed. No arbitrary system values are introduced. Ready for a scoped prototype/specification review; runtime and rendered-quality approval remains pending.

## Content-heavy knowledge library

Route: [Information Architecture](../../01-Foundation/Information%20Architecture.md), [Content Design](../../01-Foundation/Content%20Design.md), [Search Patterns](../../06-Patterns/Search%20Patterns.md).

Information model: Browse/search -> policy metadata -> article -> related document.

Use editorial reading structure with current-version provenance above the article and a navigable section outline where content warrants it. Related links follow the reading task.

A stale bookmark identifies archive status and links to the current policy; absent access differs from a missing document. Returning preserves query and reading context.

Long headings wrap, article measure follows existing type rules, and reflow keeps content order meaningful. RTL, zoom and keyboard navigation need rendered/runtime checks.

Reuse article styles, document metadata and links; avoid turning each paragraph into a card.

Review: task-specific structure and recovery are specified. Stress cases (RTL and translated titles; Text zoom; Long headings; Stale bookmarked version) are addressed as intended behavior; none was executed. No arbitrary system values are introduced. Ready for a scoped prototype/specification review; runtime and rendered-quality approval remains pending.

## B2B settings and permissions

Route: [Settings & Permissions](../../06-Patterns/Settings%20%26%20Permissions.md), [Authentication & Account Patterns](../../06-Patterns/Authentication%20%26%20Account%20Patterns.md).

Information model: Member -> effective/inherited access -> proposed change -> consequences -> save.

Use a scoped role summary and expandable source of inherited grants. Show which authority can change each grant; do not imply toggles can override inherited access.

Preview removal consequences. Protect a last-admin case according to server policy; a stale-write response asks the admin to review current access while retaining their proposed choice.

Use explicit Save for consequential edits. Announce result without leaking restricted members. Keyboard and narrow layouts preserve the scope and selected member.

Reuse role selector and warning panel. Effective permissions and audit events require server evidence.

Review: task-specific structure and recovery are specified. Stress cases (Last admin; Concurrent role update; Long role descriptions; Insufficient permission) are addressed as intended behavior; none was executed. No arbitrary system values are introduced. Ready for a scoped prototype/specification review; runtime and rendered-quality approval remains pending.

## Large application form

Route: [Form Workflows](../../06-Patterns/Form%20Workflows.md), [Inputs & Forms](../../05-Components/Inputs%20%26%20Forms.md), [Content Design](../../01-Foundation/Content%20Design.md).

Information model: Grouped application sections -> saved draft -> review errors -> final submission.

Group related decisions, reveal dependent questions when relevant and provide progress from actual completed sections. A wizard is chosen only if sequence requires it.

Draft status is separate from submitted status. Validate after suitable interaction and at review; an error summary links to fields while retaining inputs and completed uploads.

Out-of-order async validation cannot replace current answers. Interrupted upload retries that document; expired drafts explain what remains recoverable. Long answers expand without losing labels.

Reuse field groups and summary patterns. Retention and consent follow actual policy; successful submission comes from the service.

Review: task-specific structure and recovery are specified. Stress cases (Interrupted upload; Async validation race; Long answers; Keyboard and screen reader intent) are addressed as intended behavior; none was executed. No arbitrary system values are introduced. Ready for a scoped prototype/specification review; runtime and rendered-quality approval remains pending.

## Responsive procurement table

Route: [Tables & Data Grids](../../05-Components/Tables%20%26%20Data%20Grids.md), [Responsive Design](../../01-Foundation/Responsive%20Design.md).

Information model: Filter bids -> select comparison set -> compare -> open bid detail.

Keep native table semantics for read-only comparison. On narrow screens expose a selected-bid comparison with intentional horizontal scroll where two-dimensional relationships are essential, plus detail access.

Selection states specify page versus full query; sorting does not silently change selected IDs. Errors and stale bids show row/source context.

Keep critical vendor, total and currency visible; other columns remain reachable. Long vendor names wrap where useful, identifier detail stays accessible, and real virtualized semantics need runtime verification.

Reuse table headers, selection and compact roles. Reflow exceptions require a task justification, not a blanket exemption for the entire page.

Review: task-specific structure and recovery are specified. Stress cases (50000 rows; Long vendor names; Mixed currencies; Keyboard navigation) are addressed as intended behavior; none was executed. No arbitrary system values are introduced. Ready for a scoped prototype/specification review; runtime and rendered-quality approval remains pending.

## Search and refinement

Route: [Search Patterns](../../06-Patterns/Search%20Patterns.md), [Menus, Lists & Selection Controls](../../05-Components/Menus,%20Lists%20%26%20Selection%20Controls.md).

Information model: Query/scope -> ranked results -> refine -> document -> restored results.

Use a results page, with a combobox only if suggestions are actually offered. Explain owner/date filter conjunction and retain query/filter state in the supported URL model.

Ignore stale responses. Distinguish no matches, inaccessible scope and failed query; recovery preserves entered text and filters. Do not leak forbidden titles in suggestions.

Updating results does not steal focus. Keyboard suggestion selection follows the chosen model, while the page supports regular links. Back restores scroll and active filters.

Reuse search, filters and results. Ranking promises need actual search behavior; debounce should fit latency, not a universal number.

Review: task-specific structure and recovery are specified. Stress cases (Slow response order; Very long query; No results; Navigation back) are addressed as intended behavior; none was executed. No arbitrary system values are introduced. Ready for a scoped prototype/specification review; runtime and rendered-quality approval remains pending.

## First value onboarding

Route: [Onboarding & First-Time User Experience Patterns](../../06-Patterns/Onboarding%20%26%20First-Time%20User%20Experience%20Patterns.md), [State Patterns](../../06-Patterns/State%20Patterns.md).

Information model: Create/import first project -> assign one task -> optional education.

Start with the useful task and contextual guidance rather than a prerequisite slideshow. Label any example data and provide a clear route to real work.

Resume actual imported/assigned state; partial import offers affected-item recovery. Declining notifications does not block task assignment.

Revisit optional guidance from help. Avoid fixed progress that reports steps as complete after failed operations. Long titles wrap without hiding the relevant next action.

Reuse project list and task editor. Permission request timing follows a real benefit and current platform behavior.

Review: task-specific structure and recovery are specified. Stress cases (Declined permission; Partial import; Returning user; Long project title) are addressed as intended behavior; none was executed. No arbitrary system values are introduced. Ready for a scoped prototype/specification review; runtime and rendered-quality approval remains pending.

## Design-system combobox

Route: [Component Principles](../../05-Components/Component%20Principles.md), [Menus, Lists & Selection Controls](../../05-Components/Menus,%20Lists%20%26%20Selection%20Controls.md), [Token Architecture](../../03-Design-Tokens/Token%20Architecture.md), [Figma Production](../../04-Figma/Figma%20Production.md).

Information model: Input -> suggestions -> explicit selection -> committed value.

Specify one reusable single-selection contract; editable text is a query rather than a custom selected value. Distinguish typed query, selected value and highlighted suggestion.

Define async pending, no match, failed fetch and now-invalid option behavior. Preserve the last valid value or explain invalidation according to product requirements.

Define label, description, expanded state, active option and expected keys for the chosen implementation. IME composition prevents premature query/selection handling.

Map text, visibility and configuration properties to actual code APIs; keep semantic token bindings. Use meaningful density/state variants with documented invalid combinations instead of all prop products.

Review: task-specific structure and recovery are specified. Stress cases (Long labels; IME composition; Stale suggestions; Disabled selected option) are addressed as intended behavior; none was executed. No arbitrary system values are introduced. Ready for a scoped prototype/specification review; runtime and rendered-quality approval remains pending.

## Complete checkout feature

Route: [Checkout & Payments](../../06-Patterns/Checkout%20%26%20Payments.md), [Form Workflows](../../06-Patterns/Form%20Workflows.md), [State Patterns](../../06-Patterns/State%20Patterns.md).

Information model: Cart -> delivery/address -> review total -> payment challenge -> result.

A task-based checkout sequence uses order summary beside forms on wide screens and inline summary on narrow screens. The final total and currency precede commitment.

Price changes return to an understandable review. Challenge cancellation, payment failure and unknown status retain cart/address; stable request identity and reconciliation prevent unsafe retries.

Field errors preserve input and focus the summary/field appropriately. Back after challenge reconciles service state. Do not require an account without a product rule.

Reuse address, commerce and receipt patterns. Payment idempotency is a service contract, not a loading-button property.

Review: task-specific structure and recovery are specified. Stress cases (Network timeout; Shipping unavailable; Long address; Back after challenge) are addressed as intended behavior; none was executed. No arbitrary system values are introduced. Ready for a scoped prototype/specification review; runtime and rendered-quality approval remains pending.

## Task-specific empty state

Route: [State Patterns](../../06-Patterns/State%20Patterns.md), [Feedback Components](../../05-Components/Feedback%20Components.md).

Information model: Identify cause -> explain scope -> authorized next action.

Use distinct first-use, zero-filter and restricted messages within the report list region. First-use can offer Create, filters offer Clear/adjust, restriction offers an allowed access route.

Initial loading does not show an empty state. A failed request has retry; lack of create authority cannot show an actionable Create button.

Keep copy concrete and translated-length tolerant. An illustration is optional only if it improves understanding; the action and status must remain discoverable.

Reuse report-list, button and link roles; no new decorative container or mascot is required.

Review: task-specific structure and recovery are specified. Stress cases (No create permission; Filters from URL; Slow initial request; Long translated copy) are addressed as intended behavior; none was executed. No arbitrary system values are introduced. Ready for a scoped prototype/specification review; runtime and rendered-quality approval remains pending.

## Creative spatial editor

Route: [Advanced Components](../../05-Components/Advanced%20Components.md), [Interaction Design](../../01-Foundation/Interaction%20Design.md), [Art Direction](../../02-Visual-System/Art%20Direction.md).

Information model: Canvas and layers -> selection -> properties -> reversible operation.

Use a spatial artboard with coordinated layers and property panels. Canvas context is primary while panels expose the selected object's controls; this is not a dashboard layout.

Tool switches preserve selection where appropriate. Undo/history distinguish reversible local edits from irreversible external operations. Conflicts preserve work for explicit recovery.

Offer non-drag movement/reordering alternatives, keyboard commands with discovery, and touch-appropriate controls. Thousands of layers need a tested virtualized navigation contract.

Reuse existing canvas chrome, command library and selection roles. Supported tablet scope must match actual editor capabilities.

Review: task-specific structure and recovery are specified. Stress cases (Thousands of layers; Touch input; Accidental destructive operation; Reduced motion) are addressed as intended behavior; none was executed. No arbitrary system values are introduced. Ready for a scoped prototype/specification review; runtime and rendered-quality approval remains pending.

## Healthcare record review

Route: [Product Thinking](../../01-Foundation/Product%20Thinking.md), [Data Management Patterns](../../06-Patterns/Data%20Management%20Patterns.md), [Content Design](../../01-Foundation/Content%20Design.md).

Information model: Verify patient/context -> review timeline/source -> reconcile supplied list -> confirm.

Keep patient identity, provenance and temporal ordering visible. Use the supplied clinical policy to define review and commitment; do not derive care recommendations from UI precedent.

Partial outages, stale entries and unverified data remain visibly uncertain. Denied records reveal only permitted information and offer an authorized path.

Similar names need sufficient identity context. Long medication names remain readable. Confirmations follow clinical/service authority; accidental commitments need specified recovery.

Reuse patient header and timeline roles. Policy, consent and clinical semantics are consequential external dependencies, explicitly unresolved in a design-only fixture.

Review: task-specific structure and recovery are specified. Stress cases (Similar patient names; Partial source outage; Restricted record; Long medication names) are addressed as intended behavior; none was executed. No arbitrary system values are introduced. Ready for a scoped prototype/specification review; runtime and rendered-quality approval remains pending.

## Messaging continuity

Route: [Collaboration Patterns](../../06-Patterns/Collaboration%20Patterns.md), [Media Components](../../05-Components/Media%20Components.md), [Notifications & Communication Patterns](../../06-Patterns/Notifications%20%26%20Communication%20Patterns.md).

Information model: Conversation list -> unread context -> thread -> composer -> delivery feedback.

Use a continuous message thread and anchored composer, with contextual conversation list on wide screens. Keep drafts tied to their conversation.

Queued, sent, delivered and failed states differ. Reconnect retries according to stable message identity; attachment failure preserves the draft and permits retry/removal.

New messages do not force scroll away from the user's reading position. Provide unread navigation; announcements avoid flooding; long content and large text remain readable.

Reuse conversation, composer and delivery markers. Presence is an estimate, while delivery status requires service evidence.

Review: task-specific structure and recovery are specified. Stress cases (Long thread; Upload failure; Reconnect; Keyboard and large text) are addressed as intended behavior; none was executed. No arbitrary system values are introduced. Ready for a scoped prototype/specification review; runtime and rendered-quality approval remains pending.

## Batch findings

The sixteen proposals use native sequential commitment, comparative analytical workspaces, paired ledgers, editorial reading, scoped access management, grouped forms, comparison tables, retrieval pages, contextual onboarding, a reusable control contract, commerce review, causal empty states, a spatial canvas, a clinical timeline and conversation continuity. The shared authority/token model does not require shared page composition.

The initial static route audit exposed unreachable Advanced Components and Media Components guides; Knowledge Graph now connects both. Critical service dependencies stay explicit in finance, permissions, healthcare and messaging. A future independent artifact-based batch should test visual craft, actual keyboard/focus behavior, state execution and whether the model follows these instructions under generation pressure.
