#!/usr/bin/env python3
"""
Author : Ted Osborne <ted@tedosborne.com>
Date   : 2020-10-07
Purpose: Encode numbers using "jump the five".
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Jump the Five",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("input", metavar="str", help="input text to encode")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    encodings = {
        "1": "9",
        "2": "8",
        "3": "7",
        "4": "6",
        "5": "0",
        "6": "4",
        "7": "3",
        "8": "2",
        "9": "1",
        "0": "5",
    }

    args = get_args()
    for char in args.input:
        print(encodings.get(char, char), end="")
    print()


# --------------------------------------------------
if __name__ == "__main__":
    main()
