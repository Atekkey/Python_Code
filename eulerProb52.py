#SOLVED
"""Find the smallest positive integer such that 2x,3x,4x,5x,6x, contain the same digits"""
def checkCount(list):
    for x in range(len(list)):
        list[x] = str(list[x])
        if(len(list[x]) != len(list[0])):
            return False
        for i in list[0]:
            if(list[x].count(i) != list[0].count(i)):
                return False
    return True
for mult in range(10): #changable variable
    bott = 10**mult
    for n in range(bott, int(bott*10/6)):
        mainList = [n, 2*n, 3*n, 4*n, 5*n, 6*n]
        if(checkCount(mainList)): print(f"found at num = {n}, list = {mainList}")

