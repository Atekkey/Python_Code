#SOLVED
from Prime import *
def genNums(top):
    nList = []
    for i in range(0, top+1):
        for k in range(0, top+1):
            nList.append((i, k))
    return nList
def allOdd(top):
    oList = []
    for i in range(1, top+1, 2):
        oList.append(i)
    return oList
oList = allOdd(1000000)
nList = genNums(1000)
pList = primes_top(10005)
fList = []
for n in nList:
    num = pList[n[0]] + 2 * (n[1] ** 2)
    fList.append(num)
fList = list(set(fList))

for o in oList[3:]:
    if(o not in fList):
        print(o)
        break
