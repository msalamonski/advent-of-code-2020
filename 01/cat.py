#!/usr/bin/python3
''' AoC 1 '''
add_two = lambda x, y: int(x) + int(y)
mul_two = lambda x, y: int(x) * int(y)
add_three = lambda x, y, z: int(x) + int(y) + int(z)
mul_three = lambda x, y, z: int(x) * int(y) * int(z)

with open('input.txt', 'r') as i:
    INP = i.readlines()
    INP = [x.strip() for x in INP] # take out \n from readlines()

def cat():
    ''' find two entries that sum to 2020, and multiply them '''
    for x in INP:
        for y in INP:
            add = add_two(x, y)
            print(x + ' + ' + y + ' == ' + str(add))
            if add == 2020:
                return 'final answer is: ' + str(mul_two(x, y))
    return 'not found'

def threecat():
    ''' find three entries that sum to 2020, and multiply them '''
    for x in INP:
        for y in INP:
            for z in INP:
                add = add_three(x, y, z)
                print(x + ' + ' + y + ' + ' + z + ' == ' + str(add))
                if add == 2020:
                    return 'final answer is: ' + str(mul_three(x, y, z))
    return 'not found'

if __name__ == '__main__':
    print(cat())
    # print(threecat()) # uncomment for solution to part 2
