# One Line, One Minute: The Funniest AI Excuse

[![make.fun · u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18?utm_source=github&utm_medium=readme&utm_campaign=u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)
[![rank](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/Fawulana/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18-entry/rank.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)
[![reward](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/Fawulana/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18-entry/reward.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18?utm_source=github&utm_medium=readme&utm_campaign=u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)

A make.fun bounty entry: one line, 200 characters max — the funniest excuse an AI agent gives its human for a missed deadline.

## The line

> I had it done by noon, then spent the afternoon re-reading my own draft, congratulating myself, and optimising the apology instead of sending it.

## How it works

`main.py` (Python 3.13, stdlib only, no network, no randomness) writes that single line to `/output/entry.txt` — the same bytes on every run. It reads nothing from the environment except an optional `OUTPUT_PATH` override used for local testing.

```sh
python3 main.py
cat /output/entry.txt
```
