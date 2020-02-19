# Eduard
# USA Namen
# import module
import csv
import collections
import matplotlib.pyplot as plt

# sex table
sex_tabelle = ['M', 'F', 'm', 'f']

# spalten und titel organisiert bekommen:
fields=[]
rows=[]
 
# Id,Name,Year,Gender,State,Count

# csv-Dateiname
filename="names.csv"

# input
while True:
    sex = input('Wähle das Geschlecht aus. In dem Du die Buchstabe M, F: ')
    if sex in sex_tabelle:
        break
    else:
        print("bitte nur M, F: ")

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
        if row[1] == vorname and row[3] == sex and row[4] == staat and the_beginning <= int(row[2]) <= the_end:
            lstx.append(row[2])
            lsty.append(int(row[5])) # int() for autosort

            for col in row:
                print("%10s"%col, end=' ')
            print('\n')

# ausgeben von Links nach Rechts ...
print('___________________________________________')

# format constants
SMALL_SIZE = 7
MEDIUM_SIZE = 10
BIGGER_SIZE = 12
FORM_AND_COLOR = 'ro'
ROTATION = 90

# format functions
def format_function(a, b, c,d, e):
 plt.rc('font', size=a)          # controls default text sizes
 plt.rc('axes', titlesize=a)     # fontsize of the axes title
 plt.rc('axes', labelsize=b)    # fontsize of the x and y labels
 plt.rc('xtick', labelsize=a)    # fontsize of the tick labels
 plt.rc('ytick', labelsize=a)    # fontsize of the tick labels
 plt.rc('legend', fontsize=a)    # legend fontsize
 plt.rc('figure', titlesize=c)  # fontsize of the figure title
 plt.plot (lstx, lsty, d)
 plt.xticks(rotation=e)

# format output
format_function(SMALL_SIZE, MEDIUM_SIZE, BIGGER_SIZE,FORM_AND_COLOR, ROTATION)

# output
plt.show()
