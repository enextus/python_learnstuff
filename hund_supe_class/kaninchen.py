from hund import Dog

# class Kaninchen
class Kaninchen(Dog):
 def __init__(self, name, age=0, spitzname='Keine', kg=0):
  Dog.__init__(self, name, age, spitzname='')
  self.koerper_gewicht=kg

 def koerper_gewicht_erhoehen(self, wert):
  self.koerper_gewicht += wert
 def alter_erhoehen(self, wert):
  self.age += wert

# Test
if __name__ == "__main__":
 kaninchen = Kaninchen('Artus')
 print('kaninchen = ', kaninchen)
 print(kaninchen.name)
 print(kaninchen.age)
 print(kaninchen.spitzname)
 print(kaninchen.koerper_gewicht)

 # erhöhen der körpergewicht
 kaninchen.alter_erhoehen(2)
 kaninchen.koerper_gewicht_erhoehen(15)
 kaninchen.set_spitzname("Buddy")

 print(kaninchen.koerper_gewicht)

 # erhöhen der körpergewicht
 kaninchen.alter_erhoehen(1)
 kaninchen.koerper_gewicht_erhoehen(14)

 print('kaninchen = ', kaninchen)
 print(kaninchen.name)
 print(kaninchen.spitzname)
 print(kaninchen.age)
 print(kaninchen.koerper_gewicht)