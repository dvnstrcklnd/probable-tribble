"""
Tools for processing lists and strings
"""
__author__ = "Devin Strickland"
__maintainer__ = "Devin Strickland"
__email__ = "dvn.strcklnd@gmail.com"
__copyright__ = "Copyright 2021, Devin Strickland"

from sys import stderr
from argparse import ArgumentParser, Namespace
from re import search, findall

def main():
    """
    Parse args, do function specified by the first argument, raise exception if unable to.
    """
    parser = get_argument_parser()
    args = parser.parse_args()
    try:
        args.func(args)
    except AttributeError:
        parser.print_help(stderr)

def get_argument_parser() -> ArgumentParser:
    """
    Get command line arguments.
    """
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
    """
    Given a list of integers and a threshold, count the numer of integers in the list
        that are above and below the threshold (non inclusive). Print the result.

    Args:
        args (Namespace): the args from ArgumentParser, must include `list` and `value`

    Returns:
        None
    """
    if search(r"\d*\.\d*", str(args.list)):
        print("This function accepts only lists of integers.")
        return

    list = [int(i) for i in findall(r"\d+", str(args.list))]
    value = int(args.value)
    print(formatted_count_above_below(list, value))

def formatted_count_above_below(lst: list, val: int) -> str:
    """
    Given a list of integers and a threshold, count the numer of integers in the list
        that are above and below the threshold (non inclusive).

    Args:
        lst (list): list of integers
        val (int): the threshold

    Returns:
        str: a formatted string reporting the results
    """
    below, above = count_above_below(lst, val)
    return "above: {}, below: {}.".format(above, below)

def count_above_below(lst: list, val: int) -> tuple:
    """
    Given a list of integers and a threshold, count the numer of integers in the list
        that are above and below the threshold (non inclusive).

    Args:
        lst (list): list of integers
        val (int): the threshold

    Returns:
        tuple: (number below, number above)
    """
    below = 0
    above = 0
    for i in lst:
        if i < val:
            below += 1
        elif i > val:
            above += 1

    return (below, above)

def do_rotate_string(args: Namespace) -> None:
    """
    Given a string and an integer n, rotate it by removing n characters from the end
        and placing them at the beginning. If n is negative, removes from the beginning
        and places at the end. Prints the result.

    Args:
        args (Namespace): the args from ArgumentParser, must include `string` and `number`

    Returns:
        None
    """
    string = str(args.string)
    number = int(args.number)

    try:
        print(rotate_string(string, number))
    except IndexError as err:
        print(err)

def rotate_string(string: str, n: int) -> str:
    """
    Given a string and an integer n, rotate it by removing n characters from the end
        and placing them at the beginning. If n is negative, removes from the beginning
        and places at the end.

    Args:
        string (str): the string to rotate
        n (int): the number of characters to rotate

    Returns:
        string: the rotated string

    Raises:
        IndexError: You cannot rotate the string by more than its length!
    """
    if abs(n) > len(string):
        raise IndexError("You cannot rotate the string by more than its length!")
    return string[-n:] + string[:-n]

if __name__ == "__main__":
    main()