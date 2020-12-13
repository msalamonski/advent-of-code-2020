#!/usr/bin/python3
''' AoC 13 -- ./bus.py 13.ex '''
import fileinput
import copy

def bus(): # 1000508 # 1000517 - 1000508 = 9 # 37*9 = 333
    ''' What is the ID of the earliest bus... '''
    i, timestamp, busid = 0, 0, 0
    for line in fileinput.input():
        if i == 0:
            timestamp = int(line.strip())
        else:
            busid = line.replace('x,', '').strip().split(',')
        i += 1
    newbusid = copy.deepcopy(busid)
    i = 0
    for i in range(len(busid)):
        while int(newbusid[i]) < timestamp:
            newbusid[i], busid[i] = int(newbusid[i]), int(busid[i])
            newbusid[i] += busid[i]
    return newbusid

if __name__ == '__main__':
    print(bus())
