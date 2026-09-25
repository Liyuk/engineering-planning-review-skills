# Metric and Decision Method

Use this reference when a request needs detailed metric design or investigation. Keep the workflow proportional: do not build a dashboard or full event taxonomy when a small definition check answers the decision. For a requested minimum design, show the primary metric, only the events needed to calculate it, one data-quality check, and list further diagnostics as optional.

## 1. Define the task before choosing metrics

Describe who does what, under which conditions, to obtain which result. Specify the start and end of one task, observable success and failure, exclusions, and the user-visible consequence. A successful API response is not necessarily a successful user task.

## 2. Map states and events

List the meaningful states and transitions before proposing instrumentation. Include success, failure, timeout, cancellation, retry, and late completion when they affect the outcome. Events should share an identifier for one task and include only fields needed for the decision and diagnosis.

| State transition | Event evidence | Diagnostic use |
| --- | --- | --- |
| Task begins | start event and task ID | denominator and entry volume |
| Work is submitted | submit event, attempt, context | retries and processing latency |
| User sees a result | success/failure/timeout event | user-visible completion and delay |
| Backend finishes later | final outcome linked to task ID | user-visible versus eventual success |

## 3. Write a metric definition card

| Field | Required detail |
| --- | --- |
| Decision | What choice could this metric change? |
| Object | User, session, request, or end-to-end task |
| Numerator / denominator | Explicit formula and population |
| Exclusions | Tests, duplicates, invalid or unlinked events; report excluded volume separately when material |
| Source and window | Dataset, instrumentation/version, dates, delay, sample size |
| Segments | Only dimensions relevant to the decision, with per-segment sample sizes |
| Companion metrics | Pick only the layers relevant to the decision: L1 user outcome, L2 experience/risk guardrails, L3 diagnostic signals, and L4 measurement health |
| Limits | What the metric cannot establish |

For a normal plan, distinguish the primary outcome (L1), material guardrails (L2), optional diagnosis (L3), and data-quality checks (L4). Do not require all four layers for a minimum request; the minimum-design rule in `SKILL.md` takes precedence.

Never compare values across changed definitions or collection paths as if they were one continuous series. If they can be reconciled, document the method; otherwise mark the windows non-comparable.

## 4. Verify an observed change

Check these questions in order:

1. Is event coverage, task linkage, deduplication, and reporting delay stable?
2. When did the change start, and did releases, traffic, definitions, or instrumentation change at the same time?
3. Where is it concentrated? Compare relevant platforms, versions, entry points, and conditions while retaining sample sizes.
4. What changed for the user or system? Pair outcome metrics with latency, retries, failures, abandonment, and data-quality signals.
5. Which explanation can be reproduced or falsified with logs, traces, a controlled rollout, or another available check?

An anomaly record should label **observed facts**, **hypotheses**, **unknowns**, and **current decisions/actions** separately. Record counter-evidence and the strongest alternative explanation.

## 5. Turn analysis into a verified action

Use an action hypothesis card:

| Field | Description |
| --- | --- |
| Observation | The measured change and comparable baseline |
| Hypothesis | A falsifiable explanation, with evidence and alternatives |
| Action | Smallest useful intervention or next investigation |
| Expected result | Primary metric and direction; do not invent a target |
| Guardrails | Outcomes that must not materially worsen |
| Verification | Same definition, relevant slices, full comparison window, and owner/date when known |
| Stop / rollback | Threshold or observed condition that reverses or pauses the action |

When randomized testing is unavailable, use comparable complete windows, mark concurrent changes, preserve metric definitions, and describe the result as an observed association rather than proven causation. Verify the original user task after a change; deployment alone is not evidence of success.

## 6. Choose a review cadence that can still change the decision

Retain a light periodic record when users need to see whether a signal is changing over time. Each comparable row should keep the task/metric definition version, dates, numerator and denominator, traffic or version context, data coverage, material changes, current interpretation, and action status. If definitions or collection paths changed, split the series or record the reconciliation method instead of drawing a continuous trend.

Set cadence by the decision's risk and the signal's freshness: a release-related high-risk measure may need a pre/post-release check; a stable low-risk measure may need only a weekly or monthly review. A normal period does not require a long report or meeting. Review whether prior actions changed the original user outcome, and change or stop the action when the evidence invalidates its hypothesis.
