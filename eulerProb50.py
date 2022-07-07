from Prime import *
import time
#print(primes_top(100))
def largConsecCount(num):
    pList, countMax, sumCur, countCur, bestPrime = primes_top(num), 0, 0, 0, 0
    for i in range(len(pList)-1):
        countCur = 0
        sumCur = 0
        for k in range(i, len(pList)):
            sumCur += pList[k]
            countCur+=1
            if(sumCur!=pList[k] and pList.count(sumCur)==1):
                if(countCur > countMax): 
                    countMax = countCur
                    bestPrime = sumCur
    return countMax, bestPrime
st = time.time()
print(largConsecCount(8000))
et = time.time()
print(f"Run Time {str(et-st)[0:6]} sec")
"""
Num // AVG Time
1k     0.0371
5k     2.1
10k   12.8
15k   36.7
20k   80.9
25k  145.5
30k  238.4
"""