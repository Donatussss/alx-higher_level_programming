#!/usr/bin/python3
"""
square_matrix_simple -a function that computes the 
square value of all integers of a matrix
matrix is a 2 dimensional array
Returns a new matrix:
Same size as matrix
Each value should be the square of the value of the input
Initial matrix should not be modified
You are not allowed to import any module
You are allowed to use regular loops, map, etc
"""


def square_matrix_simple(matrix=[]):
    out_matrix = []
    for i in matrix:
        out_row = []
        for j in i:
            out_row.append(j*j)
        out_matrix.append(out_row)
    return out_matrix
