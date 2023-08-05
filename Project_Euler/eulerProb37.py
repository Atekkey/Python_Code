#SOLVED
from Prime import *
import pandas as pd
import pickle
def bothTrunc(num):
    st = str(num)
    tList = []
    for i in range(len(st)):
        if(i!=0): tList.append(int(st[0:i]))
        tList.append(int(st[i:len(st)]))
    return tList
"""
pList = list(pd.read_csv('millionPrimes.csv'))
with open("test", "wb") as fp:   #Pickling
    pickle.dump(pList, fp)

print("done loading")
"""
with open("test", "rb") as fp:   # Unpickling
    pList = pickle.load(fp)
pList2 = [eval(i) for i in pList]
print("done loading")
fList = []
for i in range(4, int(len(pList2))):
    if(i%500 ==0): print(i, "out of", int(len(pList2)))
    boolpass = True
    num = pList2[i]
    tList = bothTrunc(num)
    for t in tList:
        if(t not in pList2):
            boolpass = False
            break
    if(boolpass):
        fList.append(num)
        print(fList)

print(fList, "len =", len(fList), "sum =", sum(fList))

#[23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397] len = 11 sum = 748317