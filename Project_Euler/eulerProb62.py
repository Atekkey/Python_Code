#UNSOLVED
import math
from itertools import permutations
isCube = lambda x : round(math.pow(x, 1/3), 10) % 1 == 0
def intPermus(num):
    perm = list(permutations(str(num)))
    iList = []
    for p in perm:
        iList.append(int("".join(p)))
    return iList
def main1():
    for i in range(1740, 2000):
        pCount = 0
        if(i%10 ==0):print("i is", i)
        numMain = i ** 3
        iList = list(set(intPermus(numMain)))
        for t in iList:
            if(isCube(t)): pCount += 1
            if(pCount>5): break
        if(pCount == 5):
            print("found at numMain = ", numMain)
            return
#main()
# Checked from 0 --> 1740
def main2():
    cList = []
    for i in range(2000):
        cList.append(i**3)
    for i in range(0, 400):
        pCount = 0
        if(i%10 ==0):print("i is", i)
        numMain = i ** 3
        iList = list(set(intPermus(numMain)))
        for t in iList:
            if(t in cList): pCount += 1
            if(pCount>5): break
        if(pCount == 5):
            print("found at numMain = ", numMain)
            return
main1()