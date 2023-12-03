#!/usr/bin/python3
"""
 multiple_returns - a function that returns a
 tuple with the length of a string and its first character
 If the sentence is empty, the first character should be equal to None
 You are not allowed to import any module
"""


def multiple_returns(sentence):
    if len(sentence) == 0:
        return (0, None)
    else:
        return (len(sentence), sentence[0])
