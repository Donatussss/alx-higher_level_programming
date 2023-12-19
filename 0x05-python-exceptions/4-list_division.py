#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    temp = None
    result_list = []

    while i < list_length:
        try:
            temp = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            temp = 0
        except TypeError:
            print("wrong type")
            temp = 0
        except IndexError:
            print("out of range")
            temp = 0
        finally:
            i += 1
            result_list.append(temp)
    return result_list
