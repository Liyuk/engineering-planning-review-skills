# Public Case Evaluation

Date: 2026-09-24

This note records one matched run of the four skills on public-source cases, the independent rubric review, and targeted regression runs after fixing two observed failures. The source notes and exact reproducible prompts are in [`docs/research/public-case-materials.md`](../research/public-case-materials.md) and each skill's `evals/evals.json`.

## Method

- Four first-party sources: [GitHub's gh-ost announcement](https://github.blog/news-insights/company-news/gh-ost-github-s-online-migration-tool-for-mysql/), [GitLab's MR Rate discussion](https://about.gitlab.com/blog/measuring-engineering-productivity-at-gitlab/), [GitHub's schema migration workflow](https://github.blog/enterprise-software/automation/automating-mysql-schema-migrations-with-github-actions-and-more/), and [Google SRE's satellite incident postmortem](https://sre.google/workbook/postmortem-culture/).
- Each exact prompt includes the relevant paraphrased public facts and source URL. Baseline and skill runs used the same supplied information and did not browse during generation; this avoids giving one condition extra evidence.
- Separate agents produced baseline and skill answers. An independent evaluator scored the paired answers with [`agent/eval-rubric.md`](../../agent/eval-rubric.md): fact restraint, task match, actionability, format, and tone, each 0–2. The scoring was independent but not blind to condition.
- One response per condition and case is exploratory. It is not a controlled study and cannot show general or causal effectiveness.

## First run

| Case | No-skill baseline | Skill | Observation |
| --- | ---: | ---: | --- |
| MySQL migration decision | 10/10 | 9/10 | Both bounded GitHub's 2016 account and proposed a low-risk test. The skill answer was too long for the request for a short brief (format 1/2). |
| MR Rate and individual targets | 10/10 | 10/10 | Both rejected the inference from aggregate MR Rate to individual productivity and called for definition, cohort, quality, and delivery checks. |
| Production migration review | 10/10 | 10/10 | Both found the explicit missing rollout, pause/threshold, concurrency, owner, and post-migration controls. The skill response made evidence, impact, and actions easier to scan. |
| Satellite incident leadership update | 8/10 | 7/10 | The skill response exceeded the 130-word limit (131 counted words) and overstated that mitigation “stopped the active impact.” The baseline kept under the limit but did not name the concrete mitigation action. |
| **Total** | **38/40** | **36/40** | The first run exposed real regressions despite strong scores. |

## Changes and targeted regression

The initial outputs provided failing examples before editing the skills:

- `tech-planning` now says a requested short brief should include only the decision, decision-changing unknowns, main option differences, and one reversible next step. It should not expand the full reference method into the answer.
- `eng-reporting` now requires checking hard word/character limits with margin, avoiding unsupported source details, and distinguishing a recorded mitigation action from full recovery or proof that recurrence was prevented.

The same two prompts were rerun against the updated skills. The evaluator scored the updated planning answer **10/10**, matching the 10/10 baseline. It scored the updated reporting answer **10/10**, versus the 8/10 baseline: the final body was 111 English words, named traffic rerouting to core clusters as the reported mitigation, and did not claim the impact had fully stopped.

| Targeted regression | Baseline | Initial skill | Updated skill | Result |
| --- | ---: | ---: | ---: | --- |
| Short gh-ost decision brief | 10/10 | 9/10 | 10/10 | Verbosity failure corrected; now matches baseline. |
| Satellite incident update | 8/10 | 7/10 | 10/10 | Word-limit and mitigation-claim failures corrected on this prompt. |

The metric and review skill files were unchanged; their first-run paired results remain 10/10 each. Combining those unchanged outputs with the two targeted reruns gives a latest per-case total of 40/40 for skills versus 38/40 for baseline, but it is not a single synchronized final batch. Treat this as a regression result on four fixed prompts, not proof that the skills generally outperform the base model.

## What the test says about skill value

The strongest visible value here is consistent structure and more explicit decision gates. In three first-run cases, the baseline already scored 10/10; skills did not raise the score. In the reporting case, the first skill answer performed worse, and the prompt exposed a word-count and evidence-boundary failure. The resulting edits fixed that case in one targeted rerun. More varied prompts, repeated runs, other models, and external scoring would be needed before making broader effectiveness claims.

No further skill changes are justified by these four cases alone. Continue adding cases for missing data, conflicting sources, ordinary successful work, hard length constraints, and evidence that rules out a tempting conclusion. Re-run a held-out prompt set after future instruction changes to reduce overfitting to these examples.
