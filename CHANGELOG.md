# Changelog

## v1.0.0 — 2026-09-24

Initial public release of four independently installable skills:

- `tech-planning` — technical investment choices and roadmaps.
- `tech-review` — evidence-based review of existing proposals.
- `metric-decision` — metric definition, validation, and decision follow-through.
- `eng-reporting` — evidence-preserving engineering management updates.

The collection uses the MIT License. Each skill includes its own entrypoint, focused references, and scenario evaluations where applicable. The planning workflow distinguishes confirmed owners from suggested or unknown responsibility assignments.

### Verification

- `python3 scripts/validate_repo.py` passed.
- Vercel Skills CLI copied all four skills from the public repository into a temporary Codex skills directory.
- The repository contains 29 scenario prompts. A single-run, rubric-scored behavior spot check covered 12 prompts; one planning attribution issue was corrected and two focused reruns scored 10/10. This is exploratory evaluation, not evidence of general improvement across models or tasks.
- Installation and behavior were smoke-tested with Codex. Claude Code and other agent hosts have not been directly validated.

No npm package is published; install from GitHub with the Skills CLI.
