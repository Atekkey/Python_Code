#Find the smallest prime which, by replacing part of the number 
# (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.

#Basic Func "isFamily" input, two nums, output if they are close 

def isFamily(num1, num2):
    n1s, n2s = str(num1), str(num2)
    while(len(n1s)>len(n2s)): #Make the lengs equal (incase of leading 0's)
        n2s = "0" + n2s
    while(len(n2s)>len(n1s)):
        n1s = "0" + n1s
    indList = []
    for i in range(len(n1s)): #Find index of diffDigits
        if(n1s[i] != n2s[i]):
            indList.append(i)
    repDigBool = True
    if(len(indList)>1):
        for i in indList[0:len(indList)-1]:
            if(n1s[i]!=n1s[i+1]): repDigBool = False
            if(n2s[i]!=n2s[i+1]): repDigBool = False 
    if(repDigBool):
        print("Family:", n1s, n2s)
        print("repDig index:", indList)
    return 
isFamily(56003, 56223)
