#1504170715041707n mod 4503599627370517
# E factors = 17 * 1249 * 12043
# M factors
"""
e = 1504170715041707
m = 4503599627370517
num = e
eulerCoins = [e]
skip = 0
for n in range(1, 5*10**6):
    n+=skip
    num = e*n % m
    if(num < min(eulerCoins)):
        eulerCoins.append(num)
        skip += 0
print("skip =", skip, "len =", len(eulerCoins), "min =", min(eulerCoins), "sum =", sum(eulerCoins))"""
