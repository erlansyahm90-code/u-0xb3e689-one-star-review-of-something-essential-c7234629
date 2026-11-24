"""Produce a single deadpan one-star review as a plain-text file.

The competition expects one short review placed at /output/entry.txt.
This script holds the review as a constant, checks it against the
competition's length gate, and writes it out byte for byte, with no
extra newline at the end.
"""

from pathlib import Path

ENTRY = "One star. Spent eight hours on it and woke up tired. The product does not work as advertised."

# The gate: between 1 and 160 characters, and not whitespace only.
assert 1 <= len(ENTRY) <= 160
assert ENTRY.strip()

OUT = Path("/output/entry.txt")

# Make sure the destination folder exists, then write the review verbatim.
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(ENTRY, encoding="utf-8")

print(f"Wrote {len(ENTRY.encode('utf-8'))} bytes to {OUT}")
