# 第 8 章｜逐项进度

更新日期：2026-10-25。下面记我这次实际做的部分。作者以前的运行另列在“历史材料”里；文件能读到，只说明这份材料在当前 Git 快照中。

| 实验 | 本机操作与范围 | 回执 | 历史材料 |
| --- | --- | --- | --- |
| 8-1 Q-learning 在寻宝游戏中的表现 | 本机实际训练 10,000 轮，固定 seed=42，100 轮贪心评估 100/100，平均 12 步。 | [训练与评估](results/q-learning.json) | [保存的材料](../../chapter1/learning-from-experience/validation/20260730_011704/evidence.json) |
| 8-2 传统 RL 与 LLM Agent 的对比研究 | 阅读 Kimi 的历史调用；本次未新跑同环境的 LLM 比较。 | 源码/说明核对 | [保存的材料](../../chapter1/learning-from-experience/validation/20260730_011704/evidence.json) |
| 8-3 从头训练 LLM——算法改进的威力 | 阅读、抽查 MiniMind 历史训练报告；未在本机重训六组。 | 源码/说明核对 | [保存的材料](../../chapter8/MiniMind-pretrain/validation/runs/exp8-3-training-report-20260731-v1/manifest.json) |
| 8-4 自己训练 VLM | 阅读 VLM 对齐/SFT 报告；未下载 CLIP/训练数据重训。 | 源码/说明核对 | [保存的材料](../../chapter8/MiniMind-pretrain/validation/runs/exp8-4-training-report-20260731-v1/manifest.json) |
| 8-5 继续预训练学习新语言 | 核对韩语继续预训练报告；未重新训练和做英语保留集。 | 源码/说明核对 | [保存的材料](../../chapter8/continued-pretraining/validation/runs/exp8-5-training-report-20260731-v1/manifest.json) |
| 8-6 语音 SFT——从 “声音复制” 到 “副语言建模” `[扩展实验]` | 语音 SFT 的分析/契约测试；未新训练语音 LoRA。 | [speech-sft: passed](results/checks/speech-sft.txt) | [保存的材料](../../chapter8/speech-sft-experiment/validation/exp8-6-20260804-v1/REPORT.md) |
| 8-7 多语言思考——让模型用任意语言思考 `[扩展实验]` | 检查多语言思考训练入口；没有新 checkpoint 和前后对照。 | 源码/说明核对 | 无本次选定的完整证据文件 |
| 8-8 Prompt 蒸馏——以更小开销复现可用能力 | Prompt 蒸馏流水线测试及历史材料核对；未生成新教师数据或训练学生。 | [prompt-distillation: passed](results/checks/prompt-distillation.txt) | [保存的材料](../../chapter8/prompt-distillation/validation/exp8-8-kimi3-smollm2-20260730/manifest.json) |
| 8-9 思维链（Chain of Thought, CoT）蒸馏 | CoT 筛选与学生评估流程测试；历史 1/24→2/24 不等于显著提升。 | [cot: passed](results/checks/cot.txt) | [保存的材料](../../chapter8/cot-distillation/validation/experiment_8_9_complete_20260803_v2.json) |
| 8-10 AdaptThink——学会 “何时不思考” | 阅读 AdaptThink 无 checkpoint 报告；未新训练或运行独立 checkpoint 评估。 | 源码/说明核对 | [保存的材料](../../chapter8/AdaptThink/TRAINING_REPORT.md) |
| 8-11 GeneralPoints——单轮 RL 的 “记忆与泛化” 对照 | 外部 GeneralPoints 复现入口核对；缺数据/权重/实际训练。 | 源码/说明核对 | 无本次选定的完整证据文件 |
| 8-12 V-IRL-VL——多轮视觉导航 | 外部 V-IRL 入口核对；未执行视觉导航训练。 | 源码/说明核对 | 无本次选定的完整证据文件 |
| 8-13 SimpleVLA-RL——结果奖励下的开放探索 `[扩展实验]` | SimpleVLA-RL 依赖和指南核对；未配置完整仿真及模型。 | 源码/说明核对 | 无本次选定的完整证据文件 |
| 8-14 ReTool——代码解释器增强数学解题 | ReTool 指南核对；缺 SandboxFusion 服务与训练 checkpoint。 | 源码/说明核对 | 无本次选定的完整证据文件 |
| 8-15 AWorld-train——在沙盒中学习使用工具 | AWorld/veRL 指南核对；未运行奖励曲线训练。 | 源码/说明核对 | 无本次选定的完整证据文件 |
| 8-16 RLVP——奖励结果、惩罚路径 | RLVP 指南核对；未完成源码、CUDA 训练和多种子评估。 | 源码/说明核对 | 无本次选定的完整证据文件 |
| 8-17 从“过早结束”问题案例到 DPO 修复 | 生成偏好对并演示 mock 指标；没有新的真实 DPO 权重训练。 | [dpo: passed](results/checks/dpo.txt) · [演示 exit=0](results/demos/dpo-mock.txt) | [保存的材料](../../chapter8/premature-completion-dpo/validation/train_20260807T163349Z/training_receipt.json) |
| 8-18 作用域敏感的中文弯引号 SFT | 检查作用域数据、受保护区域和评估函数；未新训 LoRA。 | [quotes: passed](results/checks/quotes.txt) | [保存的材料](../../chapter8/curly-quote-sft/validation/manifest.json) |
| 8-19 特殊字符串的精确复制 SFT | 检查随机字符串、字节级评分和数据隔离；未新训精确复制模型。 | [copy: passed](results/checks/copy.txt) | [保存的材料](../../chapter8/exact-copy-sft/validation/manifest.json) |
