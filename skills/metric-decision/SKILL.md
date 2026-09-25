---
name: metric-decision
description: Use when the metric itself needs definition or validation, when a product/engineering metric changes unexpectedly, or when measurement evidence must support an action. Use tech-review for broader proposal review.
---

# Metric Decision

Start from the user task, check how the number was produced, then connect trustworthy measurement to a decision. A metric is useful only when its object, definition, evidence quality, and decision consequence are clear.

## Workflow

1. **Frame the decision.** Identify the user task or system outcome, audience, scope, and comparison window. Turn vague requests such as “saving is slow” into an observable task.
2. **Define the measure.** State the measured object, numerator, denominator, exclusions, source, time window, segments, sample size, and relevant companion or guardrail metrics. If inputs are missing, mark them unknown and give the calculation needed. Match detail to the decision: for a minimum design, start with the primary metric, the smallest event set that computes it, and one material data-quality check; keep optional diagnostics separate.
3. **Track evidence status.** Mark material claims as user-provided, sourced, measured, estimated, inferred, assumed, or unknown/to confirm. Preserve source, method, and date/window; do not promote an estimate or hypothesis to fact.
4. **Validate before explaining.** Check definition changes, instrumentation coverage, delays, duplicate events, sample size, and comparability. Separate a real product change from a measurement change.
5. **Bound the explanation.** Compare plausible explanations and state what evidence would confirm or reject each. Do not claim causation from timing or correlation alone.
6. **Make the next action testable.** For each proposed action, state the hypothesis, expected metric movement, guardrails, owner or decision needed when known, verification window, and stop or rollback condition.

## Output

Match detail to the request. For an investigation, report the decision question, metric definition and evidence status, supported finding, unresolved explanations, and next action with verification. For a measurement-design request, provide the task definition, event/state model, metric card, and data-quality checks. Read [the method reference](references/metric-decision-method.md) for the cards and diagnostic sequence.

Use the shared evidence labels in the repository's `agent/decision-and-review-contract.md` when available. Preserve source, method, and time window when handing results to planning, review, or reporting. For a worked example, read [instrumentation-change example](examples/instrumentation-change.md).

Use this skill when measurement itself is the task. Route broader investment choices to `tech-planning`, review of an existing proposal to `tech-review`, and audience-specific communication of confirmed findings to `eng-reporting` when those skills are available.
