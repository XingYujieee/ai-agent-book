# Chapter 4 实验过程与结果

本次在 Windows 的项目 `.venv` 内运行，未设置外部模型、日历或通知服务凭据。历史正式活动均从 Git 基线 `382d39d2` 读取并核验文件哈希，详见[审计报告](results/historical-evidence-audit.json)。作者原始清单保留章节重编号前的实验标签；此处按目前正文的 4-1 至 4-5 编号记录。

## 4-1：工具很多时，何时找工具

在 `chapter4/active-tool-discovery` 运行 `demo.py --offline --output ...`。126 个工具、8 个任务分别走全量注入、一次性检索预筛选、主动发现。本机[结构化结果](results/4-1-offline.json)显示三组精确选对任务为 8/8、4/8、8/8；总注入 token 为 93,040、8,236、7,796。这里的嵌入是本地哈希向量，模型是脚本化 mock；准确率只检验路由机制。

作者的[Qwen3-4B 正式活动](../../chapter4/active-tool-discovery/validation/experiment_4_1/rerun_20260825/summary.json)中，控制与主动发现两组都是 3/3 完成，故没有证明准确率增益。主动发现实测总用时 783.442 秒，控制组 3,056.294 秒；轨迹里仍有无关调用和过早结束。本机没有重跑 4B 模型及真实 MCP 工具群。

## 4-2：感知工具

在 `chapter4/perception-tools` 运行 `cli.py demo --offline`，[日志](results/4-2-offline-log.txt)记录本地 grep 命中 5 处、文件读取成功、知识库检索命中 1 个文件；网络、公开数据和私有数据步骤在离线模式中跳过。作者[正式清单](../../chapter4/perception-tools/validation/experiment_4_2/real_mcp_dashscope_intl_20260730T070000Z/summary.json)已覆盖真实 MCP 目录、搜索、多模态、文件系统和公开数据，私有日历及 Notion 因缺 OAuth/集成凭据保持 `blocked`。本次没有把跳过的类别写成成功。

## 4-3：同一材料的三种多模态路线

运行 `create_sample.py --output-dir ...`，生成[图表](results/4-3-sample/sample_chart.png)与[单页 PDF](results/4-3-sample/sample_report.pdf)。人工查看图表：Q4 最高，为 180M；`PyPDF2` 提取 PDF 文本时，Q1—Q4 的四个精确数字均未出现，[校验记录](results/4-3-sample-analysis.json)。所以只读正文不足以回答“哪一季、精确多少”。这仅验证输入材料的设计。

作者的[四问正式对照](../../chapter4/multimodal-agent/validation/runs/20260729T185433Z-4_2-e028c9db/evidence.json)里，原生多模态与按需工具分析均为 4/4，先提取为文本为 0/4；平均用时分别约 8.0、29.8、10.9 秒（按原生、工具、文本顺序）。本机没有重新调用视觉模型或外部裁判，不能把样例生成算作三路线复现。

## 4-4：执行工具的安全边界

在 `chapter4/execution-tools` 用 CLI 把合法的 `sample.py` 写入限定的[实验目录](results/4-4-workspace/)，[语法校验通过](results/4-4-valid-write.json)；无效 Python [被拦截](results/4-4-invalid-code.json)，`..\outside.py` [因越界被拒绝](results/4-4-escape-rejection.json)。只测试了文件写入这一局部能力，没有运行删除命令或外部系统变更。

作者的[正式活动](../../chapter4/execution-tools/validation/experiment_4_4/real_mcp_gui_20260802T093657Z/summary.json)通过 13/15 门禁，含终端、沙盒、长输出、浏览器、桌面与移动设备；真实日历和邮件写入缺凭据，故仍标为 `blocked`。其历史 GitHub PR 属于作者活动，本次没有新建 PR。

## 4-5：协作需要状态和授权

运行 `main.py list` 查看子 Agent、人工审批、通知等工具：[本机清单](results/4-5-tool-list.txt)。没有实际给任何人发消息、调用通知渠道或替用户自动批准操作。针对历史超时缺陷运行 `test_run_experiment_4_5.py`：初次 15/17 通过，两个 Windows 匿名管道测试因 `select()` 仅支持 socket 失败。修复为可超时的 Windows 管道轮询后，17/17 通过，另有 6 个子测试通过。作者[正式活动](../../chapter4/collaboration-tools/validation/experiment_4_5/real_mcp_human_20260803_v2/summary.json)已验证真人审批和子 Agent 生命周期，但真实邮件、IM、Slack 通知均未配置，仍为 `blocked`。

## 验证边界

本机的定向测试另包括 4-1 十项、4-2 五项、4-3 十二项、4-4 三项，加上 4-5 十七项，共 47 项通过。4-2 有一项要求创建符号链接的测试因 Windows 权限未执行。历史 5 份清单哈希均吻合，164 个声明文件中 163 个一致；唯一不符的旧符号链接目标详见[审计](results/historical-evidence-audit.json)。哈希核对不能替代授权后的真实外部操作。
