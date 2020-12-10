#!/usr/bin/python3
''' AoC 10 -- ./jolts.py 10.ex '''
import fileinput

def jolts():
    ''' what is the number of 1-jolt differences multiplied by the 3-jolt diffs? '''
    # start with 0. if there's a number 1 higher then go with that first. if
    # there's 3 higher then go with that as a secondary choice. count each
    # increments of 1 and 3. multiply the 1's and 3's together. add another
    # increment of 3.
    cur = 0
    ones, threes = 0, 0
    list_ = []
    for line in fileinput.input():
        list_.append(int(line.strip()))
    list_.sort()
    print(list_)
    for num in list_:
        # print(num + '-' + str(cur) str(int(num) - cur))
        if int(num) - cur == 1:
            ones += 1
        else:
            threes += 1
        cur = num

    print('ones: ' + str(ones))
    print('threes: ' + str(threes + 1))
    mul = ones * (threes + 1)
    return mul

if __name__ == '__main__':
    print(jolts())
