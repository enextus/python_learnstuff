# eine Klasse bauen, bzw. definieren:
class Fahrzeug:
 # Eigenschaften
 geschwindigkeit = 0
 # Methoden
 # def speed(auto, wert):
 #  auto.geschwindigkeit += wert
 # def ausgabe(auto):
 #  print('Geschwindigkeit aktuell: ', auto.geschwindigkeit)
 def speed(self, wert):
  self.geschwindigkeit += wert
 def ausgabe(self):
  print('Geschwindigkeit aktuell: ', self.geschwindigkeit)

# objekte der Klasse Fahrzeug instanzieren:
opel = Fahrzeug()
opel2 = opel
vw = Fahrzeug()

print(opel)
print(opel2)
print(vw)

# objectmethoden:
opel.ausgabe()
opel.speed(20)
opel.ausgabe()