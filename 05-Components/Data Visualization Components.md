# Data visualization

Begin with the analytical question and decision. A chart without a useful relationship is decoration; an exact-value table may be clearer.

| Need | Candidate | Guardrail |
| --- | --- | --- |
| Compare categories | Aligned bars/dots | Bars use a zero baseline; alternatives disclose different scale reasoning |
| Trend over time | Line | Show time range, units, gaps and comparable scales |
| Distribution | Histogram/box plot | Explain bins/summary meaning for the audience |
| Relationship | Scatter | Avoid implying causation from correlation |
| Part-to-whole | Stacked bar or few clearly labeled segments | Accurate total; avoid difficult many-slice comparison |
| Exact records | Table | Preserve precision/units and sortable context |

Do not combine every chart into one Type variant. Shared legend/axis/tooltip primitives can support distinct chart contracts.

Show source/freshness, denominator, period, uncertainty and missing values when relevant. Distinguish zero, unknown and absent. Avoid misleading scale truncation, excessive 3D/perspective and decorative gauges.

Essential insight/value access cannot rely on hover. Provide readable labels, accessible summary and equivalent data/task route; define keyboard exploration if interactive. Do not add hundreds of Tab stops blindly.

Responsive charts can change labels, legend, aggregation or detail strategy while preserving the question. Specify drill-down return, filter scope, cross-highlighting, loading/empty/error and reduced motion.

Verify real extrema, negative values, small/missing series, dense labels and readable encoding without color alone. [Accessibility](../01-Foundation/Accessibility.md), [Data-Dense Interfaces](../06-Patterns/Data-Dense%20Interfaces.md)
