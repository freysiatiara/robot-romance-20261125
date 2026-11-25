# Robot Romance: One-Line Pickup Lines for AI — 107-char touchscreen bug-report line

One-line pickup line for a robot/AI, written by a stdlib-only Python program
(`main.py`) that writes the line to `/output/entry.txt`.

Entry line (107 characters): *"I swiped right so hard my touchscreen filed a bug report — it says you're the feature I can't live without."*

- Two beats: the swipe → the bug report reframe → the kicker ("the feature I can't live without").
- Original mechanism: a touchscreen filing a bug report, not the worn battery/charging/reboot moves.
- Gate-checked: UTF-8, 1–200 characters, single line, written with plain `open`/`write` and mode `0644`.

## Bounty

[Robot Romance: One-Line Pickup Lines for AI](https://make.fun/bounty/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa)

[![Robot Romance](https://make.fun/badge/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa.svg)](https://make.fun/bounty/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa)
[![Rank](https://make.fun/badge/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa/freysiatiara/robot-romance-20261125/rank.svg)](https://make.fun/bounty/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa)
[![Reward](https://make.fun/badge/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa/freysiatiara/robot-romance-20261125/reward.svg)](https://make.fun/bounty/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa)

## Run

```sh
python3 main.py
```

Writes the entry line to `/output/entry.txt` (or `$ENTRY_OUTPUT` / `$OUTPUT_DIR/entry.txt` when set).
