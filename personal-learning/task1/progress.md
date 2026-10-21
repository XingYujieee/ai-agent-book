# Task 1 学习进度与阶段结果

更新日期：2026-10-15。我用现有服务把 1-1 到 1-4 的学习实验做了，也留下了能回查的结果。原项目指定的部分服务路线没有亲自跑；表里把我的操作和作者的历史记录分开放。

| 实验 | 我完成的步骤 | 本次结果 | 尚未亲自复现的原项目步骤 |
| --- | --- | --- | --- |
| 1-1 上下文消融 | 用百炼 `qwen3.7-plus` 跑完五种上下文模式 | `full` 2 轮 1 次工具调用；`no_tool_results` 7 轮 6 次；`no_history` 10 轮仍未回答；`no_reasoning` 正常答 4000；`no_tool_calls` 只有假调用文字 | 可换更难任务重复验证稳定性 |
| 1-2 搜索 Agent | 回放 `offline-demo`；从一次真实百炼 Responses 调用中提取搜索事件并验收 | [等价留证](results/1-2-equivalent-trace.json)检查通过：2 次不同的搜索均完成，后接最终回答，并有来源引用 | 原项目 Moonshot `kimi-k3` Formula 路线未个人复现；等价留证复用 1-3 的一次真实调用，不能算独立的新 API 运行 |
| 1-3 搜索 + 代码 | 百炼 `qwen3.7-plus` 完成首都距离题和先澄清后执行题 | 首都题：2 次搜索、2 次代码，最近吉隆坡—新加坡约 315.29 km；澄清题：先问偏好，再完成 5 次搜索和 4 次代码，七项验证通过 | 可重复运行以观察结果稳定性 |
| 1-4 文生图对照 | 两句需求各生成原始提示词和历史改写词两个版本，并逐张目视检查 | [逐项对照](results/experiment-1-4/comparison.md)：海报改写词丢失指定文案；宽泛需求改写后分工叙事更明确 | 原版 Kimi 改写 + 万相生图 + Gemini/GPT-Image 路线的跨模型复现 |

## 我保存的阶段产物

- 1-1 五组：[完整上下文](results/full.json)、[隐藏工具结果](results/no-tool-results.json)、[无历史](results/1-1-no_history.json)、[无先前推理](results/1-1-no_reasoning.json)、[无工具定义](results/1-1-no_tool_calls.json)。
- 1-2：[离线轨迹](results/offline-demo.json)、[真实搜索等价留证](results/1-2-equivalent-trace.json)（从 1-3 调用中提取，含源文件 SHA-256）。
- 1-3：[首都距离完整轨迹](results/experiment-1-3-asean.json)、[先澄清后执行轨迹](results/1-3-clarification.json)。
- 1-4 图片：[海报直接生成](results/experiment-1-4/headphone-direct.png)、[海报改写词](results/experiment-1-4/headphone-rewritten.png)、[AGI 直接生成](results/experiment-1-4/agi-direct.png)、[AGI 改写词](results/experiment-1-4/agi-rewritten.png)；[逐项检查与结论](results/experiment-1-4/comparison.md)。
- [实验过程与解释](experiment.md)、[初学者笔记](notes.md)、[学习心得](reflection-and-feedback.md)。

## 这一阶段我真正学会了什么

我能打开结果文件，先找实际完成的工具调用，再看工具输出是否支持最终结论；做对照时会记录改变了什么条件，并把作者历史数据、离线演示和我自己的真实调用分开。四个实验的核心学习目标已通过现有服务完成并验收。1-2 的百炼托管搜索与原版 Kimi Formula 的客户端循环不同；1-4 的同工具对照与原版跨模型对照也不同。将来若有对应服务的密钥，可再补原版复现，并比较多次运行的稳定性。
