#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    l_args = len(sys.argv) - 1
    end_part = ':' if l_args == 1 else 's.' if l_args == 0 else 's:'
    print('{} argument{}'.format(l_args, end_part))
    for ind, i in enumerate(sys.argv):
        if ind > 0:
            print('{}: {}'.format(ind, i))
