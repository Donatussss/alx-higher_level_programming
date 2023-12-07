#!/usr/bin/python3
def best_score(a_dictionary):
    prev_value = None
    max_key = ''
    if a_dictionary is None:
        return None
    for key, value in a_dictionary.items():
        if prev_value is None:
            prev_value = value
            continue
        if value > prev_value:
            prev_value = value
            max_key = key
    return max_key
