# 第 9 章｜实验记录

本次在 Windows 的项目 `.venv` 中执行。普通脚本与模型请求的命令、退出码、耗时和日志都保存在 `results/`。离线演示和测试通过，仅对应它们检查到的内容。

本机检查：5 组命令中 5 组退出成功；pytest 的末次汇总为 `{'passed': 73}`。首次失败日志保留在 `checks/*.attempt*.txt`，没有从统计中删掉失败后假装从未发生。

[检查汇总](results/check-summary.json) · [历史材料抽查](results/saved-evidence-review.json)

历史抽查固定在 Git 提交 `faa6db95`，每份 JSON 最多检查 40 个声明文件；使用原始 Git 字节，避免 Windows 换行影响。未能解析的旧路径、未跟踪产物和实际哈希差异会出现在报告中，因此这份抽查不是“所有历史验收重新通过”的证明。

## 9-4 的本机补充

| 提示条件 | 正确决策 | API 错误 |
| --- | ---: | ---: |
| baseline | 3/6 | 0 |
| append_feedback | 2/6 | 0 |
| scoped_skill | 4/6 | 0 |

固定 qwen3:0.6b、temperature=0、seed=42、think=false，三组使用相同六题；[协议和逐次原始响应](results/clarification-trial/)全部保留。只测 ask/confirm_spec/execute 的下一步选择，没有真正执行用户任务；样本与 Skill 是本次设计的，不能推断稳定的真实用户收益。Skill 组仍对范围明确的小修改和只读请求过度确认。

[安全门禁 quick](results/demos/safety-gate.txt)没有执行外部删除或推送，执行器是验证器提供的内存模拟器。

## 9-1｜为客服 Agent 构建轨迹验证器

启发式三层 verifier 跑四条轨迹；不是本次真实 LLM Judge 校准。

本机记录：[verifier: passed](results/checks/verifier.txt) · [演示 exit=0](results/demos/trajectory-verifier.txt)

历史材料：[保存的材料](../../chapter9/trajectory-verifier/validation/real_20260729T165247Z/evidence.json)。 Git 原始文件 SHA-256：`4365122d36f543e967026fe123c2de17e9ebd99ac9ddd696b4ac06f99c56068c`。

## 9-2｜从 τ²-bench 失败轨迹提炼转接与工具使用规则

阅读失败提炼及迁移集历史活动；未新跑 τ²-bench 三臂。

本机记录：本次只阅读了正文与入口，没有新运行回执。

历史材料：[保存的材料](../../chapter9/tau2-escalation-experience/validation/evidence.json)。 Git 原始文件 SHA-256：`f1a490f35e6d83994b56de8db01618a2b77cd3bfdf503b590675f4c9e13025e1`。

## 9-3｜基于失败轨迹优化航空客服的系统 Prompt

配置预演和补丁/发布门禁单测；未新跑任务 Agent、Judge、Coding Agent。

本机记录：[prompt: passed](results/checks/prompt.txt) · [演示 exit=0](results/demos/prompt-plan.txt)

历史材料：[保存的材料](../../chapter9/prompt-auto-optimization/validation/latest.json)。 Git 原始文件 SHA-256：`cbcf05add7228f02442155583c77cb1adce8f5a91926d10c3690d6d00332646a`。

## 9-4｜从用户反馈中进化需求澄清与 Spec 确认 Skill

本机 qwen3:0.6b 三臂各六题：3/6、2/6、4/6；非完整用户反馈长期活动。

本机记录：[18 次实际本地请求](results/clarification-trial/summary.json)

历史材料：无本次选定的完整证据文件。

## 9-5｜从浏览器轨迹生成可验证工作流

离线状态谓词、候选回放、页面变化失效演示；不是新浏览器在线学习。

本机记录：[rpa: passed](results/checks/rpa.txt) · [演示 exit=0](results/demos/rpa-replay.txt)

历史材料：[保存的材料](../../chapter9/browser-use-rpa/validation/latest.json)。 Git 原始文件 SHA-256：`5465dc76f12e53da24f8655d3a53c290d50db723511af25f5ca945a16f9ce0fb`。

## 9-6｜由失败轨迹触发 Agent 自我修改

核对隔离补丁、回归与回滚设计；缺 Docker，未运行任意候选代码。

本机记录：本次只阅读了正文与入口，没有新运行回执。

历史材料：[保存的材料](../../chapter9/self-modifying-agent/validation/latest.json)。 Git 原始文件 SHA-256：`ed1ca773ff7313a5c61e4a098a99a153940d7c08757e210391d918c4ec399eae`。

## 9-7｜由用户反馈触发高风险操作确认门禁

quick 模式接受确定性提案、拒绝过宽反例；修复跨平台路径识别并测过。

本机记录：[safety: passed](results/checks/safety.txt) · [演示 exit=0](results/demos/safety-gate.txt)

历史材料：[保存的材料](../../chapter9/harness-safety-gate/validation/latest.json)。 Git 原始文件 SHA-256：`f7cf31dc5072b0e185b1f267d9cf8600b07dc5301a28eec3f01ff572076c3027`。

## 9-8｜把这本书交给 Hermes：它能升级自己吗？

核对 Hermes 历史活动；缺少其运行环境与模型服务，未执行新的自身代码更新。

本机记录：本次只阅读了正文与入口，没有新运行回执。

历史材料：[保存的材料](../../chapter9/hermes-self-evolution/validation/exp9-8-hermes-gpt56luna-autonomous-20260802-v2/manifest.json)。 Git 原始文件 SHA-256：`1bcdff99e3346dcab78613b24c9c499e8146420d4ad93cfc11cede427b801c77`。

## 9-9｜评估 Agent 是否在持续进化

运行三种确定性参考策略并检查统计；没有 126 次新的在线模型活动。

本机记录：[evolution: passed](results/checks/evolution.txt) · [演示 exit=0](results/demos/evolution-reference.txt)

历史材料：[保存的材料](../../chapter9/self-evolution-eval/validation/latest.json)。 Git 原始文件 SHA-256：`1d24ee2ded4e2e189e7fc15b9a902c13370e3316205009f4fae8593169b6c105`。
