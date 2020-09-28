#!/usr/bin/env python3
"""
Author : Ted Osborne <ted@tedosborne.com>
Date   : 2020-09-27
Purpose: Announce the appearance of something "off the larboard bow" to the
         captain of the ship.
"""

import argparse

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Crow's Nest -- choose the correct article",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("word", metavar="word", help="A word")
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    word = get_args().word
    article = "an" if word[0].lower() in "aeiou" else "a"
    print(f"Ahoy, Captain, {article} {word} off the larboard bow!")


# --------------------------------------------------
if __name__ == "__main__":
    main()
