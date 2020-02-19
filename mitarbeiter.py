# class Mitarbeiter
class Mitarbeiter:
 """ Klass Mitarbeiter """
 # Konstruktor
 def __init__(self, name, personal_id, steuerklasse, familienstand, anzahl_der_kinder, gehalt):
  self.name = name
  self.personal_id = personal_id
  self.steuerklasse = steuerklasse
  self.familienstand = familienstand
  self.anzahl_der_kinder = anzahl_der_kinder
  self.sozialversicherungsbeitraege = 0
  self.sozialversicherungsbeitraege_berechnet = 0
  self.gehalt = gehalt
  self.all_einkommenssteuer = 0
  self.all_einkommenssteuer_berechnet = 0
  self.freibetrag=0
  self.netto_monatsgehalt = 0

 # Methoden
  # Methode zum Berechnen von Prozenten
 def prozent_berechnen(self, x, y):
   x = float(x)
   y = float(y)
   return round((x * y / 100.0), 2)
