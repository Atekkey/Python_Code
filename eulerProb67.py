file = open('p067_triangle.txt','r')
lines = file.readlines()
file.close()
for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", "").replace(" ", ", ").replace(" 0", " ")
lines = list(lines)
for j in range(len(lines)):
    lines[j] = list(lines[j].split(", "))
#print(lines)
#BRUTE FORCE
print('\n')
def bestSum(lines):
    countMax = 0
    for x in range(2**(len(lines)-1)):
        binary = bin(x).replace("b", "")
        binary = binary.zfill(len(lines))
        countCur = int(lines[0][0])
        placeCur = 0
        if(x%10000==0):
            print(f"Current: {x} | check#{x}:{countMax} ")
        for y in range(1,len(lines)):
            placeCur += int(binary[-y])
            countCur += int(lines[y][placeCur])
        if(countCur > countMax):
            countMax = countCur
            print(f"check#{x}:{countMax}")
    return countMax

print(bestSum(lines))
#tested 5774, incorrect, tested up to 4mil

#Other possible strategy
#Break the triangle into smaller triangles, 
#the maximum path within each triangle is the value for that triangle
#Use this method to reduce the amount of rows, work from the bottom up

def rowReduce(lines, row):
    for i in range(row):
        for j in range(len(lines[-(row+2)])):
            lines[i]