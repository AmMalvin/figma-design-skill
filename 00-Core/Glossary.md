# Design vocabulary

| Term | Meaning and boundary |
| --- | --- |
| Foundation | Product design principles and visual decisions such as type, color, space and motion |
| Primitive token | Named raw reusable value without product meaning |
| Semantic token | Role or purpose mapped to a primitive or another justified alias |
| Component token | A component-specific contract mapped to system semantics when needed |
| Variable | Figma's reusable typed value; collections and modes organize contextual values |
| Style | A reusable group of visual properties; useful where a single variable cannot represent a composite |
| Component | Reusable anatomy and behavior with a meaningful API |
| Composite component | Composition of components that shares a reusable interaction need |
| Pattern | A recurring solution spanning decisions or a task flow |
| Template | A structural starting composition with content/behavior constraints |
| Product-specific component | Reuse within a product domain, with business concepts unsuitable for the core system |
| Screen | A view of one moment in a flow |
| Flow | Connected states, decisions, entry/exit and recovery for a user goal |
| State | Condition affecting behavior or presentation; not every state is a persisted variant |
| Density | Information/task throughput balanced with legibility and input comfort |
| Reference | Evidence or inspiration with scope, provenance and adaptation limits |
| Heuristic | A diagnostic rule of thumb, not measured proof |
| Critique | Evidence-based assessment and proposed improvement |
| QA | Verification of the implemented or inspectable contract |
| Permission state | What users can perceive or do under effective access; distinct from authentication |
| Optimistic UI | Provisional feedback before commitment; requires rollback and uncertainty handling |

Engineering: [Token Architecture](../03-Design-Tokens/Token%20Architecture.md) and [Component Principles](../05-Components/Component%20Principles.md).
