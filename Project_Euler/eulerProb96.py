# Get all 50 puzzles
fileName = ('Py1/Project_Euler/p096_sudoku.txt')
file = open(fileName,'r')
line = file.read()
file.close()
lines = line.split("Grid")
lines.remove(lines[0])
# Format one puzzle
myPuzzle = lines[0][4:93]
rows = myPuzzle.split("\n")
myPuzzle = [[0 for k in range(9)] for j in range(9)]
for row in range(9):
    for col in range(9):
        myPuzzle[row][col] = int(rows[row][col])

# Format a solved Puzzle
solvLine = ["298317645","764285139","153946278","327168954","981453726","645792813","539821467","872634591","416579382"]
solvedPuzzle = [[0 for k in range(9)] for j in range(9)]
for row in range(9):
    for col in range(9):
        solvedPuzzle[row][col] = int(solvLine[row][col])


class Puzzle():

    def __init__(self, myPuzzle):
        self.origPuzzle = myPuzzle
        self.current = myPuzzle.copy()
        self.nineSet = {1,2,3,4,5,6,7,8,9}

    def checkNine(self, array):
        return set(array) == self.nineSet and len(array) == 9

    def checkRow(self, row):
        intList = []
        for i in range(9):
            intList.append(self.current[row][i])
        return self.checkNine(intList)
    
    def checkCol(self, col):
        intList = []
        for i in range(9):
            intList.append(self.current[i][col])
        return self.checkNine(intList)
    
    def getBlock(row, col):
        blockRow = int(row/3) * 3
        blockCol = int(col/3) * 3
        return blockRow, blockCol
    
    def checkBlock(self, blockRow, blockCol):
        intList = []
        for row in range(blockRow, blockRow+3):
            for col in range(blockCol, blockCol+3):
                intList.append(self.current[row][col])
        return self.checkNine(intList)
    
    def checkSpot(self, row, col):
        blockTuple = Puzzle.getBlock(row,col)
        return self.checkBlock(blockTuple[0], blockTuple[1]) and self.checkCol(col) and self.checkRow(row)
    
    def getMissingNums(self, row, col):
        mySet1 = set([self.current[row][i] for i in range(9)])
        mySet2 = set([self.current[i][col] for i in range(9)])
        bT = Puzzle.getBlock(row, col)
        mySet3 = set([])
        for row in range(bT[0], bT[0]+3):
            for col in range(bT[1], bT[1]+3):
                mySet3.add(self.current[row][col])
        return self.nineSet.difference(mySet1, mySet2, mySet3)


#Check notSolv
notSolv = Puzzle(myPuzzle)
testArray = [1,2,4,3,5,6,7,8,9]
print(notSolv.checkCol(0))

#Check Solv
solv = Puzzle(solvedPuzzle)
boolList = []
for i in range(9):
    for j in range(9):
        boolList.append(solv.checkSpot(i, j))
print(set(boolList))

#Workspace
print(notSolv.getMissingNums(0, 0))
