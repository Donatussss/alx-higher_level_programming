#!/usr/bin/python3
"""
add_tuple - a function that adds 2 tuples.
Returns a tuple with 2 integers:
The first element should be the addition of the first element
of each argument
The second element should be the addition of the second element
of each argument
You are not allowed to import any module
You can assume that the two tuples will only contain integers
If a tuple is smaller than 2, use the value 0 for each
missing integer
If a tuple is bigger than 2, use only the first 2 integers

"""


def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    a_temp = [*tuple_a[:2]]
    b_temp = [*tuple_b[:2]]

    if len_a < 2:
        [a_temp.append(0) for i in range(len_a, 2)]
    if len_b < 2:
        [b_temp.append(0) for i in range(len_b, 2)]

    return (a_temp[0] + b_temp[0], a_temp[1] + b_temp[1])
