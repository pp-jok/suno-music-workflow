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

Read [the lyric workflow](references/lyric-workflow.md) for Hook, drafting, and revision guidance. Read [the production plan and Style guide](references/production-plan.md) before writing or shortening a Style prompt.
Read [the Mandarin songwriting quality guide](references/mandarin-songwriting.md) before offering or expanding a Hook.

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

Read [the lyric workflow](references/lyric-workflow.md) for scoped revisions. Read [the production plan and Style guide](references/production-plan.md) before writing or shortening a Style prompt. Read [the audio review guide](references/audio-review.md) for evidence-bounded audio and LRC review.
Read [the Mandarin songwriting quality guide](references/mandarin-songwriting.md) before offering or expanding a Hook.
Read [the non-Studio generation loop](references/generation-loop.md) after a generation result or feedback-led music revision.

## Published scenario contract

| Scenario | Expected mode | Non-negotiable behavior |
|---|---|---|
| Character song | Fast mode | preserve the named character details and direction; use a creative card and two or three Hook candidates before expansion |
| Restrained breakup song | Fast mode | preserve the restrained direction and supplied central line without inventing an upbeat or unrelated direction |
| Pre-chorus-only revision with chorus fixed | Producer mode | change only the pre-chorus and keep the approved chorus fixed |
| Overlong Style requiring supplied source text | Producer mode | require the source Style text, then preserve tempo or groove and avoid items while shortening it below 1,000 characters |
| Audio/LRC request requiring supplied audio plus approved lyrics | Producer mode | require both supplied audio and approved lyrics; do not fabricate review evidence, official lyrics, or timestamps |
| Template-like Hook | Fast mode | stop expansion, identify the missing landing point or contrast, and return to the Hook |
| Rhyme harms natural Chinese | Fast mode | repair natural phrasing before rhyme; do not hide the problem with more wordplay |
| Lyrics work but Style feels flat | Producer mode | keep lyrics fixed and change song identity or section dynamics only |
| User only says the version feels ordinary | Producer mode | diagnose one likely layer and propose one controlled experiment, not a full rewrite |
| Confirmed chorus stays fixed | Producer mode | preserve the approved chorus during local revision unless the user explicitly unlocks it |
| Single stochastic render appears better | Producer mode | report a low-confidence tendency, not prompt causality; compare multiple candidates when practical |
| A section feels dragging | Producer mode | diagnose one likely lyrics, Hook, structure, dynamics, or vocal/Style layer before changing it |
| Internal quality checks | Fast mode | show only the creative result and one or two material risks unless the user requests the checklist |
