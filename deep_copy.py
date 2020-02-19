# 

from copy import deepcopy
d = {"a":3, "b":4}

copy_of_d = deepcopy(d)

print(d)

print(copy_of_d)

p = {"Frank":{"Gewicht":74.8, "Grösse":183.4}, "Sarah":{"Gewicht":57.3, "Größe": 168.9}}

# einfache kopie

# p2 = p.copy()
# p["Sarah"]["Gewicht"] -= 0.4

# print(p)
# print(p2)

p2 = deepcopy(p)
p["Sarah"]["Gewicht"] -= 0.4

print(p)
print(p2)

