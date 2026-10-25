"""Build factual per-experiment tables from the retained local receipts."""
from __future__ import annotations
import json
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[1]
HOME=ROOT/'personal-learning'
LABELS={5:'代码生成与 Coding Agent',6:'交互与异步',7:'评估',8:'模型后训练',9:'持续进化',10:'多 Agent 协作'}
CHECKS={
5:{1:['handoff'],2:['handoff'],3:['math'],4:['logic','logic-random'],5:['rules'],6:['slides'],7:['video'],8:['editing'],9:['cad'],11:['diagnosis'],12:['form'],13:['erp'],14:['ui'],16:['creator']},
6:{1:['mailbox'],2:['async'],3:['steering'],5:['streaming'],6:['speech'],7:['tts'],9:['browser'],11:['teleop'],13:['navigation'],14:['sim2real']},
7:{3:['rubric'],4:['rubric'],5:['tts-judge'],7:['policy'],8:['elo'],9:['action'],10:['cost'],11:['benchmark'],12:['rubric'],13:['android'],14:['robot-eval']},
8:{8:['prompt-distillation'],9:['cot'],17:['dpo'],18:['quotes'],19:['copy'],6:['speech-sft']},
9:{1:['verifier'],3:['prompt'],5:['rpa'],7:['safety'],9:['evolution']},
10:{1:['roles'],2:['translation'],3:['registration'],4:['parallel'],5:['social'],6:['werewolf']}}
DEMOS={5:{4:'logic-solver',8:'video-smoke',10:'log-parser',12:'dynamic-form'},6:{1:'event-timer',2:'async-demo'},7:{10:'cost-analysis'},8:{17:'dpo-mock'},9:{1:'trajectory-verifier',3:'prompt-plan',5:'rpa-replay',7:'safety-gate',9:'evolution-reference'},10:{1:'roles-list',2:'translation-plan',6:'werewolf-offline'}}
NOTES={
'5-1':'测试跨厂商轨迹的中立表示；未新调用三家服务。','5-2':'测试截断与接续逻辑；未重做真实流式断连活动。',
'5-3':'测试 AIME 数据与活动门禁；未新跑 30 题双模型调用臂。','5-4':'离线 CSP 12/12；模型把题意翻译成约束的双臂实验仍未新跑。',
'5-5':'规则环境与配对统计测试；当前本机不是作者的 4B 60×2 活动。','5-6':'测试页数/空审核结果处理；未新生成并独立盲评两套论文幻灯片。',
'5-7':'测试视频合成与时长处理；未新合成真实讲解语音。','5-8':'ffmpeg 生成并剪辑约 5 秒素材，生成 bpy 脚本；未运行 Blender/Vision 闭环。',
'5-9':'测量真实 STL fixture 并测试缺孔反例；未新调用生成式 3D 服务。','5-10':'预置解析器完成新格式安装、测试和复用；不是现场 LLM 代码生成。',
'5-11':'诊断编排与回放单测；未向 GitHub 创建外部 Issue。','5-12':'生成可打开的级联 HTML，校验并模拟提交 JSON；未真实订票。',
'5-13':'SQL 解析相关单测；未建立真实 PostgreSQL 的新端到端模型活动。','5-14':'测试生成结果的参数容错；未新调用模型修改 React 并验收 HMR。',
'5-15':'阅读数据层权限和测试；缺 PostgreSQL 测试库，未执行数据库演示。','5-16':'Agent 创建器单测；清单引用的历史 comparison.json 未被当前 Git 跟踪。',
'6-1':'两秒定时器 mock 演示与邮件入口单测；没有真实邮件 OAuth/Unipile 凭据。',
'6-2':'运行真实子进程四场景及离线异步流程，具体门禁结果见实验记录。','6-3':'原生异步/steering 判定器单测；未新调用对应模型协议。',
'6-4':'阅读真实语音链路历史记录；未采集麦克风或新跑 ASR→LLM→TTS。','6-5':'本地机制测试；完整历史验证还引用本机没有的 Whisper/Qwen2-Audio 权重。',
'6-6':'模型接口与证据校验单测；未新推理 MiniCPM-o。','6-7':'Fish 接口与参数单测；未新生成/盲评 24 条真实语音。',
'6-8':'阅读作者原生 Computer Use 活动；缺对应服务凭据，未新跑。','6-9':'开放模型入口配置与证据测试；未新调用视觉服务操作浏览器。',
'6-10':'真机遥操作需要 XLeRobot、校准和现场急停，本机没有设备。','6-11':'自包含 GPU 模拟控制上限；本次运行状态见 GPU 回执。',
'6-12':'自主真机运行需要 XLeRobot 与模型服务，本机没有设备。','6-13':'GPU 模拟比较开环、逐步检查和预测闭环；不代表真机已运行。',
'6-14':'GPU RGB 域变化实验；模拟域迁移不等于完成真实机械臂部署。',
'7-1':'复核 τ²-bench 保存的活动；未新启动完整客服 benchmark。','7-2':'阅读作者 18 项人工任务记录；未将其计作本人的新人工操作。',
'7-3':'Rubric 与评估框架测试；清单列出的完整报告未随当前快照提供。','7-4':'评估框架测试；未新跑同一 60 题三策略真实模型比较。',
'7-5':'阅读真实音频盲评活动；未新生成多供应商音频。','7-6':'读取失败归因、轨迹和前缀回归资料；未新跑 AndroidWorld。',
'7-7':'格式化与记忆边界测试；修复工作区换行后历史哈希测试通过。','7-8':'复核 Arena 排名活动资料；未重新下载 2 GB 投票快照跑全量。',
'7-9':'固定 Harness 的任务设计与指标测试；未新调用不同厂商各 9 次。','7-10':'从保存的四组真实用量复算成本；价格为脚本假设，不是本次账单。',
'7-11':'活动门禁单测；缺 N≥100 全矩阵、限流爬坡和连续 168 小时记录。','7-12':'核对现有 1,440 单元矩阵及框架；未重新调用全部模型。',
'7-13':'Android 评估器单测和历史资料核对；未运行 580 次新 episode。','7-14':'修复缺失路径的预检错误并测试；没有重建 OpenVLA/RoboTwin2 权重与模拟器。',
'8-1':'本机实际训练 10,000 轮，固定 seed=42，100 轮贪心评估 100/100，平均 12 步。','8-2':'阅读 Kimi 的历史调用；本次未新跑同环境的 LLM 比较。',
'8-3':'阅读、抽查 MiniMind 历史训练报告；未在本机重训六组。','8-4':'阅读 VLM 对齐/SFT 报告；未下载 CLIP/训练数据重训。',
'8-5':'核对韩语继续预训练报告；未重新训练和做英语保留集。','8-6':'语音 SFT 的分析/契约测试；未新训练语音 LoRA。',
'8-7':'检查多语言思考训练入口；没有新 checkpoint 和前后对照。','8-8':'Prompt 蒸馏流水线测试及历史材料核对；未生成新教师数据或训练学生。',
'8-9':'CoT 筛选与学生评估流程测试；历史 1/24→2/24 不等于显著提升。','8-10':'阅读 AdaptThink 无 checkpoint 报告；未新训练或运行独立 checkpoint 评估。',
'8-11':'外部 GeneralPoints 复现入口核对；缺数据/权重/实际训练。','8-12':'外部 V-IRL 入口核对；未执行视觉导航训练。',
'8-13':'SimpleVLA-RL 依赖和指南核对；未配置完整仿真及模型。','8-14':'ReTool 指南核对；缺 SandboxFusion 服务与训练 checkpoint。',
'8-15':'AWorld/veRL 指南核对；未运行奖励曲线训练。','8-16':'RLVP 指南核对；未完成源码、CUDA 训练和多种子评估。',
'8-17':'生成偏好对并演示 mock 指标；没有新的真实 DPO 权重训练。','8-18':'检查作用域数据、受保护区域和评估函数；未新训 LoRA。',
'8-19':'检查随机字符串、字节级评分和数据隔离；未新训精确复制模型。',
'9-1':'启发式三层 verifier 跑四条轨迹；不是本次真实 LLM Judge 校准。','9-2':'阅读失败提炼及迁移集历史活动；未新跑 τ²-bench 三臂。',
'9-3':'配置预演和补丁/发布门禁单测；未新跑任务 Agent、Judge、Coding Agent。','9-4':'本机 qwen3:0.6b 三臂各六题：3/6、2/6、4/6；非完整用户反馈长期活动。',
'9-5':'离线状态谓词、候选回放、页面变化失效演示；不是新浏览器在线学习。','9-6':'核对隔离补丁、回归与回滚设计；缺 Docker，未运行任意候选代码。',
'9-7':'quick 模式接受确定性提案、拒绝过宽反例；修复跨平台路径识别并测过。','9-8':'核对 Hermes 历史活动；缺少其运行环境与模型服务，未执行新的自身代码更新。',
'9-9':'运行三种确定性参考策略并检查统计；没有 126 次新的在线模型活动。',
'10-1':'角色清单与技能/角色编排测试；未重做 30 对在线任务和盲评。','10-2':'翻译 dry-run 与术语/审核参数测试；未新翻译整书。',
'10-3':'注册编排与原始收据验收器测试；未拨号或提交外部表单。','10-4':'取消、完成确认、重复消息测试；未新开十站真实在线并行搜索。',
'10-5':'小镇存储/供应商适配等单测与历史资料核对；未新跑 25 人×三组×两虚拟日。','10-6':'离线游戏信息隔离通过，2 个完整循环；无真实语音回环和 LLM 策略。',
}

