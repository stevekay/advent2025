#!/usr/bin/python3

import fileinput

partone = 0
parttwo = 0

for l in open(0).readlines():
    for r in l.split(','):
        for id in range(int(r.split('-')[0]),int(r.split('-')[1])+1):
            first = str(id)[0:int(len(str(id))/2)]
            if first+first == str(id):
                partone += id

print(partone)
