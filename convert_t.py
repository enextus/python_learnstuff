# input

temperaturzeichen = ['C', 'F', 'K', 'c', 'f', 'k']

while True:
    a = input('Wähle das Ausgangstemperatursystem aus. In dem Du die Buchstabe C, F oder K hier eingibst: ')
    if a in temperaturzeichen:
        break
    else:
        print("bitte nur C,F,K: ")

while True:
    z = input('Wähle das Zieltemperatursystem aus. In dem Du die Buchstabe C, F oder K hier eingibst: ')
    if z in temperaturzeichen:
        break
    else:
        print("bitte nur C,F,K: ")

while True:
    t = input ("Gebe das Temperatur ein. (Float): ")
    try:
        val = float(t)
        break
    except ValueError:
        print("No.. the input string is not a number. It's a string")

print('Das Ausgangstemperatursystem ist', "°"+a, 'und das Zieltemperatursystem ist',"°"+z,".")

temp = {"fc":(5.0/9.0, -160.0/9.0),
            "fk":(1.0/1.8, 459.67/1.8),
            "cf":(1.8, 32.0),
            "ck":(1.0, 273.15),
            "kc":(1.0, -273.15),
            "kf":(1.8, -459.67),
            "cc":(1.0, 0),
            "ff":(1.0, 0),
            "kk":(1.0, 0)}

a, z = a.lower(), z.lower()

# Tupel entpacken:
factor, offset = temp[a+z]

# Eine Formel für alle Berechnungen
ziel = factor*val + offset

# round() rundet! 
ziel = round(ziel,3)

print("Das Ergebnis der Konvertierung ist", val, "°"+a.upper()," entspricht ", ziel, "°"+z.upper())
print(" ")
