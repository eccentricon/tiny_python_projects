#!/usr/bin/env python3
"""
Author : Ted Osborne <ted@tedosborne.com>
Date   : 2020-10-13
Purpose: Howler (upper-cases input)
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Howler upper-cases input",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("text", help="input string or file", metavar="text", type=str)

    parser.add_argument(
        "-o",
        "--outfile",
        help="output filename",
        metavar="FILE",
        type=argparse.FileType("wt"),
        default=None,
    )

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    out_fh = args.outfile if args.outfile else sys.stdout
    out_fh.write(args.text.upper() + "\n")
    out_fh.close()


# --------------------------------------------------
if __name__ == "__main__":
    main()
