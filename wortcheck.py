# input

dictionary = {}
wort = input('Gib bitte ein Wort ein: ')

# abca

for element in wort:
    dictionary[element] = wort.count(element)

    print(' i = ', element)

print(dictionary)


