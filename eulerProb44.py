#SOLVED
import math
from itertools import combinations
def pentas(ind):
    pList = []
    for n in range(1, ind+1):
        pList.append(int((n/2)*(3*n - 1)))
    return pList

def checkPenta(num):
    a, b, c = 1.5, -0.5, -num
    cur = math.sqrt(b**2 - 4*a*c)
    sol1 = (-b + cur)/(2*a)
    if(sol1==int(sol1)):
        return True
    else:
        return False
pList = pentas(3000)
combo = list(combinations(pList, 2))
store = (0,0)
minDif = 10**13
for c in combo:
    dif = abs(c[0] - c[1])
    sum = c[0] + c[1]
    if(not checkPenta(dif) or not checkPenta(sum)):
        continue
    if(dif < minDif):
        minDif = dif
        store = c
print("min =", minDif, "nums =", store)