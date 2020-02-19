liste = [1, 2, 3, 4, 5]
tuple = ('', 1.03, True, 5)
# 'for each'

for element in liste:
    print(element, end= ' | ')

print()

for i in tuple:
    print(i, end= ' # ')

print()

mydict2 = {'rot':'red', 'gruen':'green', 'blau':'blue', 'gelb':'yellow'}

for i in mydict2:
    print(i, end= ' * ')

wort = 'dies ist kein wort, sondern ein Satz'
for x in wort:
    print(x*wort.index(x)))

#####
mydict2 = {'rot':'red', 'gruen':'green', 'blau':'blue', 'gelb':'yellow'}
for x, y in mydict2.items():
    print(x, y)

mydict3 = {'rot':'red', 'gruen':'green', 'blau':'blue', 'gelb':'yellow'}
for x in mydict3.keys():
    print(x)

# 