#!/usr/bin/python3

import fileinput

partone = 0
parttwo = 0

for bank in open(0).readlines():
    bank = bank.strip()

    highest_voltage = max(bank[:len(bank)-1])
    highest_position = bank.index(highest_voltage)
    next_highest_voltage = max(bank[highest_position+1:])

    partone += int(highest_voltage + next_highest_voltage)

print(partone)
