# GitHub 社区相似 Skill 项目调研

调研日期：2026-09-24
范围：GitHub 一手仓库、仓库内说明与 Skill 文件。这里只比较公开描述的能力与工程组织方式，不推断项目作者的实际使用效果。

## 结论摘要

用户提到的 “matt/skill” 最可能是 [mattpocock/skills](https://github.com/mattpocock/skills)：仓库自称 “Skills For Real Engineers”，明确强调小型、可改、可组合，并提供 Claude 插件和 `skills` 安装器两种分发方式。仓库的核心覆盖面是从需求澄清、领域语言、规格、任务拆分，到 TDD、实现和代码评审的日常软件交付流程。

当前仓库和 Matt Pocock 的项目不是同一种定位。现有内容更聚焦在**中文技术管理规划与评审**：中长期技术规划及架构图、技术负责人视角的方案/汇报评审、原始材料到管理/晋升叙事的整理。它的潜在独特性是把“战略规划—向上表达—技术方案把关”放在一套面向中国工程管理语境的技能包里；GitHub 上查到的相邻项目多数聚焦编码交付、实施计划可执行性或自动化的计划迭代评审。

建议把这个仓库做成可独立安装和维护的**规划与技术评审 Skill 集**，而不是复制通用 coding-agent 工作流。最值得补齐的差距是：输出证据和数据来源纪律、方案/计划可执行性检查、可复现的质量评测、技能之间的路由与共享事实模型、清晰的安装/许可证/变更说明，以及把人格化“毒舌”收敛成可校准的专业评审标准。

## 对标项目

| 项目 | 主要流程与产物 | 工程能力与维护方式 | 对本项目的启发 |
| --- | --- | --- | --- |
| [mattpocock/skills](https://github.com/mattpocock/skills) | 以组合式日常工程技能串联需求澄清、共享领域术语、规格、tracer-bullet tickets、实现/TDD、代码评审；`to-tickets` 会显式表达任务依赖，并经用户确认后发布到本地文件或 issue tracker。 | 同时提供 Claude Code 插件和 `skills` 安装器；前者托管更新、后者把文件拷入项目由使用者自行更新；项目有顶层 README、文档、变更记录、工作流和技能分类，并区分 user-invoked 与 model-invoked。 | 借鉴“技能小而可组合”、显式定位/安装说明和前置配置；可以在用户确认之后，将规划结论拆为可执行、带依赖的工单。不要丢掉自身的管理规划定位。 |
| [obra/superpowers](https://github.com/obra/superpowers) | 通用软件开发方法论，强调先澄清/设计、编写计划、按计划实施、TDD、调试与代码审查的流程约束；每项能力由具体 Skill 承载。 | 仓库根目录按多种 agent/plugin 入口组织，包含 hooks、scripts、tests、docs 与 skills，说明其不只是提示词集合，而是可分发、可验证的工作流框架。 | 可以借鉴流程门和自动化回归；本项目可以把“规划草案→评审→修订→管理摘要/落地计划”定义成清楚的交接契约。 |
| [FareedKhan-dev/claude-code-staff-engineer](https://github.com/FareedKhan-dev/claude-code-staff-engineer) | 面向 Claude Code 的多代理 Staff Engineer 工作流：写计划并让新子代理按规格审查完整性、规格覆盖、任务拆分和可执行性；另外分开做规格审查、代码审查、TDD、调试和完成验证。 | 通过明确角色、审查类别、严重问题校准和验证关口组织成“团队”工作流；计划审查的结果是 `Approved` 或 `Issues Found`，问题关联到任务。 | 为技术方案/规划评审增加“针对原始目标逐项追溯”的审查表，并区分阻塞问题与文字偏好，防止 reviewer 只输出尖锐但不可操作的意见。 |
| [testdouble/han](https://github.com/testdouble/han) 的 [iterative-plan-review](https://github.com/testdouble/han/blob/main/han-planning/skills/iterative-plan-review/SKILL.md) | 专门打磨已有计划：多轮以代码库为依据检查并原地修改，同时将每轮 finding 和版本记入互相引用的伴随文件；另有从零写计划的 skill，职责边界明确。 | 长流程会记账、留痕、引用配置和项目上下文；将“评审已有计划”“新建计划”“配对逐轮看结果”等使用模式拆开。 | 借鉴计划评审的证据链与逐轮记录。若要审架构方案，也可保留原文、问题、证据、决策和改写的对应关系，而不是只给一份最终结论。 |
| [dachev/plan-review](https://github.com/dachev/plan-review) | 在 Claude Code 计划提交审批时提供独立评审轮次，支持选择 reviewer/model、逐项调查或驳回意见、修订并继续，直到阻塞项解决或达到用户设定的流程终点。 | 把每个版本与 reviewer 消息保存在 Markdown；支持暂停/恢复、最大轮数、配置和多 reviewer CLI；自动提示出错时 fail-open。 | 可借鉴可审计评审记录、有限轮次、逐项采纳/驳回机制和失败时不阻塞用户。适合日后把本项目的人工评审改造成可选的迭代审查。 |
| [Pricing-Logic/Claude-et-Codex](https://github.com/Pricing-Logic/Claude-et-Codex) | 在 Claude 制定实现方案期间调用 Codex CLI 做交叉评审；Codex 可看到项目代码，输出架构、边界情况、简化度、文件位置的结构化判断。 | 单一 skill 文件外加执行脚本/依赖与安装说明；利用不同模型/agent 做第二意见。 | 对高影响方案，可把“独立架构审阅”设成可选能力，但应先把输入、权限、成本和意见冲突处理说清楚；当前仓库不必默认依赖第二个 CLI。 |

## 这个项目现在已有的差异点

以下判断来自本地仓库现有文件，而非外部项目宣传：

1. **管理层级更高。** `skills/tech-planning/SKILL.md` 面向年度/双月规划、业务约束、投资取舍和路线图，更接近技术战略和资源决策。
2. **评审目标贴近技术管理者决策。** `skills/tech-review/SKILL.md` 面向已有方案、Benchmark、AI 落地和架构评审，输出证据、影响、建议动作及有边界的结论。
3. **覆盖管理材料的上下游转换。** `skills/eng-reporting/SKILL.md` 处理会议纪要、项目总结、绩效/述职/晋升素材，并为不同读者组织内容。
4. **新增决策级度量闭环。** `skills/metric-decision/SKILL.md` 从用户任务和指标口径开始，先验证数据质量，再界定原因，最后把行动和复查连起来；它处于工程投资决策的证据环节，不重复编码流程或已有计划评审。
5. **以中文和中国大厂管理表达作为默认场景。** 五三规划、向上汇报、ROI 账本、P0-P3、跨团队兜底等概念共同构成鲜明语境。这个定位有辨识度，但要避免把语境表达误当成事实依据或质量标准。
6. **有质量验证材料。** 当前四项 skill 均有 `evals/evals.json`，覆盖缺数据、冲突信息和正常方案，并共用事实克制、任务匹配、可执行性、格式、语气五项评分量规。

## 可补充的工程环节、观点与能力

### P0：提升可信度和可执行性

- **加入证据账本。** 每个数字标为“用户提供 / 一手公开来源 / 估算 / 待确认”，记录口径、时间范围、公式与来源；没有数据时给指标方向和待补字段，不强迫编出数字。规划 skill 当前要求量化 DoD、粗算 ROI，同时又禁止造数，可以将这两条落成明确的数据协议。
- **把评审变成可处置的问题单。** 每条问题包含严重度、影响、证据/原文位置、需要的决策、建议动作；分别标注阻塞项、建议项和可接受风险。借鉴 staff-engineer 仓库按规格覆盖和可执行性审计划、`plan-review` 的逐条调查/驳回流程。
- **补齐决策与依赖闭环。** 方案/规划至少输出目标、当前基线、目标值、假设、备选方案、成本/人员、依赖团队、风险、回滚/Plan B、owner、里程碑和决策请求；未确认字段明确显示 TBD，不让角色人设把缺口掩盖掉。
- **调整“毒舌”边界。** 保留挑战假设的力度，删除要求辱骂、夸张或先设定“致命漏洞/核武器”的硬性输出要求。评审应当按证据和风险判断，不应因为角色提示而必须凑出两处问题；问题不足时允许给出通过结论。
- **取消对隐藏思维过程的输出要求。** 现有两个 skill 要求回复前生成 `<evaluation_process>`。改为内部按检查表分析，用户可见内容只包含结论、证据、假设、问题和建议，提升稳定性与可读性。

### P1：组成能串联的 Skill 仓库

- 为当前三类能力明确分工和路由：`规划（提出方向与资源选择）→方案评审（找证据缺口、风险和决策）→汇报材料（按受众重组已确认事实）`。建立共享术语和事实状态，避免规划稿里的估计在汇报稿里变成事实。
- 增加“技术方案/架构评审”或“规划可执行性审查”独立 skill：检查需求到技术动作追溯、系统边界/数据迁移/兼容性/安全/可观测性/测试与运维/回滚、依赖与路径、阶段验收。初始调研时的 `tech-lead-reviewer`（现名 `tech-review`）能谈架构，但输出协议主要是高管评审和汇报重塑。
- 加入轻量级任务拆分能力：将已定方向转换成阶段、里程碑、依赖、验收条件和可以交给工程师的 tracer-bullet 工单；将“战略方案”与“实施票据”分层，不要把所有规划都压成一个清单。
- 设置共用产物模板：一页决策摘要、技术规划、架构评审报告、ROI/成本表、风险登记册、跨团队依赖表、管理汇报版。模板标清输入字段及不可编造字段。

### P2：把 Skill 仓库做成可分发、可回归的工程项目

- **仓库入口：** README 说明适用对象、典型触发语句、三项技能关系、安装方式、示例输入/输出、已知限制、许可证和贡献方式；为中文首发定位，后续可增加英文 README 或双语元数据。Matt 仓库说明了 Claude 插件与可编辑安装两种分发哲学，可以按维护能力选择其一先落地。
- **格式与兼容：** 每个技能采用标准的独立目录和 `SKILL.md`，提供 frontmatter 的 `name`、描述、适用场景、依赖/能力声明；把模板/参考资料通过相对路径链接，并检查路径正确。按目标 agent 兼容范围选择 Agent Skills 规范作为基础。
- **可重复评测：** 扩展现有 evals，包含模糊目标、缺失数据、冲突指标、多团队依赖、方案过度设计、无竞品数据、坏例子等案例；为事实准确性、关键字段覆盖、问题可操作性、语气校准、模板格式定义评分量规和拒绝标准。保存黄金输出或判分规则，PR 改 Skill 时做人工回归。
- **维护约定：** 记录版本/变更，规定更新参考方法论时一并更新 eval；将示例中数据明确虚构，防止被模型当成可引用事实；提供变更日志和兼容性说明。Matt 仓库用文档/changesets/工作流维护并把 skills 和 user docs 对齐，可作为维护模型参考。
- **有条件的自动化：** 只在存在稳定评测脚本后增加 lint/路径检查/格式校验 CI；跨模型评分或 CLI reviewer 作为可选项，保留可复核的人工评测结果。不要仅凭高分或“模拟大厂经验”声称能提升规划质量。

## 推荐仓库结构

```text
README.md
LICENSE
CHANGELOG.md
skills/
  tech-planning-cn/
    SKILL.md
    references/
    assets/
    evals/
  tech-solution-review-cn/
    SKILL.md
    references/
    assets/
    evals/
  engineering-lead-review-cn/
    SKILL.md
    references/
    assets/
    evals/
  engineering-reporting-cn/
    SKILL.md
    references/
    assets/
    scripts/
docs/
  workflow.md
  output-contracts.md
```

推荐顺序：先写清仓库定位、许可和安装入口；然后修订现有两个评审 skill 的事实/语气协议；再补独立方案评审和依赖/任务拆分；最后将现有 evals 扩成回归案例，并通过 README 里的真实使用样例验证新用户能单独安装和触发每项 skill。

## 后续设计状态

这份报告记录社区对标与初始差距。之后已将技能目录缩短为 `$tech-planning`、`$tech-review`、`$eng-reporting`，并新增 `$metric-decision`。当前文章到技能的方法映射、边界和评测要求见 [`docs/methodology/writing-to-skills-map.md`](../methodology/writing-to-skills-map.md) 和 [`docs/superpowers/specs/2026-09-24-methodology-derived-skills-design.md`](../superpowers/specs/2026-09-24-methodology-derived-skills-design.md)。

## 一手来源

- Matt Pocock skills 主 README 与流程/分发说明：[README.md](https://github.com/mattpocock/skills)、[to-tickets/SKILL.md](https://github.com/mattpocock/skills/blob/main/skills/engineering/to-tickets/SKILL.md)、[grill-with-docs/SKILL.md](https://github.com/mattpocock/skills/blob/main/skills/engineering/grill-with-docs/SKILL.md)
- Superpowers 方法论和仓库结构：[README.md](https://github.com/obra/superpowers)、[writing-plans/SKILL.md](https://github.com/obra/superpowers/blob/main/skills/writing-plans/SKILL.md)
- Staff engineer 工作流：[README.md](https://github.com/FareedKhan-dev/claude-code-staff-engineer)
- Han 计划评审流程：[iterative-plan-review 文档](https://github.com/testdouble/han/blob/main/han-planning/docs/skills/iterative-plan-review.md)、[iterative-plan-review/SKILL.md](https://github.com/testdouble/han/blob/main/han-planning/skills/iterative-plan-review/SKILL.md)
- 自动化计划审查：[dachev/plan-review](https://github.com/dachev/plan-review)
- 跨 agent 方案审阅：[Pricing-Logic/Claude-et-Codex](https://github.com/Pricing-Logic/Claude-et-Codex)
- Skill 格式规范：[Agent Skills specification](https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx)
