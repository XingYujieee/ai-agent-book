# 第 9 章｜逐项进度

更新日期：2026-10-25。下面记我这次实际做的部分。作者以前的运行另列在“历史材料”里；文件能读到，只说明这份材料在当前 Git 快照中。

| 实验 | 本机操作与范围 | 回执 | 历史材料 |
| --- | --- | --- | --- |
| 9-1 为客服 Agent 构建轨迹验证器 | 启发式三层 verifier 跑四条轨迹；不是本次真实 LLM Judge 校准。 | [verifier: passed](results/checks/verifier.txt) · [演示 exit=0](results/demos/trajectory-verifier.txt) | [保存的材料](../../chapter9/trajectory-verifier/validation/real_20260729T165247Z/evidence.json) |
| 9-2 从 τ²-bench 失败轨迹提炼转接与工具使用规则 | 阅读失败提炼及迁移集历史活动；未新跑 τ²-bench 三臂。 | 源码/说明核对 | [保存的材料](../../chapter9/tau2-escalation-experience/validation/evidence.json) |
| 9-3 基于失败轨迹优化航空客服的系统 Prompt | 配置预演和补丁/发布门禁单测；未新跑任务 Agent、Judge、Coding Agent。 | [prompt: passed](results/checks/prompt.txt) · [演示 exit=0](results/demos/prompt-plan.txt) | [保存的材料](../../chapter9/prompt-auto-optimization/validation/latest.json) |
| 9-4 从用户反馈中进化需求澄清与 Spec 确认 Skill | 本机 qwen3:0.6b 三臂各六题：3/6、2/6、4/6；非完整用户反馈长期活动。 | [18 次实际本地请求](results/clarification-trial/summary.json) | 无本次选定的完整证据文件 |
| 9-5 从浏览器轨迹生成可验证工作流 | 离线状态谓词、候选回放、页面变化失效演示；不是新浏览器在线学习。 | [rpa: passed](results/checks/rpa.txt) · [演示 exit=0](results/demos/rpa-replay.txt) | [保存的材料](../../chapter9/browser-use-rpa/validation/latest.json) |
| 9-6 由失败轨迹触发 Agent 自我修改 | 核对隔离补丁、回归与回滚设计；缺 Docker，未运行任意候选代码。 | 源码/说明核对 | [保存的材料](../../chapter9/self-modifying-agent/validation/latest.json) |
| 9-7 由用户反馈触发高风险操作确认门禁 | quick 模式接受确定性提案、拒绝过宽反例；修复跨平台路径识别并测过。 | [safety: passed](results/checks/safety.txt) · [演示 exit=0](results/demos/safety-gate.txt) | [保存的材料](../../chapter9/harness-safety-gate/validation/latest.json) |
| 9-8 把这本书交给 Hermes：它能升级自己吗？ | 核对 Hermes 历史活动；缺少其运行环境与模型服务，未执行新的自身代码更新。 | 源码/说明核对 | [保存的材料](../../chapter9/hermes-self-evolution/validation/exp9-8-hermes-gpt56luna-autonomous-20260802-v2/manifest.json) |
| 9-9 评估 Agent 是否在持续进化 | 运行三种确定性参考策略并检查统计；没有 126 次新的在线模型活动。 | [evolution: passed](results/checks/evolution.txt) · [演示 exit=0](results/demos/evolution-reference.txt) | [保存的材料](../../chapter9/self-evolution-eval/validation/latest.json) |
