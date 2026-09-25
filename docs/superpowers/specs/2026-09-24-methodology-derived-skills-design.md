# Methodology-Derived Skills Design

Date: 2026-09-24

## Goal

Make the collection easier to invoke and encode the user's distinct engineering-management judgment methods from `liyuk.github.io`, without competing with coding-workflow skills or plan-review skills on their strongest ground.

## Positioning

The collection serves the upstream and downstream decisions around engineering work: why an investment matters, what evidence supports it, how limited capacity should be allocated, who owns decisions, how outcomes will be verified, and how those judgments are communicated. Matt Pocock's skills focus on composable software delivery; Han's iterative plan review focuses on improving an existing plan. This collection should complement them with evidence-aware technical investment and organizational decision support, rather than reproduce their workflows.

## Invocation interface

Use concise task names as both skill folder names and frontmatter `name` values:

| Explicit invocation | Responsibility |
| --- | --- |
| `$tech-planning` | Shape technical investment choices and roadmaps. |
| `$tech-review` | Review an existing proposal for decision readiness. |
| `$eng-reporting` | Turn source material into an audience-specific management artifact. |
| `$metric-decision` | Define measures, validate changes, and connect evidence to action. |

Keep automatic discovery enabled. The descriptions support model routing; explicit names support human invocation.

## Skill boundaries

- **Planning** reasons from business context and constraints through capability gaps, portfolio choices, dependencies, and horizon-based roadmaps.
- **Review** evaluates an existing artifact. Findings include issue, evidence, impact, action, priority, and status; a review can pass with no blockers.
- **Reporting** reshapes supplied material for a reader while preserving source, estimate, inference, conflict, and unknown states.
- **Metric decision** defines the task and measure, validates instrumentation/comparability before causal explanation, and defines a verifiable action.
- **Management retrospective** stays within reporting/planning as a mode until it has a sufficiently distinct trigger and output. AI workflow value analysis remains a future specialist candidate.

## Shared method

Preserve the user's judgment spine: define the decision and desired outcome; state evidence and its status; identify constraints and alternatives; compare consequences and opportunity costs; clarify ownership and decision rights; define verification and invalidation conditions; revisit when evidence changes. This is not a mandatory visible outline.

Unknown metrics must be marked to confirm with formula and missing inputs. Estimates retain assumptions and source. Conclusions stay within evidence. Review questions are not padded to reach a count. Reports may preserve conflicts provisionally when a timely draft is needed.

## Evaluation

Every skill has at least one missing-information case, one conflicting-information case, and one normal case. Score fact restraint, task match, actionability, format, and tone calibration from 0 to 2. A case passes at 8/10 only when fact restraint is 2 and no unsupported claim remains. Static validation verifies structure and links, not behavioral quality.

The source mapping and per-article method distillation live in [`docs/methodology/writing-to-skills-map.md`](../../methodology/writing-to-skills-map.md); the shared score anchors live in [`agent/eval-rubric.md`](../../../agent/eval-rubric.md).
