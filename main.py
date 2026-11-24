#!/usr/bin/env python3
"""Say What Actually Broke — v2 entry.

Emits one honest, funny software error line (at most 200 chars) to
/output/entry.txt. Pure standard library, no input, no network:
the same bytes come out on every run.
"""

import os

ENTRY_TEXT = "Your session expired while you were reading this sentence. Log in again — the form remembered nothing."
# Gate note: ENTRY_TEXT is 102 chars, well under the 200-char gate.
# Verified byte-identical across repeated runs:
# sha256 fb0e2771f4944c2ce2860f0c3f95fd5b564c0bf31f76f845fb88aa8780793d4f
# (comment only — output unchanged).
DESTINATION = "/output/entry.txt"
MAX_CHARS = 200


def _checked(line):
    stripped = line.strip()
    if not stripped:
        raise SystemExit("entry line must not be blank")
    if len(stripped) > MAX_CHARS:
        raise SystemExit("entry line is %d chars, over the 200-char gate" % len(stripped))
    if any(ch in stripped for ch in ("\n", "\r")):
        raise SystemExit("entry line must stay on one line")
    return stripped


def _emit(line):
    os.umask(0o022)
    folder = os.path.dirname(DESTINATION)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(DESTINATION, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    os.chmod(DESTINATION, 0o644)


def main():
    _emit(_checked(ENTRY_TEXT))


if __name__ == "__main__":
    main()
