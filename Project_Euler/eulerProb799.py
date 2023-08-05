#UNSOLVED
import math; import time; #import numpy as np
tDif = lambda t1, t2 : (str(t2 - t1)[0:6] + " sec") 
tDifNum = lambda t1, t2 : (int((t2 - t1) * 10000))/10000

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
    C0 = time.time()
    pList = pentas(ind)
    sList, fList, maxCount = [], [], [0, 0]
    leng = len(pList)
    C1 = time.time()
    alpha = 1
    for i in range(int(leng/alpha)): #Changeable
        for k in range(leng-1, int(alpha * (i-1)), -1):
            num = pList[i]+pList[k]
            if(checkPenta(num)):
                sList.append(num)
    C2 = time.time()
    for j in sList:
        if(sList.count(j)>=(ways)):
            if(sList.count(j)>maxCount[0]):
                maxCount[0] = sList.count(j)
                maxCount[1] = j
            fList.append(j)
    fList = list(set(fList))
    fList.sort()
    
    C3 = time.time()
    print("\n")
    #print(f"maxCount = {maxCount}, time check|| innit : {tDif(C0, C1)}, allSums : {tDif(C1, C2)}, countWays : {tDif(C2, C3)}, timeProj : {tDif(C0,C3)}")
    #above code shows that C2-C1 or "allSums" is the slowest part by a wide margin
    print("allSums efficiency =", int(1000 * tDifNum(C1,C2) / tDifNum(C0, C3))/10, "% of total time")
    #return fList
    return maxCount

st = time.time()
maxC = genSums(10000, 8)
et = time.time()
print(f"maxCount : {maxC[0]}, maxCount Num : {maxC[1]}, Run Time : {tDif(st, et)} \n")

#if(et-st>0.01): print(f"Run Time {str(et-st)[0:6]} sec \n")
#else: print("Run Time 0 sec \n")


#July 22, Ran:  genSums(10000, 8)
"""allSums efficiency = 98.2 % of total time
maxCount : 9, maxCount Num : 28043302 , Run Time : 37.867 sec"""


#print(min(genSums(200,2)))
#Value, (10000, 8) returns (183413517, count:9, time: 35)
#Value, (20000, 9) returns (538587427, count: 11, time 142)

#2nd approach
"""
M1 = [1,2,3,4] + [1,2,3,4] then M2 = [1,2,3,4] + [4,1,2,3] 
then M3 = [1,2,3,4] + [3,4,1,2] then M4 = [1,2,3,4] + [2,3,4,1]
M2 and M4 are repetitive, M3 is self repetitive
1 1 M1
1 2 M2
1 3 M3[1]
1 4 M2 *
2 2 M1
2 3 M2 *
2 4 M3[2]
3 3 M1
3 4 M2
4 4 M1
//
M1 = [1:6] + [1:6] M1->M6
6 + 5 + 4 + 3 + 2 + 1 = 21
6 + 6 + 6 + 6/3
Use M1, M2, M3, 1/2 M4?
need n+1 / 2 matricies
""" 
"""
def allArr(array):
    arrayMain = array
    n = len(arrayMain)
    bigArr = np.zeros( (int((len(array)+1) /2) + 1 - n%2 , n) ) #adds extra row for even 'n'
    for i in range(int((len(array)+1)/2)):
        bigArr[i] = np.zeros(n)
        for j in range(n):
            bigArr[i][j] = arrayMain[(j+i)%n]
    if(n%2 ==0):
        for k in range(int(n/2)):
            bigArr[int((n/2))][k] = arrayMain[((k+ int(n/2)) % n)]
            bigArr[int((n/2))][-(k+1)] = arrayMain[-(k+1)] * -1
    return bigArr
arr = np.array(pentas(10))
print(allArr(arr))
et = time.time()
if(et-st>0.01):
    print(f"Run Time {str(et-st)[0:6]} sec")"""