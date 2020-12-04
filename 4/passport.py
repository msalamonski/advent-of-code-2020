#!/usr/bin/python3
''' AoC 4 -- rough draft -- part 2 not yet working'''
import re

with open('input.txt', 'r') as i:
    INP = i.readlines()
    INP = [x.strip() for x in INP] # take out \n from readlines()

def passport():
    ''' count number of passports with 7 key:values present '''
    valid = 0
    new_valid = 0
    passp = ''
    for passport in INP:
        if len(passport) > 3:
            passp += (' ' + passport)
            continue
        if ('ecl' in passp and
            'pid' in passp and
            'eyr' in passp and
            'hcl' in passp and
            'byr' in passp and
            'iyr' in passp and
            'hgt' in passp):
            valid += 1
            # print(str(valid) + ':' + passp)
            new_valid += valid_passport(passp)
        passp = ''
    return 'valid passports: ' + str(new_valid) # note that the last line is not counted

def valid_passport(line):
    ''' count the number of passports with values present and valid '''
    key = 'ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt'
    color = 'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'
    ecl, pid, eyr, hcl, byr, iyr, hgt = '', '', '', '', '', '', ''
    valid = 0
    # print(line.split())
    passp = line.split()
    for k in passp:
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

        # print(byr)
    if ((1920 < int(byr) < 2002) and
    (2010 < int(iyr) < 2020) and
    (2020 < int(eyr) < 2030)):
        if 'cm' in hgt:
            if 150 < int(hgt.replace('cm', '')) < 193:
                match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', hcl)
                if match:
                    for eye in color:
                        if eye in ecl:
                            if len(pid) == 9:
                                valid += 1
        if 'in' in hgt:
            if 59 < int(hgt.replace('in', '')) < 76:
                match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', hcl)
                if match:
                    for eye in color:
                        if eye in ecl:
                            if len(pid) == 9:
                                valid += 1

    return valid


if __name__ == '__main__':
    print(passport())
