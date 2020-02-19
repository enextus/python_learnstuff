lst = [ [c for c in range(r)] for r in range(3) ]
print(f"1. lst: {lst}, type(lst): {type(lst)}\n")
for x in lst:
    print(f"2. x: {x}, type(x): {type(x)}\n")
    for y in x:
        print(f"3. y: {y}, type(y): {type(y)}\n")
        if y <2:
            print(f"\n")
            print(f"4. y: {y}, type(y): {type(y)}\n")
            print('*', sep=' : ', end='')

            