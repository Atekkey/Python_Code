#SOLVED
"""
Tn=n(n+1)/2
Pn=n(3n−1)/2	 
Hn=n(2n−1)
T285 = P165 = H143 = 40755.
FIND NEXT INSTANCE
"""

#Trying Brute Force
triList = []
PentaList = []
HexaList = []
for n in range(900, 180000):
    triList.append(n*(n+1)/2)
    PentaList.append(n*(3*n-1)/2)
    HexaList.append(n*(2*n-1))
print("done1")
for m in range(50000, 60000):
    if((PentaList.count(triList[m]) + HexaList.count(triList[m]))>1):
        print(triList[m])
        break
print("done2")
#Answer: 1533776805, correct