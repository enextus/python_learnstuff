# imports
import random
from itertools import count
from datetime import datetime
from os import system, name
import time

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
    @classmethod
    def check_input_name(x):
        """ # Methode check_input """
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
            x = x.strip() 
            if x:
                break
            else:
                print("Darf nicht leer sein, bitte Eingabe!")
        return x
    @classmethod
    def from_input(cls):
        """ Methode from_input """
        return cls(
            Inputdata.check_input_name(), 
            Inputdata.check_input_adresse(), 
            Inputdata.check_input_telefon(),
            Inputdata.check_input_e_mail()
        )

    def __str__(self):
        """ Magis method __str__ """
        return self.strname
    def __repr__(self):
        """ Magis method __repr__ """
        return self.reprname
    def __del__(self):
        """ Magis method __del__ """
        print("Destruktor für Inputdata gestartet.")


# ___________________________________________________________________________________________________________App_controller
class App_controller:
    """ 1. class App_controller """
    login = None
    login_kontonummer = None
    @staticmethod
    def get_login():
        return App_controller.login 
    @staticmethod
    def clear():
        """ define our clear function Windows & mac"""
        # for windows 
        if name == 'nt': 
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else: 
            _ = system('clear')
        return 
    @staticmethod
    def show_actions():
        """ define our show_actions """
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
    @staticmethod
    def show_actions_after_login():
        """ define our show_actions """
        messages = ['                                                                  ',
                    '_____Girokontosystem::Kundenlogin______________________________________________',
                    '',
                    'Wählen Sie die gewünschte Aktion aus, \nindem Sie eine Nummer aus der Liste eingeben: ',
                    '',
                    ' 1 - Kontostand',                   
                    ' 2 - Einzahlen',
                    ' 3 - Auszahlen',
                    ' 4 - Überweisen',
                    ' 5 - Ausloggen',
                    '__________________________________________________________________',
                    "Zum Verlassen des Menüs  Sie Folgendes ein: 'exit'",
                    '__________________________________________________________________']
        for i in messages:
            print(i)
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
            self.obj1 = None
            self.obj2 = None

    def __str__(self):
        """ Magis method __str__ """
        return self.strname
    def __repr__(self):
        """ Magis method __repr__ """
        return self.reprname
    def __del__(self):
        """ Magis method __del__ """
        print("Destruktor für App_controller gestartet.")
    
    def check_action(self, x):
        """ Methode check_action """
        if self.login:
            if x == '1':
                # 1 - Kontostand
                k = self.get_konten_liste()
                for i in k:
                    if str(self.login_kontonummer) == str(i.get_kontonummer()):
                        part1 = "Der Kontostand von dem Konto " + str(i.get_kontonummer()) + " ist "
                        part2 = str(i.get_kontostand()) + " Eur."
                        App_controller.clear()
                        self.print_something(part1, part2)
            elif x == '2':
                # 2 - Einzahlen
                k = self.get_konten_liste()
                for i in k:
                    if str(self.login_kontonummer) == str(i.get_kontonummer()):
                        q = input("Wieviel Geld möchten Sie einzahlen? ")
                        i.make_einzahlung(q)
                        part1 = "Der Kontostand von dem Konto " + str(i.get_kontonummer()) + " ist "
                        part2 = str(i.get_kontostand()) + " Eur."
                        App_controller.clear()
                        self.print_something(part1, part2)
                self.make_clear_with_sleep()
            elif x == '3':
                # 3 - Auszahlen     
                k = self.get_konten_liste()
                for i in k:
                    if str(self.login_kontonummer) == str(i.get_kontonummer()):
                        q = input("Wieviel Geld möchten Sie auszahlen? ")
                        i.make_auszahlung(q)
                        part1 = "Der Kontostand von dem Konto " + str(i.get_kontonummer()) + " ist "
                        part2 = str(i.get_kontostand()) + " Eur."
                        App_controller.clear()
                        self.print_something(part1, part2)
                self.make_clear_with_sleep()
            elif x == '4':
                # 4 - Überweisen
                k = self.get_konten_liste()
                
                print('Für eine Überweisung vorhandene Konten: ')
                for i in k:
                    if str(self.login_kontonummer) != str(i.get_kontonummer()):
                        print(i.get_kontonummer())

                if True:
                    q = input("Wieviel Geld möchten Sie überweisen? ")
                    kn = input("Wie lautet das Ziel-Kontonummer? ")

                    for w in k:
                        if str(w.get_kontonummer()) == str(kn):
                            self.obj2 = w # Ziel-Object
                        elif str(w.get_kontonummer()) == str(App_controller.login_kontonummer):
                            self.obj1 = w # Ausgangs-Object

                    self.obj1.make_transfer(self.obj2, q)
                        
                part1 = "Der Kontostand von dem Konto " + str(self.obj1.get_kontonummer()) + " ist "
                part2 = str(self.obj1.get_kontostand()) + " Eur."
                self.make_clear_with_sleep()
                self.print_something(part1, part2)
            elif x == '5':
                # 5 - Ausloggen
                self.make_clear_with_sleep()
                App_controller.login_kontonummer = None
                App_controller.login = False
                part1 = "Sie sind nun Ausgelogt!\n"
                part2 = ""
                self.print_something(part1, part2)
            else:
                print('Bitte wiederholen Sie die Eingabe!')
                self.make_clear_with_sleep()
        else: 
            if x == '1':
                self.make_clear_with_sleep()
                self.create_konto()
            elif x == '2':
                self.make_clear_with_sleep()
                self.einlogen()
            elif x == '3':
                self.make_clear_with_sleep()
                x = "Anzahl der Konten: "
                self.print_something(x, self.get_anzahl_der_konten())
            elif x == '4':
                self.make_clear_with_sleep()
                x = "Die Konten als Objekte sehen so aus:\n"
                self.print_something(x, self.get_konten_liste())
            elif x == '5':
                self.make_clear_with_sleep()
                x = "Die Konten als Objekte sehen so aus:\n"
                self.print_something(x, self.get_konten_liste())
            else:
                print('Bitte wiederholen Sie die Eingabe!')
                self.make_clear_with_sleep()

    def make_clear(self):
        """ Methode clear disprlay: """
        return App_controller.clear() 
    def make_clear_with_sleep(self, x=1):
        """ Methode clear disprlay with sleep time """
        time.sleep(x)
        return App_controller.clear()
    def get_start_message(self):
        """ Methode get_start_message """
        return self.start_message
    def create_konto(self):
        """ create_konto """
        obj = Konto.from_input()
        self.accounts.append(obj)
        return obj
    def get_anzahl_der_konten(self):
        """ check Anzahl der Konten """
        return len(self.accounts)
    def get_konten_liste(self):
        """ schow Konten-Objects """
        return self.accounts
    def print_something(self, x='', y=''):
        """ print wrapper """
        return print(f'{x}{y}')
    def einlogen(self):
        """ einloggen """
        self.print_something('Bitte loggen Sie sich ein.')
        x = str(input('Login: '))
        y = str(input('Password: '))
        if x in [str(i.get_kontonummer()) for i in self.accounts]:
            if y in [str(j.get_pin_code()) for j in self.accounts]:
                App_controller.login = True
                App_controller.login_kontonummer = x
        return App_controller.login, App_controller.login_kontonummer

