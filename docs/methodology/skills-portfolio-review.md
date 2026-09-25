# Skills Portfolio Review

Date: 2026-09-24

This note synthesizes the independent discussion group review of the four skills, the source-to-skill map, and the author's writing in `liyuk.github.io`. It records product boundaries and one round of behavioral comparison; it is not a claim that the skills outperform a capable base model in general.

## Portfolio purpose

The collection turns recurring engineering-management judgment into four callable workflows. Its shared thread is to make a decision easier to inspect: identify the outcome, preserve evidence and its status, compare constraints and options, make responsibility visible, and define what would change the decision. The four skills are complementary, not a mandatory sequence.

| Skill | User's question | Useful output | Boundary |
| --- | --- | --- | --- |
| `tech-planning` | Where should limited engineering capacity go, and what should we defer or stop? | Investment options, trade-offs, roadmap and decision gates | Does not conduct market research or supply missing business data by itself. |
| `metric-decision` | What does this number measure, can I trust its movement, and what action can it support? | Metric definition, data checks, bounded hypotheses and verification plan | Does not replace analysis of source data or prove causality from chronology. |
| `tech-review` | Does an existing proposal have enough evidence and delivery safeguards for the decision? | Findings tied to evidence, impact, action and a bounded conclusion | Does not guarantee production safety or replace specialist security, privacy, legal, or compliance review. |
| `eng-reporting` | How can existing project evidence help this reader decide or act? | Audience-shaped update, retrospective or promotion draft with provenance preserved | Does not create business impact, inflate an individual's role, or turn estimates into measured results. |

Use one skill for the actual task. Combine them only when the work crosses a real handoff: planning may need metric definition; a proposal review may need evidence validation; confirmed findings may then need a management update. The same evidence labels should follow the handoff.

## Differentiation and limits

The project's distinctive proposition is not code generation or a universal engineering-agent team. It is a Chinese-language, engineering-leadership decision workflow grounded in the author's writing: business and competitive context for investment choices; user-task definitions for measurement; findings that can be acted on; and communication organized around the reader's decision. Relevant source essays include [technical planning as business and competitive analysis](https://liyuk.com/writing/2025/11/technical-planning-business-and-competitive-analysis/), [define the measurement before arguing about metrics](https://liyuk.com/writing/2021/03/define-the-measurement-before-arguing-about-metrics/), [periodic metrics and retrospectives](https://liyuk.com/writing/2021/05/periodic-metrics-and-retrospectives/), [information sync for decisions](https://liyuk.com/writing/2023/03/information-sync-for-decisions/), and [AI productivity in complex systems](https://liyuk.com/writing/2026/08/ai-productivity-complex-systems/).

