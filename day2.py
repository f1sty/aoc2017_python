# -*- coding: utf-8 -*-
"""
URL: http://adventofcode.com/2017/day/2

Part 1:
The spreadsheet consists of rows of apparently-random numbers. To make sure
the recovery process is on the right track, they need you to calculate the
spreadsheet's checksum. For each row, determine the difference between the
largest value and the smallest value; the checksum is the sum of all of
these differences.

Part 2:
It sounds like the goal is to find the only two numbers in each row where
one evenly divides the other - that is, where the result of the division
operation is a whole number. They would like you to find those numbers on
each line, divide them, and add up each line's result.

Examples:
---------

    >>> get_answer('inputs/day2_part_one_test', part=1)
    18
    >>> get_answer('inputs/day2_part_two_test', part=2)
    9
"""
from helpers import read_and_split, digits, min_max


def get_answer(puzzle_input_filename, part=1):
    if part == 1:
        part_func = _part_one_func
    elif part == 2:
        part_func = _part_two_func
    else:
        part_func = _part_one_func

    parsed_input = read_and_split(puzzle_input_filename)

    return sum(part_func(input_row) for input_row in parsed_input)


def _part_one_func(puzzle_row):
    in_min, in_max = min_max(digits(puzzle_row))
    return in_max - in_min


def _part_two_func(puzzle_row):
    from math import gcd

    parsed = sorted(digits(puzzle_row))
    while parsed != []:
        denominator, *parsed = parsed
        numerator = list(filter(lambda digit:
                         abs(denominator * digit) // gcd(denominator, digit)
                         in range(denominator, digit + 1), parsed))
        if numerator:
            return numerator.pop() // denominator
    return 0


if __name__ == '__main__':
    import doctest
    doctest.testmod()
