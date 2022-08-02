#SOLVED
from Prime import *
import time
import math
#print(primes_top(100))
def largConsecCount(num, Q):
    bestI, Qreal = 0, 0
    if(Q==0):
        Q = int(num/50)
    pList, countMax, sumCur, countCur, bestPrime = primes_top(num), 0, 0, 0, 0
    for i in range(Q):
        countCur = 0
        sumCur = 0
        for k in range(i, len(pList)):
            if(sumCur > num):
                break
            sumCur += pList[k]
            countCur+=1
            if(sumCur!=pList[k] and pList.count(sumCur)==1):
                if(countCur > countMax): 
                    countMax = countCur
                    bestPrime = sumCur
                    bestI = i
    return countMax, bestPrime, Q, num, pList[bestI]
st = time.time()
tuple = largConsecCount(100000, 5)
#Q is a coeff that might make it more efficient.  range( int((1/Q)*len(pList)-1) )
#Q=30 has proven to work for 1k-->10k . Same with Q = 4*math.log(num)
#
et = time.time()
print(f"\nCeil: {tuple[3]} | Prime: {tuple[1]} | Consec: {tuple[0]} | startPrime: {tuple[4]} | Run Time {str(et-st)[0:6]} sec | Q = {tuple[2]}\n")

"""
Ceil: 1000 | Prime: 953 | Consec: 21 | startPrime: 7 | Run Time 0.0043 sec 
Ceil: 5000 | Prime: 4651 | Consec: 45 | startPrime: 7 | Run Time 0.0764 sec 
Ceil: 10000 | Prime: 9521 | Consec: 65 | startPrime: 3 | Run Time 0.2280 sec 
Ceil: 15000 | Prime: 13099 | Consec: 75 | startPrime: 3 | Run Time 0.4899 sec 
Ceil: 20000 | Prime: 16823 | Consec: 81 | startPrime: 11 | Run Time 1.0585 sec 
Ceil: 30000 | Prime: 28697 | Consec: 108 | startPrime: 2 | Run Time 1.8204 sec
Ceil: 40000 | Prime: 38921 | Consec: 124 | startPrime: 2 | Run Time 2.9122 sec 
Ceil: 100000 | Prime: 92951 | Consec: 183 | startPrime: 3 | Run Time 14.804 sec | Q = 5
Ceil: 200000 | Prime: 182107 | Consec: 249 | startPrime: 3 | Run Time 69.920 sec 
Ceil: 300000 | Prime: 287137 | Consec: 308 | startPrime: 2 | Run Time 125.48 sec 
"""
