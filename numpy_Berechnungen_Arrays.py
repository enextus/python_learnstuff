# numpy: numerical python
import numpy as np

# numpy eignet sich für Berechnungen mit Arrays
# array()
liste = [1,2,3]
a=np.array([1,2,3])
print(type(a)) # <class 'numpy.ndarray'>
print(liste)
print(a)
b = a + 5
print(b)
# l = [1,2,3]
# mittelwert .mean()
print(a.mean())
# mittelwert .max()
print(a.max())
# mittelwert .min()
print(a.min())
print(dir(a))
print(any(a))


# a[start:end]       alle Elemente ab start bis end-1
# a[start:]          alle Elemente ab start bis zum Ende
# a[:end]            alle Elemente vom Anfang bis zu end-1
# a[:]               alle Elemente
# a[start:end:step]  Ellemente nach start Schrittweite step vor end
# a[-1]              das letzte Element
# a[-2:]             die letzten beiden Elemente
# a[:-2]             alle bis auf die letzten beiden Elemente
# a[::-1]            gesamtes Array rueckwaerts auslesen