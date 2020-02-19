# Dictionary: Datensequenz, nicht-geordnet, indiziert und änderbar
# Syntax: mydictionary = 

mydict = {'rot':'red', 'gruen':'green', 'blau':'blue', 'gelb':'yellow'}
print(mydict)

# Ein Element auslesen
print(mydict['rot'])

# ein neues Element eintagen
mydict['schwarz'] = 'black'
print(mydict)

x = mydict.get('schwarz')
print(mydict.get('schwarz'))
print(x)

# Einen Wert ändern, erstzen oder verbessern
mydict['grau'] = 'brown'
print(mydict)

mydict['grau'] = 'grey'
print('Korrigiert: \n', mydict)

# Duplikate sind nicht erlaubt.
mydict2 = {'rot':'red', 'rot':'green', 'rot':'blue', 'rot':'yellow'}
print('Korrigiert: \n', mydict2)

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

# key-value paare:
for x in mydict2.values():
    print(x)


for x, y in mydict2.items():
    print(x, y)

