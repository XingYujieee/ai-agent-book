# 第 6 章｜实验记录

本次在 Windows 的项目 `.venv` 中执行。普通脚本与模型请求的命令、退出码、耗时和日志都保存在 `results/`。离线演示和测试通过，仅对应它们检查到的内容。

本机检查：10 组命令中 9 组退出成功；pytest 的末次汇总为 `{'passed': 62, 'failed': 1}`。首次失败日志保留在 `checks/*.attempt*.txt`，没有从统计中删掉失败后假装从未发生。

[检查汇总](results/check-summary.json) · [历史材料抽查](results/saved-evidence-review.json)

历史抽查固定在 Git 提交 `faa6db95`，每份 JSON 最多检查 40 个声明文件；使用原始 Git 字节，避免 Windows 换行影响。未能解析的旧路径、未跟踪产物和实际哈希差异会出现在报告中，因此这份抽查不是“所有历史验收重新通过”的证明。

## 本次真实运行

异步四场景第一次用了 0.05 秒 tick，真实长任务不足协议要求的三秒，只通过 8/9 门禁；[失败记录](results/subprocess-campaigns/local-20261025/summary.json)保留。恢复原协议的 0.15 秒 tick 后，[v2](results/subprocess-campaigns/local-20261025-v2/summary.json)通过 9/9。该活动检验真实子进程和脚本化调度，不包含新模型决策。

| 当前编号 | 实际运行 | 独立验证 |
| --- | --- | --- |
| 6-11 | 3 seeds × 3 object-counts × 256 episodes，共 2,304；各 cell 成功率 100% | [通过](results/gpu/6-11-validation.txt) |
| 6-13 | 3 seeds × 3 故障概率 × 3 模式 × 128，共 3,456 episodes | [通过](results/gpu/6-13-validation.txt) |
| 6-14 | 3 seeds × 4 训练条件 × 4,096 样本，10 epochs；目标域每种 1,024 例 | [通过](results/gpu/6-14-validation.txt) |

[运行命令、源码哈希和时间](results/gpu/summary.json)。显卡为 RTX 3070 Laptop GPU，PyTorch 2.11.0+cu128。原始源文件保留旧实验编号 6-10/6-12/6-13，与当前编号一一对应。所有动作都在自包含模拟器里，未驱动硬件。

RGB 三种子均值：干净训练在原域 92.74%、target_realistic 56.28%；完整随机化分别为 88.05%、75.46%。这次没有复现“完整随机化在所有目标域都优于所有单因素组”：appearance 的 target_realistic 为 75.55%，略高于 full，差距也需结合种子波动看。

## 6-1｜事件驱动的邮件处理 Agent

两秒定时器 mock 演示与邮件入口单测；没有真实邮件 OAuth/Unipile 凭据。

本机记录：[mailbox: passed](results/checks/mailbox.txt) · [演示 exit=0](results/demos/event-timer.txt)

历史材料：[保存的材料](../../chapter6/agent-with-event-trigger/validation/experiment_6_1/credential_probe_20260730T064500Z/manifest.json)。 Git 原始文件 SHA-256：`5b8befd016806b719bec1eca4ac3caa12067308b65cdee19e8ef358bd8f864c5`。

## 6-2｜带并行执行和打断能力的异步 Agent

运行真实子进程四场景及离线异步流程，具体门禁结果见实验记录。

本机记录：[async: passed](results/checks/async.txt) · [演示 exit=0](results/demos/async-demo.txt) · [四场景原始记录](results/subprocess-campaigns/local-20261025-v2/summary.json)

历史材料：[保存的材料](../../chapter6/async-agent/validation/experiment_6_2/real_subprocess_20260730T052500Z/manifest.json)。 Git 原始文件 SHA-256：`fff6b43a2e3a0b706fdd68bca289119f726d3f827f3f4d837e97321f7d48a825`。

## 6-3｜模型原生异步与回合中途引导

原生异步/steering 判定器单测；未新调用对应模型协议。

本机记录：[steering: passed](results/checks/steering.txt)

历史材料：[保存的材料](../../chapter6/astra-async-steering/validation/runs/exp6-14-20260905-formal/manifest.json)。 Git 原始文件 SHA-256：`bfece1666a63131e44c911908f4b0a07e6afffb719e8463b7507840d7d998c9e`。

## 6-4｜构建传统语音 Agent

阅读真实语音链路历史记录；未采集麦克风或新跑 ASR→LLM→TTS。

本机记录：本次只阅读了正文与入口，没有新运行回执。

历史材料：[保存的材料](../../chapter6/live-audio/backend/validation/real_pipeline_20260729_localwhisper_ark_fish/evidence.json)。 Git 原始文件 SHA-256：`8b8f3aa52a64f6013891e05ca8336f3f50048e2cb9590fbf4e91abf7f0240d62`。

## 6-5｜使用 Qwen2-Audio 模拟流式语音感知

