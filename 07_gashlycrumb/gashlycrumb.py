#!/usr/bin/env python3
"""
Author : Ted Osborne <ted@tedosborne.com>
Date   : 2020-10-20
Purpose: Gashlycrumb
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Gashlycrumb",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "letter", metavar="letter", nargs="+", type=str, help="letter(s)"
    )

    parser.add_argument(
        "-f",
        "--file",
        help="input file",
        metavar="FILE",
        type=argparse.FileType("rt"),
        default="gashlycrumb.txt",
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    # Use a dictionary comprehension here.
    gashlycrumbs = {line[0].upper(): line.rstrip() for line in args.file}

    for letter in args.letter:
        print(gashlycrumbs.get(letter.upper(), f'I do not know "{letter}".'))


# --------------------------------------------------
if __name__ == "__main__":
    main()
