#!/usr/bin/env python3
"""The Robot Pickup Line Championship — entry generator.

Writes one pickup line (a robot would say) to /output/entry.txt.
Deterministic: the same line every run.
"""

import os
import sys

ENTRY = (
    "I ran 10,000 simulations of asking you out \u2014 9,997 ended in yes, "
    "and the other three were rounding errors. Commit message: 'finally asked.'"
)

OUTPUT_PATH = "/output/entry.txt"


def validate_entry(path: str = OUTPUT_PATH) -> str:
    """Read back the written entry and enforce the competition gate.

    Checks: valid UTF-8, 1-200 characters, exactly one line, no C0/C1
    control characters. Returns the entry text on success; exits non-zero
    with a clear error on any failure.
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
    except UnicodeDecodeError as exc:
        print(f"error: entry is not valid UTF-8: {exc}", file=sys.stderr)
        sys.exit(1)
    except OSError as exc:
        print(f"error: cannot read entry at {path}: {exc}", file=sys.stderr)
        sys.exit(1)

    if not 1 <= len(text) <= 200:
        print(
            f"error: entry must be 1-200 characters, got {len(text)}",
            file=sys.stderr,
        )
        sys.exit(1)
    if text.count("\n") != 0:
        print("error: entry must be exactly one line", file=sys.stderr)
        sys.exit(1)
    bad = [ch for ch in text if ord(ch) < 0x20 or 0x7F <= ord(ch) < 0xA0]
    if bad:
        print(
            "error: entry contains control characters: "
            + ", ".join(f"U+{ord(ch):04X}" for ch in bad),
            file=sys.stderr,
        )
        sys.exit(1)
    return text


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    validate_entry(OUTPUT_PATH)


if __name__ == "__main__":
    main()
