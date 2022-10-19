#SOLVED
from itertools import combinations
from decimal import *
getcontext().prec = 10000

def shortestCycle(longFloat):
    numStr = str(longFloat)[2:]
    leng = len(numStr)
    allSub = []
    for i in range(1, int(leng/2 + 1)):
        allSub.append(numStr[leng-i:leng])
    for sub in allSub:
        sub = str(sub)
        if(numStr.count(10*sub)>0):
            return sub
    return '0'


maxim = ['0', 0]
cur = 0
for M in range(2,1000):
    cur = shortestCycle(Decimal(1)/Decimal(M))
    if(len(cur)>len(maxim[0])):
        maxim = [cur, M]
        print("New at M =", M, "length =",len(maxim[0]))

    if(M%20==0): print(M)

print(maxim, len(maxim[0]))

    
