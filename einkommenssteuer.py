# Module Einkommenssteuer

from mitarbeiter import Mitarbeiter

class Einkommenssteuer(Mitarbeiter):
 """ Klass Einkommenssteuer """
 # auf den monatlichen steuerfreien Betrag achten
 def __init__(self, name, personal_id, steuerklasse, familienstand, anzahl_der_kinder, gehalt):
  super().__init__(name, personal_id, steuerklasse, familienstand, anzahl_der_kinder, gehalt)
  self.soli_zuslag = 7.5
  self.kirchensteuer = 8.0

 # Methoden
 def get_freibetrag(self):
  self.steuerklasse = int(self.steuerklasse)
  if self.steuerklasse == 1:
    self.freibetrag = 1029.0
  elif self.steuerklasse == 2:
    self.freibetrag = 1225.0
  elif self.steuerklasse == 3:
    self.freibetrag = 1952.0
  return self.freibetrag

 # Methode zum Auflisten von Einkommenssteuer
 def get_all_einkommenssteuer(self):
  self.all_einkommenssteuer={'soli_zuslag':self.soli_zuslag,
                             'kirchensteuer':self.kirchensteuer
                             }
  return self.all_einkommenssteuer

 # Methode zum Berechnen von Einkommenssteuer
 def get_all_einkommenssteuer_berechnet(self):
  self.all_einkommenssteuer_berechnet={'soli_zuslag':self.prozent_berechnen(self.gehalt, self.soli_zuslag), 
                                       'kirchensteuer':self.prozent_berechnen(self.gehalt, self.kirchensteuer)
                                       }
  return self.all_einkommenssteuer_berechnet

