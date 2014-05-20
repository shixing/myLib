#!/usr/bin/env python
'''
Author: Xing Shi
'''
import argparse


def ap():
    # argparse http://docs.python.org/2/library/argparse.html#module-argparse
    parser = argparse.ArgumentParser(description='Descriptions')

    # actions:
    # action='store_const', const=42
    # action='store_true'

    # positional arguments
    parser.add_argument('f', default=None, type=int, help="file")
    # optional arguments
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        '-a', '--arg', default=None, type=int, required=False, help="argument")
    # version info
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')
    args = vars(parser.parse_args())
    return args


def main():
    args = ap()
    print args


if __name__ == '__main__':
    main()
