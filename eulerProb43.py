#SOLVED
from itertools import permutations
pList = list(permutations([0,1,2,3,4,5,6,7,8,9]))
sList = []
for p in pList:
    s = ''
    if(p[3]%2 != 0): continue
    if(sum(p[2:5])%3 != 0): continue
    if(p[5] % 5 !=0): continue
    if((p[4] * 10 + p[5] - 2 * p[6]) % 7 !=0): continue
    if((p[5] - p[6] + p[7]) % 11 !=0 ): continue
    if((100*p[6] + 10 *p[7] + p[8]) % 13 != 0): continue
    if((100*p[7] + 10 *p[8] + p[9]) % 17 != 0): continue
    for d in p:
        s += str(d)
    sList.append(int(s))
print(len(sList), sList[0:5])
print("sum", sum(sList))
