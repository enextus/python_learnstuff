# build-in function zip

z = zip(((3,5,6),(12,14,16),(21,25,27)))

print(z)
print(type(z))


x = ['rot', 'gruen', 'blau']
y = ['red, green', 'blue']

for counter, farbe, color in zip(range(1, len(x)), x, y):
    print(counter + '. ' + ' heißt im Englischen: ' + color)

z1 = [11,12,13]
z2 = [21,22,23]
z3 = [31,32,33]

matrix = zip(z1,z2,z3)

print(list(matrix))

# ......................

a = [1,2,3]
b = "xyz"
c = (None, True)
 
res = list(zip(a, b, c))
print (res)
 
[(1, 'x', None), (2, 'y', True)]

# .................................

# iterieren !!! kann man sehr leicht

country = ['Germany', 'Italy', 'France', 'Russia']
cap = ['Berlin', 'Rome', 'Paris', 'Moscow']

# list 