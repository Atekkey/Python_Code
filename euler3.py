numStr = ""
prod = 1
for x in range(1, 1000001):
    numStr += str(x)
for y in range(1,8):
    y = (10**(y-1))-1
    print(numStr[y])
    prod *= int(numStr[y])
print(prod)


topCount = 0
topInt = 0
for x in range(800000,1000000):
    count = 0
    y = x
    while(x!=1):
        if(x%2==0):
           x/=2
           count+=1
        else:
           x*=3
           x+=1
           count+=1
    if(count>topCount):
        topCount = count
        topInt = y
print(topInt)


alist = []
for x in range(2,1001):
    alist.append(x)
blist = [2, 4, 5, 8, 25, 124, 625, 16, 32, 64, 128, 256, 512, 1000]
for y in blist:
    alist.remove(y)
print(alist)
