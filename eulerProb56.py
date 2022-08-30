#SOLVED
def digitList(num):
    num = str(num)
    digList = []
    for i in range(len(num)):
        digList.append(int(num[i]))
    return digList

def digitSum(num):
    dList = digitList(num)
    dSum = sum(dList)
    return dSum

def main():
    dMax = 0
    for a in range(1, 100):
        print("a is", a)
        for b in range(1, 100):
            dSum = digitSum(a**b)
            dMax = max(dSum, dMax)
    return dMax

