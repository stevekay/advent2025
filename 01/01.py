#!/usr/bin/python3

import fileinput

pos = 50
partone = 0
parttwo = 0

for b in open(0).readlines():
    direction = b[:1]
    turns = int(b.strip()[1:])

    if direction == 'L':
        for c in range(turns):
            pos -= 1
            if pos == 0 and c+1 < turns:
                parttwo += 1
            if pos < 0:
                pos += 100
    else:
        for c in range(turns):
            pos += 1
            if pos == 100 and c+1 < turns:
                parttwo += 1
            if pos > 99:
                pos -= 100

    partone += (pos==0)

print(partone,partone+parttwo)
