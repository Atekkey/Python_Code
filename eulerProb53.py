#SOLVED
import math
greatSum = 0
for n in range(23, 101):
    if(n%5==0): print(n, "out of", 100)
    for r in range(1, n):
        num = math.factorial(n) / (math.factorial(r) * math.factorial(n - r))
        if(num> 10**6): greatSum +=1
print(greatSum)
