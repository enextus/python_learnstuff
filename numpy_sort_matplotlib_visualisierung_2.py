import numpy as np

import matplotlib.pyplot as plt

# x=np.arange(0, 75, 1)

# y=np.sin(x)

# plt.plot(x,y)
# plt.xlabel('x-werte')
# plt.ylabel('y-werte')
# plt.title('Eine Linie')

# plt.show()

# x=[1,2,3]
# y=[2,5,2]

# plt.margins(0,0)
# plt.plot(x,y)
# plt.xlabel('x-werte')
# plt.ylabel('y-werte')
# plt.title('Überschrift')

# plt.show()

x1=[10,20,30]
y1=[20,40,20]

plt.margins(0)
plt.plot(x1, y1, label='Linie 1', linestyle='--')

x2=[15,25,35]
y2=[20,40,20]

plt.margins(0)
plt.plot(x2, y2, label='Linie 2', linewidth=2)

plt.xlabel('x-werte')
plt.ylabel('y-werte')

# plt.xlim(0,10)
# plt.ylim(0,10)

plt.title('Überschrift')
plt.legend()
plt.show()