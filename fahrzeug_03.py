# eine Klasse bauen, bzw. definieren:
# Life-Time (Lebenszeit, Lebensdauer)
# Danach lebt das Object nicht mehr
# Achtung: Allerdings, können Objectinstanzen doch gespeichert werden
class Fahrzeug:
  pass
  # Konstruktor
  def __init__(self, bez, ge=0):
    self.bezeichnung = bez
    self.geschwindigkeit = ge
  # Destruktor
  # def __del__(self):
  #   print("Objekt", self.bezeichnung, " entfernt!")
  # # custome methods
  def __str__(self):
   return self.bezeichnung + " " + str(self.geschwindigkeit) + "km/h"
  
  def __repr__(self):
   return self.bezeichnung + " " + str(self.geschwindigkeit) + "km/h"

  def speed(self, wert):
    self.geschwindigkeit += wert
    self.ausgabe()
  def ausgabe(self):
    print(self.bezeichnung, self.geschwindigkeit, "km/h")

 # operator methoden
  def __eq__(self, other): # equal
   return self.geschwindigkeit == other.geschwindigkeit

  def __gt__(self, other): # greater than 
   return self.geschwindigkeit == other.geschwindigkeit
  def __ge__(self, other): # greater than or equal
   return self.geschwindigkeit == other.geschwindigkeit

 # Rechnop.
  def __sub__(self, other):
   return self.geschwindigkeit - other.geschwindigkeit
 
  def __lt__(self, other):  # less than <
   return self.geschwindigkeit == other.geschwindigkeit
 # Rechnop.
  def __le__(self, other): # less than or equal <= 
   return self.geschwindigkeit - other.geschwindigkeit


# # Objektinstanzen erzeugen
opel = Fahrzeug('opel admiral')
toyota = Fahrzeug('toyota iris', 45)
vw = Fahrzeug('vw CLS-300', 250)
# # Überprüfung
# opel.ausgabe()
# toyota.ausgabe()
# del opel
# del toyota

print(opel)
print(toyota)
print(vw)

# print(repr(opel))
# print(repr(toyota))
# print(repr(vw))

# print(str(opel))
# print(str(toyota))
# print(str(vw))

# vergleich
if opel == vw:
 print('Opel ist gleich VW')
elif opel > vw:
 print('Opel ist schneller als VW')
else:
 print('VW ist schneller')

# substract
# dif = opel - vw:
#  print()

# Built-In Rechnenmethoden

# +: __add__()
# -: __sub__()
# *: __mul__()
# /: __truediv__()
# //: __floordiv__()
# %: __mod__() 
# **: __pow__()

