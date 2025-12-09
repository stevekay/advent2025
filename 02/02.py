#!/usr/bin/python3

import fileinput

pone = { }
ptwo = { }
for l in open(0).readlines():
    for r in l.split(','):
        for id in range(int(r.split('-')[0]),int(r.split('-')[1])+1):
            z = { }
            sid = str(id)
            if len(sid) > 1:
                z[sid[0]] = None
            if len(sid) > 3:
                z[sid[0:2]] = None
            if len(sid) > 5:
                z[sid[0:3]] = None
            if len(sid) > 7:
                z[sid[0:4]] = None
            if len(sid) == 10:
                z[sid[0:5]] = None

            for p in z:
                reps = int(len(sid) / len(p))
                if sid == p * reps:
                    if reps == 2:
                        pone[id] = None
                    ptwo[id] = None

print(sum(list(pone.keys())),sum(list(ptwo.keys())))
