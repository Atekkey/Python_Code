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
    return pList
    
primeList = primes_top(100000)
count = 0
for prime in primeList:
    prime = str(prime)
    aCycleList = []
    for x in prime:
        prime = prime[len(prime)-1]+prime[0:len(prime)-1]
        aCycleList.append(prime)
    bCycleList = []
    for x in aCycleList:
        bCycleList.append(int(x))
    for x in bCycleList: #Fix this
        if(prime_check(x)==False):
            break
#If any prime has a 2, it is not circular
print(count)


