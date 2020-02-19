
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

#
# ___________________________________________________________________________
#

class Pkw(Fahrzeug):
 # Konstruktor Methode
 def __init__(self, bez, ge, pers):
  Fahrzeug.__init__(self, bez, ge)
  self.personen=pers
 def __str__(self):
  return Fahrzeug.__str__(self) + " " + str(self.personen) + " Personen"
 
 def einsteigen(self, anzahl):
  self.personen += anzahl
 def aussteigen(self, anzahl):
  self.personen -= anzahl

# Ein Objekt instanzieren
fiat = Pkw('Fiat Pasta', 50, 0)

print('fiat = ', fiat)

fiat.einsteigen(3)
# fiat.aussteigen(1)
# fiat.speed()
