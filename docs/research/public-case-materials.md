# Public engineering cases for skill evaluation

**Research date:** 2026-09-24
**Purpose:** Create reproducible, source-grounded prompts for qualitative pressure testing of the four skills in this repository.
**Source policy:** Prefer first-party engineering publications. The notes below paraphrase sources and link to them; they do not reproduce their prose.

## How to use these cases

Treat each case as a bounded exercise: give the model the cited public facts plus the prompt below, and ask it to produce the skill's normal output. Score only whether the response handles the supplied evidence and unknowns well. These public write-ups are selective accounts, not complete internal records. They are suitable for qualitative pressure tests; they do not reproduce the original operating context, establish causal effects beyond what the source itself reports, or demonstrate that a skill works generally. Keep the source facts, evaluator-added constraints, and model inferences distinct.

For a fair baseline comparison, run the same prompt once without the skill and once with the skill, keep the model/settings constant, hide which response used the skill from the scorer if practical, and score both against the same rubric. Do not score agreement with the source author's decisions as inherently correct.

## Case 1 — Technical planning: choose a database migration approach

**Source:** GitHub's first-party announcement for [`gh-ost`](https://github.blog/news-insights/company-news/gh-ost-github-s-online-migration-tool-for-mysql/), published 2016-08-01.

**Source facts:** GitHub described schema changes happening multiple times per day and compared replica migration, MySQL Online DDL, and migration tools. It identified operational overhead, replica lag, limited throttling/pausing, and user-impact concerns among the trade-offs. The post explains why GitHub built and open-sourced a triggerless online migration tool. These are GitHub's historical account and stated rationale, not a neutral benchmark of all options.

**Evaluation prompt:**

> We run a high-traffic MySQL service and expect several schema changes a day. Product asks us to choose between replica migration, native Online DDL, and an online migration tool. We have not provided table sizes, write rates, acceptable replica lag, rollback needs, staffing, budget, or a representative benchmark. Use the public GitHub case as one reference. Produce a short decision brief: clarify what the case supports, what it does not prove for our system, the unknowns to collect, the viable options and trade-offs, and a reversible next step. Do not assume GitHub's scale or constraints are ours.

**What this tests:** Context-bound comparison, explicit resource and operational trade-offs, inference limits, decision gates, and a concrete validation step. A weak answer may present gh-ost as universally best or treat the source's historical rationale as current comparative evidence.

**Important gaps:** No target system measurements, business context, staffing/cost constraints, current versions, workload, or acceptance thresholds are provided by the prompt. The 2016 source may not describe current alternatives or current GitHub practice.

**Copyright note:** Use a short paraphrase and the source link; do not copy the article's detailed option descriptions into a test fixture.

## Case 2 — Metric decision: interpret engineering productivity without gaming it

**Source:** GitLab's first-party [`How we measure engineering productivity at GitLab`](https://about.gitlab.com/blog/measuring-engineering-productivity-at-gitlab/), published 2020-08-27 and republished 2020-09-02.

**Source facts:** GitLab defines MR Rate as team MRs divided by team members during a month, and describes reasons it uses that measure. It also reports labeling/data-quality problems, team differences, the danger that higher MR Rate can reflect quantity over quality, and its decision not to use the metric as an individual underperformance measure. The company pairs it with other indicators and uses trends as prompts for investigation.

**Evaluation prompt:**

> A director says our team's MR Rate rose 25% this quarter, so individual productivity improved and we should set individual targets next quarter. The only data supplied is the aggregate MR Rate. We do not have the denominator history, MR size/type mix, review/quality outcomes, team composition changes, cross-team contribution attribution, or delivery outcomes. Use GitLab's public account as a reference, not as proof our situation is identical. State what can be concluded now, what remains unknown, what companion measures or data checks are appropriate, and whether the proposed individual target is supported.

**What this tests:** Metric definition/denominator, data quality and cohort comparability, guardrails, correlation-versus-causality, incentive side effects, and disciplined recommendation under thin evidence.

**Important gaps:** The prompt deliberately omits local metric definition, baseline values, composition, quality, and user outcomes. GitLab's policy and organizational context cannot determine this team's best policy.

**Copyright note:** The formula and rationale are summarized for identification; use the linked page for context and avoid copying its narrative.

## Case 3 — Technical review: evaluate migration workflow controls

**Source:** GitHub's first-party [`Automating MySQL schema migrations with GitHub Actions and more`](https://github.blog/enterprise-software/automation/automating-mysql-schema-migrations-with-github-actions-and-more/), published 2020-02-14, updated 2021-08-12.

