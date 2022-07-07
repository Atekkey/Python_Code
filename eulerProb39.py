#SOLVED
"""If p is the perimeter of a right angle triangle with integral length sides, {a,b,c},
 there are exactly three solutions for p = 120.
{20,48,52}, {24,45,51}, {30,40,50}
For which value of p ≤ 1000, is the number of solutions maximised?"""
#Approach No.1: create a list of tuples of every pythagorean triple
import math
tuple = []
tuple2 = []
for a in range(1, 1000):
    for b in range(a, 1000):
        pythag = a**2 + b**2
        c = math.sqrt(pythag)
        if(c%1 == 0 and a+b+c <=1000):
            tuple.append([a, b, int(c), a+b+int(c)])
            tuple2.append(a+b+int(c))
#print(tuple)
print(tuple2)

for i in tuple2:
    if(tuple2.count(i)>7):
        print(i)
#Printed 840, correct

    