# ___________________________________________________________________________________________________________class_Inhaber
class Inhaber:
    """ 3. Klass Inhaber """
    def __init__(self, name, adresse, telefon, e_mail):
        self.name = name
        self.adresse = adresse
        self.telefon = telefon
        self.e_mail = e_mail
        self.reprname = "reprname: Klass Inhaber"
        self.strname = "strname: Klass Inhaber"

    def __str__(self):
        """ Magis method __str__ """
        return self.strname
    def __repr__(self):
        """ Magis method __repr__ """
        return self.reprname
    def __del__(self):
        """ Magis method __del__ """
        print("Destruktor für App_controller gestartet.")

# ___________________________________________________________________________________________________________class_Konto
class Konto(Inhaber, Inputdata, App_controller):
    """ 4. Klass Konto """
    _ids = count(0) # Klassen-Objects zähler

    def __init__(self, name, adresse, telefon, e_mail):
        super().__init__(name, adresse, telefon, e_mail)
        self.id = next(self._ids)
        self.kontonummer = self.generate_kontonummer()
        self.kontostand = 0.0
        self.tages_limit_fuer_abzuege = 1000.0
        self.tages_abzuege = 0.0
        self.tagesumsatz = 0.0
        self.login = self.get_kontonummer()
        self.pin_code = "123"
        self.timestamp = self.get_now()
        self.reprname = "Nummer: "+str(self.id)+"; Obj-id: "+str(id(self))+"; Kontonummer: "+str(self.get_kontonummer())+";"
        self.strname = "strname: Klass Konto"
        self.das_konto_ist_da()

    def __str__(self):
        """ Magis method __str__ """
        return self.strname
    def __repr__(self):
        """ Magis method __repr__ """
        return self.reprname
    def __del__(self):
        """ Magis method __del__ """
        print("Destruktor für App_controller gestartet.")

    @staticmethod
    def get_now():
        """ a static method to check a datetime. """
        return datetime.now()
    @staticmethod
    def typename(x):
        """ a static method to check a typename. """
        return type(x).__name__
    def get_instance_counter(self):
        """ Methode get_instance_counter"""
        return self.id
    def prozent_berechnen(self, x, y):
        """ Methode zum Berechnen von Prozenten """
        x = float(x)
        y = float(y)
        return round((x * y / 100.0), 2)
    def generate_kontonummer(self):
        """ Methode generate_kontonummer """
        return random.randint(100000, 999999)
    def get_kontonummer(self):
        """ Methode get_kontonummer """
        return self.kontonummer
    def get_pin_code(self):
        """ Methode pin_code """
        return self.pin_code

    # def ueberweisen(self, ziel, betrag):
    #         if(self.__Kontostand - betrag < -self.__Kontokorrent):
    #         # Deckung nicht genuegend
    #         return False  
    #     else: 
    #         self.__Kontostand -= betrag 
    #         ziel.__Kontostand += betrag 
    #         return True

    def make_transfer(self, other, transfer_summe):
        """ Methode Transfer """
        transfer_summe = float(transfer_summe)
        # print('Ausgangs-Object. self: ', self.__dict__)
        # print(f'\n')
        # print('Destination-Object. other: ', other.__dict__)
        # print(f'\n')
        if transfer_summe <= self.kontostand and (self.get_tages_abzuege() + transfer_summe) <= self.get_tages_limit_fuer_abzuege():
            self.kontostand -= transfer_summe
            self.tages_abzuege += transfer_summe
            other.kontostand += transfer_summe
            other.tagesumsatz += transfer_summe
        else:
            return False
    def make_einzahlung(self, einzahlung):
        """ Methode Einzahlung """
        einzahlung = float(einzahlung)
        if einzahlung >= 0:
            self.kontostand += einzahlung
            self.tagesumsatz += einzahlung
        else:
            return False
    def make_auszahlung(self, auszahlung):
        """ Methode Auszahlung """
        auszahlung = float(auszahlung)
        if (auszahlung <= self.kontostand) and ((self.get_tages_abzuege() + auszahlung) <= self.get_tages_limit_fuer_abzuege()):
            self.kontostand -= auszahlung
            self.tagesumsatz += auszahlung
            self.tages_abzuege += auszahlung
        else:
            return False
    def get_kontostand(self):
        """ Methode Kontostand prüffen """
        return self.kontostand
    def get_tagesumsatz(self):
        """ Methode Tagesumsatz prüffen """
        return self.tagesumsatz   
    def get_tages_abzuege(self):
        """ Methode tages_abziehen prüffen """
        return self.tages_abzuege
    def get_tages_limit_fuer_abzuege(self):
        """ Methode tages_abziehen prüffen """
        return self.tages_limit_fuer_abzuege
    def get_id(self):
        """ Methode get_id prüffen """
        return self.id
    def das_konto_ist_da(self):
        """ Methode das_konto_ist_da """
        return print('Konto', self.kontonummer, 'für', self.name, 'nun geöffnet, ', 'Interne-ID: ', self.id, "\n\n")


# _______________________________________________________________________________________________________________________Runtime
if __name__ == "__main__":
    App_controller.clear()
    app_controller = App_controller()

    while True:
        if App_controller.get_login():
            app_controller.show_actions_after_login()
        else: 
            app_controller.show_actions()
        choice = str(input("Ihre Eingabe: "))
        if choice == 'exit':
            break
        app_controller.check_action(choice)
