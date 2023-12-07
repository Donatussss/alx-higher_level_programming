#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    out_sum = 0
    out_weight = 0
    for i in my_list:
        out_mul = i[0]
        for j in i[1:]:
            out_mul *= j
        out_weight += i[-1]
        out_sum += out_mul

    return out_sum / out_weight
