import numpy as np

import matplotlib.pyplot as plt

languages=['Java', 'C', 'C++', 'Python', 'C#', 'JavaScript', 'PHP', 'Ruby']
popularity=[17.25, 16.08, 6.11, 10.30, 4.80, 2.09, 2.04, 1.31]

colors=["b", "r", "m", "g", "c", "y", "b", "yellow"]
colors2=["black", "black", "black", "black", "black", "black", "black", "black"]
explode=(0.2, 0.1, 0.1, 0.1, 0, 0, 0, 0)

# plt.margins(0)
# plt.plot(lang, popularity, label='Linie 2', linewidth=3)

plt.xlabel('Languages')
plt.ylabel('Popularity in %')

plt.title('Languages popularity in %')

xpos=range(len(languages))
plt.xticks(xpos, languages) # for i in range xpos: languages[i]
plt.yticks()


# plt.pie(popularity, labels=languages, explode=explode, color=colors, shadow=True, startangle=140)
plt.bar(xpos, popularity, color=colors, alpha=0.5,  zorder=100)
plt.bar(xpos, popularity, color=colors2, zorder=50, offset = 72)
# Grid hinzufügen

plt.minorticks_on() # minor grid einschalten
plt.grid(which='major', linestyle='-', linewidth='0.3', color='black')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')

plt.show()

# schatten https://matplotlib.org/3.1.1/tutorials/advanced/transforms_tutorial.html
