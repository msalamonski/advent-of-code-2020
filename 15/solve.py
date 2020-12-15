#!/usr/bin/python3
''' AoC 15 -- ./solve.py 15.input '''
import fileinput

def solve():
    ''' find the nth number in the pattern '''
    for line in fileinput.input():
        inp = line.strip().split(',')
    mem = []
    endnow = False
    occlist = [0, 0]
    for num in inp:
        mem.append(int(num))

    while True:
        if endnow:
            return mem[2020 - 1]
        if mem[-1] in mem[:-1]:
            for turn, num in enumerate(mem, 1):
                if turn >= 2020 + 1:
                    endnow = True
                if num == mem[-1]:
                    occlist.append(turn)
            diff = occlist[-1] - occlist[-2]
            mem.append(diff)
        else:
            mem.append(0)

    return None

if __name__ == '__main__':
    print(solve())
