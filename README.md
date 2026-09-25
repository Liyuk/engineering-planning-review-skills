# Engineering Decision Skills

面向中文技术管理场景的一组可独立安装、按需组合的 Agent Skills，覆盖技术规划、技术评审、指标决策和工程汇报。仓库按 Agent Skills 的目录格式组织：每项能力以 `SKILL.md` 为入口，可带 references、assets 和脚本；它们不是必须编译或运行的 Node.js 库。[OpenAI Skills 文档](https://developers.openai.com/api/docs/guides/tools-skills) · [Vercel Skills CLI](https://github.com/vercel-labs/skills)

## Skills

| Skill | 适用场景 | 入口 |
| --- | --- | --- |
| 技术规划 `$tech-planning` | 年度/双月规划、投资取舍、依赖和架构图 | [`skills/tech-planning/SKILL.md`](skills/tech-planning/SKILL.md) |
| 技术评审 `$tech-review` | 评审已有方案、Benchmark、AI 落地蓝图和架构决策 | [`skills/tech-review/SKILL.md`](skills/tech-review/SKILL.md) |
| 管理材料 `$eng-reporting` | 将项目证据整理为汇报、总结、复盘、述职或晋升材料 | [`skills/eng-reporting/SKILL.md`](skills/eng-reporting/SKILL.md) |
| 指标决策 `$metric-decision` | 定义/核验指标、调查变化、将证据转为可验证行动 | [`skills/metric-decision/SKILL.md`](skills/metric-decision/SKILL.md) |

每个 skill 都是独立目录，可单独复制到 Agent 的 skills 搜索路径。按当前任务调用即可；组合使用时，建议按“规划 → 评审 → 基于确认事实整理材料”流转，但它们不要求一起安装。

### 推荐先试：`$metric-decision`

**从用户任务定义指标，先确认数据可信，再把有边界的结论变成可验证行动。**适合指标定义、埋点迁移后的数据异常、产品/工程指标口径冲突，以及指标变化后的原因核验。

它覆盖技术规划之前的“这个变化是否可信、值不值得行动”，以及变更之后的“怎样验证是否有效”。Matt Pocock 的 skills 更专注软件交付流程；Han 的 iterative plan review 更专注评审和迭代已有计划。`metric-decision` 补的是决策所需的测量和证据闭环，不替代实现或计划评审。

快速试用：

```text
$metric-decision
保存成功率从 98% 降到 93%，但同期迁移了埋点。请先判断数据是否可比，再给我今天能向老板同步的结论和下一步。
```

这组数值是演示用的用户输入，不代表任何生产系统结果。完整示例见 [`skills/metric-decision/examples/instrumentation-change.md`](skills/metric-decision/examples/instrumentation-change.md)。

## 安装与使用

将需要的技能目录复制到 Agent 支持的 skills 目录。例如，在 Codex 的个人技能目录中：

```sh
mkdir -p ~/.codex/skills
cp -R skills/tech-planning ~/.codex/skills/
```

将需要的技能目录复制到 `~/.codex/skills/` 后，可在 Codex 中用表格里的 `$技能名` 显式调用；也可以直接描述任务，由模型根据技能名称和描述判断是否使用。

也可用 npm 提供的 [skills CLI](https://github.com/vercel-labs/skills) 从 Git 仓库安装单项 skill；这里使用 npm 执行的是通用安装工具，**不需要把本项目发布成 npm 包**：

```sh
npx skills add OWNER/REPO --skill metric-decision --agent codex --global
```

本仓库远端为私有仓库，安装者需要有 GitHub 访问权限；本地使用时也可以直接复制所需目录到 `~/.codex/skills/`，再调用 `$metric-decision`。发布给社区时，应先准备可公开且许可明确的仓库，再使用公开仓库地址。只在增加需要 npm 管理的可执行 CLI、共享运行时或依赖/版本 API 时，才考虑发布 npm 包。

## 面向社区的采用路径

优先用一个具体问题介绍它：**指标变了，先判断变化是否可信，再决定做什么。**目标读者是需要在产品、工程与数据口径之间作决策的技术负责人、产品负责人和分析工程师。展示“埋点迁移与指标下降同时发生”的完整例子，比泛称“数据分析助手”更能体现它解决的工作环节。

当前 GitHub 远端 [`Liyuk/engineering-planning-review-skills`](https://github.com/Liyuk/engineering-planning-review-skills) 为私有仓库，尚未向社区公开。公开使用前，需要先确认各技能的授权范围并设置清晰的许可证；[`eng-reporting`](skills/eng-reporting/SKILL.md) 标记为 Proprietary，其余三个技能也未声明许可证，因此不能把整仓作为开放许可内容发布。Skills CLI 的安装方式是从 Git 仓库选取技能，并非要求每个仓库发布 npm 包；社区分发前仍需准备权限可访问、许可明确的公开来源。[Skills CLI 文档](https://github.com/vercel-labs/skills) · [Skills 目录格式说明](https://developers.openai.com/plugins/build/skills)

目前只在 Codex 上完成了发现与复制安装烟雾检查。CLI 支持多种 agent，但该技能尚未逐一验证其他 agent 的触发和输出行为；发布时应明确这个验证范围。[Skills CLI README](https://github.com/vercel-labs/skills/blob/main/README.md)

## 仓库结构

```text
agent/                       跨技能共用的原则与输出约定
skills/                      可单独安装的技能包
  tech-planning/              技术规划
  tech-review/                技术评审
  eng-reporting/              管理材料整理
  metric-decision/            指标与决策证据分析
docs/research/                GitHub 社区对标研究
docs/methodology/             原文方法映射、技能评审与行为验收
docs/blog/                    可复用的博客项目介绍草稿
docs/superpowers/             本仓库结构规格与实施计划
scripts/                      结构及引用校验工具
```

本仓库有多个独立 skill，因此不在根目录放一个会与它们职责重叠的 `SKILL.md`。根 README 负责发现与导航；安装入口仍是各技能目录中的 `SKILL.md`。

## 开发与校验

调整技能或移动目录后，在仓库根目录运行：

```sh
python3 scripts/validate_repo.py
```

该工具检查技能目录和 frontmatter 名称、Markdown 本地链接，以及 `evals/evals.json` 的 JSON 格式。四项技能当前共有 28 个 prompt，用例覆盖缺数据、冲突信息、正常任务、决策压力和四个公开案例。四个公开案例做过无技能/启用技能配对评分；两项针对失败的回归在修改后重跑。评测方法、分项分数和限制见 [`docs/methodology/public-case-evaluation.md`](docs/methodology/public-case-evaluation.md)。人工复核使用 [`agent/eval-rubric.md`](agent/eval-rubric.md) 的事实克制、任务匹配、可执行性、格式和语气五项量规。结构校验不等于行为评测。

## 许可证

当前没有全仓统一许可证。汇报材料技能声明为 `Proprietary`；其余三项技能没有声明许可证。安装技术上可行不等于获得再分发许可，请在确认每项技能的授权范围前，不要将其视为可自由再发布的内容。

因此，当前安装说明用于本地试用和发现验证，不代表仓库已获准公开再分发。面向社区发布前，需要明确新技能和原有各技能的许可证边界；尤其不能把声明为 `Proprietary` 的材料默认打包进开放许可集合。

## npm 发布判断

本项目目前是 Markdown 工作流和配套参考文件，直接按 skill 目录安装即可，不需要创建 `package.json` 或发布 npm 包。npm 在这里仅用于运行 `npx skills` 安装 CLI。只有当项目新增独立可执行工具、需要依赖管理/语义化版本 API，或需要被其他 Node.js 程序作为库调用时，才值得评估 npm 包；若只是面向 Agent 分发 skill，先发布许可证明确的 GitHub 仓库并用 Skills CLI 安装更合适。

## 研究

- [GitHub 社区相似 Skill 项目调研](docs/research/github-similar-skill-repositories.md)
- [公开工程案例及四项技能评测](docs/research/public-case-materials.md) · [评测结果](docs/methodology/public-case-evaluation.md)
- [个人写作方法到技能的映射](docs/methodology/writing-to-skills-map.md)
- [`metric-decision` 行为验收记录](docs/methodology/metric-decision-evaluation.md)
- [四项技能用途、边界和价值评审](docs/methodology/skills-portfolio-review.md)
- [可直接用于博客的项目模块](docs/blog/project-module.md)
