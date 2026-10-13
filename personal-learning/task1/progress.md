# Task 1 学习进度与阶段结果

更新日期：2026-10-13。这里的“完成”只指有对应证据的学习步骤；仓库作者的历史验证与我本次操作分开记录。

| 实验 | 我完成的步骤 | 本次结果 | 尚未亲自复现的原项目步骤 |
| --- | --- | --- | --- |
| 1-1 上下文消融 | 用百炼 `qwen3.7-plus` 跑完五种上下文模式 | `full` 2 轮 1 次工具调用；`no_tool_results` 7 轮 6 次；`no_history` 10 轮仍未回答；`no_reasoning` 正常答 4000；`no_tool_calls` 只有假调用文字 | 可换更难任务重复验证稳定性 |
| 1-2 搜索 Agent | 回放 `offline-demo` 并解读两轮 ReAct；在 1-3 的真实轨迹中观察模型连续搜索 | 离线演示说明控制流；1-3 的第二用例真实完成 5 次托管搜索 | 原项目 Moonshot `kimi-k3` 路线未个人复现，仓库留有历史联网验证 |
| 1-3 搜索 + 代码 | 百炼 `qwen3.7-plus` 完成首都距离题和先澄清后执行题 | 首都题：2 次搜索、2 次代码，最近吉隆坡—新加坡约 315.29 km；澄清题：先问偏好，再完成 5 次搜索和 4 次代码，七项验证通过 | 可重复运行以观察结果稳定性 |
| 1-4 文生图对照 | 两句需求各生成原始提示词和历史改写词两个版本 | 海报改写词丢失指定文案；宽泛需求改写后叙事更明确 | 原版 Kimi 改写 + 万相生图 + Gemini/GPT-Image 路线的跨模型复现 |

## 我保存的阶段产物

- 1-1 五组：[完整上下文](results/full.json)、[隐藏工具结果](results/no-tool-results.json)、[无历史](results/1-1-no_history.json)、[无先前推理](results/1-1-no_reasoning.json)、[无工具定义](results/1-1-no_tool_calls.json)。
- [1-2 离线轨迹](results/offline-demo.json)。
- 1-3：[首都距离完整轨迹](results/experiment-1-3-asean.json)、[先澄清后执行轨迹](results/1-3-clarification.json)。
- 1-4 图片：[海报直接生成](results/experiment-1-4/headphone-direct.png)、[海报改写词](results/experiment-1-4/headphone-rewritten.png)、[AGI 直接生成](results/experiment-1-4/agi-direct.png)、[AGI 改写词](results/experiment-1-4/agi-rewritten.png)。
- [实验过程与解释](experiment.md)、[初学者笔记](notes.md)、[学习心得](reflection-and-feedback.md)。

## 这一阶段我真正学会了什么

我能打开结果文件，先找实际完成的工具调用，再看工具输出是否支持最终结论；做对照时会记录改变了什么条件，并把作者历史数据、离线演示和我自己的真实调用分开。四个实验的核心学习目标都已经实践或用可核验轨迹完成；原项目特定提供商的 1-2、1-4 路线仍未个人复现。下一步可补这些路线，并比较同一任务多次运行是否稳定。
