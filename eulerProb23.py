import math

def propDiv(num):#Proper Divisors
    pdList = []
    for x in range(1, int(0.5*num)+1):
        if(num%x==0):
            pdList.append(x)
    return pdList

def propDivSum(num):
    list = propDiv(num)
    sum = 0
    for x in list:
        sum+=x
    return sum

def qualify(num):
    if(propDivSum(num)>num):
        return True
    else:
        return False

def findAll(): #find all abundant numbers
    listAbund = []
    for i in range(10, 28124):
        if(qualify(i)):
            listAbund.append(i)
    return listAbund

def maxSum(): #subtract from here
    sum = 0
    for i in range(0, 28124):
        sum+=i
    return sum

def listSumAbund(listAbund):
    listSums = []
    for i in listAbund:
        for k in listAbund:
            if(i+k <= 28123):
                listSums.append(i+k)
    listSums = list(set(listSums)) #removes Duplicates
    return listSums

ans = maxSum() - sum(listSumAbund(findAll()))
print(ans)

#print(listSumAbund(findAll())[0:10])

