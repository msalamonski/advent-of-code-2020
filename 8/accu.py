#!/usr/bin/python3
''' AoC 8 -- ./accu.py 8.ex'''
import fileinput

def accumulator():
    ''' what value is in the accumulator '''
    inst = []
    cur, acc, = 0, 0
    for line in fileinput.input():
        inst.append(line.strip())
    while True:
        step = inst[cur]
        if step == '!':
            return acc
        inst[cur] = '!'
        if 'acc' in step:
            acc += int(step.split()[1])
            cur += 1
        elif 'jmp' in step:
            cur += int(step.split()[1])
        else:
            cur += 1
        print(str(cur) + ' ' + step + ': ' + str(acc))
        step = '!'
    return None

def fix_acc():
    ''' fix the accumulator (part 2) (incomplete) '''
    # generate lists
    inst = []
    x = []
    skip = 0
    for line in fileinput.input():
        inst.append(line.strip())
    # make a list of lists. if val in item, replace. else, return item.
    for i in range(0, len(inst)):
        if 'jmp' in inst[i]:
            x.append(inst[i].replace('jmp', 'nop'))
            break
    # make each list in the list change only one item. increment skip, and break
    print(inst)
    print([x for i in x]) # list comprehension

    return None

if __name__ == '__main__':
    print(accumulator()) # part 1
    # print(fix_acc()) # part 2
