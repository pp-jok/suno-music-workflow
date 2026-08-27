# Audio Review Guide

Use Producer mode for audio review. Separate what can be observed from what is reported and what is interpreted; do not present an interpretation as a measurement.

## Objective evidence

Record duration, codec, audible or supplied transcript segments, structure when supported by the supplied audio, and LRC alignment as **objective evidence**. State missing inputs plainly. If transcription or timing is uncertain, label the uncertainty rather than presenting a transcript as official lyrics.

## User feedback

Quote or concisely restate the user's reported target, preferences, and perceived issues. User feedback is attributed to the user, not presented as independent measurement.

## Editorial judgement

Melody quality, vocal emotion, arrangement appeal, and commerciality are **editorial judgement** unless supplied by the user. Explain the audible cue behind a judgement when possible, but keep the label.

## Inference

Mark causes, likely production choices, and proposed fixes as inference. Offer a small next test instead of claiming certainty from a single render.

## Producer review card

Every Producer-mode review card must contain exactly these four labels, in this order. Use the bracketed evidence tags inside field values rather than adding more labels.

```text
Changed variables: <use [User feedback], [Editorial judgement], and [Inference] tags as needed>
Keep fixed: <approved lyrics, Hook, voice, structure, timing anchors, and other approved choices>
Evidence limitations: <use an [Objective evidence] tag; state missing inputs and uncertainty>
Next experiments:
1. <one controlled change, expected result, and comparison>
```

`Next experiments` contains at most three items.

## LRC text authority

For LRC work, approved lyrics are authoritative for LRC text. When they are supplied, correct the transcription against the approved lyrics; never copy a transcription error into the LRC. Use transcription only to align the approved text with the performance. If they are absent, state that formal LRC text cannot be finalized without approved lyrics, request the approved lyrics, and do not present a transcript as formal LRC text. When one sung phrase merges multiple approved lyric lines, split timestamps as **approximate** and say that the split is approximate.
