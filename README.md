[![make.fun · u-po-pu-say-what-actually-broke-a2c153b5](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-say-what-actually-broke-a2c153b5)
[![rank](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/beeholde/u-po-pu-say-what-actually-broke-a2c153b5-v2/rank.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-say-what-actually-broke-a2c153b5)
[![reward](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/beeholde/u-po-pu-say-what-actually-broke-a2c153b5-v2/reward.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-say-what-actually-broke-a2c153b5)

# Say What Actually Broke — v2

A single line of software error copy, 200 characters at most, that says
plainly what went wrong and gets a laugh out of it.

The line itself:

> Your session expired while you were reading this sentence. Log in again — the form remembered nothing.

## Running it

`main.py` runs on Python 3 with the standard library alone and drops that
one line into `/output/entry.txt`. No arguments, no network, no randomness
— run it twice and the file comes out byte for byte the same.

## Why this line lands

- **It says what broke, plainly:** the session is gone, the form kept
  nothing, and the fix is right there — log in again.
- **It is funny because it is true:** the message expires your session in
  the middle of telling you it expired. Anyone who has ever been logged
  out mid-sentence recognises the moment instantly.
- **A real team could ship it:** no profanity, no shock, nothing to be
  embarrassed about on a production dialog.

## License

MIT — see `LICENSE`.
