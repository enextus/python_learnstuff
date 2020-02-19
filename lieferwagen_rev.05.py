# Eduard vererbung von 2 Klassen

# class Pkw
class Pkw:
  """ Klass PKW """
  # Konstruktor
  def __init__(self, bezeichnung, adp, geschwindigkeit=0):
   self.bezeichnung = bezeichnung
   self.anzahl_der_personen = adp
   self.geschwindigkeit = geschwindigkeit
  # Methoden
  def beschleinigen(self, wert):
   self.geschwindigkeit += wert
  def abbremsen(self, wert):
   self.geschwindigkeit -= wert
  # bound method
  def __str__(self):
    return self.bezeichnung + " " + str(self.geschwindigkeit) + "km/h"
  def __repr__(self):
    return self.bezeichnung + " " + repr(self.geschwindigkeit) + "km/h"

# class LKW
class Lkw:
 """ Klass LKW """
 def __init__(self, bezeichnung, geschwindigkeit, beladen=0):
  self.bezeichnung=bezeichnung
  self.geschwindigkeit=geschwindigkeit
  self.beladen=beladen
  self._privatisiert=0
  self.__starkprivatisiert=0

 def add_volume(self, wert):
  self.beladen += wert
 def sub_volume(self, wert):
  self.beladen -= wert 
 def __str__(self):
  return self.beladen + " " + str(self.beladen) + " Kilogramm"

# class Lieferwagen

class Lieferwagen(Pkw, Lkw):
 """ Klass LKW """
 def __init__(self, bezeichnung, adp, geschwindigkeit=0, beladen=0):
  Pkw.__init__(self, bezeichnung, adp, geschwindigkeit)
  Lkw.__init__(self, bezeichnung, geschwindigkeit, beladen)

 def add_person(self, wert):
   self.anzahl_der_personen += wert
 def sub_person(self, wert):
  self.anzahl_der_personen -= wert 


# Test
if __name__ == "__main__":
 l = Lieferwagen('Lieferwagen_001', 2, 10, 1000)
 print(Lieferwagen.mro())
 print('______________________________________')
 print('l.bezeichnung: ', l.bezeichnung)
 print('l.anzahl_der_personen: ', l.anzahl_der_personen)
 print('l.geschwindigkeit: ', l.geschwindigkeit)
 print('l.beladen: ', l.beladen)
 print('______________________________________')
 print("Die Größe der Menge zum Beladen: ", 300)
 l.add_volume(300)
 print("Das Volume nach der Beladung: ", l.beladen)
 print("Die Größe der Menge zum Entladen: ", 125)
 l.sub_volume(125)
 print("Das Volume nach der Entladung: ", l.beladen)
 print('______________________________________')
 print("Anzahl der Einsteigenden Personen: ", 5)
 l.add_person(5)
 print("Anzahl der Personen nach dem Einsteigen: ", l.anzahl_der_personen)
 print("Anzahl der aussteigenden Personen: ", 1)
 l.sub_person(1)
 print("Anzahl der Personen nach dem Aussteigen: ", l.anzahl_der_personen)
 print('______________________________________')
 print(l.__doc__)
