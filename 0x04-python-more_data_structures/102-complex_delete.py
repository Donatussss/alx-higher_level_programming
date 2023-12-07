#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if not a_dictionary:
        return None
    del_keys = []
    for key, d_value in a_dictionary.items():
        if d_value == value:
            del_keys.append(key)
    for key in del_keys:
        del a_dictionary[key]
    return a_dictionary
