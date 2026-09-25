# Skill 仓库结构设计

日期：2026-09-24

## 目标

将三个独立技能整理成易发现、易单独安装、易维护的集合型仓库。结构参考 `evidence-based-person-analysis` 的 README、规范分层、评测和校验工具；由于本仓库包含多项独立技能，采用社区多技能仓库常见的 `skills/<name>/SKILL.md`，不在根目录增加重复的 router skill。

## 设计依据

- `evidence-based-person-analysis` 使用根 README 说明入口和边界，将主技能、模块、参考资料、evals 与结构校验工具分层，并声明验证工具不能证明领域有效性。
- 本仓库现有三项技能有各自的名称、参考资料、模板、脚本或 evals，应保持独立安装。
- 跨技能规则使用一个规范来源；单项技能的知识与模板留在技能包内。
- 汇报材料技能声明 `Proprietary`，另两项未声明许可证，因此不添加全仓统一许可证。

## 目录结构

```text
.gitignore
AGENTS.md
README.md
agent/
  README.md
  decision-and-review-contract.md
  adr/0001-collection-layout.md
skills/
  tech-planning/
    SKILL.md
    references/
    evals/
  tech-review/
    SKILL.md
    references/
    evals/
  eng-reporting/
    SKILL.md
    references/
    assets/
    scripts/
docs/
  research/github-similar-skill-repositories.md
  superpowers/specs/
  superpowers/plans/
scripts/validate_repo.py
```

## 规范与职责

- 根 `README.md` 提供技能目录、任务匹配、单独安装、校验方法和许可证说明。
- 根 `AGENTS.md` 定义仓库维护约定和文件归属。
- `agent/` 是跨技能共用规则的唯一来源；每个 skill 负责执行适用部分，并保留自身参考文件。
- `skills/<name>/` 是可单独安装的包，目录名必须与 `SKILL.md` frontmatter 中的 `name` 相同。
- 每项技能当前已有的 references、assets、evals 和 scripts 随技能保留。
- `docs/research/` 保存社区对标研究；`docs/superpowers/` 保存本仓库的结构设计与实施记录。
- `scripts/validate_repo.py` 只做结构、name、现有 eval JSON 和 Markdown 本地链接的静态检查；它不判断技能输出是否有效。

## 本轮范围

1. 初始化本地 Git 元数据和忽略规则，不配置远端、不推送、不发布。
2. 将技能目录移动到 `skills/`，保持 skill 名称和内容不变。
3. 将社区研究报告归入 `docs/research/`。
4. 增加仓库 README、AGENTS、共用证据/评审契约、结构 ADR 和轻量验证脚本。
5. 本次目录结构调整不更改三个 skill 的正文和既有 eval，不增加新技能，不新增根级 router skill，不解决许可证授权。后续功能和方法论扩展由单独设计记录维护。

## 后续 P0/P1 工作

1. 按 `agent/decision-and-review-contract.md` 调整三个 skill：未知数据提供计算口径、只给证据支持的结论、记录来源与估算状态、评审结论允许没有阻塞项，并保持评审与改写边界。
2. 为每项 skill 增加缺失数据、冲突信息、正常/无阻塞方案等 eval 案例，并用事实克制、任务匹配、可执行性、格式、语气五项量规复核。
3. 单独设计技术方案评审和规划拆解 skill；新增前确认它们不与现有 Tech Lead 评审重复。

## 验收结果

- 三项 skill 及其所有当前文件均位于 `skills/` 下，入口名与目录名一致。
- 根 README 能解释技能用途并提供安装/校验入口。
- 结构校验命令 `python3 scripts/validate_repo.py` 通过。
- Git 仓库为本地初始化状态；没有配置远端或创建提交。
- 没有添加全仓许可证或修改原技能内容。
