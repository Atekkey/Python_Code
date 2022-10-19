from eulerProb32 import *
from Prime import *
from eulerProb32 import checkPandigital
import pickle
import pandas as pd
from itertools import permutations

"""pList = list(pd.read_csv('millionPrimes.csv'))
with open("test", "wb") as fp:   #Pickling
    pickle.dump(pList, fp)

with open("test", "rb") as fp:   # Unpickling
    pList = pickle.load(fp)
print("pListGened, max = ", pList[-1])

maxim = 0
nums = [1,2,3,4,5,6,7,8,9, 0]
for prime in pList:
    if(checkPandigital(prime, nums[len(prime):10])):
        prime = int(prime)
        maxim = max(prime, maxim)
        print("New max", maxim)
print("done", maxim)
"""

pList = list(permutations([1,2,3,4,5,6,7], 7))
#The prime can't be 8 digit or 9 digit b/c then the digits would add to make it divis by 3, meaning its divis by 3 and not prime
sList = []
for p in pList:
    s = ''
    if(p[-1]%2 ==0): continue
    for d in p:
        s += str(d)
    if(sum(p)%3 == 0):
        continue
    sList.append(int(s))
#print(len(sList))


for s in range(len(sList)-1 , -1, -1):
    if(prime_check(sList[s])):
        print(sList[s])
        break