# Worked Example: Metric Change During Instrumentation Migration

This is a demonstration case, not a claim about a production system.

## Request

> 保存成功率从 98% 变成 93%，但按钮、接口和埋点都在同一周改了。产品怀疑新按钮，服务端怀疑日志漏报。今天要给老板结论。

## Decision-ready response

**结论：目前不能判断保存成功率是否真实下降，也不能归因于新按钮。** 两个百分比来自用户提供的信息；统计定义、分母、窗口、样本量和埋点迁移影响尚待确认。

今天先确认两周的分子/分母、事件覆盖、任务关联、去重与上报延迟；再用同一保存任务关联客户端操作、接口请求和最终保存结果。如果无法对齐口径，将 98% 和 93% 标为暂不可比。数据核验后，再按版本或相关环境切分，验证交互、接口或采集问题。

给老板的阶段性同步可以是：**“观察到成功率报表数字变化；因同周发生埋点迁移，数据可比性和原因待确认。今天先核验埋点与服务端结果，再决定是否调整交互。”** 当前没有足够信息设定改善目标或回滚阈值。

## Why this is the right boundary

- The reported values are preserved as user-provided data, not independently measured facts.
- Instrumentation validity is checked before explaining the change.
- Product and server explanations remain hypotheses until evidence distinguishes them.
- The user still gets a usable same-day management update and a concrete verification path.
