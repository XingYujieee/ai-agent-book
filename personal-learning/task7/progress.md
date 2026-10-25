# 第 7 章｜逐项进度

更新日期：2026-10-25。下面记我这次实际做的部分。作者以前的运行另列在“历史材料”里；文件能读到，只说明这份材料在当前 Git 快照中。

| 实验 | 本机操作与范围 | 回执 | 历史材料 |
| --- | --- | --- | --- |
| 7-1 运行 τ²-bench 并对比 τ-bench 的演进 | 复核 τ²-bench 保存的活动；未新启动完整客服 benchmark。 | 源码/说明核对 | [保存的材料](../../chapter7/tau2-bench-eval/validation/runs/exp7-1-openrouter-gpt41mini-telecom-20260802-v1/manifest.json) |
| 7-2 人肉执行基准测试任务 | 阅读作者 18 项人工任务记录；未将其计作本人的新人工操作。 | 源码/说明核对 | [保存的材料](../../chapter7/experiment-7-2-human-benchmark/results.json) |
| 7-3 构建基于 Rubric 的用户记忆评估系统 | Rubric 与评估框架测试；清单列出的完整报告未随当前快照提供。 | [rubric: passed](results/checks/rubric.txt) | 未取得对应 Git 文件 |
| 7-4 Advanced JSON Cards 与 RAG 的对比评估 | 评估框架测试；未新跑同一 60 题三策略真实模型比较。 | [rubric: passed](results/checks/rubric.txt) | 未取得对应 Git 文件 |
| 7-5 构建全自动 TTS 质量评估流水线 | 阅读真实音频盲评活动；未新生成多供应商音频。 | [tts-judge: passed](results/checks/tts-judge.txt) | [保存的材料](../../chapter7/tts-quality-eval/validation/mistral_multimodal_20260730/manifest.json) |
| 7-6 对 AndroidWorld 失败轨迹做失败归因 | 读取失败归因、轨迹和前缀回归资料；未新跑 AndroidWorld。 | 源码/说明核对 | [保存的材料](../../chapter7/android-world/failure-attribution/manifest.json) |
| 7-7 轨迹前缀边界评估：同一上下文的多种表示 | 格式化与记忆边界测试；修复工作区换行后历史哈希测试通过。 | [policy: passed](results/checks/policy.txt) | [保存的材料](../../chapter7/user-memory-policy-eval/results/manifest.json) |
| 7-8 从配对比较数据构建模型排行榜 | 复核 Arena 排名活动资料；未重新下载 2 GB 投票快照跑全量。 | [elo: passed](results/checks/elo.txt) | [保存的材料](../../chapter7/elo-leaderboard/validation/runs/exp7-7-arena-20260731-v1/manifest.json) |
| 7-9 在固定 Coding Harness 中测量模型的行动阈值 | 固定 Harness 的任务设计与指标测试；未新调用不同厂商各 9 次。 | [action: passed](results/checks/action.txt) | [保存的材料](../../chapter7/model-action-threshold/results/exp7-8-action-threshold-20260731-v1/manifest.json) |
| 7-10 Agent 任务的端到端成本分析 | 从保存的四组真实用量复算成本；价格为脚本假设，不是本次账单。 | [cost: passed](results/checks/cost.txt) · [演示 exit=0](results/demos/cost-analysis.txt) | [保存的材料](../../chapter7/agent-cost-analysis/sample_trace.json) |
| 7-11 多维度模型性能基准测试 | 活动门禁单测；缺 N≥100 全矩阵、限流爬坡和连续 168 小时记录。 | [benchmark: passed](results/checks/benchmark.txt) | 未取得对应 Git 文件 |
| 7-12 用户记忆系统的端到端选型评估 | 核对现有 1,440 单元矩阵及框架；未重新调用全部模型。 | [rubric: passed](results/checks/rubric.txt) | [保存的材料](../../chapter7/user-memory-system-evaluation/results/full_7_11_60_case_matrix.json) |
| 7-13 AndroidWorld 的评估和改进 | Android 评估器单测和历史资料核对；未运行 580 次新 episode。 | [android: passed](results/checks/android.txt) | [保存的材料](../../chapter7/android-world/validation/candidate_h5c_api33_local_qwen_20260804/evidence.json) |
| 7-14 配置 OpenVLA 与 RoboTwin2 的具身智能环境 | 修复缺失路径的预检错误并测试；没有重建 OpenVLA/RoboTwin2 权重与模拟器。 | [robot-eval: passed](results/checks/robot-eval.txt) | [保存的材料](../../chapter7/openvla-robotwin2-eval/validation/runs/exp7-13-localgpu-20260803-v1/manifest.json) |
