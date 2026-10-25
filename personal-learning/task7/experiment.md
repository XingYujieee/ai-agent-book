# 第 7 章｜实验记录

本次在 Windows 的项目 `.venv` 中执行。普通脚本与模型请求的命令、退出码、耗时和日志都保存在 `results/`。离线演示和测试通过，仅对应它们检查到的内容。

本机检查：9 组命令中 9 组退出成功；pytest 的末次汇总为 `{'passed': 87}`。首次失败日志保留在 `checks/*.attempt*.txt`，没有从统计中删掉失败后假装从未发生。

[检查汇总](results/check-summary.json) · [历史材料抽查](results/saved-evidence-review.json)

历史抽查固定在 Git 提交 `faa6db95`，每份 JSON 最多检查 40 个声明文件；使用原始 Git 字节，避免 Windows 换行影响。未能解析的旧路径、未跟踪产物和实际哈希差异会出现在报告中，因此这份抽查不是“所有历史验收重新通过”的证明。

## 成本复算

脚本内假设计费为每百万 token：输入 0.15、缓存输入 0.075、输出 0.60 美元。以下是旧用量在这套假设下的计算结果，未作为当前市场报价或本次真实账单。

| 条件 | 同一计价假设下的总成本（美元） |
| --- | ---: |
| naive | 0.00377580 |
| kv | 0.00270750 |
| compress | 0.00311475 |
| both | 0.00264285 |

[逐轮 JSON](results/cost-analysis.json)保留缓存/未缓存输入、输出、工具上下文与时延。7-11 的 168 小时活动没有启动。

## 7-1｜运行 τ²-bench 并对比 τ-bench 的演进

复核 τ²-bench 保存的活动；未新启动完整客服 benchmark。

本机记录：本次只阅读了正文与入口，没有新运行回执。

历史材料：[保存的材料](../../chapter7/tau2-bench-eval/validation/runs/exp7-1-openrouter-gpt41mini-telecom-20260802-v1/manifest.json)。 Git 原始文件 SHA-256：`ba93a26d81929149ab8086f868e5e42d887f1b7a0430288bea21a31850f7e0d6`。

## 7-2｜人肉执行基准测试任务

阅读作者 18 项人工任务记录；未将其计作本人的新人工操作。

本机记录：本次只阅读了正文与入口，没有新运行回执。

历史材料：[保存的材料](../../chapter7/experiment-7-2-human-benchmark/results.json)。 Git 原始文件 SHA-256：`6376f499d767c80cddc3b150a06546540d975a93cc57b2a1bd588a49af07be2c`。

## 7-3｜构建基于 Rubric 的用户记忆评估系统

Rubric 与评估框架测试；清单列出的完整报告未随当前快照提供。

本机记录：[rubric: passed](results/checks/rubric.txt)

历史材料：未取得对应 Git 文件。

## 7-4｜Advanced JSON Cards 与 RAG 的对比评估

评估框架测试；未新跑同一 60 题三策略真实模型比较。

本机记录：[rubric: passed](results/checks/rubric.txt)

历史材料：未取得对应 Git 文件。

## 7-5｜构建全自动 TTS 质量评估流水线

阅读真实音频盲评活动；未新生成多供应商音频。

本机记录：[tts-judge: passed](results/checks/tts-judge.txt)

历史材料：[保存的材料](../../chapter7/tts-quality-eval/validation/mistral_multimodal_20260730/manifest.json)。 Git 原始文件 SHA-256：`9acf5a561568eb241b6d297744973d85e157ecbd528b35b98c50d2c21bab8e4a`。

## 7-6｜对 AndroidWorld 失败轨迹做失败归因

读取失败归因、轨迹和前缀回归资料；未新跑 AndroidWorld。

本机记录：本次只阅读了正文与入口，没有新运行回执。

历史材料：[保存的材料](../../chapter7/android-world/failure-attribution/manifest.json)。 Git 原始文件 SHA-256：`da9d3b250e610a2753fac24906916f876a7fd6c1336bda8515979066b9b2be3e`。

