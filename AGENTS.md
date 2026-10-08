# Repository operating contract

This repository packages one design skill. For a design task, read [SKILL.md](SKILL.md), then only the modules relevant to the requested outcome. For a repository change, inspect affected files and their callers; a full-repository audit is appropriate only when architecture is under review.

- Preserve unrelated working-tree changes. The audit's three pre-existing edited files are listed in [09-QA/audit-baseline.json](09-QA/audit-baseline.json).
- [AI Operating Rules](00-Core/AI%20Operating%20Rules.md) owns design-source precedence. Specialist documents define decisions within their scope.
- Read the relevant directory's AGENTS.md before using or editing its modules if that scoped guidance has not already been loaded.
- Keep shared rules at their owner; link instead of copying. Preserve compatibility entry paths until callers and migration needs are checked.
- Make recommendations explain product fit, alternatives, failure conditions and verification. Do not impose one visual formula across products.
- Run `python scripts/validate_repository.py` and `python -m unittest discover -s tests -v` after structural, reference-schema or evaluation changes. Use relevant scenarios in [09-QA/evaluations/README.md](09-QA/evaluations/README.md) for design-instruction changes.
- Report observed checks separately from proposed tests. Do not claim a Figma file, prototype or runtime was inspected unless it was.
- Local instructions do not authorize publishing libraries, changing permissions, messaging others or touching unrelated product assets.

Scoped AGENTS.md files cover only Figma operations, evidence curation, evaluation and the preserved legacy notes. This contract does not require rereading the entire repository for small tasks.
