# 第 10 章｜实验记录

本次在 Windows 的项目 `.venv` 中执行。普通脚本与模型请求的命令、退出码、耗时和日志都保存在 `results/`。离线演示和测试通过，仅对应它们检查到的内容。

本机检查：6 组命令中 6 组退出成功；pytest 的末次汇总为 `{'passed': 72}`。首次失败日志保留在 `checks/*.attempt*.txt`，没有从统计中删掉失败后假装从未发生。

[检查汇总](results/check-summary.json) · [历史材料抽查](results/saved-evidence-review.json)

历史抽查固定在 Git 提交 `faa6db95`，每份 JSON 最多检查 40 个声明文件；使用原始 Git 字节，避免 Windows 换行影响。未能解析的旧路径、未跟踪产物和实际哈希差异会出现在报告中，因此这份抽查不是“所有历史验收重新通过”的证明。

## 离线协作检查

翻译预演只估算四角色的上下文与术语预算，不生成新译文。狼人杀的[本机报告](results/werewolf-offline.json)为 supplemental_only：信息隔离通过，完成两个完整循环，真实 LLM 策略未运行，音频回环为零。因此它没有达到完整语音狼人杀要求。

## 10-1｜共享上下文中的多角色转换——系统提示词与 Skill 的对比

角色清单与技能/角色编排测试；未重做 30 对在线任务和盲评。

本机记录：[roles: passed](results/checks/roles.txt) · [演示 exit=0](results/demos/roles-list.txt)

历史材料：[保存的材料](../../chapter10/multi-role-transfer/validation/comparison/runs/exp10-1-qwen35flash-20260809-v2/manifest.json)。 Git 原始文件 SHA-256：`0fc5c6276230fefdf16d5af4cb487f0c093dac49bbf4eb418cda826dd65db830`。

## 10-2｜书籍翻译 Agent

翻译 dry-run 与术语/审核参数测试；未新翻译整书。

本机记录：[translation: passed](results/checks/translation.txt) · [演示 exit=0](results/demos/translation-plan.txt)

历史材料：[保存的材料](../../chapter10/book-translation/validation/real_20260730T061500Z_v4/evidence.json)。 Git 原始文件 SHA-256：`9e765aa3d9b194346e1b9b5398018b99c369c2f8c79df231a433cc9e89ab1b5e`。

## 10-3｜自主编排的电话 + 电脑 Agent

注册编排与原始收据验收器测试；未拨号或提交外部表单。

本机记录：[registration: passed](results/checks/registration.txt)

历史材料：[保存的材料](../../chapter10/autonomous-phone-registration/validation/runs/exp10-3-webrtc-raw-20260731-v4/manifest.json)。 Git 原始文件 SHA-256：`496f212e2ddb8cfa68a8071f07832b9a8a2cbe9d9e0155d1d06c33c8f491a911`。

## 10-4｜同时从多个网站搜集信息的 Agent

取消、完成确认、重复消息测试；未新开十站真实在线并行搜索。

本机记录：[parallel: passed](results/checks/parallel.txt)

历史材料：[保存的材料](../../chapter10/parallel-web-research/validation/runs/exp10-4-real-receipts-20260730-v2/manifest.json)。 Git 原始文件 SHA-256：`da70764d5917f999a14d52f10cb147ce53c8c378853dd8dbc947b8d97bbfbc97`。

## 10-5｜运行斯坦福 AI 小镇

小镇存储/供应商适配等单测与历史资料核对；未新跑 25 人×三组×两虚拟日。

本机记录：[social: passed](results/checks/social.txt)

历史材料：[保存的材料](../../chapter10/generative-agents/validation/runs/exp10-5-qwen37flash-20260804-v1/acceptance.json)。 Git 原始文件 SHA-256：`a97f665b163f3e557809c1d9e9e5e8a2e01fb0f21f01ceb43dfc363bb00fb750`。

## 10-6｜语音狼人杀 Agent 系统

离线游戏信息隔离通过，2 个完整循环；无真实语音回环和 LLM 策略。

本机记录：[werewolf: passed](results/checks/werewolf.txt) · [演示 exit=0](results/demos/werewolf-offline.txt)

历史材料：[保存的材料](../../chapter10/voice-werewolf/validation/runs/exp10-6-simulated-user-openrouter-20260803-v11/acceptance_report.json)。 Git 原始文件 SHA-256：`190a2679c495410137e007accc3caeb7960a108bb165ca574674a725b72276a1`。
