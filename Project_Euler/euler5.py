"""
ones = 3+3+5+4+4+3+5+5+4 = 36
tens = 70 + 47 = 117
hundreds = 126

[1,9] = 36
[10,19] = 70
8*36 + 47*10
[1,99] = 864
126*100 + 47*100 + 36*90

print((126*100 + 47*100 + 70*10 + 36*90)+11)"""

#17 Amicable#s
#Find all factors of a given integer
def find_factors(num):
    factorSum = 0
    for y in range(1, int((num/2)+2)):
        if(num%y==0):
            factorSum += y
    return factorSum
total = 0
numList = []
for num in range(10, 10000):
    a = find_factors(num)
    if(num==find_factors(a) and a!=num and (not a in numList)):
        total += (a + num)
        numList.append(num)
        print(a, num)
print(total)
