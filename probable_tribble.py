"""
Tools for processing lists and strings
"""
__author__ = "Devin Strickland"
__maintainer__ = "Devin Strickland"
__email__ = "dvn.strcklnd@gmail.com"
__copyright__ = "Copyright 2021, Devin Strickland"

import sys
import argparse

def main():
    parser = get_argument_parser()
    args = parser.parse_args()
    try:
        args.func(args)
    except AttributeError:
        parser.print_help(sys.stderr)

def get_argument_parser():
    parser = argparse.ArgumentParser(
        description="Process lists and strings")

    subparsers = parser.add_subparsers(title="subcommands")

    parser_count_over_under = subparsers.add_parser("count-over-under")
    parser_count_over_under.add_argument('-l', '--list', nargs='+',
                                         help="the list of integers to be processed")
    parser_count_over_under.add_argument('-v', '--value',
                                         help="the value that items are over or under")
    parser_count_over_under.set_defaults(func=do_count_over_under)

    parser_rotate_string = subparsers.add_parser("rotate-string")
    parser_rotate_string.add_argument('-s','--string',
                                      help="the string to rotate")
    parser_rotate_string.add_argument('-n', '--number',
                                      help="the number of letters to rotate")
    parser_rotate_string.set_defaults(func=do_rotate_string)

    return parser

def do_count_over_under(args):
    print("count_over_under")
    print(args.list)
    print(args.value)

def do_rotate_string(args):
    rotate_string(args.string, args.number)

def rotate_string(string, n):
    if n > len(string):
        raise IndexError("You cannot rotate the string by more than its length!")
    return string[-n:] + string[:-n]

if __name__ == "__main__":
    main()