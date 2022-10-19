#SOLVED
from eulerProb36 import *
rev = lambda inte : int(str(inte)[::-1])
lyc = lambda inte : inte + rev(inte)
chk = lambda sum : checkPalin(str(sum))
lychelCount = 0
for i in range(10000):
    lyBool = False
    iter = 0
    num = i
    while(lyBool == False):
        iter += 1
        num = lyc(num)
        if(chk(num)):
            lyBool = True
        if(iter>=49 and lyBool == False):
            lychelCount += 1
            break
print(lychelCount)


