#SOLVED
#If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
"Maybe I can make a list of all of the most used words, then identify when the words are needed in a number"
ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["ten", "eleven" , "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"] #exception on 15
#GOAL No.1, how many letters from 1 to 99



onesSum = 0
for i in ones:
    onesSum += len(i) # 1:9 = 36
teensSum = 0
for j in teens:
    teensSum += len(j) #10:19 = 70

hundoSum = 0
for x in range(2, 10): # x is the tens
    for y in range(0, 10): # y is the ones
        hundoSum += len(tens[x]) + len(ones[y])
hundoSum += teensSum + onesSum 
# 1 : 99 = 854
fullSum = hundoSum * 10 
hundos = [""] * 10
for z in range(1, 10):
    hundos[z] = ones[z] + "hundred"
for s in range(1, 10):
    fullSum += len(hundos[z]) * 100
    fullSum += len("and") * 99
fullSum += len("onethousand")
print(fullSum)

