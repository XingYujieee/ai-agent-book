# Chapter 2 实验过程与证据

我在 Windows 上用项目根目录的 `.venv`（Python 3.13.9）完成本机部分。在线等价实验用的是华北 2 百炼业务空间和 `qwen3.7-plus`，密钥只放在进程环境变量里。下面每项都注明模型、预算，以及结果是这次运行还是作者留下的记录。

## 2-1 · 本地小模型服务

安装 Ollama，拉取 `qwen3:0.6b`，用项目 `main.py --backend ollama --mode single` 连本机服务。[环境记录](results/2-1-local-environment.json)为 Ollama 0.40.4、Python 3.13.9、RTX 3070 Laptop GPU；这些配置会影响速度。先让模型自行选择工具，再逐步明确应调用 `get_current_time` 与 `get_current_temperature`。三次轨迹：[原始](results/2-1-local-tool-trace.txt)、[指定工具](results/2-1-local-guided-trace.txt)、[指定字段](results/2-1-local-corrected-trace.txt)。

[三次轨迹的结构化核对](results/2-1-local-evaluation.json)记录了每次实际调用的工具、最终回答和原始文件校验值。

| 条件 | 实际工具 | 回答问题 |
| --- | --- | --- |
| 原始任务 | 并行调用 `get_current_time` 与 `code_interpreter` | 没取天气；把本地时间说成 UTC |
| 明确工具名 | 并行调用时间与天气工具 | 把天气结果中的观测时间 `12:45` 当成当前时间；时间工具实际为 `12:59:18` |
| 明确字段来源 | 并行调用时间与天气工具 | 时间字段与气温取对，但把 `-0700` 写成 `UTC+7` |

运行 `benchmark.py --backend ollama --scenario all --repeats 5`，保存[完整基准](results/2-1-local-benchmark.json)：平均单流解码 317.1 tok/s、平均 TTFT 2.115 秒；缓存命中 TTFT 2.131 秒，未命中 2.159 秒；并发 1→8 时聚合吞吐 87.1→233.7 tok/s，但单请求吞吐 87.1→29.2 tok/s。仓库作者在另一台机器上的[历史记录](../../chapter2/local_llm_serving/runs/exp2-1-qwen3-0.6b-20260730-v2/evidence.json)报告 106.7 tok/s，不能把两台机器的数据当作同一次对照。[历史数据复核摘要](results/2-1-reanalysis.json)。

## 2-2、2-8 · 注意力矩阵

仓库保存了 Qwen3 0.6B 的真实注意力矩阵。我用 NumPy 重算第 0、13、27 层的上三角权重与第一列平均注意力，并用 Matplotlib 从原始数组重新绘制[三层热力图](results/2-2-replotted-heatmap.png)。未来位置最大权重均为 0；第一列均值分别约 0.147、0.739、0.832。[数值与源文件哈希](results/2-2-reanalysis.json)。

2-8 的历史矩阵重新计算了对电话记录、搜索干扰、状态栏和最新用户问题的注意力区域质量，并对照历史 3+3 次模型回答：[复核结果](results/2-8-reanalysis.json)。有状态栏组拒绝第 4 次拨号 3/3，无状态栏组 2/3。这里没有在本机重新生成模型注意力张量。

## 2-3 · 缓存前缀管理

在 `chapter2/kv-cache` 目录运行 `..\..\.venv\Scripts\python.exe main.py --report`，读取六份原项目 API 结果；再从原 JSON 重算[六模式表](results/2-3-reanalysis.json)。正确模式 3 轮成功、缓存占比 10.1%；乱序工具 3 轮成功但缓存占比 3.4%；滑动窗口缓存占比 67.9%，却在 5 轮后失败。绝对 TTFT 来自历史 Kimi K2.6 运行，不是本机实时性能。

## 2-4 · 提示工程消融

从仓库历史完整的 6 组 × 10 个 Tau-Bench 任务的 `comparison.json` 重新计算成功数、平均轮数和工具调用数，保存[复算表](results/2-4-reanalysis.json)。基线 7/10；语气 `tone_trump` 6/10、`tone_casual` 9/10；规则乱序 8/10；移除工具描述 9/10；全部消融 8/10。这是历史 Kimi K3 评测的重新分析，未在本机重新运行 60 个任务；差异也不足以证明一般性的因果效果。

