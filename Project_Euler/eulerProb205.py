peter = [0] * 28
colin = [0] * 31
for q in range(4):
    for w in range(4):
        for e in range(4):
            for r in range(4):
                for t in range(4):
                    for y in range(4):
                        for u in range(4):
                            for i in range(4):
                                for o in range(4):
                                    sum1 = q + w + e + r + t + y + u + i + o
                                    peter[sum1] = peter[sum1] + 1
for q in range(6):
    for w in range(6):
        for e in range(6):
            for r in range(6):
                for t in range(6):
                    for y in range(6):
                        sum2 = q + w + e + r + t + y
                        colin[sum2] = colin[sum2] + 1

colinP = colin.copy()
peterP = peter.copy()
colinSum = sum(colin)
peterSum = sum(peter)
for i in range(len(colinP)):
    colinP[i] = colinP[i] / colinSum
for i in range(len(peterP)):
    peterP[i] = peterP[i] / peterSum
