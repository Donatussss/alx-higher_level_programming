#!/usr/bin/python3
"""
replace_in_list - a function that replaces an element
of a list at a specific position (like in C)
If idx is negative, the function should not modify anything,
and returns a copy of the original list
If idx is out of range (> of number of element in my_list),
the function should not modify anything, and returns
a copy of the original list
You are not allowed to import any module
You are not allowed to use try/except
"""


def new_in_list(my_list, idx, element):
    temp = my_list[:]
    if idx < 0 or idx >= len(my_list):
        return temp
    temp[idx] = element
    return temp
