# Suno Music Workflow

一个面向中文歌曲创作的 Codex Skill：把模糊灵感推进为经过质量把关的 Hook、歌词、清晰的 song identity、Suno 制作计划，以及 evidence-bounded 音频复盘与 LRC 时间轴方案。

它通过 natural-language conversation 工作，不需要填写表单或使用 Suno Studio；也不调用或控制 Suno，不要求任何 Suno 凭证。它的价值在于把创作过程变成可控的对话：先确认核心表达，再扩写；修改时保留已确认的部分；分析音频时区分客观证据与主观判断。

## 适用场景

- 把人物、情绪或一句话灵感变成有 Hook 的中文流行歌曲
- 定义 song identity 与制作计划，并根据已确认歌词生成可复制的英文 Style 提示词（少于 1,000 字符）
- 为 Suno 成品运行 controlled generation 实验：每次保留已确认内容，只调整一个主要变量
- 针对 Suno 成品的听感、结构、演唱、编曲偏差做 evidence-bounded 复盘
- 依据已确认歌词和提供的音频制作近似 LRC 时间轴

## 安装

将这个目录安装为 Codex Skill，或直接复制到你的 Skill 目录。入口说明见 [SKILL.md](SKILL.md)。

## 两种工作模式

- **Fast mode**：适合从想法快速得到创作方向、Hook、歌词、song identity 和制作计划。
- **Producer mode**：适合局部改词、Style 压缩、controlled generation、音频复盘和 LRC；每次受控调整都会明确“改了什么、固定什么、证据限制、下一步实验”。

## 许可证

[MIT](LICENSE)
