#UNSOLVED
#How many different ways can one hundred be written as a sum of at least two positive integers? 
"""
S(1) = 0 [1]??
S(2) = 1 + 1 [1]
S(3) = 1 + 2, 1 + 1 + 1 [2]
S(4) = 1 + 3, 1 + 2 + 1, 2 + 2, 1 + 1 + 1 + 1 [4]
S(5) = [6]
Attempt 1. Step1: Break each number into composits of 2 nums
Ex: S(6) --> (1,5), (2,4) (3,3) (4,2) (5,1)
Step2 : Break each first number into the tuple into components. Let the second number remain.
Ex: (2, 4) --> ((1, 1), 4), (3, 3) --> ((2,1),3) [Needs to be broken down again]
This should mean S(6) = S(1) + S(2) +... S(5)
Does S(n) = SUM( i = 0:n-1) [S(i)] ??
NO, it will be less because repeats are found

Maybe consider a graphical approach/ Pascals triangle? no

Maybe consider a matrix approach:
    1a + 2b + 3c ... 100z
    where SUM(a:z) > 2
    where sum(1a + 2b + ... 100z) = 100
    run a for loop starting at z then y, x
    O(n!) --> Could lead to time = 100! (much too large) 
"""
import time
st = time.time()
num = 11
pList = []
for i in range(0,num):
    pList.append(i)
from itertools import combinations_with_replacement
cList = list(combinations_with_replacement(pList, num))
ind = 0
for c in range(len(cList)):
    c += ind
    if(sum(cList[c]) != 5):
        cList.remove(cList[c])
        ind -= 1
print(len(cList), "\n", cList)
et = time.time()
print("time =", round(et - st, 5), "sec")