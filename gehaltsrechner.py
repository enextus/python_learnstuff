# Module Gehaltsrechner

from mitarbeiter import Mitarbeiter

class Gehaltsrechner(Mitarbeiter):
 """ Klass Gehaltsrechner """
 def __init__(self, familienstand, anzahl_der_kinder, gehalt, freibetrag, netto_monatsgehalt, sozialversicherungsbeitraege_berechnet, all_einkommenssteuer_berechnet):
   self.familienstand = familienstand
   self.anzahl_der_kinder = int(anzahl_der_kinder)
   self.gehalt = float(gehalt)
   self.freibetrag = float(freibetrag)
   self.netto_monatsgehalt = float(netto_monatsgehalt)
   self.sozialversicherungsbeitraege_berechnet = sozialversicherungsbeitraege_berechnet
   self.all_einkommenssteuer_berechnet = all_einkommenssteuer_berechnet
   self.steuersatz = 0
 # Methoden
 def get_steuerzatz(self):
   if float(self.gehalt) > 4000.0 and self.familienstand == 'alleinstehende':
     self.steuersatz = 26
   elif float(self.gehalt) <= 4000.0 and self.familienstand == 'alleinstehende':
     self.steuersatz = 22
   elif float(self.gehalt) <= 4000.0 and (self.familienstand == 'verheiratet' or self.familienstand == 'alleinerzihend'):
     self.steuersatz = 18
   elif float(self.gehalt) > 4000.0 and (self.familienstand == 'verheiratet' or self.familienstand == 'alleinerzihend'):
     self.steuersatz = 22
   return self.steuersatz

 def get_netto_monatsgehalt(self):
   sozialabgaben = float(self.sozialversicherungsbeitraege_berechnet['krankenversicherung']) + float(self.sozialversicherungsbeitraege_berechnet['pflegeversicherung']) + float(self.sozialversicherungsbeitraege_berechnet['rentenversicherung']) + float(self.sozialversicherungsbeitraege_berechnet['arbeitslosenversicherung']) 
   einkommensteuer = float(self.all_einkommenssteuer_berechnet['soli_zuslag']) + float(self.all_einkommenssteuer_berechnet['kirchensteuer'])
   self.netto_monatsgehalt = (self.gehalt - sozialabgaben - einkommensteuer) - self.prozent_berechnen(self.gehalt - self.freibetrag, self.get_steuerzatz()) 
   return self.netto_monatsgehalt
