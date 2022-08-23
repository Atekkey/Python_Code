#SOLVED
def pBin(num): #pure binary removes the leading 0b
    #ARGS) int num
    #OUT) string strBin
    biny = str(bin(num))
    biny = biny[2:]
    return biny
def checkPalin(main):
    #ARGS) string main
    #OUT) boolean
    for i in range(int(len(main)/2)):
        if(main[i]!=main[len(main)-1 - i]):
            return False
    return True

sum = 0
for num in range(10**6):
    st = str(num)
    if(checkPalin(st) and checkPalin(pBin(num))):
        sum += num
print("\n", sum)
