#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return
    for i in matrix:
        i_len = len(i)
        for idj, j in enumerate(i):
            post_fix = '' if idj == i_len - 1 else ' '
            end_format = '' if post_fix == ' ' else '\n'
            print('{:d}{}{}'.format(j, post_fix, end_format), end='')
