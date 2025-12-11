#!/usr/bin/python3

import fileinput
import re

partone = 0
ranges = []

for x in open(0).readlines():
    z = re.match(r'(\d+)-(\d+)', x)
    if z:
        ranges.append( [int(z.group(1)), int(z.group(2))] )

    z = re.match(r'(\d+)$', x)
    if z:
        i = int(z.group(1))
        for [start,end] in ranges:
            if i >= start and i <= end:
                partone += 1
                break

print(partone)


