# Representative design evaluations

[scenarios.json](scenarios.json) defines sixteen contrasting problems, with existing-system fixtures and stress cases. It covers every requested product class plus empty states, creative work, healthcare and messaging. These are scenario contracts, not automated proof of design quality.

## Run a forward evaluation

1. Start a fresh session with this repository, the scenario's prompt, fixture and deliverable. Let the generator discover SKILL.md. Do not give it evaluator criteria or another scenario's answer.
2. Produce the requested design/specification using only relevant routes. Record files read, assumptions, system bindings, composition and actual checks. Use isolated artifacts for tests; do not mutate production Figma files or publish anything.
3. Evaluate the resulting artifact against the scenario criteria and [Design Critique](../Design%20Critique.md). Each of the 25 dimensions needs evidence, a rating or justified unknown/not-applicable. A missing critical recovery or accessibility requirement blocks approval.
4. Apply stress cases to the artifact. A written plan is intended evidence; rendered QA is inspected evidence; interaction tests are observed evidence.
5. Compare the batch: mobile transfer, analytical comparison, editorial reading and creative canvas should not converge on the same composition. Shared tokens are expected; identical task structure needs a reason.
6. Record generator/evaluator, independence, source context, output artifact, findings, revisions and unresolved checks in [Evaluation Result](../../Templates/Evaluation%20Result.md). A different model or fresh reviewer is useful when authorized; an author review is labeled as such.

## Current evidence

[Author Walkthroughs](Author%20Walkthroughs.md) records sequential author reasoning across all sixteen routes. It is not an independent new-session experiment, usability study or rendered Figma test. [Examples](examples/README.md) contains contrasting worked specifications and critique calibration. Future runs can append dated results without replacing these evidence limits.

Run `python scripts/validate_repository.py` for route, local-link, reference-contract and preservation checks, and `python -m unittest discover -s tests -v` for tooling regressions. Those commands do not rate an interface. Use the actual artifact and runtime to evaluate typography, focus, assistive technology, latency and polish.
