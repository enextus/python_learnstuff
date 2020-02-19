import numpy as np

import matplotlib.pyplot as plt

from pylab import randn

x=[21,22,23,4,5,6,75,8,9,10,33,34,36,37,49,50,100]
num_bins=5
# histogramm
n, bins, patches = plt.hist(x, num_bins, facecolor='blue', alpha=1, zorder=100 )
plt.minorticks_on() # minor grid einschalten
plt.grid(which='major', linestyle='-', linewidth='0.3', color='black')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()