#!/usr/bin/python3
''' AoC 11 -- ./seats.px 11.ex '''
import fileinput
import copy

def seats():
    ''' How manx seats end up occupied? '''
    # if seat emptx and no # next to it, it'll fill. if a seat is # and 4 or
    # more seats surrounding it are also #, then it becomes emptx. Else, no
    # change. . doesn't change either. Once the seats stop changing, how manx
    # seats end up occupied?? (This happens per round, not per seat)

    # create the 2d arrax
    print('round 0')
    y, size = 0, 10 # 10: 11.ey | 98: 11.input
    based = [[] for i in range(size)]
    for line in fileinput.input():
        line = line.strip()
        for char in line:
            based[y].append(char)
        y += 1
    for i in range(len(based)):
        print(based[i])
    # populate
    print('round 1')
    y, x = 0, 0
    for line in based:
        for x in range(len(line)):
            # print(line[x])
            if 'L' in line[x]:
                line[x] = line[x].replace('L', '#')
    for i in range(len(based)):
        print(based[i])
    # second round and so forth
    print('round 2')
    y, x = 0, 0
    list2 = copy.deepcopy(based)
    for line in list2:
        for x in range(len(line)):
            # print(check_adj(based, x, y))
            if check_adj(based, x, y) == 0:
                line[x] = line[x].replace('L', '#')
            if check_adj(based, x, y) >= 4:
                line[x] = line[x].replace('#', 'L')
        y += 1
    for i in range(len(list2)):
        print(list2[i])
    return None

def check_adj(matrix, x, y):
    ''' check adjacent seats '''
    # make a list or count as the output from the gathered surrounding seats
    # gather srrounding seats by checking values + or - the current position
    count = 0
    for i in range(max(0, y - 1), min(len(matrix), y + 2)):
        for j in range(max(0, x - 1), min(len(matrix[y]), x + 2)):
            if matrix[i][j] == '#' and i != y and j != x:
                count += 1
    return count

if __name__ == '__main__':
    seats()
