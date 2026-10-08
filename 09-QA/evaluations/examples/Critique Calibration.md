# Critique calibration

Apply [Design Critique](../../Design%20Critique.md) to the three written specifications. Ratings below describe intended evidence: 2 viable, 3 strong, U unknown and NA not applicable with a reason. They do not score rendered output, and no aggregate is used. The same author wrote and reviewed these examples.

| Dimension | Transfer | Analytics | Editorial |
| --- | --- | --- | --- |
| User-goal alignment | 3: review before monetary commit | 3: comparison to investigation | 3: locate and trust current policy |
| Task completion | 2: status and receipt specified | 2: drill-back preserved | 2: browse, read and return |
| Information architecture | 3: explicit decision sequence | 3: linked comparison/detail | 3: version and article hierarchy |
| Interaction clarity | 2: edits and commit boundary | 2: shared selection/filter scope | 2: outline and retrieval paths |
| Visual hierarchy | 2: recipient and total priority | 2: concurrent expert priorities | 2: body over related links |
| Typography | U: actual ledger styles unrendered | U: numeric/label rendering absent | U: actual article measure unrendered |
| Spacing | U: native geometry uninspected | U: compact spacing unrendered | U: section rhythm unrendered |
| Composition | 2: review label/value sequence | 3: comparative workspace | 3: editorial reading structure |
| Density | 2: compact review without crowding | 2: useful compact comparison | 2: reading measure takes precedence |
| Color | U: semantic intent, contrast untested | U: palette/series contrast untested | U: link/text contrast untested |
| Accessibility | 2: intended naming/focus/status | 2: intended table/chart alternative | 2: intended headings/reflow |
| Feedback | 3: unknown differs from success | 3: source freshness explicit | 2: archive/failure distinctions |
| Error prevention | 3: total and recipient before commit | 2: explicit filters and selection | 2: current-version provenance |
| Recovery | 3: reconcile before retry | 3: retained comparison context | 2: return and current policy route |
| Responsive behavior | 2: text and keyboard intent | 2: comparison/detail access | 2: article and local overflow |
| Platform appropriateness | U: target OS verification required | 2: web table model specified | 2: web reading/navigation model |
| Design-system consistency | 2: no arbitrary native restyling | 2: existing semantic/density roles | 2: article/link roles reused |
| Component reuse | 2: controls/receipt mapped conceptually | 2: chart/table primitives | 2: document metadata/article |
| Content quality | 2: state-specific copy contract | 2: unit/source/status contract | 2: ownership/version fields |
| Motion | NA: no motion required by spec | NA: no motion required by spec | 2: optional navigation reduction |
| Performance perception | 2: truthful request state | 3: usable retained context | 2: loading not mistaken for absence |
| Edge cases | 2: offline/long name/unknown result | 2: missing/large data/narrow scope | 2: archive/RTL/long headings |
| Implementation feasibility | U: service/API evidence absent | U: data/query/runtime absent | U: permission/version routes absent |
| Originality | 2: task-fit rather than decoration | 2: distinctive analytical structure | 2: restrained provenance structure |
| Polish | U: rendered artifact required | U: rendered artifact required | U: rendered artifact required |

## Failure calibration

Hypothetical comparator: an attractive banking mockup with a glowing balance card, decorative chart and immediate ?Transfer complete? after a timeout. This is an invented specification for rubric calibration, not a screenshot audit.

Finding: critical, high confidence in the described contract. A timeout cannot establish monetary success; the design misleads the user and may induce duplicate transfers. User-goal alignment, feedback, error prevention and recovery are weak regardless of attractive typography. Repair: retain pending/unknown state, reconcile the original request and expose only service-supported retry. Verification: runtime timeout, delayed success and duplicate-request tests. An aggregate visual score cannot approve this flow.

The restrained transfer specification ranks above that comparator on task reasoning. Typography, spacing and polish stay unknown until actual rendering; the comparison is not empirical user-test evidence.
