# input

language = ['D', 'F', 'E', 'd', 'f', 'e']

while True:
    a = input('Wähle das Herkunftsprache aus: In dem Du die Buchstabe D, F, E: ')
    if a in language:
        break
    else:
        print("bitte nur D,F,E,I: ")

while True:
    z = input('Wähle das Zielsprache aus: In dem Du die Buchstabe D, F, E: ')
    if z in language:
        break
    else:
        print("bitte nur D,F,E: ")

while True:
    print(f"test")
    wort = input('Bitte das Word eingeben: ')
    if wort.isdigit():
        print("bitte nur Wörter eingeben! ")
    else:
        break


a, z, wort = a.lower(), z.lower(),  wort.lower()

e_d = {"red" : "rot", "green" : "grün", "blue" : "blau", "yellow":"gelb"}
d_f = {"rot" : "rouge", "grün" : "vert", "blau" : "bleu", "gelb":"jaune"}

temp = a + '_' + z

if temp == "e_d":
    translate = e_d[wort]
elif temp == "d_f":
    translate = d_f[wort]
elif temp == "e_f":
    translate = d_f[e_d[wort]]
elif temp == "d_e":
    translate = d_f[wort]


print('Das Herkunftsprache ist', a, 'Das Wort ist', " \" "+wort+" \" ", 'und das Zielsprache ist', z,".")
print("Die Übersetzung lautet: ", translate)
