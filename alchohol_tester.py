# Eduard


sex_tabelle = ['M', 'F', 'm', 'f']
while True:
    v = input ("Gebe die Menge des Getränke-Volumens. (Float): ")
    try:
        v = float(v)
        break
    except ValueError:
        print("No.. the input string is not a number. It's a string")

while True:
    e = input ("Gebe die Alkoholvolumenanteil in % - z.B. Bier 4%. (Float): ")
    try:
        e = float(e)
        break
    except ValueError:
        print("No.. the input string is not a number. It's a string")

while True:
    p = input ("Gebe die Dichte in g/ml. (Float): ")
    try:
        p = float(p)
        break
    except ValueError:
        print("No.. the input string is not a number. It's a string")

while True:
    sex = input('Wähle das Geschlecht aus. In dem Du die Buchstabe M, F: ')
    if sex in sex_tabelle:
        break
    else:
        print("bitte nur M, F: ")

while True:
    m = input ("Gebe das Gewicht ein. (Float): ")
    try:
        m = float(m)
        break
    except ValueError:
        print("No.. the input string is not a number. It's a string")

if sex == 'M':
    r = 0.7
else:
    r = 0.6

# c = v * e * p

c = ( v * e * (p * 1000)  ) / (m*r)
print( "Blutalkoholspiegel: ", c )