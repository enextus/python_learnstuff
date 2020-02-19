# reduce()

# reduce() ist seit Python 3.0 nicht mehr als built-in function
# functools

import functools

# reduce(func, array)
# array = a, b, c, d
# w1 = func(a, b)
# w2 = func(w1, c)
# w3 = func(w2, d)#

# nested functions !!! recursive Aufruf

temp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(functools.reduce(lambda x,y: x*y, temp))


