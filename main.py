#!/usr/bin/env python3
"""news-image-20261120 entry: write the bundled entry image as entry.png."""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "bundled_entry.png")


def main():
    if not os.path.isfile(SOURCE):
        sys.exit("error: bundled_entry.png not found next to main.py")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(HERE, "output")
    os.makedirs(out_dir, exist_ok=True)

    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, dest)

    print("Wrote %s (%d bytes)" % (dest, os.path.getsize(dest)))


if __name__ == "__main__":
    main()
