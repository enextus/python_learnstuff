print(f"sum([1,32]): {sum([1,32])}")

import numpy as np 
# np.prod() , ndarray.prod (equivalent method)
# вычисляет произведение элементов массива
x = np.array([1,2,3,4,5])

print(x)
print(np.prod(x))
print(x.prod())
""" 
3
6
[1 2 3 4 5]
120
120
"""

v = np.random.seed()
v = np.random.randint(0, 1000, 10)
print(f"v: {v}")

"""
v: [226 346 449 490 277  14  89 908   5 843]
"""