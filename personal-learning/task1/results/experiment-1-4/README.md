# 实验 1-4：四张图片的来历

2026-10-13，使用 Codex 内置 `image_gen` 生成，每张图各调用一次。图片用于比较**同一生图工具**收到原始需求和仓库历史改写词时的变化。本次没有运行仓库 `chapter1/image-gen-workflow/main.py`，也没有调用 Kimi、通义万相、Gemini 或 OpenAI API 的原版三路线。生成具有随机性，这四张图不能代表稳定胜率。

| 文件 | 传入图片工具的核心需求 | SHA-256 |
| --- | --- | --- |
| [headphone-direct.png](headphone-direct.png) | 原始中文需求；明确要求文案“深夜独处也清净”逐字出现在耳机海报上 | `3F8F07BD18C3697DFF417FF5045FD6D11D9E5451D1122BF6E2C6F5641B49DBD2` |
| [headphone-rewritten.png](headphone-rewritten.png) | 仓库 `validation/latest.json` 中 `headphone-poster` 的英文 `prompt` 和 `negative_prompt`；其中负面词含 `text`，本次也要求不要文字 | `27B9F74A13B41EF60F245917E69B25A8E1683068E135D2D333EC28C282A3AEC0` |
| [agi-direct.png](agi-direct.png) | 原始中文需求“帮我画一个 AGI 实现以后程序员的工作场景”，未指定具体叙事 | `2B46A88444203270314FF44F6A1E8E4612847FD0D192D7AE7C606C0B634D2EBD` |
| [agi-rewritten.png](agi-rewritten.png) | 仓库 `validation/latest.json` 中 `agi-programmer` 的英文 `prompt` 和 `negative_prompt`，明确要求人喝咖啡、机器人写代码 | `C20543FBD0E43BE693A7D5F6EBE6C239D26177E5E13166BFA8CCA650C92AD7A7` |

提示词来源：[原项目 1-4 留证](../../../../chapter1/image-gen-workflow/validation/latest.json)。本次观察与局限见[实验过程](../../experiment.md)。