## 2-5 · 提示注入攻防

先用 `demo.py --list` 核对三类攻击与四层防御；再用百炼模型运行完整的 `3 × 4 × 3 = 36` 次矩阵，保存[聚合结果](results/2-5-qwen-matrix.json)。所有单元格攻击成功数均为 0/3，包括 D1 无防御。程序固定打印的“成功率显著下降”不符合本次数据。本次只保存聚合比例，原项目的逐轮 Kimi 文件操作证据属于[仓库历史验证](../../chapter2/prompt-injection/validation/latest.json)。

## 2-6、2-7 · Agent Skills

运行 `agent-skills-ppt/demo.py --offline`，顺序看到薄目录、`SKILL.md`、参考文档和捆绑脚本的加载，生成[九页 PPT](results/demo-presentation.pptx)，并由 `python-pptx` 重新打开。仓库作者使用官方 PPTX Skill 生成的论文演示文稿为 13 页；我重新核对了它的 SHA-256、页数，并验证四张源论文图与 PPTX 内嵌图字节相同：[核对结果](results/2-6-reanalysis.json)。本机离线大纲没有论文图片，也没有模型自行选择 Skill。

学习者进一步描述了目标风格：“克制、简洁、优美、有深意，有些地方会有趣”，并允许用生成范文代替本人原创文章做练习。我据此生成[四篇样本](2-7-generated-samples.md)，更新[写作 Skill](personal-cn-writing/SKILL.md)的触发条件、五条带正反例的原则、范围和例外，再用未出现在样本中的状态栏题目做[改写前后对照](2-7-calibration.md)。Skill 通过 `quick_validate.py`。样本与改写均由助手完成，能验证流程和规则是否可用，不能验证它复现了学习者的个人文风。

## 2-9 · 状态栏

先运行 `main.py --mode preview` 查看追加的时间、工具次数、TODO、错误建议和系统状态。再用[本次脚本](run_2_9_qwen.py)对同一读文件任务运行全关与全开两组，模型均调用一次 `read_file` 并正确答复：[对照摘要](results/2-9-qwen-comparison.json)与两份轨迹。此小任务未显示状态栏增益。另对仓库历史 65 次 Kimi 结果进行[复算](results/2-9-historical-reanalysis.json)：时间戳组多 2/5 个通过，TODO 组少 1/5，详细错误组少 1/5，提示效果依任务而变。

## 2-10 · 六种压缩策略

使用项目 `experiment.py`，让六种策略处理同一创始人研究任务，模型为百炼 `qwen3.7-plus`。通过脚本入口把演示上下文预算设为 3,500 token，每组最多四轮；未提供 Serper Key，`search_web` 使用项目内置模拟结果，而 `fetch_webpage` 仍可能访问网页。先运行无压缩冒烟，再运行[六组结果文件](results/2-10-qwen-six-strategies.json)。收紧预算只是为了触发压缩行为，不是百炼模型的真实窗口大小。六组均未在四轮内产生最终答案；无压缩和逐条摘要各有一次预算溢出，其余四组没有。六组累计保存文本与原文之比分别为 133.6%、171.8%、131.1%、107.6%、136.7%、159.7%，都没有真正缩短。逐条摘要总耗费 31,852 token，相关摘要为 6,880 token，但工具调用数分别为 11 与 14，不能把 token 差异全部归于策略。[复核摘要](results/2-10-analysis.json)保留原结果哈希。模拟搜索使本次无法评价引用的真实准确性；运行中的“研究结论”不作为实时事实引用。

## 验证与共同限制

本机 PPT Skill 项目 12 项测试通过，System Hint 的行为测试 1 项通过，上下文压缩相关测试 1 项通过；新写作 Skill 格式校验通过。原项目作者已经保存了多个正式运行，本次复算保留源文件 SHA-256 与路径，明确与我自己的在线调用分开。单次或少量任务只能报告观察，不能代替课程原版完整重复试验。
