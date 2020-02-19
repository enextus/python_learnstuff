# Eduard
import numpy as np
cities=[("Berlin", 12), ("Hamburg", 10), ("Düsseldorf", 11), ("Frankfurt", 9)]
[print(int(i[1])*9/5+32) for i in np.array(cities)]