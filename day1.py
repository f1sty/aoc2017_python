# -*- coding: utf-8 -*-
"""
URL: http://adventofcode.com/2017/day/1

Part 1:
The captcha requires you to review a sequence of digits (your puzzle input)
and find the sum of all digits that match the next digit in the list.
The list is circular, so the digit after the last digit is the first digit
in the list.

Part 2:
Now, instead of considering the next digit, it wants you to consider the
digit halfway around the circular list. That is, if your list contains
10 items, only include a digit in your sum if the digit 10/2 = 5 steps
forward matches it. Fortunately, your list has an even number of elements.

Examples:
---------

    >>> get_answer(1122, part=1)
    3
    >>> get_answer(1234, part=1)
    0
    >>> get_answer(91212129, part=1)
    9
    >>> get_answer(1212, part=2)
    6
    >>> get_answer(1221, part=2)
    0
    >>> get_answer(123425, part=2)
    4
    >>> get_answer(123123, part=2)
    12
    >>> get_answer(12131415, part=2)
    4
"""
from itertools import cycle


def get_answer(puzzle_input, part=1):
    length = len(str(puzzle_input))
    digits = cycle(str(puzzle_input))
    if part == 1:
        step = 1
    else:
        step = length // 2

    digits_list = []

    for _ in range(length + step):
        digits_list.append(next(digits))

    answer = 0

    for index in range(length):
        if digits_list[index] == digits_list[index+step]:
            answer += int(digits_list[index])

    return answer


if __name__ == "__main__":
    import doctest
    doctest.testmod()
