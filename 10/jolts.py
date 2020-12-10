#!/usr/bin/python3
''' AoC 10 -- ./jolts.py 10.input '''
import fileinput
from collections import defaultdict # https://docs.python.org/3/library/collections.html

def jolts():
    ''' what is the number of 1-jolt differences multiplied by the 3-jolt diffs? '''
    list_, cur, ones, threes = [], 0, 0, 0
    for line in fileinput.input():
        list_.append(int(line.strip()))
    list_.sort()
    print(arrange(list_)) # do part 2 here
    for num in list_:
        if int(num) - cur == 1:
            ones += 1
        else:
            threes += 1
        cur = num
    print('ones: {0} | threes: {1}'.format(str(ones), str(threes + 1)))
    return 'part 1 answer: ' + str(ones * (threes + 1))

def arrange(list_):
    ''' how many distinct arrangements can there be? '''
    disarr = defaultdict(int) # a dict that creates new entries instead of keyerror
    disarr[0] = 1
    for num in list_: # at every step, jump from 1, 2, or 3; add the possibilities
        disarr[num] += disarr[num - 1] + disarr[num - 2] + disarr[num - 3]
        print('{1} + {2} + {3} = {0}'.format(disarr[num], disarr[num - 1],
              disarr[num - 2], disarr[num - 3]))
    return 'part 2 answer: ' + str(disarr[num])

if __name__ == '__main__':
    print(jolts())
