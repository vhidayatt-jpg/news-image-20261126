#!/usr/bin/env python3
"""news-image-20261126 entry: write the 26 November 2026 front page to entry.png.

The entry ships a single image (entry.png, an 832x832 editorial front page
summarising the world's news of Thursday 26 November 2026). This program
copies it, byte for byte, to the output directory. Standard library only,
no network, no randomness: two runs write identical bytes.
"""

import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    if not os.path.isfile(source):
        print("missing", source, file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        out_dir = "/output" if os.path.isdir("/output") else "output"
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, dest)
    print("wrote", dest)
    return 0


if __name__ == "__main__":
    sys.exit(main())
