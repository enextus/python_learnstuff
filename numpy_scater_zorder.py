import numpy as np
import matplotlib.pyplot as plt
from pylab import randn

x1=randn(30)
y1=randn(30)

x2=randn(30)
y2=randn(30)

plt.scatter(x2,y2, color='y', s=100, label='Böse', zorder=2)
plt.scatter(x1,y1, color='r', s=100, label='Guten')

plt.xlabel('X')
plt.ylabel('Y')

plt.legend()
plt.show()