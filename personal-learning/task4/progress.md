# Task 4 逐项进度

2026-10-25 的[补充记录](follow-up-20261025.md)已加入；17 项协作回归通过，私有服务与通知门禁仍缺配置。

更新日期：2026-10-21。下面列的是我本机做过的部分，以及作者留下的正式活动各自到了哪一步。原版门禁见 [Chapter 4 实验清单](../../chapter4/EXPERIMENT_LEDGER.md)。

| 实验 | 本次本机操作 | 证据与结果 | 原版门禁状态 |
| --- | --- | --- | --- |
| 4-1 主动工具发现 | 离线对比 126 个工具、8 任务、三策略 | [本机结果](results/4-1-offline.json)：全量 8/8、预筛 4/8、主动发现 8/8；注入 token 分别 93,040、8,236、7,796 | [作者正式运行](../../chapter4/active-tool-discovery/validation/experiment_4_1/rerun_20260825/summary.json) `passed`：Qwen3-4B 两组均 3/3，未观察到准确率提升 |
| 4-2 感知工具 MCP | 跑本地文件 grep、读取和知识库搜索的离线流程 | [本机日志](results/4-2-offline-log.txt)：grep 命中 5 处、知识库命中 1 个文件 | [历史活动](../../chapter4/perception-tools/validation/experiment_4_2/real_mcp_dashscope_intl_20260730T070000Z/summary.json) `blocked`：Google Calendar、Notion 缺授权 |
| 4-3 多模态三范式 | 本机生成[柱状图和 PDF](results/4-3-sample/)并检查文本层 | [样例分析](results/4-3-sample-analysis.json)：Q4 为 180M，四个精确图表数值都不在 PDF 文本层 | [历史正式对照](../../chapter4/multimodal-agent/validation/runs/20260729T185433Z-4_2-e028c9db/evidence.json) `passed`；本机未新调用视觉模型 |
| 4-4 执行工具 MCP | 在隔离工作目录验证合法文件、语法错误和越界路径 | [成功写入](results/4-4-valid-write.json)、[语法拦截](results/4-4-invalid-code.json)、[越界拦截](results/4-4-escape-rejection.json) | [历史活动](../../chapter4/execution-tools/validation/experiment_4_4/real_mcp_gui_20260802T093657Z/summary.json) 13/15 门禁；真实日历/邮件仍 `blocked` |
| 4-5 协作工具 MCP | 列出工具并测试 HITL 超时/拒绝/重复回复；修复 Windows 管道等待 | [工具清单](results/4-5-tool-list.txt)；相关 17 项测试通过 | [历史活动](../../chapter4/collaboration-tools/validation/experiment_4_5/real_mcp_human_20260803_v2/summary.json) `blocked`：真实邮件、即时消息、Slack 通知无配置；本次未发送任何通知 |

## 历史证据核对

[审计脚本](verify_history.py)按基线提交 `382d39d2` 的 Git 原始字节核对：[报告](results/historical-evidence-audit.json)中 5/5 份清单哈希一致，164 个声明文件中 163 个哈希一致。唯一例外是 4-2 的 `escape-link`：清单记录的是符号链接目标的 28 字节内容，而仓库保留的链接指向重编号前的绝对路径，不能按当前 Git 链接字节核验。其余文件一致只证明证据未变，不等于本机重新完成外部调用。

## 本机检查

4-1、4-2、4-3、4-4、4-5 的针对性测试合计 47 项通过；4-2 的一项符号链接逃逸测试因当前 Windows 用户没有创建符号链接权限而未运行。运行 4-5 测试时发现 Windows `select()` 不能等待匿名管道，已改用可超时轮询并复测通过。
