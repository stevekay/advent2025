#!/usr/bin/python3

import fileinput

pos = 50
partone = 0
parttwo = 0

for b in open(0).readlines():
    direction = b[:1]
    turns = int(b.strip()[1:])
    z = 0
    if direction == 'L':
        for c in range(0,turns):
            pos -= 1
            if pos == 0 and c+1 < turns:
                z += 1
            if pos < 0:
                pos += 100
    else:
        for c in range(0,turns):
            pos += 1
            if pos == 100 and c+1 < turns:
                z += 1
            if pos > 99:
                pos -= 100

    partone += (pos==0)
    parttwo += z

print(partone,partone+parttwo)
