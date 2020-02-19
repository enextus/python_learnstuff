# Eduard

# eingabe
n = int(input('n-Zahl bitte eingeben: '))

# list
nat_zahlen = list(range(2,n))
a = True

# loop
for x in nat_zahlen:
 for y in nat_zahlen:
     if x != y and y != 1:
         if not x % y:
             a = False
             break
 if a == True:
     print(x,end=' ')
 a = True
