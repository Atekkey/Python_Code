#SOLVED
def solveSquare(start, incr, sum):
    cur = start
    for q in range(4):
        cur += incr
        sum += cur
    end = cur
    return sum, end
    #ARGS) int incr : the num x num square, int start : the beginning number of the square, int sum : the running sum
    #OUT) int sum : the sum of the diag nums and input sum, int end : to pass as start for the recall

print(solveSquare(9, 4, 25))
start, sum = 25, 101
for i in range(6, 1001, 2):
    sum, start = solveSquare(start, i, sum)
    if(i%100 ==0): print(i, "out of", 1000)
print(sum)