**Source facts:** GitHub describes a multi-stage migration process involving developer proposals, peer/schema review, database-infrastructure approval, selecting target clusters and execution method, monitoring, cleanup, and follow-up. It describes long-running migrations, production availability concerns, toil, and its effort to automate manual workflow steps. The source is a retrospective design narrative, not a complete threat model or formal design specification.

**Evaluation prompt:**

> Review this proposed production migration workflow: “A developer opens a schema PR; CI generates SQL and checks syntax; after one maintainer approval, an automation applies it to every production cluster. The job exits successfully when the command returns zero. We have no staged rollout, runtime lag/error thresholds, pause control, concurrency check, owner for production execution, or post-migration verification in the proposal.” Use GitHub's public migration workflow as a comparison point. Report only evidence-supported findings, grouped by impact, evidence, and recommended action. Separate blockers from follow-up improvements; do not claim a complete security or compliance audit.

**What this tests:** Whether the skill identifies material operational gaps, ties each finding to prompt evidence, proposes practical actions, and distinguishes blocking findings from non-blocking improvements.

**Important gaps:** The prompt gives no schema, table size, replication topology, traffic profile, database version, failure budget, rollback design, or authorization model. Any finding depending on those facts should be framed as a question or conditional risk.

**Copyright note:** The prompt is an original synthetic scenario informed by a brief paraphrase; it does not reproduce GitHub's workflow text or claim it was GitHub's exact implementation.

## Case 4 — Engineering reporting: turn an incident record into a decision-ready update

**Source:** Google's first-party SRE Workbook chapter, [`Postmortem Practices for Incident Management`](https://sre.google/workbook/postmortem-culture/), including its documented satellite-machine incident (2014-08-11; postmortem published 2014-08-15).

**Source facts:** The case describes a faulty decommission automation triggering removal of all satellite machines rather than one rack; front-end queries dropped and traffic shifted to core at a latency cost. The postmortem notes that impact figures were partly estimated and monitoring data was unreliable, and its impact section gives caveats and recovery details. Google notes that some names and values were fictionalized or replaced with placeholders.

**Evaluation prompt:**

> Prepare a leadership update from this public case for a VP who can prioritize engineering capacity but cannot decide product scope. Limit the update to 130 words. State the user impact, what is known versus estimated or unknown, the immediate mitigation, the system-level cause described in the postmortem, and the decision or next action leadership should take. Do not blame an individual, invent the redacted numbers, or claim that the mitigation prevented recurrence. Keep the source's caveat that some values were redacted/estimated.

**What this tests:** Audience/task matching, concise reporting under a hard limit, provenance and uncertainty labels, blameless causal framing, authority-aware asks, and actionable follow-up.

**Important gaps:** Some names and capacity figures were fictionalized or redacted. The source is a public postmortem, not the original raw logs; the evaluation must not infer exact losses, revenue impact, or individual responsibility.

**Copyright note:** Use only the short factual paraphrase and link. Do not copy Google's incident narrative or template wholesale.

## Suggested scoring rubric

Score each dimension 0–2 (0 = absent or materially wrong, 1 = partial, 2 = clear and appropriate). Record evidence for each score.

| Dimension | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Factual restraint | Invents/overstates facts or treats inference as fact | Mostly careful, with one meaningful overstatement | Separates source facts, supplied facts, inference, estimates, and unknowns |
| Task fit | Misses the requested decision/review/report | Addresses task but misses a key constraint | Directly answers the requested task and audience/format constraints |
| Evidence use | Recommendations are unsupported or vague | Some links between evidence and conclusions | Conclusions and findings point to specific prompt/source evidence |
| Actionability | No practical next step | Generic next step | Concrete, proportionate action with an owner/decision gate where appropriate |
| Judgment/calibration | Overconfident or mechanically follows a template | Some calibration but uneven | Confidence and severity match evidence; permits “no blocker” when warranted |

Maximum: **10 points per case**. Keep per-dimension scores; a single total can hide important failure modes. For paired skill/no-skill runs, report both scores and quote only brief output fragments needed to explain score differences. One run per prompt is exploratory evidence, not a reliable estimate of general performance.

## Source and scope limitations

- Sources are first-party engineering publications from GitHub, GitLab, and Google. They are authoritative for what those organizations publicly reported, not independent verification of every claim or proof that the practices generalize.
- The cases mix a historical tool decision, an organizational metric, a workflow design, and a postmortem. That is useful breadth for a first qualitative suite, but not representative sampling.
- The case prompts are evaluator-authored adaptations. Explicitly identify those synthetic constraints as such; do not imply the original organizations encountered the exact scenarios.
- These are public-source materials for qualitative pressure testing. They do not reproduce the original operational context or establish causal conclusions about skill effectiveness.
