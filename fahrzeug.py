# class Fahrzeug
class Fahrzeug:
  # Konstruktor
  def __init__(self, bezeichnung, geschwindigkeit=0):
    self.bezeichnung = bezeichnung
    self.geschwindigkeit = geschwindigkeit
  # ...........
  def beschleinigen(self, wert):
    self.geschwindigkeit += wert

  def __str__(self):
    return self.bezeichnung + " " + str(self.geschwindigkeit) + "km/h"

# Test

if __name__ == "__main__":
  f = Fahrzeug('opel')
  print('f = ', f)
  f.beschleinigen(10)
  print('f = ', f)
