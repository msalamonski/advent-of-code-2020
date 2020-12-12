#!/usr/bin/python3
''' AoC 12 -- ./ship.py 12.ex '''
import fileinput
from angles import normalize

east, north = 0, 0
face = 0 # east
wp_e, wp_n = 10, 1 # waypoint
wps_e, wps_n = 0, 0 # waypoint ship (for part 2)
for line in fileinput.input():
    num = int(line.strip()[1:])
    if 'N' in line:
        north += num
        wp_n += num
    if 'S' in line:
        north -= num
        wp_n -= num
    if 'E' in line:
        east += num
        wp_e += num
    if 'W' in line:
        east -= num
        wp_e -= num
    if 'L' in line:
        face += num
        face = normalize(face)
        while num:
            wp_e, wp_n = -wp_n, wp_e
            num -= 90
    if 'R' in line:
        face -= num
        face = normalize(face)
        while num:
            wp_e, wp_n = wp_n, -wp_e
            num -= 90
    if 'F' in line:
        face = normalize(face)
        if face == 0:
            east += num
        if face == 90:
            north += num
        if face == 180:
            east -= num
        if face == 270:
            north -= num
        for i in range(num):
            wps_e += wp_e
            wps_n += wp_n

print('part 1:')
print('east: ' + str(east) + ' | north: ' + str(north))
print('manhattan distance: ' + str(abs(east) + abs(north)))
print('part 2:')
print('east: ' + str(wps_e) + ' | north: ' + str(wps_n))
print('manhattan distance: ' + str(abs(wps_e) + abs(wps_n)))
