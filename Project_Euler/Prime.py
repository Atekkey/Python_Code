import math
import csv
import time
#st = time.time()
def factors(num):
    fList = []
    for x in range(int(0.5*num)+3, 1, -1): 
        if(num%x==0):
            fList.append(x)
    #print(fList)
    return fList
    

def prime_factors(num):
    pfList = []
    for x in range(2, num):
        while(num%x==0):
            pfList.append(x)
            num = num/x
    return pfList


def primes_pos(pos):
    pList = [2,3]
    posCount = 2
    prime = 3
    while(posCount<=pos):
        prime += 2
        primeCheck = True
        for x in range(3, int(0.5*prime)+1):
            if(prime%x==0):
                primeCheck = False
                break
        if(primeCheck==True):
            posCount +=1
            pList.append(prime)
            #print(pList)
    return pList
    
def prime_check(num):
    for x in range(2, int(num**0.5)+1):
        if(num%x==0):
            return False
    return True

def primes_top(topNum):
    pList = [2]
    topNum = int(topNum)
    for x in range(3,topNum,2):
        if(prime_check(x)==True):
            pList.append(x)
    #print(pList)
    return pList

def GCF(A, B):
    for i in range(min(A,B), 0, -1):
        if(A%i==0 and B%i==0):
            return i
    return 1

def relPrimeList(num):
    relPrime = set()
    for i in range(num-1, 0, -1):
        if(GCF(num, i)==1):
            relPrime.add(i)
    return relPrime

#Done, dont use again
"""def writeTo():
    f = open('millionPrimes.csv', 'w')
    writer = csv.writer(f)
    writer.writerow(primes_top(10**6))
    f.close()
    print("done with mil")
"""


# print(primes_top(5 * (10**5))[-1])
# #print(prime_factors(9883542))
# et = time.time()
# print(round(et-st , 6), " sec")