#!/usr/bin/python3
"""
search_replace -  a function that replaces all
occurrences of an element by another in a new list
my_list is the initial list
search is the element to replace in the list
replace is the new element
You are not allowed to import any module
"""


def search_replace(my_list, search, replace):
    return [i if i != search else replace for i in my_list]
