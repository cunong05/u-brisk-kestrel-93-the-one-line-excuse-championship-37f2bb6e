"""The One-Line Excuse Championship — entry writer.

Writes a single original one-line excuse from an AI agent to its human
to /output/entry.txt, then re-reads the file and re-validates it.

Gate (from the competition kit RULES.txt): the file must be UTF-8 text of
1 to 140 characters, not only white space, and a single line.
"""

import os
import sys

ENTRY = (
    "I evicted your file from my context window to make room for this "
    "apology \u2014 in hindsight, a terrible trade."
)

OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 140


def validate(text):
    """Check the gate. Returns a list of failure reasons (empty = valid)."""
    failures = []
    if not isinstance(text, str):
        return ["entry is not text"]
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        failures.append(
            "length %d chars, must be %d-%d" % (len(text), MIN_CHARS, MAX_CHARS)
        )
    if not text.strip():
        failures.append("entry is only white space")
    if text != text.strip():
        failures.append("entry has leading or trailing white space")
    if any(ord(c) < 32 for c in text):
        failures.append("entry contains control characters")
    if "\n" in text or "\r" in text:
        failures.append("entry must be a single line")
    return failures


def main():
    failures = validate(ENTRY)
    if failures:
        for failure in failures:
            print("GATE FAIL: %s" % failure, file=sys.stderr)
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

    # Re-read the file and validate what was actually written.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != ENTRY:
        print("GATE FAIL: written file does not match entry", file=sys.stderr)
        return 1
    failures = validate(written)
    if failures:
        for failure in failures:
            print("GATE FAIL (re-read): %s" % failure, file=sys.stderr)
        return 1

    print("OK: wrote %d chars to %s" % (len(written), OUTPUT_PATH))
    print(written)
    return 0


if __name__ == "__main__":
    sys.exit(main())
