import numpy as np
import random
# from random import *

# arange(start, stop, step)
z = np.arange(1, 50, 3)
print(z)
# [ 1  4  7 10 13 16 19 22 25 28 31 34 37 40 43 46 49]
print()
# ones(): ein Array mit 1 befüllt
t = np.ones(5)
print(t)
print()
u=np.ones((3, 4)) # 3 Zeilen und 4 Spalten
print(u)
print()
w=np.zeros((3, 4)) # 3 Zeilen und 4 Spalten
print(w)

# Zufall-Array
randy=np.random.randint(0, 100, 10)
print(randy)
# Zufall-Array: mehrdimensional
randy2=np.random.randint(0, 100, (3,5))
print(randy2)