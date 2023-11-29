def uppercase(str):
    f_str = ''
    for i in range(len(str)):
        asc = ord(str[i])
        if asc in range(97, 123):
            f_str += '{}'.format(chr(asc - 32))
        else:
            f_str += str[i]

    print('{}'.format(f_str))
