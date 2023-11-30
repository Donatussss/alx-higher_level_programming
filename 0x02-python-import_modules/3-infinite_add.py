#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    sum_args = 0
    for i in sys.argv[1:]:
        sum_args += int(i)
    print(sum_args)
