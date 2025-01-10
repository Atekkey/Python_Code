import numpy as np
import time
st = time.time()
def main1(arr, k):
    arr.sort() # O( nlog(n) )
    arr = arr[::-1]
    arr = arr[:k]
    test = [i for i in range(1, arr[0]+1)] 
    best = arr[-1]
    for testNum in test: # O(L)
        count = 0
        for a in arr: # O(n)
            count += a//testNum
            if(count >= k):
                break
        if count >= k:
            best = testNum
        else:
            break
    return best

def main2(arr, k):
    test = 1
    good = True
    best = 1
    while good: 
        count = 0
        for a in arr:
            count += a//test
        if count >= k:
            best = test
            test+=1
        else:
            good = False
    return best

def main3(arr, k):
    arr.sort() # O( nlog(n) )
    arr = arr[::-1]
    topNum = arr[0]
    left, right = 1, topNum # just assume 1 indexing
    while left+1 != (right) and left!=right: # O( log(L_max) )
        mid = (left + right) // 2
        count = 0
        for a in arr: # O(n)
            count += a//mid
            if(count >= k):
                break
        if count >= k:
            left = mid
        else:
            right = mid
    return left

print(main3(np.random.randint(0, 10**7, 10**7), 100))

et = time.time()
print("time: ", et-st)