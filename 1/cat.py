#!/usr/bin/python3
'''
    Day 1 Advent of Code Challenge
    https://adventofcode.com/2020/day/1
'''
with open('input.txt', 'r') as i:
    INP = i.readlines()
    INP = [x.strip() for x in INP]

def cat():
    ''' find two entries that sum to 2020, and multiply them '''
    for x in INP:
        x = int(x)
        for y in INP:
            y = int(y)
            print(str(x) + ' + ' + str(y) + ' == ' + str(x + y))
            if x + y == 2020:
                return 'final answer is: ' + str(x * y)
    return 'not found'

if __name__ == '__main__':
    print(cat())
