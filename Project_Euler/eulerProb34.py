#SOLVED
#Find the sum of all numbers which are equal to the sum of the factorial of their digits
import math
def digitList(num):
    num = str(num)
    digList = []
    for i in range(len(num)):
        digList.append(int(num[i]))
    return digList

#trying to find the max
x = math.factorial(9)*8
print(x)

finalSum = 0
last = 0
top = 2903040
for num in range(3, top):
    if(num%1000 == 0):
        print(f"{(num/(top/100))} out of {100}%")
    digList = digitList(num)
    digSum = 0
    for d in digList:
        digSum += math.factorial(d)
    if(digSum == num):
        finalSum += num
        last = num
print(f"Final Sum = {finalSum}, Last = {last}")

