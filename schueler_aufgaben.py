# import
from random import randint

#  input
while True:
    eingabe = input('Bitte die Anzahl der Aufgaben eingeben: ')
    if eingabe.isdigit():
        anzahl_der_aufgaben = int(eingabe)
        break
    else:
        print("bitte nur Zahlen eingeben! ")

print("Anzahl der Aufgaben: ", anzahl_der_aufgaben)

moeglichen_aufgaben = {0:"+", 1:"-", 2:"*", 3:"/"}

aufgabe_fuer_loesung = {}
die_aufgabe = {}

for elem in range(anzahl_der_aufgaben):
    art_der_aufgabe = (randint(1, 4))
    aufgabe_fuer_loesung[elem] = art_der_aufgabe

for elem in aufgabe_fuer_loesung:
    erste_zahl = randint(0, 9)
    zweite_zahl = randint(0, 9)
    math_operator = moeglichen_aufgaben[elem]

    die_aufgabe[elem] = erste_zahl, math_operator, zweite_zahl

ergebnisse = {}
rictiger_ergebnisse = {}

for elem in die_aufgabe:
    print("Lösen Sie die Aufgabe: ", die_aufgabe[elem][0],  die_aufgabe[elem][1], die_aufgabe[elem][2])

    v = str(die_aufgabe[elem][0]) +  die_aufgabe[elem][1] + str(die_aufgabe[elem][2])

    eingabe_2 = input('Bitte das Ergebniss eingeben: ' )
    ergebnis = int(eingabe_2)

    rictiger_ergebnisse[elem] = eval(v)
    ergebnisse[elem] = eingabe_2

print("Ergebnisse: ", ergebnisse[0],  ergebnisse[1])

print("Richtigen Ergebnisse:", end= " ")

for i in rictiger_ergebnisse:
    print(rictiger_ergebnisse[i], end= " ")

# stop

