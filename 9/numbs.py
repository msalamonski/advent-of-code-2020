#!/usr/bin/python3
''' AoC 9 -- ./numbs.py 9.ex'''
import fileinput

def numbs():
    ''' find the number which is not the sum... '''
    nums = []
    for line in fileinput.input():
        nums.append(line.strip())

    pre = 25 # preamble length
    post = nums[pre:] # after preamble
    for x in range(pre + 1, len(nums)):
        prenums = nums[x - pre - 1:x]
        print(prenums)
        i = 0
        sumlist = []
        for y in range(0, len(prenums)):
            for z in range(0, len(prenums)):
                q = int(prenums[int(y)]) + int(prenums[int(z)])
                sumlist.append(q)
        print(sumlist)
        ifpre = lambda item: True if int(item) == int(prenums[pre]) else False
        fil = filter(ifpre, sumlist)
        print(list(fil))
        print('^^^' + prenums[pre] + '^^^')

    return None # the line below the first '[]' is the answer

if __name__ == '__main__':
    print(numbs()) # part 1
