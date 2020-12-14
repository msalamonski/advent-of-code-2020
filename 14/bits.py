#!/usr/bin/python3
''' AoC 14 -- ./bits.py 14.ex '''
import fileinput
import re

def bits():
    ''' what is the sum of all values left in memory? '''
    mask = ''
    memnum = 0
    mem = [0 for x in range(70000)]
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
                if bit == '0':
                    val[i] = '0'
                if bit == '1':
                    val[i] = '1'
                i += 1
            result = ''.join(val)
            print('result: ' + result)
            mem[memnum] = int(result, 2)
    
    return sum(mem)

if __name__ == '__main__':
    print(bits())
