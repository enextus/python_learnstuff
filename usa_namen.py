# Eduard
# USA Namen
# import module
import csv
import collections
import matplotlib.pyplot as plt
 
# spalten und titel organisiert bekommen:
fields=[]
rows=[]
 
# Id,Name,Year,Gender,State,Count

# csv-Dateiname
filename="names.csv"

# input
vorname = input('Gib bitte eine beliebigen Vornamen ein: ')
staat = input('Gib bitte ein US-Staat ein: ')

while True:
    try:
        the_beginning = int(input('Gib mir einen Jahr womit man die Suche beginnen soll: '))
        break
    except:
        print("Bitte geben Sie eine Zahl ein: ")

while True:
    try:
        the_end = int(input('Gib mir einen Jahr womit man die Suche enden soll: '))
        break
    except:
        print("Bitte geben Sie eine Zahl ein: ")

# lstx lsty
lstx = []
lsty = []

# die csv-datei auslesen:
with open(filename, 'r') as csvdatei:
    # csv-reader-objekt
    csvreader = csv.reader(csvdatei)
    # kopfzeile auslesen (fields)
    fields=next(csvreader) #.next() eine built-in Methode für alle iterierbaren Objekte

    print('fields = ', fields)
     
    # Daten Zeile für Zeile auslesen:
    for row in csvreader:
        rows.append(row)
    # die Anzahl der Zeilen:
    print('Die Gesamtanzahl der Zeilen: %d'%(csvreader.line_num))

    print("\nDas Ergennis: \n")

    for field in fields:
        print("%10s"%field, end=' ')
    print('\n')
    for row in rows:
        if (row[1] == vorname) and (row[4] == staat) and (the_beginning <= int(row[2]) <= the_end):
            lstx.append(row[2])
            lsty.append(row[5])

            for col in row:
                print("%10s"%col, end=' ')
            print('\n')

# ausgeben von Links nach Rechts ...
print('___________________________________________')
plt.plot (lstx, lsty, 'ro')
plt.show()
