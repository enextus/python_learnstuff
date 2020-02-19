import numpy as np
import matplotlib.pyplot as plt

time_arr = np.arange(0, 11, 1)
print(f"02. time_arr: {time_arr}\n")

dist_arr = np.zeros(len(time_arr))
print(f"03. dist_arr: {dist_arr}\n")

dist_arr = np.array([404, 416.5, 420, 405, 415, 410, 420, 405, 415, 410, 429])
print(f"04. dist_arr: {dist_arr}\n")
print(f"05. type dist_arr: {type(dist_arr)}\n")

# logic
fig = plt.figure(figsize=(10,10))

plt.plot(time_arr, dist_arr, 'blue', linestyle='-', label='Höhenwerte', linewidth=1)

plt.xlabel('Zeit (m)', fontsize=25)
plt.ylabel('Wasser Höhenwerte', fontsize=25)
plt.tick_params(axis='x', labelsize=20)
plt.tick_params(axis='y', labelsize=20)
plt.title('Grafik für Höhenwerte', fontsize = 32, y=1.008)
plt.legend(loc='best', fontsize=25)

plt.show()
