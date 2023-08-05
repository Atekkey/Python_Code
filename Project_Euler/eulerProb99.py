#SOLVED
import math
fileName = ('p099_base_exp.txt')
file = open(fileName,'r')
lines = file.readlines()
file.close()
mList = []
for line in lines:
    line = line.strip('\n')
    tuple = list(line.split(","))
    tuple[0], tuple[1] = int(tuple[0]), int(tuple[1])
    mList.append(tuple)
conv = lambda base, exp : math.log(base, 2) * exp

max = (-1, 0)
for i in range(len(mList)):
    realExp = conv(mList[i][0], mList[i][1])
    if(realExp > max[1]):
        max = (i + 1, realExp)
print(max)