# class Fahrzeug
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