# Eduard

# input
n = int(input('Gib bitte eine ganze Zahl ein: '))

# function
def multiplizieren3(n):
    if n == 0:
        return 0
    elif n == 1:
        return 3
    else:
        return multiplizieren3(n-1) + 3

# output
print("Die Zahl:", n, "und um 3 vervielfacht:", multiplizieren3(n), end=".")10