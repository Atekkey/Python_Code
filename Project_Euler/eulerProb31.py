#There are eight coins in general circulation:
#1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
#How many different ways can £2 be made using any number of coins?
coinList = [1, 2, 5, 10, 20, 50, 100, 200]
count = 0
sum = 0
for a in range(201):
    print(a)
    for b in range(101):
        for c in range(41):
            for d in range(21):
                for e in range(11):
                    for f in range(5):
                        for g in range(3):
                            for h in range(2):
                                sum =  a*coinList[0] + b*coinList[1] + c*coinList[2] + d*coinList[3] + e*coinList[4] + f*coinList[5] + g*coinList[6] + h*coinList[7]
                                if(sum==200):
                                    count+=1
                                sum = 0
print("count is: ", count)