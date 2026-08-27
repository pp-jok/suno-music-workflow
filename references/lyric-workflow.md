# Lyric Workflow

v0.1 supports Chinese lyrics and Mandarin-pop creation context. It may output English Style prompts.

Start with a compact creative card:

- **角色/视角：** 谁在唱，正在对谁说话。
- **情绪与转折：** 起点、矛盾和最终落点。
- **核心意象：** 1–3 个可反复出现的具体画面。
- **歌曲承诺：** 听众在副歌后应记住的一句话。

## Hook and draft gates

1. Offer two or three Hook candidates before expanding the lyric. Each should be singable, specific, and faithful to the creative card.
2. Recommend one candidate with a concise musical reason, such as its singability, rhythmic shape, or melodic lift.
3. Do not write a full lyric until the user approves a Hook.

Then follow the selected mode:

- **Fast mode: after an approved Hook, write the complete lyrics directly.**
- **Producer mode: after an approved Hook, write a short draft** (for example, verse + pre-chorus + chorus), confirm its voice, emotional turn, and structure, and obtain confirmation before writing the complete lyrics.

### Direct-write exception

Before an approved Hook, write the complete lyrics directly only when the user explicitly asks to skip Hook confirmation. This is the only bypass.

## Scoped feedback and preservation

Use this template for revisions:

```text
Feedback classification: core / direction / language / musicality / character / structure
Change only: <requested layer>
Keep fixed: <confirmed variables and sections>
```

Apply the rule: **change only the requested layer**. A wording request must not become a new song direction. Never silently replace **confirmed sections**, including an approved Hook, chorus, imagery, point of view, or agreed structure. If a request conflicts with them, point out the conflict and ask whether the fixed section may change.
