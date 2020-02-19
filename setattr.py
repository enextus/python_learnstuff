# Klasse def
class Klasse:
 def __init__(self):
  pass

# obj
k=Klasse()

# setattr(obj, 'farbe', 'rot')
setattr(k, 'farbe', 'rot')

print(k.farbe)
print(dir(Klasse))

# getattr
print(getattr(k, 'farbe'))

# hasattr(obj, attributsname)
print(hasattr(k, 'farbe'))

# delattr(obj, attributsname)
delattr(k, 'farbe')

print(hasattr(k, 'farbe'))

# #####################################

class F:
 def myfunc(self):
  print('hi')
print(dir(F))

l = dir(F)

for i in l:
 if i[0] == '_' and i[1] == '_':
  continue
 else: print(i)


