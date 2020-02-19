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
  # custome methods
  def speed(self, wert):
    self.geschwindigkeit += wert
    self.ausgabe()
  def ausgabe(self):
    print(self.bezeichnung, self.geschwindigkeit, "km/h")

# # Objektinstanzen erzeugen
opel = Fahrzeug('opel admiral')
toyota = Fahrzeug('toyota iris', 45)
# # Überprüfung
opel.ausgabe()
toyota.ausgabe()
del opel
del toyota

