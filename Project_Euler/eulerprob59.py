# chr(int), ord(int), int1 ^ int2 is XOR
#print(ord('a'), ord('z')) yields 97, 122
fileName = "p059_cipher.txt"
file = open(fileName,'r')
line = file.readlines()[0]
file.close()
lineFix = line.split(",")
lineFixInt = []
for l in lineFix:
    lineFixInt.append(int(l))
print(lineFixInt)