# import csv module
import csv
 
# spalten und titel organisiert bekommen:
fields=[]
rows=[]
 
# csv-Dateiname
filename="aapl.csv"
 
# die csv-datei auslesen:
with open(filename, 'r') as csvdatei:
    # csv-reader-objekt
    csvreader = csv.reader(csvdatei)
    # kopfzeile auslesen (fields)
    fields=next(csvreader) #.next() eine built-in Methode für alle iterierbaren Objekte
     
    # Daten Zeile für Zeile auslesen:
    for row in csvreader:
    # die Anzahl der Zeilen:
        print('Die Gesamtanzahl der Zeilen: %d'%(csvreader.line_num))
 
    print("\nDie ersten 5 Zeilen: \n")
    for field in fields:
        print("%10s"%field, end=' ')
    print('\n')
    for row in rows[:5]:
        for col in row:
            print("%10s"%col, end=' ')
        print('\n')