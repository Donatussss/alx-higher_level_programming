#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    from calculator_1 import add, sub, mul, div
    op_dict = {'+': add, '-': sub, '*': mul, '/': div}
    if len(sys.argv) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        sys.exit(1)
    if sys.argv[2] not in '+-*/':
        print('Unknown operator. Available operators: +, -, * and /')
        sys.exit(1)
    print('{} {} {} = {}'.format(*sys.argv[1:], op_dict[sys.argv[2]](int(sys.argv[1]), int(sys.argv[3]))))
