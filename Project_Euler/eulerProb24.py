#SOLVED
import math
import numpy as np
from itertools import permutations
perm = permutations([0,1,2,3,4,5,6,7,8,9])
print(list(perm)[999999])

"""
def checkPermu(num):
    num = str(num)
    if((len(num)<10)):
        for i in range(1,10):
            if(num.count(str(i))!=1):
                return False
        return True
    for i in range(10):
        if(num.count(str(i))!=1):
            return False
    return True

pList = []
for z in range(123456789,9876543210):
    if(z%100000 == 0):
        print(z)
    if(checkPermu(z)):
        pList.append(z)
        print(f"{len(pList)} out of 1000000")
    if(len(pList)>1000000):
        print(pList.sort()[1000000-1])
        break
"""


"""
#guess = np.zeros(10)
def permu(guess):
    permu = 0
    for i in range(10):
        permu += guess[i] * math.factorial(i)
    return int(permu)

def cost(guess):
    cost = 0
    for j in range(len(guess)):
        cost += math.factorial(j) * guess[j] * ((j+1)**2)
    return int(cost)

x = 0
guess = [0,0,2,2,1,5,2,6,6,2]
x += guess[9] * math.factorial(9)
x += guess[8] * math.factorial(8)
x += guess[7] * math.factorial(7)
x += guess[6] * math.factorial(6)
x += guess[5] * math.factorial(5)
x += guess[4] * math.factorial(4)
x += guess[3] * math.factorial(3)
x += guess[2] * math.factorial(2)
x += guess[1] * math.factorial(1)
x += guess[0] * math.factorial(0)

#print(cost(guess), x)
# 0 1 2 3 4 5 6 7 8 9
#
# 2 7 8 3 9 1 5 6 0 4




#guess = [0, 0, 2, 2, 1, 5, 2, 6, 6, 2]
#print(permu(guess), cost(guess))
def iter():
    pList = []
    guess = np.zeros(10)
    costMin = [10**30, 0]
    for i in range(62,123456762, 100):
        for j in range(len(str(i))):
            guess[j] = int(str(i)[j])
        if(len(str(i))<10):
            for k in range(10-len(str(i))):
                guess[k] = 0
                for j in range(10-len(str(i)), 10):
                     guess[j] = int(str(i)[j - (10-len(str(i)))])
        for p in range(10):
            if(guess[p] > p):
                guess = np.zeros(10)
        if((i-62)%100000==0):
            print(i, cost(guess), permu(guess))
        if(permu(guess)==1000000):
            pList.append(guess)
            print("new permu")
            costG = cost(guess)
            if(costMin[0] > costG):
                costMin[0] = costG
                costMin[1] = i
                print(f"\nNew low :{costMin[0]} \n")
        if(i==99900062 or i==100000062):
            print("here", i, guess)
    return costMin, pList

print(iter())

#DECODING 
# 0 1 2 3 4 5 6 7 8 9
# 1 1 1 2 1 5 2 6 6 2 

# 2 7 8 3 9 4 1 5 6 0

# 0 1 2 3 4 5 6 7 8 9
# 1112159562
# 0 3 4 5 
# 2 7 5 9 8 1 3 4 5 0

# 0 1 2 3 4 5 6 7 8 9
# 2 2 0 2 1 5 2 6 6 2
# 4 6
# 2 7 8 3 9 1 5 0 6 4

# 0 1 2 3 4 5 6 7 8 9
# 0 0 2 2 1 5 2 6 6 2

# 2 7 8 3 9 1 5 6 0 4
"""