def recurse(x):
    if(x == 0):
        return 0
    else:
        return 1 / (2 + recurse(x-1))

z = (recurse(3) + 1)
print(10 * z - z)