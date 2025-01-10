## SOLVED

## Prime family

from Prime import prime_check
import time
st = time.time()

def gen(topNum):
    for kx in range(6, topNum, 6):
        if(prime_check(kx-1)):
            getFamily(kx-1)
        if(prime_check(kx+1)):
            getFamily(kx+1)
    

def getFamily(num):
    temp = str(num)
    digToCount = {"0" : 0, "1" : 0, "2" : 0, "3" : 0, "4" : 0, "5" : 0, "6" : 0, "7" : 0, "8" : 0, "9" : 0}
    cont = False
    ind = 0
    dig = "0"
    for i in range(len(temp)):
        digToCount[temp[i]] += 1
        if(digToCount[temp[i]] == 3):
            cont = True
            ind = i
            dig = temp[i]
            break
    if(cont == False):
        return
    for i in range(ind, -1, -1):
        if(temp[i] == dig):
            temp = temp[0:i] + "x" + temp[i+1:]
    fromX(temp)

def fromX(input):
    count = 0
    recall = 0
    for i in range(10):
        if(input[0] == "x" and i == 0):
            continue
        temp = input
        for j in range(len(temp)):
            if(temp[j] == "x"):
                temp = temp[0:j] + str(i) + temp[j+1:]
        num = int(temp)
        if(prime_check(num)):
            count += 1
        if(count == 1):
            recall = num
        if(i - count >= 3):
            return
    if(count >= 8):
        print("FOUND AT: ", recall, " from ", input)


### MAIN
    
gen(1000000)

et = time.time()
print(round(et-st , 6), " sec")