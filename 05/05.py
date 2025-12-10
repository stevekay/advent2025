#!/usr/bin/python3

import fileinput
import re

partone = 0
ranges = []

for x in open(0).readlines():
    x = x.strip()
#    print(x)

    z = re.match(r'(\d+)-(\d+)',x)
    if z != None:
        ranges.append( [int(z.group(1)),int(z.group(2))])

    z = re.match(r'(\d+)$',x)
    if z != None:
        i = int(z.group(1))
#        print("ingredient",i)
        fresh = 0
        for [start,end] in ranges:
            if i >= start and i <= end:
                fresh = 1
#                print(" in range")
        partone += fresh
    

#print(ranges)
print(partone)
