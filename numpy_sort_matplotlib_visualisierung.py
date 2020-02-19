import numpy as np

import matplotlib.pyplot as plt

# arr=np.random.randint(0, 11, 5)
# arr_sortiert=np.sort(arr)
# arr_absteigend= np.sort(-arr)

# print(arr)
# print(arr_sortiert)
# print(arr_absteigend)

# visualisierung
# eindimensionales array-object: werte für x-axe
x=np.arange(0, 11)
# werte für y-axe
y=np.sin(x)
print(y)

plt.plot(x, y)
plt.show()