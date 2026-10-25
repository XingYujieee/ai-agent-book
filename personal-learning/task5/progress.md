# 第 5 章｜逐项进度

更新日期：2026-10-25。下面记我这次实际做的部分。作者以前的运行另列在“历史材料”里；文件能读到，只说明这份材料在当前 Git 快照中。

| 实验 | 本机操作与范围 | 回执 | 历史材料 |
| --- | --- | --- | --- |
| 5-1 跨厂商的轨迹接管 | 测试跨厂商轨迹的中立表示；未新调用三家服务。 | [handoff: passed](results/checks/handoff.txt) | [保存的材料](../../chapter5/provider-failover/validation/runs/exp5-1-handoff-20260824T150228Z/manifest.json) |
| 5-2 输出到一半断掉之后的接续 | 测试截断与接续逻辑；未重做真实流式断连活动。 | [handoff: passed](results/checks/handoff.txt) | [保存的材料](../../chapter5/provider-failover/validation/runs/exp5-2-continuation-20260824T152045Z/manifest.json) |
| 5-3 使用代码生成工具提升数学解题能力 | 测试 AIME 数据与活动门禁；未新跑 30 题双模型调用臂。 | [math: passed](results/checks/math.txt) | [保存的材料](../../chapter5/code-for-math/validation/runs/exp5-1-ark-doubao-flash-aime2024-20260730-v1/manifest.json) |
| 5-4 使用代码生成工具提升逻辑思考能力 | 离线 CSP 12/12；模型把题意翻译成约束的双臂实验仍未新跑。 | [logic: passed](results/checks/logic.txt) · [logic-random: passed](results/checks/logic-random.txt) · [演示 exit=0](results/demos/logic-solver.txt) | [保存的材料](../../chapter5/code-for-logic/validation/real_ark_doubao_flash_hf84_20260730.json) |
| 5-5 小模型通过代码化知识提升执行规则的准确性 | 规则环境与配对统计测试；当前本机不是作者的 4B 60×2 活动。 | [rules: passed](results/checks/rules.txt) | [保存的材料](../../chapter5/small-model-codified-rules/validation/real_ollama_qwen3_4b_60x2_20260730.json) |
| 5-6 基于论文的 PPT 自动生成 | 测试页数/空审核结果处理；未新生成并独立盲评两套论文幻灯片。 | [slides: passed](results/checks/slides.txt) | [保存的材料](../../chapter5/paper-to-ppt/validation/runs/exp5-4-real-pdf-both-20260730-v9/comparison_summary.json) |
| 5-7 论文讲解视频的自动生成 | 测试视频合成与时长处理；未新合成真实讲解语音。 | [video: passed](results/checks/video.txt) | [保存的材料](../../chapter5/paper-to-video/validation/runs/exp5-5-kimi-fish-qwen-20260730-v1/manifest.json) |
| 5-8 基于 API 的智能视频剪辑 | ffmpeg 生成并剪辑约 5 秒素材，生成 bpy 脚本；未运行 Blender/Vision 闭环。 | [editing: passed](results/checks/editing.txt) · [演示 exit=0](results/demos/video-smoke.txt) | [保存的材料](../../chapter5/video-edit/validation/runs/exp5-6-real-blender-20260730-055102/manifest.json) |
| 5-9 同一个零件的两种生成路线——代码与生成模型 | 测量真实 STL fixture 并测试缺孔反例；未新调用生成式 3D 服务。 | [cad: passed](results/checks/cad.txt) | [保存的材料](../../chapter5/cad-vs-diffusion/validation/runs/exp5-7-cad-vs-diffusion-20260821-015734-v1/manifest.json) |
| 5-10 自适应的日志解析系统 | 预置解析器完成新格式安装、测试和复用；不是现场 LLM 代码生成。 | [演示 exit=0](results/demos/log-parser.txt) | [保存的材料](../../chapter5/adaptive-log-parser/validation/runs/20260729T212342Z-5_7-live/manifest.json) |
| 5-11 生产日志的智能诊断系统 | 诊断编排与回放单测；未向 GitHub 创建外部 Issue。 | [diagnosis: passed](results/checks/diagnosis.txt) | [保存的材料](../../chapter5/log-diagnosis/validation/runs/exp5-8-live-http-mcp-20260730-053403/manifest.json) |
| 5-12 动态表单生成的意图澄清系统 | 生成可打开的级联 HTML，校验并模拟提交 JSON；未真实订票。 | [form: passed](results/checks/form.txt) · [演示 exit=0](results/demos/dynamic-form.txt) | [保存的材料](../../chapter5/dynamic-form/validation/runs/20260729T212542Z-5_9-live-browser/manifest.json) |
| 5-13 自然语言交互的 ERP Agent | SQL 解析相关单测；未建立真实 PostgreSQL 的新端到端模型活动。 | [erp: passed](results/checks/erp.txt) | [保存的材料](../../chapter5/erp-agent/validation/runs/20260729T210334Z-5_10-postgresql/manifest.json) |
| 5-14 对话式界面定制系统 | 测试生成结果的参数容错；未新调用模型修改 React 并验收 HMR。 | [ui: passed](results/checks/ui.txt) | [保存的材料](../../chapter5/conversational-ui/validation/runs/20260729T212933Z-5_11-hmr/manifest.json) |
| 5-15 动态生成软件的权限内嵌数据对象 | 阅读数据层权限和测试；缺 PostgreSQL 测试库，未执行数据库演示。 | 源码/说明核对 | 无本次选定的完整证据文件 |
| 5-16 开发一个能创造 Agent 的 Agent | Agent 创建器单测；清单引用的历史 comparison.json 未被当前 Git 跟踪。 | [creator: passed](results/checks/creator.txt) | 未取得对应 Git 文件 |
