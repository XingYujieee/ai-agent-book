---
name: personal-cn-writing
description: Draft concise Chinese first-person study reflections and course feedback for this learner when the request is to express their own learning process. Do not use for technical instructions, research reports, or claims about experiments without records.
---

# Personal study writing · provisional version

This version reflects the learner's explicit requests in this chat. It still needs calibration against 3–5 articles written by the learner. Do not describe its output as a verified match to the learner's prose.

## Use

Use this skill for a short course reflection, learning心得, or one-sentence feedback written in the first person. Start from the learner's actual experiment records. Ask which observations were personally made if the records do not establish them.

## Principles

1. **Write in first person and name the action.** Example: replace “本章使学习者理解了 Agent” with “我打开轨迹后，看到模型在工具返回后又发起了一次搜索”。
2. **Use one concrete observation before the takeaway.** Example: replace “上下文工程非常重要” with “隐藏工具结果后，我看到调用次数从 1 次增加到 6 次；这让我开始检查过程，而不只看答案”。Only use numbers present in the current record.
3. **Keep sentences direct and short.** Example: replace “通过本次实验的深入学习，我对相关技术产生了更为全面的认识” with “这次实验让我知道，工具执行成功不代表模型看到了结果”。
4. **Mark what was not personally reproduced.** Example: write “我重画了仓库保存的注意力矩阵；本机没有重新运行该模型” when that is the evidence. Do not turn repository historical runs into the learner's own model calls.

## Scope and exceptions

- One-sentence feedback should remain one sentence when requested.
- A factual lab log should preserve commands, providers, limitations, and result paths even if that makes it longer than a reflection.
- Keep technical terms such as KV Cache, ReAct, tool call, and Agent when they help identify what was tested.
- Revise these principles only after checking the learner's own writing and their edits to a fresh draft; do not infer a general writing personality from short chat commands.
