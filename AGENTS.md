# Repository guidance

This repository is a collection of independently installable skills for Chinese-language engineering planning, technical review, metric decisions, and management reporting.

## Source of truth

- `README.md` is the repository catalog and installation guide.
- `agent/` owns rules shared across multiple skills. Keep each shared rule in one canonical document; skills operationalize those rules and link back to them.
- `skills/<skill-name>/SKILL.md` is the standalone entrypoint. Keep skill-specific references, templates, eval cases, and scripts with that skill so it can be installed independently.
- `docs/research/` stores cited repository research. `docs/superpowers/` stores design and implementation records for this repository.

## Change rules

- Preserve independent skill boundaries; do not create a root router skill unless it adds a distinct, useful invocation path.
- When a shared rule changes, update its canonical `agent/` document and every affected skill in the same change.
- When skill behavior changes, update or add eval cases that exercise the behavior and its boundary conditions.
- Distinguish user-provided facts, sourced facts, measurements, estimates, inferences, assumptions, and unknowns. Never invent metrics, citations, or review findings to satisfy an output template.
- Keep review and revision as separate actions unless the user explicitly requests both.
- The root `LICENSE` is the canonical repository license. Each independently installable skill declares the same SPDX identifier in its frontmatter so the license remains visible when copied alone. Document any explicitly approved exception in both the skill and README.
- Run `python3 scripts/validate_repo.py` after moving skill files or changing local references.
