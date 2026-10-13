# Task 1 实验过程与阶段结果

## 实验目标

依次学习第 1 章实验 1-1 至 1-4：上下文消融、搜索 Agent、搜索加代码执行，以及文生图工作流对照。下文严格区分三类证据：**我在本机得到的结果**、**仓库作者留下的历史验证**、**为学习原理而做的简化对照**。

## 1-2：搜索 Agent 的离线轨迹

使用 `web-search-agent` 的 `offline-demo` 模式回放预写轨迹。问题是“Moonshot AI 的 Context Caching 是什么技术？”。轨迹依次显示：

1. 思考：先查定义；行动：调用 `web_search`；观察：得到定义与作用。
2. 思考：还缺适用场景；行动：再次调用 `web_search`；观察：得到典型用途。
3. 最终综合回答。

这个演示用于看懂“思考 → 行动 → 观察”的控制流。搜索结果是教学示例，不能当作真实联网搜索或服务连通性证据。原始输出：[offline-demo.json](results/offline-demo.json)。

仓库的[历史联网验证](../../chapter1/web-search-agent/validation/latest.json)使用 Moonshot `kimi-k3` 与托管 `web_search`，记录了多轮搜索、15 个成功的搜索任务、来源链接及最终回答。这是作者的运行记录，不是我本次离线演示产生的结果；我没有 Moonshot 密钥时，不能把离线演示写成已完成联网复现。

## 1-1：上下文消融对照

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

仓库的[五组历史验证](../../chapter1/context/validation/latest.json)还包括移除历史、推理与工具定义三组，任务是多币种换算，与我的简单算术任务不同。因此只能用于理解五种消融各在测试什么，不能把它们的数字并入上表。尤其是移除工具结果时，工具可以执行成功，但发送给模型的观察内容为空；模型在下一轮无法依据该结果决策。

## 1-3：联网搜索加托管 Python

**执行日期：**2026-10-13。**后端及模型：**华北 2 百炼业务空间、`qwen3.7-plus`。**任务：**搜索东盟 10 国首都坐标，并用 Python 比较首都两两之间的大圆距离。实际命令在 `chapter1/search-codegen` 目录运行：

```powershell
..\..\.venv\Scripts\python.exe main.py --backend dashscope --mode single --request "东盟 10 国首都之间最近的一对是哪两个？请搜索并用 Python 计算" --output result-1-3.json
```

这次请求成功，服务端轨迹有 **2 个完成的 `web_search_call`**、**2 个完成的 `code_interpreter_call`**，并记录了 20 条来源引用。第一段实际 Python 日志枚举 45 对首都，报告最近的一对为**吉隆坡—新加坡，315.29 公里**。第二段代码比较了努桑塔拉与这两个城市的距离。原始结果：[experiment-1-3-asean.json](results/experiment-1-3-asean.json)。不同坐标点会让公里数略有变化，重点是查验城市集合、坐标和代码日志，而非只抄最终答案。

排障过程也属于实验记录：最初把华北 2 密钥发到国际站地址，得到 `InvalidApiKey`；改成业务空间专属域名后，程序又因域名不含 `dashscope` 而误判提供商，发送了不合适的参数；修正识别逻辑后仍报 `Bad Request`，最终查出传入的密钥实际上只有 1 个字符。重新安全输入完整密钥后，最小请求返回 HTTP 200，完整实验成功。错误消息相同不代表原因相同，应检查实际请求体和最小调用。

仓库还要求观察“模糊问题先澄清、再使用工具”的第二个用例；我的本次运行只完成了首都距离用例，不能将仓库[历史完整验收](../../chapter1/search-codegen/validation/latest.json)算作我的第二次实测。

## 1-4：提示词改写与直接生图

我用项目的两句原始需求与仓库[历史改写结果](../../chapter1/image-gen-workflow/validation/latest.json)，通过同一个内置生图工具做了 **2 个需求 × 2 种提示词**的小规模对照。这次的两条路径都使用同一生图工具；改写词来自仓库历史记录，**没有在本次运行 Kimi 改写节点或通义万相工作流**。这样可以直观看提示词内容如何影响结果，但不能代替原项目跨模型的正式对照。

| 需求 | 原始需求直接生成 | 使用仓库历史改写词生成 | 观察 |
| --- | --- | --- | --- |
| 降噪耳机海报，必须有“深夜独处也清净” | [图片](results/experiment-1-4/headphone-direct.png)有完整中文文案 | [图片](results/experiment-1-4/headphone-rewritten.png)有夜景耳机，没有文案 | 改写结果的负面提示词含 `text`，把用户的核心文案排除了 |
| AGI 后程序员的工作场景 | [图片](results/experiment-1-4/agi-direct.png)有程序员与 AI 合作的场景 | [图片](results/experiment-1-4/agi-rewritten.png)明确表现“人喝咖啡、机器人写代码” | 改写词把宽泛主题变成具体叙事，但直接生成也能自行补充场景 |

四张图片均保存在 `results/experiment-1-4/`。这是每个条件各一次生成，只能说明这四张图的差异，不能推断哪条路线总是更好。仓库原版[1-4 记录](../../chapter1/image-gen-workflow/README.md)包含 5 句需求、3 条路线共 15 次成功调用；其原始图片并未包含在当前仓库检出中，所以我没有对那些图片进行独立目视评分。

## 下一步

若要严格复现原项目的全部验收，应补齐 1-1 的其余三种个人消融、1-2 的 Moonshot 实时搜索、1-3 的先澄清后执行任务，以及 1-4 的 Kimi／万相／原生生图跨模型路线。补跑时保留模型、提示词、接口、返回内容与图片，避免把作者历史记录当成自己的实验。
