#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    out_list = []
    for i in my_list:
        out_list.append(i % 2 == 0)
    return out_list
