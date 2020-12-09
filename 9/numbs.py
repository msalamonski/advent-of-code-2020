#!/usr/bin/python3
''' AoC 9 -- ./numbs.py 9.input'''
import fileinput

def numbs():
    ''' find the num which is not the sum of two of the 25 nums before it '''
    nums, pre = [], 25 # pre = preamble length | 5 for 9.ex, 25 for 9.input
    for line in fileinput.input():
        nums.append(line.strip())
    for thing in range(pre + 1, len(nums)):
        sumlist, prenums = [], nums[thing - pre - 1:thing]
        set_ = range(0, len(prenums))
        print('working with set: ' + str(prenums))
        sumlist = [int(prenums[int(x)]) + int(prenums[int(y)]) for x in set_ for y in set_]
        print('list of sums: ' + str(sumlist))
        ifpre = lambda item: bool(int(item) == int(prenums[pre]))
        fil = filter(ifpre, sumlist)
        confirmed = str(len(list(fil)))
        print('number of confirmed sums: ' + confirmed)
        if int(confirmed) == 0:
            return 'Answer: ' + str(prenums[pre])
        print('^^^ selected number: ' + prenums[pre] + ' ^^^')
    return None

if __name__ == '__main__':
    print(numbs()) # part 1
