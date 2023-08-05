def StoC(s):
    cList = []
    for x in s:
        cList.append(x)
    return cList
def wordComp(w1, w2):
    if(len(w1) != len(w2)):
        return False
    c1 = StoC(w1)
    c2 = StoC(w2)
    for i in range(len(w1)):
        if(c1.count(w1[i]) != c2.count(w1[i])):
            return False
    return True
def createKey():
    return

def aListGen():
    isSq = lambda num: round((num ** 1/2), 10) % 1 == 0
    fileName = ('p098_words.txt')
    file = open(fileName,'r')
    line = file.read()
    file.close()
    line = line.strip("\"")
    wList = line.split("\",\"")
    aList = []
    for w1 in range(len(wList)):
        for w2 in range(w1, len(wList)):
            if(wordComp(wList[w1], wList[w2]) and w1 != w2):
                aList.append([wList[w1], wList[w2]])
def main():   
    aList = aListGen()
    
main()
