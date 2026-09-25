# Writing Methods to Skills Map

This map records which methods from `liyuk.github.io` inform the skills collection. Skills distill reusable judgment methods; they do not copy full articles or force every article's structure into every answer.

## Shared judgment spine

Across planning, measurement, review, and reporting, preserve this sequence when relevant: define the outcome and decision → establish evidence and its status → identify constraints and alternatives → compare costs and consequences → assign ownership and decision rights → set verification or invalidation conditions → revisit the decision when evidence changes. This is a judgment order, not a mandatory document outline.

The shared evidence labels and review contract live in [`agent/decision-and-review-contract.md`](../../agent/decision-and-review-contract.md); evaluation dimensions live in [`agent/eval-rubric.md`](../../agent/eval-rubric.md).

## Source-to-skill mapping

| Writing source in `liyuk.github.io` | Method distilled | Skill destination | Boundary |
| --- | --- | --- | --- |
| `src/content/writing/2025/11/technical-planning-business-and-competitive-analysis/zh.md` — 技术规划中的业务与竞争分析 | Business context; constraint → consequence → evidence; capacity and capability gaps; portfolio choices; defer/validate/abandon; invalidation conditions; roadmap certainty by horizon; ownership and operating cadence | `tech-planning` | Creates a direction and investment decision; does not replace implementation ticket planning or independent review. |
| `src/content/writing/2021/03/define-the-measurement-before-arguing-about-metrics/zh.md` — 指标争论之前，先定义测量对象; `src/content/writing/2021/05/periodic-metrics-and-retrospectives/zh.md` — 周期统计与复盘 | User task → state/event model → metric definition → data validity → bounded diagnosis → action hypothesis → same-definition follow-up | `metric-decision` | Defines and investigates measures; does not assert causality from timing/correlation or turn a dashboard into a decision by itself. |
| `src/content/writing/2026/08/management-retrospective/zh.md` — 管理复盘：从执行到系统的八个判断 | Problem judgment, boundaries, alignment, context handoffs, closed loops, capacity, team growth, retrospective | `eng-reporting` initially; consider a separate skill only if it proves to have a distinct invocation and output | Analyze system causes when requested; do not automatically convert every status report into a management audit. |
| `src/content/writing/2026/08/structured-thinking-practice/zh.md` — 结构化思维实践; `src/content/writing/2023/03/information-sync-for-decisions/zh.md` — 信息同步不是抄送 | Reader's decision, evidence versus assumption, status/blocker/decision/next step; resolve disagreement around shared goals, facts, and decision rights | `tech-review`, `eng-reporting` | Structure is selected for the task; do not force every answer into STAR, MECE, or a fixed executive template. |
| `src/content/writing/2023/03/engineering-standards-without-bureaucracy/zh.md` — 工程规范怎样既减少返工，也不制造官僚流程 | Start from recurring rework; minimum delivery loop; owners, acceptance, release/rollback, post-release signal | `tech-planning`, `tech-review` | Add operating controls in proportion to risk and observed failure. |
| `src/content/writing/2026/08/ai-productivity-complex-systems/zh.md` — AI 不会自动带来生产力 | Distinguish local speed from system/product value; inspect bottleneck movement, data/system boundaries, failure ownership, resilience, cost and attribution | Candidate future skill | Keep as a specialized mode until enough cases show it needs a separate command and evaluation set. |

## Invocation names

Use short, task-shaped names that can be typed explicitly in Codex:

| Command | Use for |
| --- | --- |
| `$tech-planning` | Create or revise a technical direction, investment portfolio, or roadmap. |
| `$tech-review` | Review an existing proposal or decision. |
| `$eng-reporting` | Turn source material into an audience-specific management artifact. |
| `$metric-decision` | Define or investigate measures and connect evidence to action. |

The skills remain eligible for normal automatic discovery. Explicit names improve manual invocation; they do not make the long-term differentiation by themselves. The differentiated content is the evidence-aware engineering investment and organizational decision method represented by the source mapping above.
