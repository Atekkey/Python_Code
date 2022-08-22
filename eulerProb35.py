from Prime import *
#pList = primes_top(10**5)
#print(pList[-1])
import pandas as pd

def allCircles(num):
    nList = []
    numStr = str(num)
    leng = len(numStr)
    cur = 0
    for i in range(leng):
        cur = numStr[i : leng] + numStr[0:i]
        nList.append(int(cur))
    return nList

pList = list(pd.read_csv('millionPrimes.csv'))
for p in range(len(pList)):
    pList[p] = int(pList[p])
print("done reading")
pCount = 13
i = 25
c = 0
while(i<len(pList)):
    if(i<0): i = 0
    if(i%100==0): print(i, "out of", len(pList))

    isCirc = True
    prime = pList[i]
    nList = allCircles(prime)
    for n in nList:
        if(n not in pList):
            isCirc = False
            break
    if(isCirc):
        pCount +=1
        #print("isCirc")
    i+=1

print("primeCount = ", pCount)
