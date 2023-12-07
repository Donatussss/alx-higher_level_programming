#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    num_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
    rev = roman_string[::-1]
    num = None if len(roman_string) > 0 else 0
    for id_c, c in enumerate(rev):
        if c not in num_dict:
            return 0
        if num is None:
            num = num_dict[c]
            continue
        if num_dict[c] >= num_dict[rev[id_c - 1]]:
            num += num_dict[c]
        elif num_dict[c] < num_dict[rev[id_c - 1]]:
            num -= num_dict[c]

    return num