def read(path):return json.loads(path.read_text(encoding='utf-8'))
def local_findings(chapter):
    if chapter==5:
        return ['## 本次可打开的产物','', '[级联表单](results/flight-form.html) · [视频剪辑](results/edit-smoke.mp4) · [剪辑抽帧](results/edit-smoke-frame.png) · [逐题 CSP 结果](results/logic-solver.json) · [混合日志解析](results/parsed-logs.jsonl)','', 'CSP 的 12/12 使用直接给定的结构化约束，不包含模型翻译题意。视频约 5.03 秒，实际后端是 ffmpeg；生成的 bpy 脚本没有经 Blender 执行。日志演示安装的是预置函数。','']
    if chapter==6:
        return ['## 本次真实运行','', '异步四场景第一次用了 0.05 秒 tick，真实长任务不足协议要求的三秒，只通过 8/9 门禁；[失败记录](results/subprocess-campaigns/local-20261025/summary.json)保留。恢复原协议的 0.15 秒 tick 后，[v2](results/subprocess-campaigns/local-20261025-v2/summary.json)通过 9/9。该活动检验真实子进程和脚本化调度，不包含新模型决策。','', '| 当前编号 | 实际运行 | 独立验证 |','| --- | --- | --- |','| 6-11 | 3 seeds × 3 object-counts × 256 episodes，共 2,304；各 cell 成功率 100% | [通过](results/gpu/6-11-validation.txt) |','| 6-13 | 3 seeds × 3 故障概率 × 3 模式 × 128，共 3,456 episodes | [通过](results/gpu/6-13-validation.txt) |','| 6-14 | 3 seeds × 4 训练条件 × 4,096 样本，10 epochs；目标域每种 1,024 例 | [通过](results/gpu/6-14-validation.txt) |','', '[运行命令、源码哈希和时间](results/gpu/summary.json)。显卡为 RTX 3070 Laptop GPU，PyTorch 2.11.0+cu128。原始源文件保留旧实验编号 6-10/6-12/6-13，与当前编号一一对应。所有动作都在自包含模拟器里，未驱动硬件。','', 'RGB 三种子均值：干净训练在原域 92.74%、target_realistic 56.28%；完整随机化分别为 88.05%、75.46%。这次没有复现“完整随机化在所有目标域都优于所有单因素组”：appearance 的 target_realistic 为 75.55%，略高于 full，差距也需结合种子波动看。','']
    if chapter==7:
        return ['## 成本复算','', '脚本内假设计费为每百万 token：输入 0.15、缓存输入 0.075、输出 0.60 美元。以下是旧用量在这套假设下的计算结果，未作为当前市场报价或本次真实账单。','', '| 条件 | 同一计价假设下的总成本（美元） |','| --- | ---: |','| naive | 0.00377580 |','| kv | 0.00270750 |','| compress | 0.00311475 |','| both | 0.00264285 |','', '[逐轮 JSON](results/cost-analysis.json)保留缓存/未缓存输入、输出、工具上下文与时延。7-11 的 168 小时活动没有启动。','']
    if chapter==8:
        return ['## 本次实际训练','', '[Q-learning 记录](results/q-learning.json)：seed 42，10,000 轮训练；100 轮贪心评估胜率 100%，平均 12 步。累计训练胜率 45.1% 包括探索期，不能与最后贪心评估直接混为同一指标。','', '![本机 Q-learning 曲线](results/q-learning-curve.png)','', '这是真实表格型 Q-learning，不是 LLM 权重微调。其余演示的 mock 指标和作者保存的训练报告都按来源标明。','']
    if chapter==9:
        return ['## 9-4 的本机补充','', '| 提示条件 | 正确决策 | API 错误 |','| --- | ---: | ---: |','| baseline | 3/6 | 0 |','| append_feedback | 2/6 | 0 |','| scoped_skill | 4/6 | 0 |','', '固定 qwen3:0.6b、temperature=0、seed=42、think=false，三组使用相同六题；[协议和逐次原始响应](results/clarification-trial/)全部保留。只测 ask/confirm_spec/execute 的下一步选择，没有真正执行用户任务；样本与 Skill 是本次设计的，不能推断稳定的真实用户收益。Skill 组仍对范围明确的小修改和只读请求过度确认。','', '[安全门禁 quick](results/demos/safety-gate.txt)没有执行外部删除或推送，执行器是验证器提供的内存模拟器。','']
    if chapter==10:
        return ['## 离线协作检查','', '翻译预演只估算四角色的上下文与术语预算，不生成新译文。狼人杀的[本机报告](results/werewolf-offline.json)为 supplemental_only：信息隔离通过，完成两个完整循环，真实 LLM 策略未运行，音频回环为零。因此它没有达到完整语音狼人杀要求。','']
    return []
