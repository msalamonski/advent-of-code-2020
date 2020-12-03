#!/usr/bin/python3
''' AoC 3 '''
with open('input.txt', 'r') as i:
    INP = i.readlines()
    INP = [x.strip() for x in INP] # take out \n from readlines()

def traverse(x, y):
    ''' see how many trees encountered '''
    cur = [0, 0] # x, y # cursor
    tree = 0
    for line in INP:
        if y == 2 and ((cur[1] % 2) != 0):
            continue
        if cur[1] == 0: # if you're on the first line
            cur[0] += x # right x amount of times
            cur[1] += y # down y
            continue
        if cur[0] >= len(line): # go back to left side if touching right
            cur[0] = cur[0] - len(line)
        if '#' in line[cur[0]]:
            tree += 1
        cur[0] += x
        cur[1] += y
        print('x: ' + str(cur[0]) + ' y: ' + str(cur[1]))
    return tree

if __name__ == '__main__':
    print(traverse(1, 1))
