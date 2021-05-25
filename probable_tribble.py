"""
Tools for processing lists and strings
"""
__author__ = "Devin Strickland"
__maintainer__ = "Devin Strickland"
__email__ = "dvn.strcklnd@gmail.com"
__copyright__ = "Copyright 2021, Devin Strickland"

from sys import stderr
from argparse import ArgumentParser, Namespace

def main():
    parser = get_argument_parser()
    args = parser.parse_args()
    try:
        args.func(args)
    except AttributeError:
        parser.print_help(stderr)

def get_argument_parser() -> ArgumentParser:
    parser = ArgumentParser(
        description="Process lists and strings")

    subparsers = parser.add_subparsers(title="subcommands")

    parser_count_above_below = subparsers.add_parser("count-above-below")
    parser_count_above_below.add_argument('-l', '--list', nargs='+',
                                         help="the list of integers to be processed")
    parser_count_above_below.add_argument('-v', '--value',
                                         help="the value that items are above or below")
    parser_count_above_below.set_defaults(func=do_count_above_below)

    parser_rotate_string = subparsers.add_parser("rotate-string")
    parser_rotate_string.add_argument('-s','--string',
                                      help="the string to rotate")
    parser_rotate_string.add_argument('-n', '--number',
                                      help="the number of letters to rotate")
    parser_rotate_string.set_defaults(func=do_rotate_string)

    return parser

def do_count_above_below(args: Namespace) -> None:
    print(formatted_count_above_below(args.list, args.value))

def formatted_count_above_below(lst: list, val: int) -> str:
    below, above = count_above_below(lst, val)
    return "above: {}, below: {}.".format(above, below)

def count_above_below(lst: list, val: int) -> tuple:
    below = 0
    above = 0
    for i in lst:
        if i < val:
            below += 1
        elif i > val:
            above += 1

    return (below, above)

def do_rotate_string(args: Namespace) -> None:
    print(rotate_string(args.string, args.number))

def rotate_string(string: str, n: int) -> str:
    if abs(n) > len(string):
        raise IndexError("You cannot rotate the string by more than its length!")
    return string[-n:] + string[:-n]

if __name__ == "__main__":
    main()