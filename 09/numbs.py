#!/usr/bin/python3
''' AoC 9 -- ./numbs.py 9.input '''
import fileinput

def numbs():
    ''' find the num which is not the sum of two of the 25 nums before it '''
    nums, pre = [], 25 # pre = preamble length | 5 for 9.ex, 25 for 9.input
    for line in fileinput.input():
        nums.append(int(line.strip()))
    for thing in range(pre + 1, len(nums)):
        sumlist, prenums = [], nums[thing - pre - 1:thing]
        set_ = range(0, len(prenums))
        print('working with set: ' + str(prenums))
        sumlist = [int(prenums[int(x)]) + int(prenums[int(y)]) for x in set_ for y in set_]
        print('list of sums: ' + str(sumlist))
        ifpre = lambda item: bool(item == prenums[pre])
        fil = filter(ifpre, sumlist)
        confirmed = len(list(fil))
        print('number of confirmed sums: ' + str(confirmed))
        if confirmed == 0:
            print(encw(prenums[pre], nums)) # part 2
            return 'Answer: ' + str(prenums[pre])
        print('^^^ selected number: ' + str(prenums[pre]) + ' ^^^')
    return None

def encw(ans, nums):
    ''' what is the encryption weaknes in the list of numbers? '''
    while True:
        set_ = range(0, len(nums))
        for x in set_:
            for y in set_:
                conlist = nums[x:y] # contiguous list
                sum_ = sum(conlist)
                if sum_ > ans: # start over
                    continue
                if sum_ == ans: # found the contiguous set
                    conlist.sort()
                    p2ans = conlist[0] + conlist[-1]
                    return 'part 2 answer: ' + str(p2ans)

if __name__ == '__main__':
    print(numbs()) # part 1
