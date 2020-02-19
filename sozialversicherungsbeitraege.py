
from mitarbeiter import Mitarbeiter

class Sozialversicherungsbeitraege(Mitarbeiter):
 """ Klass Sozialversicherungsbeiträge """
 # Konstruktor
 def __init__(self, name, personal_id, steuerklasse, familienstand, anzahl_der_kinder, gehalt):
  super().__init__(name, personal_id, steuerklasse, familienstand, anzahl_der_kinder, gehalt)
  self.krankenversicherung = 14.60
  self.pflegeversicherung = 3.05
  self.rentenversicherung = 18.60
  self.arbeitslosenversicherung = 2.50
 # Methoden
 # Methode zum Berechnen von Sozialversicherungsbeitraege
 def get_sozialversicherungsbeitraege(self):
  self.sozialversicherungsbeitraege={'krankenversicherung':self.krankenversicherung,     
                                      'pflegeversicherung':self.pflegeversicherung, 
                                      'rentenversicherung':self.rentenversicherung, 
                                      'arbeitslosenversicherung':self.arbeitslosenversicherung
                                      }
  return self.sozialversicherungsbeitraege
 # Methode zum Berechnen von Sozialversicherungsbeitraege
 def get_sozialversicherungsbeitraege_berechnet(self):
  self.sozialversicherungsbeitraege_berechnet={'krankenversicherung':self.prozent_berechnen(self.gehalt, self.krankenversicherung),
                                      'pflegeversicherung':self.prozent_berechnen(self.gehalt, self.pflegeversicherung), 
                                      'rentenversicherung':self.prozent_berechnen(self.gehalt, self.rentenversicherung), 
                                      'arbeitslosenversicherung':self.prozent_berechnen(self.gehalt, self.arbeitslosenversicherung)
                                      }
  return self.sozialversicherungsbeitraege_berechnet
