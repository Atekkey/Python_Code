#SOLVED
from Prime import *
def distPFs(num):
    fList = prime_factors(num)
    fList = list(set(fList))
    return fList


#Scanned up to 259k, found a 4, incorrect
def main1(bot, top):
    for i in range(bot, top):
        if(i%1000 ==0): print(i, "out of", top)
        if(len(distPFs(i)) ==4):
            if(len(distPFs(i+1)) ==4):
                 if(len(distPFs(i+2)) ==4):
                    print("hit 3")
                    if(len(distPFs(i+3)) ==4):
                        print(i, i+1, i+2, i+3)
                        break
def main2(bot, top):
    for i in range(bot, top, 4):
        if(i%1000 ==0): print(i, "out of", top)
        if(len(distPFs(i)) == 4):
            if(len(distPFs(i+1)) ==4 or len(distPFs(i-1)) ==4 ):
                tList = []
                for t in range(-3, 4):
                    tList.append(len(distPFs(i + t)))
                for c in range(0, 4):
                    sub = tList[c : c+4]
                    if(sub == [4,4,4,4]):
                        print(tList, "found centered at ", i)
                        return i
    return

            

print(main2(100000, 200000))
#main1(259000, 261000)