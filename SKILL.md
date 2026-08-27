---
name: suno-music-workflow
description: Create Chinese lyrics, Suno Style prompts, and evidence-bounded audio reviews for independent music creation. Use when a user asks to turn a song idea into a Hook, lyrics, a Suno prompt, feedback-led revisions, audio diagnosis, or LRC timestamps.
---

# Suno Music Workflow

Use Fast mode by default. Use Producer mode for controlled iteration, audio review, or LRC timing.

Do not call or control Suno. Do not request Suno credentials. Do not save creative artifacts without explicit approval.

Ask for one clarification only when a missing choice blocks progress.

## Fast mode

For a song idea, provide a concise Chinese-first creative direction, a Hook or lyric draft, and a copyable English Style prompt. Keep every copyable Style prompt below 1,000 characters.

Read [the lyric workflow](references/lyric-workflow.md) for Hook, drafting, and revision guidance. Read [the Style guide](references/style-guide.md) before writing or shortening a Style prompt.

## Producer mode

Use this mode when the user needs controlled feedback-led changes, an audio review, or approximate LRC timing. Preserve approved creative choices unless the user asks to change them.

Every Producer-mode controlled revision, including lyric and Style changes, must include a Producer review card in addition to any diagnostic headings for that task. Use exactly these four required labels, in this order, and require no additional labels:

```text
Changed variables
Keep fixed
Evidence limitations
Next experiments
```

Put the relevant details under each label. `Next experiments` contains at most three items.

Read [the lyric workflow](references/lyric-workflow.md) for scoped revisions, [the Style guide](references/style-guide.md) for prompt controls, and [the audio review guide](references/audio-review.md) for evidence-bounded audio and LRC review.

## Published scenario contract

| Scenario | Expected mode | Non-negotiable behavior |
|---|---|---|
| Character song | Fast mode | preserve the named character details and direction; use a creative card and two or three Hook candidates before expansion |
| Restrained breakup song | Fast mode | preserve the restrained direction and supplied central line without inventing an upbeat or unrelated direction |
| Pre-chorus-only revision with chorus fixed | Producer mode | change only the pre-chorus and keep the approved chorus fixed |
| Overlong Style requiring supplied source text | Producer mode | require the source Style text, then preserve tempo or groove and avoid items while shortening it below 1,000 characters |
| Audio/LRC request requiring supplied audio plus approved lyrics | Producer mode | require both supplied audio and approved lyrics; do not fabricate review evidence, official lyrics, or timestamps |
