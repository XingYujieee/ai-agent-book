# Task 3 逐项进度

更新日期：2026-10-21。我把这次本机运行和作者以前留下的结果分开列；表里的“历史”只表示我复核了保存的证据。原版验收要求见 [Chapter 3 清单](../../chapter3/EXPERIMENT_LEDGER.md)。

| 实验 | 本次操作 | 结果与证据 | 边界 |
| --- | --- | --- | --- |
| 3-1 三层记忆评估 | 核对 60 个用例与作者四模式完整评估 | [历史证据审计](results/historical-evidence-audit.json)；每层 20 题 | 未在本机重新执行 60 题的生成与独立裁判 |
| 3-2 四种记忆策略 | 复算作者各层通过率 | [作者清单](../../chapter3/user-memory/validation/latest.json)；总体 notes 80%、enhanced notes 86.7%、JSON cards 85%、advanced cards 81.7% | 同一历史 60 题，非本机新对照 |
| 3-3 日志脱敏 | 本机 Ollama `qwen3:0.6b` 跑满 12 个样本 × 3 策略，并修复无效 JSON 使程序保留失败回执 | [新证据](../../chapter3/log-sanitization/validation/latest.json)：hybrid 召回 79.2%、残留泄漏 0 | 12 个合成日志；不是生产环境安全保证 |
| 3-4 稠密向量与 ANN | 复核作者同向量 ANNOY/HNSW 比较 | [历史清单](../../chapter3/dense-embedding/validation/latest.json)；两组 recall@k 为 1.0 | 本机没有重新下载嵌入模型及构建 ANN |
| 3-5 BM25 稀疏检索 | 本机跑手算校验和标注语料基准 | [新证据](../../chapter3/sparse-embedding/validation/latest.json)：精确词召回 100%，纯同义词 0% | 教学语料规模较小 |
| 3-6 混合检索与重排 | 复核作者稀疏、稠密、RRF、加权融合与重排消融 | [历史清单](../../chapter3/retrieval-pipeline/validation/latest.json) | 本机未加载稠密编码器和交叉编码器 |
| 3-7 RAPTOR 与 GraphRAG | 本机跑结构化索引离线示意；复核作者 Intel 文档正式实验 | [离线结果](results/3-7-offline.json)、[历史清单](../../chapter3/structured-index/validation/latest.json) | 离线图与树是预置示意，未在本机调用 LLM 建索引 |
| 3-8 Agentic RAG | 本机离线 BM25 对比；复核作者在线司法问答 | [离线结果](results/3-8-offline.json)：7 题证据召回 76.2%→100%；[历史清单](../../chapter3/agentic-rag/validation/latest.json) | 离线子查询预先写好，不等于模型现场制定检索计划 |
| 3-9 跨会话记忆检索 | 本机跑两辆车的离线多轮检索；复核作者 60 题 | [离线结果](results/3-9-offline.json)：本例召回 50%→100%；[历史清单](../../chapter3/agentic-rag-for-user-memory/validation/latest.json) | 本机只是一个预设检索案例，未调用独立裁判 |
| 3-10 上下文感知检索 | 核对作者 15 条查询的 BM25、稠密、混合对照 | [历史清单](../../chapter3/contextual-retrieval/validation/latest.json) | 本机缺原运行的 `document_store.json`，没有重新生成前缀 |
| 3-11 双层用户记忆 | 本机运行 8 问离线词法对照；复核作者 60 题三组对照 | [离线结果](results/3-11-offline.json)：Recall@1 62.5%→75%；[历史清单](../../chapter3/contextual-retrieval-for-user-memory/validation/latest.json) | 离线前缀预先写好；本机未生成卡片或执行 60 题 |
| 3-12 判例隐性知识 | 审核作者 CAIL2018 正式活动的因子、原型与留出集摘要 | [历史清单](../../chapter3/structured-knowledge-extraction/validation/latest.json) | 官方原始压缩包未随仓库提供；本机未重新下载或调用模型 |

## 本次核查

- 用 [审计脚本](verify_history.py)按基线提交 `6ccf611d` 的 Git 原始字节验证历史清单：33/33 件结果文件哈希一致；559 个声明输入中 551 个一致、6 个与当前基线文件不同、2 个缺失。清单可查，但不能由此推断所有历史环境已完整保留。
- 本机 3-3 与 3-5 的新清单均报告 `passed`，原始回执和 SHA-256 保存在各项目 `validation/runs/`。
- 针对脱敏、BM25 和结构化图检索运行 37 个回归测试，全部通过。
