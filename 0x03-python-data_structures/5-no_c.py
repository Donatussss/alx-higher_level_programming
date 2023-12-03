#!/usr/bin/python3
"""
no_c - a function that removes all characters
c and C from a string
The function should return the new string
You are not allowed to import any module
You are not allowed to use str.replace()
"""


def no_c(my_string):
    out_string = ''
    for i in my_string:
        if i not in ['C', 'c']:
            out_string += out_string.join(i)
    return out_string
