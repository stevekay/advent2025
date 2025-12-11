#!/usr/bin/python3

import fileinput

partone = 0
grid = []
for l in open(0).readlines():
    grid.append(list(l.strip()))

for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == '@':
            a = 0
            for ydelta in [ -1, 0, 1 ]:
                for xdelta in [ -1, 0, 1 ]:
                    if ydelta != 0 or xdelta != 0:
                        newy = y + ydelta
                        newx = x + xdelta
                        a += (newy < len(grid) and newy > -1 and newx < len(grid[y]) and newx > -1 and grid[newy][newx] == '@')
            if a < 4:
                partone += 1
print(partone)
