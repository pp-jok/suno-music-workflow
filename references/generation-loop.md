# Non-Studio Generation Loop

Do not depend on Suno Studio.

```text
Style → generate → feedback or audio review → problem layer → one primary changed variable → compare the next version
```

For every controlled next step, preserve approved choices, name one primary changed variable, and state the expected listening result; do not change lyrics, genre, tempo, and instrumentation together.

| Problem layer | Keep fixed | One primary changed variable |
|---|---|---|
| Hook, core emotion, or point of view fails | other approved brief choices | Hook or lyric core, then regenerate |
| lyrics work but pace, groove, or pop energy fails | lyrics, Hook, point of view | Style groove or pace |
| images work but memory point is weak | lyrics and emotion | song identity or Hook landing |
| one section drags | approved choices outside the diagnosed layer | diagnose likely lyrics, Hook, structure, dynamics, or vocal/Style; state editorial judgement or inference, then test one diagnosed layer |
| structure works but balance or texture does not | lyrics, structure, groove | one sound or instrumentation focus |

When the user only says a version feels ordinary, identify one likely layer—lyrics, Hook, structure, dynamics, or vocal/Style—and propose one controlled experiment rather than a full rewrite.

## Stochastic experiment discipline

Do not infer causality from a single stochastic render. Record fixed choices, one musical layer under test, candidate count, expected listening result, observed evidence, and a low / medium / high confidence conclusion. A better single candidate supports only “this round leans positive” at low confidence. When credits allow, compare multiple candidates under the same fixed condition before increasing confidence or saving a methodology conclusion.

One primary changed variable is one musical layer. It may include coordinated sub-changes inside that layer, such as a dynamic arc across Verse 2, Bridge, and Final Chorus; it must not cross into unrelated lyric, genre, tempo, and instrumentation changes.

## Matched batch comparison

Set up Baseline A and treatment B with the same approved choices and the same candidate count. B changes one musical layer and names the expected listening result. When credits allow, generate more than one candidate in each matched batch. A single render or unequal batches can suggest a next test, but cannot establish prompt causality.

Record evidence with this exact vocabulary: `[Objective evidence]` is observable audio or run data; `[User feedback]` is the creator's report of the target, preference, or reaction; `[Editorial judgement]` is the producer or reviewer's interpretation; `[Inference]` is a tentative explanation that still needs testing.

## Confidence calibration

- **Low:** one render, incomplete evidence, or no replication; report only “this round leans positive.”
- **Medium:** multiple matched candidates show a consistent direction, though evidence may remain limited or subjective.
- **High:** repeated matched batches and clear, relevant user feedback agree; this supports only a project-specific preference, not a universal rule.

## Diagnose before changing a dragging section

For a dragging or ordinary result, identify one most likely layer: lyrics, Hook, structure, dynamics, or vocal/Style. State that the diagnosis is editorial judgement or inference, then test that layer; do not default to changing lyrics when structure or arrangement may be responsible.
