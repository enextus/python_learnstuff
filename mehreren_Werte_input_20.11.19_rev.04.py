# Eduard

# Radiuse als verschiedenen Datentypen eingeben
# Die Fläche des Kreises wir berechnet

# import math
import math
from math import pi

# eingabe
radius = input('Radius bitte eingeben: ')

# convert
radius = list(radius.split(','))
radius = [x.strip(' ') for x in radius]

# Fläche funktion
def  flaeche_kreis(x):
    x = eval(x)
    return math.pi * x * x

# output
[print(f"Der Kreis mit Radius {i} cm hat eine Flaeche von {flaeche_kreis(i)} cm2.") for i in radius]
