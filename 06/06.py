#!/usr/bin/python3

import fileinput

partone = 0
grid = []

for l in open(0).readlines():
    grid.append(l.split())

for col in range(len(grid[0])):
    op = grid[len(grid)-1][col]
    t = 0
    if op == '*':
        t = 1
    for row in range(len(grid)-1):
        v = int(grid[row][col])
        if op == '*':
            t *= v
        if op == '+':
            t += v
    partone += t
print(partone)
