#UNSOLVED
import math; import time
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
def genSums(ind, ways):
    pList = pentas(ind)
    sList, fList, maxCount = [], [], 0
    leng = len(pList)
    for i in range(leng):
        for k in range(i, leng):
            num = pList[i]+pList[k]
            if(checkPenta(num)):
                sList.append(num)
    for j in sList:
        if(sList.count(j)>=(ways)):
            if(sList.count(j)>maxCount): maxCount = sList.count(j)
            fList.append(j)
    fList = list(set(fList))
    fList.sort()
    print(f"maxCount = {maxCount}")
    return fList

st = time.time()
print(genSums(30000, 11))

et = time.time()
print(f"Run Time {str(et-st)[0:6]} sec")

#print(min(genSums(200,2)))
#Value, (10000, 8) returns (183413517, count:9, time: 35)
#Value, (20000, 9) returns (538587427, count: 11, time 142)
