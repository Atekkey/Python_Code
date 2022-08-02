"""find first 4 consecutive numbers to have 4 distinct prime factors? """
from Prime import *
import time
st = time.time()
check = lambda num : len(set(prime_factors(num)))
def consec(bot, top):
    rowCount = 0
    for i in range(bot, top):
        if(i % 1000 ==0): print(i)
        if(prime_check(i) or prime_check(int(i/2))):
            rowCount = 0
            continue
        if(check(i)==4): rowCount+=1
        else: rowCount = 0
        if(rowCount==4):
            return i - 3
    return -1
def consecV2(bot, top):
    ans = -1
    for i in range(bot, top, 4):
        if((i-2)%1000==0): print(i-2)
        if(check(i)==4):
            ans = consec(i-3, i+3)
        if(ans != -1):
            return ans
    return -1
#print(f"Ans = {consec(200000, 250000)}")
#print(consecV2(250000, 300000))
"""print(consec(253000, 254000))
et = time.time()
print(f"{et - st} sec")"""
#253894
print(prime_factors(253894),prime_factors(253895),prime_factors(253896),prime_factors(253897))
