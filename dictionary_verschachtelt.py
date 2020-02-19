# input

language = ['D', 'F', 'E', 'd', 'f', 'e']

while True:
    a = input('Wähle das Herkunftsprache aus: In dem Du die Buchstabe D, F oder E: ')
    if a in language:
        break
    else:
        print("bitte nur D,F,E: ")

while True:
    z = input('Wähle das Zielsprache aus: In dem Du die Buchstabe D, F oder E: ')
    if z in language:
        break
    else:
        print("bitte nur D,F,E: ")

while True:
    wort = input('Bitte das Word eingeben: ')
    if wort.isdigit():
        print("bitte nur Wörter eingeben! ")
    else:
        break

a, z, wort = a.lower(), z.lower(),  wort.lower()

ed = {"red" : "rot", "green" : "grün", "blue" : "blau", "yellow":"gelb"}
df = {"rot" : "rouge", "grün" : "vert", "blau" : "bleu", "gelb":"jaune"}

temp = a+z

if temp == "ed":
    translate = ed[wort]
elif temp == "df":
    translate = df[wort]
elif temp == "ef":
    translate = df[ed[wort]]
elif temp == "de":
    translate = df[wort]


print('Das Herkunftsprache ist', a, 'Das Wort ist', " \" "+wort+" \" ", 'und das Zielsprache ist', z,".")
print("Die Übersetzung lautet: ", translate)

