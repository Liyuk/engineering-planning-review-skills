# Methodology-Derived Skill Implementation Record

**Goal:** Shorten explicit skill invocations, preserve the user's engineering-management methods, and add a complete metric decision skill with behavioral eval coverage.

**Architecture:** Each skill remains an independently installable folder whose short frontmatter name matches its directory. Shared evidence and scoring contracts stay in `agent/`; task-specific methods and cases stay with their skill. A methodology map links public writing topics to skill responsibilities and boundaries.

**Tech Stack:** Markdown, YAML frontmatter, JSON eval cases, Python repository validator.

**Spec:** `docs/superpowers/specs/2026-09-24-methodology-derived-skills-design.md`

## Completion

- [x] Rename existing skill packages to `tech-planning`, `tech-review`, and `eng-reporting`.
- [x] Add `metric-decision` with workflow, method reference, and three eval cases.
- [x] Record writing-to-skill mapping and differentiation boundaries.
- [x] Add missing, conflicting, and normal eval cases for all skills with shared rubric.
- [x] Update planning/review/reporting guidance where baseline or contract conflicts were identified.
- [ ] Complete forward behavioral review for all skill cases.
- [ ] Run repository validation after all edits.
