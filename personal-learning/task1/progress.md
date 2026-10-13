# Task 1 学习进度与阶段结果

更新日期：2026-10-13。这里的“完成”只指有对应证据的学习步骤；仓库作者的历史验证与我本次操作分开记录。

| 实验 | 我完成的步骤 | 本次结果 | 尚未亲自复现的原项目步骤 |
| --- | --- | --- | --- |
| 1-1 上下文消融 | 用百炼 `qwen3.7-plus` 跑 `full` 与 `no_tool_results` 两组 | 都答 4000；工具调用从 1 次增至 6 次 | 其余三种消融模式的个人运行；可先研读仓库五组历史证据 |
| 1-2 搜索 Agent | 回放 `offline-demo` 并解读两轮 ReAct | 看懂思考、搜索动作、观察与最终回答 | Moonshot `kimi-k3` 的个人联网运行；仓库留有真实联网验证 |
| 1-3 搜索 + 代码 | 百炼 `qwen3.7-plus` 完成东盟十国首都距离题 | 2 次搜索、2 次托管代码执行、20 条来源；最近为吉隆坡—新加坡，约 315.29 km | “模糊请求先澄清再执行”的个人运行 |
| 1-4 文生图对照 | 两句需求各生成原始提示词和历史改写词两个版本 | 海报改写词丢失指定文案；宽泛需求改写后叙事更明确 | 原版 Kimi 改写 + 万相生图 + Gemini/GPT-Image 路线的跨模型复现 |

## 我保存的阶段产物

- [1-1 完整上下文结果](results/full.json)与[隐藏工具结果](results/no-tool-results.json)。
- [1-2 离线轨迹](results/offline-demo.json)。
- [1-3 完整 JSON 轨迹](results/experiment-1-3-asean.json)。
- 1-4 图片：[海报直接生成](results/experiment-1-4/headphone-direct.png)、[海报改写词](results/experiment-1-4/headphone-rewritten.png)、[AGI 直接生成](results/experiment-1-4/agi-direct.png)、[AGI 改写词](results/experiment-1-4/agi-rewritten.png)。
- [实验过程与解释](experiment.md)、[初学者笔记](notes.md)、[学习心得](reflection-and-feedback.md)。

## 这一阶段我真正学会了什么

我能打开结果文件，先找实际完成的工具调用，再看工具输出是否支持最终结论；做对照时会记录改变了什么条件，并把作者历史数据、离线演示和我自己的真实调用分开。下一步应补齐上表的个人复现，再比较同一任务多次运行是否稳定。