## 7-7｜轨迹前缀边界评估：同一上下文的多种表示

格式化与记忆边界测试；修复工作区换行后历史哈希测试通过。

本机记录：[policy: passed](results/checks/policy.txt)

历史材料：[保存的材料](../../chapter7/user-memory-policy-eval/results/manifest.json)。 Git 原始文件 SHA-256：`cdfecbf56b6207404b0fe8c194b57bfb5b7f0bdc380dfc876424368c8ef674ff`。

## 7-8｜从配对比较数据构建模型排行榜

复核 Arena 排名活动资料；未重新下载 2 GB 投票快照跑全量。

本机记录：[elo: passed](results/checks/elo.txt)

历史材料：[保存的材料](../../chapter7/elo-leaderboard/validation/runs/exp7-7-arena-20260731-v1/manifest.json)。 Git 原始文件 SHA-256：`e7593c1c833b98009d4289872a2793c63d6da6475a9208314f0782bf2d061a2d`。

## 7-9｜在固定 Coding Harness 中测量模型的行动阈值

固定 Harness 的任务设计与指标测试；未新调用不同厂商各 9 次。

本机记录：[action: passed](results/checks/action.txt)

历史材料：[保存的材料](../../chapter7/model-action-threshold/results/exp7-8-action-threshold-20260731-v1/manifest.json)。 Git 原始文件 SHA-256：`294c70dbe36c3a4b6048eb7a35db4489681c74d8de910ac73b8dbf0c243dd4d5`。

## 7-10｜Agent 任务的端到端成本分析

从保存的四组真实用量复算成本；价格为脚本假设，不是本次账单。

本机记录：[cost: passed](results/checks/cost.txt) · [演示 exit=0](results/demos/cost-analysis.txt)

历史材料：[保存的材料](../../chapter7/agent-cost-analysis/sample_trace.json)。 Git 原始文件 SHA-256：`3bb66868a5a0b3557f1087ef603161295320a5c1f9ad31bbc3bd960497407e92`。

## 7-11｜多维度模型性能基准测试

活动门禁单测；缺 N≥100 全矩阵、限流爬坡和连续 168 小时记录。

本机记录：[benchmark: passed](results/checks/benchmark.txt)

历史材料：未取得对应 Git 文件。

## 7-12｜用户记忆系统的端到端选型评估

核对现有 1,440 单元矩阵及框架；未重新调用全部模型。

本机记录：[rubric: passed](results/checks/rubric.txt)

历史材料：[保存的材料](../../chapter7/user-memory-system-evaluation/results/full_7_11_60_case_matrix.json)。 Git 原始文件 SHA-256：`b33d0e14ce70a7042868767a98956de2624cd70e33d061900b4a2f647b2269e8`。

## 7-13｜AndroidWorld 的评估和改进

Android 评估器单测和历史资料核对；未运行 580 次新 episode。

本机记录：[android: passed](results/checks/android.txt)

历史材料：[保存的材料](../../chapter7/android-world/validation/candidate_h5c_api33_local_qwen_20260804/evidence.json)。 Git 原始文件 SHA-256：`39a5de8fa7007e353084792f2e830ff5baa3d3f677f4bebe3c29c08a88a38a4e`。

## 7-14｜配置 OpenVLA 与 RoboTwin2 的具身智能环境

修复缺失路径的预检错误并测试；没有重建 OpenVLA/RoboTwin2 权重与模拟器。

本机记录：[robot-eval: passed](results/checks/robot-eval.txt)

历史材料：[保存的材料](../../chapter7/openvla-robotwin2-eval/validation/runs/exp7-13-localgpu-20260803-v1/manifest.json)。 Git 原始文件 SHA-256：`f8c53d38c0f8b8fd91206f7f41f7c06925691b4aeb5d95f9675b241e0ca58f2c`。
