#!/usr/bin/python3
"""
uniq_add - a function that adds all unique
integers in a list (only once for each integer)
You are not allowed to import any module
"""


def uniq_add(my_list=[]):
    out_sum = 0
    for id_i, i in enumerate(my_list):
        if i not in my_list[:id_i]:
            out_sum += i
    return out_sum
