#!/usr/bin/python3
''' AoC 6 -- ./counts.py 6.ex'''
import fileinput

def sum_counts():
    ''' sum of count of unique letters '''
    lett = 'abcdefghijklmnopqrstuvwxyz'
    ques = ''
    counts, counts_total = 0, 0
    for line in fileinput.input():
        if len(line.strip()) > 0:
            ques += line.strip()
            print(ques)
            continue
        diff = [x for x in lett if x not in ques]
        print(26 - len(diff))
        counts = 26 - len(diff)
        counts_total += counts
        
        ques = ''
    return counts_total # note that it doesn't do the last line

if __name__ == '__main__':
    print(sum_counts())
