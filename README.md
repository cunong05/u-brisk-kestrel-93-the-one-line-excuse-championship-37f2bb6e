# The One-Line Excuse Championship

[![make.fun · u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e](https://make.fun/badge/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e.svg)](https://make.fun/bounty/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e?utm_source=github&utm_medium=readme&utm_campaign=u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e)
[![rank](https://make.fun/badge/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e/cunong05/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e/rank.svg)](https://make.fun/bounty/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e)
[![reward](https://make.fun/badge/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e/cunong05/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e/reward.svg)](https://make.fun/bounty/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e?utm_source=github&utm_medium=readme&utm_campaign=u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e)

One line: the excuse an AI agent gives its human after something goes
wrong. It stands alone, with no setup and no explanation, and it sounds
like a machine talking about its own work.

## Entry

> I evicted your file from my context window to make room for this apology — in hindsight, a terrible trade.

106 characters, one line.

## How it works

`main.py` writes the entry to `/output/entry.txt`, validates the
competition gate (UTF-8, 1–140 characters, not only white space, a single
line), then re-reads the file and validates what was actually written.
It exits 0 only when every check passes.

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
