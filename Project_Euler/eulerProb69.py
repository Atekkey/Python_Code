# SOLVED in Pt2
from Prime import *;
import time;
st = time.time()

def totient(num):
    return len(relPrimeList(num))
"""
maxTot = 0
maxN = 0
for n in range(5, 1000):
    tot = n/(totient(n))
    if(tot > maxTot): 
        maxTot = tot
        maxN = n
"""

et = time.time()
#print(f"\nMax n/Tot = {maxTot} at n={maxN} | Runtime: {et-st} sec\n")