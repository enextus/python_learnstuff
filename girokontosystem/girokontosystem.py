# Girokonto Klass

# import random
import random

# class Inhaber
class Inhaber:
 """ Klass Inhaber """
 # Konstruktor
 def __init__(self, name, adresse, telefon, e_mail):
  self.name = name
  self.adresse = adresse
  self.telefon = telefon
  self.e_mail = e_mail

 # Methoden
# ________________________________________________________ #

# class Konto
class Konto(Inhaber):
 """ Klass Konto """
 # Konstruktor
 def __init__(self, name, adresse, telefon, e_mail):
  super().__init__(name, adresse, telefon, e_mail)
  self.kontonummer = self.get_kontonummer()
  self.kontostand = 0.0
  self.tages_limit_fuer_abzuege = 1000.0
  self.tages_abzuege = 0.0
  self.tagesumsatz = 0.0
  self.konto_ist_da()

 # Methoden
 # Methode zum Berechnen von Prozenten
 def prozent_berechnen(self, x, y):
   x = float(x)
   y = float(y)
   return round((x * y / 100.0), 2)
 # Methode Transfer
 def get_kontonummer(self):
   return random.randint(0, 1000000000)
 # Methode Transfer
 def make_transfer(self, transfer_summe):
  transfer_summe = float(transfer_summe)
  if transfer_summe <= self.kontostand and (self.get_tages_abzuege() + transfer_summe) <= self.get_tages_limit_fuer_abzuege():
    self.kontostand -= transfer_summe
    self.tages_abzuege += transfer_summe
    return self.kontostand
  else:
    return False
 # Methode Einzahlung
 def make_einzahlung(self, einzahlung):
  einzahlung = float(einzahlung)
  if einzahlung >= 0:
    self.kontostand += einzahlung
    self.tagesumsatz += einzahlung
    return self.kontostand
  else:
    return False
 # Methode Auszahlung
 def make_auszahlung(self, auszahlung):
  auszahlung = float(auszahlung)
  if (auszahlung <= self.kontostand) and ((self.get_tages_abzuege() + auszahlung) <= self.get_tages_limit_fuer_abzuege()):
    self.kontostand -= auszahlung
    self.tagesumsatz += auszahlung
    self.tages_abzuege += auszahlung
    return self.kontostand
  else:
    return False
 # Methode Kontostand prüffen
 def get_kontostand(self):
  return self.kontostand
 # Methode Tagesumsatz prüffen
 def get_tagesumsatz(self):
  return self.tagesumsatz   
 # Methode tages_abziehen prüffen
 def get_tages_abzuege(self):
  return self.tages_abzuege
 # Methode tages_abziehen prüffen
 def get_tages_limit_fuer_abzuege(self):
  return self.tages_limit_fuer_abzuege  
 # Mtehode konto_ist_da
 def konto_ist_da(self):
  return print('Das Konto', self.kontonummer, 'ist für', name, 'nun geöffnet.')
# ________________________________________________________ #

# seeds
name, adresse, telefon, e_mail  ='Ed Park', 'Ostseestr. 67; 10409 Berlin', "016099813206", "eduardberlin@gmail.com"

# Make Object
k = Konto(name, adresse, telefon, e_mail)

# show the values of the object
print(k.__dict__)