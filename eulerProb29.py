from itertools import combinations, combinations_with_replacement, permutations
numList = []
for x in range(2, 101):
    numList.append(x)
perms = list(permutations(numList, 2))
fList = []
print(perms[0:300])
for t in perms:
    fList.append(t[0] ** t[1])
    #if(t[0]==t[1]):
for q in numList:
    fList.append(q**q)

fList = list(set(fList))
fList.sort()
permDist = len(fList)
print(fList[0:10])
print(permDist)
