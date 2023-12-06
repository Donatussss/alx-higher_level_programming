#!/usr/bin/python3
"""
common_elements - a function that returns a set
of common elements in two sets
You are not allowed to import any module
"""


def common_elements(set_1, set_2):
    out_set = set()
    larger_set = set_1 if len(set_1) > len(set_2) else set_2
    other_set = set_1 if larger_set == set_2 else set_1

    for i in larger_set:
        if i in other_set:
            out_set.add(i)

    return out_set
