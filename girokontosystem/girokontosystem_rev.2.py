# Girokonto Klass

# imports
import random
from itertools import count
from datetime import datetime
from os import system, name
import time

# class App_controller
class App_controller:
  # define our clear function 
  @staticmethod
  def clear(): 
      # for windows 
      if name == 'nt': 
          _ = system('cls')
      # for mac and linux(here, os.name is 'posix') 
      else: 
          _ = system('clear')
  @staticmethod
  def show_actions():
    messages = ['Wählen Sie die gewünschte Aktion aus, indem Sie eine Nummer aus der Liste eingeben: ',
                '\n'
                ' 1 - Konto erstellen',
                ' 2 - Einlogen',
                '__________________________________________________________________',
                "Zum Verlassen des Menüs  Sie Folgendes ein: 'exit'",
                '__________________________________________________________________']
    for i in messages:
          print(i)
  # Konstruktor
  def __init__(self):
        # super().__init__(name, adresse, telefon, e_mail)
        self.accounts = [] # alle Konten Objekte drin
        self.reprname = "obj-id: " + str(id(self))
        self.strname = "strname: App_controller"
        self.start_message = '\n*** Willkommen in das Girokontosystem! ***\n\n'
        self.get_start_message()

  # Magis methods
  def __str__(self):
        return self.strname
  def __repr__(self):
    return self.reprname

  # Object Methods
  # method check_action
  def check_action(self, choice):
    if choice == '1':
          self.create_konto(self, name, adresse, telefon, e_mail)
          return
    elif choice == '2':
      # self.einlogen()
      return 
    else:
      print('Bitte wiederholen Sie die Eingabe!')
      time.sleep(1)
      App_controller.clear()
      return
  # method get_start_message
  def get_start_message(self):
      print(self.start_message)
  
 # ###############    1 - Konto erstellen  ##################################

  # create_konto
  def create_konto(self, name, adresse, telefon, e_mail):
        k = Konto(name, adresse, telefon, e_mail)
        print(id(k))
        print(k.name)
        # @kontos[name.to_sym] = station
        # konto_created(station.name)
        return k

#  def konto_created(self, x):
#       return print(f'\n Konto «{x}» erstellt.')

#  # ###############    2 - In das Konto einlogen  ##################################

#   def einlogen(self):
#         pass

# ##################################################################################################



# class Inhaber
class Inhaber:
 """ Klass Inhaber """
 # Konstruktor

 def __init__(self, name, adresse, telefon, e_mail):
  self.name = name
  self.adresse = adresse
  self.telefon = telefon
  self.e_mail = e_mail
  self.reprname = "reprname: Klass Inhaber"
  self.strname = "strname: Klass Inhaber"  
# Magis methods
 def __str__(self):
      return self.strname
 def __repr__(self):
  return self.reprname


# class Konto
class Konto(Inhaber):
 """ Klass Konto """
 _ids = count(0) # Klassen-Objects zähler

 # Konstruktor
 def __init__(self, name, adresse, telefon, e_mail):
  self.id = next(self._ids)
  super().__init__(name, adresse, telefon, e_mail)
  self.kontonummer = self.generate_kontonummer()
  self.kontostand = 0.0
  self.tages_limit_fuer_abzuege = 1000.0
  self.tages_abzuege = 0.0
  self.tagesumsatz = 0.0
  self.das_konto_ist_da()
  self.reprname = "obj-id: " + str(id(self))
  self.strname = "strname: Klass Konto"
  self.timestamp = self.get_now()
# Magis methods
 def __str__(self):
      return self.strname
 def __repr__(self):
  return self.reprname
# a static method to check a datetime.
 @staticmethod
 def get_now():
    return datetime.now()
 @staticmethod
 def typename(x):
    return type(x).__name__
 # Object Methoden
 # Methode get_instance_counter
 def get_instance_counter(self):
    return self.id
 # Methode zum Berechnen von Prozenten
 def prozent_berechnen(self, x, y):
   x = float(x)
   y = float(y)
   return round((x * y / 100.0), 2)
 # Methode Transfer
 def generate_kontonummer(self):
   return random.randint(100000, 999999)
 # Methode get_kontonummer
 def get_kontonummer(self):
    return self.kontonummer
 # Methode Transfer
 def make_transfer(self, kontonummer, transfer_summe):
    # zeige nummer der vorhandenen Kontos an. ( 1. Konto... 2. Konto... 3. Konto...)
    # Wählen Sie die Kontonummer aus für die bevorstehende Überweisung.##
  transfer_summe = float(transfer_summe)
  if transfer_summe <= self.kontostand and (self.get_tages_abzuege() + transfer_summe) <= self.get_tages_limit_fuer_abzuege():
    self.kontostand -= transfer_summe
    self.tages_abzuege += transfer_summe
    # print(ko.id, ko.kontonummer, ko.kontostand)
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
 # Methode get_id prüffen
 def get_id(self):
  return self.id
 # Methode das_konto_ist_da
 def das_konto_ist_da(self):
  return print('Konto', self.kontonummer, 'für', self.name, 'nun geöffnet, ', 'Interne-ID: ', self.id)

if __name__ == "__main__":
  # # Make Objects and load seed over these
  # k1, k2, k3, k4 = Konto("Ed Park", "Ostseestr. 67 10409 Berlin",   "0160998132506", "eduardberlin@gmail.com"), Konto("Nikolaus", "Ostseestr. 77 10409 Berlin", "0160994563456", "berlin@gmail.com"), Konto("Markus", "Ostseestr. 277 10409 Berlin",  "0160935446455", "melle@gmail.com"), Konto("Stephan", "Ostseestr. 247 10409 Berlin", "0160435653455", "beer@gmail.com")

  # for i in [k1,k2,k3,k4]:
  #       if all(i.accounts):
  #             # eval(i.typename(i)).accounts.append(i)
  #             i.accounts.append(i)
  #       else:
  #         print("Das Array 'accounts' existiert nicht!")

  # for i in Konto.accounts:
  #   print('Kontonummer:', i.get_kontonummer())

  # now call function we defined above 
  App_controller.clear()
  app_controller = App_controller()

  while True:
        app_controller.show_actions()
        choice = str(input("Ihre Eingabe: "))
        if choice == 'exit':
                break
        app_controller.check_action(choice)


