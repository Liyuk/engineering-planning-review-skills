# Metric Decision Skill Adoption Plan

**Goal:** Make `$metric-decision` distinct, independently usable, behaviorally evaluated, and ready for public discovery once repository ownership and licensing are settled.

**Architecture:** Keep one concise skill entrypoint for routing and core workflow, a focused reference for measurement mechanics, eval cases for missing/conflicting/normal inputs, and one end-to-end example for onboarding. Keep installation and repository-wide discovery instructions in the root README.

**Tech Stack:** Agent Skills (`SKILL.md`), Markdown, JSON eval cases, Python validation, Vercel `skills` CLI for local discovery/install compatibility checks.

**Spec:** `docs/superpowers/specs/2026-09-24-methodology-derived-skills-design.md`

## Review Focus

- A migrated event definition can make two metric values incomparable; test behavior before causal explanation.
- Competing reports may use different objects or denominators; preserve both sources and state what would reconcile them.
- A normal measurement-design request should get a usable minimal design without invented targets or oversized instrumentation.
- A public install path depends on a public repository URL; document a pattern without inventing owner/repository details.
- Public redistribution depends on license status; do not imply a license or publish on the user's behalf.

## Tasks

### Task 1: Lock the distinction and audience

- [x] Position the skill around user-task measurement, data validity, bounded explanation, and verifiable action.
- [x] State the boundary from coding workflow, plan review, planning, and reporting in the writing-to-skills map.
- [x] Make the one-line value proposition visible in the skill README/catalog and the skill's first paragraph.

### Task 2: Complete the standalone skill package

- [x] Add concise `SKILL.md`, full measurement method reference, and missing/conflict/normal eval cases.
- [x] Use the shared evidence-state contract and score rubric.
- [x] Add one end-to-end example showing a metric movement that coincides with an instrumentation change.
- [x] Confirm no broken dependency on files outside the individual package for normal use. The shared evidence contract is explicitly optional when unavailable; method and example links stay inside the package.

### Task 3: Make discovery and adoption concrete

- [x] Add `$metric-decision` to the collection catalog and install guidance.
- [x] Add a public-repository install example that selects only this skill, plus a local smoke-check command.
- [x] Explain who should use it and when to hand off to planning, review, or reporting.

### Task 4: Run behavioral evaluation and repair

- [x] Compare a no-skill baseline with the skill on the saving-success / instrumentation-migration case.
- [x] Forward-test conflicting denominators and normal metric design.
- [x] Add a causal-boundary case where metric comparability is confirmed but cause is not.
- [x] Add rubric calibration anchors and run matched no-skill / skill checks for normal design and causal-boundary scenarios.
- [x] Identify that the normal-design response was more elaborate than a “minimum” plan needed; add an explicit minimum-design constraint.
- [x] Record baseline-versus-skill findings against the five shared rubric dimensions.
- [x] Fix the normal-design verbosity gap and re-run the affected case.

### Task 5: Verify release readiness

- [x] Validate folder/frontmatter names, references, and all JSON evals.
- [x] Run the local skill-list check via the skills CLI; a temporary Codex install copy matched the source `SKILL.md`.
- [x] Check the whole repository's licensing boundary and record what must be decided before publishing.
- [x] Update this plan with actual acceptance results and remaining limitations.

## Acceptance results

- Static repository validation passed for all four skill entrypoints, names, eval JSON files, and local Markdown links.
- Skills CLI listed the local package as one skill and copied it into a temporary Codex skills directory; installed and source entrypoint files matched.
- Missing-data and conflicting-denominator comparisons passed the five-part rubric at 10/10 with the skill. No-skill baselines scored approximately 6/10 and 8/10, respectively; see [`metric-decision-evaluation.md`](../../methodology/metric-decision-evaluation.md) for the limitations and observed evidence.
- Normal minimum-design case scored 10/10 both with and without the skill. The skill response more tightly followed the one-primary-metric / minimum-event-set / one-quality-check shape; this is a fit improvement, not a score gain.
- Causal-boundary case scored 10/10 with and without the skill. The skill made evidence status and confirm/reject criteria more explicit, with no rubric score gain.
- The shared rubric now includes concrete 0/1/2 calibration anchors for a causal-boundary scenario. These evaluations still use one sample per condition and are agent-scored, not a blinded human or multi-model study.
- No public remote or repository-wide license is configured. Public upload and redistribution are not complete; permission boundaries are retained in the README.

## Release boundary at plan time

When this plan was written, the repository had no configured public remote, the reporting skill declared `Proprietary`, and the new skill had no explicit standalone redistribution license. This plan prepared discoverability and local use without publishing or claiming open reuse.

## Subsequent licensing decision

This plan records the release boundary at the time it was written. The user later chose MIT for the entire repository; [ADR 0003](../../../agent/adr/0003-repository-wide-mit-license.md) and the root `LICENSE` supersede the provisional per-skill licensing status above. GitHub currently reports the repository as public; visibility is a separate setting from the license decision.
