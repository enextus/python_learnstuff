# Eduard HR-System

# import der Modulen
from mitarbeiter import Mitarbeiter
from sozialversicherungsbeitraege import Sozialversicherungsbeitraege
from einkommenssteuer import Einkommenssteuer
from gehaltsrechner import Gehaltsrechner
# from hr import Hr

# Einlesen der Daten
# import csv module
import csv

# spalten und titel organisiert bekommen:
fields=[]
rows=[]

# csv-Dateiname
filename="mitarbeiter_01.csv"

# Das Mitarbeiter-Objects-Array
Mitarbeitern = []

# die csv-datei auslesen:
with open(filename, 'r') as csvdatei:
    # csv-reader-objekt
    csvreader = csv.reader(csvdatei)
    # kopfzeile auslesen (fields)
    fields=next(csvreader) #.next() eine built-in Methode für alle iterierbaren Objekte
     
    # Daten Zeile für Zeile auslesen:
    for row in csvreader:
     # print('Die Mitarbeiternummer: %d'%(csvreader.line_num-1))
     Mitarbeitern.append(Mitarbeiter(row[0], row[1], row[2], row[3], row[4], row[5]))

# die Objekte mit Mitarbeiter-Daten sind in der Liste
print('Mitarbeitern = ', Mitarbeitern)
print('________________________________________________________________________________')
# Der Zugang zum Daten in der Objecten
for m in Mitarbeitern:
  # Sozialversicherungsbeitraege werden für jeden Mitarbeiter-Objekt berechnet
  svn = Sozialversicherungsbeitraege(m.name, m.personal_id, m.steuerklasse, m.familienstand, m.anzahl_der_kinder, m.gehalt)
  # Sozialversicherungsbeitraege werden für jeden Mitarbeiter-Objekt hinzugefühgt
  m.sozialversicherungsbeitraege=svn.get_sozialversicherungsbeitraege()
  m.sozialversicherungsbeitraege_berechnet=svn.get_sozialversicherungsbeitraege_berechnet()
  e = Einkommenssteuer(m.name, m.personal_id, m.steuerklasse, m.familienstand, m.anzahl_der_kinder, m.gehalt)
  m.freibetrag = e.get_freibetrag()
  m.all_einkommenssteuer=e.get_all_einkommenssteuer()
  m.all_einkommenssteuer_berechnet=e.get_all_einkommenssteuer_berechnet()
  g = Gehaltsrechner(m.familienstand, m.anzahl_der_kinder, m.gehalt, m.freibetrag, m.netto_monatsgehalt, m.sozialversicherungsbeitraege_berechnet, m.all_einkommenssteuer_berechnet)
  m.netto_monatsgehalt = g.get_netto_monatsgehalt()
  print('Mitarbeitern  = ',m.__dict__['name'], ": ", m.__dict__)
  print()
# stop