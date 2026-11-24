#!/usr/bin/env python3
"""One Line of Earned Pride — make.fun entry.

Writes a single line of quiet, earned pride to /output/entry.txt.
No network, no randomness, no input files: the same line every run.
"""

import os
import sys

LINE = (
    "The fisherman who mended nets for forty winters finally watched "
    "his son steer their boat home alone through the fog, and said "
    "nothing at all."
)


def main() -> int:
    # Gate: the entry must be 1-240 UTF-8 characters, not only whitespace.
    if not (1 <= len(LINE) <= 240 and LINE.strip()):
        print("entry out of gate: length %d" % len(LINE), file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
