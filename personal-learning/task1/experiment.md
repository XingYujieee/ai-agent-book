# Task 1 实验过程与阶段结果

## 实验目标

观察 ReAct 循环，并比较模型在完整上下文与看不到工具结果时的行为。对应原书第 1 章的实验 1-2（搜索 Agent 轨迹）和实验 1-1（上下文消融）。

## A. 离线搜索轨迹

使用 `web-search-agent` 的 `offline-demo` 模式回放预写轨迹。问题是“Moonshot AI 的 Context Caching 是什么技术？”。轨迹依次显示：

1. 思考：先查定义；行动：调用 `web_search`；观察：得到定义与作用。
2. 思考：还缺适用场景；行动：再次调用 `web_search`；观察：得到典型用途。
3. 最终综合回答。

这个演示用于看懂“思考 → 行动 → 观察”的控制流。搜索结果是教学示例，不能当作真实联网搜索或服务连通性证据。原始输出：[offline-demo.json](results/offline-demo.json)。

## B. 上下文消融对照

**执行日期：**2026-10-13。**提供商及模型：**阿里云百炼 `dashscope`，`qwen3.7-plus`。**相同任务：**“请调用计算器计算 (125 + 375) * 8，并给出结果。”两组只改变 `--context-mode`。

```powershell
# 在 chapter1\context 目录执行；使用仓库根目录已有的 .venv
..\..\.venv\Scripts\python.exe main.py --mode single --provider dashscope --context-mode full --task "请调用计算器计算 (125 + 375) * 8，并给出结果。" --output full.json
..\..\.venv\Scripts\python.exe main.py --mode single --provider dashscope --context-mode no_tool_results --task "请调用计算器计算 (125 + 375) * 8，并给出结果。" --output no-tool-results.json
```

| 观察项 | `full` | `no_tool_results` |
| --- | --- | --- |
| 完成终止响应 | 是 | 是 |
| Agent 轮数 | 2 | 7 |
| 工具调用次数 | 1 | 6 |
| 工具调用过程 | `calculate` 一次 | `calculate` 四次、`code_interpreter` 两次；尝试重复表达式与简化表达式 |
| 最终数值 | 4000 | 4000 |
| 模型能否看到工具返回值 | 能 | 不能；发送给模型的 `tool.content` 为空 |

完整组调用一次计算器，读到返回值后回答。消融组的工具**实际执行成功**，但工具结果在发送给模型前被清空。模型认为工具没有正常返回，先重复调用计算器，再尝试代码工具，最终改为手算并给出 4000。

**结论：**这次简单算术题的最终数值没有变，但移除工具结果使执行从 2 轮、1 次工具调用增加到 7 轮、6 次工具调用。消融组的回答不能算作“依据工具结果确认”，因为模型没有看到结果。单次任务只能说明这次运行的行为，不代表所有任务都会如此。

原始输出：[full.json](results/full.json) · [no-tool-results.json](results/no-tool-results.json)。这些文件是用户实际运行产生的结果；本记录没有重新运行实验。

## 下一步

可以选择一个不能轻易心算、又能核对标准答案的任务，用相同模型和参数重复对照。记录每轮发给模型的消息、工具调用和终止原因，再判断差异是否稳定。
