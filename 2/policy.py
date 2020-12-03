#!/usr/bin/python3
''' AoC 2 -- part 1 '''
with open('input.txt', 'r') as i:
    INP = i.readlines()
    INP = [x.strip() for x in INP] # take out \n from readlines()

def parse():
    ''' parse input lines, and validate if password meets policy'''
    valid = 0 # number of valid passwords
    for line in INP:
        par = line.split(' ')
        freq = par[0].split('-') # frequency
        lett = par[1][0] # letter/character
        pasw = par[2] # password

        if int(freq[0]) <= occurances(lett, pasw) <= int(freq[1]):
            valid += 1
    return valid

def occurances(lett, pasw):
    ''' find occurances of a letter in a password '''
    occ = 0
    for char in list(pasw): # for each character in the password
        if char == lett: # if the selected character matches the letter
            occ += 1
    return occ

if __name__ == '__main__':
    print(parse())
