#!/usr/bin/python3
''' AoC 4 '''
from re import search

with open('input.txt', 'r') as i:
    INP = i.readlines()
    INP = [x.strip() for x in INP] # take out \n from readlines()

def passport():
    ''' count number of passports with 7 key:values present '''
    valid, new_valid, passp = 0, 0, ''
    key = 'ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt'
    for passpor in INP:
        if len(passpor) > 3:
            passp += (' ' + passpor)
            continue
        check = 0
        for k in key:
            if k in passp:
                check += 1
                if check == 7:
                    valid += 1 # for part 1
                    new_valid += valid_passport(passp) # for part 2
        passp = ''
    return 'valid passports: ' + str(new_valid)

def valid_passport(line):
    ''' count the number of passports with values present and valid '''
    key = 'ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt'
    color = 'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'
    ecl, pid, eyr, hcl, byr, iyr, hgt = '', '', '', '', '', '', ''
    valid, passp = 0, line.split()
    for k in passp: # assign values in a passport to it's respective key
        if key[0] in k:
            ecl = k[4:]
        if key[1] in k:
            pid = k[4:]
        if key[2] in k:
            eyr = k[4:]
        if key[3] in k:
            hcl = k[4:]
        if key[4] in k:
            byr = k[4:]
        if key[5] in k:
            iyr = k[4:]
        if key[6] in k:
            hgt = k[4:]
    # begin validation
    if ((1920 <= int(byr) <= 2002) and
    (2010 <= int(iyr) <= 2020) and
    (2020 <= int(eyr) <= 2030)):
        mes = validate(hgt)
        if mes[0] <= int(hgt.replace(mes[1], '')) <= mes[2]:
            if search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', hcl):
                for eye in color:
                    if eye in ecl:
                        if len(pid) == 9:
                            valid += 1
    return valid

def validate(hgt):
    ''' validate height -- check if 'cm' or 'in' in 'hgt' '''
    mes = 1, '', -1 # cause an entry with missing 'cm' or 'in' to be false
    if 'cm' in hgt:
        mes = 150, 'cm', 193
    if 'in' in hgt:
        mes = 59, 'in', 76
    return mes

if __name__ == '__main__':
    print(passport()) # note that the last line in the input is not counted
