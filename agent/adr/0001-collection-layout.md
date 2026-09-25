# ADR 0001: Keep each skill independently installable

- Status: Accepted
- Date: 2026-09-24

## Context

The project contains three distinct skills: technology planning, engineering-lead review, and management-report structuring. They share a management decision context but have different triggers, outputs, references, and evaluation examples.

## Decision

Organize the repository as a skill collection: each installable skill lives at `skills/<frontmatter-name>/SKILL.md`. Keep skill-specific references, templates, scripts, and evals with that skill. Use `agent/` for shared standards and `README.md` for discovery and installation.

Do not add a root-level router `SKILL.md` in this change. A root skill would need a distinct user-facing workflow to justify being installed alongside the existing standalone skills.

## Rationale

- A user can install only the skill needed for the current task.
- Each skill's local assets and eval cases stay next to the workflow that uses them.
- Shared rules have one canonical source and can evolve without copying policy into every prompt.
- This combines the single-skill packaging clarity of `evidence-based-person-analysis` with the multi-skill collection pattern used by community skill repositories.

## Consequences

- Directory names match existing frontmatter names; skill names and behavior are not changed by the move.
- README and a small validator are required to keep entrypoints, links, and basic metadata discoverable.
- At the time of this decision, redistribution status was unresolved. That provisional state was superseded by [ADR 0003](0003-repository-wide-mit-license.md), which applies MIT to the repository and all four independently installable skills.
