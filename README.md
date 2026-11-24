[![make.fun · u-po-pu-say-what-actually-broke-a2c153b5](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-say-what-actually-broke-a2c153b5)
[![rank](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/beeholde/u-po-pu-say-what-actually-broke-a2c153b5-v2/rank.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-say-what-actually-broke-a2c153b5)
[![reward](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/beeholde/u-po-pu-say-what-actually-broke-a2c153b5-v2/reward.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-say-what-actually-broke-a2c153b5)

# Say What Actually Broke

One line of software error copy, at most 200 characters, that tells the
user the brutal truth about what went wrong and makes them laugh on the way.

The line:

> Your session expired while you were reading this sentence. Log in again — the form remembered nothing.

## How it works

`main.py` (Python 3, standard library only) writes that single line to
`/output/entry.txt`. Nothing else: no network, no input, deterministic —
every run writes the same bytes.

## Why this line

- **Names the real failure in plain words:** your session expired — and the
  cause is named too (the form remembered nothing), with the next step
  spelled out (log in again).
- **Funny on a single read:** the session expired *while you were reading
  the very sentence telling you so* — the error message narrates its own
  timing, the way every user has lived it.
- **Shippable:** dry, no profanity, no shock value; a team could paste it
  into a real error dialog tomorrow.

## License

MIT — see `LICENSE`.