The packages can structure supplied information and expose missing evidence. They cannot independently verify unavailable source data, make an organization's decision, or ensure a proposal succeeds. Planning's external comparison is conditional on relevant sources being supplied or researched. The repository now has a unified MIT license and a public GitHub remote at [`Liyuk/engineering-planning-review-skills`](https://github.com/Liyuk/engineering-planning-review-skills).

## Source method coverage

The source writing contains more than four skill entrypoints can responsibly load on every task. The planning reference now preserves the original ten-part reasoning map: business context; competitive context; deduction and resource clocks; four-layer capability map; outcome and boundaries; portfolio choices; near/mid/far roadmap; collaboration and decision rights; operating cadence; and audience-specific communication. It is an on-demand map, not a mandatory ten-section answer template.

Other source methods remain visible in [`writing-to-skills-map.md`](writing-to-skills-map.md) but are only partially operationalized. The management retrospective's eight judgments and structured-thinking's five lenses are not a complete dedicated workflow in the current four skills. Reporting uses selected ideas such as reader decisions and evidence provenance; that is not equivalent to preserving the full retrospective or five-lens method. They are candidates for a separate skill only if they have a distinct trigger, output, and evaluation set. This is a known packaging boundary, not evidence that the original articles were absent from the source map.

## Discussion group findings

- **Planning:** the strongest fit is investment choice under constraints, including explicit defer/validate/abandon decisions. Do not market it as automatic competitor analysis; the current skill only uses external comparison when it helps and has evidence.
- **Measurement:** distinguish measurement validity from causal explanation, and use one primary metric plus minimal instrumentation when the user asks for a minimum design.
- **Review:** credible findings need evidence, impact and action; no-blocker proposals may pass. The skill can surface specialist-review gaps but cannot act as that specialist review.
- **Reporting:** organize material for a particular reader and decision. Preserve individual/team contribution boundaries and preserve conflicting source scopes; forceful writing must remain supportable.
- **Portfolio:** avoid a fixed four-step funnel. The user should call the one relevant workflow, then hand off only when another deliverable is needed.

## Matched behavioral spot checks

For one pressure case per skill, an evaluator agent generated a no-skill answer and then a skill-guided answer, scoring each against the shared five-dimension rubric. This is one sample per condition, not a blinded human study.

| Skill and case | Baseline → skill | Observed difference |
| --- | --- | --- |
| Planning: management demands a 20% conversion commitment without baseline | 10/10 (2,2,2,2,2) → 10/10 (2,2,2,2,2) | Both rejected unsupported commitment and avoided fictional staffing. Skill made the unproven link between checkout feedback, release delays and refactoring more explicit, and added decision gates. |
| Review: deadline pressure despite an unrepresentative benchmark and incomplete rollback plan | 10/10 (2,2,2,2,2) → 10/10 (2,2,2,2,2) | Both found material gaps; skill more consistently stated the review's evidence scope and fields. No failure in the baseline on this sample. |
| Reporting: request to inflate personal ownership and claim unmeasured growth | 9/10 (2,2,1,2,2) → 10/10 (2,2,2,2,2) | Both preserved facts. Baseline named missing evidence but did not give a concrete collection path; skill listed scope, integration result, personal contribution and metrics to gather. |
| Metric decision: completion rate rises while event linkage coverage falls | 10/10 (2,2,2,2,2) → 10/10 (2,2,2,2,2) | Both rejected celebrating or removing old monitoring; skill enumerated the reconciliation inputs and exit condition more explicitly. No score failure in the baseline on this sample. |

Score tuple order is fact restraint, task match, actionability, format, tone. Each 0–2 judgment is tied to the corresponding behavior described in the observation column. The only observed scored gap was reporting actionability in this sample; the other comparisons are consistency checks, not evidence that the skill is necessary for a capable model to reach the same conclusion.

These results show format and method consistency in these prompts, not a general score gain. The repository currently contains 29 eval prompts across the four skills. Ten selected scenarios have paired baseline/skill spot checks: six earlier synthetic cases and four source-grounded public engineering cases. The public-case results are recorded in [`public-case-evaluation.md`](public-case-evaluation.md); the earlier comparisons are summarized above and in the metric evaluation note. Five earlier pressure scenarios remain candidate regression cases without a matched behavior run, and most prompt cases have not been paired. Do not describe this qualitative set as broad effectiveness evidence.

## Additional skill-guided behavior check

On 2026-09-24, separate runs used each skill for one missing-data case, one conflicting-information case, and one normal case. Rubric scores were planning 10/10, 10/10, 9/10; review 10/10 on all three; reporting 10/10 on all three; and metric decision 10/10 on all three. The 9/10 planning answer stated that a checkout owner was responsible for the outcome even though the prompt had not assigned that role. This was a concrete evidence-boundary failure, not a general weakness in the skill.

The planning instructions now distinguish confirmed responsibility from suggested assignment, and the eval suite includes an explicit unconfirmed-owner boundary case. The same normal case and the new boundary case were rerun with the updated skill; both scored 10/10. These are single-run rubric judgments by the repository evaluator, not blind or no-skill comparisons. They show that the observed defect was corrected on these prompts; they do not establish broad effectiveness.

## Publication guidance

Describe this as a method-packaging and evaluation project. Suitable claims: four independent skills; examples and pressure scenarios; explicit treatment of source, estimate, inference and unknown states; Codex discovery/install smoke-tested. Avoid claims of measured productivity gains, universal model compatibility, or proven decision-quality improvement. Claude Code behavior has not yet been directly tested.
