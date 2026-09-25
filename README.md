# Engineering Planning & Review Skills

面向中文技术管理场景的一组可独立安装、组合使用的 Agent Skills，覆盖技术规划、技术方案评审和管理材料整理。

## Skills

| Skill | 适用场景 | 入口 |
| --- | --- | --- |
| 技术规划 `$tech-planning` | 年度/双月规划、投资取舍、依赖和架构图 | [`skills/tech-planning/SKILL.md`](skills/tech-planning/SKILL.md) |
| 技术评审 `$tech-review` | 评审已有方案、Benchmark、AI 落地蓝图和架构决策 | [`skills/tech-review/SKILL.md`](skills/tech-review/SKILL.md) |
| 管理材料 `$eng-reporting` | 将项目证据整理为汇报、总结、复盘、述职或晋升材料 | [`skills/eng-reporting/SKILL.md`](skills/eng-reporting/SKILL.md) |
| 指标决策 `$metric-decision` | 定义/核验指标、调查变化、将证据转为可验证行动 | [`skills/metric-decision/SKILL.md`](skills/metric-decision/SKILL.md) |

每个 skill 都是独立目录，可单独复制到 Agent 的 skills 搜索路径。组合使用时，建议按“规划 → 评审 → 基于确认事实整理材料”的顺序；它们不要求一起安装。

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

仓库发布到 GitHub 后，也可用 [skills CLI](https://github.com/vercel-labs/skills) 单独安装，不必安装整个集合：

```sh
npx skills add OWNER/REPO --skill metric-decision --agent codex --global
```

`OWNER/REPO` 需要替换为实际公开仓库地址。尚未发布前，可从仓库根目录运行 `npx skills add ./skills/metric-decision --list` 检查单项技能能否被发现；要使用它则复制该目录到 `~/.codex/skills/`，再调用 `$metric-decision`。

## 面向社区的采用路径

优先用一个具体问题介绍它：**指标变了，先判断变化是否可信，再决定做什么。**目标读者是需要在产品、工程与数据口径之间作决策的技术负责人、产品负责人和分析工程师。展示“埋点迁移与指标下降同时发生”的完整例子，比泛称“数据分析助手”更能体现它解决的工作环节。

公开使用前，先确认各技能的授权范围并设置清晰的许可证；当前仓库尚无公开地址，且 [`eng-reporting`](skills/eng-reporting/SKILL.md) 标记为 Proprietary，因此不能把整仓作为开放许可内容发布。确定可公开的仓库和许可后，社区用户可用上面的命令只安装 `metric-decision`。Skills CLI 文档说明，排行榜基于匿名聚合安装次数，公开仓库经用户实际安装后会自动计入；安装可见度依赖有人试用，README 示例、可复用评测用例和清楚的边界说明才是当前可落实的采用材料。[Skills CLI FAQ](https://www.skills.sh/docs/faq)

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

该工具检查技能目录和 frontmatter 名称、Markdown 本地链接，以及 `evals/evals.json` 的 JSON 格式。每项技能包含缺数据、冲突信息和正常方案用例；`metric-decision` 另有“数据已核实但因果未明”的边界用例。人工复核时使用 [`agent/eval-rubric.md`](agent/eval-rubric.md) 的事实克制、任务匹配、可执行性、格式和语气五项量规及判分示例。结构校验不等于行为评测。

## 许可证

当前没有全仓统一许可证。汇报材料技能声明为 `Proprietary`；其余三项技能没有声明许可证。安装技术上可行不等于获得再分发许可，请在确认每项技能的授权范围前，不要将其视为可自由再发布的内容。

因此，当前安装说明用于本地试用和发现验证，不代表仓库已获准公开再分发。面向社区发布前，需要明确新技能和原有各技能的许可证边界；尤其不能把声明为 `Proprietary` 的材料默认打包进开放许可集合。

## 研究

- [GitHub 社区相似 Skill 项目调研](docs/research/github-similar-skill-repositories.md)
- [个人写作方法到技能的映射](docs/methodology/writing-to-skills-map.md)
- [`metric-decision` 行为验收记录](docs/methodology/metric-decision-evaluation.md)
- [四项技能用途、边界和价值评审](docs/methodology/skills-portfolio-review.md)
- [可直接用于博客的项目模块](docs/blog/project-module.md)
