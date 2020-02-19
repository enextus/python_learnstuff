# Eduard
# pandas 

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("weather.csv", delimiter=',')

print(f'\n')
print(f'\n')
print(df.__dict__)
print(f'\n')
print(f'\n')


sunshine_duration = []

for row in df.iterrows():
    pos= row[0]
    info= row[1]
    sunshine_duration.append(info['Sunshine'])
    
x=range(366)
y=sunshine_duration

plt.margins(0)

plt.plot(x, y, label='Linie 2', linewidth=2, color='yellow')
plt.xlabel('Days number')
plt.ylabel('Sunshine duration in hours')

plt.title('Sunshine duration of the days in year.')
plt.legend()
plt.show()