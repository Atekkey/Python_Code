#SOLVED
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

"""
for a in range(97, 123):
    for b in range(97, 123): #123
        for c in range(97, 123):
            phrase = ""
            for i in range(len(lineFixInt)):
                if (i % 3 == 0):
                    phrase += chr(lineFixInt[i] ^ a)
                if (i % 3 == 1):
                    phrase += chr(lineFixInt[i] ^ b)
                if (i % 3 == 2):
                    phrase += chr(lineFixInt[i] ^ c)
            if " the " in phrase:
                print(a, b, c, phrase)
"""
phrase = ""
sum = 0
for i in range(len(lineFixInt)):
    if (i % 3 == 0):
        phrase += chr(lineFixInt[i] ^ 101)
        sum += lineFixInt[i] ^ 101
    if (i % 3 == 1):
        phrase += chr(lineFixInt[i] ^ 120)
        sum += lineFixInt[i] ^ 120
    if (i % 3 == 2):
        phrase += chr(lineFixInt[i] ^ 112)
        sum += lineFixInt[i] ^ 112
    print(phrase)

print("done", sum)