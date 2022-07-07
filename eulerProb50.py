from Prime import *
import time
import math
#print(primes_top(100))
def largConsecCount(num, Q):
    if(Q==0):
        Q = int(num/20)
    pList, countMax, sumCur, countCur, bestPrime = primes_top(num), 0, 0, 0, 0
    for i in range(int((1/Q)*len(pList))):
        countCur = 0
        sumCur = 0
        for k in range(i, len(pList)):
            sumCur += pList[k]
            countCur+=1
            if(sumCur!=pList[k] and pList.count(sumCur)==1):
                if(countCur > countMax): 
                    countMax = countCur
                    bestPrime = sumCur
    return countMax, bestPrime, Q, num
st = time.time()
tuple = largConsecCount(10000, 0)
#Q is a coeff that might make it more efficient.  range( int((1/Q)*len(pList)-1) )
#Q=30 has proven to work for 1k-->10k . Same with Q = 4*math.log(num)
#
et = time.time()
print(f"\nCeil: {tuple[3]} | Prime: {tuple[1]} | Consec: {tuple[0]} | Run Time {str(et-st)[0:6]} sec | Q = {tuple[2]}\n")

"""
Ceil: 1000 | Prime: 953 | Consec: 21 | Run Time 0.0044 sec | Q = 29
Ceil: 5000 | Prime: 4651 | Consec: 45 | Run Time 0.1611 sec | Q = 36
Ceil: 10000 | Prime: 9521 | Consec: 65 | Run Time 0.7866 sec | Q = 40
Ceil: 30000 | Prime: 28697 | Consec: 108 | Run Time 2.2095 sec | Q = 600.0
Ceil: 40000 | Prime: 38921 | Consec: 124 | Run Time 3.1374 sec | Q = 2000

"""
#Idea, pick a num value, then slowly increase Q for that num value until the expression changes.
#Use the Q values that barely fall into the correct outcome in order to create a linear regression model
# that predicts the best optimized Q for a given num