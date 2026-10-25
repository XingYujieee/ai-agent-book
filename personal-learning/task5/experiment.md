# 第 5 章｜实验记录

本次在 Windows 的项目 `.venv` 中执行。普通脚本与模型请求的命令、退出码、耗时和日志都保存在 `results/`。离线演示和测试通过，仅对应它们检查到的内容。

本机检查：14 组命令中 14 组退出成功；pytest 的末次汇总为 `{'passed': 130}`。首次失败日志保留在 `checks/*.attempt*.txt`，没有从统计中删掉失败后假装从未发生。

[检查汇总](results/check-summary.json) · [历史材料抽查](results/saved-evidence-review.json)

历史抽查固定在 Git 提交 `faa6db95`，每份 JSON 最多检查 40 个声明文件；使用原始 Git 字节，避免 Windows 换行影响。未能解析的旧路径、未跟踪产物和实际哈希差异会出现在报告中，因此这份抽查不是“所有历史验收重新通过”的证明。

## 本次可打开的产物

[级联表单](results/flight-form.html) · [视频剪辑](results/edit-smoke.mp4) · [剪辑抽帧](results/edit-smoke-frame.png) · [逐题 CSP 结果](results/logic-solver.json) · [混合日志解析](results/parsed-logs.jsonl)

CSP 的 12/12 使用直接给定的结构化约束，不包含模型翻译题意。视频约 5.03 秒，实际后端是 ffmpeg；生成的 bpy 脚本没有经 Blender 执行。日志演示安装的是预置函数。

## 5-1｜跨厂商的轨迹接管

测试跨厂商轨迹的中立表示；未新调用三家服务。

本机记录：[handoff: passed](results/checks/handoff.txt)

历史材料：[保存的材料](../../chapter5/provider-failover/validation/runs/exp5-1-handoff-20260824T150228Z/manifest.json)。 Git 原始文件 SHA-256：`102f27e469fcc020667be93eec0e16d84dec7f454244a147401fd4f932b242be`。

## 5-2｜输出到一半断掉之后的接续

测试截断与接续逻辑；未重做真实流式断连活动。

本机记录：[handoff: passed](results/checks/handoff.txt)

历史材料：[保存的材料](../../chapter5/provider-failover/validation/runs/exp5-2-continuation-20260824T152045Z/manifest.json)。 Git 原始文件 SHA-256：`c513b9e8265c4ce4eaf1bb0e6f082c68f756d1cff6e7784cf13ea923357605f4`。

## 5-3｜使用代码生成工具提升数学解题能力

测试 AIME 数据与活动门禁；未新跑 30 题双模型调用臂。

本机记录：[math: passed](results/checks/math.txt)

历史材料：[保存的材料](../../chapter5/code-for-math/validation/runs/exp5-1-ark-doubao-flash-aime2024-20260730-v1/manifest.json)。 Git 原始文件 SHA-256：`3f4508457ae620efdb8864ed52ef150d3e584da128f2249ca18553904d6f571a`。

## 5-4｜使用代码生成工具提升逻辑思考能力

离线 CSP 12/12；模型把题意翻译成约束的双臂实验仍未新跑。

本机记录：[logic: passed](results/checks/logic.txt) · [logic-random: passed](results/checks/logic-random.txt) · [演示 exit=0](results/demos/logic-solver.txt)

历史材料：[保存的材料](../../chapter5/code-for-logic/validation/real_ark_doubao_flash_hf84_20260730.json)。 Git 原始文件 SHA-256：`ac602aebf67e9b2ee508f3472f4348fd7c30edd05098fed8cbc6ebef15d2df28`。

## 5-5｜小模型通过代码化知识提升执行规则的准确性

规则环境与配对统计测试；当前本机不是作者的 4B 60×2 活动。

本机记录：[rules: passed](results/checks/rules.txt)

历史材料：[保存的材料](../../chapter5/small-model-codified-rules/validation/real_ollama_qwen3_4b_60x2_20260730.json)。 Git 原始文件 SHA-256：`003c8e0593623b700a173b463199ae080a6c7bcbcedce1f5568d579515da66ab`。

## 5-6｜基于论文的 PPT 自动生成

测试页数/空审核结果处理；未新生成并独立盲评两套论文幻灯片。

本机记录：[slides: passed](results/checks/slides.txt)

历史材料：[保存的材料](../../chapter5/paper-to-ppt/validation/runs/exp5-4-real-pdf-both-20260730-v9/comparison_summary.json)。 Git 原始文件 SHA-256：`bfd913d311ab4d6ad5a8cae93b61ce54ce6d19f9d2d10ee2afdef06becd1e09f`。

