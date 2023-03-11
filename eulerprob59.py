# chr(int), ord(int), int1 ^ int2 is XOR
#print(ord('a'), ord('z')) yields 97, 122
fileName = "p059_cipher.txt"
file = open(fileName,'r')
line = file.readlines()
file.close()
#have list of strings, need to convert to int