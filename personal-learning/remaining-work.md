# Chapter 4–10｜尚未完成的正式运行

这是继续实验时要补的条件。当前笔记和本机结果已经整理好，下列范围仍没有新的完整运行证据。

| 范围 | 缺少的条件 | 接着从哪里做 |
| --- | --- | --- |
| 4-2、4-4、4-5 | 私有日历、Notion、邮件、IM/Slack 服务配置和对应测试对象 | [第 4 章原版门禁](../chapter4/EXPERIMENT_LEDGER.md) |
| 5-1、5-2及在线代码/媒体实验 | 对应模型服务；论文、音频或 3D 供应商；完整独立审核环境 | [第 5 章目录](../chapter5/README.md) |
| 5-13、5-15 | 专用 PostgreSQL 测试数据库；当前没有建立测试库 | [权限对象说明](../chapter5/permission-embedded-data-objects/README.md) |
| 5-16 | 清单所指历史 comparison.json 不在当前 Git；新双臂活动还需要模型服务 | [Agent 创建器](../chapter5/agent-creator/README.md) |
| 6-1、6-3至6-9 | 邮件/原生异步/语音/视觉服务或对应本地模型；流式验收还引用未取得的原作者音频输入和本地权重 | [第 6 章目录](../chapter6/README.md) |
| 6-10、6-12 | XLeRobot 真机、驱动、校准、急停、现场观察及模型服务 | [真机遥操作](../chapter6/xlerobot-teleoperation/README.md) · [自主操作](../chapter6/gemini-xlerobot-navigation/README.md) |
| 7-1至7-9、7-12至7-14的完整活动 | 各自完整数据/模拟器/模型和在线费用；部分历史报告未跟踪 | [评估目录](../chapter7/README.md) |
| 7-11 | N≥100 的性能矩阵、限流爬坡、Agent 成本阶段和连续 168 小时可用性记录 | [模型基准](../chapter7/model-benchmark/README.md) |
| 8-2至8-19 | 每项独立的数据、基础权重、训练栈与评估环境；部分依赖 CUDA/Linux/较大显存或外部服务 | [训练实验清单](../chapter8/EXPERIMENT_LEDGER.md) |
| 9-2、9-3、9-5至9-9的完整模型活动 | 对应真实模型；自修改候选需要 Docker；Hermes 需要独立运行环境 | [持续进化目录](../chapter9/README.md) |
| 9-4 | 已做六题本机三臂决策补充，完整任务交付、用户反馈、独立保留集和发布门槛仍未实现 | [本次十八次调用](task9/results/clarification-trial/summary.json) |
| 10-1至10-6的完整在线路线 | 模型、搜索、浏览器/语音服务和各项目环境；小镇完整活动涉及大量模型调用 | [多 Agent 目录](../chapter10/README.md) |

本次可以重跑的入口：

```powershell
# 从仓库根目录执行，使用已经安装依赖的 .venv
.\.venv\Scripts\python.exe personal-learning/run_learning_checks.py
.\.venv\Scripts\python.exe personal-learning/run_learning_demos.py
.\.venv\Scripts\python.exe personal-learning/task8/run_q_learning.py
.\.venv\Scripts\python.exe personal-learning/task9/run_clarification_trial.py
.\.venv\Scripts\python.exe personal-learning/task6/run_gpu_labs.py
```

最后两项分别要求本机 Ollama 的 qwen3:0.6b 和可用的 CUDA PyTorch。它们没有调用收费云服务。四场景子进程脚本使用固定活动目录，重复运行前应给脚本换一个新的 campaign ID，保留前一次记录。
