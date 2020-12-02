#!/usr/bin/python3
''' AoC 2 -- part 2 -- (not yet correct) '''
with open('input.txt', 'r') as i:
    INP = i.readlines()
    INP = [x.strip() for x in INP] # take out \n from readlines()

def parse():
    ''' parse input lines, and validate if password meets policy'''
    valid = 0 # number of valid passwords
    for line in INP:
        par = line.split(' ')
        pos = par[0].split('-') # position
        lett = par[1][0] # letter/character
        pasw = par[2] # password

        if (pasw[int(pos[0]) - 1] == lett) and (pasw[int(pos[1]) - 1] != lett):
            valid += 1
    return valid

if __name__ == '__main__':
    print(parse())
    # parse()
