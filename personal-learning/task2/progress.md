# Task 2 进度与阶段结果

更新日期：2026-10-15。课程原版的模型和平台要求以 [Chapter 2 实验清单](../../chapter2/EXPERIMENT_LEDGER.md)为准。本表只记本次在 Windows 电脑上实际做过的事。

| 实验 | 本次操作 | 可核查的结果 | 边界 |
| --- | --- | --- | --- |
| 2-1 本地服务 | 安装 Ollama 与 `qwen3:0.6b`；运行三次流式工具任务及完整本地基准 | [基准 JSON](results/2-1-local-benchmark.json)、[三次轨迹与质量检查](results/2-1-local-evaluation.json) | 吞吐超过 100 tok/s，但小模型的工具选择和时区整合仍有错误 |
| 2-2 注意力 | 从仓库保存的真实矩阵重算三层指标，重画热力图 | [数值](results/2-2-reanalysis.json)、[图片](results/2-2-replotted-heatmap.png) | 本机没有重新执行 Transformer 推理 |
| 2-3 KV Cache | 跑离线报告，再从六份原始结果重算 | [六模式表](results/2-3-reanalysis.json) | 采用仓库历史 Kimi API 结果，本机未重新请求 Kimi |
| 2-4 提示工程 | 复算历史 Tau-Bench 六组成功率及平均工具数 | [复算结果](results/2-4-reanalysis.json) | 不是本人的新 Tau-Bench 在线评测；每组 10 题 |
| 2-5 提示注入 | 百炼 `qwen3.7-plus` 跑 3 种攻击 × 4 种防御 × 每格 3 次 | [36 次矩阵](results/2-5-qwen-matrix.json)：12 格均为 0/3 | 无法从这组全零数据量出逐层防御的增益；脚本仅保存聚合矩阵 |
| 2-6 PPT Skill | 跑本机离线三层加载，生成并重新打开 9 页 PPT；核对仓库历史 13 页官方 Skill 成品和四张原图 | [本机 PPT](results/demo-presentation.pptx)、[成品复核](results/2-6-reanalysis.json) | 本机离线版用内置大纲且无论文原图；13 页成品是作者历史运行 |
| 2-7 写作 Skill | 按本人描述生成[四篇练习范文](2-7-generated-samples.md)，更新可加载的[Skill](personal-cn-writing/SKILL.md)，在新题目上对照试写 | [校准记录](2-7-calibration.md) | 样本由助手生成，未经过本人逐句修改；这是目标风格练习，不是个人文风复现验证 |
| 2-8 状态栏注意力 | 重算有无状态栏的注意力区域质量，并核对历史 3+3 次回答 | [复算结果](results/2-8-reanalysis.json) | 基于仓库历史模型矩阵，本机未重新生成注意力张量 |
| 2-9 状态栏 | 本机离线预览；百炼同任务对比全开/全关；复算历史 65 次 Kimi 结果 | [本机对比](results/2-9-qwen-comparison.json)、[历史复算](results/2-9-historical-reanalysis.json) | 简单读文件任务两组均成功，不能证明状态栏提高成功率 |
| 2-10 上下文压缩 | 百炼同任务跑完六种策略，模拟搜索并收紧上下文预算 | [运行结果](results/2-10-qwen-six-strategies.json)、[复核摘要](results/2-10-analysis.json) | 六组均未在四轮内完成；全部累计保存文本比原文长 |

## 本次检查

- `python -m pytest chapter2/agent-skills-ppt/tests -q`：12 项通过。
- `python -m pytest chapter2/system-hint/test_hint_behavior.py -q`：1 项通过。
- `python -m pytest chapter2/context-compression/test_token_tracking.py chapter2/context-compression/test_null_content_compression.py -q`：1 项通过。
- 写作 Skill 用 `quick_validate.py` 校验通过。

2.7 已按本人允许的替代方案完成；原版个人风格验收仍需本人原创范文及改稿。其它历史复算也不能冒充本机原版复现。
