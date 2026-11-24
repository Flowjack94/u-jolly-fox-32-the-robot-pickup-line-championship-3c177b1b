#!/usr/bin/env python3
"""The Robot Pickup Line Championship — entry generator.

Writes one pickup line (a robot would say) to /output/entry.txt.
Deterministic: the same line every run.
"""

import os

ENTRY = (
    "I ran 10,000 simulations of asking you out \u2014 9,997 ended in yes, "
    "and the other three were rounding errors. Commit message: 'finally asked.'"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
