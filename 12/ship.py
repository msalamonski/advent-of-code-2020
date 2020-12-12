#!/usr/bin/python3
''' AoC 12 -- ./ship.py 12.ex '''
import fileinput
from angles import normalize

def ship():
    ''' What is the distance between the end location and starting position? '''
    # move a cursor/add values to variables according to certain rules per line
    east, north = 0, 0
    face = 0 # east
    for line in fileinput.input():
        line = line.strip()
        num = int(line[1:])
        print('MOVING:: east: ' + str(east) + ' | north: ' + str(north))
        if 'N' in line:
            north += num
        if 'S' in line:
            north -= num
        if 'E' in line:
            east += num
        if 'W' in line:
            east -= num
        if 'L' in line:
            face += num
        if 'R' in line:
            face -= num
        if 'F' in line:
            face = normalize(face)
            print(face)
            if face == 0:
                east += num
            if face == 90:
                north += num
            if face == 180:
                east -= num
            if face == 270:
                north -= num
            ###
    print('east: ' + str(east) + ' | north: ' + str(north))
    print('manhattan distance: ' + str(abs(east) + abs(north)))

    return None
    
if __name__ == '__main__':
    ship()
