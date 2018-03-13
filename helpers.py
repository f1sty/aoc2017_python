# -*- coding: utf-8 -*-
""" Helper functions for common tasks in AoC solutions. """


def read_and_split(input_filename):
    with open(input_filename, 'r') as f:
        parsed = f.readlines()

    return [line.strip().split() for line in parsed]


def digits(input_list):
    return [int(digit) for digit in input_list]


def min_max(input_list):
    return min(input_list), max(input_list)
