play1 = input("Player one Choice (R/P/S)")
play2 = input("Player one Choice (R/P/S)")
if(play1 == play2):
    print("Its a tie!")
if( (play1 == "R" and play2 == "S")  or (play1 == "P" and play2 == "R")   or  (play1 == "S" and play2 == "P")):
    print("Player 1 wins!")
else:
    print("Player 2 wins!")