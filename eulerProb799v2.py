from itertools import combinations_with_replacement
import math
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

pList = pentas(100)
combo = list(combinations_with_replacement(pList, 3))
fList = []
for i in range(len(combo)):
    comboSum = sum(combo[i])
    if(checkPenta(comboSum)):
        fList.append(comboSum)

print(fList[0:10])

