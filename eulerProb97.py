#SOLVED
#Plan: Convert the number into a base 10 exponent
# 28433×2^7830457+1
#Goal: Find the last ten digits of this prime number.
#from decimal import *
#import math
#D = lambda x : Decimal(x)
#getcontext().prec = 10**5
"""
exp1 = math.log(Decimal(28433), Decimal(10))
exp2 = Decimal(Decimal(math.log(Decimal(2), Decimal(10))) * Decimal(7830457))
exp = Decimal(Decimal(exp1) + Decimal(exp2))
# 10 ^ exp + 1
ans = Decimal(math.pow(Decimal(10), Decimal(exp%Decimal(1000))))
print(Decimal(ans % Decimal(10**10)  + 1))"
x = D(math.log(28433, 10))
y = D(math.log(2, 10) * 7830457)
z = x+y
a = D(z - int(z))
b = D(10 ** a)
bS = str(b)
print(bS[-10:])
"""
dig10 = lambda num : num % 10**10
def step1():
    num = 1
    for i in range(1, 7830457 + 1):
        if(i %1000 == 0): print(int(i/1000), " out of 7830k" )
        num = dig10(num * 2)
    return num
num1 = step1()
num2 = dig10(num1 * 28433) + 1
print(num2)
