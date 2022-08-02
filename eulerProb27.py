#SOLVED
from Prime import *

def checkQuadPrime(a,b,n):
    sum = n**2 + a*n + b
    if(sum%1!=0 or sum<0):
        return False
    return prime_check(sum)

maxi = [0, 0, 0]
for a in range(-1000, 1001):
    if(a%2==0):
        print(a)
    for b in range(-1000, 1001):
        cond, n = True, 0
        while(cond):
            check = checkQuadPrime(a,b,n)
            if(check):
                n+=1
            else:
                cond = False
                if(abs(n) > maxi[0]):
                    print(f"max : {maxi[0]} a : {a} b : {b}")
                    maxi = [abs(n), a, b]

print(f"FINAL  max : {maxi[0]} a : {maxi[1]} b : {maxi[2]} prod : {maxi[1]*maxi[2]}")
#FINAL  max : 71 a : -61 b : 971 prod : -59231