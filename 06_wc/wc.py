#!/usr/bin/env python3
"""
Author : Ted Osborne <ted@tedosborne.com>
Date   : 2020-10-15
Purpose: Emulate wc (word count)
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Emulate wc (word count)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "files",
        help="input file(s)",
        metavar="FILE",
        type=argparse.FileType("rt"),
        nargs="*",
        default=[sys.stdin],
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    line_total = 0
    word_total = 0
    byte_total = 0
    for fh in args.files:
        line_count = 0
        word_count = 0
        byte_count = 0
        for line in fh:
            line_count += 1
            word_count += len(line.split())
            byte_count += len(line)
        print(f"{line_count:8}{word_count:8}{byte_count:8} {fh.name}")
        line_total += line_count
        word_total += word_count
        byte_total += byte_count
    if len(args.files) > 1:
        print(f"{line_total:8}{word_total:8}{byte_total:8} total")
    return 0


# --------------------------------------------------
if __name__ == "__main__":
    main()
