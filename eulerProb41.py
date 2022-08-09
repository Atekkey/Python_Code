from eulerProb32 import *
from Prime import *
from eulerProb32 import checkPandigital
pList = primes_top(int(10**6))
print("pListGened, max = ", pList[-1])
maxim = 0
nums = [1,2,3,4,5,6,7,8,9, 0]
for prime in pList:
    if(checkPandigital(str(prime), nums[len(str(prime)):10])):
        maxim = max(prime, maxim)
        print("New max", maxim)
print("done", maxim)

