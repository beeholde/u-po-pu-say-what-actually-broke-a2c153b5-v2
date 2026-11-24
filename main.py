#!/usr/bin/env python3
"""Say What Actually Broke — entry program (v2).

Writes one single line of software error copy (at most 200 characters)
to /output/entry.txt: the brutal truth about what broke, and funny
enough to repeat out loud.

Standard library only. Deterministic: the same bytes on every run.
No network, no input, no arguments.
"""

import os

LINE = "Your session expired while you were reading this sentence. Log in again — the form remembered nothing."
# Gate note: LINE is 102 chars, well under the 200-char gate.
# Verified byte-identical across repeated runs:
# sha256 fb0e2771f4944c2ce2860f0c3f95fd5b564c0bf31f76f845fb88aa8780793d4f
# (comment only — output unchanged).

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = LINE.strip()
    if not (1 <= len(text) <= 200):
        raise SystemExit("entry must be 1 to 200 characters, got %d" % len(text))
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    os.umask(0o022)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
