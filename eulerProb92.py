#SOLVED
def digitList(num):
    num = str(num)
    digList = []
    for i in range(len(num)):
        digList.append(int(num[i]))
    return digList

def checkChain(num):
    runIter = 0
    while(num != 89 and num != 1):
        runIter += 1
        dList = digitList(num)
        num = 0
        for i in dList:
            num += int(i ** 2)
    return num

def main():
    count = 0
    for num in range(1, 10 * (10**6)):
        if(checkChain(num) == 89):
            count +=1
        if(num%10000 == 0):
            print(f"{num} out of 10 000 000")
    return count

print(main())