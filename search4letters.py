# Eduard

while True:
    wort = input('Bitte das Word eingeben: ')
    if wort.isdigit():
        print("bitte nur Wörter eingeben! ")
    else:
        break

while True:
    kombination = input('Bitte die Kombination eingeben: ')
    if kombination.isdigit():
        print("bitte nur Buchstaben eingeben! ")
    else:
        break

wort = set(wort)
kombination = set(kombination)

ergebnis = wort.intersection(kombination)

print("type wort = ", type(wort))
print("type wort = ", type(kombination))

print("wort = ", wort, "kombination = ", kombination)

print(" ergebnis = ", ergebnis)

