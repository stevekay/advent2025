#!/usr/bin/python3

import fileinput

partone = 0
parttwo = 0

for bank in open(0).readlines():
    print(bank.strip())
    highest = -1
    highestpos = -1
    for pos in range(0,len(bank.strip())-1):
        battery = int(bank[pos])
        print(" pos=",pos,"value=",battery)
        if battery > highest:
            highest = battery
            highestpos = pos
    print("highest battery was",highest,"at pos",highestpos)
    zhighest = -1
    for pos in range(highestpos+1,len(bank.strip())):
        battery = int(bank[pos])
        if battery > zhighest:
            zhighest = battery
    print("so best combo was",highest,zhighest)
    v = highest * 10 + zhighest
    print(v)
    partone += v

print(partone)

