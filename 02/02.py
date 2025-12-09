#!/usr/bin/python3

import fileinput

pone = { }
ptwo = { }

for l in open(0).readlines():
    for r in l.split(','):
        print(r)
        for id in range(int(r.split('-')[0]),int(r.split('-')[1])+1):
#            print(id)
            first = str(id)[0:int(len(str(id))/2)]
            if first+first == str(id):
                pone[id] = None

            # part two
            # Now, an ID is invalid if it is made only of some sequence of digits repeated at least twice.
           
            z = { }
            sid = str(id)
            if len(sid) == 2:
                z[sid[0]]='x'
            if len(sid) == 3:
                z[sid[0]]='x'
            if len(sid) == 4:
                z[sid[0]]='x'
                z[sid[0:2]]='x'
            if len(sid) == 5:
                z[sid[0]]='x'
                z[sid[0:2]]='x'
            if len(sid) == 6:
                z[sid[0]]='x'
                z[sid[0:2]]='x'
                z[sid[0:3]]='x'
            if len(sid) == 7:
                z[sid[0]]='x'
                z[sid[0:2]]='x'
                z[sid[0:3]]='x'
            if len(sid) == 8:
                z[sid[0]]='x'
                z[sid[0:2]]='x'
                z[sid[0:3]]='x'
                z[sid[0:4]]='x'
            if len(sid) == 9:
                z[sid[0]]='x'
                z[sid[0:2]]='x'
                z[sid[0:3]]='x'
                z[sid[0:4]]='x'
            if len(sid) == 10:
                z[sid[0]]='x'
                z[sid[0:2]]='x'
                z[sid[0:3]]='x'
                z[sid[0:4]]='x'
                z[sid[0:5]]='x'
            if len(sid) > 10:
                print("more than 10, len=",len(sid))
                exit()

#            print("search list is",z)
            for p in z:
                reps = int(len(sid) / len(p))
                c = 0
                ss = ''
                while c < reps:
                    ss = ss + p
                    c += 1
#                print("processing possibility",p,"reps=",reps,"ss=",ss)
#                print("comparing ",sid,"with",ss)
                if sid == ss:
                    print("   DUPLICATE",sid)
                    ptwo[id] = None


print("part one",sum(list(pone.keys())))
print("part two",sum(list(ptwo.keys())))

# notes
# 6161588270-6161664791
#  DUPLICATE 6161616161
#  DUPLICATE 6161661616 <<<<<< wrong!

# 25894449318 is too low
# 25912654324 not right
