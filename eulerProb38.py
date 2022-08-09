#SOLVED
from eulerProb32 import *
string = ""
panDig = []
nums = [1,2,3,4,5,6,7,8,9,10,11]
for integ in range(100000):
    numCur = 0
    string = ""
    while(len(string)<10):
        if(len(string)==9):
            if(checkPandigital(string, [0])):
                panDig.append(int(string))
        string += str(integ*nums[numCur])
        numCur += 1
print(panDig)
print(max(panDig))