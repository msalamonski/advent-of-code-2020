#!/usr/bin/python3
''' AoC 16 -- ./solve.py 16.input '''
import fileinput

def solve():
    ''' what is your ticket scanning error rate '''
    # parse number ranges. see if nearby tickets lists fits in these numbers. if
    # not, add to errorlist. sum(errorlist) will give answer.
    for line in fileinput.input():
        if line == '':
            # beh
        else:
            line_ = line.strip().split()
            for param in line_:
                if '-' in param:
                    # 1-3 convert to range(1,3)
                    # x-y, range(x, y)

    return None

if __name__ == '__main__':
    print(solve())
