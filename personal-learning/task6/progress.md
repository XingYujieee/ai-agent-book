# 第 6 章｜逐项进度

更新日期：2026-10-25。下面记我这次实际做的部分。作者以前的运行另列在“历史材料”里；文件能读到，只说明这份材料在当前 Git 快照中。

| 实验 | 本机操作与范围 | 回执 | 历史材料 |
| --- | --- | --- | --- |
| 6-1 事件驱动的邮件处理 Agent | 两秒定时器 mock 演示与邮件入口单测；没有真实邮件 OAuth/Unipile 凭据。 | [mailbox: passed](results/checks/mailbox.txt) · [演示 exit=0](results/demos/event-timer.txt) | [保存的材料](../../chapter6/agent-with-event-trigger/validation/experiment_6_1/credential_probe_20260730T064500Z/manifest.json) |
| 6-2 带并行执行和打断能力的异步 Agent | 运行真实子进程四场景及离线异步流程，具体门禁结果见实验记录。 | [async: passed](results/checks/async.txt) · [演示 exit=0](results/demos/async-demo.txt) · [四场景原始记录](results/subprocess-campaigns/local-20261025-v2/summary.json) | [保存的材料](../../chapter6/async-agent/validation/experiment_6_2/real_subprocess_20260730T052500Z/manifest.json) |
| 6-3 模型原生异步与回合中途引导 | 原生异步/steering 判定器单测；未新调用对应模型协议。 | [steering: passed](results/checks/steering.txt) | [保存的材料](../../chapter6/astra-async-steering/validation/runs/exp6-14-20260905-formal/manifest.json) |
| 6-4 构建传统语音 Agent | 阅读真实语音链路历史记录；未采集麦克风或新跑 ASR→LLM→TTS。 | 源码/说明核对 | [保存的材料](../../chapter6/live-audio/backend/validation/real_pipeline_20260729_localwhisper_ark_fish/evidence.json) |
| 6-5 使用 Qwen2-Audio 模拟流式语音感知 | 本地机制测试；完整历史验证还引用本机没有的 Whisper/Qwen2-Audio 权重。 | [streaming: failed](results/checks/streaming.txt) | [保存的材料](../../chapter6/streaming-speech/validation/runs/exp6-4-qwen2audio-whisper-provenance-20260730-v3/manifest.json) |
| 6-6 本地运行 MiniCPM-o 4.5，对比端到端与自级联 | 模型接口与证据校验单测；未新推理 MiniCPM-o。 | [speech: passed](results/checks/speech.txt) | [保存的材料](../../chapter6/end-to-end-speech/validation/runs/exp6-5-minicpmo45-20260801-v1/evidence.json) |
| 6-7 基于 Fish Audio 的控制标记驱动 TTS | Fish 接口与参数单测；未新生成/盲评 24 条真实语音。 | [tts: passed](results/checks/tts.txt) | [保存的材料](../../chapter6/controllable-tts/validation/acceptance.json) |
| 6-8 运行 Computer Use（Anthropic 参考路径或开放模型路径） | 阅读作者原生 Computer Use 活动；缺对应服务凭据，未新跑。 | 源码/说明核对 | [保存的材料](../../chapter6/claude-computer-use-native/validation/runs/exp6-7-anthropic-native-20260803-v2/acceptance.json) |
| 6-9 使用 browser-use 实现自动浏览器操作 | 开放模型入口配置与证据测试；未新调用视觉服务操作浏览器。 | [browser: passed](results/checks/browser.txt) | [保存的材料](../../chapter6/computer-use-open-model/validation/latest.json) |
| 6-10 真机遥操作 XLeRobot 整理桌面 | 真机遥操作需要 XLeRobot、校准和现场急停，本机没有设备。 | 源码/说明核对 | 无本次选定的完整证据文件 |
| 6-11 在模拟器中测量同任务的理想控制上限 | 自包含 GPU 模拟控制上限；本次运行状态见 GPU 回执。 | [teleop: passed](results/checks/teleop.txt) · [本次 GPU 证据](results/gpu/6-11/evidence.json) · [独立校验](results/gpu/6-11-validation.txt) | [保存的材料](../../chapter6/xlerobot-teleoperation/validation/runs/local-gpu/evidence.json) |
| 6-12 使用 Gemini Robotics-ER 1.5 驱动 XLeRobot 自主整理桌面 | 自主真机运行需要 XLeRobot 与模型服务，本机没有设备。 | 源码/说明核对 | 无本次选定的完整证据文件 |
| 6-13 在模拟器中比较三种自主整理桌面的闭环 | GPU 模拟比较开环、逐步检查和预测闭环；不代表真机已运行。 | [navigation: passed](results/checks/navigation.txt) · [本次 GPU 证据](results/gpu/6-13/evidence.json) · [独立校验](results/gpu/6-13-validation.txt) | [保存的材料](../../chapter6/gemini-xlerobot-navigation/validation/runs/local-gpu/evidence.json) |
| 6-14 同一桌面任务的 RGB 跨环境测试 | GPU RGB 域变化实验；模拟域迁移不等于完成真实机械臂部署。 | [sim2real: passed](results/checks/sim2real.txt) · [本次 GPU 证据](results/gpu/6-14/evidence.json) · [独立校验](results/gpu/6-14-validation.txt) | [保存的材料](../../chapter6/rgb-sim2real-grasping/validation/runs/local-gpu/evidence.json) |
