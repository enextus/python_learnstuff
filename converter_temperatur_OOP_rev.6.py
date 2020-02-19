# Eduard; Temperaturkonverter.

# import count
from itertools import count

# class Input_data:
class Inputdata:
    def __init__(self, a, z, temperatur):
        self.ausgangstemperatursystem = self.lower_case(a)
        self.zieltemperatursystem = self.lower_case(z)
        self.temperatur = temperatur
    # Methode lower case
    def lower_case(self, x):
        return x.lower()
    # Methode upper case
    def upper_case(self, x):
        return x.upper()
    # Methode input_variable
    @classmethod
    def input_variable(x):
        temperaturzeichen = ['C', 'F', 'K', 'c', 'f', 'k']
        while True:
            x = input('Wähle das Temperatursystem aus. In dem Du die Buchstabe C, F oder K hier eingibst: ')
            if x in temperaturzeichen:
                break
            else:
                print("No.. the input was out of range! Bitte nur C,F,K: ")
        return x
    # Methode input_temperatur  
    @classmethod
    def input_temperatur(x, a):
        azc = -273.15
        azf = -459.67
        azk = 0.0
        while True:
            x = float(input("Bitte geben Sie die Temperatur ein, die Sie umrechnen möchten! (Float): "))
            try:
                if a in ['C', 'c'] and x > azc:
                    break
                elif a in ['F', 'f'] and x > azf:
                    break
                elif a in ['K', 'k'] and x > azk:
                    break
                print("No.. the input was out of range! Please repeat the input!")
            except ValueError:
                print("No.. the input string is not a number! Please repeat the input!")
                continue
        return x
    # Methode from_input  
    @classmethod
    def from_input(cls):
        a = Inputdata.input_variable()
        return cls(
            a, 
            Inputdata.input_variable(), 
            Inputdata.input_temperatur(a),
        )

# class Temperaturumwandlung
class Temperaturumwandlung(Inputdata):
    _ids = count(0)
    def __init__(self, a, z, temperatur):
        self.id = next(self._ids)
        super().__init__(a, z, temperatur)
        self.temp = {"fc":(5.0/9.0, -160.0/9.0),
                     "fk":(1.0/1.8, 459.67/1.8),
                     "cf":(1.8, 32.0),
                     "ck":(1.0, 273.15),
                     "kc":(1.0, -273.15),
                     "kf":(1.8, -459.67),
                     "cc":(1.0, 0),
                     "ff":(1.0, 0),
                     "kk":(1.0, 0),
                    }
        self.factor, self.offset = self.temp[self.ausgangstemperatursystem+self.zieltemperatursystem]
        self.ziel = 0
    # Methode get_instance_counter
    def get_instance_counter(self):
        return self.id
    # Methode rounden bis 3 Nachkomma-Stellen
    def rounden_drei(self, x):
        return round(x,3)
    # Methode Eine Formel für alle Berechnungen
    def convert_function(self, x, y, z):
        return x*y+z
    # Methode make_ziel()
    def make_ziel(self):
        self.ziel = self.convert_function(self.factor, self.temperatur, self.offset)
        return self.ziel
    # Methode get_ziel()
    def get_ziel(self):
        return self.ziel
    # Methode get_zieltemperatursystem()
    def get_zieltemperatursystem(self):
        return self.zieltemperatursystem
    # Methode get_ausgangstemperatursystem()
    def get_ausgangstemperatursystem(self):
        return self.ausgangstemperatursystem
    # Methode get_temperatur()
    def get_temperatur(self):
        return self.temperatur

# main programm
t = Temperaturumwandlung.from_input()
t.make_ziel()

# Ausgabe
print(f"Das Ausgangstemperatursystem ist {t.upper_case(t.get_ausgangstemperatursystem())}° und das Zieltemperatursystem ist {t.upper_case(t.get_zieltemperatursystem())}°.")
print(f"Das Ergebnis der Konvertierung ist {t.get_temperatur()}°{t.upper_case(t.get_ausgangstemperatursystem())} und entspricht {t.get_ziel()}°{t.upper_case(t.get_zieltemperatursystem())}")