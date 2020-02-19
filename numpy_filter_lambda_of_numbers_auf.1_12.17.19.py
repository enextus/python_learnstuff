import numpy as np

listofNum = [1,3,33,12,34,56,11,19,21,34,15]

# Filter list of numbers by keeping numbers from 10 to 20 in the list only
listofNum = list(filter(lambda x : x%2, listofNum))
print('Filtered List : ', listofNum)

# a[start:end]       alle Elemente ab start bis end-1
# a[start:]          alle Elemente ab start bis zum Ende
# a[:end]            alle Elemente vom Anfang bis zu end-1
# a[:]               alle Elemente
# a[start:end:step]  Ellemente nach start Schrittweite step vor end
# a[-1]              das letzte Element
# a[-2:]             die letzten beiden Elemente
# a[:-2]             alle bis auf die letzten beiden Elemente
# a[::-1]            gesamtes Array rueckwaerts auslesen