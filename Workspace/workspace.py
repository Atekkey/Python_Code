
"""play1 = input("Player one Choice (R/P/S)")
play2 = input("Player one Choice (R/P/S)")
if(play1 == play2):
    print("Its a tie!")
if( (play1 == "R" and play2 == "S")  or (play1 == "P" and play2 == "R")   or  (play1 == "S" and play2 == "P")):
    print("Player 1 wins!")
else:
    print("Player 2 wins!")"""

arr1 = [0,5]
arr2 = arr1.copy()
arr3 = [5,0]
#arr2[0] = 100
#print(arr2)
print(set(arr1) == set(arr2) == set(arr3))
