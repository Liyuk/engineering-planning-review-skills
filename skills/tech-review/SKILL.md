---
name: tech-review
description: Use when reviewing an existing technical proposal, architecture, benchmark, AI adoption plan, or decision brief for evidence, trade-offs, delivery risk, and decision readiness. Use tech-planning to create a new roadmap.
---

# 技术方案评审

评审的目标是帮助用户作出更可靠的决定，而不是证明评审者更犀利。只报告有材料依据、且会影响决策或交付的问题；评审与改写分开，除非用户明确要求两者。

## 工作方式

1. 确认要评审的材料、目标、读者、决策和评审范围。没有原文时，说明结论仅基于用户描述。
2. 提取关键主张及其证据状态。核对数据口径、比较条件、假设、依赖和未验证事项；不要把偏好写成缺陷。
3. 按方案实际风险检查相关部分，如需求追溯、架构边界、数据迁移、兼容、安全、容量、测试、可观测性、发布、回滚和运维。跳过不适用项。
4. 每项实质发现列出**问题、依据、影响、建议动作、优先级和状态**。没有依据的问题不列为发现；需要信息才能判断时，标为待确认。
5. 给出证据支持的结论：通过、带条件通过、暂缓决定或不通过。没有阻塞问题时可以通过，并把改进建议列为非阻塞项。说明结论依据与重要限制。

## 输出与参考

按评审场景选择简洁格式；无需固定提问数量、问题数量或汇报模板。只有用户要求时才重写原方案。需要问题检查清单时读 [评审问题库](references/interrogation_snippets.md)；需要汇报表达时读 [汇报结构参考](references/presentation_template.md)；需要示例时读 [评审示例](references/good_bad_examples.md)。

评审问题的字段和严重度遵循仓库的 `agent/decision-and-review-contract.md`（单独安装时按本 skill 前述字段执行）。保持直接、专业、可商量；事实不充分时明确不确定性，不用尖锐语气替代证据。