def summary(chapter):
    jobs=[];totals={}
    directory=HOME/f'task{chapter}'/'results'/'checks'
    for p in sorted(directory.glob('*.json')):
        if '.attempt' in p.name:continue
        job=read(p);text=p.with_suffix('.txt').read_text(encoding='utf-8',errors='replace')
        line=next((x for x in reversed(text.splitlines()) if re.search(r'\d+ (passed|failed|skipped|errors?)',x)), '')
        counts={k:int(n) for n,k in re.findall(r'(\d+) (passed|failed|skipped|errors?)',line)}
        job['pytest_summary']=line;job['counts']=counts
        jobs.append(job)
        for k,n in counts.items():totals[k]=totals.get(k,0)+n
    return {'jobs':len(jobs),'passed_jobs':sum(x['status']=='passed' for x in jobs),'pytest_counts':totals,'rows':jobs}

def main():
    all_checks=[{'chapter':4,**summary(4)}]
    for chapter,label in LABELS.items():
        dest=HOME/f'task{chapter}';dest.mkdir(exist_ok=True)
        evidence=read(dest/'results'/'saved-evidence-review.json')
        checks=summary(chapter);all_checks.append({'chapter':chapter,**checks})
        (dest/'results'/'check-summary.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        progress=[f'# 第 {chapter} 章｜逐项进度','', '更新日期：2026-10-25。下面记我这次实际做的部分。作者以前的运行另列在“历史材料”里；文件能读到，只说明这份材料在当前 Git 快照中。','', '| 实验 | 本机操作与范围 | 回执 | 历史材料 |','| --- | --- | --- | --- |']
        experiment=[f'# 第 {chapter} 章｜实验记录','', '本次在 Windows 的项目 `.venv` 中执行。普通脚本与模型请求的命令、退出码、耗时和日志都保存在 `results/`。离线演示和测试通过，仅对应它们检查到的内容。','', f'本机检查：{checks["jobs"]} 组命令中 {checks["passed_jobs"]} 组退出成功；pytest 的末次汇总为 `{checks["pytest_counts"]}`。首次失败日志保留在 `checks/*.attempt*.txt`，没有从统计中删掉失败后假装从未发生。','', '[检查汇总](results/check-summary.json) · [历史材料抽查](results/saved-evidence-review.json)','', '历史抽查固定在 Git 提交 `faa6db95`，每份 JSON 最多检查 40 个声明文件；使用原始 Git 字节，避免 Windows 换行影响。未能解析的旧路径、未跟踪产物和实际哈希差异会出现在报告中，因此这份抽查不是“所有历史验收重新通过”的证明。','']
        experiment.extend(local_findings(chapter))
        for row in evidence['rows']:
            exp=row['experiment'];number=int(exp.split('-')[1]);links=[]
            for name in CHECKS.get(chapter,{}).get(number,[]):
                p=dest/'results'/'checks'/f'{name}.json'
                if p.exists():
                    d=read(p);links.append(f'[{name}: {d["status"]}](results/checks/{name}.txt)')
            name=DEMOS.get(chapter,{}).get(number)
            if name and (dest/'results'/'demos'/f'{name}.json').exists():
                d=read(dest/'results'/'demos'/f'{name}.json');links.append(f'[演示 exit={d["returncode"]}](results/demos/{name}.txt)')
            if exp=='8-1':links.append('[训练与评估](results/q-learning.json)')
            if exp=='9-4':links.append('[18 次实际本地请求](results/clarification-trial/summary.json)')
            if chapter==6 and number in (11,13,14) and (dest/'results'/'gpu'/exp/'evidence.json').exists():
                links.append(f'[本次 GPU 证据](results/gpu/{exp}/evidence.json)')
                links.append(f'[独立校验](results/gpu/{exp}-validation.txt)')
            if exp=='6-2':links.append('[四场景原始记录](results/subprocess-campaigns/local-20261025-v2/summary.json)')
            path=row['evidence']
            historical=f'[保存的材料](../../{path})' if row['evidence_in_git'] else '未取得对应 Git 文件' if path else '无本次选定的完整证据文件'
            observation=NOTES.get(exp,'阅读正文与对应实现，未执行新的正式活动。')
            progress.append(f'| {exp} {row["title"].replace("|","/")} | {observation} | {" · ".join(links) or "源码/说明核对"} | {historical} |')
            experiment.extend([f'## {exp}｜{row["title"]}','',observation,'',f'本机记录：{" · ".join(links) or "本次只阅读了正文与入口，没有新运行回执。"}','',f'历史材料：{historical}。'+(f' Git 原始文件 SHA-256：`{row["baseline_sha256"]}`。' if row['baseline_sha256'] else ''),''])
        (dest/'progress.md').write_text('\n'.join(progress)+'\n',encoding='utf-8')
        (dest/'experiment.md').write_text('\n'.join(experiment).rstrip()+'\n',encoding='utf-8')
        (dest/'README.md').write_text(f'# 第 {chapter} 章｜{label}\n\n我把这章的阅读、实验和还没补齐的条件放在这里。逐项进度以本机实际记录为准，作者的历史活动有单独链接。\n\n- [学习笔记](notes.md)\n- [学习心得与课程反馈](reflection-and-feedback.md)\n- [实验记录](experiment.md)\n- [逐项进度](progress.md)\n- [运行结果](results/)\n\n原文：[第 {chapter} 章](../../book/chapter{chapter}.md)。\n',encoding='utf-8')
    (HOME/'chapter4-10-checks.json').write_text(json.dumps(all_checks,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('Wrote chapter 5-10 records and test summaries.')

if __name__=='__main__':main()
