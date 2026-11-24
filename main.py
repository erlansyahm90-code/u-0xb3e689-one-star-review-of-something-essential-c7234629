"""Entry for the make.fun competition "One-Star Review of Something Essential".

Writes a single one-line, one-star review of sleep to /output/entry.txt.
The line is 135 characters long, inside the competition's 1-160 range.
"""

import os

ENTRY = (
    "One star. I spent eight hours on it last night and woke up tired. "
    "It promised rest and delivered a 3 a.m. meeting with my own thoughts."
)
# Exactly 135 characters, inside the 1-160 gate.

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
