#SOLVED
from Prime import *

primeList = primes_top(10000)
neg = 0
for i in range(300):
    i -= neg
    if(primeList[i]<1000):
        primeList.pop(i)
        neg+=1
# ^ gets all 4 digit primes

inc = 0
num3 = 0
temp= 0
strTemp = ""
listDig = []
listCombos = []
for i in range(len(primeList)-1):
    for k in range(i+1, len(primeList)):
        inc = primeList[k] - primeList[i]
        num3 = primeList[k] + inc
        if(primeList.count(num3)>0):
            listStr =  [str(primeList[i]), str(primeList[k]), str(num3)]
            listInt =  [(primeList[i]), (primeList[k]), (num3)]
            string = str(primeList[i]) + str(primeList[k]) + str(num3)
            temp = 0
            for x in listStr:
                for y in range(12):
                    if(x.count(string[y]) > 0):
                        temp += 1
            if(temp == 36):
                print(listStr)
                
            """temp = 0
            for i in range(4):
                if(string.count(string[i])>-1):
                    temp+=1
                if(temp==4):
                    print(string)"""


print("done")
