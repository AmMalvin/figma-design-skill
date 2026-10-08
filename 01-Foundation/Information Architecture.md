# Information architecture

Owns content organization, vocabulary, search scope and navigation relationships. Widget behavior belongs in [Navigation Components](../05-Components/Navigation%20Components.md).

Inventory relevant objects, task entry points and relationships. Organize around user/domain models; company departments fit only when they match those models. Small edits do not need a full sitemap.

| Model | Fits | Failure condition |
| --- | --- | --- |
| Hierarchy | Stable contained parent/child resources | Cross-cutting tasks acquire duplicate homes |
| Sequence | Real prerequisites/commitment stages | Users need non-linear review/editing |
| Facets | Objects share independent attributes | Vocabulary is unknown or counts mislead |
| Workspace/matrix | Experts use simultaneous contexts | Beginners cannot locate the next decision |

Define metadata, labels, ownership and lifecycle where content needs them. Multiple discovery paths can lead to one authoritative object.

Differentiate global, section, contextual and utility navigation. Preserve location, back behavior, deep-link orientation and return state. Search complements structure; it cannot compensate for missing language or inaccessible content.

Use [Search Patterns](../06-Patterns/Search%20Patterns.md) for relevance/filter/access semantics. Verify findability through [Design Research](Design%20Research.md) when uncertain; card sorting and tree testing are useful methods, not compulsory ceremonies.
