#!/usr/bin/env python3
"""
Author : Ted Osborne <ted@tedosborne.com>
Date   : 2020-09-29
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('items',
                        metavar='str',
                        nargs='+',
                        help='item(s) to bring')

    parser.add_argument('-s',
                        '--sorted',
                        help='sort the items',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items = args.items

    if args.sorted:
        items.sort()

    items_list = items[-1]

    if len(items) >= 3:
        items[-1] = 'and ' + items[-1]
        items_list = ', '.join(items)
    elif len(items) == 2:
        items_list = ' and '.join(items)

    print(f'You are bringing {items_list}.')

# --------------------------------------------------
if __name__ == '__main__':
    main()
