import numpy as np;
import time
st = time.time()

def fileToList(fileName):
    arr = np.zeros((81,81))
    file = open(fileName,'r')
    lines = file.readlines()
    file.close()
    for j in range(len(lines)):
        lines[j] = list(lines[j].split(","))
        for i in range(len(lines[j])):
            arr[j][i] = int(lines[j][i])
    return arr
arr = fileToList('p081_matrix.txt')
#print(arr[79][79])
arr1 = arr.copy()
#Idea on a smaller scale: 
# [2, 3, 5] --> [2, 3, 5] --> [2, 3, 9]  --> [2, 12, 0] ANS = 14
# [3, 9, 2] --> [3, 9, 4] --> [3, 13, 0] --> [14, 0, 0]
# [4, 5, 2] --> [4, 7, 0] --> [11, 0, 0] --> [0, 0, 0]

addMin = lambda row, col, arr: min(arr[row+1][col], arr[row][col+1])
sList = []
for iter in range (1, 159):
    sList = []
    for row in range (79, 79- 3*iter, -1):
        for col in range(79, 79- 3*iter, -1):
            if( row+col+iter == 158):
                sList.append([row, col])
                if(row==79):
                    arr[row][col] += arr[row][col+1]
                elif(col==79):
                    arr[row][col] += arr[row+1][col]
                else:
                    arr[row][col] += addMin(row, col, arr)
    for s in sList:
        arr[s[0]+1][s[1]], arr[s[0]][s[1]+1] = 0, 0


print(arr[:80][:80])
print(int(arr[0][0]))
#Correct, Answer = 427337

et = time.time()
print(f"Run Time {str(et-st)[0:6]} sec")