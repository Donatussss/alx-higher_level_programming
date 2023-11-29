#!/usr/bin/python3
for ch_r in reversed(range(97, 123)):
    print("{:c}".format(ch_r if (ch_r % 2 == 0) else (ch_r - 32)), end='')
