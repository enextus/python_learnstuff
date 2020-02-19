import autos
# from autos import *
# fully qualified name, d.h. modul name.submodule.object
print(autos.auto_1['hersteller'])
print(autos.auto_2['hersteller'])
print(autos.auto_3['hersteller'])

# weistere Eigenschaft vergeben
autos.auto_1['geschwindigkeit'] = 120
print(autos.auto_1['geschwindigkeit'])

meinauto = autos.auto_1
autos.appendfunction(meinauto, 'geschwindigkeit', 530)

print(meinauto)
print(id(autos.auto_1))

print(id(meinauto))
autos.appendfunction(meinauto, 'geschwindigkeit', 2530)
print("meinauto['geschwindigkeit'] = ", meinauto['geschwindigkeit'])
print(meinauto)