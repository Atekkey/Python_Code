# SOLVED
from Prime import *
import time
st = time.time()

def totient(num):
    prod = num
    pList = set(prime_factors(num))
    for p in pList:
        prod *= (1 - (1/p))
    return int(prod)
"""
for num in range (10**4 * 2):
    if (num % 1000 == 0):
        print(str(num/1000) + "k")
    totient(num)"""
#UPTO 280k, DownTo 980k : maxTot = 5.3155, maxN = 881790
"""
maxTot = 5.213541
maxN = 30030
for n in range(int(2.8 * (10**5)), int(3.0 * (10**5))):
    if(n%1000 == 0):
        print(str(n/1000) + "k")
    tot = n/(totient(n))
    if(tot > maxTot): 
        maxTot = tot
        maxN = n

et = time.time()
print(f"\nMax n/Tot = {maxTot} at n={maxN} | Runtime: {round(et-st, 6)} sec\n")
"""
num = 2 * 3 * 5 * 7 * 11 * 13 * 17
tot = num / totient(num)
print(num, tot)    
