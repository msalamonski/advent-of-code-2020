#!/usr/bin/python3
''' AoC 14 Part 2 -- ./floats.py 14.2ex '''
import fileinput, re
from itertools import combinations_with_replacement

def floats():
    ''' what is the sum of all values left in memory? '''
    # part 2
    # 0's now don't do anything. 1's replace with 1's. X is a floating value, this
    # could be either 0 or 1 -- produce all possible combinations using the X's,
    # append them, and add the sum of all items in the list
    mem, memnum, mask = [0 for x in range(70000)], 0, ''
    xlist, bflist, finallist = [], [], []
    for line in fileinput.input():
        if 'mask' in line:
            mask = line.split()[2]
        if 'mem' in line:
            memnum = int(re.search(r'\[.*\]', line).group(0)[1:-1])
            mem[memnum] = line.split()[2]

            value = "{0:036b}".format(int(mem[memnum]))
            print('value:  ' + value)
            print('mask:   ' + mask)
            i = 0
            val = list(value)
            for bit in mask:
                if bit == '1':
                    val[i] = '1'
                if bit == 'X':
                    val[i] = 'X'
                i += 1
            result = ''.join(val)
            print('result: ' + result)
            xlist.append(result)
            ### mem[memnum] = int(result, 2)
    print('---')
    for x in xlist: # results
        bflist = []
        i, j = 0, 0
        for poss in combinations_with_replacement(range(2), x.count('X')):
            bflist.append(poss)
        # map(rep, x) # replace the X's in x with the bits in each item in bflist
        '''
        for b in bflist:
            for bit in x:
                if bit == 'X':
                    newx[i] = b[j]
                    j += 1
                i += 1
        
        res = ''.join(newx)
        finallist.append(res)
        '''
    # print(finallist)

    return None ### sum(mem)

if __name__ == '__main__':
    print(floats())
