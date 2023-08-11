#SOLVED
#Did brute force, could try another way?
eqRem = lambda a, n : (((a-1) ** n) + ((a+1) ** n)) % (a ** 2)
rTot = 0
for a in range(3, 1001):
    rTemp = 0
    for n in range(2000):
        rem = eqRem(a,n)
        if(rem == ((a**2) - 1)):
            rTemp = rem
            break
        rTemp = max(rTemp, rem)
    rTot += rTemp
print(rTot, "done2k")