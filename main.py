#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuses — make.fun entry.

Writes one funny line (71 characters, one line) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The line is fixed and deterministic: every run writes the exact same
bytes, with no trailing newline, so the two grading runs agree.
"""

import os
import sys

LINE = "A user did exactly what the button said to do. We never tested that."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
