import math
import csv

def factors(num):
    fList = []
    for x in range(2, int(0.5*num)+3):
        if(num%x==0):
            fList.append(x)
    return fList
    print(fList)

def prime_factors(num):
    pfList = []
    for x in range(2, int(0.5*num)+1):
        while(num%x==0):
            pfList.append(x)
            num = num/x
    return pfList


def primes_pos(pos):
    pList = [2,3]
    posCount = 2
    prime = 2
    while(posCount!=pos):
        prime += 2
        primeCheck = True
        for x in range(3, int(0.5*prime)+1):
            if(prime%x==0):
                primeCheck = False
                break
        if(primeCheck==True):
            posCount +=1
            pList.append(prime)
    return pList

def prime_check(num):
    checkBool = True
    for x in range(2, int(0.5*num)+1):
        if(num%x==0):
            checkBool = False
            break
    return checkBool

def primes_top(topNum):
    pList = [2]
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
#print(primes_top(1000000))
#print(prime_factors(9883542))
