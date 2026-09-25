# Shared skill standards

This directory is the canonical home for rules used by more than one skill. Skill files should point here instead of copying shared policy. Skill-specific workflow details stay next to their `SKILL.md`.

| Document | Owns |
| --- | --- |
| `decision-and-review-contract.md` | Evidence states, bounded conclusions, review findings, and shared handoff fields |
| `eval-rubric.md` | Shared behavioral evaluation dimensions and pass thresholds for every skill |
| `adr/` | Accepted decisions about the repository's skill architecture and maintenance model |

If a rule is needed by only one skill, keep it in that skill's references. Add a shared document only when more than one skill needs the same contract.