## 5-7｜论文讲解视频的自动生成

测试视频合成与时长处理；未新合成真实讲解语音。

本机记录：[video: passed](results/checks/video.txt)

历史材料：[保存的材料](../../chapter5/paper-to-video/validation/runs/exp5-5-kimi-fish-qwen-20260730-v1/manifest.json)。 Git 原始文件 SHA-256：`93bb69a916a76d12de56270928971f6e39f47755214f7a135817d7effd8b3f09`。

## 5-8｜基于 API 的智能视频剪辑

ffmpeg 生成并剪辑约 5 秒素材，生成 bpy 脚本；未运行 Blender/Vision 闭环。

本机记录：[editing: passed](results/checks/editing.txt) · [演示 exit=0](results/demos/video-smoke.txt)

历史材料：[保存的材料](../../chapter5/video-edit/validation/runs/exp5-6-real-blender-20260730-055102/manifest.json)。 Git 原始文件 SHA-256：`fd044738e812faa832863f4c112880a9583c268afb7d08f388c00623498ab7a8`。

## 5-9｜同一个零件的两种生成路线——代码与生成模型

测量真实 STL fixture 并测试缺孔反例；未新调用生成式 3D 服务。

本机记录：[cad: passed](results/checks/cad.txt)

历史材料：[保存的材料](../../chapter5/cad-vs-diffusion/validation/runs/exp5-7-cad-vs-diffusion-20260821-015734-v1/manifest.json)。 Git 原始文件 SHA-256：`ae7c5fdf685562e5e53ac625fe1b512b6ba7a8692bbc45bada888b555c702b86`。

## 5-10｜自适应的日志解析系统

预置解析器完成新格式安装、测试和复用；不是现场 LLM 代码生成。

本机记录：[演示 exit=0](results/demos/log-parser.txt)

历史材料：[保存的材料](../../chapter5/adaptive-log-parser/validation/runs/20260729T212342Z-5_7-live/manifest.json)。 Git 原始文件 SHA-256：`00851a7b15fba8bad94422b7870b9eda1a9f3b12f3e509b2d768db244edc2507`。

## 5-11｜生产日志的智能诊断系统

诊断编排与回放单测；未向 GitHub 创建外部 Issue。

本机记录：[diagnosis: passed](results/checks/diagnosis.txt)

历史材料：[保存的材料](../../chapter5/log-diagnosis/validation/runs/exp5-8-live-http-mcp-20260730-053403/manifest.json)。 Git 原始文件 SHA-256：`68e09e7c8b4fc100e0612a6f81978079c393a822025bfa794b6dda85134a5813`。

## 5-12｜动态表单生成的意图澄清系统

生成可打开的级联 HTML，校验并模拟提交 JSON；未真实订票。

本机记录：[form: passed](results/checks/form.txt) · [演示 exit=0](results/demos/dynamic-form.txt)

历史材料：[保存的材料](../../chapter5/dynamic-form/validation/runs/20260729T212542Z-5_9-live-browser/manifest.json)。 Git 原始文件 SHA-256：`6e6b2cc9c31071c880f2c66a7f172d4933a1ee2f51ac7206b89a1cd89dca08a7`。

## 5-13｜自然语言交互的 ERP Agent

SQL 解析相关单测；未建立真实 PostgreSQL 的新端到端模型活动。

本机记录：[erp: passed](results/checks/erp.txt)

历史材料：[保存的材料](../../chapter5/erp-agent/validation/runs/20260729T210334Z-5_10-postgresql/manifest.json)。 Git 原始文件 SHA-256：`5b167f34d18cca867b6fa5fe2d61cd1bf4324f618d6e21221fe9131e56aaed16`。

## 5-14｜对话式界面定制系统

测试生成结果的参数容错；未新调用模型修改 React 并验收 HMR。

本机记录：[ui: passed](results/checks/ui.txt)

历史材料：[保存的材料](../../chapter5/conversational-ui/validation/runs/20260729T212933Z-5_11-hmr/manifest.json)。 Git 原始文件 SHA-256：`34d6d8f325ac598b8e55a8a93763dda2bdb019020aa0cf67aa421e861be9279c`。

## 5-15｜动态生成软件的权限内嵌数据对象

阅读数据层权限和测试；缺 PostgreSQL 测试库，未执行数据库演示。

本机记录：本次只阅读了正文与入口，没有新运行回执。

历史材料：无本次选定的完整证据文件。

## 5-16｜开发一个能创造 Agent 的 Agent

Agent 创建器单测；清单引用的历史 comparison.json 未被当前 Git 跟踪。

本机记录：[creator: passed](results/checks/creator.txt)

历史材料：未取得对应 Git 文件。
