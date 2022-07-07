from Prime import *
import time
import math
#print(primes_top(100))
def largConsecCount(num, Q):
    bestI, Qreal = 0, 0
    if(Q==0):
        Q = int(num/50)
    pList, countMax, sumCur, countCur, bestPrime = primes_top(num), 0, 0, 0, 0
    for i in range(int((1/Q)*len(pList))):
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
tuple = largConsecCount(300000, 8000)
#Q is a coeff that might make it more efficient.  range( int((1/Q)*len(pList)-1) )
#Q=30 has proven to work for 1k-->10k . Same with Q = 4*math.log(num)
#
et = time.time()
print(f"\nCeil: {tuple[3]} | Prime: {tuple[1]} | Consec: {tuple[0]} | startPrime: {tuple[4]} | Run Time {str(et-st)[0:6]} sec | Q = {tuple[2]}\n")

"""
Ceil: 1000 | Prime: 953 | Consec: 21 | startPrime: 7 | Run Time 0.0043 sec | Q = 34
Ceil: 5000 | Prime: 4651 | Consec: 45 | startPrime: 7 | Run Time 0.0764 sec | Q = 160
Ceil: 10000 | Prime: 9521 | Consec: 65 | startPrime: 3 | Run Time 0.2280 sec | Q = 610
Ceil: 15000 | Prime: 13099 | Consec: 75 | startPrime: 3 | Run Time 0.4899 sec | Q = 850
Ceil: 20000 | Prime: 16823 | Consec: 81 | startPrime: 11 | Run Time 1.0585 sec | Q = 400
Ceil: 30000 | Prime: 28697 | Consec: 108 | startPrime: 2 | Run Time 1.8204 sec | Q = 1600
Ceil: 40000 | Prime: 38921 | Consec: 124 | startPrime: 2 | Run Time 2.9122 sec | Q = 3200
Ceil: 100000 | Prime: 92951 | Consec: 183 | startPrime: 3 | Run Time 17.747 sec | Q = 4500
Ceil: 200000 | Prime: 182107 | Consec: 249 | startPrime: 3 | Run Time 69.920 sec | Q = 5000
"""
#Idea, pick a num value, then slowly increase Q for that num value until the expression changes.
#Use the Q values that barely fall into the correct outcome in order to create a linear regression model
# that predicts the best optimized Q for a given num
