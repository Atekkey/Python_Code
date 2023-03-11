fileName = ('Py1\p054_poker.txt')
file = open(fileName,'r')
lines = file.readlines()
hand1List = []
hand2List = []
valueComp = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
for i in range(1000):
    lines[i] = lines[i].strip('\n')
    lines[i] = lines[i].split(' ')
    hand1List.append(lines[i][0:5])
    hand2List.append(lines[i][5:10])
print(hand1List[0])

def getNums(hand):
    numList = []
    for i in range(5):
        numList.append(valueComp.index(hand[i][0]) + 2)
    return numList
def getSuits(hand):
    suitList = []
    for i in range(5):
        suitList.append(hand[i][1])
    return suitList

print(getSuits(hand1List[0]), getNums(hand1List[0]))

def highCardWin(hand1, hand2):
    h1 = getNums(hand1)
    h2 = getNums(hand2)
    while(len(h1)>0):
        if(max(h1)>max(h2)):
            return 1
        if(max(h1)<max(h2)):
            return 2
        else:
            h1.remove(max(h1))
            h2.remove(max(h2))
    return -1
print(highCardWin(hand1List[0], hand2List[0]))