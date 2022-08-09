#Solved
#Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
def checkPandigital(string, excludeList):
    nums = [0, 1,2,3,4,5,6,7,8,9]
    for i in excludeList:
        nums.remove(i)
    if(len(string)!=len(nums)):
        return False
    for x in nums:
        if(string.count(str(x)) != 1):
            return False
    return True
"""
pandigList = []
for a in range(10000):
    if(a%100):
        print(a/100, "out of 100%")
    for b in range(10000):
        if(a>100 and b>100):
            continue
        c = a * b
        string = str(a) + str(b) + str(c)
        if(checkPandigital(string, [0])):
            pandigList.append(c)
pandigList = list(set(pandigList))
print(sum(pandigList))"""