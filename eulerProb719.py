#unsolved
import time
from itertools import permutations
st = time.time()

def T(num):
    perm = list(set(permutations([0,0,0,0,0,1,1,1,1,1], 5))) #for splitting
    tot = 0 #exclude 1**2
    num = int( num ** (1/2))
    for x in range(1, num + 1):
        n = x ** 2
        s = str(n)
        for i in range(2**(len(str(n))-1)):
            pi = perm[i]
            place = 0
            s = str(n)
            addends = []
            for bin in pi:
                if(s == ""):
                    break
                if(len(s) == 1):
                    addends.append(int(s[0]))
                    break
                if(place > len(s)):
                    place = len(s)
                    addends.append(int(s[0:place+1]))
                    break
                if(bin == 1):
                    addends.append(int(s[0:place+1]))
                    s = s[place+1:]
                    place = 0
                if(bin == 0):
                    place+=1
            if(len(addends)>1 and sum(addends) == x):
                print(n)
                tot += n
                break
    return tot


print("sum = ", T(10**4))
et = time.time()
print("time = ", round(et-st, 4), "sec")