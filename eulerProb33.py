#SOLVED
from itertools import permutations
import numpy as np
rList = list(permutations("123456789", 2))
rList2 = []
for q in rList:
    rList2.append((q[0]+q[1]))
for i in range(1, 10):
    rList2.append(str(11*i))
rList2.sort()
iList = rList2

d = lambda st, place : int(st[place])

def getDCFs(iList):
    dcfList = []
    for deno in iList:
        for nume in iList:
            cancel0, cancel1 = -1,-1
            den0, den1 = d(deno, 0), d(deno, 1)
            num0, num1 = d(nume, 0), d(nume, 1)
            if(int(nume)>=int(deno)): break
            if(den0 == num1):
                cancel0 = num0 / den1
            if(den1 == num0):
                cancel1 = num1 / den0
            if(round(int(nume)/int(deno), 4) == round(cancel0, 4) or round(int(nume)/int(deno), 4) == round(cancel1, 4)):
                dcfList.append(nume + "/" + deno)
    return dcfList

#print(getDCFs(iList))
# ['16/64', '26/65', '19/95', '49/98']
# 1/4 * 2/5 * 1/5 * 1/2
# 1/4 * 1/5 * 1/5

