#!/usr/bin/python3
''' AoC 7 -- ./bags.py 7.ex'''
import fileinput

bag = lambda x: str(x[0] + ' ' + x[1])

def bags():
    ''' How many bag colors can eventually contain at least one shiny gold bag? '''
    target = 'shiny gold'
    can_hold = []
    for line in fileinput.input(): # todo: make this into a function
        sent = line.strip().split()
        begg = bag(sent)
        if target in line.strip().split(' ', 2)[2]:
            if begg not in can_hold:
                can_hold.append(begg)

    i = 0
    while True:
        try:
            target = can_hold[i]
            for line in fileinput.input():
                sent = line.strip().split()
                begg = bag(sent)
                if target in line.strip().split(' ', 2)[2]:
                    if begg not in can_hold:
                        can_hold.append(begg)
            i += 1
        except IndexError:
            break
    print(can_hold)
    return len(can_hold)

def reverse_bags():
    ''' How many bags can eventually be contained into one shiny gold bag? '''
    target = 'shiny gold'
    can_hold = []
    for line in fileinput.input(): # find target's rules
        if target in line.strip():
            t_line = line.strip()
            break
    print(t_line)
    # for line in fileinput.input():

if __name__ == '__main__':
    # print(reverse_bags())
    print(bags())
