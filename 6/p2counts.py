#!/usr/bin/python3
''' AoC 6 PART 2 -- ./p2counts.py 6.ex'''
import fileinput

def sum_counts():
    ''' sum of count of unique letters '''
    lett = 'abcdefghijklmnopqrstuvwxyz'
    yes, yes_total, ques, people = 0, 0, '', []
    for line in fileinput.input():
        if len(line.strip()) > 0:
            ques += line.strip()
            print(ques)
            people.append(ques)
            continue
        yes = 0
        for l in lett:
            lcou = ques.count(l)
            if lcou == len(people):
                yes += 1
        print(yes)
        yes_total += yes
        
        yes, ques, people = 0, '', []
        print('---')
    return 'total: ' + str(yes_total)

if __name__ == '__main__':
    print(sum_counts())
