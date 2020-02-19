# module import
from fahrzeug import Fahrzeug


# class LKW
class Lkw(Fahrzeug):
 def __init__(self, bezeichnung, geschwindigkeit, beladen=0):
  Fahrzeug.__init__(self, bezeichnung, geschwindigkeit=0)
  self.beladen=beladen

 def volume(self, wert):
  self.beladen += wert

 def __str__(self):
  return Fahrzeug.__str__(self) + " " + str(self.beladen) + " Kilogramm"

# Test
lkw = Lkw('opel', 55, 0)
print('lkw = ', lkw)
print(lkw.beladen)
print('lkw = ', lkw)
lkw.volume(300)
print('lkw = ', lkw)