本地机制测试；完整历史验证还引用本机没有的 Whisper/Qwen2-Audio 权重。

本机记录：[streaming: failed](results/checks/streaming.txt)

历史材料：[保存的材料](../../chapter6/streaming-speech/validation/runs/exp6-4-qwen2audio-whisper-provenance-20260730-v3/manifest.json)。 Git 原始文件 SHA-256：`3d02bce7ac422449bf29bdf61576377b44b9d7b8b046e2cd4f6a7e065f1da67b`。

## 6-6｜本地运行 MiniCPM-o 4.5，对比端到端与自级联

模型接口与证据校验单测；未新推理 MiniCPM-o。

本机记录：[speech: passed](results/checks/speech.txt)

历史材料：[保存的材料](../../chapter6/end-to-end-speech/validation/runs/exp6-5-minicpmo45-20260801-v1/evidence.json)。 Git 原始文件 SHA-256：`dcfe73476f96315252a13cc97457f5012c6dc4b047854a29da0bbad9fbe48e0f`。

## 6-7｜基于 Fish Audio 的控制标记驱动 TTS

Fish 接口与参数单测；未新生成/盲评 24 条真实语音。

本机记录：[tts: passed](results/checks/tts.txt)

历史材料：[保存的材料](../../chapter6/controllable-tts/validation/acceptance.json)。 Git 原始文件 SHA-256：`d64aad2fa73e7f8522c98c0b7a0a1bf08cbbcffdac0ded2a382ed744bb128f4d`。

## 6-8｜运行 Computer Use（Anthropic 参考路径或开放模型路径）

阅读作者原生 Computer Use 活动；缺对应服务凭据，未新跑。

本机记录：本次只阅读了正文与入口，没有新运行回执。

历史材料：[保存的材料](../../chapter6/claude-computer-use-native/validation/runs/exp6-7-anthropic-native-20260803-v2/acceptance.json)。 Git 原始文件 SHA-256：`fe7383ca9759200870ab61cb1a068b8ec32370feb5d4b2b7c1202aaac4bd7c33`。

## 6-9｜使用 browser-use 实现自动浏览器操作

开放模型入口配置与证据测试；未新调用视觉服务操作浏览器。

本机记录：[browser: passed](results/checks/browser.txt)

历史材料：[保存的材料](../../chapter6/computer-use-open-model/validation/latest.json)。 Git 原始文件 SHA-256：`306a1dd6e704c36457912d19a6887b80714f85b4df7732712671f249780712db`。

## 6-10｜真机遥操作 XLeRobot 整理桌面

真机遥操作需要 XLeRobot、校准和现场急停，本机没有设备。

本机记录：本次只阅读了正文与入口，没有新运行回执。

历史材料：无本次选定的完整证据文件。

## 6-11｜在模拟器中测量同任务的理想控制上限

自包含 GPU 模拟控制上限；本次运行状态见 GPU 回执。

本机记录：[teleop: passed](results/checks/teleop.txt) · [本次 GPU 证据](results/gpu/6-11/evidence.json) · [独立校验](results/gpu/6-11-validation.txt)

历史材料：[保存的材料](../../chapter6/xlerobot-teleoperation/validation/runs/local-gpu/evidence.json)。 Git 原始文件 SHA-256：`a71cb8d83a7890a02be6295952a1a452dcb618ecddfd036b80a7738ee797acbd`。

## 6-12｜使用 Gemini Robotics-ER 1.5 驱动 XLeRobot 自主整理桌面

自主真机运行需要 XLeRobot 与模型服务，本机没有设备。

本机记录：本次只阅读了正文与入口，没有新运行回执。

历史材料：无本次选定的完整证据文件。

## 6-13｜在模拟器中比较三种自主整理桌面的闭环

GPU 模拟比较开环、逐步检查和预测闭环；不代表真机已运行。

本机记录：[navigation: passed](results/checks/navigation.txt) · [本次 GPU 证据](results/gpu/6-13/evidence.json) · [独立校验](results/gpu/6-13-validation.txt)

历史材料：[保存的材料](../../chapter6/gemini-xlerobot-navigation/validation/runs/local-gpu/evidence.json)。 Git 原始文件 SHA-256：`4f6134fc0ef687830a0aee23c20e6670b2377456f7760ce983d76553c480e071`。

## 6-14｜同一桌面任务的 RGB 跨环境测试

GPU RGB 域变化实验；模拟域迁移不等于完成真实机械臂部署。

本机记录：[sim2real: passed](results/checks/sim2real.txt) · [本次 GPU 证据](results/gpu/6-14/evidence.json) · [独立校验](results/gpu/6-14-validation.txt)

历史材料：[保存的材料](../../chapter6/rgb-sim2real-grasping/validation/runs/local-gpu/evidence.json)。 Git 原始文件 SHA-256：`fc03af6fda9dc9e348e8b1bf6d606465316df51fe67554c477444108027dbe3c`。
