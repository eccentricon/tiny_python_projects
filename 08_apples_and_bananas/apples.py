#!/usr/bin/env python3
"""
Author : Ted Osborne <ted@tedosborne.com>
Date   : 2020-10-22
Purpose: Apples and bananas (Ex. 08)
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Apples and bananas",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-v",
        "--vowel",
        help="the vowel to substitute",
        choices="aeiou",
        metavar="vowel",
        default="a",
    )

    parser.add_argument("text", help="input text or file", type=str, default=None)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    translations = {}
    for letter in "aeiou":
        translations[letter] = args.vowel
        translations[letter.upper()] = args.vowel.upper()

    lines = open(args.text) if os.path.isfile(args.text) else [f"{args.text}"]
    for line in lines:
        print(line.rstrip().translate(str.maketrans(translations)))


# --------------------------------------------------
if __name__ == "__main__":
    main()
