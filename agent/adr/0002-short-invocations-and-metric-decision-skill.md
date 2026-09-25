# ADR 0002: Short Skill Invocations and Evidence-Based Metric Decisions

## Status

Accepted

## Context

The original skill folder/frontmatter names were long to type and overlapped in scope. The writing corpus contains a complete recurring method for defining measurements, checking data quality, investigating changes, and verifying resulting actions. The collection also needs shared evaluation cases that test missing data, conflicting information, and normal requests.

## Decision

- Use the short explicit commands `$tech-planning`, `$tech-review`, `$eng-reporting`, and `$metric-decision`; the folder and frontmatter `name` stay identical.
- Preserve normal automatic discovery. Short names improve explicit invocation and do not replace the actual differentiation.
- Add `metric-decision` as a standalone skill because metric definition and causal investigation have a distinct input, workflow, and output from planning, review, and reporting.
- Distill the user's writing into reusable methods and boundaries; do not copy whole articles or turn every article topic into a separate skill.
- Keep management retrospective as a mode/candidate until it demonstrates a distinct trigger and output; defer a standalone AI-value skill until there are enough representative cases.
- Evaluate each skill with missing-information, conflicting-information, and normal cases using `agent/eval-rubric.md`.

## Consequences

- Existing skill folder paths change, so README and local references must use the short names.
- `metric-decision` can be installed independently and includes its method reference and eval cases.
- A short command alone does not improve behavior; existing planning/review/reporting instructions and their relevant references must preserve evidence status, bounded conclusions, actionable review findings, and proportionate tone.
- The shared rubric is not proof of skill quality by itself; behavioral samples still require human review.
