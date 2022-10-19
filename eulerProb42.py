#SOLVED
fileName = ('p042_words.txt')
file = open(fileName,'r')
line = file.read()
file.close()
lines = line.split("\",\"")
lines[-1] = lines[-1].strip("\"")
lines[0] = lines[0].strip("\"")
#print(lines)
print(lines[1][0])
numTri = 0
def triList(top):
    tList = []
    for n in range(1, top):
        tList.append((1/2)*n * (n+1))
    return tList

tList = triList(40)
print(tList)
numTri = 0

for l in lines:
    sumLet = 0
    for i in range(len(l)):
        sumLet += ord(l[i]) - 64
    if(sumLet in tList):
        numTri += 1

print("numTri --> ", numTri)
        
