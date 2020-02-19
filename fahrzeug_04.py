# eine Klasse bauen, bzw. definieren:
# Life-Time (Lebenszeit, Lebensdauer)
# Danach lebt das Object nicht mehr
# Achtung: Allerdings, können Objectinstanzen doch gespeichert werden
class Fahrzeug:
  # Konstruktor
  def __init__(self, bez, ge):
    self.bezeichnung = bez
    self.geschwindigkeit = ge
  # ...........
  def speed(self, wert):
    self.geschwindigkeit += wert

  def __str__(self):
    return self.bezeichnung + " " + str(self.geschwindigkeit) + "km/h"


# Objekte erzeugen
opel = Fahrzeug("Opel Admiral", 40)

# Kopie eines Objektes
ein_zweites_opel = Fahrzeug(opel.bezeichnung, opel.geschwindigkeit)
ein_zweites_opel.speed(100)

# Tiefe Kopie
import copy
dritt_opel=copy.deepcopy(opel)
dritt_opel.speed(200)

# Neue Referenz
viertes_opel=opel
viertes_opel.speed(20)

print("opel = ", id(opel))
print("ein_zweites_opel = ", id(ein_zweites_opel))
print("dritt_opel = ", id(dritt_opel))
print("viertes_opel = ", id(viertes_opel))

print(opel is ein_zweites_opel)
print(opel is dritt_opel)
print(opel is viertes_opel)