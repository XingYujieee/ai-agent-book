# Chapter 3 实验过程与结果

环境：Windows、仓库 `.venv`（Python 3.13.9），本机 Ollama `qwen3:0.6b`。本次没有可用的云模型环境变量。历史正式结果属于作者先前的模型与数据环境；我从基线提交读取原始 Git 文件核对 SHA-256，见[审计报告](results/historical-evidence-audit.json)。

## 3-1、3-2：先确定记忆评估的标尺

课程把记忆分为基础回忆、跨会话检索、主动服务，每层 20 题。作者的四策略同题对照保存在 [user-memory 清单](../../chapter3/user-memory/validation/latest.json)。总体通过率依次为 notes 80%、enhanced notes 86.7%、JSON cards 85%、advanced JSON cards 81.7%。Advanced cards 在第三层 95%，第二层只有 60%；结构更复杂不等于每层都更好。本次只复核历史记录，未新跑模型裁判。

## 3-3：本机日志脱敏

命令：在 `chapter3/log-sanitization` 运行 `..\..\.venv\Scripts\python.exe campaign.py --model qwen3:0.6b`。首次运行第二个样本时遇到模型输出截断的 JSON。我让脚本关闭思考输出，并把解析失败写入回执、标记为非完整活动；随后完整重跑 12 个合成日志。新[证据清单](../../chapter3/log-sanitization/validation/latest.json)指向三个策略和全部原始回执。

| 策略 | 平均精确率 | 平均召回率 | 残留泄漏数 | 平均可用信息比例 |
| --- | ---: | ---: | ---: | ---: |
| 正则 | 41.7% | 50.0% | 9 | 95.4% |
| 本地 LLM | 51.4% | 62.5% | 3 | 67.7% |
| 正则 + LLM | 51.4% | 79.2% | 0 | 76.1% |

这组数据展示了漏检与过度遮盖的取舍。样本只有 12 条，且敏感值均为虚构。

## 3-4、3-5、3-6：从关键词到混合检索

3-4 的[历史结果](../../chapter3/dense-embedding/validation/latest.json)在相同真实嵌入上比较 ANNOY 与 HNSW，两者 recall@k 都是 1.0；前者增量添加需要重建，后者可直接追加。本机没重建嵌入索引。

3-5 本机在 `chapter3/sparse-embedding` 执行 `..\..\.venv\Scripts\python.exe benchmark.py`，手算 BM25 分数误差为 0，精确词查询 Recall@5 为 100%，只靠同义词的查询为 0%。[新清单](../../chapter3/sparse-embedding/validation/latest.json)保留评分明细。它让我看清倒排索引的强项，也看到“找不到同义词”是词法机制本身的边界。

3-6 的[历史五组消融](../../chapter3/retrieval-pipeline/validation/latest.json)中，稀疏检索 Recall@k 为 83.3%，稠密、RRF、加权融合与重排均为 100%；但 MRR 分别为 0.792、1.0、1.0、0.958、0.903。重排没有在这份小数据上提高 MRR，因此不能把流水线越长理解为质量必然越高。本机未加载对应神经模型。

## 3-7、3-8：组织证据，再决定是否继续搜索

3-7 在 `chapter3/structured-index` 运行 `main.py demo --output ...`，保存[预置 Intel 指令示意](results/3-7-offline.json)。它显示图关系如何连接寄存器、指令与控制位，层次树如何先给概览再下钻。作者的[真实 Intel 文档活动](../../chapter3/structured-index/validation/latest.json)则保存了在线抽取与摘要；两种索引在 8 条查询上的平均引用召回同为约 95.8%。离线示意本身不能验证 LLM 建索引质量。

3-8 在 `chapter3/agentic-rag` 运行 `compare_offline.py --output ...`，本机索引 288 篇法律文档、21,372 个法条块。[7 题离线对照](results/3-8-offline.json)的整体证据召回由单次检索 76.2% 提高到分解检索 100%，平均查询次数由 1.0 增至 1.29；复杂题为 58.3%→100%。子查询是题目预先提供的，不能冒充模型现场推理。作者的[在线活动](../../chapter3/agentic-rag/validation/latest.json)另外记录了模型调用、引用与延迟。

## 3-9、3-10、3-11：检索回到用户记忆

3-9 在 `chapter3/agentic-rag-for-user-memory` 运行 `offline_demo.py --quiet --output ...`。[两辆车案例](results/3-9-offline.json)中，单次检索覆盖一半关键事实；五次聚焦查询覆盖全部。作者的[60 题在线结果](../../chapter3/agentic-rag-for-user-memory/validation/latest.json)总体通过率 78.3%，第三层 65%。

3-10 本机核对了[作者 15 题正式活动](../../chapter3/contextual-retrieval/validation/latest.json)：BM25 Recall@1 从 60% 到 80%，稠密从 86.7% 到 93.3%，混合从 73.3% 到 86.7%。这不是本机新生成前缀的结论；原活动的 `document_store.json` 没在本仓库提交。

3-11 在 `chapter3/contextual-retrieval-for-user-memory` 运行 `contextual_compare.py --output ...`。[8 问离线对照](results/3-11-offline.json)的 Recall@1 从 62.5% 到 75%，Recall@3 两组都为 100%；前缀已写在教学数据里。作者的[60 题三组对照](../../chapter3/contextual-retrieval-for-user-memory/validation/latest.json)总体通过率：普通窗口 78.3%，上下文前缀 86.7%，前缀加 Advanced JSON Cards 95%。这是历史活动，不是本机复现。

## 3-12：从判例中找原型

作者的[CAIL2018 活动](../../chapter3/structured-knowledge-extraction/validation/latest.json)保存了因子发现、抽取、聚类和留出集建议的回执；摘要显示 16 个通用因子、11 个原型。官方原始压缩包不在这个 checkout 中，我未重新下载数百条判例或调用模型。历史摘要的部分中文标签有编码损坏，不能从标签推断具体罪名；只将数值作为保存记录引用。

## 检查和可复现边界

`python personal-learning/task3/verify_history.py` 从 Git 基线 `6ccf611d` 验证 33/33 份历史结果文件的 SHA-256。声明输入有 551 份匹配、6 份与基线不同、2 份缺失；缺失项是 3-10 的文档存储和 3-12 的官方数据压缩包。`pytest` 对本次涉及的脱敏、BM25、图检索运行 37 项，全部通过。历史 `passed` 表示作者保存的活动状态；哈希一致只能证明文件未变，不能代替本机重新调用模型或独立确认裁判正确。
