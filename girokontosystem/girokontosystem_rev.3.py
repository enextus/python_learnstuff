# imports
import random
from itertools import count
from datetime import datetime
from os import system, name
import time

# ___________________________________________________________________________________________________________App_controller
class App_controller:
    """ 1. class App_controller """
    # define our clear function 
    @staticmethod
    def clear(): 
        # for windows 
        if name == 'nt': 
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else: 
            _ = system('clear')
    # define our show_actions
    @staticmethod
    def show_actions():
        messages = ['                                                                  ',
                    '_____Girokontosystem______________________________________________',
                    '',
                    'Wählen Sie die gewünschte Aktion aus, \nindem Sie eine Nummer aus der Liste eingeben: ',
                    '',
                    ' 1 - Konto erstellen',
                    ' 2 - Einlogen',
                    ' 3 - Anzahl der bestehenden Konten kontrolieren',
                    ' 4 - Die Konto-Objekte in der Liste anschauen',
                    '__________________________________________________________________',
                    "Zum Verlassen des Menüs  Sie Folgendes ein: 'exit'",
                    '__________________________________________________________________']
        for i in messages:
            print(i)

    # Konstruktor
    def __init__(self):
            self.a = None
            self.b = None
            self.c = None
            self.d = None
            self.accounts = [] # alle Konten Objekte kommen hier rein
            self.start_message = '\n*** Willkommen in das Girokontosystem! ***\n'
            self.print_something(self.get_start_message())
            self.reprname = "obj-id: " + str(id(self))
            self.strname = "strname: App_controller"

    # Magic methods
    def __str__(self):
            return self.strname
    def __repr__(self):
        return self.reprname
    
    # Methode check_action
    def check_action(self, x):
        if x == '1':
            # hier soll das Konto erstellt werden
            self.make_clear_with_sleep()
            return self.create_konto()
        elif x == '2':
            self.make_clear_with_sleep()
            return self.einlogen()
        elif x == '3':
            self.make_clear_with_sleep()
            x = "Anzahl der Konten: "
            return self.print_something(x, self.get_anzahl_der_konten())
        elif x == '4':
            self.make_clear_with_sleep()
            x = "Die Konten als Objekte sehen so aus:\n"
            return self.print_something(x, self.show_anzahl_der_konten())
        else:
            print('Bitte wiederholen Sie die Eingabe!')
            return self.make_clear_with_sleep()

    # Methode clear disprlay:
    def make_clear(self):
        return App_controller.clear() 
    # Methode clear disprlay with sleep time:
    def make_clear_with_sleep(self, x=1):
        time.sleep(x)
        return App_controller.clear()
    # Methode get_start_message
    def get_start_message(self):
        return self.start_message
    # create_konto
    def create_konto(self):
        obj = Konto.from_input()
        self.accounts.append(obj)
        return obj
    # check Anzahl der Konten
    def get_anzahl_der_konten(self):
        return len(self.accounts)
    # schow Konten-Objects
    def show_anzahl_der_konten(self):
        return self.accounts
    # print wrapper
    def print_something(self, x='', y=''):
        return print(f'{x}{y}')


# ___________________________________________________________________________________________________________Input_data
class Inputdata:
    """ 2. class Inputdata """
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.reprname = "obj-id: " + str(id(self))
        self.strname = "strname: Input_data"
    # Methode check_input
    @classmethod
    def check_input_name(x):
        while True:
            x = input('Wähle die Name aus: ')
            # Leerzeichen entfernen
            x = x.strip() 
            if x:
                break
            else:
                print("Darf nicht leer sein, bitte Eingabe!")
        return x
    @classmethod
    def check_input_adresse(x):
        while True:
            x = input('Wähle die Adresse aus: ')
            # Leerzeichen entfernen
            x = x.strip() 
            if x:
                break
            else:
                print("Darf nicht leer sein, bitte Eingabe!")
        return x
    @classmethod
    def check_input_telefon(x):
        while True:
            x = input('Wähle das Telefon aus: ')
            # Leerzeichen entfernen
            x = x.strip() 
            if x:
                break
            else:
                print("Darf nicht leer sein, bitte Eingabe!")
        return x
    @classmethod
    def check_input_e_mail(x):
        while True:
            x = input('Wähle die E-Mail aus: ')
            # Leerzeichen entfernen
            x = x.strip() 
            if x:
                break
            else:
                print("Darf nicht leer sein, bitte Eingabe!")
        return x
    # Methode from_input  
    @classmethod
    def from_input(cls):
        return cls(
            Inputdata.check_input_name(), 
            Inputdata.check_input_adresse(), 
            Inputdata.check_input_telefon(),
            Inputdata.check_input_e_mail()
        )

    # Magis methods
    def __str__(self):
            return self.strname
    def __repr__(self):
        return self.reprname


# ___________________________________________________________________________________________________________class_Inhaber
class Inhaber:
    """ 3. Klass Inhaber """
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


# ___________________________________________________________________________________________________________class_Konto
class Konto(Inhaber, Inputdata):
    """ 4. Klass Konto """
    _ids = count(0) # Klassen-Objects zähler
    # Konstruktor
    def __init__(self, name, adresse, telefon, e_mail):
        super().__init__(name, adresse, telefon, e_mail)
        self.id = next(self._ids)
        self.kontonummer = self.generate_kontonummer()
        self.kontostand = 0.0
        self.tages_limit_fuer_abzuege = 1000.0
        self.tages_abzuege = 0.0
        self.tagesumsatz = 0.0
        self.login = self.get_kontonummer()
        self.pin_code = "1234"
        self.timestamp = self.get_now()

        self.reprname = "Nummer: "+str(self.id)+"; Obj-id: "+str(id(self))
        self.strname = "strname: Klass Konto"

        self.das_konto_ist_da()

    # Magis methods
    def __str__(self):
        return self.strname
    def __repr__(self):
        return self.reprname
    # a static method to check a datetime.
    @staticmethod
    def get_now():
        return datetime.now()
    # a static method to check a typename.
    @staticmethod
    def typename(x):
        return type(x).__name__
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
        return print('Konto', self.kontonummer, 'für', self.name, 'nun geöffnet, ', 'Interne-ID: ', self.id, "\n\n", self.__dict__, "\n\n")


# _______________________________________________________________________________________________________________________Runtime
if __name__ == "__main__":
    # now call function we defined above 
    App_controller.clear()
    app_controller = App_controller()

    while True:
            app_controller.show_actions()
            choice = str(input("Ihre Eingabe: "))
            if choice == 'exit':
                break
            app_controller.check_action(choice)
